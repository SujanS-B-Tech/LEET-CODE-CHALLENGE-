class Solution:

    def letterCombinations(self, digits: str) -> list[str]:
     
        mapping = [["a", "b", "c"],
        ["d", "e", "f"],
        ["g", "h", "i"],
        ["j", "k", "l"],
        ["m", "n", "o"],
        ["p", "q", "r", "s"],
        ["t", "u", "v"],
        ["w", "x", "y", "z"]]
       

        output = []
        for digit in digits:
            digit = int(digit)
            if not output:
             
                output += mapping[digit-2]
            else:
               
                output = [f"{a}{b}" for a in output for b in mapping[digit-2]]
        return output