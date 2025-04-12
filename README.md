# Medical Chat Bot 🚑🤖

Welcome to **Medical Chat Bot**, a conversational AI application designed to provide accurate and professional medical information. This chatbot leverages advanced language models and retrieval-based QA systems to deliver precise answers to user queries. 

---

## Features ✨

- **Accurate Medical Responses**: Uses professional medical terminology to ensure reliable answers.
- **Customizable Prompt Template**: Tailored to provide concise and context-aware responses.
- **Retrieval-Based QA**: Integrates with FAISS vector store for efficient document retrieval.
- **Streamed Responses**: Provides real-time, streamed answers for a seamless user experience.

---

## How It Works 🛠️

1. **Custom Prompt Template**: A predefined prompt ensures the chatbot provides accurate and professional responses.
2. **LLM Integration**: Powered by the `llama-2-7b-chat` model for natural language understanding.
3. **Vector Store**: Uses FAISS for efficient document retrieval, enabling context-aware answers.
4. **Chainlit Framework**: Built on Chainlit to handle chat interactions and manage user sessions.

---

## Setup Instructions 🚀

### Prerequisites

- Python 3.10 or higher
- Required Python libraries (see `requirements.txt`)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/DhananjayPorwal/medical-chatbot-llama2.git
   cd medical-chatbot-llama2
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the LLM model:
   - Place the `llama-2-7b-chat.ggmlv3.q8_0.bin` model file in the appropriate directory.

4. Set up the FAISS vector store:
   - Ensure the FAISS database is located at `vectorstores/db_faiss`.

---

## Usage 🩺

1. Start the chatbot:

```bash
chainlit run model.py
```

2. Open the chatbot in your browser (default: `http://localhost:8000`).

3. Interact with the chatbot by asking medical-related questions.

---

## Configuration ⚙️

### Custom Prompt Template

The chatbot uses a custom prompt template defined in the `model.py` file:

```python
custom_prompt_template = """Use the following pieces of information to answer the user's question.

- If the answer is not clear or if the information is insufficient, simply say: "I don't know" and do not make up an answer.
- Always use professional, accurate medical terminology when necessary.
- Provide only the direct answer to the user's question. Do not include any additional information or explanations unless explicitly requested.

Context: {context}
Question: {question}
Answer:
"""
```

You can modify this template to suit your specific requirements.

### Chainlit Configuration

The chatbot's UI and behavior can be customized via the `config.toml` file located in the `.chainlit` directory. For example:

- **Assistant Name**: Change the assistant's name in the `[UI]` section.
- **Themes**: Set the default theme (light/dark/system).
- **Custom CSS/JS**: Add custom styles or scripts for the UI.

---

## Contributing 🤝

We welcome contributions to improve the chatbot! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

---

## Useful Links 🔗

- **Chainlit Documentation**: [docs.chainlit.io](https://docs.chainlit.io)
- **Join the Community**: [Chainlit Discord](https://discord.gg/k73SQ3FyUh)

---

Thank you for using Medical Chat Bot. If you have any questions or feedback, feel free to reach out. 😊 
