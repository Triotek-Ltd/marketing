"""Doc runtime hooks for digital_channel."""

class DocRuntime:
    doc_key = "digital_channel"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'archive']
