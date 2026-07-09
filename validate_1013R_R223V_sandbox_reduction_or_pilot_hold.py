import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

REQUIRED_FILES = [
    "R223V_sandbox_reduction_review.md",
    "R223V_teacher_draft_full_reading_recommendation.md",
    "R223V_review_ledger_default_collapse_policy.md",
    "R223V_component_trigger_metadata_policy.md",
    "R223V_v0_1_v0_2_difference_summary_policy.md",
    "R223V_pilot_or_hold_decision.md",
    "R223V_next_stage_handoff.md",
    "R223V_decision_report.md",
    "README_FOR_GPT_REVIEW.md",
    "PACKAGE_MANIFEST.json",
]

REQUIRED_DECISIONS = [
    "PASS_CONTINUE_TO_R223W_REVIEW_ONLY_PILOT_GATE_SPEC",
    "HOLD_FOR_R223T_SANDBOX_PREVIEW_REDUCTION",
    "HOLD_FORMAL_V0_2_NOT_READY",
]

REQUIRED_PHRASES = [
    "review-only pilot gate",
    "document-style",
    "collapsed_summary",
    "metadata only",
    "not executable",
    "difference summary",
    "R223M_STANDARD_V0_2 = NOT_PUBLISHED",
    "FORMAL_UI = BLOCKED",
    "R97B_ROUTE = BLOCKED",
    "RUNTIME_PROVIDER_MODEL_PROMPT_DB = BLOCKED",
    "LESSON_BODY_WRITEBACK = BLOCKED",
]

BANNED_PHRASES = [
    "R223M_STANDARD_V0_2 = PUBLISHED",
    "FORMAL_UI = ALLOWED",
    "R97B_ROUTE = ALLOWED",
    "teacher_confirmed=true",
    "formal_apply_allowed=true",
    "database_written=true",
    "lesson_body_written=true",
]

FALSE_BOUNDARIES = [
    "schema_v0_2_published",
    "formal_ui",
    "r97b_modified",
    "formal_route_added",
    "frontend_backend_modified",
    "runtime_connected",
    "provider_model_connected",
    "prompt_modified",
    "database_written",
    "lesson_body_written",
    "existing_teacher_drafts_modified",
    "r222d_component_library_modified",
    "formal_apply",
]

def read_text(name):
    return (ROOT / name).read_text(encoding="utf-8")

def main():
    failures = []
    checks = 0

    for name in REQUIRED_FILES:
        checks += 1
        if not (ROOT / name).exists():
            failures.append(f"missing required file: {name}")

    combined = "\n".join(read_text(name) for name in REQUIRED_FILES if (ROOT / name).exists())

    for decision in REQUIRED_DECISIONS:
        checks += 1
        if decision not in combined:
            failures.append(f"missing decision output: {decision}")

    for phrase in REQUIRED_PHRASES:
        checks += 1
        if phrase not in combined:
            failures.append(f"missing required phrase: {phrase}")

    for phrase in BANNED_PHRASES:
        checks += 1
        if phrase in combined:
            failures.append(f"forbidden phrase present: {phrase}")

    manifest_path = ROOT / "PACKAGE_MANIFEST.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        checks += 1
        if manifest.get("stage_id") != "1013R_R223V_SANDBOX_REDUCTION_OR_PILOT_HOLD":
            failures.append("manifest stage_id mismatch")
        checks += 1
        if manifest.get("decision") != "PASS_CONTINUE_TO_R223W_REVIEW_ONLY_PILOT_GATE_SPEC":
            failures.append("manifest decision mismatch")
        boundaries = manifest.get("boundaries", {})
        for key in FALSE_BOUNDARIES:
            checks += 1
            if boundaries.get(key) is not False:
                failures.append(f"manifest boundary must be false: {key}")

    result = {
        "passed": not failures,
        "check_count": checks,
        "failed": len(failures),
        "failures": failures,
        "decision": "PASS_CONTINUE_TO_R223W_REVIEW_ONLY_PILOT_GATE_SPEC",
    }
    (ROOT / "validate_1013R_R223V_sandbox_reduction_or_pilot_hold_result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(result, ensure_ascii=False))
    raise SystemExit(0 if not failures else 1)

if __name__ == "__main__":
    main()

