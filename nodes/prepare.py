from tools.bigtool_picker import BigtoolPicker
from mcp.common_client import CommonClient
from mcp.atlas_client import AtlasClient

def prepare_node(state: dict):
    print("\n--- [PREPARE] Normalizing & Enriching Vendor ---")

    vendor_name = state["invoice_payload"]["vendor_name"]

    normalized = vendor_name.strip().title()
    atlas = AtlasClient()
    enrichment = atlas.enrich_vendor(vendor_name)

    common = CommonClient()
    flags = common.compute_flags(state["invoice_payload"])

    print(f"[PREPARE] Normalized Vendor: {normalized}")
    print(f"[PREPARE] Enrichment Info: {enrichment}")
    print(f"[PREPARE] Flags: {flags}")

    return {
        **state,
        "vendor_profile": {
            "normalized_name": normalized,
            "tax_id": enrichment.get("tax_id"),
            "enrichment_meta": enrichment
        },
        "normalized_invoice": {
            "amount": state["invoice_payload"]["amount"],
            "currency": state["invoice_payload"]["currency"],
            "line_items": state["parsed_invoice"]["parsed_line_items"]
        },
        "flags": flags
    }
