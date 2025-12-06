def reconcile_node(state: dict):
    print("\n--- [RECONCILE] Building Accounting Entries ---")

    entries = [
        {"account": "Accounts Payable", "amount": state["invoice_payload"]["amount"], "type": "credit"},
        {"account": "Expense", "amount": state["invoice_payload"]["amount"], "type": "debit"}
    ]

    return {
        **state,
        "accounting_entries": entries,
        "reconciliation_report": {"status": "OK"}
    }
