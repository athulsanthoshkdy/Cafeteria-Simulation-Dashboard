import random

def random_time(mean, half_range):
    """Generate random time with ± range"""
    return random.triangular(mean - half_range, mean + half_range, mean)

# ============================================================================
# INITIALIZE VARIABLES
# ============================================================================
current_time = 0
total_arrivals = 0
customers_left = 0

# Queue counts
sandwich_queue_count = 0
main_queue_count = 0
cashier_queue_count = 0
eating_count = 0
dessert_count = 0

# Server status
sandwich_busy = False
main_busy = False
cashier_busy = False

# Finish times (when will service complete?)
next_arrival_time = 0
sandwich_finish_time = float('inf')
main_finish_time = float('inf')
cashier_finish_time = float('inf')

# Lists to track finish times (but no customer IDs)
eating_finish_times = []      # [(finish_time, wants_dessert), ...]
dessert_finish_times = []     # [finish_time, ...]

# ============================================================================
# MAIN SIMULATION LOOP
# ============================================================================
print("Starting cafeteria simulation...")
print("="*60)

while customers_left < 100:
    current_time += 1  # Advance 1 second at a time
    
    # ========================================
    # CHECK 1: New customer arrival?
    # ========================================
    if current_time >= next_arrival_time:
        total_arrivals += 1
        
        # Schedule next arrival (30 ± 20 seconds)
        next_arrival_time = current_time + random_time(30, 20)
        
        # Decide which counter (40% sandwich, 60% main)
        if random.random() < 0.4:
            sandwich_queue_count += 1
        else:
            main_queue_count += 1
    
    # ========================================
    # CHECK 2: Sandwich worker finished?
    # ========================================
    if sandwich_busy and current_time >= sandwich_finish_time:
        sandwich_busy = False
        cashier_queue_count += 1
    
    # ========================================
    # CHECK 3: Main worker finished?
    # ========================================
    if main_busy and current_time >= main_finish_time:
        main_busy = False
        cashier_queue_count += 1
    
    # ========================================
    # CHECK 4: Cashier finished?
    # ========================================
    if cashier_busy and current_time >= cashier_finish_time:
        cashier_busy = False
        eating_count += 1
        
        # Schedule eating finish (20 ± 10 minutes = 1200 ± 600 seconds)
        eating_finish = current_time + random_time(1200, 600)
        wants_dessert = random.random() < 0.1
        eating_finish_times.append((eating_finish, wants_dessert))
    
    # ========================================
    # CHECK 5: Start sandwich service if possible
    # ========================================
    if not sandwich_busy and sandwich_queue_count > 0:
        sandwich_busy = True
        sandwich_queue_count -= 1
        # Service takes 60 ± 30 seconds
        sandwich_finish_time = current_time + random_time(60, 30)
    
    # ========================================
    # CHECK 6: Start main service if possible
    # ========================================
    if not main_busy and main_queue_count > 0:
        main_busy = True
        main_queue_count -= 1
        # Service takes 45 ± 30 seconds
        main_finish_time = current_time + random_time(45, 30)
    
    # ========================================
    # CHECK 7: Start cashier service if possible
    # ========================================
    if not cashier_busy and cashier_queue_count > 0:
        cashier_busy = True
        cashier_queue_count -= 1
        # Service takes 25 ± 10 seconds
        cashier_finish_time = current_time + random_time(25, 10)
    
    # ========================================
    # CHECK 8: Anyone finished eating?
    # ========================================
    for i in range(len(eating_finish_times) - 1, -1, -1):
        finish_time, wants_dessert = eating_finish_times[i]
        
        if current_time >= finish_time:
            eating_count -= 1
            eating_finish_times.pop(i)
            
            if wants_dessert:
                dessert_count += 1
                # Dessert takes 10 ± 2 minutes = 600 ± 120 seconds
                dessert_finish = current_time + random_time(600, 120)
                dessert_finish_times.append(dessert_finish)
            else:
                customers_left += 1
    
    # ========================================
    # CHECK 9: Anyone finished dessert?
    # ========================================
    for i in range(len(dessert_finish_times) - 1, -1, -1):
        finish_time = dessert_finish_times[i]
        
        if current_time >= finish_time:
            dessert_count -= 1
            dessert_finish_times.pop(i)
            customers_left += 1

# ============================================================================
# SIMULATION COMPLETE - REPORT RESULTS
# ============================================================================
total_remaining = (sandwich_queue_count + main_queue_count + 
                   cashier_queue_count + eating_count + dessert_count +
                   int(sandwich_busy) + int(main_busy) + int(cashier_busy))

print("="*60)
print("SIMULATION COMPLETE")
print("="*60)
print(f"Simulation time: {current_time} seconds ({current_time/60:.1f} minutes)")
print(f"Total arrivals: {total_arrivals}")
print(f"Customers left: {customers_left}")
print(f"\nCustomers remaining in cafeteria: {total_remaining}")
print("-"*60)
print(f"  Sandwich queue: {sandwich_queue_count}")
print(f"  Main queue: {main_queue_count}")
print(f"  Cashier queue: {cashier_queue_count}")
print(f"  Currently eating: {eating_count}")
print(f"  Having dessert: {dessert_count}")
print(f"  Being served at sandwich: {int(sandwich_busy)}")
print(f"  Being served at main: {int(main_busy)}")
print(f"  Being served at cashier: {int(cashier_busy)}")
print("="*60)
