# Blockchain-Based Energy Trading Simulation ⚡🔗

## Overview
This project is a high-performance simulation of a decentralized energy trading system. It simulates an environment where 1,000 "prosumers" (households that both produce and consume energy) trade energy directly with each other using a custom-built blockchain architecture. 

As a Data Analysis project, the primary goal is to generate, process, and visualize transaction logs to identify network bottlenecks and system efficiency.

## Features
* **Blockchain Architecture:** Implements a basic cryptographic ledger using SHA-256 hashing to ensure transaction security and strict privacy metrics.
* **Prosumer Simulation:** Generates random trading data (energy volume and price) for 1,000 agents over a simulated 7-day period.
* **Data Analysis & Visualization:** Utilizes **NumPy** to process thousands of transaction logs and **Matplotlib** to build interactive visual dashboards showing network latency and trading distributions.

## Tech Stack
* **Language:** Python
* **Data Processing:** NumPy
* **Data Visualization:** Matplotlib
* **Security:** Hashlib (Standard Library)

## How to Run
1. Clone this repository.
2. Install the required dependencies:
   `pip install numpy matplotlib`
3. Run the simulation:
   `python main.py`
