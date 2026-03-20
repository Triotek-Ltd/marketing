"""Workflow service seed for product_lifecycle_case."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "product_lifecycle_case"
ARCHETYPE = "workflow_case"
INITIAL_STATE = 'proposed'
STATES = ['proposed', 'in_review', 'approved', 'in_progress', 'completed', 'cancelled', 'archived']
TERMINAL_STATES = ['archived']
ACTION_RULES: dict[str, dict[str, Any]] = {'create': {'allowed_in_states': ['proposed', 'in_review', 'approved', 'in_progress', 'completed', 'cancelled'], 'transitions_to': None}, 'review': {'allowed_in_states': ['proposed', 'in_review', 'approved', 'in_progress', 'completed', 'cancelled'], 'transitions_to': 'in_review'}, 'approve': {'allowed_in_states': ['proposed', 'in_review', 'approved', 'in_progress', 'completed', 'cancelled'], 'transitions_to': 'approved'}, 'activate': {'allowed_in_states': ['proposed', 'in_review', 'approved', 'in_progress', 'completed', 'cancelled'], 'transitions_to': None}, 'close': {'allowed_in_states': ['proposed', 'in_review', 'approved', 'in_progress', 'completed', 'cancelled'], 'transitions_to': None}, 'cancel': {'allowed_in_states': ['proposed', 'in_review', 'approved', 'in_progress', 'completed', 'cancelled'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['proposed', 'in_review', 'approved', 'in_progress', 'completed', 'cancelled'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'govern product lifecycle, pricing decisions, and catalog changes in a controlled way', 'actors': ['product manager', 'pricing owner', 'approver'], 'start_condition': 'a product is launched, updated, or repositioned', 'ordered_steps': ['Route launch or change requests through lifecycle control.'], 'primary_actions': ['create', 'assign', 'approve', 'close'], 'primary_transitions': ['product_lifecycle_case: opened -> in_review -> approved -> closed'], 'downstream_effects': ['feeds sales materials, catalog publication, and forecast planning'], 'action_actors': {'create': ['product manager'], 'review': ['pricing owner'], 'approve': ['approver'], 'activate': ['pricing owner'], 'close': ['pricing owner'], 'cancel': ['pricing owner'], 'archive': ['pricing owner']}}

class WorkflowService:
    def allowed_actions_for_state(self, state: str | None) -> list[str]:
        if not state:
            return list(ACTION_RULES.keys())
        allowed = []
        for action_id, rule in ACTION_RULES.items():
            states = rule.get("allowed_in_states") or []
            if not states or state in states:
                allowed.append(action_id)
        return allowed

    def is_action_allowed(self, action_id: str, state: str | None) -> bool:
        return action_id in self.allowed_actions_for_state(state)

    def next_state_for(self, action_id: str) -> str | None:
        rule = ACTION_RULES.get(action_id, {})
        return cast(str | None, rule.get("transitions_to"))

    def apply_action(self, action_id: str, state: str | None) -> dict:
        if not self.is_action_allowed(action_id, state):
            raise ValueError(f"Action '{action_id}' is not allowed in state '{state}'")
        next_state = self.next_state_for(action_id)
        updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
        return {
            "action_id": action_id,
            "current_state": state,
            "next_state": next_state,
            "updates": updates,
        }

    def is_terminal(self, state: str | None) -> bool:
        return bool(state and state in TERMINAL_STATES)

    def workflow_summary(self) -> dict:
        return {
            "initial_state": INITIAL_STATE,
            "states": STATES,
            "terminal_states": TERMINAL_STATES,
            "business_objective": WORKFLOW_HINTS.get("business_objective"),
            "ordered_steps": WORKFLOW_HINTS.get("ordered_steps", []),
        }

    def workflow_profile(self) -> dict:
        return {'mode': 'case_flow', 'supports_assignment': True, 'supports_escalation': True}
