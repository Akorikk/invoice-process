def approve_node(state: dict):
    print("\n--- [APPROVE] Running Approval Policy ---")

    amount = state["invoice_payload"]["amount"]
    approval_status = "APPROVED" if amount < 1000 else "ESCALATED"

    return {
        **state,
        "approval_status": approval_status,
        "approver_id": "system_auto" if approval_status == "APPROVED" else "manager_01"
    }
