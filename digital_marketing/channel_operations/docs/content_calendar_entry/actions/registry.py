"""Action registry seed for content_calendar_entry."""

from __future__ import annotations


DOC_ID = "content_calendar_entry"
ALLOWED_ACTIONS = ['create', 'review', 'approve', 'schedule', 'publish', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['draft', 'approved', 'scheduled', 'published'], 'transitions_to': None}, 'review': {'allowed_in_states': ['draft', 'approved', 'scheduled', 'published'], 'transitions_to': None}, 'approve': {'allowed_in_states': ['draft', 'approved', 'scheduled', 'published'], 'transitions_to': 'approved'}, 'schedule': {'allowed_in_states': ['draft', 'approved', 'scheduled', 'published'], 'transitions_to': None}, 'publish': {'allowed_in_states': ['draft', 'approved', 'scheduled', 'published'], 'transitions_to': 'published'}, 'archive': {'allowed_in_states': ['draft', 'approved', 'scheduled', 'published'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'

def get_action_handler_name(action_id: str) -> str:
    return f"handle_{action_id}"

def get_action_module_path(action_id: str) -> str:
    return f"actions/{action_id}.py"

def action_contract(action_id: str) -> dict:
    return {
        "state_field": STATE_FIELD,
        "rule": ACTION_RULES.get(action_id, {}),
    }
