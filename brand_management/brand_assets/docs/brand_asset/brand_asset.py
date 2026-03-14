"""Doc runtime hooks for brand_asset."""

class DocRuntime:
    doc_key = "brand_asset"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'approve', 'archive']
