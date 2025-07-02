# 📑 Subnet Questions Answers

---

## 1️⃣ Which subnet has the most hosts?

**Answer:**  
- The subnet(s) with mask `255.255.252.0` (**CIDR /22**) have the most usable hosts: **1022**.

**How:**  
- Usable hosts = `2^(32 - prefix length) - 2`
  - `/22` → `2^(32-22) - 2 = 1022`
  - `/23` → `2^(32-23) - 2 = 510`
  - `/24` → `2^(32-24) - 2 = 254`

---

## 2️⃣ Are there any overlapping subnets?

**Answer:**  
- **No overlapping subnets** in this dataset.

**How:**  
- Each IP is turned into a `Network Address` and `CIDR` using its original subnet mask.
- The script also calculates the **usable host range** (`First Host` to `Last Host`) for each subnet.
- These ranges are included in `report.csv`.
- By checking these start–end ranges, we can verify that no two ranges overlap — each block is unique.


---

## 3️⃣ What is the smallest and largest subnet?

**Answer:**  
- **Largest:** `/22` → `1022` usable hosts.
- **Smallest:** `/24` → `254` usable hosts.

**How:**  
- Calculated by: `2^(32 - prefix length) - 2`.
- `/22` → `2^(10)` = 1024 → minus 2.
- `/24` → `2^(8)` = 256 → minus 2.

---

## 4️⃣ Suggested subnetting strategy to reduce waste

**Answer:**  
- **Split larger blocks** (`/22`, `/23`) into smaller subnets (`/25`, `/26`) that match real usage.
- Combine low-usage hosts together.
- Use VLANs or NAT if needed to minimize unused address space.

**How:**  
- Subnet mask math: smaller blocks = fewer wasted IPs.
- For example: `/26` → 62 usable hosts instead of 1022.