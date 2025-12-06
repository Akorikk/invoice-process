from app.checkpoint_store import CheckpointStore
import uuid

def checkpoint_node(state: dict):
    print("\n--- [CHECKPOINT_HITL] Creating Checkpoint ---")

    store = CheckpointStore()

    checkpoint_id, review_url = store.save_checkpoint(
        state["invoice_payload"]["invoice_id"],
        state
    )

    print(f"[CHECKPOINT] Saved checkpoint {checkpoint_id}, URL: {review_url}")

    return {
        **state,
        "checkpoint_id": checkpoint_id,
        "review_url": review_url,
        "paused_reason": "MATCH_FAILED"
    }
