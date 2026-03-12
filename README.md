# ai-first-crm-hcp-module
# AI-First CRM – HCP Interaction Module

## Overview
This project demonstrates an AI-powered CRM module designed for healthcare sales representatives to log and manage interactions with Healthcare Professionals (HCPs) such as doctors and clinics.

The system supports two interaction methods:
1. Structured form input
2. Conversational AI interface

The AI component extracts structured CRM data from natural language conversations and stores it in the system.

---

## Tech Stack

Frontend  
- React  
- Redux (conceptually for state management)  
- Google Inter Font  

Backend  
- Python  
- FastAPI  

AI Layer  
- LangGraph agent workflow  
- Groq LLM (gemma2-9b-it / llama-3.3-70b)

Database  
- PostgreSQL / MySQL

---

## System Architecture

React Frontend → FastAPI Backend → LangGraph Agent → Groq LLM → Database

### Flow
1. Sales representative logs interaction.
2. Data is sent to FastAPI backend.
3. LangGraph AI agent processes conversational input.
4. Groq LLM extracts structured data.
5. Interaction data is stored in the database.

---

## Key Features

- Log doctor interactions
- Conversational AI interaction logging
- Interaction history storage
- Follow-up scheduling
- CRM data extraction from natural language

---

## Example Interaction

User Input:

"I met Dr Sharma today and discussed a diabetes drug. He requested clinical trial data."

Extracted Output:

Doctor Name: Dr Sharma  
Topic: Diabetes drug  
Follow Up: Send clinical trial data  

---

## Project Structure
