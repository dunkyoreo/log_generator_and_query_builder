from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

@app.route('/search', methods=['POST'])
def search_logs():
    query = request.json['query']
    result = es.search(index='airline_logs', body=query)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
