"""Doc runtime hooks for brand_campaign_brief."""

class DocRuntime:
    doc_key = "brand_campaign_brief"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'approve', 'activate', 'archive']
