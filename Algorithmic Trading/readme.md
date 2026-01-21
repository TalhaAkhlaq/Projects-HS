# Algorithmic Trading

## Overview
- Real-time crypto market data via Bybit REST/WebSocket (ticks + order book) with indicator-driven signals (EMA, RSI, Bollinger Bands, VWAP, Kalman filter) and risk controls (slippage, stop-loss, drawdown limits, Kelly Criterion position sizing)

## Implementation
- JSON tick/order book parsing into timestamp-indexed circular buffers; bid-ask spreads, mid-price velocity (discrete derivatives), rolling volatility (Welford)
- Log-return processing; QR decomposition for covariance handling; Newton-Raphson and imbalance-based execution; latency handling (delay measurement, NTP sync)

## Contents
- `Stock API/` - Market data ingestion and processing
- `Stock Data/` - Data collection and analysis utilities
- `Trading Bot/` - Trading bot prototype using real-time data streams
- `main.py`, `screener.py` - Additional scripts and experiments
