import heapq
import heapq


def min_heap():
    heap = []
    heapq.heappush(heap, 4) # 삽입
    heapq.heappush(heap, 5) # 삽입
    heapq.heappush(heap, 6) # 삽입

    result = heapq.heappop(heap) # 최솟값 반환

    min = heapq.heappushpop(heap, 1)

    print(heap)
    print(result)
    print(min)
    print(len(heap))

def max_heap():
    heap = []