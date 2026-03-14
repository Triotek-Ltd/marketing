"""Doc runtime hooks for research_study."""

class DocRuntime:
    doc_key = "research_study"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'approve', 'launch', 'close', 'archive']
