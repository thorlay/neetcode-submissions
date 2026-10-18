class Solution:

    def encode(self, strs: List[str]) -> str:
        l = len(strs);
        strs.append(str(l));
        result = "「".join(strs)
        return result;

    def decode(self, s: str) -> List[str]:
        result = s.split("「");
        if result[-1] == 0:
            return [];
        return result[:-1];
