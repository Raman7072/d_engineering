# GitHub Guide: Upload Your Project to GitHub  

## Step 1: Git vs GitHub  
- **Git** = Version control tool on your computer.  
  - Saves snapshots of your project (commits).  
  - Lets you track changes, roll back, and collaborate.  

- **GitHub** = Online platform for Git repositories.  
  - Cloud storage for projects.  
  - Enables collaboration, sharing, and open-source contributions.  

👉 You use **Git locally** and **GitHub online** together.  

---

## Step 2: Install Git  
1. Update package list:  
   ```bash
   sudo apt update
   ```
2. Install Git:
   ```bash
   sudo apt install git
   ```
3. Verify installation:
   ```bash
   git --version
   ```
   ✅ If version is displayed, installation is successful.
---

## Step 3: Create a GitHub Account
1. Go to [GitHub](https://github.com/) → Click **Sign up**.
2. Enter email, password, and choose a **username**.
3. Verify email with code.
4. 🎉 You’re now part of the GitHub community.
---

## Step 4: Create a New Repository
- Repository (Repo) = Project folder on GitHub.
Steps:
1. Log in → Click + → **New repository**.
2. Fill details:
   - Name: e.g., `my-first-project`
   - Description (optional)
   - Visibility: **Public** (anyone) or **Private** (restricted).
3. Click **Create repository**.
---

## Step 5: Upload Files via GitHub Website (Beginner Method)
1. Go to repo page → Click **Add file → Upload files**.
2. Drag & drop files or choose manually.
3. Add commit message (e.g., `"Initial commit"`).
4. Click Commit changes.
   ✅ Your project is now online!
---

## Step 6: Set Up SSH Keys (Secure Access)
1. Generate SSH key:
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```
2. Start agent & add key:
   ```bash
   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/id_rsa
   ```
3. Copy public key:
   ```bash
   cat ~/.ssh/id_rsa.pub
   ```
4. Add key in GitHub:
   - Settings → SSH and GPG Keys → New SSH Key → Paste key → Save.
5. Test connection:
   ```bash
   ssh -T git@github.com
   ```
   ✅ Should show “Successfully authenticated.”
---

## Step 7: Upload Files Using Command Line (Pro Method)
1. Navigate to project folder:
   ```bash
   cd path/to/project
   ```
2. Initialize Git:
   ```bash
   git init
   ```
3. Add files:
   ```bash
   git add .
   ```
4. Commit files:
   ```bash
   git commit -m "Initial commit"
   ```
5. Rename main branch:
   ```bash
   git branch -M main
   ```
6. Link GitHub repo:
   ```bash
   git remote add origin https://github.com/username/repo.git
   ```
7. Push code:
   ```bash
   git push -u origin main
   ```
---

## Step 8: Confirm Upload
- Visit your repo URL → Refresh → Files should appear.
---

## Step 9: Update Your Project (Daily Workflow)
When making changes, run:
```bash
git add .
git commit -m "Describe your changes"
git push origin branch-name
```
---

## Git + GitHub Workflow Diagram

```mermaid
flowchart TD

A[Write/Update Code] --> B[git add .]
B --> C[git commit -m message]
C --> D[git push origin main]
D -->|Uploads| E[GitHub Repository]

E --> F[Project Available Online]
F --> G[Collaboration / Sharing]

subgraph Setup
S1[Install Git]
S2[Create GitHub Account]
S3[Create Repository]
S4[Setup SSH Keys (optional)]
S1 --> S2 --> S3 --> S4
end
```
---

## ✅ Summary
- **Git** = Tracks changes locally.
- **GitHub** = Stores and shares projects online.
- You can upload via **website** (easy) or **command line** (professional).
- Use **SSH keys** for secure, password-free workflow.
- Daily GitHub workflow = `add → commit → push`.
- 
