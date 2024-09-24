class Solution:
    def compress(self, chars: List[str]) -> int:
        #initialize two pointer write and i
        write = 0 #write for writing
        i = 0 #i for iterating

        while i < len(chars):
            char = chars[i] #
            count = 0

            while i < len(chars) and chars[i] == char:
                count += 1 # if the count is found increase the counter
                i += 1 # increase the iterator 

            chars[write] = char #write the character in the list
            write += 1 #increase the write counter

            if  count >1: #only greater than one needs to be written to chars
                for c in str(count): #taking count as a str to write it into chars
                    chars[write] = c
                    write += 1

        return write
