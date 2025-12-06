from tools.bigtool_picker import BigtoolPicker
import uuid

def posting_node(state: dict):
    print("\n--- [POSTING] Posting to ERP & Scheduling Payment ---")

    erp_tool = BigtoolPicker.select("erp_connector")
    print(f"[POSTING] ERP tool selected: {erp_tool}")

    return {
        **state,
        "posted": True,
        "erp_txn_id": str(uuid.uuid4()),
        "scheduled_payment_id": str(uuid.uuid4())
    }

