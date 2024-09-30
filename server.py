from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Initialize a pre-trained model (use a mock model here for simplicity)
vulnerability_models = {'py': pipeline('text-classification', model='python_balanced_model_model_9')}

@app.route('/ping', methods=['GET'])
def ping():
    return "Hello world"

@app.route('/predict', methods=['POST'])
def predict_vulnerability():
    data = request.get_json(force=True)

    app.logger.debug(f"Received data: {data}")

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    # Get the function code from the request
    functions = data.get('functions', '')
    app.logger.debug(functions)

    if not functions:
        return jsonify({'error': 'No function code provided'}), 400

    func_predictions = {}
    for entry in functions:
        for func_name, code in entry.items():
            app.logger.debug(code)
            func_predictions[func_name] = vulnerability_models['py'](code)[0]

    return jsonify(func_predictions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
