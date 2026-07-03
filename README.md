## 🔄 CI/CD Pipeline (GitHub Actions)

This project follows a complete **CI/CD workflow** using GitHub Actions.

### ⚡ Continuous Integration (CI)
CI is fully active and runs on every push and pull request.

It performs:
- Dependency installation
- Flask application import validation
- Build verification

### 🚀 Continuous Deployment (CD)

The project was designed with a CD pipeline targeting an AWS EC2 instance.

The deployment workflow includes:
- SSH-based connection to EC2
- Pulling latest code from GitHub
- Installing dependencies
- Restarting Flask service via systemd

### 📌 Current Status
- CI: ✅ Fully Active
- CD: ⚙️ Configured but not currently executed (infrastructure dependency: EC2 instance)

### 🧠 Reason
CD requires an active deployment server (AWS EC2). The pipeline is ready and tested, but deployment execution is currently paused due to temporary infrastructure unavailability.

### 🔮 Future Improvement
- Reactivate EC2-based deployment
- OR migrate CD to Docker-based cloud deployment (recommended for scalability)
