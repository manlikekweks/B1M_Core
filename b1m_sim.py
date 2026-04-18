import json
import hashlib

def generate_b1m_contracts():
    # Manifesto Data [cite: 22]
    manifesto_prices = [2100, 3503, 5843, 9747, 16260, 27123, 45243, 75470, 125892, 210000]
    domain = "manlikekweks.com" # Your proof-of-authority domain [cite: 47]
    
    print("--- B1M SOVEREIGN ASSET REGISTRY MANIFEST ---")
    
    all_contracts = {}

    for i, price in enumerate(manifesto_prices):
        epoch = i + 1
        asset_name = f"B1M Epoch {epoch}"
        ticker = f"B1M.{epoch}"
        
        # This is the "Sovereign Contract" that Liquid nodes verify [cite: 13, 16]
        contract = {
            "entity": {"domain": domain},
            "issuer_pubkey": "MANLIKEKWEKS_GENESIS_PUBKEY", # To be replaced with your Liquid wallet pubkey
            "name": asset_name,
            "precision": 0, # B1M is issued in whole units [cite: 20]
            "ticker": ticker,
            "version": 0,
            "collection": "B1M_ETERNAL_STRIKE",
            "metadata": {
                "epoch": epoch,
                "genesis_price_sats": price,
                "royalty_bps": 210 # 2.1% Sovereign Fee 
            }
        }
        
        # Calculate a unique hash for this epoch's contract
        contract_json = json.dumps(contract, sort_keys=True)
        contract_hash = hashlib.sha256(contract_json.encode()).hexdigest()
        
        print(f"EPOCH {epoch}: {asset_name} ({ticker})")
        print(f"  Price: {price} sats")
        print(f"  Contract Hash: {contract_hash}")
        print("-" * 45)
        
        all_contracts[ticker] = contract

    # Save to a file for your registry upload
    with open("b1m_registry_contracts.json", "w") as f:
        json.dump(all_contracts, f, indent=4)
    print("\n[SUCCESS] Registry manifest saved to b1m_registry_contracts.json")

if __name__ == "__main__":
    generate_b1m_contracts()