from mcp.common_client import CommonClient

def match_two_way_node(state: dict):
    print("\n--- [MATCH_TWO_WAY] Matching Invoice vs PO ---")

    common = CommonClient()
    score = common.compute_match_score(state, state["matched_pos"])

    match_result = "MATCHED" if score >= 0.90 else "FAILED"

    print(f"[MATCH_TWO_WAY] match_score={score}, result={match_result}")

    return {
        **state,
        "match_score": score,
        "match_result": match_result,
        "tolerance_pct": 5,
        "match_evidence": {"source": "simple_match_mock"}
    }
