"""Doc runtime hooks for brand_guideline."""

class DocRuntime:
    doc_key = "brand_guideline"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'publish', 'archive']
