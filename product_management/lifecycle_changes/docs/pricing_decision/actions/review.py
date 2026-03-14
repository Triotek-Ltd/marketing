"""Action handler seed for pricing_decision:review."""

from __future__ import annotations


DOC_ID = "pricing_decision"
ACTION_ID = "review"
ACTION_RULE = {'allowed_in_states': ['draft', 'reviewed', 'approved', 'effective'], 'transitions_to': 'reviewed'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'govern product lifecycle, pricing decisions, and catalog changes in a controlled way', 'actors': ['product manager', 'pricing owner', 'approver'], 'start_condition': 'a product is launched, updated, or repositioned', 'ordered_steps': ['Decide pricing for the product state.'], 'primary_actions': ['create', 'review', 'approve'], 'primary_transitions': ['pricing_decision: draft -> approved -> active'], 'downstream_effects': ['feeds sales materials, catalog publication, and forecast planning']}

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
