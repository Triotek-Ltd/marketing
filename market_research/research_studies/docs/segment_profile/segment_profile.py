"""Doc runtime hooks for segment_profile."""

class DocRuntime:
    doc_key = "segment_profile"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'archive']
