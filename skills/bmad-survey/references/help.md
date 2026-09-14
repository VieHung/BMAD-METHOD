# Survey Debate

Survey Debate turns a research question into an auditable survey whose claims,
evidence, critiques, and decisions remain traceable after the conversation ends.

Use `bmad-survey` for a new end-to-end survey. It plans the taxonomy, builds the
evidence base, runs adversarial role passes, adjudicates claims, and produces the
final report. A complete run has `survey-workspace.md` and `survey.md`; it is
publishable only when the workspace and report both say `ready`.

The focused skills use the same artifact contracts:

- `bmad-survey-plan` creates the taxonomy and coverage contract.
- `bmad-survey-research` creates atomic claims and evidence cards.
- `bmad-survey-critic` produces actionable falsification requests.
- `bmad-survey-verify` audits source support and benchmark comparability.
- `bmad-survey-synthesize` renders adjudicated claims into the report.
- `bmad-survey-debate` pressure-tests an existing draft or claim ledger.
- `bmad-survey-update` incorporates new evidence without losing provenance.
- `bmad-survey-graph` exports the adjudicated survey as a low-density Obsidian graph organized around decision-relevant clusters.

For a new topic, start with `bmad-survey`. Use a focused skill only when the
user requests that stage or already has the required input artifact. Use
`bmad-survey-debate` to audit a draft without rebuilding the full survey. Use
`bmad-survey-update` when a structured workspace already exists and the user
wants to add sources, change the as-of date, or reassess affected conclusions.
Invoke the `bmad-survey-graph` skill when the user wants an Obsidian map after
the survey has an adjudicated workspace.

Forced termination is not consensus. A report stays blocked when central claims
lack inspected evidence, benchmark comparisons are materially incompatible, or
the execution topology is unknown.
