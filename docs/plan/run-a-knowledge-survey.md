---
title: 'Run a Knowledge Survey'
description: Build an evidence-grounded survey of a research topic with the Survey Debate skills — plan a taxonomy, collect evidence, let a skeptic and a verifier attack it, then synthesize a report you can audit.
sidebar:
  order: 5
---

Use the `bmad-survey` skills to turn a research question into a survey whose
every conclusion traces back to inspected evidence and a recorded debate. This
page explains what the module produces, when to use each of its eight skills,
and how to read the result.

## When to Use This

- You need a literature review or state-of-the-art survey that a technical
  reader can check, not a summary to take on trust.
- A decision hinges on comparing approaches (an architecture, a method, a
  vendor) and you want the weaknesses argued out before you commit.
- You already have a draft survey or a list of claims and want it
  pressure-tested without rewriting it.
- A survey exists and new papers or sources have appeared since it was written.

For a single decision that needs quick, cited research, use
[Research a Decision](./research-a-decision.md) instead. Survey Debate costs
more and is built for topics where the disagreement is the point.

## How It Works

Survey Debate separates the work into roles that see only shared artifacts —
claims, evidence cards, critiques — never each other's reasoning. Each pass
writes to a workspace file, and the report is generated from that workspace,
never from prose the roles drafted.

| Phase | Role         | What happens                                                                     |
| ----- | ------------ | -------------------------------------------------------------------------------- |
| 1     | Planner      | Breaks the topic into taxonomy leaves with stable IDs, priorities, evidence policy |
| 2     | Researcher   | Proposes atomic claims and evidence cards for each leaf                          |
| 3     | Skeptic      | Turns objections into falsifiers, missing controls, boundary cases               |
| 4     | Verifier     | Checks that each source actually supports its claim and that benchmarks compare  |
| 5     | Adjudicator  | Moves each claim to a status and records why every critique was resolved or not  |
| 6     | Synthesizer  | Renders the adjudicated workspace into `survey.md`                               |

Every claim carries one of six statuses: `proposed`, `supported`, `disputed`,
`incomparable`, `insufficient-evidence`, or `rejected`. A debate round runs
only while unresolved high-impact critiques remain. Hitting the round or
budget limit is recorded as `forced-termination`, never as consensus, and
stable disagreement is a valid result.

:::caution[No source, no claim]
When the session has no search or document tools, the skills create evidence
requests and leave claims `insufficient-evidence`. They never invent citations,
snippets, or benchmark numbers. Give them a local corpus, or fill the requests
yourself and run an update.
:::

## The Skills

| Skill                    | Use it when                                                        | Input                              | Output                          |
| ------------------------ | ------------------------------------------------------------------ | ---------------------------------- | ------------------------------- |
| `bmad-survey`            | You want the whole flow, start to report                           | Topic and decision                 | Workspace, report, memlog       |
| `bmad-survey-plan`       | You want to approve the taxonomy before spending on research       | Topic, decision, scope             | `survey-plan.md`                |
| `bmad-survey-research`   | You want evidence for one leaf or claim set                        | Plan or leaf IDs                   | Research packet                 |
| `bmad-survey-critic`     | You want the skeptic's pass on a claim ledger                      | Claims                             | Critique packet                 |
| `bmad-survey-verify`     | You want citations and benchmark comparability checked             | Claims and evidence cards          | Verification report             |
| `bmad-survey-synthesize` | You have an adjudicated workspace and only need the report         | `survey-workspace.md`              | `survey.md`                     |
| `bmad-survey-debate`     | You have a draft or claim list and want it attacked, not rebuilt   | Draft or claims                    | `debate-report.md`              |
| `bmad-survey-update`     | New sources or a new as-of date for an existing survey             | Workspace and new sources          | Updated report, `survey-delta.md` |

`bmad-survey` invokes the focused skills itself, so most runs need only that
one. Reach for a focused skill when you already hold its input artifact or
want to control a single stage.

## Steps

### 1. Frame the inquiry

Start `bmad-survey` and give it five things in one message: the topic, the
decision it serves, the scope and exclusions, any corpus you already have, and
the evidence policy (which source types count). Anything you leave out is
inferred and recorded as an assumption in the workspace.

:::note[Example]
`/bmad-survey` Topic: state space models versus Transformers for long
sequences. Decision: whether to move our internal LLM backbone to an SSM.
Scope: 2023 onward, long-context inference; exclude vision. Corpus:
`./papers/`. Evidence: primary papers and official repositories only, no
blog posts. Budget: two debate rounds.
:::

### 2. Review the plan

The skill writes a taxonomy of leaves, each with a priority and a completion
test, and an evidence policy. Read the leaves and cut or reprioritize before
research starts; effort goes where decision impact and uncertainty are highest,
so a wrong priority costs the most here.

### 3. Let the passes run

Research, critique, verification, and adjudication run without you. With
subagents available (Claude Code, Codex), each role runs in isolation and the
workspace records `independent` as its execution topology. Without them, the
passes run one after another in the same session and the workspace records
`role-separated`; the result is still usable, and the report says so under
process limitations.

### 4. Read the result

Open `survey.md` for the conclusions, the comparison matrix, and the research
gaps. Open `survey-workspace.md` when you want to know why a conclusion was
accepted: find the claim in the **Claims** table, follow its evidence IDs to
the **Evidence cards** table, then read its rows in **Critiques** and
**Adjudications**. The **Evidence requests** table lists what the run could not
find.

### 5. Keep it current

When a new paper lands, run `bmad-survey-update` with the workspace path and
the new source. It snapshots the workspace and report, re-opens adjudication
only for affected claims, keeps every unchanged ID and status, and writes
`survey-delta.md` naming exactly what moved.

## What You Get

```
your-project/
└── _bmad-output/
    └── survey-debate/
        └── survey-<topic>-<date>/
            ├── survey-workspace.md   # scope, taxonomy, claims, evidence, critiques, adjudications
            ├── survey.md             # the report: matrix, findings, gaps, unresolved disputes
            ├── survey-delta.md       # after an update: what changed and why
            └── .memlog.md            # append-only decision log
```

The workspace front matter carries `status` (`ready` or `blocked`) and
`termination` (`converged` or `forced-termination`). A report is publishable
only when the workspace says `ready`; `blocked` names the publication blocker.

## Starting It

| Goal                              | Type this                                                                  |
| --------------------------------- | -------------------------------------------------------------------------- |
| Full survey                       | `/bmad-survey` then describe the topic and decision                        |
| Plan only                         | `/bmad-survey-plan` with the topic and what you will decide                |
| Attack an existing draft          | `/bmad-survey-debate` with the draft path and a round limit                |
| Add new sources                   | `/bmad-survey-update` with the workspace path and the sources              |
| Regenerate the report             | `/bmad-survey-synthesize` with the workspace path                          |

On Codex the prefix is `$` instead of `/`; on Cursor and most other tools,
type the skill name without a prefix.
