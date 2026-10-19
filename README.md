# StudyMate AI – AI-Powered Study Assistant

## 🌐 Live Demo

**Live App:** https://studymate-ai-8v7mrkuqw2ekdmybwctrlc.streamlit.app/

**GitHub Repository:** https://github.com/r7611568-Ruhi/StudyMate-AI

## 📖 About the Project

StudyMate AI is an AI-powered educational web application designed to help students study smarter and understand academic materials more easily. It uses Generative Artificial Intelligence to summarize PDF documents, answer questions based on study materials, and generate practice questions for exam preparation.

The application is built using Python and Streamlit and integrates Google's Gemini API to provide AI-generated responses.

## ✨ Features

- **📄 PDF Upload:** Upload PDF study materials directly to the application.
- **📝 AI-Powered Summarization:** Generate summaries of lengthy study documents.
- **💬 Ask Questions:** Ask questions about uploaded study materials and receive AI-generated answers.
- **❓ Practice Questions:** Generate practice questions to test your understanding.
- **🎯 Student-Friendly Interface:** Simple interface designed to make studying easier.
- **🤖 Generative AI Integration:** Uses Google's Gemini API to process study materials and generate responses.

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API
- Generative Artificial Intelligence (GenAI)
- PDF document processing

## 🎯 Project Objectives

1. Make academic learning easier with artificial intelligence.
2. Help students understand lengthy study materials.
3. Reduce the time required to revise academic notes.
4. Support self-learning through AI-generated answers and practice questions.
5. Demonstrate the practical application of Generative AI in education.

## ⚙️ How It Works

1. Open the StudyMate AI web application.
2. Upload a PDF containing your study material.
3. Choose the feature you want to use.
4. Generate a summary, ask a question, or create practice questions.
5. Review the generated response and use it to support your learning.

## 💻 Installation and Setup

Follow these steps to run StudyMate AI on your computer.

### Prerequisites

- Python installed on your computer.
- Git installed on your computer.
- A Google Gemini API key.

### Step 1: Clone the Repository

Open Terminal and run:

```bash
git clone https://github.com/r7611568-Ruhi/StudyMate-AI.git
cd StudyMate-AI
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Configure the API Key

Create a folder named `.streamlit` in the project directory. Inside it, create a file named `secrets.toml`.

Add the following line:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

Replace `YOUR_GEMINI_API_KEY` with your own valid Gemini API key.

**Security note:** Never upload your actual API key or the `secrets.toml` file to a public GitHub repository.

### Step 4: Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your web browser.

## ☁️ Deployment

StudyMate AI is deployed using Streamlit Community Cloud.

**Live Application:** https://studymate-ai-8v7mrkuqw2ekdmybwctrlc.streamlit.app/

The deployed application uses Streamlit secrets to securely configure the Gemini API key.

## 🔐 Security

- Store the Gemini API key securely using Streamlit secrets.
- Do not hardcode secret API keys in the source code.
- Do not commit `.streamlit/secrets.toml` or `.env` files to GitHub.
- Keep API credentials private.

## 🔮 Future Enhancements

- Support for additional document formats.
- Faster PDF processing and AI responses.
- Saved chat history and study sessions.
- Customizable quizzes and multiple-choice questions.
- More personalized learning and revision features.

## 🎓 Conclusion

StudyMate AI demonstrates how Generative AI can be applied to education to support students in understanding study materials, revising important concepts, and practising questions. By combining PDF uploads, summarization, question answering, and practice question generation, the project provides a practical example of AI-assisted learning.

## 👩‍💻 Developer

**Ruhi Farhaz**

GitHub: https://github.com/r7611568-Ruhi

---

*StudyMate AI — Learn smarter with Generative AI.*
