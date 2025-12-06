# api/human_review.py

from fastapi import APIRouter
from app.checkpoint_store import CheckpointStore

router = APIRouter()
store = CheckpointStore()


@router.get("/human-review/pending")
def list_pending():
    """
    Returns checkpoints waiting for human decision.
    """
    pending = store.list_pending()

    items = []
    for row in pending:
        checkpoint_id, invoice_id, review_url = row
        items.append({
            "checkpoint_id": checkpoint_id,
            "invoice_id": invoice_id,
            "review_url": review_url,
            "reason_for_hold": "MATCH_FAILED"
        })

    return {"items": items}


@router.post("/human-review/decision")
def submit_decision(data: dict):
    """
    Human submits ACCEPT or REJECT decision.
    """
    checkpoint_id = data["checkpoint_id"]
    decision = data["decision"].upper()

    print(f"\n--- [HITL API] Reviewer submitted decision: {decision}")

    state = store.get_state(checkpoint_id)

    if not state:
        return {"error": "Invalid checkpoint ID"}

    store.resolve_checkpoint(checkpoint_id, decision)

    resume_token = f"resume-{checkpoint_id}-token"

    return {
        "resume_token": resume_token,
        "next_stage": "RECONCILE" if decision == "ACCEPT" else "COMPLETE"
    }
