# CRM Lifecycle ETL: Technical Assignment

**Audience:** candidates (Data / Analytics Engineer, CRM Engineer)
**Time box:** 4 to 6 hours. Please do not exceed it; we value judgment over polish.
**Language/tools:** Your choice (Python or SQL-first recommended). Any warehouse is fine; SQLite or DuckDB is plenty.

---

## 1. Scenario

You have joined a company that sells subscription software. Its CRM holds leads, sales activity, opportunities, orders and support tickets. Today every lead lands in one shared queue, so:

- hot leads wait days for a call,
- customers with escalated tickets get sales emails,
- renewals are discovered when they have already lapsed,
- nobody trusts the data (duplicates, bad emails, mixed date formats).

Leadership wants a nightly **ETL pipeline** that cleans the CRM extracts, works out **where each lead is in the customer lifecycle**, and **assigns it to the right team**: Inside Sales, Enterprise Sales, Customer Success (Onboarding), Service, Renewals, Win-back, Account Management, Marketing Nurture or Reactivation.

We are less interested in whether your code runs than in **how you think about the customer lifecycle**.

## 2. What you receive

Five CSV extracts in `data/raw/` (synthetic, safe to share). See `docs/DATA_DICTIONARY.md` for every column.

| File | Content |
|---|---|
| `leads.csv` | One row per captured lead / contact |
| `activities.csv` | Marketing and sales touchpoints |
| `opportunities.csv` | Sales opportunities and their stage |
| `orders.csv` | Closed orders and contract end dates |
| `tickets.csv` | Support tickets |

The data is **intentionally imperfect**, like a real CRM export. Part of the task is finding the problems yourself. Treat **2026-11-16** as "today" so your results are reproducible.

## 3. Your tasks

### Part A: Lifecycle design (written, about 1 page)
1. Define your lifecycle stages (for example Subscriber, MQL, SQL, Opportunity, Customer sub-stages, Dormant, Lost). Give an **entry condition** for each, based only on data available in the extracts.
2. Define which **team owns each stage** and why. Say what you would do when a lead qualifies for more than one stage, and what takes priority.
3. List **at least three business rules you had to assume** and the question you would ask the business to confirm each.

### Part B: ETL pipeline (code)
1. **Extract** the five files.
2. **Transform**
   - Validate and clean fields (emails, phones, dates, amounts, country, status).
   - De-duplicate leads and make sure child records (activities, orders, tickets) still attach to the right lead.
   - Quarantine unusable records with a **reason**; nothing may be dropped silently.
   - Build a **lead score** from the activity data (you choose weights; justify them).
3. **Classify and route** every clean lead to exactly one lifecycle stage and one team, with a priority and a human-readable reason.
4. **Load** to a warehouse (relational tables) and also produce **one work-queue file per team**.
5. The pipeline must be **idempotent** (re-running it must not duplicate data) and must log row counts at each stage.

### Part C: Analytics (SQL)
Using your warehouse, answer:
1. How many leads sit in each lifecycle stage?
2. What is the workload (lead count) per team and priority?
3. How much customer lifetime value is in the renewal window?
4. Which lead source produces the best share of SQL-or-better leads?
5. Which customers have a high-severity open ticket, ranked by value?

### Part D: Quality and operations
1. Include automated tests (at least the routing rules and the cleaning logic).
2. Describe how you would run this nightly in production, how you would detect a bad run, and how you would handle a **rule change** (for example, "SQL threshold moves from 60 to 70") without rewriting history.

### Stretch (optional, only if time allows)
- Incremental loading (only changed records).
- A rule table in configuration instead of code.
- Show how a lead's stage **moves over time** using daily snapshots.

## 4. Deliverables

Submit in **your own private GitHub repository** (see the README in this folder for the exact steps: add the reviewer as a collaborator and email us the link before the deadline). Your repository should contain:

1. `README.md`: how to set up and run your pipeline in a few commands.
2. `docs/lifecycle_design.md`: Part A.
3. Pipeline code and tests.
4. `sql/analytics.sql` with answers to Part C (include the results).
5. Sample outputs: the team queue files and the rejects file.
6. `docs/decisions.md`: assumptions, trade-offs and what you would do with more time (short).

**Data handling:** the provided data is synthetic. Do not upload it, or your solution, to any public service. Do not put credentials in the repository.

## 5. How we will evaluate

| Area | Weight |
|---|---|
| Lifecycle thinking and routing logic (Part A + B3) | 30% |
| Data quality handling (B2) | 20% |
| Pipeline engineering: structure, idempotency, logging (B1, B4, B5) | 20% |
| Analytics correctness (Part C) | 10% |
| Tests and operational thinking (Part D) | 10% |
| Communication: README, assumptions, clarity | 10% |

There is no single correct answer to the lifecycle design. A well-argued, internally consistent design beats a clever but unexplained one. We will discuss your solution with you in a follow-up conversation.

## 6. Questions

If something is ambiguous, state your assumption in `docs/decisions.md` and move on. That is exactly what we want to see.

---
*Generated by Claude*
