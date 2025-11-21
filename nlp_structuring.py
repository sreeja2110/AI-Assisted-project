def structure_medical_record(text):
    record = f"""
    ---- Structured Medical Record ----

    Chief Complaint:
    {text}

    Assessment:
    • Symptoms analyzed and converted from speech.

    Plan:
    • Follow-up and further diagnosis recommended.

    -----------------------------------
    """
    return record
