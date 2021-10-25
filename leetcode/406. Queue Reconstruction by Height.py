'''
You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order).
Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people
in front who have a height greater than or equal to hi.

Reconstruct and return the queue that is represented by the input array people.
The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] is the attributes of the jth person
in the queue (queue[0] is the person at the front of the queue).

Example 1:

Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
Explanation:
Person 0 has height 5 with no other people taller or the same height in front.
Person 1 has height 7 with no other people taller or the same height in front.
Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
Person 3 has height 6 with one person taller or the same height in front, which is person 1.
Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
Person 5 has height 7 with one person taller or the same height in front, which is person 1.
Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.
Example 2:

Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]

# 키에 다른 대기열 재구성
# 여러 명의 사람들이 줄을 서 있다. 각각 사람은 (h, k)의 두 정수 쌍을 갖는데. h는 그 사람의키 k는 앞에 줄 서있는 사름들 중 자신의 키 이상인
키 이상인 사람들의 수를 뜻한다. 이 값이 올바르도록 줄을 재 정렬하는 알고리즘을 작성하라
# 키가 5인 사람이 가장 먼저 섰고, 앞에는 아무도 없다. 7인 사람이 뒤따르고, 그보다 키가 더 큰사람은 아무도 없다.
5인 사람의 앞에는 자신보다 큰 키 7인 사람 한 명이 있다. 4인 사람 앞에는 5,7, 5, 6 네 명이 있다. 마지막으로 7인 사람 앞에 자신보다 크거나
같은 이는 키가 7인 사람 한명이다.

'''
# 우선순위 큐를 이용해 순서대로 입력값을 추출
def reconstructQueue(self, people):
    heap = []
    # 키 역순, 인덱스 삽입
    for person in people:
        heapq.heappush(heap, (-person[0], person[1]))

    result = []
    # 키 역순, 인덱스 추출
    while heap:
        person = heapq.heappop(heap)
        result.insert(person[1], [-person[0], person[1]])
    return result
# 첫 번째 값이 큰순서대로 추출되는 최대 힙 Max Heap 형태로 풀이할 수 있고, 부전 째 값은 삽입되는 인덱스로 활용할 수 있다
# 파이썬의 최소 힙 Min Heap 맘 지원하기 때문에, 첫번째 값을 음수로 변경해 최소 힙에서도 최대 힙처럼 구현
# 두 번째 값은 인덱스로 해 삽입되는 위치로 구현 

# Runtime: 144 ms, faster than 37.11% of Python online submissions for Queue Reconstruction by Height.
# Memory Usage: 14.4 MB, less than 6.92% of Python online submissions for Queue Reconstruction by Height.