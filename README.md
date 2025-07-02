# Subnet Analyzer Tool

This tool analyzes IP addresses and subnets from an Excel file, generates a detailed CSV report, and creates a bar chart showing the number of usable hosts per subnet.

---

## 📁 Project Structure

```
.
├── Dockerfile
├── ip_data.xlsx
├── requirements.txt
├── subnet_analyzer.py
├── visualize.py
├── entrypoint.sh
├── README.md
├── subnet_report.csv
├── summary_report.csv
├── network_plot.png

```

---

## 📂 Input

The tool reads from `ip_data.xlsx`.  
| IP Address | Subnet Mask |
|------------|--------------|

---

## 📂 Outputs

After running the tool, you’ll get these main output files:

### 1. `subnet_report.csv`

| IP Address | Subnet Mask | CIDR | Network Address | Broadcast Address | Usable Hosts | First Host | Last Host |
|------------|--------------|------|-----------------|-------------------|---------------|-------------|-----------|

- **Contains:** The full details for each input IP:
  - CIDR notation
  - Calculated network & broadcast addresses
  - Number of usable hosts
  - First and last usable host IPs


### 2. `summary_report.csv`

| Network Address | CIDR | Usable Hosts | IP Count |
|-----------------|------|---------------|----------|

- **Contains:** Grouped summary by unique subnets:
  - Total usable hosts per subnet
  - Count of how many IPs were in that subnet group



### 3. `network_plot.png`

- A **bar chart** showing the number of usable hosts per subnet.
- Saved as `network_plot.png` in the working directory.

---

## 🛠️ Tech Stack

- Python 3.10+
- Libraries: `pandas`, `ipaddress`, `matplotlib`, `openpyxl`
- Containerized using Docker

---

## 🚀 How to Run

**1. Build the Docker image**

```bash
docker build -t subnet-analyzer .
```

**2. Run the container**

```bash
docker run -v $PWD:/app subnet-analyzer
```

✅ The `-v $PWD:/app` flag mounts current folder into the container so that output files appear in local directory.

---

## 📹 Video Explanation

A short video of me explaining the solution:  
**➡️ [Watch the explanation](https://drive.google.com/file/d/1jfyxC5LD9a84c4lTMqgeeI-40GEhMTeu/view?usp=sharing)**  
