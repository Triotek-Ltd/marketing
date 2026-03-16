"""Workflow service seed for pricing_decision."""

from __future__ import annotations


DOC_ID = "pricing_decision"
ARCHETYPE = "transaction"
INITIAL_STATE = 'draft'
STATES = ['draft', 'reviewed', 'approved', 'effective', 'archived']
TERMINAL_STATES = ['archived']
ACTION_RULES = {'create': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'effective'], 'transitions_to': None}, 'review': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'effective'], 'transitions_to': 'reviewed'}, 'approve': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'effective'], 'transitions_to': 'approved'}, 'reject': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'effective'], 'transitions_to': None}, 'activate': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'effective'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'effective'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'govern product lifecycle, pricing decisions, and catalog changes in a controlled way', 'actors': ['product manager', 'pricing owner', 'approver'], 'start_condition': 'a product is launched, updated, or repositioned', 'ordered_steps': ['Decide pricing for the product state.'], 'primary_actions': ['create', 'review', 'approve'], 'primary_transitions': ['pricing_decision: draft -> approved -> active'], 'downstream_effects': ['feeds sales materials, catalog publication, and forecast planning'], 'action_actors': {'create': ['product manager'], 'review': ['pricing owner'], 'approve': ['approver'], 'reject': ['approver'], 'activate': ['pricing owner'], 'archive': ['pricing owner']}}

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
        return rule.get("transitions_to")

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
        return {'mode': 'transaction_flow', 'supports_submission': True}
