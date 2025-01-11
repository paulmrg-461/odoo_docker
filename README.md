
# Odoo Setup Guide with Docker

## Step 1: Start the Odoo Container

1. Open **PowerShell** in the folder where your `docker-compose.yml` file is located.
2. Run the container in detached mode (background):
   ```powershell
   docker compose up -d
   ```

## Step 2: Access the Odoo Container

1. Enter the Odoo container with a shell (bash):
   ```powershell
   docker compose exec odoo bash
   ```
   > Note: The service name in your `docker-compose.yml` might be different (e.g., `odoo_server`, `odoo-1`, etc.). Adjust accordingly.

## Step 3: Configure the Odoo Database

1. Once inside the container (you'll see a prompt like `root@container_id:/...#`), execute the following command to configure the database:
   ```bash
   odoo --db_host=db --db_user=odoo --db_password=odoo --db_port=5432 \
        -d odoo -i base --stop-after-init
   ```
   This will force the installation of the `base` module in the `odoo` database.

2. Exit the container:
   ```bash
   exit
   ```

## Step 4: Check Odoo Logs

1. Review the logs to ensure Odoo is running correctly:
   ```powershell
   docker compose logs -f odoo
   ```

2. After restarting Odoo (or if it continues running), the `base` module should now be installed.

---

> This method is optimized for **Windows** using PowerShell, avoiding potential issues with parameter interpretation (`--`) by PowerShell.

# Quick Guide: Getting Started with Odoo

## 1. How do I log in for the first time?

### A) If you **haven’t** created a “usable” database yet
1. At the bottom of the login screen, click **“Manage Databases”**.
2. Odoo may ask for the **Master Password**. If you haven’t changed it, it’s usually `admin` by default (although it’s recommended to change it in production).
3. Create your new database and specify the **email** + **password** for your administrator user.
4. Go back to the main login screen and enter the credentials you just set up.

### B) If you already created the database with an admin user
1. On the login screen, enter the **Email** and **Password** you assigned to the administrator user.  
2. Forgot the password? 
   - Use **“Manage Databases”** to reset it,  
   - or the **“Reset password”** option if enabled,  
   - or a console command (advanced) to reset it directly.

> **Tip**: In older Odoo versions (10 or 11), default credentials were often `admin` / `admin`. In more recent versions (like Odoo 16), you set the credentials when creating the database or via environment variables.

---

## 2. How do I change the logo?
1. Log in as an administrator.  
2. Go to **Settings** → **General Settings** (or **Settings** → **Company** depending on your Odoo version).  
3. There you’ll find the **Company** section.  
4. Edit it and **upload your custom logo**. Odoo will use it in the top bar, login screen, reports, and so on.  
   - **Further customization**: Install or develop a **branding module** if you need separate logos for login, reports, etc.

---

## 3. Can I apply custom colors?
**Yes**, in several ways:

1. **Website Builder / Themes**: If you install the **Website** module, you can pick or download **themes** (from Odoo Apps store) that change colors and design.
2. **Odoo Studio (Enterprise)**: Lets you tweak some web interface elements.
3. **Develop a theme module**: If you know Odoo development (XML, SCSS, QWeb templates), you can create a custom module to modify both backend and frontend styles.

There’s no built-in color picker for the standard back-office UI, but overriding SCSS styles is quite common for customizing the look and feel.

---

## 4. Can I add new functionalities?
**Absolutely**. Some options:

1. **Official Odoo Modules**: From **Apps**, install Accounting, Inventory, CRM, Sales, etc.
2. **Third-Party Modules**: Many exist on [apps.odoo.com](https://apps.odoo.com) or GitHub, created by the community.
3. **Develop your own modules**: Using **Python**, **XML/QWeb**, and Odoo’s framework, you can tailor fields, screens, and processes to your needs.

---

## Summary
- **Login**: Create or select your desired database, note down your admin user credentials, and log in.
- **Change logo**: Go to **Settings** → **General Settings** → **Company** to upload a custom logo.
- **Custom colors**: Use **themes**, **Odoo Studio**, or a custom theme module for deeper styling.
- **New functionalities**: Install official/third-party modules or develop your own **addons**.

With these steps, you’ll have **Odoo** up and running with a customized look and functionalities suited to your business! 
