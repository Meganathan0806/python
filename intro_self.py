from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    intro = {
        "name": "Meganathan",
    
        "skills": ["Python", "JavaScript", "HTML", "CSS "  "Flask" " Git " "Github"],
        "interests": ["Web Development", "Software Engineering", "Tech Support" "Designing"],
        "goal": "To become a successful Web  Developer."
    }

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Self Introduction</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                padding: 20px;
                background-color: #f0f0f0;
            }
            .card {
                background-color: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                max-width: 600px;
                margin: auto;
            }
            h1 {
                color: #333;
            }
            ul {
                list-style-type: square;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Hello, I'm {{ intro.name }}</h1>
            <p><strong>Education:</strong> {{ intro.education }}</p>
            <p><strong>Skills:</strong></p>
            <ul>
                {% for skill in intro.skills %}
                    <li>{{ skill }}</li>
                {% endfor %}
            </ul>
            <p><strong>Interests:</strong> {{ ", ".join(intro.interests) }}</p>
            <p><strong>Career Goal:</strong> {{ intro.goal }}</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html, intro=intro)

if __name__ == '__main__':
    app.run(debug=True)
