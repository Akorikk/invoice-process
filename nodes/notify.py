from tools.bigtool_picker import BigtoolPicker

def notify_node(state: dict):
    print("\n--- [NOTIFY] Sending Notifications ---")

    email_tool = BigtoolPicker.select("email")
    print(f"[NOTIFY] Email tool selected: {email_tool}")

    return {
        **state,
        "notify_status": {"email": "SENT", "slack": "SENT"},
        "notified_parties": ["vendor", "finance_team"]
    }

