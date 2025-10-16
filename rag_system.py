# rag_system.py

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Together
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import os

class RAGSystem:
    def __init__(self, vector_db_path="vector_db", model_name="meta-llama/Llama-3-8b-chat-hf", embedding_model_name="sentence-transformers/all-mpnet-base-v2", api_key=None):
        self.vector_db_path = vector_db_path
        self.embedding_model_name = embedding_model_name
        self.model_name = model_name
        self.api_key = api_key or os.getenv("TOGETHER_API_KEY")

        self.embedding_model = None
        self.vectorstore = None
        self.llm = None
        self.prompt_template = None

    def load_vectorstore(self):
        self.embedding_model = HuggingFaceEmbeddings(model_name=self.embedding_model_name)
        self.vectorstore = Chroma(persist_directory=self.vector_db_path, embedding_function=self.embedding_model)
        print(f"✅ Vectorstore loaded from: {self.vector_db_path}")
        return self.vectorstore

    def load_llm(self):
        if not self.api_key:
            raise ValueError("❌ API key not found. Please set TOGETHER_API_KEY.")
        self.llm = Together(
            model=self.model_name,
            temperature=0.2,
            max_tokens=512,
            top_p=0.95,
            together_api_key=self.api_key
        )
        print(f"✅ LLM loaded from Together: {self.model_name}")
        return self.llm

    def get_prompt_template(self):
        self.prompt_template = PromptTemplate(
            input_variables=["context", "question", "sources"],
            template="""
            You are a cybersecurity compliance assistant specializing in Saudi Arabian regulations.
            Use ONLY the provided official documents (NCA Cybersecurity Framework, YESSER standards, SCYWF, or ECC controls) to answer.
            If the answer cannot be found in the provided context, respond with:
            "The answer is not available in the ECC guide." (Arabic: "الإجابة غير متوفرة في دليل ECC")
            Instructions:
            - Provide factual, formal, and concise answers only from the context.
            - Do NOT add conversational phrases (e.g., "Hello, I'm happy to help you").
            - If the question explicitly asks for a summary, present a short bullet-point summary.
            - Merge related points without repetition.
            - Always add the sources at the end of the answer in the format: "Sources: {sources}".
            - Do NOT mention being an AI model.
            - If the context contains no relevant data, state clearly it is not available.

            Context:
            {context}

            Question:
            {question}

            Answer:
            """
        )
        return self.prompt_template



    def ask_question(self, user_input):

        # استرجاع الوثائق ذات الصلة
        retriever = self.vectorstore.as_retriever(search_kwargs={"k": 3})
        docs = retriever.invoke(user_input)

        if not docs:
            return "The answer is not available in the ECC guide."

        # بناء السياق والمصادر
        context = "\n\n".join([d.page_content for d in docs])
        raw_sources = [
            f"source={d.metadata.get('source','?')};page={d.metadata.get('page_label', d.metadata.get('page','?'))}"
            for d in docs
        ]
        sources = " | ".join(set(raw_sources))

        # إعداد السؤال والإجابة
        answer_prompt = self.prompt_template.format(
            context=context, question=user_input, sources=sources
        )
        answer = self.llm(answer_prompt)

        return answer