"""Action handler seed for segment_profile:update."""

from __future__ import annotations


DOC_ID = "segment_profile"
ACTION_ID = "update"
ACTION_RULE = {'allowed_in_states': ['active'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'investigate market questions, collect evidence, and publish usable commercial insight', 'actors': ['researcher', 'analyst', 'marketing owner'], 'start_condition': 'a market-research question is defined', 'ordered_steps': ['Open the study and define the target segment.'], 'primary_actions': ['create', 'review', 'approve'], 'primary_transitions': ['segment_profile: draft -> active'], 'downstream_effects': ['supports product, pricing, sales, and campaign decisions']}

def handle_update(payload: dict, context: dict | None = None) -> dict:
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
