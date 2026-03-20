"""Action handler seed for campaign_record:approve."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "campaign_record"
ACTION_ID = "approve"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['draft', 'approved', 'active', 'paused', 'completed'], 'transitions_to': 'approved'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'plan, approve, launch, and monitor promotional campaigns against budget and objectives', 'actors': ['campaign owner', 'approver', 'analyst'], 'start_condition': 'a campaign objective and budget are approved', 'ordered_steps': ['Create the campaign record and objective.'], 'primary_actions': ['create', 'review', 'approve', 'launch', 'close'], 'primary_transitions': ['campaign_record: draft -> approved -> active -> completed'], 'downstream_effects': ['supports digital execution, brand review, and revenue analysis'], 'action_actors': {'create': ['campaign owner'], 'review': ['analyst'], 'approve': ['approver'], 'launch': ['campaign owner'], 'pause': ['campaign owner'], 'close': ['analyst', 'campaign owner'], 'archive': ['campaign owner']}}

def handle_approve(payload: dict, context: dict | None = None) -> dict:
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
