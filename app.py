from flask import Flask, render_template

app = Flask(__name__)

# Serve the main portfolio page
@app.route('/')
def home():
    return render_template('index.html')

# Example API endpoint
@app.route('/api/data')
def get_data():
    return {"message": "Hello from Flask API!"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
