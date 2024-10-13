# Unsplash Image Search Application📸
# Introduction
The Unsplash Image Search Application is a web-based tool built with Streamlit that allows users to search and view images from Unsplash by simply entering a text prompt. The app leverages the Unsplash API to deliver high-quality, responsive images based on the user's input.

![images](https://github.com/user-attachments/assets/b833f23f-3447-421c-9045-e3f7ebeeadfa)


# Features
● Search Images: Users can input any text prompt to search for related images.

● Display Results: Up to 20 images are displayed in a 5-column grid layout for easy viewing.

● Responsive UI: The application is clean, simple, and responsive, built with Streamlit’s easy-to-use interface.

● API Integration: The app connects to the Unsplash API to retrieve real-time image data.

# Prerequisites
Ensure you have the following before starting:

● Python 3.x installed.

● An API key from Unsplash to access their services.

● Basic Python libraries including streamlit, requests, and python-dotenv.

# Installation
1. Clone the repository:

   ● Clone the GitHub repository to your local machine.

2. Install dependencies:

   ● Install the required Python packages using pip.

3. Unsplash API Setup:

   ● Create a .env file in the root directory and add your Unsplash API key for authentication.

4. Run the application:

   ● Launch the app locally by running the Streamlit script.
# How It Works
# API Key Management
The application securely loads the Unsplash API key from a .env file using python-dotenv to protect sensitive information. This key is required to interact with the Unsplash API.

# Image Search Functionality
The application takes a user-provided prompt and sends it as a query to the Unsplash API. In return, the API responds with a set of image URLs matching the prompt. The images are then processed and displayed dynamically.

# User Interface
Streamlit is used to build a simple and responsive UI. Users can input a search prompt, and the application will display the search results in a grid format, with each image labeled and resized for a clean viewing experience.

# Usage Instructions
1. Run the application.
2. Input a search term: Type a keyword or phrase in the input box (e.g., “mountains” or “cityscape”).
3. View results: The images related to your search will be displayed in a grid format.
4. Explore: Scroll through the images and enjoy!
# Example Use Cases
● Find Inspiration: 
Quickly search for creative or thematic images for your personal projects.

● Content Creation:
Use the search tool to find visually appealing images for blogs, websites, or social media.

● Personal Use:
Browse and explore beautiful imagery based on interests.

# Future Improvements
● Advanced Search Options: Include filters for image orientation, color schemes, and categories.

● Pagination: Enable navigation through more extensive image result sets.

● Photographer Credits: Display the photographer’s name and add direct download links for the images.

● Image Download Feature: Allow users to download their favorite images directly from the app.
