"""Action handler seed for campaign_result:record."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "campaign_result"
ACTION_ID = "record"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['open', 'reviewed', 'finalized'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'plan, approve, launch, and monitor promotional campaigns against budget and objectives', 'actors': ['campaign owner', 'approver', 'analyst'], 'start_condition': 'a campaign objective and budget are approved', 'ordered_steps': ['Capture campaign results and performance review.'], 'primary_actions': ['record', 'review', 'close'], 'primary_transitions': ['campaign_result: active -> reviewed -> closed'], 'downstream_effects': ['supports digital execution, brand review, and revenue analysis'], 'action_actors': {'record': ['campaign owner'], 'review': ['analyst'], 'archive': ['campaign owner']}}

def handle_record(payload: dict, context: dict | None = None) -> dict:
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
