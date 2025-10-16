-----

# 🤖 AI-GRC-Assistant-Backend-2025

## 🌟 Project Overview

The **AI-GRC-Assistant-Backend** is a critical solution developed to address the complexity of Cybersecurity Governance, Risk, and Compliance (GRC) in the context of Saudi Arabia's **Vision 2030** digital transformation efforts.

**Problem:** Organizations struggle with interpreting and manually assessing compliance against detailed, technical regulations like the NCA's Essential Cybersecurity Controls (ECC). Manual reviews are slow and inconsistent.

**Solution:** This service implements a highly reliable **Retrieval-Augmented Generation (RAG)** architecture using **FastAPI**. It leverages Large Language Models (LLMs) and a specialized Vector Database (ChromaDB) to ground all advisory responses directly in the official NCA ECC documentation.

This microservice ensures real-time, accurate, and scalable GRC advisory, enabling fast, informed compliance self-assessments.

-----

## 🚀 Key Technical Features

This project demonstrates strong proficiency across several modern software and AI engineering disciplines:

  * **Microservices Architecture:** Implemented as a standalone **FastAPI** service (`app.py`), ensuring clean separation of concerns and enabling horizontal scaling.
  * **RAG Implementation:** Uses a custom `RAGSystem` built with **LangChain** and **ChromaDB** to retrieve context from specialized knowledge bases, focusing on precision and relevance.
  * **Security & Compliance Focus:** The system is explicitly configured via a strict `PromptTemplate` to adhere **ONLY** to the provided compliance context, significantly mitigating the risk of **hallucination** in regulatory advice (`rag_system.py`).
  * **Deployment Ready (DevOps):** Includes a lightweight and efficient **Dockerfile** for seamless **containerization** and deployment to cloud environments.
  * **Modular Design:** API routing (`app.py`) is cleanly separated from complex RAG logic (`rag_system.py`), promoting maintainability.

-----

## ⚙️ Tech Stack & Dependencies

| Component | Technology / Library | Purpose |
| :--- | :--- | :--- |
| **Framework** | **FastAPI** | High-performance backend API serving the RAG functionality. |
| **RAG/Orchestration** | **LangChain** | Manages the RAG pipeline (retrieval, prompting, output parsing). |
| **Vector Database** | **ChromaDB** | Stores the vectorized NCA ECC Guide data for efficient retrieval. |
| **Embedding Model** | `sentence-transformers` | Used by the RAG system for text vectorization. |
| **LLM Provider** | **Together AI** | Utilized for the Generative Model (`Llama-3-8b-chat-hf` default). |
| **Containerization** | **Docker** | Ensures consistent build and deployment environment. |

### 📊 Knowledge Base (VDB Asset)

The authoritative dataset is hosted separately to enable robust asset management and version control:

  * **Dataset Source (Hugging Face):** [`iMeshal/GRC-ECC-Guide-VDB`](https://www.google.com/search?q=%5Bhttps://huggingface.co/datasets/iMeshal/GRC-ECC-Guide-VDB%5D\(https://huggingface.co/datasets/iMeshal/GRC-ECC-Guide-VDB\))
  * **Content:** Essential Cybersecurity Controls (ECC) Implementation Guide – National Cybersecurity Authority (NCA).

-----

## 🎯 Model Evaluation Metrics

The performance metrics below validate the system's effectiveness in generating reliable, compliant, and contextually precise answers:

**Note:** Performance metrics were derived from an evaluation run against a **custom RAG Reference Dataset** based on the NCA ECC Guide. All evaluation artifacts (notebook and dataset) are located in the **`/evaluation`** directory.

| Metric | Score | Interpretation |
| :--- | :--- | :--- |
| **Answer Relevancy** | **0.9541** | High score indicating the generated answers directly address the user's question. |
| **Faithfulness** | **0.8113** | Confirms a strong adherence to the source context, minimizing the risk of hallucination (a critical factor in compliance applications). |
| **Context Precision** | **0.6875** | Measures the relevance of retrieved data segments. Indicates a majority of retrieved context is useful. |
| **Context Recall** | **0.7250** | Confirms a good rate of successfully retrieving necessary documents required to answer the question. |
| **Semantic Similarity** | **0.8160** | The model's answers are close in meaning to ideal reference answers. |

-----

## 🛠️ Quick Start (Local Setup)

### 1\. Prerequisites

  * **Docker** and **Docker Compose** installed.
  * An API Key for **Together AI** (set as `TOGETHER_API_KEY` environment variable).
  * The Vector Database must be downloaded from the Hugging Face repository and placed in the project directory named `vector_db`.

### 2\. Build and Run the Container

Build the Docker image:

bash
docker build -t ai-grc-backend .


Run the container, exposing the API on port `7860`:

bash
docker run -d -p 7860:7860 --env TOGETHER_API_KEY=<Your_Key> ai-grc-backend


### 3\. Test the API Endpoint

Access the live `/ask` endpoint to test the RAG functionality:

bash
curl -X POST http://localhost:7860/ask \
-H "Content-Type: application/json" \
-d '{"question": "What are the requirements for physical security according to the guide?"}'

### 4\. Replicate Evaluation
The performance metrics can be replicated and verified using the artifacts provided:

Evaluation Data: /evaluation/rag_evaluate_question_with_reference.json

Jupyter Notebook: /evaluation/evaluate.ipynb (Includes all steps to run the Ragas-based evaluation)

-----

## 🤝 Contact

| Detail | Information |
| :--- | :--- |
| **Author** | Meshal Qushaym |
| **Email** | meshalqushim@outlook.com |
| **GitHub Username** | MQushaym |

-----
