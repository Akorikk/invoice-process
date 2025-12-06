# nodes/retrieve.py

from tools.bigtool_picker import BigtoolPicker
from mcp.atlas_client import AtlasClient

def retrieve_node(state: dict):
    print("\n--- [RETRIEVE] Fetching PO / GRN / Historical Invoices ---")

    erp_tool = BigtoolPicker.select("erp_connector")
    print(f"[RETRIEVE] ERP connector selected: {erp_tool}")

    atlas = AtlasClient()
    invoice_id = state["invoice_payload"]["invoice_id"]

    pos = atlas.fetch_po(invoice_id)
    grns = atlas.fetch_grn(invoice_id)
    history = atlas.fetch_history(state["invoice_payload"]["vendor_name"])

    print(f"[RETRIEVE] Retrieved {len(pos)} POs, {len(grns)} GRNs, {len(history)} history items.")

    return {
        "matched_pos": pos,
        "matched_grns": grns,
        "history": history
    }
