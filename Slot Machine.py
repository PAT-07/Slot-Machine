import streamlit as st
import random

# Constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

symbols_count = {
    "🍒": 2,
    "🍋": 4,
    "🍊": 6,
    "🍇": 8,
}

symbols_value = {
    "🍒": 5,
    "🍋": 4,
    "🍊": 3,
    "🍇": 2,
}

# Initialize session state
if 'balance' not in st.session_state:
    st.session_state.balance = 0
if 'total_won' not in st.session_state:
    st.session_state.total_won = 0
if 'total_bet' not in st.session_state:
    st.session_state.total_bet = 0
if 'spins' not in st.session_state:
    st.session_state.spins = 0

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def display_slot_machine(columns, winning_lines):
    st.markdown("### 🎰 Slot Machine 🎰")
    for row in range(len(columns[0])):
        line_won = (row + 1) in winning_lines
        cols_display = st.columns(5)
        
        with cols_display[0]:
            if line_won:
                st.markdown(f"**→**")
        
        with cols_display[1]:
            st.markdown(f"<h1 style='text-align: center; margin: 0;'>{columns[0][row]}</h1>", unsafe_allow_html=True)
        with cols_display[2]:
            st.markdown(f"<h1 style='text-align: center; margin: 0;'>{columns[1][row]}</h1>", unsafe_allow_html=True)
        with cols_display[3]:
            st.markdown(f"<h1 style='text-align: center; margin: 0;'>{columns[2][row]}</h1>", unsafe_allow_html=True)
        
        with cols_display[4]:
            if line_won:
                st.markdown(f"**←**")

# Streamlit UI
st.set_page_config(page_title="Slot Machine Game", page_icon="🎰", layout="centered")

st.title("🎰 Slot Machine Game 🎰")
st.markdown("---")

# Sidebar for balance and stats
with st.sidebar:
    st.header("💰 Game Stats")
    st.metric("Balance", f"${st.session_state.balance}")
    st.metric("Total Spins", st.session_state.spins)
    st.metric("Total Won", f"${st.session_state.total_won}")
    st.metric("Total Bet", f"${st.session_state.total_bet}")
    
    if st.session_state.total_bet > 0:
        roi = ((st.session_state.total_won - st.session_state.total_bet) / st.session_state.total_bet) * 100
        st.metric("ROI", f"{roi:.1f}%")
    
    st.markdown("---")
    st.subheader("💎 Payout Values")
    for symbol, value in symbols_value.items():
        st.write(f"{symbol} = {value}x bet")
    
    st.markdown("---")
    if st.button("Reset Game", type="secondary"):
        st.session_state.balance = 0
        st.session_state.total_won = 0
        st.session_state.total_bet = 0
        st.session_state.spins = 0
        st.rerun()

# Main game area
if st.session_state.balance == 0:
    st.info("👋 Welcome! Please deposit money to start playing.")
    deposit_amount = st.number_input("Deposit Amount ($)", min_value=1, max_value=10000, value=100, step=10)
    if st.button("💵 Deposit", type="primary"):
        st.session_state.balance = deposit_amount
        st.success(f"Successfully deposited ${deposit_amount}!")
        st.rerun()
else:
    st.success(f"Current Balance: **${st.session_state.balance}**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        lines = st.selectbox("Number of Lines", options=[1, 2, 3], index=0)
    
    with col2:
        bet = st.slider("Bet per Line ($)", min_value=MIN_BET, max_value=MAX_BET, value=10)
    
    total_bet = bet * lines
    st.info(f"Total Bet: **${total_bet}** (${bet} × {lines} lines)")
    
    if total_bet > st.session_state.balance:
        st.error(f"⚠️ Insufficient balance! You need ${total_bet} but only have ${st.session_state.balance}")
    else:
        if st.button("🎰 SPIN!", type="primary", use_container_width=True):
            # Deduct bet
            st.session_state.balance -= total_bet
            st.session_state.total_bet += total_bet
            st.session_state.spins += 1
            
            # Spin the slot machine
            slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
            winnings, winning_lines = check_winnings(slots, lines, bet, symbols_value)
            
            # Update balance
            st.session_state.balance += winnings
            st.session_state.total_won += winnings
            
            # Display results
            st.markdown("---")
            display_slot_machine(slots, winning_lines)
            st.markdown("---")
            
            net_result = winnings - total_bet
            
            if winnings > 0:
                st.success(f"🎉 YOU WON ${winnings}! (Net: ${net_result:+d})")
                st.balloons()
                if winning_lines:
                    st.write(f"Winning lines: {', '.join(map(str, winning_lines))}")
            else:
                st.error(f"😞 No win this time. (Net: ${net_result:+d})")
            
            st.info(f"New Balance: **${st.session_state.balance}**")
            
            if st.session_state.balance == 0:
                st.warning("💸 You're out of money! Deposit more to continue playing.")

st.markdown("---")
st.caption("Good luck! 🍀")
