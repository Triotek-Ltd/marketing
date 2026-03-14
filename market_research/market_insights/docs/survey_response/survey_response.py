"""Doc runtime hooks for survey_response."""

class DocRuntime:
    doc_key = "survey_response"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['capture', 'validate', 'archive']
