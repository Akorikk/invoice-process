# mcp/common_client.py

class CommonClient:
    """
    Simulated COMMON server for vendor normalization, flags, matching.
    """

    def normalize_vendor(self, name):
        return name.strip().title()

    def compute_flags(self, invoice):
        # Fake risk & missing info detection
        return {
            "missing_info": [],
            "risk_score": 0.15
        }

    def compute_match_score(self, state, po_list):
        # Fake forced failure to demonstrate HITL
        return 0.65   # < threshold = HITL triggered
