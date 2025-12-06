# nodes/approve.py

def approve_node(state: dict):
    print("\n--- [APPROVE] Applying Approval Workflow ---")

    amount = state["invoice_payload"]["amount"]

    if amount < 5000:
        status = "AUTO_APPROVED"
    else:
        status = "ESCALATED"

    print(f"[APPROVE] Approval status: {status}")

    return {
        "approval_status": status,
        "approver_id": "system"
    }
