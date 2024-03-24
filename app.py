from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/square', methods=['POST'])
def square():
    if request.method == 'POST':
        data = request.json
        number = data['number']
        result = number ** 2
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Method Not Allowed'}), 405

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True, use_reloader=False)
