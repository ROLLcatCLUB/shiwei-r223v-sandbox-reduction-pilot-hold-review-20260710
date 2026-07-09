# README for GPT review

## Package

1013R_R223V_SANDBOX_REDUCTION_OR_PILOT_HOLD

## Review question

Should the R223T sandbox preview continue as-is, be reduced, or be held?

## Local decision

```text
R223V = PASS_LOCAL_REDUCTION_DECISION
NEXT_ALLOWED = R223W_REVIEW_ONLY_PILOT_GATE_SPEC
R223M_STANDARD_V0_2 = NOT_PUBLISHED
FORMAL_UI / R97B / runtime / prompt / model / db = BLOCKED
```

## Suggested review order

1. `R223V_decision_report.md`
2. `R223V_sandbox_reduction_review.md`
3. `R223V_review_ledger_default_collapse_policy.md`
4. `R223V_teacher_draft_full_reading_recommendation.md`
5. `R223V_component_trigger_metadata_policy.md`
6. `R223V_pilot_or_hold_decision.md`
7. `validate_1013R_R223V_sandbox_reduction_or_pilot_hold_result.json`

## Boundary

This package only makes a reduction / continue / hold decision. It does not implement a new preview or route.

