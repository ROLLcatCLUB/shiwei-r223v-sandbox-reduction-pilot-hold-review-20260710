# R223V review ledger default collapse policy

## Policy

Review ledger is required for audit but should not be open as a full right-side surface by default in a broader pilot.

## Default state

```json
{
  "review_ledger_default": "collapsed_summary",
  "full_ledger_open_requires": "reviewer_action",
  "teacher_default_draft_priority": "highest",
  "ledger_teacher_visible": false
}
```

## Summary fields allowed by default

- event count
- primary pattern count
- component status count
- screen/sheet/evidence mapping count
- teacher confirmation count

## Full ledger fields allowed after reviewer action

- unit_phase_role
- practice_intensity
- teacher_support_density
- primary_patterns
- secondary_patterns
- activated_adapter_fields
- component_trigger.status
- screen_trigger
- learning_sheet_fields
- evidence_outputs

## Hold condition

Hold if review ledger appears to be the main product or if teachers would mistake it for the final draft.

