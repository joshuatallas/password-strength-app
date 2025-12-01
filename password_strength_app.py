import streamlit as st
import re
import math
import time

# Password Entropy Calculation

def calculate_entropy(password):
    charset = 0

    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"[0-9]", password):
        charset += 10
    if re.search(r"[^a-zA-Z0-9]", password):
        charset += 33  # common special chars

    if charset == 0:
        return 0

    return round(len(password) * math.log2(charset), 2)


# Time to Crack Estimation

def time_to_crack(entropy):
    guesses_per_second = 1e9  # typical GPU rig ~1 billion guesses/s
    seconds = 2 ** entropy / guesses_per_second

    # Convert to readable format
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        return f"{seconds/60:.2f} minutes"
    elif seconds < 86400:
        return f"{seconds/3600:.2f} hours"
    elif seconds < 31536000:
        return f"{seconds/86400:.2f} days"
    else:
        years = seconds / 31536000
        if years > 1e6:
            return f"{years/1e6:.2f} million years"
        return f"{years:.2f} years"



# Pattern Detection

def detect_patterns(password):
    patterns = []

    if password.lower() in ["password", "123456", "qwerty", "password123", "abcdefg", "admin"]:
        patterns.append("Common weak password")

    if re.search(r"(.)\1{2,}", password):
        patterns.append("Repeated characters detected")

    if re.search(r"(123|234|345|456|789)", password):
        patterns.append("Sequential numbers detected")

    if re.search(r"(abc|bcd|cde|def|xyz)", password.lower()):
        patterns.append("Sequential letters detected")

    # dictionary words (simple demo dictionary)
    easy_words = ["dog", "cat", "love", "happy", "summer", "winter", "student", "class"]
    for word in easy_words:
        if word in password.lower():
            patterns.append(f"Contains dictionary word: '{word}'")

    return patterns if patterns else ["No obvious patterns detected"]



# Strength Label

def strength_label(entropy):
    if entropy < 28:
        return "Very Weak", "🔴"
    elif entropy < 36:
        return "Weak", "🟠"
    elif entropy < 60:
        return "Moderate", "🟡"
    elif entropy < 80:
        return "Strong", "🟢"
    else:
        return "Excellent", "🔵"


# Streamlit UI

st.set_page_config(
    page_title="Password Strength Visualizer",
    page_icon="🔐",
    layout="centered"
)

st.title("Password Strength Visualizer")
st.subheader("Learn how secure your password really is.")

st.write("Type a password below (this tool never stores passwords).")

password = st.text_input("Enter a test password:", type="password")

if password:
    st.divider()

    st.subheader("Analysis Results")

    entropy = calculate_entropy(password)
    time_estimate = time_to_crack(entropy)
    patterns = detect_patterns(password)
    label, emoji = strength_label(entropy)

    st.metric(label="Entropy", value=f"{entropy} bits")
    st.metric(label="Estimated Time to Crack", value=time_estimate)

    st.markdown(f"### {emoji} Strength Level: **{label}**")

    # Strength meter bar
    st.progress(min(entropy / 100, 1.0))

    st.write("### Pattern Detection")
    for p in patterns:
        st.write(f"- {p}")

    st.divider()

    st.write("### Tips to Improve")
    st.write("""
    - Use **long passphrases** (16+ characters)  
    - Mix uppercase, lowercase, numbers, and symbols  
    - Avoid dictionary words or personal info  
    - Replace passwords often  
    - Use a password manager  
    """)

else:
    st.info("Enter a password above to test its strength.")


# Footer
st.divider()
st.caption("Built for TACC Education & Outreach • Interactive Cybersecurity Lesson")

