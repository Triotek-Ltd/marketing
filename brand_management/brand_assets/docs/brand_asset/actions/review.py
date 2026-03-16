"""Action handler seed for brand_asset:review."""

from __future__ import annotations


DOC_ID = "brand_asset"
ACTION_ID = "review"
ACTION_RULE = {'allowed_in_states': ['draft', 'approved', 'active'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'maintain brand identity standards and control the assets released under the brand', 'actors': ['brand owner', 'designer', 'reviewer'], 'start_condition': 'a brand asset or guideline update is needed', 'ordered_steps': ['Create and review brand assets.', 'Release the approved asset set for use.'], 'primary_actions': ['create', 'review', 'approve', 'reject', 'publish', 'archive'], 'primary_transitions': ['brand_asset: draft -> in_review -> approved or rejected', 'brand_asset: approved -> active'], 'downstream_effects': ['supports campaigns, product marketing, and external communications'], 'action_actors': {'create': ['brand owner'], 'review': ['reviewer'], 'approve': ['reviewer'], 'archive': ['brand owner']}}

def handle_review(payload: dict, context: dict | None = None) -> dict:
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
