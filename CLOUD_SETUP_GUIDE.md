# ☁️ Djinn Constellation Hub — Cloud Setup Guide

This guide will help you deploy Djinn Constellation Hub in a cloud environment for scalable, federated AI operations.

---

## 🚦 Prerequisites
- Cloud account (AWS, Azure, GCP, or custom VPS)
- Python 3.8+
- Git
- PCloud account (for federation)
- Sufficient RAM and storage (see README for recommendations)
- API keys/tokens for cloud provider (if using automation)

## 📦 Initial Setup
```bash
git clone https://github.com/Yufok1/Djinn-Constellation-Hub.git
cd Djinn-Constellation-Hub
./setup_djinn_federation.bat
```

## ☁️ Cloud Model Deployment
- **Option 1: Manual**
    - Upload/download models using provided batch scripts:
      - `shadow_automation.bat` (cloud download)
      - `import_shadow_models.bat` (import to main instance)
- **Option 2: Automated (Advanced)**
    - Use cloud CLI tools (e.g., AWS CLI, Azure CLI) to automate model sync
    - (Optional) Use `pcloud_djinn_federation.py` for PCloud-based federation

## 🧠 Federation Configuration
- Edit `config/config.ini` or `.env` with your cloud and federation settings:
    - Model directories (local/cloud)
    - PCloud credentials and folder
    - Federation node identity, if needed
- For multi-node federation, repeat setup on each instance and ensure PCloud sync is active.

## 🚀 Launching in the Cloud
```bash
# Start the federation hub
python djinn_cli.py launch

# Or run directly
cd djinn-federation/launcher
python efficiency_first_hub.py
```

## 🔗 Example: API Server Launch
```bash
python constellation_hub.py --api
# or
python enhanced_constellation_hub.py --api
```

## 🛡️ Security & Best Practices
- Never commit API keys, secrets, or credentials to GitHub
- Use `.gitignore` to exclude `/models/`, `/memory_bank/`, `.env`, etc.
- Set up firewall rules to restrict access to your cloud instance
- Use HTTPS and authentication for any API endpoints

## 🐳 (Optional) Docker/Terraform
- For advanced users, consider writing a `Dockerfile` or `terraform` scripts for automated provisioning and scaling

---

For more details, see the main README, `PCLOUD_FEDERATION_GUIDE.md`, and `CONSTELLATION_HUB_GUIDE.md`.

**May your cloud be federated and your AI ever mystical!**
