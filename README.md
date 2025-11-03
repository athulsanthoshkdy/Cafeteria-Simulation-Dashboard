# Cafeteria-Simulation-Dashboard

People arrive at a self-service cafeteria at the rate of one every 30 ± 20 seconds. Forty percent go to the sandwich counter, where one worker makes a sandwich in 60 ± 30 seconds. The rest go to the main counter, where one server spoons the prepared meal onto a plate in 45 ± 30 seconds. All customers must pay a single cashier, which takes 25 ± 10 seconds. For all customers, eating takes 20 ± 10 minutes. After eating, 10% of the people go back for dessert, spending an additional 10 ± 2 minutes altogether in the cafeteria. Simulate until 100 people have left the cafeteria. How many people are left in the cafeteria, and what are they doing, at the time the simulation stops?


### 🧩 Problem Summary

People arrive randomly at a self-service cafeteria, move through several stages (choosing food, paying, eating, possibly having dessert), and then leave. We want to **simulate this process** until **100 people have left** the cafeteria. When that happens, we must determine **how many people are still inside** and **what they are doing**.

---

### ⚙️ Given Information

| Step                   | Description                            | Time (mean ± variation) | Notes                     |
| ---------------------- | -------------------------------------- | ----------------------- | ------------------------- |
| **Arrival**            | One person every 30 ± 20 seconds       | 10–50 sec               | Random interarrival times |
| **Choice**             | 40% sandwich counter, 60% main counter | –                       | Determines service path   |
| **Sandwich Counter**   | Sandwich made                          | 60 ± 30 sec             | 1 worker, queue possible  |
| **Main Counter**       | Meal served                            | 45 ± 30 sec             | 1 worker, queue possible  |
| **Cashier**            | Payment                                | 25 ± 10 sec             | Single cashier for all    |
| **Eating**             | Eat meal                               | 20 ± 10 minutes         | 10–30 min eating time     |
| **Dessert (optional)** | 10% go for dessert                     | 10 ± 2 minutes          | Adds to total time        |

---

### 🧮 Simulation Process (Conceptually)

1. **Generate arrivals:** Each person’s arrival time = previous arrival time + random(10–50 sec).
2. **Assign counter:** 40% → sandwich queue, 60% → main queue.
3. **Serve food:** Each counter handles one person at a time; compute waiting + service time.
4. **Pay cashier:** Single queue; add cashier time (random 15–35 sec).
5. **Eat:** After paying, each person spends random(10–30 min).
6. **Dessert:** 10% go for dessert, add random(8–12 min).
7. **Track departures:** Continue until 100 people have left the cafeteria.

---

### 💡 Expected Outcome

When the 100th customer leaves:

* Some customers will **still be eating**, since eating takes much longer than service.
* A few may be **having dessert**.
* Possibly a couple may be **waiting to pay** or just **finished eating**.

Based on typical random outcomes in such a system:

* **About 30–40 people** are likely still in the cafeteria.
* Most (~90%) are **eating**, a few (~2–4) are **having dessert**, and maybe **1–2** are still **in service** or **paying**.

---
