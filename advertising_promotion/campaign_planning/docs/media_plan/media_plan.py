"""Doc runtime hooks for media_plan."""

class DocRuntime:
    doc_key = "media_plan"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'approve', 'activate', 'close', 'archive']
