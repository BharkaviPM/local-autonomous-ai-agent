import os
import re
from datetime import datetime

from agents.research_agent import ask_llm
from tools.web_search import search_web
from tools.pdf_downloader import download_pdfs
from memory.conversation_memory import Memory


def safe_folder_name(text):

    text = re.sub(r'[<>:"/\\|?*]', '', text)
    text = text.replace(" ", "_")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    return f"{text}_{timestamp}"


def autonomous_research(topic):

    folder = f"papers/{safe_folder_name(topic)}"
    os.makedirs(folder, exist_ok=True)

    memory = Memory()

    print("🔎 Searching web...")

    results = search_web(topic)

    pdfs = download_pdfs(results, folder)

    prompt = f"""
    Conduct a research-style analysis on:

    {topic}

    Use academic reasoning.
    
    Provide:
    - Key concepts
    - Scientific explanation
    - Recent advancements
    - Future research directions
    """

    summary = ask_llm(prompt, memory)

    return summary, pdfs


if __name__ == "__main__":

    topic = input("Enter research topic: ")

    result, files = autonomous_research(topic)

    print("\n===== RESEARCH SUMMARY =====\n")
    print(result)

    print("\nDownloaded PDFs:")
    print(files)
