import streamlit as st
from agents.research_agent import ask_llm
from tools.web_search import search_web

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Autonomous AI Research Agent",
    page_icon="🧠",
    layout="wide"
)

# ---------------- SIDEBAR ---------------- #

with st.sidebar:
    st.title("🧠 AI Research Agent")

    st.markdown("""
    **Capabilities**
    ✅ Autonomous research  
    ✅ Web search  
    ✅ Local LLM reasoning  
    ✅ Structured summaries  
    """)

    st.divider()

    st.info("Built using Local LLM + Tools.\nZero API cost.")

# ---------------- HEADER ---------------- #

st.title("🚀 Autonomous AI Research Agent")

st.markdown("""
Ask any research question and the agent will:

1️⃣ Search the web  
2️⃣ Analyze sources  
3️⃣ Generate a structured research summary  
""")

st.divider()

# ---------------- INPUT ---------------- #

query = st.text_input(
    "🔍 Enter your research topic:",
    placeholder="Example: How does the body digest protein?"
)

# ---------------- RUN BUTTON ---------------- #

if st.button("Run Research", use_container_width=True):

    if query:

        with st.spinner("🧠 Agent is researching... please wait"):

            results = search_web(query)

            sources = "\n".join([r["title"] for r in results])

            prompt = f"""
            Conduct deep research on:

            {query}

            Use the following sources:
            {sources}

            Provide a structured research summary.
            """

            response = ask_llm(prompt)

        # ---------- OUTPUT ---------- #

        st.success("Research Complete!")

        st.subheader("📚 Research Summary")
        st.write(response)

        with st.expander("🔎 Sources"):
            for r in results:
                st.markdown(f"- [{r['title']}]({r['url']})")

    else:
        st.warning("Please enter a research topic.")
