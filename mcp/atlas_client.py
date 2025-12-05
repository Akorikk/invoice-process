# mcp/atlas_client.py

class AtlasClient:
    """
    Simulated ATLAS external server.
    """

    def enrich_vendor(self, vendor_name):
        return {
            "tax_id": "GST1234",
            "credit_score": 720
        }

    def fetch_po(self, invoice_id):
        return [{"po_id": "PO-7788", "amount": 1000}]

    def fetch_grn(self, invoice_id):
        return [{"grn_id": "GRN-8822"}]

    def fetch_history(self, vendor_name):
        return [{"invoice": "Prev123", "amount": 500}]
