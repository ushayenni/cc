from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route(&#39;/greet&#39;, methods=[&#39;GET&#39;])
def greet():
name = request.args.get(&#39;name&#39;, &#39;Student&#39;)
return jsonify({&quot;message&quot;: f&quot;Hello {name}, welcome to REST API!&quot;})
if __name__ == &#39;__main__&#39;:
app.run(debug=True)
