class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

       
        items = []
        for ch in freq:
            items.append((ch, freq[ch]))

      
        items.sort(key=lambda x: x[1], reverse=True)

       
        result = ""
        for ch, count in items:
            result += ch * count

        return result

        