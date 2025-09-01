from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)
borehole_data = []

template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Borehole Log Entry</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
<div class="container mt-4">
    <h2 class="text-center mb-4">Geotechnical Borehole Log</h2>
    <form method="post" action="{{ url_for('submit') }}">
        <div class="mb-3">
            <label for="depth" class="form-label">Depth (m)</label>
            <input type="number" step="0.01" class="form-control" id="depth" name="depth" required>
        </div>
        <div class="mb-3">
            <label for="soil_type" class="form-label">Soil Type</label>
            <input type="text" class="form-control" id="soil_type" name="soil_type" required>
        </div>
        <div class="mb-3">
            <label for="moisture" class="form-label">Moisture Content (%)</label>
            <input type="number" step="0.01" class="form-control" id="moisture" name="moisture" required>
        </div>
        <button type="submit" class="btn btn-primary w-100">Add Entry</button>
    </form>

    <hr class="my-4">

    <h4 class="text-center">Log Preview</h4>
    <table class="table table-bordered table-striped mt-3">
        <thead class="table-dark">
            <tr>
                <th>Depth (m)</th>
                <th>Soil Type</th>
                <th>Moisture Content (%)</th>
            </tr>
        </thead>
        <tbody>
            {% for entry in data %}
            <tr>
                <td>{{ entry['depth'] }}</td>
                <td>{{ entry['soil_type'] }}</td>
                <td>{{ entry['moisture'] }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</div>
</body>
</html>
"""

@app.route('/', methods=['GET'])
def index():
    return render_template_string(template, data=borehole_data)

@app.route('/submit', methods=['POST'])
def submit():
    entry = {
        'depth': request.form['depth'],
        'soil_type': request.form['soil_type'],
        'moisture': request.form['moisture']
    }
    borehole_data.append(entry)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
