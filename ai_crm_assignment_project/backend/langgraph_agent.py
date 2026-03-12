
# Example LangGraph style workflow (concept demo)

def process_interaction(user_text):
    '''
    This function represents how an AI agent could extract CRM data
    from a conversation using an LLM.
    '''

    # In real system this would call Groq API with LLM
    extracted = {
        "doctor_name": "Dr Example",
        "discussion_notes": user_text,
        "interaction_type": "Meeting"
    }

    return extracted
