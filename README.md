# Engine Council Project

## Overview
This project simulates a financial system where:
- **Pieces** represent indivisible units of value.
- **Engines** are trading algorithms that invest pieces in stocks.
- **Council** is a decision-making algorithm that reallocates pieces and adjusts strategy across engines.
- **All-bank** temporarily holds value waiting for reassignment.

The system runs in cycles:
1. **Period a (cash phase):** pieces are liquid, council may change value or stock identity.
2. **Period b (stock phase):** pieces are locked into stocks until sold.

The project will evolve from a toy simulation into a robust automated system with persistence, monitoring, and council intelligence.

## Quick start
```bash
python main.py
