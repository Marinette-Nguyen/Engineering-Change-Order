# ECO Management & Procurement Intelligence System

## 📌 Project Overview
In a complex electronics manufacturing environment with multi-level Bill of Materials (BOM), the Engineering Change Order (ECO) process faced significant operational bottlenecks. This project provides an end-to-end automation suite to streamline ECO tracking, impact analysis, and mass approvals.

### 🔴 The Challenges (Pain Points)
* **BOM Complexity:** Standard databases only showed single-level changes. Planners spent hours manually tracing impacts down to the "Buy" component level, leading to high error rates.
* **Communication Gaps:** ECO Coordinators manually collected approvals from Buyers/Planners via email. Lack of automated triggers led to missing information and delayed replies.
* **SLA Pressure:** Manual tracking resulted in lead times exceeding the 2-day target, causing internal complaints and supply chain delays.

---

## 🛠 Tech Stack & Solutions
I developed an integrated system using a multi-tool approach:

### 1. Deep-Level BOM Analysis (Python)
* **Tool:** `Python (Pandas)`
* **Solution:** Developed a script to traverse complex BOM structures, automatically identifying which "Buy" components are affected by an ECO. This transformed raw data into actionable intelligence for Planners.

### 2. Communication & Response Collection (VBA)
* **Tool:** `VBA (Excel & Outlook)`
* **Solution:** Automated the distribution of ECO impact reports to relevant stakeholders and implemented a system to collect and consolidate email responses/approvals into a central tracker.

### 3. Mass Action Automation (Playwright)
* **Tool:** `Playwright (Python)`
* **Solution:** Built a high-performance bot to handle bulk **Approve/Reject/Schedule** actions on the Oracle ERP (E-Business Suite) web interface.
* **Key Features:** Managed persistent browser contexts and multi-tab workflows to eliminate manual data entry.

### 4. Operational Dashboard (Power BI)
* **Tool:** `Power BI`
* **Solution:** Created a "Single Source of Truth" dashboard to monitor ECO status, approval aging, and team workload, ensuring 100% visibility.

---

## 📈 Key Results
* **SLA Optimization:** Successfully reduced ECO processing lead time to consistently meet the **<2-day SLA**.
* **Zero Mapping Errors:** Eliminated human error in identifying component-level impacts.
* **Process Digitalization:** Replaced fragmented individual tracking with a centralized, automated workflow.

---
