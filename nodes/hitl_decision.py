def hitl_node(state: dict):
    print("\n--- [HITL_DECISION] Waiting for Human Decision ---")

    # This node doesn't run automatically — only after HITL API completes
    decision = state.get("human_decision", "PENDING")

    print(f"[HITL] Human decision: {decision}")

    return {
        **state,
        "next_stage": "RECONCILE" if decision == "ACCEPT" else "COMPLETE"
    }

