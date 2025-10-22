🤖 YAZVEB Chatbot

LangChain + Gemini API + Gradio tabanlı RAG (Retrieval-Augmented Generation) sohbet botu
Bu proje, yapay zeka ve veri bilimi öğrenci topluluğu hakkında bilgi içeren metin dosyalarını işleyip, kullanıcı sorularına bağlama dayalı akıllı yanıtlar verir.

⸻

🎯 Projenin Amacı

Bu proje, Yapay Zeka ve Veri Bilimi Topluluğu üyelerinin topluluk hakkında daha kolay bilgi edinmelerini sağlamak amacıyla geliştirilmiştir.
Proje, topluluk başkanı olarak tarafımdan yürütülmüş olup, kullanıcıların geçmiş etkinlikler, genel bilgiler ve iletişim detaylarına hızlı şekilde ulaşabilmelerini hedeflemektedir.

⸻

📊 Veri Seti Hakkında

Veri seti, topluluğun Google Drive dizininde bulunan kaynaklar kullanılarak hazırlanmıştır.
Aşağıdaki dosyalar kullanılarak veri seti oluşturulmuştur:
	•	hakkında.txt → Topluluk hakkında genel bilgiler
	•	eski_etkinlikler.txt → Topluluğun geçmiş etkinliklerine ait kayıtlar
	•	iletişim.txt → Topluluk iletişim bilgileri

Bu dosyalar birleştirilerek, topluluk verilerini temsil eden bütüncül bir veri seti elde edilmiştir.

⸻

🚀 Proje Özeti

Bu chatbot, LangChain ve Google Gemini (Generative AI) modellerini kullanarak,
önceden hazırlanmış topluluk metinlerinden anlamlı cevaplar üretir.
Kullanıcı sorularını vektör tabanlı benzerlik (semantic search) ile ilgili dokümanlarla eşleştirir
ve bağlama uygun yanıt üretir.

Teknolojiler:
	•	🧠 LangChain
	•	🔍 Chroma (vektör veritabanı)
	•	🗣️ Google Gemini API
	•	💬 Gradio arayüzü
	•	💾 Hugging Face Embeddings (multilingual-e5-base)

 ⸻

🧠 Elde Edilen Sonuçlar

Oluşturulan veri seti, ChromaDB içerisine gömülmüş ve RAG (Retrieval-Augmented Generation) yaklaşımı kullanılarak sorgulanabilir hale getirilmiştir.
Kullanıcı bir girdi (soru) yazdığında sistem:
	1.	Girdiye en yakın 3 bağlamsal sonucu ChromaDB’den getirir.
	2.	Bu sonuçları kullanarak Gemini modeli ile kullanıcıya anlamlı ve bilgilendirici bir yanıt üretir.

Bu sayede kullanıcılar, toplulukla ilgili sorularına doğrudan, doğru ve bağlama uygun yanıtlar alabilmektedir.

⸻

🧩 Gereksinimler

Bu proje için aşağıdaki kütüphaneler gereklidir:

langchain
langchain-community
langchain-chroma
langchain-text-splitters
langchain-huggingface
langchain-google-genai
gradio

🔹 Colab veya terminal üzerinden tek komutla yükleyebilirsin:

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

⸻

💻 Uygulamayı Çalıştırma

🔸 Yerel Ortamda

python app.py

⸻

📂 Proje Yapısı

yazveb-chatbot/
 ├── app.py                    # Gradio arayüzü
 ├── requirements.txt          # Bağımlılıklar
 ├── .gitignore                # Gizli / gereksiz dosyaları hariç tutar
 └── data/
     ├── raw/                  # Ham metin verileri
     └── processed/
         └── chroma_db/        # (ignore edilir)

⸻

Deploy Linki

https://huggingface.co/spaces/omeberkaycoskun/yazveb
