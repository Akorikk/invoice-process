# nodes/notify.py

from tools.bigtool_picker import BigtoolPicker

def notify_node(state: dict):
    print("\n--- [NOTIFY] Sending Notifications ---")

    email_tool = BigtoolPicker.select("email")
    print(f"[NOTIFY] Email tool selected: {email_tool}")

    notify_status = {
        "vendor": "sent",
        "finance_team": "sent"
    }

    return {
        "notify_status": notify_status,
        "notified_parties": ["vendor", "finance_team"]
    }
