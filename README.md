# FindMyFamily

FindMyFamily is a web application that helps you track the location of your family members using GPS coordinates. It allows Android mobile clients to send GPS coordinates every 15 minutes, which are then stored in a database. The application provides functionality to process the data and generate a response showing where the mobile has been in a given date range.

## Features

- Receive GPS coordinates from Android mobile clients every 15 minutes.
- Store GPS coordinates in a database.
- Process GPS data to generate a response showing the location history.
- User-friendly UI for viewing and analyzing location data.

## Installation

1. Clone the repository: git clone https://github.com/your-username/findmyfamily.git
2. Install the dependencies: pip install -r requirements.txt
3. Set up the database:
- Create a new database named `family`.
- Update the database configuration in `app/db/database.py` with the appropriate connection details.

4. Run the application: uvicorn main:app --reload


## Usage

1. Start the application by running `uvicorn main:app --reload` in the terminal.

2. Open the application in your web browser at `http://localhost:8000`.

3. Use the application to track the location of your family members by sending GPS coordinates from your Android mobile clients.

4. Process the GPS data to generate a response showing the location history.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- FastAPI - The web framework used for building the API.
- React - The frontend framework used for building the UI.
- Axios - The library used for making HTTP requests from the frontend.
- [Your other dependencies] - The libraries used for other functionalities.
