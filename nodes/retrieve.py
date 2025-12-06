from tools.bigtool_picker import BigtoolPicker
from mcp.atlas_client import AtlasClient

def retrieve_node(state: dict):
    print("\n--- [RETRIEVE] Fetching PO, GRN, and history ---")

    erp_tool = BigtoolPicker.select("erp_connector")
    print(f"[RETRIEVE] ERP connector selected: {erp_tool}")

    atlas = AtlasClient()
    po = atlas.fetch_po(state["invoice_payload"]["invoice_id"])
    grn = atlas.fetch_grn(state["invoice_payload"]["invoice_id"])
    history = atlas.fetch_history(state["invoice_payload"]["vendor_name"])

    print("[RETRIEVE] Data fetched successfully.")

    return {
        **state,
        "matched_pos": po,
        "matched_grns": grn,
        "history": history
    }
