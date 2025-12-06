# nodes/hitl_decision.py

from app.checkpoint_store import CheckpointStore

def hitl_node(state: dict):
    print("\n--- [HITL] Resuming After Human Decision ---")

    decision = state["human_decision"]

    print(f"[HITL] Reviewer decision: {decision}")

    if decision == "ACCEPT":
        return {
            "next_stage": "RECONCILE",
            "resume_token": "resume-123"
        }

    return {
        "next_stage": "COMPLETE",
        "status": "MANUAL_HANDOFF"
    }
