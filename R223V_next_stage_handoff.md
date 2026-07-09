# R223V next stage handoff

## Next allowed stage

```text
1013R_R223W_REVIEW_ONLY_PILOT_GATE_SPEC
```

## R223W purpose

R223W should define a reduced review-only pilot gate. It must not implement a route.

## R223W must include

- gate entry conditions
- teacher draft document-style reading requirement
- collapsed review ledger policy
- component metadata-only policy
- v0.1/v0.2 short difference summary policy
- safety flags
- hold / rollback conditions

## R223W must not include

- R97B route change
- formal UI implementation
- frontend/backend implementation
- runtime/provider/model/prompt/db connection
- lesson body writeback
- component execution
- v0.2 publication
- formal apply

## Status to carry forward

```text
R223M_STANDARD_V0_2 = NOT_PUBLISHED
FORMAL_UI = BLOCKED
R97B_ROUTE = BLOCKED
RUNTIME_PROVIDER_MODEL_PROMPT_DB = BLOCKED
LESSON_BODY_WRITEBACK = BLOCKED
FORMAL_APPLY = BLOCKED
```

