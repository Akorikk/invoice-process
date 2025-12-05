#!/bin/bash

# Create subdirectories directly in the current location
echo "Creating subdirectories..."
mkdir -p app
mkdir -p nodes
mkdir -p tools
mkdir -p mcp
mkdir -p api

# Create files in the current directory
echo "Creating base files..."
touch main.py
touch workflow.json
touch README.md
touch requirements.txt

# Create files in app/
echo "Creating app/ files..."
touch app/__init__.py
touch app/graph_builder.py
touch app/state_manager.py
touch app/checkpoint_store.py

# Create files in nodes/
echo "Creating nodes/ files..."
touch nodes/intake.py
touch nodes/understand.py
touch nodes/prepare.py
touch nodes/retrieve.py
touch nodes/match_two_way.py
touch nodes/checkpoint_hitl.py
touch nodes/hitl_decision.py
touch nodes/reconcile.py
touch nodes/approve.py
touch nodes/posting.py
touch nodes/notify.py
touch nodes/complete.py

# Create files in tools/
echo "Creating tools/ files..."
touch tools/bigtool_picker.py
touch tools/ocr_tools.py
touch tools/enrichment_tools.py
touch tools/erp_tools.py
touch tools/db_tools.py
touch tools/email_tools.py

# Create files in mcp/
echo "Creating mcp/ files..."
touch mcp/common_client.py
touch mcp/atlas_client.py

# Create files in api/
echo "Creating api/ files..."
touch api/server.py
touch api/human_review.py

echo "Project structure created successfully in the current directory!"