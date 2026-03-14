"""Doc runtime hooks for catalog_change."""

class DocRuntime:
    doc_key = "catalog_change"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'review', 'archive']
