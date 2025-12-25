from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Coming Soon</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                color: #333;
                text-align: center;
                padding: 20px;
            }
            
            h1 {
                font-size: 3rem;
                margin-bottom: 1rem;
            }
            
            p {
                font-size: 1.2rem;
                line-height: 1.6;
            }
            
            strong {
                color: #0066cc;
            }
            
            @media (max-width: 600px) {
                h1 {
                    font-size: 2rem;
                }
                p {
                    font-size: 1rem;
                }
            }
        </style>
    </head>
    <body>
        <h1>Coming Soon!</h1>
        <p>The website will be deployed on <strong>26.12.2025 23:59 UTC+5</strong>.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)