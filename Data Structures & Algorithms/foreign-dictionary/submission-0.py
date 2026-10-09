from typing import List
from collections import defaultdict, deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # 1. 初始化所有字符
        graph = {c: set() for word in words for c in word}
        indegree = {c: 0 for c in graph}

        # 2. 从相邻单词中找约束
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            # prefix invalid: ["abc", "ab"]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for j in range(min(len(w1), len(w2))):
                c1, c2 = w1[j], w2[j]

                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[c2] += 1
                    break

        # 3. Kahn 拓扑排序
        q = deque([c for c in indegree if indegree[c] == 0])
        res = []

        while q:
            c = q.popleft()
            res.append(c)

            for nei in graph[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        # 4. 如果没包含所有字符，说明有环
        if len(res) != len(indegree):
            return ""

        return "".join(res)