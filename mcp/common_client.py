# mcp/common_client.py

class CommonClient:
    """
    Simulated COMMON server.
    Used for normalization, flags, matching, etc.
    """

    def normalize_vendor(self, name):
        return name.strip().title()

    def compute_flags(self, invoice):
        return {
            "missing_info": [],
            "risk_score": 0.15
        }

    def compute_match_score(self, invoice, pos):
        return 0.65  # force HITL for demo
