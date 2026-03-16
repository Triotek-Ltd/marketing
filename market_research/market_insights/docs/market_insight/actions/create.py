"""Action handler seed for market_insight:create."""

from __future__ import annotations


DOC_ID = "market_insight"
ACTION_ID = "create"
ACTION_RULE = {'allowed_in_states': ['draft', 'reviewed', 'published'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'turn raw prospects into qualified leads with documented outreach and qualification evidence', 'actors': ['sales rep', 'sales manager', 'reviewer'], 'start_condition': 'a target customer or lead source is identified', 'ordered_steps': [], 'primary_actions': [], 'primary_transitions': [], 'downstream_effects': ['feeds opportunity, negotiation, and forecast workflows'], 'action_actors': {'create': ['sales rep'], 'review': ['reviewer'], 'publish': ['sales rep'], 'archive': ['sales manager']}}

def handle_create(payload: dict, context: dict | None = None) -> dict:
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
