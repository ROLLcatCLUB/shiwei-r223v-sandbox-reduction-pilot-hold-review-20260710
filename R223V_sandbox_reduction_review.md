# R223V sandbox reduction review

stage_id: 1013R_R223V_SANDBOX_REDUCTION_OR_PILOT_HOLD  
status: reduction_or_pilot_hold_decision_only  
source: R223U_SANDBOX_TEACHER_REVIEW

## Current judgment

R223T sandbox preview is safe enough for review, but should not move forward unchanged as a wider pilot surface.

R223U showed:

- safety banner is clear
- teacher default draft is readable
- v0.1 / v0.2 candidate comparison is understandable
- review ledger is useful but could become heavy
- component trigger status is safe as metadata

Therefore R223V recommends a reduced, review-only pilot gate specification before any broader pilot preview.

## Required reductions

1. Review ledger must default collapsed or summary-first.
2. Teacher draft must support document-style full reading.
3. Component trigger status must carry a stronger metadata-only label.
4. v0.1 / v0.2 comparison must show short difference summary first.
5. Safety banner must remain visible.
6. No action controls may be added.

## Decision

```text
PASS_CONTINUE_TO_R223W_REVIEW_ONLY_PILOT_GATE_SPEC
```

This does not authorize formal UI, R97B route, runtime, model, prompt, database or v0.2 publication.

