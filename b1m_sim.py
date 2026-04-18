# B1M Sovereign Engine - Manifesto v5.2 Corrected
def run_manifesto_simulation():
    # Price points taken directly from the B1M Manifesto table
    manifesto_prices = [
        2100, 3503, 5843, 9747, 16260, 
        27123, 45243, 75470, 125892, 210000
    ]
    
    supply_per_epoch = 21000
    total_distributed = 0

    print("--- B1M ETERNAL STRIKE: OFFICIAL LADDER ---")
    for i, price in enumerate(manifesto_prices):
        epoch = i + 1
        total_distributed += supply_per_epoch
        
        # Calculate the 20% "Mission Harvest" for the Arusha Storehouse
        harvest_sats = (supply_per_epoch * price) * 0.20
        
        print(f"Epoch {epoch}:")
        print(f"  Price:     {price:>7} sats")
        print(f"  Harvest:   {int(harvest_sats):>7} sats (20% Mission Reserve)")
        print(f"  Progress:  {total_distributed:>7} / 210,000 units")
        print("-" * 40)

if __name__ == "__main__":
    run_manifesto_simulation()