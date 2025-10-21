# SynchroHR - HRMS Application

## Environment Variables

This project requires the following environment variables to be configured:

### Client-Side Variables (VITE_ prefix - available in browser)
```
VITE_SUPABASE_URL=https://wapydsvgltbhkvbfaybp.supabase.co
VITE_SUPABASE_PUBLISHABLE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndhcHlkc3ZnbHRiaGt2YmZheWJwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjA3MjE4MDQsImV4cCI6MjA3NjI5NzgwNH0.eH2IIr5h_-5s4-Vd-tyOFm84X298kWP38AzWiUh95pU
VITE_SUPABASE_PROJECT_ID=wapydsvgltbhkvbfaybp
```

### Server-Side Variables (Edge Functions only)
These are automatically available in Supabase Edge Functions via Lovable Cloud:
```
SUPABASE_URL=https://wapydsvgltbhkvbfaybp.supabase.co
SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndhcHlkc3ZnbHRiaGt2YmZheWJwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjA3MjE4MDQsImV4cCI6MjA3NjI5NzgwNH0.eH2IIr5h_-5s4-Vd-tyOFm84X298kWP38AzWiUh95pU
SUPABASE_SERVICE_ROLE_KEY=(managed by Lovable Cloud)
LOVABLE_API_KEY=(managed by Lovable Cloud)
RESEND_API_KEY=(your Resend API key)
MAIL_FROM=dhivyabalakumar28@gmail.com
```

**IMPORTANT**: Never commit the `.env` file to version control. These values are provided here for deployment configuration only.

## Project info

**URL**: https://lovable.dev/projects/4eee3e1e-e462-4a0a-9fac-57049778ab14

## How can I edit this code?

There are several ways of editing your application.

**Use Lovable**

Simply visit the [Lovable Project](https://lovable.dev/projects/4eee3e1e-e462-4a0a-9fac-57049778ab14) and start prompting.

Changes made via Lovable will be committed automatically to this repo.

**Use your preferred IDE**

If you want to work locally using your own IDE, you can clone this repo and push changes. Pushed changes will also be reflected in Lovable.

The only requirement is having Node.js & npm installed - [install with nvm](https://github.com/nvm-sh/nvm#installing-and-updating)

Follow these steps:

```sh
# Step 1: Clone the repository using the project's Git URL.
git clone <YOUR_GIT_URL>

# Step 2: Navigate to the project directory.
cd <YOUR_PROJECT_NAME>

# Step 3: Install the necessary dependencies.
npm i

# Step 4: Start the development server with auto-reloading and an instant preview.
npm run dev
```

**Edit a file directly in GitHub**

- Navigate to the desired file(s).
- Click the "Edit" button (pencil icon) at the top right of the file view.
- Make your changes and commit the changes.

**Use GitHub Codespaces**

- Navigate to the main page of your repository.
- Click on the "Code" button (green button) near the top right.
- Select the "Codespaces" tab.
- Click on "New codespace" to launch a new Codespace environment.
- Edit files directly within the Codespace and commit and push your changes once you're done.

## What technologies are used for this project?

This project is built with:

- Vite
- TypeScript
- React
- shadcn-ui
- Tailwind CSS

## How can I deploy this project?

Simply open [Lovable](https://lovable.dev/projects/4eee3e1e-e462-4a0a-9fac-57049778ab14) and click on Share -> Publish.

## Can I connect a custom domain to my Lovable project?

Yes, you can!

To connect a domain, navigate to Project > Settings > Domains and click Connect Domain.

Read more here: [Setting up a custom domain](https://docs.lovable.dev/features/custom-domain#custom-domain)
