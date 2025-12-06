# nodes/match_two_way.py

from mcp.common_client import CommonClient

def match_two_way_node(state: dict):
    print("\n--- [MATCH] Performing 2-Way Invoice Matching ---")

    common = CommonClient()

    score = common.compute_match_score(state["invoice_payload"], state["matched_pos"])
    print(f"[MATCH] Match score computed: {score}")

    threshold = 0.9  # force HITL for demo

    match_result = "FAILED" if score < threshold else "MATCHED"
    print(f"[MATCH] Result: {match_result}")

    return {
        "match_score": score,
        "match_result": match_result,
        "tolerance_pct": 5,
        "match_evidence": {"po_match": score}
    }
