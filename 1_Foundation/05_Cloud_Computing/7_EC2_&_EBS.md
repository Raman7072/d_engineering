# Amazon EC2 — Your Personal Computer in the Cloud

## What is EC2?
- **EC2 (Elastic Compute Cloud)** provides on-demand virtual machines (called **instances**) hosted in AWS data centers.
- You can **rent compute power** instead of buying physical servers.
- Instances include:
  - **vCPUs**
  - **RAM**
  - **Storage (ephemeral, block, or object)**
  - **Operating Systems (Linux, Windows, etc.)**
- Instances can be **started/stopped in minutes** from anywhere.

---

## Separation of Compute and Storage
- **Compute** = CPU + RAM (runs applications)
- **Storage** = SSDs/Disks (stores data)
- Why separate?
  - Restart/replace compute without affecting storage
  - Attach storage to multiple instances
  - Increases **flexibility** and **fault tolerance**

---

## Storage Types
| Storage Type   | Used With | Acts Like      | Good For                  |
|----------------|-----------|----------------|---------------------------|
| **Block Storage (EBS)** | EC2        | Hard Disk/SSD | OS, databases, app files |
| **Object Storage (S3)** | Any app    | Online Drive   | Images, backups, logs    |

- **Block Storage (EBS):** Like a laptop’s SSD (tied to OS).
- **Object Storage (S3):** Like Google Drive (independent of machine).

---

## Persisting Data After Instance Stops
- Default **ephemeral storage** → data is lost when stopped.
- To persist data:
  - **EBS Volumes:** attach/detach like external drives
  - **S3:** store large files/backups
- Options:
  - Detach volume before shutdown
  - Take snapshots (backup)
  - Reattach volume later

---

## Pricing Models
| Type        | Pricing              | Best Use              | Limitation              |
|-------------|----------------------|-----------------------|-------------------------|
| **On-Demand** | Pay per hour/second  | Short tasks, testing  | Most expensive          |
| **Reserved**  | 1–3 year commitment  | Long-term apps        | Upfront cost            |
| **Spot**      | Up to 90% cheaper    | Batch jobs, flexible  | Can be terminated anytime |

- **Spot = airline clearance sale** (cheap, but not guaranteed).

---

## IP Address Types
| IP Type      | Visible To | Changes on Reboot? | Purpose                          |
|--------------|------------|--------------------|----------------------------------|
| **Public IP**  | Internet   | Yes                | Temporary access                 |
| **Elastic IP** | Internet   | No                 | Permanent IP for production apps |
| **Internal IP**| Private    | No                 | Communication between EC2s       |

- Use **Elastic IP** for static apps/domains.

---

## Monitoring & Alerts
- Use **CloudWatch** for:
  - CPU, disk, network traffic, memory
- Set alarms:
  - Example: **“CPU > 80% for 5 min → Send Email”**
- Acts like a **smoke alarm** for EC2.

---

## Security Groups (Firewall)
- EC2 lives inside a **VPC (Virtual Private Cloud)**.
- **Security Groups** = Firewall rules for EC2.
- Rules:
  - Block all traffic by default
  - Allow specific access:
    - TCP 22 (SSH) from your IP
    - TCP 80/443 (Web traffic)
- Think of it as **keys to specific doors**, not whole building.

---

## Using EC2
### GUI (AWS Console):
1. Go to **EC2 Dashboard**
2. Click **Launch Instance**
3. Choose OS, type, storage, security
4. Launch and **SSH into instance**

### CLI (Command Line):
```bash
aws ec2 run-instances \
  --image-id ami-xxxx \
  --instance-type t2.micro \
  --key-name my-key \
  --security-group-ids sg-xxxx \
  --subnet-id subnet-xxxx
```
- Useful for automation, DevOps, scripting.
---

## Exercise
1. Launch an EC2 instance from AWS Console.
2. SSH into it.
3. Install NGINX (`sudo apt install nginx`).
4. Open public IP → See **"Hello Web!"** page.
5. Stop & relaunch instance → Notice **public IP changes**.
6. Allocate an **Elastic IP** → Attach to make IP permanent.
### Bonus Tasks
- Create a **CloudWatch alarm** for high CPU.
- Create an **EBS volume, attach, format, and mount** it.
