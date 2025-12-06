# nodes/checkpoint_hitl.py

from app.checkpoint_store import CheckpointStore

def checkpoint_node(state: dict):
    print("\n--- [CHECKPOINT] Match Failed — Triggering Human Review ---")

    store = CheckpointStore()

    invoice_id = state["invoice_payload"]["invoice_id"]
    checkpoint_id, review_url = store.save_checkpoint(invoice_id, state)

    print(f"[CHECKPOINT] Saved checkpoint {checkpoint_id}, Review URL: {review_url}")

    return {
        "checkpoint_id": checkpoint_id,
        "review_url": review_url,
        "paused_reason": "MATCH_FAILED"
    }
