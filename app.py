
import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(
    page_title="StudyMate AI",
    page_icon="📚",
    layout="wide"
)

st.title("📚 StudyMate AI")
st.write("Your AI-powered study assistant for PDF notes.")
st.caption("Upload a PDF to ask questions, summarize notes, and practise.")

MAX_SIZE = 50 * 1024 * 1024

@st.cache_resource
def get_client():
    return genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

def ask_gemini(pdf_bytes, prompt):
    pdf_part = types.Part.from_bytes(
        data=pdf_bytes,
        mime_type="application/pdf"
    )

    response = get_client().models.generate_content(
        model="gemini-3.8-flash",
        contents=[
            pdf_part,
            (
                "You are StudyMate AI, a helpful study tutor. "
                "Read the attached PDF directly, including scanned pages, "
                "images, tables, and diagrams where possible. "
                "Base your response on the document. "
                "If the answer is not available, say so. "
                "Use simple, clear language. "
                "When useful, identify the relevant PDF page numbers. "
                "Never invent page references or facts.\n\n"
                + prompt
            )
        ]
    )

    return response.text or "No text response was returned."

uploaded_file = st.file_uploader(
    "Upload your study PDF",
    type=["pdf"]
)

if uploaded_file is not None:
    pdf_bytes = uploaded_file.getvalue()

    if len(pdf_bytes) > MAX_SIZE:
        st.error("This PDF is larger than 50 MB. Please upload a smaller PDF.")
        st.stop()

    if not pdf_bytes.startswith(b"%PDF-"):
        st.error("This file does not appear to be a valid PDF.")
        st.stop()

    st.success(
        f"PDF selected: {uploaded_file.name} "
        f"({len(pdf_bytes) / (1024 * 1024):.2f} MB)"
    )

    st.warning(
        "Your PDF is sent to Google's Gemini API for processing. "
        "Avoid uploading confidential documents."
    )

    tab1, tab2, tab3 = st.tabs([
        "💬 Ask Questions",
        "📝 Summarize",
        "🎯 Practice Questions"
    ])

    with tab1:
        question = st.text_area(
            "What do you want to know from this PDF?",
            placeholder="Example: Explain the main topic in simple words."
        )

        if st.button("Get Answer", key="get_answer"):
            if not question.strip():
                st.warning("Please enter a question.")
            else:
                try:
                    with st.spinner("Reading your PDF and preparing an answer..."):
                        answer = ask_gemini(
                            pdf_bytes,
                            "Answer this question:\n" + question
                        )
                    st.markdown("### Answer")
                    st.markdown(answer)
                except Exception as error:
                    st.error("Could not process the PDF.")
                    st.caption(str(error))

    with tab2:
        summary_style = st.selectbox(
            "Choose summary style",
            ["Short summary", "Detailed summary", "Exam revision notes"]
        )

        if st.button("Generate Summary"):
            try:
                with st.spinner("Preparing your summary..."):
                    summary = ask_gemini(
                        pdf_bytes,
                        "Use headings and bullet points where appropriate. "
                        f"Create a {summary_style.lower()} of this PDF. "

                        "Include important definitions, formulas, and examples."
                    )
                st.markdown("### Your Summary")
                st.markdown(summary)
            except Exception as error:
                st.error("Could not summarize the PDF.")
                st.caption(str(error))
    with tab3:
        count = st.slider(
            "Number of questions",
            min_value=5,
            max_value=15,
            value=10
        )

        question_type = st.selectbox(
            "Question type",
            ["Multiple-choice questions", "Short-answer questions", "Mixed questions"]
        )

        if st.button("Generate Practice Questions"):
            try:
                with st.spinner("Creating practice questions..."):
                    practice = ask_gemini(
                        pdf_bytes,
                        f"Create {count} {question_type.lower()} "
                        "based only on this PDF. "
                        "Provide an answer key and brief explanations. "
                        "For multiple-choice questions, provide four options "
                        "and clearly identify the correct answer."
                    )
                st.markdown("### Practice Questions")
                st.markdown(practice)
            except Exception as error:
                st.error("Could not generate practice questions.")
                st.caption(str(error))

else:
    st.info("Upload a PDF to unlock all study features.")
