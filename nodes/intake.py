from tools.bigtool_picker import BigtoolPicker
import datetime, uuid

def intake_node(state: dict):
    print("\n--- [INTAKE] Starting Invoice Intake Stage ---")

    invoice = state.get("invoice_payload")

    # Basic validation
    required_fields = ["invoice_id", "vendor_name", "amount"]
    for field in required_fields:
        if field not in invoice:
            raise ValueError(f"Missing required field: {field}")

    storage_tool = BigtoolPicker.select("storage") if "storage" in BigtoolPicker.TOOL_POOLS else "local_fs"
    print(f"[INTAKE] Storage tool selected: {storage_tool}")

    ingest_ts = datetime.datetime.utcnow().isoformat()
    raw_id = f"raw-{uuid.uuid4()}"

    print(f"[INTAKE] Invoice {invoice['invoice_id']} successfully validated and ingested.")

    return {
        **state,
        "raw_id": raw_id,
        "ingest_ts": ingest_ts,
        "validated": True
    }
