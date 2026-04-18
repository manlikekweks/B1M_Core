import random

def run_manifesto_simulation():
    # Price points from B1M Manifesto v5.2
    manifesto_prices = [2100, 3503, 5843, 9747, 16260, 27123, 45243, 75470, 125892, 210000]
    supply_per_epoch = 21000
    total_distributed = 0

    print("--- B1M ETERNAL STRIKE: OFFICIAL LADDER ---")
    for i, price in enumerate(manifesto_prices):
        epoch = i + 1
        total_distributed += supply_per_epoch
        harvest_sats = (supply_per_epoch * price) * 0.20
        print(f"Epoch {epoch}: Price {price:>7} sats | Harvest: {int(harvest_sats):>9} sats")
    return 420  # Simulating 420 units of "Dead Stock" for the Ghost Protocol test

def run_ghost_protocol_sim(dead_stock_count):
    print("\n--- GHOST PROTOCOL ACTIVATION: THE INVENTORY REVIVER ---")
    print(f"Activation: 00:00 - 21:00 UTC | Target: {dead_stock_count} Dead Stock units")
    
    slots = 42  # One auction every 30 minutes [cite: 29]
    window = 21 # Each auction lasts 21 minutes 
    
    for slot in range(1, slots + 1):
        if dead_stock_count <= 0:
            break
            
        # Tokens appear like "Rare Pokemon" [cite: 31]
        revived_this_slot = random.randint(0, 21) 
        dead_stock_count -= revived_this_slot
        
        status = f"[STRIKE] {revived_this_slot} tokens revived" if revived_this_slot > 0 else "[SIGNAL] Scanning..."
        print(f"Slot {slot:02} (30m): {status} | Window: {window} mins")

    print(f"\n--- GHOST PROTOCOL SETTLED | Remaining Dead Stock: {max(0, dead_stock_count)} ---")

if __name__ == "__main__":
    remnants = run_manifesto_simulation()
    run_ghost_protocol_sim(remnants)