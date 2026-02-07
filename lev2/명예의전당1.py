

def solution1(k, score):
    import heapq
    heap = []
    answer = []
    
    for x in score:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)  
        answer.append(heap[0])
    return answer

print(solution1(3, [10, 100, 20, 150, 1, 100, 200]))