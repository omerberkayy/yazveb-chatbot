🤖 YAZVEB Chatbot

LangChain + Gemini API + Gradio tabanlı RAG (Retrieval-Augmented Generation) sohbet botu

Bu proje, Yapay Zeka ve Veri Bilimi Topluluğu hakkında bilgi içeren metin dosyalarını işleyip, kullanıcı sorularına bağlama dayalı akıllı yanıtlar üretir.

⸻

🎯 Projenin Amacı

Bu proje, topluluk üyelerinin topluluk hakkında daha kolay bilgi edinmelerini sağlamak amacıyla geliştirilmiştir.
Topluluk başkanı olarak tarafımdan yürütülmüş olup, kullanıcıların geçmiş etkinlikler, genel bilgiler ve iletişim detaylarına hızlı şekilde ulaşabilmeleri hedeflenmiştir.

⸻

📊 Veri Seti Hakkında

Veri seti, topluluğun Google Drive dizininde yer alan kaynaklardan oluşturulmuştur:
	•	hakkında.txt → Topluluk hakkında genel bilgiler
	•	eski_etkinlikler.txt → Geçmiş etkinlik kayıtları
	•	iletişim.txt → Topluluk iletişim bilgileri

Bu dosyalar birleştirilerek, topluluk verilerini temsil eden bütüncül bir veri seti elde edilmiştir.

⸻

🚀 Proje Özeti

Chatbot, LangChain ve Google Gemini (Generative AI) modellerini kullanarak önceden hazırlanmış topluluk metinlerinden anlamlı, bağlama uygun cevaplar üretir.
Kullanıcı girdileri, vektör tabanlı benzerlik (semantic search) yöntemiyle analiz edilerek en ilgili dokümanlarla eşleştirilir.

🔧 Kullanılan Teknolojiler
	•	🧠 LangChain – RAG pipeline yönetimi
	•	🔍 ChromaDB – Vektör veritabanı
	•	🗣️ Google Gemini API – Yanıt üretimi
	•	💬 Gradio – Kullanıcı arayüzü
	•	💾 Hugging Face Embeddings (multilingual-e5-base) – Metin gömme modeli

⸻

🧠 Elde Edilen Sonuçlar

Oluşturulan veri seti, ChromaDB içerisine gömülmüş ve RAG (Retrieval-Augmented Generation) yaklaşımıyla sorgulanabilir hale getirilmiştir.

Kullanıcı bir soru sorduğunda:
	1.	Girdiye en yakın 3 bağlamsal sonuç ChromaDB’den alınır.
	2.	Bu sonuçlar Gemini modeli ile birleştirilerek anlamlı ve bilgilendirici bir yanıt oluşturulur.

Bu sayede kullanıcılar, toplulukla ilgili sorularına doğrudan, doğru ve bağlama uygun yanıtlar alabilir.

⸻

🧩 Gereksinimler

Aşağıdaki kütüphaneler gereklidir:

langchain
langchain-community
langchain-chroma
langchain-text-splitters
langchain-huggingface
langchain-google-genai
gradio

🧱 Tek komutla yükleme:

pip install -U langchain langchain-community langchain-chroma langchain-text-splitters langchain-huggingface langchain-google-genai gradio


⸻

⚙️ Kurulum Adımları

1️⃣ Reponu Klonla

git clone https://github.com/omerberkayy/yazveb-chatbot.git
cd yazveb-chatbot

2️⃣ Gerekli Bağımlılıkları Yükle

pip install -r requirements.txt

3️⃣ Veri Klasörünü Kontrol Et

Metin dosyalarının data/raw/ dizininde olduğundan emin ol:

data/
 ├── raw/
 │   ├── topluluk_bilgileri.txt
 │   ├── etkinlikler.txt
 │   └── iletişim.txt

💡 data/processed/chroma_db/ klasörü .gitignore içinde olmalıdır (embedding verileri commit edilmemelidir).

⸻

🔐 API Anahtarı Ekleme

Proje, Google Gemini API kullanır.
API anahtarını Google AI Studio üzerinden alabilirsin.

.env dosyasına ekle:

GOOGLE_API_KEY=AIzaSy...


⸻

💻 Uygulamayı Çalıştırma

🔸 Yerel Ortamda

python app.py

Terminalde aşağıdaki bağlantıyı göreceksin:

Running on local URL: http://127.0.0.1:7860/

Tarayıcıda aç → http://127.0.0.1:7860

⸻

🌐 Deploy Linki

https://huggingface.co/spaces/omeberkaycoskun/yazveb
