# nodes/complete.py

def complete_node(state: dict):
    print("\n--- [COMPLETE] Finalizing Workflow ---")

    final_payload = {
        "invoice_id": state["invoice_payload"]["invoice_id"],
        "status": "COMPLETED",
        "match_score": state.get("match_score"),
        "approval_status": state.get("approval_status")
    }

    print("[COMPLETE] Workflow successfully completed.")

    return {
        "final_payload": final_payload,
        "audit_log": ["Completed all stages successfully"],
        "status": "SUCCESS"
    }
