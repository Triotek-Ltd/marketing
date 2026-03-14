"""Doc runtime hooks for product_record."""

class DocRuntime:
    doc_key = "product_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'archive']
