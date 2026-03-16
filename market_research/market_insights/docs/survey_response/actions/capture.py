"""Action handler seed for survey_response:capture."""

from __future__ import annotations


DOC_ID = "survey_response"
ACTION_ID = "capture"
ACTION_RULE = {'allowed_in_states': ['received', 'validated'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'investigate market questions, collect evidence, and publish usable commercial insight', 'actors': ['researcher', 'analyst', 'marketing owner'], 'start_condition': 'a market-research question is defined', 'ordered_steps': ['Collect survey or interview responses.'], 'primary_actions': ['record', 'review'], 'primary_transitions': ['survey_response: active'], 'downstream_effects': ['supports product, pricing, sales, and campaign decisions'], 'action_actors': {'archive': ['marketing owner']}}

def handle_capture(payload: dict, context: dict | None = None) -> dict:
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
