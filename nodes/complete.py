def complete_node(state: dict):
    print("\n--- [COMPLETE] Finalizing Workflow ---")

    final_payload = {
        "invoice_id": state["invoice_payload"]["invoice_id"],
        "status": "SUCCESS",
        "total_amount": state["invoice_payload"]["amount"]
    }

    return {
        **state,
        "final_payload": final_payload,
        "status": "COMPLETE"
    }

