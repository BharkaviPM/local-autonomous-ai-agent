# 🧠 Local Autonomous Research Agent

A fully local AI-powered research agent that performs web search, downloads research papers, and generates structured research summaries using an on-device Large Language Model via Ollama.

## 🚀 Features

- ✅ Fully local LLM (No OpenAI / Claude required)
- ✅ Autonomous research workflow
- ✅ Web search integration (DuckDuckGo / DDGS)
- ✅ PDF auto-downloader
- ✅ Memory-ready architecture
- ✅ Zero API cost
- ✅ Privacy-friendly

---

## 🏗️ Architecture

User Query  
→ Web Search  
→ PDF Extraction  
→ Local LLM Reasoning  
→ Structured Research Summary  

---

## ⚙️ Tech Stack

- **Ollama** — Local LLM runtime  
- **Mistral / Llama3** — Reasoning engine  
- **Python**  
- **Streamlit** (optional UI)  
- **DDGS** — Free web search  

---

## 📦 Installation

### 1️⃣ Install Ollama

https://ollama.com/download

Pull a model:

```bash
ollama pull mistral
