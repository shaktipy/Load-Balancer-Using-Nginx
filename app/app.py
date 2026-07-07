from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# SERVER_ID environment variable se aata hai jo docker-compose.yml mein define hai.
# Isse hi pata chalta hai ki yeh kaunsa container hai (Server 1, 2, 3, ya 4).
server_id = os.environ.get('SERVER_ID', 'Unknown Server')


@app.route('/')
def index():
    # Jab browser http://localhost kholta hai, Nginx yeh request ek Flask container ko deta hai.
    # Wo container apna server_id template ko pass karta hai taaki UI mein dikh sake.
    return render_template('index.html', server_id=server_id)


@app.route('/api/server')
def api_server():
    # JavaScript frontend is endpoint ko call karta hai to pata kare
    # ki kaunse server ne latest request handle ki.
    # JSON format mein return hota hai: {"server_id": "Server X"}
    return jsonify({"server_id": server_id})


@app.route('/health')
def health():
    # Nginx health check ke liye yeh endpoint use hoti hai.
    # Agar yeh 200 return kare toh Nginx samajhta hai ki yeh server theek hai.
    return "OK", 200


if __name__ == '__main__':
    # 0.0.0.0 ka matlab hai ki container ke bahar se bhi accessible ho.
    # Sirf localhost likhte toh container ke andar tak limited rahta.
    app.run(host='0.0.0.0', port=5000)
