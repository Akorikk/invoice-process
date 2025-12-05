# tools/bigtool_picker.py

import random

class BigtoolPicker:
    """
    Select tools dynamically from predefined pools.
    This is MOCKED but behaves realistically.
    """

    TOOL_POOLS = {
        "ocr": ["google_vision", "tesseract", "aws_textract"],
        "enrichment": ["clearbit", "people_data_labs", "vendor_db"],
        "erp_connector": ["sap_sandbox", "netsuite", "mock_erp"],
        "db": ["sqlite", "postgres", "dynamodb"],
        "email": ["sendgrid", "smartlead", "ses"]
    }

    @staticmethod
    def select(capability: str, context: dict = None):
        """
        Pick a tool based on capability.
        Uses random selection for simulation.
        """
        pool = BigtoolPicker.TOOL_POOLS.get(capability, [])
        if not pool:
            raise ValueError(f"No tool pool found for capability: {capability}")

        selected_tool = random.choice(pool)
        print(f"[Bigtool] Selected '{selected_tool}' for capability '{capability}'")

        return selected_tool
