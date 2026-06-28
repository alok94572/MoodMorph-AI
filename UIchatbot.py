import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# --- PAGE CONFIG ---
st.set_page_config(page_title="Pudding AI", page_icon="🍮", layout="centered")

# --- STATE MANAGEMENT ---
if "messages" not in st.session_state:
    st.session_state.messages = []

def reset_chat():
    st.session_state.messages = []

# --- INITIALIZE MODEL ---
@st.cache_resource
def load_model():
    return ChatOllama(model="llama3")

model = load_model()

# --- SIDEBAR & SETUP ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #333333;'>🎀 Menu 🎀</h1>", unsafe_allow_html=True)
    
    # Bestie Names
    mood_choice = st.radio(
        "Choose a Bestie:",
        options=["Candy Bunny 🐰", "Angry Potato 🥔", "Gloomy Muffin 💧"],
        index=0
    )
    
    # Reverted Name: Drama Level
    drama_level = st.slider("🎭 Drama Level:", 1, 10, 5)
    
    # Updated Neutral/Cool Labels (Not girlish)
    if drama_level <= 3:
        vibe_label = "🟢 Level: Chill"
    elif drama_level <= 7:
        vibe_label = "🟡 Level: Wild"
    else:
        vibe_label = "🔴 Level: Insane"
    
    st.markdown(f"<div style='text-align: center; font-weight: bold; color: #111111;'>{vibe_label}</div>", unsafe_allow_html=True)
    
    st.divider()
    
    # Stickers: The original ones you loved
    stickers = {
        "Candy Bunny 🐰": "https://cdn-icons-png.flaticon.com/512/4359/4359963.png",
        "Angry Potato 🥔": "https://cdn-icons-png.flaticon.com/512/2950/2950580.png", 
        "Gloomy Muffin 💧": "https://cdn-icons-png.flaticon.com/512/6022/6022513.png"
    }
    st.image(stickers[mood_choice], width=150)
    
    st.button("✨ Clear Memory", on_click=reset_chat, use_container_width=True)

# --- DYNAMIC STYLING (Matching background & clear text) ---
def apply_kawaii_styles(mood):
    if mood == "Angry Potato 🥔":
        main_color = "#FFB7B2" 
        bg_color = "#FFDADA"
    elif mood == "Candy Bunny 🐰":
        main_color = "#B2E2F2" 
        bg_color = "#E0F7FF"
    else: # Gloomy Muffin
        main_color = "#B2B2B2" 
        bg_color = "#E6E6FA"

    st.markdown(f"""
        <style>
        .stApp {{
            background-color: {bg_color};
        }}
        
        [data-testid="stSidebar"] {{
            background-color: {main_color} !important;
        }}
        [data-testid="stSidebar"] label, [data-testid="stSidebar"] p {{
            color: #111111 !important;
            font-weight: 800 !important;
        }}

        /* Chat Bubbles */
        [data-testid="stChatMessage"] {{
            background-color: white !important;
            border: 3px solid {main_color} !important;
            border-radius: 20px !important;
            box-shadow: 4px 4px 0px {main_color}88;
        }}

        /* Text Clarity */
        .stChatMessage p {{
            color: #111111 !important;
            font-weight: 500 !important;
        }}

        h1 {{
            color: #111111 !important;
            text-align: center;
        }}
        </style>
    """, unsafe_allow_html=True)

apply_kawaii_styles(mood_choice)

# --- AVATARS ---
avatars = {
    "Angry Potato 🥔": "https://cdn-icons-png.flaticon.com/512/2950/2950580.png",
    "Candy Bunny 🐰": "https://cdn-icons-png.flaticon.com/512/2663/2663067.png",
    "Gloomy Muffin 💧": "https://cdn-icons-png.flaticon.com/512/6022/6022513.png"
}

# --- HEADER ---
st.markdown(f"<h1>{mood_choice}</h1>", unsafe_allow_html=True)

# --- DISPLAY CHAT ---
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user", avatar="🍭"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant", avatar=avatars[mood_choice]):
            st.markdown(msg.content)

# --- CHAT LOGIC ---
if prompt := st.chat_input("Say something to your bestie..."):
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user", avatar="🍭"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar=avatars[mood_choice]):
        
        # Drama Level System Prompt
        mode_map = {
            "Angry Potato 🥔": f"You are Angry Potato. You are grumpy. Drama level: {drama_level}/10.",
            "Candy Bunny 🐰": f"You are Candy Bunny. You are happy. Drama level: {drama_level}/10.",
            "Gloomy Muffin 💧": f"You are Gloomy Muffin. You are sad. Drama level: {drama_level}/10."
        }
        
        # Reaction based on level
        extra = " Be extremely dramatic and emotional!" if drama_level > 7 else " Be calm and simple."
        
        context = [SystemMessage(content=mode_map[mood_choice] + extra + " Use normal sentence case. Keep it short.")] + st.session_state.messages
        
        with st.spinner("Thinking..."):
            try:
                response = model.invoke(context)
                st.markdown(response.content)
                st.session_state.messages.append(AIMessage(content=response.content))
            except Exception as e:
                st.error("Error connecting to your bestie. 😿")