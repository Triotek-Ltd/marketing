"""Doc runtime hooks for promotion_offer."""

class DocRuntime:
    doc_key = "promotion_offer"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'approve', 'activate', 'expire', 'archive']
