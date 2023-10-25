import requests,threading,argparse

url = None
payload = None
thread = 1
request_cout = 0

def handle_status_codes(status_code):
    global request_cout
    request_cout += 1
    print(f"\r{request_cout} requests have been sent", end='')

    if status_code == 429:
        print("You have been throttled")
    if status_code == 500:
        print("Status code 500 received")



def send_get():
    try:
        response = requests.get(url)
        handle_status_codes(response.status_code)
    except requests.exceptions.RequestException:
        pass

def send_post():
    try:
        response = requests.post(url, data=payload)
        handle_status_codes(response.status_code)
    except requests.exceptions.RequestException:
        pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send concurrent HTTP GET or POST requests")
    parser.add_argument("-c", "--count", type=int, help="Specify count for POST or GET request")
    parser.add_argument("-g", "--get", help="Specify GET request")
    parser.add_argument("-p", "--post", help="Specify POST request")
    parser.add_argument("-d", "--data", help="Specify data payload for POST request")
    parser.add_argument("-t", "--threads", type=int, default=1, help="Specify the number of threads to be used")
    args = parser.parse_args()

    url = args.get or args.post
    payload = args.data
    threads = args.threads
    counts = args.count
    thread_list = []

    if not url:
        parser.print_usage()
        exit(1)

    if not args.get and not args.post:
        parser.print_usage()
        exit(1)

    for _ in range(counts):
        if url:
            if payload:
                thread_list = [threading.Thread(target=send_post) for _ in range(threads)]
            else :
                thread_list = [threading.Thread(target=send_get) for _ in range(threads)]
            for t in thread_list:
                    t.start()
    print("\nFinished")




