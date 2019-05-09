import os, random

HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']

def load_requests_from_file(fname):
    """Load individual requests from fname, strip them of whitespace and return
    them in an array. Each request must start with keyword from HTTP_METHODS."""
    
    requests = []
    
    with open(fname) as f:
        request = ""
        for line in f:
            if line.split(" ")[0] in HTTP_METHODS and len(request) > 0:
                requests.append(request.strip())
                request = ""
            request = request + line
            
    return requests

def load_supervised_dataset(dataset_dir):
    """Load data from files in dataset_dir, merge them and
    return tuple of requests in array and their corresponding labels."""
    
    train_normal_requests = load_requests_from_file(os.path.join(dataset_dir, 'normalTrafficTraining.txt'))
    test_normal_requests = load_requests_from_file(os.path.join(dataset_dir, 'normalTrafficTest.txt'))
    test_anomalous_requests = load_requests_from_file(os.path.join(dataset_dir, 'anomalousTrafficTest.txt'))

    requests = []
    labels = []
    
    for request in train_normal_requests + test_normal_requests:
        requests.append(request)
        labels.append(0) # 0 for normal
        
    for request in test_anomalous_requests:
        requests.append(request)
        labels.append(1) # 1 for anomalous
    
    requests, labels = shuffle_requests_and_labels(requests, labels)

    return (requests, labels)

def shuffle_requests_and_labels(requests, labels, seed=123):
    """Shuffle requests and their labels with the same seed."""
    random.seed(seed)
    random.shuffle(requests)
    random.seed(seed)
    random.shuffle(labels)
    
    return (requests, labels)