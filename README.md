# invoice-process

This repository is a LangGraph-style Invoice Processing demo implementing a 12-stage workflow with Human-In-The-Loop (HITL), Bigtool dynamic tool selection, and MCP client orchestration.

What is included
- LangGraph workflow builder: `app/graph_builder.py`
- Nodes for all stages: `nodes/*` (INTAKE → COMPLETE)
- Bigtool mock selector: `tools/bigtool_picker.py`
- MCP client mocks: `mcp/common_client.py`, `mcp/atlas_client.py`
- Checkpoint persistence: `app/checkpoint_store.py`
- HITL API endpoints: `api/human_review.py` + `api/server.py`
- Demo runner: `main.py` (runs workflow and starts API)
- Full workflow specification: `workflow.json`

Quick setup
1. Create a Python virtual environment & activate it (PowerShell):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Run the demo (this will execute the workflow with a sample invoice and start the HITL API server):

```powershell
python main.py
```

3. Inspect Human Review queue (while server running):

```powershell
curl http://127.0.0.1:8000/human-review/pending
```

4. Submit a human decision (example JSON):

```powershell
curl -X POST http://127.0.0.1:8000/human-review/decision -H "Content-Type: application/json" -d '{"checkpoint_id":1,"decision":"ACCEPT","notes":"Ok","reviewer_id":"rev-1"}'
```

Notes & mapping to assignment
- The full workflow spec (Appendix-1) is in `workflow.json`.
- Checkpoints are persisted to `checkpoints.db` by default (SQLite).
- Bigtool picks tools randomly from the defined pools; logs show choices.
- MCP clients are mocked to simulate COMMON/ATLAS abilities.

Submission checklist (recommended)
- Ensure `workflow.json` is present and up-to-date (done).
- Record a short demo video showing:
	- Running `main.py` and captured logs
	- Opening `/human-review/pending` and making a decision
	- Workflow resuming after decision
- Attach `workflow.json`, the repo link, and demo video link in your email submission.

If you want, I can:
- Run the demo here and capture output logs (if environment allows), or
- Add a small script to produce a demo log file and sanitized outputs for submission.

Enjoy — let me know which next step you want me to take.


runn 
python main.py
python main.py --api
python main.py --resume checkpoint_state.json

this project os about Build a 12-stage autonomous agent that reads invoices, extracts data, validates, matches with purchase orders, and posts to accounting systems — automatically choosing the best tools (OCR, ERP, enrichment, etc.) and pausing for a human only when something doesn’t match.

---
## Demo files added

- `demo/sample_invoice.json` — sample invoice payload for the demo.
- `demo/run_demo.ps1` — PowerShell demo runner: creates venv, starts API+workflow, queries the human-review endpoint, and auto-accepts the first checkpoint if present.
- `tests/test_hitl_flow.py` — pytest that validates HITL endpoints and posts a resume decision if a checkpoint exists.
- `scripts/validate_workflow.py` — small validator to ensure `workflow.json` contains required root keys.

Quick demo (PowerShell):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
.\demo\run_demo.ps1
```

Run tests:

```powershell
pytest -q
```
