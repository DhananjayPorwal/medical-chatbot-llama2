from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA
import chainlit as cl

DB_FAISS_PATH = "vectorstores/db_faiss"

custom_prompt_template = """Use the following pieces of information to answer the user's question.

- If the answer is not clear or if the information is insufficient, simply say: "I don't know" and do not make up an answer.
- Always use professional, accurate medical terminology when necessary.
- Provide only the direct answer to the user's question. Do not include any additional information or explanations unless explicitly requested.

Context: {context}
Question: {question}
Answer:
"""

def set_custom_prompt():
    """
    Prompt template for the QA Retrieval for each vector store
    """

    prompt = PromptTemplate(
        template=custom_prompt_template,
        input_variables=["context", "question"]
    )

    return prompt


def load_llm():
    """
    Load the LLM model
    """

    llm = CTransformers(
        model="llama-2-7b-chat.ggmlv3.q8_0.bin",
        model_type="llama",
        device="cpu",
        max_new_tokens=1024,
        temperature=0.1,
        # top_p=0.95,
        # top_k=40,
        # repetition_penalty=1.2,
        # n_threads=4
    )

    return llm

def retrieve_qa_chain(llm, prompt, db):
    """
    Load the vector store and create the retrieval QA chain
    """

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=db.as_retriever(search_kwargs={"k": 5}),
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )
    return qa_chain

def qa_bot():
    """
    Load the vector store and create the retrieval QA chain
    """

    embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2", model_kwargs = {'device': 'cpu'})
    db = FAISS.load_local(DB_FAISS_PATH, embeddings, allow_dangerous_deserialization=True)
    llm = load_llm()
    prompt = set_custom_prompt()
    qa_chain = retrieve_qa_chain(llm, prompt, db)
    return qa_chain

def final_result(query):
    """
    Display the result in chainlit
    """

    qa_result = qa_bot()
    response = qa_result({"query": query})
    return response

# Chain lit
@cl.on_chat_start
async def start():
    """
    Start the chat
    """
    chain = qa_bot()
    message = cl.Message(content = "Starting the chat...")
    await message.send()
    message.content = "Hi, Welcome to the Medical Chatbot. How can I help you today?"
    await message.update()
    cl.user_session.set('chain', chain)

@cl.on_message
async def main(message):
    """
    Main function to handle the chat
    """
    chain = cl.user_session.get('chain')
    cb = cl.AsyncLangchainCallbackHandler(
        stream_final_answer=True,
        answer_prefix_tokens=["FINAL", "ANSWER"]
    )
    result = await chain.acall(message.content, callbacks=[cb])

    answer = result['result']
    sources = result['source_documents']


    if sources:
        answer += f'\n\nSources:\n' + str(sources)
    else:
        answer += '\n\nSources:\nNo sources found.'

    await cl.Message(content = answer).send()
    # await cl.Message(content = "Thank you for your question!").send()
    # await cl.Message(content = "If you have any more questions, feel free to ask!").send()