# Repository: furnishka-meta-lead-fetcher-boilerplate


## README.md

````markdown
# Furnishka Meta Lead Fetcher Boilerplate

A self-serve starter kit to evaluate your ability to interact with Meta’s Graph API, parse lead data, and build a robust, idempotent CLI tool. This assignment mirrors real-world integrations you would build at Furnishka.

## Contents
1. [Assignment Goals](#assignment-goals)
2. [What We Expect from You](#what-we-expect-from-you)
3. [Steps to Follow](#steps-to-follow)
4. [Boilerplate Description](#boilerplate-description)
5. [Submission Guidelines](#submission-guidelines)
6. [Prerequisites](#prerequisites)
7. [Obtain Meta Credentials](#obtain-meta-credentials)
8. [Clone & Setup Boilerplate](#clone--setup-boilerplate)
9. [Configure Environment](#configure-environment)
10. [Install Dependencies](#install-dependencies)
11. [Run the Fetcher](#run-the-fetcher)
12. [Inspect Output](#inspect-output)
13. [Publishing to GitHub](#publishing-to-github)

---

## Assignment Goals
- Authenticate and fetch Lead Ads data from a Meta Graph API endpoint.
- Normalize and flatten the raw JSON into a simple schema (lead ID, name, email, phone, timestamp).
- Implement idempotent behavior using local persistence (SQLite) to avoid duplicates.
- Demonstrate error handling, logging, and pagination.
- Provide clear documentation and ease-of-use for future maintainers.

## What We Expect from You
- A working CLI tool (Python preferred) following the provided boilerplate.
- Idempotent fetching: re-running should fetch only new leads.
- Proper handling of missing data (skip/log leads without contact info).
- Pagination support until all pages are retrieved.
- Retry logic on transient API failures.
- Clean, commented code adhering to best practices.
- A concise README with setup, usage, and submission instructions.

## Steps to Follow
1. Read through the assignment goals and expectations.
2. Clone this boilerplate repository (see below).
3. Obtain your Meta App credentials and Lead Form ID.
4. Configure the `.env` file with real values.
5. Install dependencies.
6. Run the fetcher CLI and verify output.
7. Test idempotency by running twice.
8. Package or zip your final code.
9. Submit according to the guidelines below.

## Boilerplate Description
- **.gitignore**: Excludes `.env`, caches, and local DB files.
- **.env.sample**: Template for your Meta credentials and form ID.
- **requirements.txt**: `requests` & `python-dotenv`.
- **data/**: Contains `meta_leads_sample.json` and auto-generated `seen_leads.db`.
- **src/fetcher.py**: Main CLI fetching, normalization, dedupe, and output logic.
- **src/utils/db.py**: SQLite helper for seen lead tracking.

## Submission Guidelines
1. Create a ZIP of your project directory (exclude real `.env` or DBs).
2. Include your `.env.sample` with dummy values.
3. Ensure your README clearly explains how to:
   - Install dependencies
   - Configure credentials
   - Run your tool
   - Interpret output
4. Provide sample output logs or screenshots.
5. Submit the ZIP via the link provided in the assignment brief (or email to our hiring address).

## Prerequisites
- Python 3.8+ installed and on your PATH
- Git installed
- A Meta (Facebook) developer account with Leads Ads access

## Obtain Meta Credentials
1. **Create a Meta App**
   - Go to https://developers.facebook.com → **My Apps > Create App** → Choose **Business** → Next.
   - Under **Add Products**, select **Facebook Login** and **Leads Ads**, then **Set Up**.
2. **Generate a System User Access Token**
   - In Business Settings → **Users > System Users** → Create or select a system user.
   - Under **Add Assets**, assign your Facebook Page and grant `pages_read_user_content` & `leads_retrieval`.
   - Click **Generate New Token**, choose your system user and Page, then copy the long-lived token.
3. **Retrieve Lead Form ID**
   - In Ads Manager → **Lead Ads Forms**, click your form and copy the Form ID from the URL.
   - Or via Graph API Explorer:
     ```http
     GET /v16.0/{page_id}/leadgen_forms?access_token={META_ACCESS_TOKEN}
     ```

## Clone & Setup Boilerplate
```bash
# Clone the starter repo
git clone https://github.com/<your-org>/furnishka-meta-lead-fetcher-boilerplate.git
cd furnishka-meta-lead-fetcher-boilerplate
````

## Configure Environment

1. Copy and edit `.env.sample`:

   ```bash
   cp .env.sample .env
   ```
2. Open `.env` and fill in your credentials:

   ```dotenv
   META_APP_ID=<your_meta_app_id>
   META_APP_SECRET=<your_meta_app_secret>
   META_ACCESS_TOKEN=<your_system_user_token>
   LEAD_FORM_ID=<your_lead_form_id>
   ```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Fetcher

```bash
# Fetch leads since 2025-07-01 and output JSON
python -m src.fetcher --since 2025-07-01T00:00:00+0000 --output json
```

* Use `--output csv` to generate a CSV file.
* Use `--since` to limit results to after a given ISO timestamp.

## Inspect Output

* **new\_leads.json** or **new\_leads.csv**: Contains only new, deduplicated leads.
* **data/seen\_leads.db**: SQLite DB tracking seen `lead_id`s.
* **Logs**: Errors or skipped records appear in the console.

## Publishing to GitHub

1. **Create the repository** on GitHub named `furnishka-meta-lead-fetcher-boilerplate` (skip README init).
2. **Initialize & Push**:

   ```bash
   git init
   git add .
   git commit -m "Initial boilerplate commit"
   git branch -M main
   git remote add origin https://github.com/<your-org>/furnishka-meta-lead-fetcher-boilerplate.git
   git push -u origin main
   ```
3. **Verify** `.env` is in `.gitignore` to avoid leaking credentials.
4. **Optional**: Enable branch protection and CI/secrets in Settings.
5. **Share URL**: `https://github.com/<your-org>/furnishka-meta-lead-fetcher-boilerplate`

```
```
