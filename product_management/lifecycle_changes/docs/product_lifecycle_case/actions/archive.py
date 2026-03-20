"""Action handler seed for product_lifecycle_case:archive."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "product_lifecycle_case"
ACTION_ID = "archive"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['proposed', 'in_review', 'approved', 'in_progress', 'completed', 'cancelled'], 'transitions_to': 'archived'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'govern product lifecycle, pricing decisions, and catalog changes in a controlled way', 'actors': ['product manager', 'pricing owner', 'approver'], 'start_condition': 'a product is launched, updated, or repositioned', 'ordered_steps': ['Route launch or change requests through lifecycle control.'], 'primary_actions': ['create', 'assign', 'approve', 'close'], 'primary_transitions': ['product_lifecycle_case: opened -> in_review -> approved -> closed'], 'downstream_effects': ['feeds sales materials, catalog publication, and forecast planning'], 'action_actors': {'create': ['product manager'], 'review': ['pricing owner'], 'approve': ['approver'], 'activate': ['pricing owner'], 'close': ['pricing owner'], 'cancel': ['pricing owner'], 'archive': ['pricing owner']}}

def handle_archive(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = cast(str | None, ACTION_RULE.get("transitions_to"))
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
