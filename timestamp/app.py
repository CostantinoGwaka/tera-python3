import time


# print(time.time())

def send_email():
    for email in range(1000):
        pass


start = time.time()
send_email()
end = time.time()
duration = end - start
print(f"Time taken to send emails: {duration} seconds")
print(f"Time taken to send emails: {duration:.4f} seconds")
