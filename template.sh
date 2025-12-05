#!/bin/bash

# Define the root directory
ROOT_DIR="invoice_langgraph_agent"

# Create the root directory
echo "Creating root directory: $ROOT_DIR"
mkdir -p "$ROOT_DIR"

# Create subdirectories
echo "Creating subdirectories..."
mkdir -p "$ROOT_DIR/app"
mkdir -p "$ROOT_DIR/nodes"
mkdir -p "$ROOT_DIR/tools"
mkdir -p "$ROOT_DIR/mcp"
mkdir -p "$ROOT_DIR/api"

# Create files in the root directory
echo "Creating root files..."
touch "$ROOT_DIR/main.py"
touch "$ROOT_DIR/workflow.json"
touch "$ROOT_DIR/README.md"
touch "$ROOT_DIR/requirements.txt"

# Create files in app/
echo "Creating app/ files..."
touch "$ROOT_DIR/app/__init__.py"
touch "$ROOT_DIR/app/graph_builder.py"
touch "$ROOT_DIR/app/state_manager.py"
touch "$ROOT_DIR/app/checkpoint_store.py"

# Create files in nodes/
echo "Creating nodes/ files..."
touch "$ROOT_DIR/nodes/intake.py"
touch "$ROOT_DIR/nodes/understand.py"
touch "$ROOT_DIR/nodes/prepare.py"
touch "$ROOT_DIR/nodes/retrieve.py"
touch "$ROOT_DIR/nodes/match_two_way.py"
touch "$ROOT_DIR/nodes/checkpoint_hitl.py"
touch "$ROOT_DIR/nodes/hitl_decision.py"
touch "$ROOT_DIR/nodes/reconcile.py"
touch "$ROOT_DIR/nodes/approve.py"
touch "$ROOT_DIR/nodes/posting.py"
touch "$ROOT_DIR/nodes/notify.py"
touch "$ROOT_DIR/nodes/complete.py"

# Create files in tools/
echo "Creating tools/ files..."
touch "$ROOT_DIR/tools/bigtool_picker.py"
touch "$ROOT_DIR/tools/ocr_tools.py"
touch "$ROOT_DIR/tools/enrichment_tools.py"
touch "$ROOT_DIR/tools/erp_tools.py"
touch "$ROOT_DIR/tools/db_tools.py"
touch "$ROOT_DIR/tools/email_tools.py"

# Create files in mcp/
echo "Creating mcp/ files..."
touch "$ROOT_DIR/mcp/common_client.py"
touch "$ROOT_DIR/mcp/atlas_client.py"

# Create files in api/
echo "Creating api/ files..."
touch "$ROOT_DIR/api/server.py"
touch "$ROOT_DIR/api/human_review.py"

echo "Structure created successfully inside '$ROOT_DIR'!"