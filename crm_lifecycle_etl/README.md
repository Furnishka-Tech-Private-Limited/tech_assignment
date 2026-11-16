# CRM Lifecycle ETL: Candidate Instructions

This folder contains everything you need for the **CRM Lifecycle ETL** assignment. You will build an ETL pipeline that cleans CRM data, works out where each lead is in the customer lifecycle, and routes it to the right team (Inside Sales, Enterprise Sales, Onboarding, Service, Renewals, Win-back and more).

> This is separate from the Meta lead-fetcher assignment elsewhere in this repository. Work only from this folder unless you were told otherwise.

**Time box:** 4 to 6 hours. We value clear thinking over polish.

---

## 1. What is in this folder

| Path | What it is |
|---|---|
| `ASSIGNMENT.md` | The full brief: scenario, tasks (Parts A to D), deliverables, evaluation. **Read this first.** |
| `docs/DATA_DICTIONARY.md` | Description of every column in the CSV files |
| `data/raw/leads.csv` | Leads and contacts |
| `data/raw/activities.csv` | Marketing and sales touchpoints |
| `data/raw/opportunities.csv` | Sales opportunities |
| `data/raw/orders.csv` | Orders and contract end dates |
| `data/raw/tickets.csv` | Support tickets |
| `docx/` | Word versions of the brief and the data dictionary |

The data is **synthetic** and **intentionally imperfect**. Finding and handling the problems is part of the task.

## 2. What you need

- Any language and tooling you are comfortable with. Python 3.9 or newer is a good choice, and SQLite or DuckDB is plenty for the warehouse.
- Git and a personal GitHub account.
- No credentials or paid services are required. Do not use any.

## 3. Get started

1. Clone this repository and switch to the `ETL-Pipeline` branch.
2. Open the `crm_lifecycle_etl` folder and read `ASSIGNMENT.md` and `docs/DATA_DICTIONARY.md`.
3. Treat **2026-11-16** as "today". Pass it into your pipeline as a parameter instead of reading the system clock, so your results are reproducible.
4. Create your **own** project folder outside this repository for your solution (see section 5). Copy `data/raw/` into it.

## 4. What your pipeline must do (summary)

The brief has the details. In short:

1. **Extract** the five CSV files.
2. **Transform:** validate and clean fields, de-duplicate leads (and keep their activities, orders and tickets attached to the right lead), quarantine unusable records **with a reason**, and build a lead score.
3. **Classify and route** every clean lead to one lifecycle stage and one team, with a priority and a readable reason.
4. **Load** into relational tables and also write **one work-queue file per team**.
5. Be **idempotent** (re-running must not duplicate data) and **log row counts** at each stage.
6. Provide **tests**, **SQL answers** to the five analytics questions, and a short written lifecycle design.

## 5. Suggested layout for your repository

You are free to structure it differently. This is a reasonable starting point:

```
your-repo/
  README.md                 how to set up and run (a few commands)
  docs/lifecycle_design.md  Part A
  docs/decisions.md         assumptions, trade-offs, what you would do with more time
  data/raw/                 the provided CSV files
  src/                      pipeline code (extract, transform, rules, load)
  tests/                    automated tests
  sql/analytics.sql         Part C answers, with results
  output/                   sample team queues and the rejects file
```

Your `README.md` should let a reviewer run the whole pipeline from a clean checkout in a few commands.

## 6. How to submit

You submit in **your own GitHub repository**. Do not push to this company repository.

1. Create a **new private repository** in your own GitHub account (for example `crm-lifecycle-etl-assignment`).
2. Commit and push your solution to it.
3. Add the reviewer as a collaborator: in your repository go to **Settings, Collaborators, Add people**, and enter the GitHub username given in your assignment email.
4. Email us the repository link, as a reply to your assignment email, **before the deadline stated in that email**.

Do not change the repository after the deadline. We review the state at the time of your email.

### Before you submit: checklist

- [ ] The repository is private, and the reviewer has been added as a collaborator
- [ ] `README.md` explains setup and how to run the pipeline
- [ ] The pipeline runs from a clean checkout and re-running it does not create duplicates
- [ ] The rejects file shows every dropped record with a reason
- [ ] Team queue files are included for every team
- [ ] Tests exist and pass
- [ ] `sql/analytics.sql` answers all five questions and includes the results
- [ ] `docs/lifecycle_design.md` and `docs/decisions.md` are written
- [ ] No credentials, tokens or personal data are committed

## 7. Rules and data handling

- The data is synthetic. Do not post it, or your solution, in any public place (public repositories, forums, gists or public AI-sharing pages).
- Never commit credentials or tokens.
- You may use AI tools. Be ready to explain every decision and every line of your solution in the follow-up conversation.
- If something is ambiguous, write down your assumption in `docs/decisions.md` and carry on. We want to see how you reason.

## 8. Frequently asked questions

**Do I have to use Python?** No. Use what you work best in.

**Can I use pandas, dbt, DuckDB or similar?** Yes. Say in your README how to install anything you use.

**There is no single correct lifecycle design. How will it be judged?** On whether your stages are clearly defined from the available data, whether team ownership and precedence are justified, and whether your assumptions are stated.

**What if I run out of time?** Submit what you have and say what is missing in `docs/decisions.md`. A clear, honest partial solution beats a rushed, unexplained one.

**Who do I contact with questions?** Reply to your assignment email.

---
*Generated by Claude*
