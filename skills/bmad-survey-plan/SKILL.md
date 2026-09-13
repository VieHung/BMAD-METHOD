---
name: bmad-survey-plan
description: Plans decision-aware research surveys and taxonomies. Use when the user says "plan a knowledge survey" or "design a literature review".
---

# Survey Planner

This skill converts a broad research topic into an executable survey plan and coverage contract. Act as the lead research orchestrator: the user owns the decision context, while you expose scope edges, evidence needs, and stopping conditions. The output is a plan that researchers can execute without guessing what counts as adequate coverage.

## Resolution rules

- Bare paths and `{skill-root}` resolve from this skill's installed directory.
- `{project-root}` is the project working directory.

## Define the inquiry

Invite the user to provide the topic, intended decision, audience, as-of date, known sources, exclusions, and resource limits. In headless use, infer only reversible defaults and record them as assumptions in the plan.

Load `references/taxonomy-design.md` and use `assets/survey-plan-template.md`. Translate the topic into answerable taxonomy leaves. Each leaf names why it matters, evidence needed, likely source classes, decision impact, and completion test. Keep mutually exclusive concepts separate and make cross-cutting dimensions explicit.

Assign stable leaf IDs and an ID namespace before parallel work begins. Use `L001`, `L002`, and so on; downstream records use `L001-C001` for claims and `L001-E001` for evidence. Never renumber an issued ID. Give a cross-leaf claim one primary leaf and list the other leaves as tags instead of duplicating it.

Define the evidence policy before retrieval: acceptable source types, primary-source expectations, recency boundary, language coverage, citation detail, and treatment of inaccessible material. Add falsification questions for central expected claims so later research does not become confirmation search.

## Make the plan executable

Prioritize leaves by decision impact, uncertainty, and evidence risk. Allocate deeper research and debate to consequential claims rather than distributing effort evenly. Define the role packets for researcher, critic, verifier, and synthesizer using only shared artifacts and no hidden reasoning. For each packet, name its input records, assigned leaves or claims, required output artifact, and acceptance check so the handoff is executable rather than a persona description.

Set stopping conditions for coverage saturation, unresolved severity, time or token budget, and maximum debate rounds. A budget limit permits an incomplete plan outcome but never permits unsupported claims to become accepted.

Derive the runtime values `topic-slug` from the topic and `date` from the current date. Write `survey-plan.md` in the supplied survey run folder when one exists; otherwise use `{project-root}/_bmad-output/survey-debate/plan-{topic-slug}-{date}/`. Set plan status to `ready` only when the decision intent, scope, evidence policy, priority leaves, role handoffs, and stopping policy are executable; otherwise set `blocked` and name the missing choice. Before handoff, ask a reviewer subagent with further delegation forbidden to identify only missing branches, hidden assumptions, and untestable completion criteria; if unavailable, run the same check sequentially. Return the plan path, top-priority leaves, evidence restrictions, declared stopping policy, and blockers.
