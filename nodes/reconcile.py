# nodes/reconcile.py

def reconcile_node(state: dict):
    print("\n--- [RECONCILE] Building Accounting Entries ---")

    entries = [
        {"account": "Expenses", "debit": state["invoice_payload"]["amount"]},
        {"account": "Cash/Bank", "credit": state["invoice_payload"]["amount"]}
    ]

    print("[RECONCILE] Accounting entries created.")

    return {
        "accounting_entries": entries,
        "reconciliation_report": {"status": "OK"}
    }
