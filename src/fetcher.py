#!/usr/bin/env python3
import os
import json
import argparse
import logging
import time
import requests
from dotenv import load_dotenv
from utils.db import LeadDB


def fetch_leads(access_token, form_id, since=None):
    url = f"https://graph.facebook.com/v16.0/{form_id}/leads"
    params = {"access_token": access_token, "fields": "field_data,created_time,id"}
    if since:
        params["since"] = since
    all_leads = []
    while url:
        resp = requests.get(url, params=params)
        if resp.status_code >= 500:
            logging.warning(f"Server error {resp.status_code}, retrying once...")
            time.sleep(1)
            resp = requests.get(url, params=params)
        resp.raise_for_status()
        data = resp.json()
        all_leads.extend(data.get("data", []))
        paging = data.get("paging", {})
        url = paging.get("next")
        params = None
    return all_leads


def normalize_lead(raw):
    lead = {"lead_id": raw.get("id"), "created_time": raw.get("created_time")}
    for field in raw.get("field_data", []):
        name = field.get("name")
        values = field.get("values") or []
        lead[name] = values[0] if values else None
    return lead


def main():
    load_dotenv()
    access_token = os.getenv("META_ACCESS_TOKEN")
    form_id = os.getenv("LEAD_FORM_ID")

    parser = argparse.ArgumentParser(description="Fetch Meta leads from a Lead Ads form")
    parser.add_argument("--since", help="ISO timestamp to fetch leads since")
    parser.add_argument("--output", choices=["json", "csv"], default="json")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    db = LeadDB("data/seen_leads.db")

    raw_leads = fetch_leads(access_token, form_id, args.since)
    new_leads = []
    for raw in raw_leads:
        lead = normalize_lead(raw)
        if not lead.get("email") and not lead.get("phone"):
            logging.error(f"Skipping lead {lead['lead_id']} missing contact info")
            continue
        if db.is_seen(lead["lead_id"]):
            continue
        new_leads.append(lead)
        db.mark_seen(lead["lead_id"])

    if new_leads:
        if args.output == "json":
            with open("new_leads.json", "w") as f:
                json.dump(new_leads, f, indent=2)
        else:
            import csv
            with open("new_leads.csv", "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=new_leads[0].keys())
                writer.writeheader()
                writer.writerows(new_leads)

    print(f"Fetched {len(raw_leads)} leads, {len(new_leads)} new")


if __name__ == "__main__":
    main()
