from flask import Flask, render_template_string, jsonify
import random

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to MSOE</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;600&display=swap');

        body {
            background: linear-gradient(135deg, #ff416c, #ff4b2b);
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Poppins', sans-serif;
            margin: 0;
            text-align: center;
            transition: background 1s ease-in-out;
        }

        .container {
            color: white;
            padding: 20px;
            max-width: 500px;
            animation: fadeIn 2s ease-in-out;
        }

        h1 {
            font-size: 3rem;
            margin: 0;
        }

        .highlight {
            color: #ffeb3b;
        }

        .subtitle {
            font-size: 1.2rem;
            margin-top: 10px;
            opacity: 0.8;
        }

        .btn {
            display: inline-block;
            background: white;
            color: #ff416c;
            padding: 10px 20px;
            margin-top: 20px;
            text-decoration: none;
            border-radius: 25px;
            font-weight: bold;
            transition: 0.3s;
            cursor: pointer;
            border: none;
            font-size: 1rem;
        }

        .btn:hover {
            background: #ffeb3b;
            color: black;
        }

        /* Animation */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="title">Hello, <span class="highlight">MSOE!</span></h1>
        <p class="subtitle">Welcome to the coolest Flask app.</p>
        <button class="btn" onclick="changeBackground()">Explore</button>
    </div>

    <script>
        function changeBackground() {
            alert("Get ready for something cool! 🎨");
            const colors = ['#ff416c', '#ff4b2b', '#1e90ff', '#32cd32', '#ff1493', '#ffa500'];
            document.body.style.background = "linear-gradient(135deg, " + 
                colors[Math.floor(Math.random() * colors.length)] + ", " + 
                colors[Math.floor(Math.random() * colors.length)] + ")";
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    """Render the stylish UI"""
    return render_template_string(HTML_TEMPLATE)

@app.route("/health")
def health_check():
    """Health check endpoint"""
    return jsonify(status="healthy", message="App is running smoothly")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

