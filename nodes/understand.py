# nodes/understand.py

from tools.bigtool_picker import BigtoolPicker
from mcp.atlas_client import AtlasClient
import random

def understand_node(state: dict):
    print("\n--- [UNDERSTAND] Starting OCR + Parsing Stage ---")

    ocr_tool = BigtoolPicker.select("ocr")
    print(f"[UNDERSTAND] OCR provider selected: {ocr_tool}")

    attachments = state["invoice_payload"].get("attachments", [])

    invoice_text = "Mock OCR text extracted from invoice image."
    print(f"[UNDERSTAND] OCR extracted text: {invoice_text[:50]}...")

    # Mock parsing
    parsed_line_items = [
        {"desc": "Item A", "qty": 2, "unit_price": 100, "total": 200},
        {"desc": "Item B", "qty": 1, "unit_price": 300, "total": 300}
    ]

    detected_pos = ["PO-7788"]

    print("[UNDERSTAND] Extracted line items and PO references successfully.")

    return {
        "parsed_invoice": {
            "invoice_text": invoice_text,
            "parsed_line_items": parsed_line_items,
            "detected_pos": detected_pos,
            "currency": state["invoice_payload"]["currency"],
            "parsed_dates": {
                "invoice_date": state["invoice_payload"]["invoice_date"],
                "due_date": state["invoice_payload"]["due_date"]
            }
        }
    }
