from tool_registry import search_tools


def route_request(user_request):
    request = user_request.lower()

    # Send invoice
    if "send" in request and "invoice" in request:
        tools = search_tools("invoice")

        for tool in tools:
            if tool["name"] == "send_invoice":
                return [tool]

    # Create invoice
    elif "create" in request and "invoice" in request:
        tools = search_tools("invoice")

        for tool in tools:
            if tool["name"] == "create_invoice":
                return [tool]

    # Check / find / open dispute
    elif (
        ("check" in request or "is there" in request or "open" in request)
        and "dispute" in request
    ):
        tools = search_tools("dispute")

        for tool in tools:
            if tool["name"] == "get_dispute":
                return [tool]

    # Create dispute
    elif "create" in request and "dispute" in request:
        tools = search_tools("dispute")

        for tool in tools:
            if tool["name"] == "create_dispute":
                return [tool]

    # Refund
    elif "refund" in request:
        tools = search_tools("payment")

        for tool in tools:
            if tool["name"] == "refund_payment":
                return [tool]

    elif "invoice" in request:
        return search_tools("invoice")

    elif "sales" in request or "report" in request:
        return search_tools("report")

    elif "payment" in request:
        return search_tools("payment")

    elif "dispute" in request:
        return search_tools("dispute")

    return []