# app/graph_builder.py

from langgraph.graph import StateGraph, END
from app.state_manager import StateManager

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


def build_graph():
    workflow = StateGraph(dict)

    workflow.set_entry_point("INTAKE")

    # register all nodes
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

    # define deterministic flow
    workflow.add_edge("INTAKE", "UNDERSTAND")
    workflow.add_edge("UNDERSTAND", "PREPARE")
    workflow.add_edge("PREPARE", "RETRIEVE")
    workflow.add_edge("RETRIEVE", "MATCH_TWO_WAY")

    # conditional branch
    workflow.add_conditional_edges(
        "MATCH_TWO_WAY",
        lambda state: "CHECKPOINT_HITL" if state["match_result"] == "FAILED" else "RECONCILE",
        {
            "CHECKPOINT_HITL": "CHECKPOINT_HITL",
            "RECONCILE": "RECONCILE"
        }
    )

    workflow.add_edge("CHECKPOINT_HITL", END)  # HITL is async

    workflow.add_edge("RECONCILE", "APPROVE")
    workflow.add_edge("APPROVE", "POSTING")
    workflow.add_edge("POSTING", "NOTIFY")
    workflow.add_edge("NOTIFY", "COMPLETE")

    return workflow.compile()
