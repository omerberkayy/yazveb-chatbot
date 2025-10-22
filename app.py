import os
from dotenv import load_dotenv
import gradio as gr

#langChain bileşenleri
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate

#.env'den ortam değişkenlerini yükle
load_dotenv()

#model ve embeddin seçimi yapılıp, ayarları eklendi

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

embeddings = HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-base")


DATA_PATH = "data/raw"
CHROMA_PATH = "data/processed/chroma_db"

#chroma db başlatıldı
vector_store = Chroma(
    collection_name="community_knowledge",
    embedding_function=embeddings,
    persist_directory=CHROMA_PATH,
)

#eğer chroma boşsa veriyi yükle, parçalara (chunk) ayır ve chroma'ya ekle
def initialize_database():
    if len(vector_store.get()["ids"]) == 0:
        print("⚙️  Veritabanı boş, embedding işlemi başlatılıyor...")

        docs = []
        for filename in os.listdir(DATA_PATH):
            if filename.endswith(".txt"): #dosya uzantısı .txt olmayan dosyaları atla
                with open(os.path.join(DATA_PATH, filename), "r", encoding="utf-8") as f:
                    text = f.read().strip()
                    docs.append({"content": text, "source": filename})
        #chunk_size ve chunk_over ayarı veri setine göre ayarlandı
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=100,
            separators=["\n## ", "\n# ", "\n", " "] #veri setinde başlıklar markdown ile ayrıldı
        )

        chunks = []
        for doc in docs:
            splits = text_splitter.split_text(doc["content"])
            for chunk in splits:
                chunks.append({
                    "text": chunk,
                    "source": doc["source"]
                })
        #parça listesi langchain formatına dönüştürüldü
        all_splits = [
            Document(page_content=chunk["text"], metadata={"source": chunk["source"]})
            for chunk in chunks
        ]
        #huggingface modeli kullanılarak, veriler vektöre dönüştürüldü ve chroma db'ye eklendi
        vector_store.add_documents(all_splits)
        vector_store.persist()
        print(f"✅ {len(all_splits)} belge eklendi ve Chroma kaydedildi.")
    else:
        print("✅ Mevcut Chroma DB yüklendi.")


#veri setine uygun gelişmiş bir prompt eklendi
prompt_template = ChatPromptTemplate.from_template("""
Sen, bir öğrenci topluluğu asistanısın. Görevin, topluluk hakkında sorulan sorulara
önceden kaydedilmiş bilgilerden yararlanarak net, samimi ve doğru yanıtlar vermektir.

Aşağıda topluluk hakkında bilgiler, geçmiş etkinlikler ve iletişim detayları yer almaktadır.
Kullanıcı bir soru sorduğunda:
- Sorunun hangi kategoriye ait olduğunu (etkinlik, genel bilgi, iletişim vb.) anlamaya çalış.
- Bağlama en uygun yanıtı kısa, doğal ve açıklayıcı bir şekilde oluştur.
- Eğer bilgi mevcut değilse, “Bu konuda elimde bilgi bulunmuyor.” gibi kibar bir yanıt ver.

Topluluk Bilgileri ve Etkinlik Kayıtları:
{context}

Kullanıcı Sorusu: {question}

Asistan Yanıtı:
""")

#kullanıcının sorusuna göre en alakalı 3 sonuç chroma db'den getirilip, llm'in cevap üretmesi sağlandı
def chatbot_interface(user_query):
    if not user_query.strip():
        return "Lütfen bir soru giriniz."

    retrieved_docs = vector_store.similarity_search(user_query, k=3)
    context_text = "\n\n".join([doc.page_content for doc in retrieved_docs])

    prompt = prompt_template.format(context=context_text, question=user_query)
    response = llm.invoke(prompt)
    return response.content


#chatbota arayüz eklemek için python'ın gradio kütüphanesi kullanıldı
def launch_app():
    initialize_database()

    with gr.Blocks() as demo:
        gr.Markdown("## 🤖 Topluluk Chatbot (RAG + Gemini)")
        gr.Markdown("Topluluk hakkında sorularınızı aşağıya yazabilirsiniz 👇")

        user_input = gr.Textbox(label="Sorunuzu yazın:", placeholder="Örnek: Topluluğa nasıl katılabilirim?")
        output = gr.Textbox(label="Asistan Yanıtı", lines=6)
        submit_btn = gr.Button("Gönder")

        submit_btn.click(fn=chatbot_interface, inputs=user_input, outputs=output)

    demo.launch(server_name="0.0.0.0", server_port=7860)


if __name__ == "__main__":
    launch_app()

