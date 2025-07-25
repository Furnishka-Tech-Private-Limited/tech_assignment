# Furnishka Meta Lead Fetcher Boilerplate

## .gitignore

```gitignore
# Environment
.env

# Python
__pycache__/
*.pyc

# Data files
data/*.db
```

## .env.sample

```dotenv
# Meta Graph API credentials
# Obtain these from your Meta App (see README for instructions)
META_APP_ID=your_app_id_here
META_APP_SECRET=your_app_secret_here
META_ACCESS_TOKEN=your_access_token_here
LEAD_FORM_ID=your_lead_form_id_here
```

## requirements.txt

```text
requests
python-dotenv
```

## README.md

````markdown
# Furnishka Meta Lead Fetcher Boilerplate

A self-serve starter kit for the Furnishka Meta Lead Fetcher assignment. Clone, configure, and run with minimal effort.

### Contents
1. [Prerequisites](#prerequisites)
2. [Obtain Meta Credentials](#obtain-meta-credentials)
3. [Clone & Setup Boilerplate](#clone--setup-boilerplate)
4. [Configure Environment](#configure-environment)
5. [Install Dependencies](#install-dependencies)
6. [Run the Fetcher](#run-the-fetcher)
7. [Inspect Output](#inspect-output)
8. [Publishing to GitHub](#publishing-to-github)

---

## Prerequisites
- Python 3.8+ installed and on your PATH
- Git installed
- A Meta (Facebook) developer account with access to Leads Ads

## Obtain Meta Credentials
1. **Create a Meta App**
   - Go to https://developers.facebook.com → **My Apps > Create App** → Choose **Business** → Next.
   - In **Add Products**, select **Facebook Login** and **Leads Ads**, then **Set Up**.
2. **Generate System User Access Token**
   - In your Business Manager: **Users > System Users** → Create/select a system user.
   - Under that user: **Add Assets** → Assign your Facebook Page, grant `pages_read_user_content` & `leads_retrieval`.
   - **Generate New Token** for the Page, copy the long-lived token.
3. **Retrieve Lead Form ID**
   - In Ads Manager: **Lead Ads Forms**, click your form, copy the Form ID from URL.
   - Or via Graph API Explorer:
     ```http
     GET /v16.0/{page_id}/leadgen_forms?access_token={ACCESS_TOKEN}
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
2. Open `.env`, fill in:

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
# Fetch all leads since July 1, 2025 and output JSON
python -m src.fetcher --since 2025-07-01T00:00:00+0000 --output json
```

* Use `--output csv` for CSV format.
* Use `--since` to limit to new leads after the given ISO timestamp.

## Inspect Output

* **new\_leads.json** (or **new\_leads.csv**): Contains only newly fetched, deduplicated leads.
* **data/seen\_leads.db**: SQLite DB tracking `lead_id`s to avoid duplicates on re-runs.
* **Logs**: Errors and skips (e.g. missing contact info) printed to console or `fetcher.log` if configured.

## Publishing to GitHub

1. **Create Repo** on GitHub named `furnishka-meta-lead-fetcher-boilerplate` (no README).
2. **Initialize & Push** locally:

   ```bash
   git init
   git add .
   git commit -m "Initial boilerplate commit"
   git branch -M main
   git remote add origin https://github.com/<your-org>/furnishka-meta-lead-fetcher-boilerplate.git
   git push -u origin main
   ```
3. **Verify** that `.env` is in `.gitignore` to prevent leaking credentials.
4. **Optional**: Enable **Branch Protection** (require PRs) and add **CI/Secrets** under repository Settings.
5. **Share URL** with candidates: `https://github.com/<your-org>/furnishka-meta-lead-fetcher-boilerplate`

````markdown
# Furnishka Meta Lead Fetcher Boilerplate

This is a self-serve starter kit for the Furnishka Meta Lead Fetcher assignment. Candidates can clone this repo, obtain their Meta credentials, and run the tool end-to-end without further setup.

## 1. Obtaining Meta App Credentials

1. **Create a Meta App**
   - Visit [Facebook for Developers](https://developers.facebook.com).
   - Click **My Apps > Create App**, choose **Business** app type, and follow prompts.
   - Under **Add Products**, select **Facebook Login** and **Leads Ads**.

2. **Generate a System User Access Token**
   - In **Business Settings** under **Users > System Users**, create or select a system user.
   - Under **System User > Add Assets**, assign your Facebook Page and grant `pages_read_user_content` and `leads_retrieval` permissions.
   - Click **Generate New Token**, choose the system user, select the Page, and copy the long-lived access token.

3. **Retrieve the Lead Form ID**
   - In **Ads Manager**, go to **Lead Ads Forms** for your Page and copy the Form ID from the URL.
   - Or via Graph API Playground:
     ```http
     GET /v16.0/{page_id}/leadgen_forms?access_token={META_ACCESS_TOKEN}
     ```

4. **Configure .env**
   ```bash
   cp .env.sample .env
   # Edit .env:
   #   META_APP_ID=<your_app_id>
   #   META_APP_SECRET=<your_app_secret>
   #   META_ACCESS_TOKEN=<generated_token>
   #   LEAD_FORM_ID=<your_form_id>
   ```

## 2. Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-org/furnishka-meta-lead-fetcher-boilerplate.git
   cd furnishka-meta-lead-fetcher-boilerplate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the fetcher**
   ```bash
   python -m src.fetcher --since 2025-07-01T00:00:00+0000 --output json
   ```

4. **Inspect output**
   - New leads will be written to `new_leads.json` (or `new_leads.csv`).
   - Seen lead IDs are stored in `data/seen_leads.db` to ensure deduplication.

## 3. Structure

```
.
├── .env.sample         # Sample env file with placeholders
├── .gitignore
├── README.md           # Instructions including credential setup
├── requirements.txt
├── data/
│   ├── meta_leads_sample.json  # Example payload
│   └── seen_leads.db (auto-created)
├── src/
│   ├── fetcher.py      # Main CLI tool
│   └── utils/
│       └── db.py       # SQLite dedupe helper
```
```

## Sample Data
```json
// data/meta_leads_sample.json
{
  "data": [
    {
      "id": "1001",
      "created_time": "2025-07-24T12:34:56+0000",
      "field_data": [
        { "name": "full_name", "values": ["Alice Singh"] },
        { "name": "email",     "values": ["alice@example.com"] },
        { "name": "phone",     "values": ["+918123456789"] }
      ]
    },
    {
      "id": "1002",
      "created_time": "2025-07-24T13:00:00+0000",
      "field_data": [
        { "name": "full_name", "values": ["Bob Kumar"] }
      ]
    }
  ]
}
```

## Path: src/fetcher.py
```python
#!/usr/bin/env python3
import os
import json
import argparse
import logging
import time
import requests
from dotenv import load_dotenv
from utils.db import LeadDB

...
```

## 4. Publishing to GitHub

1. **Create the repository on GitHub**  
   - Log in to GitHub, click **+ > New repository**, name it `furnishka-meta-lead-fetcher-boilerplate`, add a description, choose **Public** or **Private**, and skip README initialization.

2. **Link your local folder**  
   ```bash
   cd furnishka-meta-lead-fetcher-boilerplate
   git init
   git add .
   git commit -m "Initial boilerplate commit"
   git branch -M main
   git remote add origin https://github.com/<your-org>/furnishka-meta-lead-fetcher-boilerplate.git
   ```

3. **Push to GitHub**  
   ```bash
   git push -u origin main
   ```

4. **(Optional) Enable branch protections & CI**  
   - Under **Settings > Branches**, protect `main` (e.g. require PR reviews).  
   - Under **Settings > Actions/Secrets**, add any CI runners or secrets.

5. **Share with candidates**  
   - Distribute the GitHub URL in your assignment brief.  
   - Confirm `.env` is listed in `.gitignore` so no secrets are ever pushed.

Once complete, candidates can clone and begin:
```bash
git clone https://github.com/<your-org>/furnishka-meta-lead-fetcher-boilerplate.git
```

````

