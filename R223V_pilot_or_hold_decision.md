# R223V pilot or hold decision

stage_id: 1013R_R223V_SANDBOX_REDUCTION_OR_PILOT_HOLD  
status: PASS_LOCAL_REDUCTION_DECISION  
decision: PASS_CONTINUE_TO_R223W_REVIEW_ONLY_PILOT_GATE_SPEC

## Decision

Proceed to R223W, but only as a review-only pilot gate specification.

R223V does not authorize:

- formal UI
- R97B route
- frontend/backend implementation
- runtime/provider/model/prompt/db
- lesson body writeback
- v0.2 publication
- formal apply

## Why continue

R223U showed the sandbox preview is understandable and safe for review. The needed changes are reductions and gate definitions, not deeper implementation.

## Required R223W direction

R223W should specify:

1. reduced review-only pilot gate
2. teacher draft document-style primary pane
3. review ledger collapsed summary by default
4. component trigger metadata-only label
5. concise v0.1/v0.2 difference summary
6. no writeback, no persistence, no formal route

## Decision outputs

```text
PASS_CONTINUE_TO_R223W_REVIEW_ONLY_PILOT_GATE_SPEC
HOLD_FOR_R223T_SANDBOX_PREVIEW_REDUCTION
HOLD_FORMAL_V0_2_NOT_READY
```

