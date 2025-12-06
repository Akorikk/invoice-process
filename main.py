import argparse
from app.graph_builder import build_graph
import uvicorn
import json
from api.server import app


def run_workflow(invoice_payload):
    print("\n================ INVOICE WORKFLOW STARTED ================\n")

    graph = build_graph()   # start from INTAKE
    state = {"invoice_payload": invoice_payload}

    result = graph.invoke(state)

    print("\n================ WORKFLOW PAUSED / FINISHED ================\n")
    print(json.dumps(result, indent=2))

    return result


def resume_workflow(state_file):
    print("\n================ RESUMING WORKFLOW ================\n")

    # Load saved state (from checkpoint)
    state = json.load(open(state_file))

    # Resume from RECONCILE
    graph = build_graph(resume_stage="RECONCILE")

    result = graph.invoke(state)

    print("\n================ WORKFLOW COMPLETED ================\n")
    print(json.dumps(result, indent=2))


def start_api():
    print("\nStarting HITL API server at http://127.0.0.1:8000\n")
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--resume", type=str, help="Resume workflow using checkpoint state file")
    parser.add_argument("--api", action="store_true", help="Start HITL API server only")
    args = parser.parse_args()

    # Start API only
    if args.api:
        start_api()
        exit()

    # Resume mode
    if args.resume:
        resume_workflow(args.resume)
        exit()

    # -------- NORMAL START MODE --------
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

    result = run_workflow(sample_invoice)

    
    if "match_result" in result and result["match_result"] == "FAILED":
        with open("checkpoint_state.json", "w") as f:
            json.dump(result, f, indent=2)
        print("\nCheckpoint saved to checkpoint_state.json")
        print("Waiting for HITL decision...")
