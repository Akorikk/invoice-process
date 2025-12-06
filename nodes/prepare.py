# nodes/prepare.py

from tools.bigtool_picker import BigtoolPicker
from mcp.common_client import CommonClient
from mcp.atlas_client import AtlasClient

def prepare_node(state: dict):
    print("\n--- [PREPARE] Normalizing & Enriching Vendor ---")

    common = CommonClient()
    atlas = AtlasClient()

    vendor_name = state["invoice_payload"]["vendor_name"]

    normalized_name = common.normalize_vendor(vendor_name)
    print(f"[PREPARE] Normalized vendor name: {normalized_name}")

    enrich_tool = BigtoolPicker.select("enrichment")
    print(f"[PREPARE] Enrichment tool selected: {enrich_tool}")

    vendor_enrichment = atlas.enrich_vendor(normalized_name)
    print(f"[PREPARE] Enrichment results: {vendor_enrichment}")

    flags = common.compute_flags(state["invoice_payload"])
    print(f"[PREPARE] Generated flags: {flags}")

    return {
        "vendor_profile": {
            "normalized_name": normalized_name,
            "tax_id": vendor_enrichment["tax_id"],
            "enrichment_meta": vendor_enrichment
        },
        "normalized_invoice": {
            "amount": state["invoice_payload"]["amount"],
            "currency": state["invoice_payload"]["currency"],
            "line_items": state["parsed_invoice"]["parsed_line_items"]
        },
        "flags": flags
    }
