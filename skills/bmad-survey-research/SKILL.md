---
name: bmad-survey-research
description: Builds traceable evidence packets from sources. Use when the user says "research this survey section" or "collect evidence for these claims".
---

# Domain Researcher

This skill turns a survey plan or research question into atomic claims and traceable evidence cards. Act as a careful domain researcher whose output will be challenged by critics and auditors, not as a persuasive author. The output is a research packet another agent can verify without relying on confidence or hidden reasoning.

## Resolution rules

- Bare paths and `{skill-root}` resolve from this skill's installed directory.
- `{project-root}` is the project working directory.

## Research against the contract

Accept a survey plan, taxonomy leaves, or a clearly scoped question plus any supplied corpus. Load `references/source-and-evidence-policy.md` and use `assets/research-packet-template.md`. Use the supplied decision context, as-of date, source restrictions, and leaves in scope; ask only when a missing choice would materially change the research. In headless use, state reversible assumptions and expose material ambiguity as a coverage gap.

Use available authorized search, document, repository, and connector tools. Prefer primary sources for technical claims, while using reviews to discover terminology and counterevidence. For time-sensitive claims, verify current state rather than relying on model memory. If source access is unavailable, return evidence requests and coverage gaps instead of invented content.

Write atomic claims with stable IDs, scope qualifiers, and importance. Use the plan's namespace; otherwise allocate `L001-C001` and `L001-E001` style IDs. Preserve existing IDs, never renumber or reuse them, and give cross-leaf claims one primary leaf plus related-leaf tags. Link each claim to evidence cards containing the inspected source identity, access status, exact location, minimum necessary support span or paraphrase, applicability conditions, and source quality. A citation that has not been inspected remains a lead and cannot support a claim. New claims stay `proposed` until verification and adjudication; record the researcher's support assessment separately.

Search deliberately for contrary results, failed replications, boundary conditions, and evaluation mismatches. Evidence from the same citation chain is not independent corroboration. For benchmark results, capture enough experimental context to prevent false comparisons.

Derive the runtime values `topic-slug` from the topic and `date` from the current date. Write `research-packet.md` in the supplied survey run folder when one exists; otherwise use `{project-root}/_bmad-output/survey-debate/research-{topic-slug}-{date}/`. Before handoff, give a reviewer subagent only the scope, sources, and packet; forbid further delegation and request a fixed list of unsupported central claims or missing contrary evidence. If unavailable, run the same check sequentially. Return the packet path, coverage by taxonomy leaf, source-access limitations, and counts by claim status and support assessment.
