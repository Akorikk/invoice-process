""""
from langgraph.graph import StateGraph, END

from nodes.intake import intake_node
from nodes.understand import understand_node
from nodes.prepare import prepare_node
from nodes.retrieve import retrieve_node
from nodes.match_two_way import match_two_way_node
from nodes.checkpoint_hitl import checkpoint_node
from nodes.hitl_decision import hitl_node
from nodes.reconcile import reconcile_node
from nodes.approve import approve_node
from nodes.posting import posting_node
from nodes.notify import notify_node
from nodes.complete import complete_node


def build_graph(resume_stage=None):

    resume_stage:
        - None  -> Normal run (start at INTAKE)
        - 'RECONCILE' -> Resume HITL flow (skip earlier steps)
   

    workflow = StateGraph(dict)

    # ⭐ DEFAULT entry point = INTAKE
    entry = "INTAKE"

    # ⭐ If resuming after HITL, skip all early stages
    if resume_stage is not None:
        print(f"[GRAPH] Resuming workflow at: {resume_stage}")
        entry = resume_stage

    workflow.set_entry_point(entry)

    # Register nodes
    workflow.add_node("INTAKE", intake_node)
    workflow.add_node("UNDERSTAND", understand_node)
    workflow.add_node("PREPARE", prepare_node)
    workflow.add_node("RETRIEVE", retrieve_node)
    workflow.add_node("MATCH_TWO_WAY", match_two_way_node)
    workflow.add_node("CHECKPOINT_HITL", checkpoint_node)
    workflow.add_node("HITL_DECISION", hitl_node)
    workflow.add_node("RECONCILE", reconcile_node)
    workflow.add_node("APPROVE", approve_node)
    workflow.add_node("POSTING", posting_node)
    workflow.add_node("NOTIFY", notify_node)
    workflow.add_node("COMPLETE", complete_node)

    # Deterministic edges
    workflow.add_edge("INTAKE", "UNDERSTAND")
    workflow.add_edge("UNDERSTAND", "PREPARE")
    workflow.add_edge("PREPARE", "RETRIEVE")
    workflow.add_edge("RETRIEVE", "MATCH_TWO_WAY")

    # Conditional branching
    workflow.add_conditional_edges(
        "MATCH_TWO_WAY",
        lambda state: "CHECKPOINT_HITL" if state["match_result"] == "FAILED" else "RECONCILE",
        {
            "CHECKPOINT_HITL": "CHECKPOINT_HITL",
            "RECONCILE": "RECONCILE"
        }
    )

    # HITL pauses workflow
    workflow.add_edge("CHECKPOINT_HITL", END)

    # Resume workflow path
    workflow.add_edge("RECONCILE", "APPROVE")
    workflow.add_edge("APPROVE", "POSTING")
    workflow.add_edge("POSTING", "NOTIFY")
    workflow.add_edge("NOTIFY", "COMPLETE")

    return workflow.compile()

"""""

# app/graph_builder.py

from langgraph.graph import StateGraph, END

from nodes.intake import intake_node
from nodes.understand import understand_node
from nodes.prepare import prepare_node
from nodes.retrieve import retrieve_node
from nodes.match_two_way import match_two_way_node
from nodes.checkpoint_hitl import checkpoint_node
from nodes.hitl_decision import hitl_node
from nodes.reconcile import reconcile_node
from nodes.approve import approve_node
from nodes.posting import posting_node
from nodes.notify import notify_node
from nodes.complete import complete_node


def build_graph(resume_stage=None):
    """
    resume_stage controls where the workflow should start:
        - None          → Start normally from INTAKE
        - "RECONCILE"   → Resume after human decision
    """

    workflow = StateGraph(dict)

    # Default entry point
    entry = "INTAKE"

    # Resume logic
    if resume_stage is not None:
        print(f"[GRAPH] Resuming workflow at: {resume_stage}")
        entry = resume_stage

    workflow.set_entry_point(entry)

    # Register nodes
    workflow.add_node("INTAKE", intake_node)
    workflow.add_node("UNDERSTAND", understand_node)
    workflow.add_node("PREPARE", prepare_node)
    workflow.add_node("RETRIEVE", retrieve_node)
    workflow.add_node("MATCH_TWO_WAY", match_two_way_node)
    workflow.add_node("CHECKPOINT_HITL", checkpoint_node)
    workflow.add_node("HITL_DECISION", hitl_node)
    workflow.add_node("RECONCILE", reconcile_node)
    workflow.add_node("APPROVE", approve_node)
    workflow.add_node("POSTING", posting_node)
    workflow.add_node("NOTIFY", notify_node)
    workflow.add_node("COMPLETE", complete_node)

    # Normal path
    workflow.add_edge("INTAKE", "UNDERSTAND")
    workflow.add_edge("UNDERSTAND", "PREPARE")
    workflow.add_edge("PREPARE", "RETRIEVE")
    workflow.add_edge("RETRIEVE", "MATCH_TWO_WAY")

    # Conditional pause for HITL
    workflow.add_conditional_edges(
        "MATCH_TWO_WAY",
        lambda state: "CHECKPOINT_HITL" if state["match_result"] == "FAILED" else "RECONCILE",
        {
            "CHECKPOINT_HITL": "CHECKPOINT_HITL",
            "RECONCILE": "RECONCILE"
        }
    )

    # HITL ends workflow temporarily
    workflow.add_edge("CHECKPOINT_HITL", END)

    # Resume path
    workflow.add_edge("RECONCILE", "APPROVE")
    workflow.add_edge("APPROVE", "POSTING")
    workflow.add_edge("POSTING", "NOTIFY")
    workflow.add_edge("NOTIFY", "COMPLETE")

    return workflow.compile()
