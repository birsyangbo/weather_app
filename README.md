# Django Weather & City Explorer

A dynamic web application built with Django that provides real-time weather data and beautiful city imagery by integrating multiple third-party APIs.

---

##  Features
* **Live Weather Updates:** Fetches temperature, wind speed, and humidity using the **OpenWeatherMap API**.
* **Dynamic Visuals:** Automatically pulls high-quality city background images using an **Image API** (Unsplash/Pixabay).
* **Search History:** Keeps track of recently searched cities for quick access.
* **Responsive UI:** Clean, mobile-friendly design built with Django Templates and CSS.
* **Language Agnostic:** Search for cities globally, from Kathmandu to New York.

---

##  Tech Stack
* **Backend:** Python 3.12, Django 5.x
* **APIs:** * OpenWeatherMap (Meteorological Data)
    * Unsplash/Pixabay API (City Images)
* **Frontend:** HTML5, CSS3 (Flexbox/Grid), JavaScript
* **Database:** SQLite3 (Local development)

---

##  How It Works
The application follows the Model-View-Template (MVT) architecture:
1. **Request:** The user enters a city name in the search bar.
2. **Fetch:** The Django view sends simultaneous requests to the Weather and Image APIs.
3. **Render:** The results are parsed and injected into the template, displaying a custom-themed weather card with a matching city background.



---

##  Installation & Setup

1. **Clone the Project:**
   ```bash
   git clone [https://github.com/birsyangbo/WeatherProject.git](https://github.com/birsyangbo/WeatherProject.git)
   cd WeatherProject
