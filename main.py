# main.py

from app.graph_builder import build_graph
from app.state_manager import StateManager
from api.server import app
import uvicorn

def run_workflow(invoice_payload):

    print("\n================ INVOICE WORKFLOW STARTED ================\n")

    graph = build_graph()

    state = {"invoice_payload": invoice_payload}

    result = graph.invoke(state)

    print("\n================ WORKFLOW FINISHED ================\n")
    print(result)

    return result


if __name__ == "__main__":

    sample_invoice = {
        "invoice_id": "INV-001",
        "vendor_name": "Acme Corporation",
        "vendor_tax_id": "GST1234",
        "invoice_date": "2024-10-01",
        "due_date": "2024-10-15",
        "amount": 500,
        "currency": "USD",
        "line_items": [],
        "attachments": ["invoice_image.png"]
    }

    # Run the workflow
    run_workflow(sample_invoice)

    # Start API server in parallel (you can run separately)
    print("\nStarting HITL API server at http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)
