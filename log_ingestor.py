from elasticsearch import Elasticsearch
import log_ingestor

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

def index_log(log):
    es.index(index='airline_logs', doc_type='_doc', body=log)

# Example usage
sample_log = log_ingestor.generate_airline_log()
index_log(sample_log)
