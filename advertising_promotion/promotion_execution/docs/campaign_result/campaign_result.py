"""Doc runtime hooks for campaign_result."""

class DocRuntime:
    doc_key = "campaign_result"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'review', 'finalize', 'archive']
