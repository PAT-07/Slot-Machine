import streamlit as st
import random
import time

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

# All symbols for animation
ALL_SYMBOLS = ["🍒", "🍋", "🍊", "🍇", "7️⃣", "💎", "⭐", "🔔"]

# Initialize session state
if 'balance' not in st.session_state:
    st.session_state.balance = 0
if 'total_won' not in st.session_state:
    st.session_state.total_won = 0
if 'total_bet' not in st.session_state:
    st.session_state.total_bet = 0
if 'spins' not in st.session_state:
    st.session_state.spins = 0
if 'spinning' not in st.session_state:
    st.session_state.spinning = False
if 'final_slots' not in st.session_state:
    st.session_state.final_slots = None
if 'winning_lines' not in st.session_state:
    st.session_state.winning_lines = []

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

def display_slot_machine_animated(placeholder, winning_lines=[]):
    """Display animated spinning effect"""
    spin_duration = 15  # Number of animation frames
    
    for frame in range(spin_duration):
        # Generate random symbols for animation
        animated_slots = []
        for col in range(COLS):
            column = []
            for row in range(ROWS):
                column.append(random.choice(ALL_SYMBOLS))
            animated_slots.append(column)
        
        # Display the animated frame
        with placeholder.container():
            st.markdown("### 🎰 Slot Machine 🎰")
            for row in range(ROWS):
                cols_display = st.columns([1, 2, 2, 2, 1])
                
                with cols_display[0]:
                    st.markdown("")
                
                with cols_display[1]:
                    st.markdown(f"<h1 style='text-align: center; margin: 0; filter: blur(2px);'>{animated_slots[0][row]}</h1>", unsafe_allow_html=True)
                with cols_display[2]:
                    st.markdown(f"<h1 style='text-align: center; margin: 0; filter: blur(2px);'>{animated_slots[1][row]}</h1>", unsafe_allow_html=True)
                with cols_display[3]:
                    st.markdown(f"<h1 style='text-align: center; margin: 0; filter: blur(2px);'>{animated_slots[2][row]}</h1>", unsafe_allow_html=True)
                
                with cols_display[4]:
                    st.markdown("")
        
        # Slow down animation progressively
        time.sleep(0.05 + (frame * 0.01))
    
    # Show final result
    if st.session_state.final_slots:
        display_slot_machine_final(placeholder, st.session_state.final_slots, winning_lines)

def display_slot_machine_final(placeholder, columns, winning_lines):
    """Display final slot machine result with winning indicators"""
    with placeholder.container():
        st.markdown("### 🎰 Slot Machine 🎰")
        for row in range(len(columns[0])):
            line_won = (row + 1) in winning_lines
            cols_display = st.columns([1, 2, 2, 2, 1])
            
            with cols_display[0]:
                if line_won:
                    st.markdown(f"<h2 style='text-align: center; color: gold;'>➤</h2>", unsafe_allow_html=True)
                else:
                    st.markdown("")
            
            # Add glow effect for winning lines
            glow_style = "text-shadow: 0 0 20px gold, 0 0 30px gold;" if line_won else ""
            
            with cols_display[1]:
                st.markdown(f"<h1 style='text-align: center; margin: 0; {glow_style}'>{columns[0][row]}</h1>", unsafe_allow_html=True)
            with cols_display[2]:
                st.markdown(f"<h1 style='text-align: center; margin: 0; {glow_style}'>{columns[1][row]}</h1>", unsafe_allow_html=True)
            with cols_display[3]:
                st.markdown(f"<h1 style='text-align: center; margin: 0; {glow_style}'>{columns[2][row]}</h1>", unsafe_allow_html=True)
            
            with cols_display[4]:
                if line_won:
                    st.markdown(f"<h2 style='text-align: center; color: gold;'>➤</h2>", unsafe_allow_html=True)
                else:
                    st.markdown("")

# Streamlit UI
st.set_page_config(
    page_title="Slot Machine Game", 
    page_icon="🎰", 
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("🎰 Slot Machine Game 🎰")
st.markdown("---")

# Custom CSS to make sidebar wider and add styling
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        min-width: 350px;
        max-width: 350px;
    }
    [data-testid="stSidebar"] > div:first-child {
        width: 350px;
    }
    .stButton>button {
        font-size: 20px;
        font-weight: bold;
        padding: 15px 30px;
    }
    </style>
""", unsafe_allow_html=True)

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
        st.session_state.final_slots = None
        st.session_state.winning_lines = []
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
    
    # Placeholder for slot machine display
    slot_placeholder = st.empty()
    
    # Display current or final slots
    if st.session_state.final_slots:
        display_slot_machine_final(slot_placeholder, st.session_state.final_slots, st.session_state.winning_lines)
    
    if total_bet > st.session_state.balance:
        st.error(f"⚠️ Insufficient balance! You need ${total_bet} but only have ${st.session_state.balance}")
    else:
        if st.button("🎰 SPIN!", type="primary", use_container_width=True, disabled=st.session_state.spinning):
            # Set spinning state
            st.session_state.spinning = True
            
            # Deduct bet
            st.session_state.balance -= total_bet
            st.session_state.total_bet += total_bet
            st.session_state.spins += 1
            
            # Generate final slots
            final_slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
            st.session_state.final_slots = final_slots
            
            # Show spinning animation
            display_slot_machine_animated(slot_placeholder)
            
            # Calculate winnings
            winnings, winning_lines = check_winnings(final_slots, lines, bet, symbols_value)
            st.session_state.winning_lines = winning_lines
            
            # Update balance
            st.session_state.balance += winnings
            st.session_state.total_won += winnings
            
            # Display final result with winning lines
            display_slot_machine_final(slot_placeholder, final_slots, winning_lines)
            
            # Reset spinning state
            st.session_state.spinning = False
            
            # Show results
            st.markdown("---")
            net_result = winnings - total_bet
            
            if winnings > 0:
                st.success(f"🎉 YOU WON ${winnings}! (Net: ${net_result:+d})")
                st.balloons()
                if winning_lines:
                    st.write(f"✨ Winning lines: {', '.join(map(str, winning_lines))}")
            else:
                st.error(f"😞 No win this time. (Net: ${net_result:+d})")
            
            st.info(f"New Balance: **${st.session_state.balance}**")
            
            if st.session_state.balance == 0:
                st.warning("💸 You're out of money! Deposit more to continue playing.")

st.markdown("---")
st.caption("Good luck! 🍀 | Featuring animated spinning effects!")
