# Tool Registry
# This registry contains 500 tool definitions.
# The first 12 tools are the core demo tools used by the prototype.


tools = [
    # Invoice tools
    {
        "name": "create_invoice",
        "category": "invoice",
        "description": "Create a new invoice"
    },
    {
        "name": "send_invoice",
        "category": "invoice",
        "description": "Send an invoice to a customer"
    },
    {
        "name": "get_invoice",
        "category": "invoice",
        "description": "Get invoice details"
    },

    # Payment tools
    {
        "name": "process_payment",
        "category": "payment",
        "description": "Process a payment"
    },
    {
        "name": "refund_payment",
        "category": "payment",
        "description": "Refund a payment"
    },
    {
        "name": "get_payment",
        "category": "payment",
        "description": "Get payment details"
    },

    # Dispute tools
    {
        "name": "create_dispute",
        "category": "dispute",
        "description": "Create a payment dispute"
    },
    {
        "name": "get_dispute",
        "category": "dispute",
        "description": "Check dispute details"
    },

    # Customer tools
    {
        "name": "create_customer",
        "category": "customer",
        "description": "Create a customer"
    },
    {
        "name": "get_customer",
        "category": "customer",
        "description": "Get customer details"
    },

    # Report tools
    {
        "name": "get_sales_report",
        "category": "report",
        "description": "Get sales report"
    },
    {
        "name": "get_payment_report",
        "category": "report",
        "description": "Get payment report"
    }
]


# Additional categories for scalability demonstration
categories = [
    "order",
    "product",
    "subscription",
    "account",
    "notification",
    "shipping",
    "inventory",
    "transaction",
    "user",
    "authentication",
    "authorization",
    "profile",
    "address",
    "cart",
    "checkout",
    "delivery",
    "refund",
    "billing",
    "currency",
    "tax",
    "analytics",
    "audit",
    "support",
    "ticket",
    "message",
    "document",
    "file",
    "reporting",
    "search",
    "settings"
]


# Generate additional tool definitions until the registry contains 500 tools.
tool_number = 1

while len(tools) < 500:
    category = categories[(tool_number - 1) % len(categories)]

    tool = {
        "name": f"{category}_tool_{tool_number}",
        "category": category,
        "description": f"Perform {category} related operation"
    }

    tools.append(tool)

    tool_number += 1


def search_tools(category):
    results = []

    for tool in tools:
        if tool["category"] == category:
            results.append(tool)

    return results


def get_tool_count():
    return len(tools)


def search_tools_by_keyword(keyword):
    keyword = keyword.lower()

    results = []

    for tool in tools:
        if (
            keyword in tool["name"].lower()
            or keyword in tool["description"].lower()
            or keyword in tool["category"].lower()
        ):
            results.append(tool)

    return results