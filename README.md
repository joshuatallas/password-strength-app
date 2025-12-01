# Password Strength Visualizer

An interactive web application that analyzes password strength by calculating entropy, estimating crack time, and detecting common weak patterns. Perfect for cybersecurity education and awareness.

## Features

- **Entropy Calculation**: Measures password randomness in bits
- **Crack Time Estimation**: Estimates how long it would take to crack your password
- **Pattern Detection**: Identifies common weak patterns (repeated chars, sequences, dictionary words)
- **Visual Feedback**: Color-coded strength indicators and progress bars
- **Privacy-First**: Passwords are never stored or transmitted

## Quick Start

### Local Installation

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**
   ```bash
   streamlit run password_strength_app.py
   ```

3. **Open your browser** at `http://localhost:8501`

## How It Works

### Entropy Calculation
```
entropy = password_length × log₂(character_set_size)
```

### Strength Levels
- 🔴 **Very Weak**: < 28 bits
- 🟠 **Weak**: 28-35 bits
- 🟡 **Moderate**: 36-59 bits
- 🟢 **Strong**: 60-79 bits
- 🔵 **Excellent**: 80+ bits

## Technologies

- **Streamlit**: Web application framework
- **Python**: Core programming language

## 📝 License

MIT License - Feel free to use and modify!

## Acknowledgments

Built for **TACC Education & Outreach** • Interactive Cybersecurity Lesson


