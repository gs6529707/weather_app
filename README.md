<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather App - Documentation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            padding: 20px;
            background-color: #f4f4f9;
            color: #333;
        }
        h1, h2 {
            color: #4caf50;
        }
        code {
            background: #e4e4e4;
            padding: 2px 4px;
            border-radius: 4px;
        }
        pre {
            background: #f4f4f4;
            padding: 10px;
            border-left: 5px solid #4caf50;
            overflow-x: auto;
        }
        ul {
            margin: 20px 0;
        }
        .project-structure {
            background: #fafafa;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        .screenshot img {
            max-width: 100%;
            height: auto;
            border: 1px solid #ddd;
            border-radius: 5px;
            margin: 20px 0;
        }
        a {
            color: #2196f3;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>Weather App 🌤️</h1>
    <p>A web-based application built with Python Flask that allows users to fetch real-time weather information for any city. The app integrates the OpenWeatherMap API to display weather details such as temperature, wind speed, and a short description.</p>

  <h2>Features</h2>
    <ul>
        <li>🌡️ Fetch real-time weather data for any city.</li>
        <li>📋 Displays:
            <ul>
                <li>Temperature</li>
                <li>Wind Speed</li>
                <li>Weather Description</li>
                <li>Current Date and Time</li>
            </ul>
        </li>
        <li>💻 Responsive UI with smooth animations.</li>
        <li>🌐 Integrated with the OpenWeatherMap API.</li>
    </ul>

  <h2>Project Structure</h2>
    <div class="project-structure">
        <pre>
project/
├── app.py               # Main Flask application
├── static/
│   └── style.css        # CSS for styling the app
├── templates/
│   └── index.html       # HTML for the frontend
└── README.md            # Documentation
        </pre>
    </div>

  <h2>Prerequisites</h2>
    <ul>
        <li>Python 3.7 or higher</li>
        <li>Pip package manager</li>
        <li>OpenWeatherMap API key</li>
    </ul>

  <h2>Installation</h2>
    <ol>
        <li><strong>Clone the Repository:</strong>
            <pre>git clone https://github.com/your-repo/weather-app.git
cd weather-app</pre>
        </li>
        <li><strong>Create a Virtual Environment (Optional):</strong>
            <pre>python -m venv venv
source venv/bin/activate    # For Linux/Mac
venv\Scripts\activate       # For Windows</pre>
        </li>
        <li><strong>Install Dependencies:</strong>
            <pre>pip install flask requests</pre>
        </li>
        <li><strong>Set Up OpenWeatherMap API Key:</strong>
            <ul>
                <li>Obtain your API key from <a href="https://openweathermap.org/" target="_blank">OpenWeatherMap</a>.</li>
                <li>Replace the placeholder <code>f00c38e0279b7bc85480c3fe775d518c</code> in <code>app.py</code> with your API key.</li>
            </ul>
        </li>
    </ol>

  <h2>Usage</h2>
    <ol>
        <li><strong>Run the Flask Application:</strong>
            <pre>python app.py</pre>
        </li>
        <li><strong>Access the App:</strong>
            <p>Open your browser and navigate to <code>http://127.0.0.1:5000</code>.</p>
        </li>
        <li><strong>Use the App:</strong>
            <p>Enter a city name in the input field and click "Get Weather" to fetch and display the weather details.</p>
        </li>
    </ol>

  <h2>Screenshots</h2>
    <div class="screenshot">
        <p><strong>Home Page:</strong></p>
        <img src="screenshot_home.png" alt="Weather App Home Page">
    </div>

  <h2>Technologies Used</h2>
    <ul>
        <li><strong>Backend:</strong> Python Flask</li>
        <li><strong>Frontend:</strong> HTML, CSS</li>
        <li><strong>API:</strong> OpenWeatherMap</li>
        <li><strong>Styling Frameworks:</strong> Google Fonts, Custom CSS</li>
    </ul>

  <h2>Future Enhancements</h2>
    <ul>
        <li>🌦️ Add weather icons based on conditions.</li>
        <li>🗓️ Display a 5-day weather forecast.</li>
        <li>🛠️ Improve error handling for invalid inputs.</li>
    </ul>

  <h2>License</h2>
    <p>This project is licensed under the MIT License. See the <code>LICENSE</code> file for details.</p>

  <h2>Contributing</h2>
    <p>Contributions are welcome! Feel free to open issues or submit pull requests. For major changes, please open an issue first to discuss what you would like to change.</p>

  <h2>Acknowledgments</h2>
    <ul>
        <li>OpenWeatherMap API for providing the weather data.</li>
        <li>Google Fonts for typography.</li>
    </ul>

   <h2>🌟 Star this repository if you found it useful!</h2>
</body>
</html>
