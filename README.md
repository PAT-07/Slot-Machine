# 🎰 Animated Slot Machine Game

An interactive slot machine game built with Python and Streamlit, featuring animated spinning effects, real-time balance tracking, and a modern web interface.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Features

- 🎰 **Animated Spinning Effect** - Watch symbols spin and slow down like a real slot machine
- 💰 **Real-time Balance Tracking** - Monitor your money as you play
- 🎯 **Multi-line Betting System** - Bet on 1-3 lines simultaneously
- 📊 **Live Statistics Dashboard** - Track ROI, total wins, total bets, and spin count
- 🎨 **Visual Win Indicators** - Gold glow effects and arrows highlight winning lines
- 🎉 **Win Animations** - Celebrate victories with balloon animations
- 📱 **Responsive Web Interface** - Clean, modern design that works on any device
- 💎 **Customizable Symbols** - Easy to modify emojis and payout values

## 🎮 Demo

```
    🎰 Slot Machine 🎰
    ➤  🍒  🍒  🍒  ➤   ← Winning line!
       🍋  🍊  🍇
       🍇  🍇  🍇
```

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/PAT-07/slot-machine-game.git
   cd slot-machine-game
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit
   ```

3. **Run the application**
   ```bash
   streamlit run slot_machine.py
   ```

4. **Open in browser**
   - The app will automatically open at `http://localhost:8501`
   - If not, manually navigate to the URL shown in the terminal

## 🎲 How to Play

1. **Deposit Money** - Start by depositing funds (default: $100)
2. **Select Lines** - Choose how many lines to bet on (1-3)
3. **Set Bet Amount** - Use the slider to set your bet per line ($1-$100)
4. **Hit SPIN!** - Click the big spin button and watch the magic happen
5. **Win Big** - Match symbols across lines to multiply your bet!

## 🏆 Game Rules

### Symbol Values (Payout Multipliers)
| Symbol | Multiplier | Rarity |
|--------|-----------|--------|
| 🍒 Cherry | 5x | Rare |
| 🍋 Lemon | 4x | Uncommon |
| 🍊 Orange | 3x | Common |
| 🍇 Grape | 2x | Very Common |

### Winning Conditions
- All three symbols in a line must match
- Only lines you bet on count toward winnings
- Winnings = Symbol Value × Bet Amount per line

### Example
```
Bet: $10 per line on 3 lines
Total Bet: $30

Result:
Line 1: 🍒 🍒 🍒  → Win $50 (5 × $10)
Line 2: 🍋 🍊 🍇  → No win
Line 3: 🍇 🍇 🍇  → Win $20 (2 × $10)

Total Win: $70
Net Profit: $70 - $30 = +$40
```

## 📊 Statistics Tracked

The sidebar displays comprehensive game statistics:
- **Current Balance** - Your available funds
- **Total Spins** - Number of times you've played
- **Total Won** - Cumulative winnings across all spins
- **Total Bet** - Cumulative amount wagered
- **ROI (Return on Investment)** - Your profit/loss percentage

## 🛠️ Customization

### Change Symbols
Edit the `symbols_count` dictionary to modify symbols and their frequency:
```python
symbols_count = {
    "💎": 2,   # Rare (high value)
    "🔔": 4,   # Uncommon
    "⭐": 6,   # Common
    "7️⃣": 8,   # Very common (low value)
}
```

### Adjust Payouts
Modify the `symbols_value` dictionary:
```python
symbols_value = {
    "💎": 10,  # Higher multiplier
    "🔔": 5,
    "⭐": 3,
    "7️⃣": 2,
}
```

### Change Betting Limits
Adjust the constants at the top of the file:
```python
MAX_BET = 100   # Maximum bet per line
MIN_BET = 1     # Minimum bet per line
MAX_LINES = 3   # Maximum lines to bet on
```

### Modify Animation Speed
In the `display_slot_machine_animated()` function:
```python
spin_duration = 15  # Increase for longer animation
time.sleep(0.05 + (frame * 0.01))  # Adjust timing
```

## 🏗️ Technical Details

### Technology Stack
- **Python 3.x** - Core programming language
- **Streamlit** - Web application framework
- **Random Module** - Slot machine logic
- **Time Module** - Animation timing

### Architecture
```
slot_machine.py
├── Game Constants (symbols, values, limits)
├── Session State Management (balance, stats)
├── Core Functions
│   ├── check_winnings() - Calculate wins
│   ├── get_slot_machine_spin() - Generate results
│   ├── display_slot_machine_animated() - Spinning effect
│   └── display_slot_machine_final() - Final display
└── Streamlit UI
    ├── Sidebar (stats, payout table)
    ├── Deposit Section
    └── Game Controls (bet, spin)
```

### Key Features Explained

**Session State Management**
- Streamlit reruns the script on every interaction
- `st.session_state` preserves data between reruns
- Essential for maintaining balance and game state

**Animation System**
- Uses `st.empty()` to create updateable container
- Loops through random symbols with blur effect
- Progressive slowdown simulates real slot machine physics

**Responsive Layout**
- `st.columns()` creates flexible grid system
- Custom CSS widens sidebar and styles buttons
- Works seamlessly on desktop and mobile

## 📝 Code Structure

```python
# 1. Imports and Constants
import streamlit as st
import random
import time

# 2. Initialize Session State
if 'balance' not in st.session_state:
    st.session_state.balance = 0

# 3. Game Logic Functions
def check_winnings(columns, lines, bet, values):
    # Calculate winnings

# 4. Display Functions
def display_slot_machine_animated(placeholder):
    # Animated spinning effect

# 5. Streamlit UI
st.set_page_config(...)
st.title("🎰 Slot Machine Game 🎰")

# 6. Sidebar
with st.sidebar:
    st.metric("Balance", f"${balance}")

# 7. Main Game
if st.button("🎰 SPIN!"):
    # Spin logic
```


**⭐ If you like this project, please give it a star on GitHub! ⭐**

*Made with ❤️ and Python*
