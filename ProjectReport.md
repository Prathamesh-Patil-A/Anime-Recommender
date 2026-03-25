# 📄 Project Report: Data-Driven Anime Recommendation Engine

**Student Name:** Prathamesh Sanjay Patil (Void Haiku)  
**Registration Number:** 25BME10014  
**Program:** B.Tech (Mechanical Engineering)  
**University:** VIT Bhopal University  

---

## 1. Abstract
The modern streaming landscape suffers from "decision fatigue," where users spend excessive time browsing catalogs rather than consuming content. This project solves this issue by deploying a custom, data-driven Anime Recommendation Engine. Built using Python and the Streamlit framework, the web application processes user preferences against a structured database using a Boolean-flag filtering algorithm to provide a single, highly accurate recommendation.

## 2. Introduction & Problem Statement
With the exponential growth of digital entertainment, users are overwhelmed by choices. The objective of this Bring Your Own Project (BYOP) was to build a localized search engine that filters out noise. By taking multiple user parameters—such as preferred genres, animation studios, minimum IMDb ratings, and specific creators—the program narrows down a comprehensive database to deliver a targeted, randomized result complete with a spoiler-free synopsis.

## 3. Technologies Used
* **Programming Language:** Python 3
* **Frontend/Web Framework:** Streamlit (`st` module)
* **Version Control:** Git & GitHub
* **Deployment:** Streamlit Community Cloud

## 4. System Architecture & Methodology
The application is divided into three core architectural components:

### 4.1 Data Structure & Storage
The foundational database is constructed as a Python `list` containing over 60 `dictionaries`. Each dictionary represents a single anime and holds key-value pairs for attributes like `title`, `genre` (stored as a nested list), `studio`, `creator`, and `imdb_rating`. 

### 4.2 Dynamic Data Extraction
Instead of hardcoding the user interface options, the program utilizes Python `Sets` to dynamically read the database. 
* A nested `for` loop iterates through the database to extract all genres. 
* By converting this data into a mathematical `Set`, duplicate entries are automatically rejected.
* The Set is then converted back into an alphabetized list, ensuring the frontend dropdown menus are always perfectly synced with the backend data.

### 4.3 The Master Filtering Algorithm
The core logic relies on a Boolean flag system. When a user submits their parameters, the algorithm assumes every anime in the database is a match (`is_match = True`). It then runs each anime through four sequential `if` statement checks (Genre, Rating, Studio, Creator). If an anime fails any check, the flag is flipped to `False`. Only anime that survive the entire gauntlet are appended to the final results list, from which a single winner is randomly selected.

## 5. Challenges & Technical Learnings
During development and deployment, several technical hurdles were overcome:
* **Terminal Path Execution:** Discovered how the command-line interface interprets spaces in folder directories, requiring path encapsulation in quotation marks to execute the local Streamlit server.
* **Cloud Deployment Dependencies:** Learned the necessity of the `requirements.txt` file for cloud environments. An initial deployment failure demonstrated how cloud servers require exact library names to build the environment before executing the main Python script.
* **UI State Management:** Understood the difference between standard Python execution and Streamlit's reactive UI, specifically how `st.button()` acts as a necessary bridge between the frontend inputs and the backend algorithm.

## 6. Conclusion
This project successfully bridged the gap between raw backend logic and a functional, user-facing web application. It reinforced fundamental programming concepts such as data iteration, type conversion, conditional logic, and cloud deployment. As a Mechanical Engineering student, developing these computational problem-solving and data structuring skills provides a strong foundation for future applications in engineering automation, robotics, and complex data analysis.
