"""Doc runtime hooks for lead_capture_record."""

class DocRuntime:
    doc_key = "lead_capture_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'qualify', 'discard', 'archive']
