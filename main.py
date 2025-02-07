import streamlit as st
import base64
import random

def add_bg_and_music():
    bg_image_path = "Valentines-Day.jpg"  # Change this to your local image file
    music_file = "Janam-Janam-Slowed-Reverb.mp3"  # Change this to your local music file
    
    with open(bg_image_path, "rb") as img_file:
        bg_image_base64 = base64.b64encode(img_file.read()).decode()
    
    page_bg = f"""
    <style>
    .stApp {{
        background: url("data:image/jpeg;base64,{bg_image_base64}") no-repeat center center fixed;
        background-size: cover;
        background-blend-mode: overlay;
        background-color: rgba(255, 255, 255, 0.5);
    }}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)
    
    with open(music_file, "rb") as audio_file:
        audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3", autoplay=True, loop=True)

def main():
    st.set_page_config(page_title="Valentine Proposal", page_icon="💖")
    add_bg_and_music()
    
    st.subheader("Hey! I've been wanting to ask you something special...")
    st.title("💘 Will You Be My Valentine? 💘")
    
    
    col1, col2 = st.columns(2)
    
    
    with col1:
        if st.button("Yes 💖"):
            st.success("I KNEW IT! ❤️ You are the best BubuJaan!")
            
            st.write("### Here’s what’s coming up:")
            st.write("- 🥰 **2 Dates**")
            st.write("- 🍽️ **2 Dinners**")
            st.write("- 🥗 **2 Lunches**")
            st.write("- ☕ **10 Teas**")
            st.write("- 🍵 **5 Coffees**")
            st.write("\n **Waiting for these days! 💕**")
    
    with col2:
        if st.button("No 🙁"):
            st.warning("Oh no! Let Me Convince You 😍...")
            convince_page()

def convince_page():    
    reasons = [
        "I'm fun to be around! 😁",
        "We have the best conversations! 🗣️",
        "I promise to make you smile every day! 😊",
        "You and I would be the perfect team! 🤝",
        "Think about all the fun things we can do together! 🎉",
        "I will always be there for you! 💖",
        "You light up my world like nobody else! ✨",
        "I'm your biggest fan and best friend! 🎶",
        "I will make your name special every day! 💖",
        "I will cook for you! 🍽️",
        "We will be the best together! 🌟",
        "I’ll support your dreams and help you achieve them! 🌈",
        "Every day with you will be an adventure! 🌍",
        "We’ll create beautiful memories that last forever! 📸",
        "You make my heart skip a beat! 💓",
        "I’ll always put a smile on your face! 😊",
        "Together, we can conquer the world! 🌏",
        "You’re my favorite person to be around! 💕",
        "I’ll love you like no one else ever will! 💘",
        "We’ll share countless moments of happiness! 🎊",
        "With you, life will always be brighter! 🌞",
        "I’ll always appreciate and respect you! 🙏",
        "I’ll make sure you feel loved every day! 💑",
        "We’ll be a great team, in every aspect of life! 💪",
        "I’ll support you through every challenge you face! 💪",
        "I’ll make your dreams come true, one step at a time! 🌠",
        "You’re my source of happiness! 😍",
        "I’ll always cherish the little moments with you! 💖",
        "Our love will be the best adventure! 🌍",
        "You deserve all the love and happiness in the world! 🌎",
        "With you by my side, everything feels perfect! 🌟",
        "I’ll stand by you through thick and thin! ❤️",
        "I promise to always be your biggest cheerleader! 🎉",
        "You make my world a better place! 🌈",
        "I’ll always listen to you and value your thoughts! 🧠",
        "Together, we’ll create a love story for the ages! 📖",
        "Our love will be the most beautiful chapter of our lives! 💌",
        "Every moment with you is a moment I’ll never forget! 💭",
    ]

    
    random_reason = random.choice(reasons)
    st.write(f"- {random_reason}")
    
    if st.button("Okay, I say YES now! 💘"):
        st.success("Yay! I knew you couldn't resist! ❤️")

if __name__ == "__main__":
    main()
