def execute_tool(tool_name, parameters):
    try:

        if tool_name == "create_invoice":
            amount = parameters.get("amount")

            if amount is None:
                return {
                    "success": False,
                    "error": "Invoice amount is required"
                }

            return {
                "success": True,
                "message": f"Invoice created for ${amount}"
            }

        elif tool_name == "send_invoice":
            invoice_id = parameters.get("invoice_id")
            amount = parameters.get("amount")

            if invoice_id is None:
                return {
                    "success": False,
                    "error": "Invoice ID is required"
                }

            if amount is None:
                return {
                    "success": False,
                    "error": "Invoice amount is required"
                }

            return {
                "success": True,
                "message": f"Invoice {invoice_id} for ${amount} sent successfully"
            }

        elif tool_name == "get_invoice":
            invoice_id = parameters.get("invoice_id", "INV001")

            return {
                "success": True,
                "message": f"Invoice details retrieved for {invoice_id}"
            }

        elif tool_name == "process_payment":
            amount = parameters.get("amount", 100)

            return {
                "success": True,
                "message": f"Payment of ${amount} processed successfully"
            }

        elif tool_name == "refund_payment":
            payment_id = parameters.get("payment_id", "PAY001")

            return {
                "success": True,
                "message": f"Payment {payment_id} refunded successfully"
            }

        elif tool_name == "get_payment":
            payment_id = parameters.get("payment_id", "PAY001")

            return {
                "success": True,
                "message": f"Payment details retrieved for {payment_id}"
            }

        elif tool_name == "create_dispute":
            payment_id = parameters.get("payment_id", "PAY001")

            return {
                "success": True,
                "message": f"Dispute created for {payment_id}"
            }

        elif tool_name == "get_dispute":
            user_id = parameters.get("user_id")

            if user_id is None:
                return {
                    "success": False,
                    "error": "User ID is required"
                }

            return {
                "success": True,
                "message": f"Dispute information retrieved for {user_id}"
            }

        elif tool_name == "create_customer":
            name = parameters.get("name", "Demo Customer")

            return {
                "success": True,
                "message": f"Customer {name} created successfully"
            }

        elif tool_name == "get_customer":
            customer_id = parameters.get("customer_id", "CUS001")

            return {
                "success": True,
                "message": f"Customer details retrieved for {customer_id}"
            }

        elif tool_name == "get_sales_report":
            return {
                "success": True,
                "message": "Sales report generated successfully"
            }

        elif tool_name == "get_payment_report":
            return {
                "success": True,
                "message": "Payment report generated successfully"
            }

        else:
            return {
                "success": False,
                "error": "Unknown tool"
            }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }