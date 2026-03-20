"""Action registry seed for campaign_result."""

from __future__ import annotations

from typing import Any


DOC_ID = "campaign_result"
ALLOWED_ACTIONS = ['record', 'review', 'finalize', 'archive']
ACTION_RULES: dict[str, dict[str, Any]] = {'record': {'allowed_in_states': ['open', 'reviewed', 'finalized'], 'transitions_to': None}, 'review': {'allowed_in_states': ['open', 'reviewed', 'finalized'], 'transitions_to': 'reviewed'}, 'finalize': {'allowed_in_states': ['open', 'reviewed', 'finalized'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['open', 'reviewed', 'finalized'], 'transitions_to': 'archived'}}

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
