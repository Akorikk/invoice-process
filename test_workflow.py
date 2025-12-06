# test_workflow.py

import subprocess
import json
import time
import requests
import os


def run_main_workflow():
    print("\n================ STEP 1: Running main workflow ================\n")

    # Run: python main.py
    process = subprocess.Popen(
        ["python", "main.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    output, _ = process.communicate()

    print(output)

    # Confirm that checkpoint_state.json was created
    if not os.path.exists("checkpoint_state.json"):
        print("\n❌ ERROR: No checkpoint was created. Matching may not have failed.\n")
        return False

    print("\n✅ Checkpoint created successfully!\n")
    return True


def start_api_server():
    print("\n================ STEP 2: Starting HITL API server ================\n")

    process = subprocess.Popen(
        ["python", "main.py", "--api"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    print("⏳ Waiting for API server to start...")
    time.sleep(3)

    return process


def list_pending():
    print("\n================ STEP 3: Fetching pending reviews ================\n")

    resp = requests.get("http://127.0.0.1:8000/human-review/pending")
    print(resp.json())

    items = resp.json().get("items", [])

    if not items:
        print("\n❌ No pending items found.\n")
        return None

    new_item = items[-1]
    print(f"\n✅ Found pending checkpoint: {new_item}\n")
    return new_item


def send_decision(checkpoint_id):
    print("\n================ STEP 4: Sending ACCEPT decision ================\n")

    payload = {
        "checkpoint_id": checkpoint_id,
        "decision": "ACCEPT",
        "reviewer_id": "test_user"
    }

    resp = requests.post(
        "http://127.0.0.1:8000/human-review/decision",
        json=payload
    )

    print(f"API Response: {resp.json()}\n")

    resume_file = resp.json().get("resume_file")
    return resume_file


def resume_workflow(resume_file):
    print("\n================ STEP 5: Resuming workflow ================\n")

    process = subprocess.Popen(
        ["python", "main.py", "--resume", resume_file],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    output, _ = process.communicate()
    print(output)

    print("\n🎉 WORKFLOW SUCCESSFULLY COMPLETED!\n")


if __name__ == "__main__":

    # Step 1: Run workflow
    if not run_main_workflow():
        exit()

    # Step 2: Start API server
    api_process = start_api_server()

    # Step 3: Fetch pending checkpoint
    checkpoint = list_pending()
    if not checkpoint:
        api_process.kill()
        exit()

    checkpoint_id = checkpoint["checkpoint_id"]

    # Step 4: Accept decision
    resume_file = send_decision(checkpoint_id)

    if resume_file is None:
        print("\n❌ ERROR: No resume file returned.\n")
        api_process.kill()
        exit()

    # Stop API before resume
    api_process.kill()
    time.sleep(1)

    # Step 5: Resume workflow
    resume_workflow(resume_file)
