"""Doc runtime hooks for pricing_decision."""

class DocRuntime:
    doc_key = "pricing_decision"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'approve', 'reject', 'activate', 'archive']
