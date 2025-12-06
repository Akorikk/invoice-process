# My Intro
* Hi my name is Abhishek Kori i am AI/ML Engineer and Data Scientist with over three years of experience building advanced machine learning, RAG, and generative AI systems.

* I specialize in LLMs, NLP, and modern MLOps, and I work extensively with the latest AI agent frameworks including LangChain, LangGraph, LangSmith, and Microsoft AutoGen, where I design multi-AI-agent workflows that can reason, collaborate, and automate complex tasks.

* Also i woul not say experience but i have good amount of study in building LLM and SLM from scratch. i have writen artical on medium of my study on LLM have a look if you have any intrest in my study unterstanding --> https://medium.com/@code2ai

* I'm currently working on an AI project to develop a chatbot integrated with Retrieval Augmented Generation (RAG) technology, tailored for university use. This chatbot will serve as a comprehensive resource, providing detailed information on colleges, teachers, faculty members, and much more. It will proactively notify students about upcoming exams, events, and teacher related updates. Additionally, students can learn any subject such as math by simply uploading PDFs or other materials, and the chatbot will generate visualizations to help explain concepts more effectively for better understanding. The system will include many other features to enhance the educational experience.


# About Assignmnet 

* This project implements a 12-stage autonomous AI agent pipeline that reads invoices, extracts data, validates, matches them against Purchase Orders (PO), enriches vendor data, interacts with ERP connectors, and posts accounting entries.

The system automatically chooses the best OCR, ERP, and enrichment tools using a dynamic tool-selector, and pauses only when a matching error requires Human-In-The-Loop (HITL) approval.

# Folder Structure
invoice-process/
│
├── api/
│   ├── server.py               → FastAPI app
│   └── human_review.py         → HITL endpoints
│
├── app/
│   ├── graph_builder.py        → Builds 12-stage workflow
│   ├── checkpoint_store.py     → SQLite checkpoint manager
│   └── state_manager.py        → Updates workflow state
│
├── nodes/                      → All workflow task nodes
│   ├── intake.py
│   ├── understand.py
│   ├── prepare.py
│   ├── retrieve.py
│   ├── match_two_way.py
│   ├── checkpoint_hitl.py
│   ├── hitl_decision.py
│   ├── reconcile.py
│   ├── approve.py
│   ├── posting.py
│   ├── notify.py
│   └── complete.py
│
├── tools/
│   └── bigtool_picker.py       → Random tool selector
│
├── mcp/
│   ├── common_client.py        → Normalization + flags + matching
│   └── atlas_client.py         → Vendor enrichment + PO/GRN fetch
│
├── checkpoint_state.json       → Saved workflow state (auto)
├── checkpoints.db              → HITL database
├── main.py                     → Run workflow manually
└── test_workflow.py            → Full automated demo


# Key Features
* ✅ 12-Stage End-to-End Agentic Workflow
1. Intake
2. Understand (OCR)
3. Prepare (Normalization + Enrichment)
4. Retrieve (PO / GRN / History)
5. Two-Way Match
6. Checkpoint HITL Pause
7. HITL Decision
8. Reconcile
9. Approve
10. Posting (ERP)
11. Notify
12. Complete


# 🤖 Dynamic Multi-Tool Selection

Tools are selected automatically:
OCR → Google Vision / AWS Textract / Tesseract
ERP Connector → SAP Sandbox / Netsuite / Mock ERP
Email → SendGrid / SES / Smartlead
Data Enrichment → PDL / Clearbit / Vendor DB
This simulates real-world autonomous multi-agent behaviour.


# 🧑‍💼 Human-In-The-Loop (HITL) Approval
If the invoice fails PO matching:
the workflow pauses
data is saved to SQLite
a reviewer must approve/reject via REST API
workflow resumes automatically

# 📡 FastAPI Server for HITL
The project exposes:
GET /human-review/pending → list pending invoices
POST /human-review/decision → submit ACCEPT / REJECT

# 🧪 Automated Demo Script Included
Run test_workflow.py to:
execute full workflow
trigger HITL
automatically approve invoice
resume workflow
complete invoice posting
Perfect for demos or video recording.

# 🚀 How to Run the Project

python main.py
This executes all 12 stages until the HITL checkpoint. After a failed PO match, the system generates: checkpoint_state.json

* Start HITL API Server by running 
python main.py --api

* View Pending Human Reviews
 run in browser --> http://127.0.0.1:8000/human-review/pending
 Example output: {
  "items": [
    {
      "checkpoint_id": 10,
      "invoice_id": "INV-001",
      "review_url": "/human-review/review/INV-001",
      "reason_for_hold": "MATCH_FAILED"
    }
  ]
}

* Submit Human Decision
curl -X POST "http://127.0.0.1:8000/human-review/decision" ^
-H "Content-Type: application/json" ^
-d "{\"checkpoint_id\": 10, \"decision\": \"ACCEPT\", \"reviewer_id\": \"demo_user\"}"

API response includes the resume token and file:
{
  "resume_token": "resume-10-token",
  "next_stage": "RECONCILE",
  "resume_file": "checkpoint_state_10.json"
}

* Resume Workflow
python main.py --resume checkpoint_state_10.json

Workflow now runs the remaining stages:

Reconcile

Approval

Posting

Notification

Completion

Final output contains:

"status": "COMPLETE"
