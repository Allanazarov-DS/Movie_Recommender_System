# Movie Recommender System

Welcome to the Movie Recommender System! This application provides movie recommendations based on your selection. It uses a machine learning model to suggest similar movies and displays movie posters to make the recommendations more visually appealing.

## Features

- **Movie Recommendation**: Select a movie, and the system will recommend five similar movies.
- **Poster Display**: The app fetches and displays movie posters alongside the recommended titles.
- **Interactive Carousel**: An image carousel at the top displays popular movie posters.
- **Responsive Layout**: The app is designed with a wide layout for a comfortable browsing experience.

## Technologies Used

- **Python**: The core language used for building the recommender system.
- **Streamlit**: For creating the web-based interface.
- **Altair**: For data visualization (theme management in this project).
- **Requests**: For fetching movie posters from the TMDB API.
- **Pickle**: For loading the pre-trained recommendation model.
- **Pandas**: For handling data structures.

## Setup Instructions

To run the Movie Recommender System locally, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd movie-recommender-system
   ```

2. **Install Dependencies**

   Ensure you have Python 3.7 or later installed. Install the required Python packages using the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**

   Start the Streamlit application by running the following command:

   ```bash
   streamlit run app.py
   ```

4. **Access the Application**

   Once the server is running, open your web browser and navigate to `http://localhost:8501` to access the application.

## API Key

The application fetches movie posters from the TMDB API. Make sure you have a valid API key from TMDB. Replace the placeholder API key in the `fetch_poster` function in `app.py` with your actual API key:

```python
url = "https://api.themoviedb.org/3/movie/{}?api_key=YOUR_API_KEY&language=en-US".format(movie_id)
```

## File Structure

```
├── app.py                  # Main application script
├── requirements.txt        # Python package dependencies
├── movies_list.pkl         # Pickle file containing movie data
├── similarity.pkl          # Pickle file containing similarity matrix
├── frontend                # Directory containing frontend components
│   └── public              # Directory for public assets (e.g., image carousel)
└── README.md               # This README file
```

## Usage

- **Select a Movie**: Use the dropdown menu to select a movie you like.
- **View Recommendations**: Click the "Show recommend" button to see five recommended movies along with their posters.
- **Hover for Full Title**: Hover over truncated movie titles to see the full title as a tooltip.

## Future Enhancements

- **Improved Recommendation Model**: Enhance the recommendation algorithm with more advanced machine learning techniques.
- **User Ratings**: Allow users to rate movies and improve recommendations based on personal preferences.
- **Customizable Themes**: Add options for users to customize the application's look and feel.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

