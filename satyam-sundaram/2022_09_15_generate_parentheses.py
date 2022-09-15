class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        candidates = ["()"]
        for i in range(n-1):
            result = []
            for ps in candidates:
                ans = [
                    ps[:i] + "()" + ps[i:]
                    for i in range(len(ps))
                ]
                ans.append(ps + "()")
                result.extend(ans)
                candidates = set(result)

        return list(candidates)
