import hashlib
import time
import random
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# PART 1: BLOCKCHAIN & NETWORK ARCHITECTURE
# ==========================================
class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions  # List of trades
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Cryptographic hashing for privacy & security (Resume bullet 2)
        block_data = f"{self.index}{self.timestamp}{self.transactions}{self.previous_hash}"
        return hashlib.sha256(block_data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []
        self.transaction_logs = [] # To store data for analysis

    def create_genesis_block(self):
        return Block(0, ["Genesis Block"], "0")

    def add_transaction(self, sender, receiver, energy_amount, price):
        # Simulating transaction creation
        tx = {
            "sender": sender,
            "receiver": receiver,
            "energy_kWh": energy_amount,
            "price": price,
            "req_time": time.time()
        }
        self.pending_transactions.append(tx)

    def mine_pending_transactions(self):
        if not self.pending_transactions:
            return

        # Simulating network latency / bottleneck (Processing max 50 tx per block)
        tx_to_process = self.pending_transactions[:50]
        self.pending_transactions = self.pending_transactions[50:]

        new_block = Block(len(self.chain), tx_to_process, self.chain[-1].hash)
        self.chain.append(new_block)

        # Log metrics for data analysis (Resume bullet 3)
        process_time = time.time()
        for tx in tx_to_process:
            latency = (process_time - tx["req_time"]) * 1000 # in milliseconds
            # Adding some random network delay jitter
            latency += random.uniform(10, 200) 
            self.transaction_logs.append({
                "block_id": new_block.index,
                "latency_ms": latency,
                "energy_traded": tx["energy_kWh"]
            })

# ==========================================
# PART 2: PROSUMER SIMULATION (1000 Users)
# ==========================================
def run_simulation(num_prosumers=1000, days=7):
    print(f"Starting Simulation with {num_prosumers} prosumers over {days} days...")
    network = Blockchain()
    
    # Run the simulation for a set number of "hours" (7 days * 24 hours)
    for hour in range(days * 24):
        # 1. Prosumers generate/consume energy
        # Randomly select buyers (deficits) and sellers (surplus)
        num_trades_this_hour = random.randint(20, 150) # Network load fluctuates
        
        for _ in range(num_trades_this_hour):
            seller_id = f"Prosumer_{random.randint(1, num_prosumers)}"
            buyer_id = f"Prosumer_{random.randint(1, num_prosumers)}"
            energy_kwh = round(random.uniform(1.0, 15.0), 2)
            price_per_kwh = round(random.uniform(3.0, 7.5), 2)
            
            if seller_id != buyer_id:
                network.add_transaction(seller_id, buyer_id, energy_kwh, price_per_kwh)
        
        # 2. Mine blocks (Process the trades)
        # Sometime network is congested, taking multiple blocks to clear mempool
        while network.pending_transactions:
            network.mine_pending_transactions()
            
    print("Simulation Complete. Blockchain Ledger and Logs generated.")
    return network.transaction_logs

# ==========================================
# PART 3: DATA ANALYSIS & VISUALIZATION
# ==========================================
def analyze_and_visualize(logs):
    print("Analyzing logs using NumPy and Matplotlib...")
    
    # Extract data into NumPy arrays for fast computation
    latencies = np.array([log["latency_ms"] for log in logs])
    block_ids = np.array([log["block_id"] for log in logs])
    energy_volumes = np.array([log["energy_traded"] for log in logs])
    
    # Find bottlenecks (Blocks with highest average latency)
    unique_blocks = np.unique(block_ids)
    avg_latency_per_block = [np.mean(latencies[block_ids == b]) for b in unique_blocks]
    
    # Setup Matplotlib Dashboard (Resume bullet 3)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # Plot 1: Network Bottlenecks (Latency over time)
    ax1.plot(unique_blocks, avg_latency_per_block, color='red', alpha=0.7)
    ax1.set_title("Network Bottleneck Analysis: Transaction Latency per Block")
    ax1.set_xlabel("Block Number (Time)")
    ax1.set_ylabel("Average Latency (ms)")
    ax1.axhline(y=np.mean(latencies), color='blue', linestyle='--', label="Avg Latency")
    ax1.legend()
    ax1.grid(True, linestyle=':', alpha=0.6)
    
    # Plot 2: System Efficiency (Energy Traded)
    ax2.hist(energy_volumes, bins=30, color='green', alpha=0.7, edgecolor='black')
    ax2.set_title("System Efficiency: Distribution of Energy Traded (kWh)")
    ax2.set_xlabel("Energy Amount (kWh)")
    ax2.set_ylabel("Frequency of Trades")
    ax2.grid(True, linestyle=':', alpha=0.6)
    
    plt.tight_layout()
    plt.show()

# Run the full pipeline
if __name__ == "__main__":
    simulation_logs = run_simulation(num_prosumers=1000, days=7)
    analyze_and_visualize(simulation_logs)
