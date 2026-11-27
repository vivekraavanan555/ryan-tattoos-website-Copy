# Ryan Tattoos & Art Studio — Flask website

## Studio details already configured
- WhatsApp: +91 97871 70303
- Instagram: https://instagram.com/vivekryan9
- Location: Thammampatti, Salem, Tamil Nadu

## Run locally on Windows
1. Install Python 3.10 or newer.
2. Extract this ZIP file.
3. Open the extracted folder in VS Code or File Explorer.
4. In the folder terminal, run:
   ```bash
   py -m venv .venv
   .venv\\Scripts\\activate
   pip install -r requirements.txt
   python app.py
   ```
5. Open http://127.0.0.1:5000

## Publish online free/low-cost with Render
1. Create a GitHub account at https://github.com/ and sign in.
2. Create a new **public** repository named `ryan-tattoos-site` (or private if your Render plan supports it).
3. Upload the contents of this extracted folder to the repository root. Do not upload the ZIP as a single file.
4. Create/sign in to https://render.com/ and choose **New + → Web Service**.
5. Connect GitHub and select `ryan-tattoos-site`.
6. Use these settings:
   - Runtime: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
7. Click **Deploy Web Service**. Wait for the build to finish. Render will provide a public `*.onrender.com` URL.
8. Test the site on a phone and computer. The free service may sleep when idle and take time to wake.

## Custom domain (optional)
1. Buy an available domain from a registrar such as Namecheap or another provider.
2. In Render, open the service **Settings → Custom Domains** and add the domain.
3. Copy the exact DNS records Render displays into the domain registrar's DNS settings. Wait for DNS and HTTPS verification.

## Before sharing publicly
- Replace the illustrative CSS artwork with real tattoo portfolio photos you own or have permission to use.
- Verify the exact studio address and add it to the map link if you want door-to-door directions. Current map link points to the Thammampatti area, not a verified shop pin.
- Check WhatsApp and Instagram links from a phone.
- The booking form opens a pre-filled WhatsApp message; it does not store appointments in a database.
