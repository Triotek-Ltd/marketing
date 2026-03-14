"""Doc runtime hooks for product_lifecycle_case."""

class DocRuntime:
    doc_key = "product_lifecycle_case"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'approve', 'activate', 'close', 'cancel', 'archive']
