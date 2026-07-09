# R223V component trigger metadata policy

## Policy

Component trigger status must remain review-only metadata.

## Required label

Every component trigger section in a future review-only pilot must include:

```text
Component trigger metadata only. Not executable. Not added to component library.
component trigger metadata only, not executable
```

## Display rules

Allowed:

- status count
- component_id in full ledger
- short explanation of why a classroom action maps to a component candidate

Blocked:

- run button
- insert button
- apply to big screen button
- add to component library button
- teacher-facing component shelf
- automatic component activation

## Status handling

| status | future pilot behavior |
| --- | --- |
| already_registered | review metadata only |
| candidate_from_R222D_pool | review metadata only |
| new_surface_candidate | full ledger only |
| unregistered_do_not_execute | full ledger only, warning required |

## Hold condition

Hold if a future preview implies that a candidate or unregistered component can be executed or inserted.
