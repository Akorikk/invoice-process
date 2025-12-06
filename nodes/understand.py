# nodes/understand.py

from tools.bigtool_picker import BigtoolPicker

def understand_node(state: dict):
    print("\n--- [UNDERSTAND] Starting OCR + Parsing Stage ---")

    # Select OCR tool
    ocr_tool = BigtoolPicker.select("ocr")
    print(f"[UNDERSTAND] OCR provider selected: {ocr_tool}")

    # Mock OCR extraction
    print("[UNDERSTAND] OCR extracted text: Mock OCR text extracted from invoice image....")

    parsed_data = {
        "invoice_text": "Mock OCR text extracted from invoice image...",
        "parsed_line_items": [
            {"desc": "Item A", "qty": 2, "unit_price": 100, "total": 200},
            {"desc": "Item B", "qty": 1, "unit_price": 300, "total": 300}
        ],
        "detected_pos": ["PO-7788"],
        "currency": state["invoice_payload"]["currency"],
        "parsed_dates": {
            "invoice_date": state["invoice_payload"]["invoice_date"],
            "due_date": state["invoice_payload"]["due_date"]
        }
    }

    print("[UNDERSTAND] Extracted line items and PO references successfully.")

    # ⭐ Merge with previous state so invoice_payload is preserved
    return {
        **state,
        "parsed_invoice": parsed_data
    }

