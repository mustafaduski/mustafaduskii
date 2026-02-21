import ccxt
import pandas as pd
import pandas_ta as ta

def analyze_crypto_and_gold():
    print("🤖 Quantum Engine: Starting Market Analysis...")
    exchange = ccxt.binance()
    
    # لیستی ئەو شتانەی بۆتەکە چاودێرییان دەکات
    assets = {
        'BTC/USDT': 'Bitcoin',
        'ETH/USDT': 'Ethereum',
        'BNB/USDT': 'Binance Coin'
    }

    print("="*40)
    for symbol, name in assets.items():
        try:
            # وەرگرتنی داتای نرخەکان (Candlesticks)
            ohlcv = exchange.fetch_ohlcv(symbol, timeframe='1h', limit=50)
            df = pd.DataFrame(ohlcv, columns=['time', 'open', 'high', 'low', 'close', 'vol'])
            
            # حیسابکردنی RSI (بۆ زانینی ئەوەی نرخ زۆر بەرزە یان نزم)
            df['RSI'] = ta.rsi(df['close'], length=14)
            current_rsi = df['RSI'].iloc[-1]
            current_price = df['close'].iloc[-1]

            print(f"💎 {name} ({symbol}):")
            print(f"   Price: ${current_price:,.2f}")
            print(f"   RSI: {current_rsi:.2f}")

            # بڕیاردانی بۆتەکە (Logic)
            if current_rsi < 30:
                print("   🚀 SIGNAL: OVERSOLD (Strong Buy Opportunity)")
            elif current_rsi > 70:
                print("   ⚠️ SIGNAL: OVERBOUGHT (Potential Sell/Take Profit)")
            else:
                print("   ✅ SIGNAL: NEUTRAL (Wait for better entry)")
            print("-" * 20)

        except Exception as e:
            print(f"❌ Error analyzing {symbol}: {e}")

if __name__ == "__main__":
    analyze_market_start_time = pd.Timestamp.now()
    analyze_crypto_and_gold()
    print(f"✅ Analysis Complete at: {analyze_market_start_time}")
