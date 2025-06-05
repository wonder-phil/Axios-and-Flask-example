def home():
  return "Hello from Flask!"

@app.route('/submit', methods=['POST'])
def submit():
  data = request.json
  name = data.get('name')
  address = data.get('address')
  print(f"You entered: Name={name}, Address={address}")
  return jsonify({'message': f'You sent name: {name} and address: {address}'})

if name == 'main':
  app.run(host='0.0.0.0', port=5000, debug=True)
