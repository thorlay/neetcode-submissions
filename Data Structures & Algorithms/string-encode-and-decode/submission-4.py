class Solution:

    def encode(self, strs: List[str]) -> str:
        result = "";
        for s in strs:
            l = len(s);
            result += str(l) + "#" + s;
        print(result);
        return result;

    def decode(self, s: str) -> List[str]:
        total = len(s);
        i = 0;
        result = [];
        print(i);
        while i < total:
            j = i;
            while s[j] != "#":
                j=j+1;
            length = int(s[i:j]);
            subs = str(s[j+1:j+1+length]);
            result.append(subs);
            i = j+1+length;
        return result;
