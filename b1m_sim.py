import math

def calculate_b1m_ark():
    # --- CONFIGURATION ---
    EPOCHS = 10
    TOKENS_PER_EPOCH = 21000
    ELDER_SUPPLY = 21
    ELDER_PRICE_BTC = 2.1
    
    # Starting and Ending target prices for the ladder
    start_price = 2100
    end_price = 210000
    
    # Calculate the exponential growth rate (multiplier)
    # Price_n = Price_1 * (multiplier)^(n-1)
    multiplier = (end_price / start_price) ** (1 / (EPOCHS - 1))
    
    print("🚢 B1M ARK PROTOCOL: MATHEMATICAL VERIFICATION")
    print("-" * 50)
    
    total_ladder_sats = 0
    
    # --- 10-EPOCH LADDER CALCULATION ---
    for n in range(1, EPOCHS + 1):
        # Calculate price for current epoch
        price = round(start_price * (multiplier ** (n - 1)))
        
        # Override epoch 10 to exactly 210,000 for clean alignment
        if n == 10: price = 210000
            
        epoch_total = price * TOKENS_PER_EPOCH
        total_ladder_sats += epoch_total
        
        print(f"Epoch {n:2}: {price:7} Sats | Total: {epoch_total/1e8:9.4f} BTC")

    # --- ELDER PLANK CALCULATION ---
    elder_total_sats = int(ELDER_PRICE_BTC * 1e8) * ELDER_SUPPLY
    
    print("-" * 50)
    print(f"ELDER SERIES: {ELDER_PRICE_BTC} BTC each x {ELDER_SUPPLY} units")
    print(f"Elder Total: {elder_total_sats/1e8:11.2f} BTC")
    print("-" * 50)
    
    # --- FINAL TALLY ---
    grand_total_sats = total_ladder_sats + elder_total_sats
    print(f"GRAND TOTAL TREASURY: {grand_total_sats/1e8:,.2f} BTC")
    print(f"SATS TOTAL: {grand_total_sats:,} Sats")

if __name__ == "__main__":
    calculate_b1m_ark()