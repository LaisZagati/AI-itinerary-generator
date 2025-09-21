# 🧳 AI Travel Itinerary Planner ✈️

An interactive Python program that helps you **plan a road trip** with the power of AI.  
It generates a **personalized travel itinerary** and shows you the **current weather** for your origin and destination cities.

---

## 🌟 Features

- 🔮 **AI-Powered Itinerary**  
  Generates a short and fun road trip plan (max 15 lines) with emojis.  

- 🌦️ **Live Weather Info**  
  Fetches the current temperature and conditions for both your origin and destination cities.  

- 🎨 **Beautiful Output**  
  Uses [Rich](https://github.com/Textualize/rich) for colorful, Markdown-style terminal output.  

---

## 🚀 How It Works

1. Enter your **origin city**  
2. Enter your **destination city**  
3. Enter your **trip duration (in days)**  
4. The program will:
   - Display current weather in both cities 🌡️  
   - Generate an itinerary using the SheCodes AI API 🤖  

---

## 🛠️ Requirements

- Python 3.8+  
- Libraries:
  - `requests`
  - `rich`

Install dependencies:

```bash
pip install requests rich
