# 🎬 Anime Recommender
**A Data-Driven Solution to Streaming Decision Fatigue**

🔴 **Live Demo:** [Click here to try the Web App!](https://anime-recommender-xsounabutjxysatwfbdh4f.streamlit.app/)

## 📌 Project Overview
This project was developed as a "Bring Your Own Project" (BYOP) capstone. The core problem it solves is **decision fatigue** the phenomenon where users spend more time scrolling through massive streaming catalogs than actually watching content. 

This application allows users to input their specific tastes (genres, preferred studios, minimum IMDb ratings, and creators) and utilizes a custom filtering algorithm to present a single, high-quality, randomized recommendation complete with a spoiler-free synopsis.

## ⚙️ Key Features
* **Dynamic Data Extraction:** The app automatically parses the dataset to generate unique, alphabetized lists of genres, studios, and creators for the UI, eliminating the need for hardcoded dropdowns.
* **Master Filter Algorithm:** A highly scalable Boolean-flag filtering system that instantly cross-references multiple user inputs against a database of 60 titles.
* **Edge-Case Handling:** Built-in error states and UI alerts if a user's highly specific query yields zero results.
* **Interactive UI:** Built using the Streamlit framework for a clean, responsive, and intuitive frontend web interface.

## 🚀 How to Run Locally (For Developers)
If you want to run this code on your own machine instead of using the Live Demo:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Prathamesh-Patil-A/Anime-Recommender.git](https://github.com/Prathamesh-Patil-A/Anime-Recommender.git)
