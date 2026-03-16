"""Action handler seed for catalog_change:record."""

from __future__ import annotations


DOC_ID = "catalog_change"
ACTION_ID = "record"
ACTION_RULE = {'allowed_in_states': ['active'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'govern product lifecycle, pricing decisions, and catalog changes in a controlled way', 'actors': ['product manager', 'pricing owner', 'approver'], 'start_condition': 'a product is launched, updated, or repositioned', 'ordered_steps': ['Publish catalog changes.'], 'primary_actions': ['create', 'approve', 'publish', 'close'], 'primary_transitions': ['catalog_change: draft -> approved -> published -> closed'], 'downstream_effects': ['feeds sales materials, catalog publication, and forecast planning'], 'action_actors': {'record': ['product manager'], 'review': ['pricing owner'], 'archive': ['pricing owner']}}

def handle_record(payload: dict, context: dict | None = None) -> dict:
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
