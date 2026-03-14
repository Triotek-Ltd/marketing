"""Doc runtime hooks for content_calendar_entry."""

class DocRuntime:
    doc_key = "content_calendar_entry"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'approve', 'schedule', 'publish', 'archive']
