"""Action registry seed for product_lifecycle_case."""

from __future__ import annotations

from typing import Any


DOC_ID = "product_lifecycle_case"
ALLOWED_ACTIONS = ['create', 'review', 'approve', 'activate', 'close', 'cancel', 'archive']
ACTION_RULES: dict[str, dict[str, Any]] = {'create': {'allowed_in_states': ['proposed', 'in_review', 'approved', 'in_progress', 'completed', 'cancelled'], 'transitions_to': None}, 'review': {'allowed_in_states': ['proposed', 'in_review', 'approved', 'in_progress', 'completed', 'cancelled'], 'transitions_to': 'in_review'}, 'approve': {'allowed_in_states': ['proposed', 'in_review', 'approved', 'in_progress', 'completed', 'cancelled'], 'transitions_to': 'approved'}, 'activate': {'allowed_in_states': ['proposed', 'in_review', 'approved', 'in_progress', 'completed', 'cancelled'], 'transitions_to': None}, 'close': {'allowed_in_states': ['proposed', 'in_review', 'approved', 'in_progress', 'completed', 'cancelled'], 'transitions_to': None}, 'cancel': {'allowed_in_states': ['proposed', 'in_review', 'approved', 'in_progress', 'completed', 'cancelled'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['proposed', 'in_review', 'approved', 'in_progress', 'completed', 'cancelled'], 'transitions_to': 'archived'}}

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
