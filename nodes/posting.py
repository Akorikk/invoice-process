# nodes/posting.py

from tools.bigtool_picker import BigtoolPicker

def posting_node(state: dict):
    print("\n--- [POSTING] Posting Invoice to ERP & Scheduling Payment ---")

    erp_tool = BigtoolPicker.select("erp_connector")
    print(f"[POSTING] ERP selected: {erp_tool}")

    txn_id = "ERP-TXN-98765"
    payment_id = "PAY-554433"

    return {
        "posted": True,
        "erp_txn_id": txn_id,
        "scheduled_payment_id": payment_id
    }
