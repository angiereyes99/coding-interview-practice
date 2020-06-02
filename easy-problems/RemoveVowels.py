class Solution:

    def approach1(self, s: str) -> str:
        
        newWrd = ""

        for ch in s:
            if (ch == 'A' or ch == 'a' or ch == 'E' or ch == 'e' 
                or ch == 'I' or ch == "i" or ch == "O" or ch == "o" 
                or ch == 'U' or ch == "u"):
                pass
            else:
                newWrd = newWrd + ch
        return newWrd

    
    def approach2(self, s: str) -> str:

        vowels = ('A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u')
        
        for i in s:
            for i in vowels:
                s = s.replace(i, "")
        return s
    



if __name__ == "__main__":
    sol = Solution()
    word = "Apple"
    print(sol.approach1(word))

    word2 = "AngELO REyes I am"
    print(sol.approach2(word2))