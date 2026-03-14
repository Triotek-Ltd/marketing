"""Doc runtime hooks for market_insight."""

class DocRuntime:
    doc_key = "market_insight"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'publish', 'archive']
