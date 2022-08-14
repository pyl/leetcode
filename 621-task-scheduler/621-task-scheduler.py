class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # heaps are good at getting the largest element
        # queue's are good at getting the element that was put in first
        # why use a queue instead of any other data structure?
        # try to use a list.
        
        c = Counter(tasks)
        mx = [-item for item in c.values()]
        heapify(mx)
        q = deque()
        time = 0
        while mx or q:
            time += 1
            if mx:
                current = -heappop(mx)
                current -= 1
                if current != 0:
                    q.append((time + n, current))
            if q and q[0][0] == time:
                val = q.popleft()
                heappush(mx, -val[1])
                
        return time
                
        
        

