
# AI First CRM – HCP Interaction Module

This project demonstrates a simple architecture for an AI powered CRM system used by healthcare sales representatives.

Tech Stack

Frontend
React

Backend
FastAPI (Python)

AI Layer
LangGraph style workflow with LLM integration

Database
Example uses in‑memory storage (can be replaced with MySQL/PostgreSQL)

Features

Log doctor interaction
Structured form submission
Conversation processing (concept)
Interaction storage
Interaction retrieval API

Run Backend

pip install -r requirements.txt
uvicorn main:app --reload

Run Frontend

npm install
npm start

Architecture

React UI → FastAPI API → AI Agent → Database
