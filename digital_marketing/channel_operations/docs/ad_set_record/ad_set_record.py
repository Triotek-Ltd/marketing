"""Doc runtime hooks for ad_set_record."""

class DocRuntime:
    doc_key = "ad_set_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'approve', 'launch', 'pause', 'archive']
