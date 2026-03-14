"""Action handler seed for brand_guideline:archive."""

from __future__ import annotations


DOC_ID = "brand_guideline"
ACTION_ID = "archive"
ACTION_RULE = {'allowed_in_states': ['draft', 'approved', 'published'], 'transitions_to': 'archived'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'maintain brand identity standards and control the assets released under the brand', 'actors': ['brand owner', 'designer', 'reviewer'], 'start_condition': 'a brand asset or guideline update is needed', 'ordered_steps': ['Publish or revise the brand guideline set.'], 'primary_actions': ['create', 'approve', 'publish'], 'primary_transitions': ['brand_guideline: draft -> approved -> active'], 'downstream_effects': ['supports campaigns, product marketing, and external communications']}

def handle_archive(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = ACTION_RULE.get("transitions_to")
    updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
    return {
        "doc_id": DOC_ID,
        "action_id": ACTION_ID,
        "payload": payload,
        "context": context,
        "allowed_in_states": ACTION_RULE.get("allowed_in_states", []),
        "next_state": next_state,
        "updates": updates,
        "workflow_objective": WORKFLOW_HINTS.get("business_objective"),
    }
