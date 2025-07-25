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
