knowledge_base = [
    {
        "topic": "invoice",
        "information": "Invoices can be created, sent, and retrieved."
    },
    {
        "topic": "payment",
        "information": "Payments can be processed and refunded."
    },
    {
        "topic": "dispute",
        "information": "Dispute information can be retrieved from the payment system."
    },
    {
        "topic": "report",
        "information": "Sales reports provide information about sales activity."
    }
]


def search_knowledge(query):
    query = query.lower()

    results = []

    for item in knowledge_base:

        if item["topic"] in query:
            results.append(item["information"])

        elif item["topic"] == "payment" and "refund" in query:
            results.append(item["information"])

    return results