"""Doc runtime hooks for campaign_record."""

class DocRuntime:
    doc_key = "campaign_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'approve', 'launch', 'pause', 'close', 'archive']
