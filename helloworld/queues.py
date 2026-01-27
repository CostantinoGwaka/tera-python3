from collections import deque
queue = deque([])
queue.append('first')
queue.append('second')
queue.append('third')
queue.popleft()
queue.popleft()
queue.popleft()
print(queue)  # deque(['second', 'third'])

if not queue:
    print("Queue is empty")
