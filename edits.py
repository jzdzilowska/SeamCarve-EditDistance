# Comments found in ChatGPT code: takes capitalization into account (fixed with lower() method), 
# bugs regarding incorrent looping through indexes: out of bounds errors when trying to access 
# n+1 and m+1 characters, which don't exist, or transforming longer words into shorter ones; in the second
# one, trying to access indices out of the bounds of strings; issues with the deletion aspect of calculating edit distance
# ; wrongly initialized matrix (starts from the beginning of the word and works forward despite the different approach 
# expected from the method) - initializes the top-left corner of the matrix to 0 which isn't always appropriate); 
# incorrect looping 
def edit_distance_fwd(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    m, n = len(word1), len(word2)
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]            
            else:
                dp[i][j] = 1 + min(dp[i-1][j],    
                                   dp[i][j-1],    
                                   dp[i-1][j-1])  

    return dp[m][n]

# ----------------------------------------------------------

def edit_distance_bwd(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower() 
    m, n = len(word1), len(word2)

    # if m == 0:
    #     return n
    # elif n == 0:
    #     return m

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # COMMENT REGARDING THE INITIAL WORKING OF CHATGPT'S CODE:
    # Firstly creates a matrix of size [length(first word) +1] x [length(second word)] with all values 
    # initialized to zero (accounting for one character more (the "null" spot) than the number of each 
    # word's characters); then iterates through the first row and the first column of the matrix, setting 
    # their values to the number of their column or row respectively. 
    
    for i in range(m+1):
        dp[i][n] = m-i
    for j in range(n+1):
        dp[m][j] = n - j

    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
                if word1[i] == word2[j]:             # COMMENTS REGARDING THE INITIAL WORKINGS OF THE CHATGPT'S CODE:
                    dp[i][j] = dp[i+1][j+1]          # if the i-th character of the w1 is the same as the jth character
                                                     # of word 2, copies over the previously calculated edit distance 
                                                     # between the suffixes of these words starting at their next ((i+1)
                                                     # or (j+1)) character from the [i+1][j+1] element of the matrix 
                else:
                    dp[i][j] = 1 + min(dp[i+1][j],   # if the i-th and j-th characters of w1 and w2 are different, 
                                                     # compares results of different types of operations to
                                                     # calculate the lowest possible edit distance by breaking it
                                                     # into subproblems.
                                                     # In this line, checks the edit distance of the first word's 
                                                     # suffix starting at j+1 and the suffix of the second word starting 
                                                     # at i, to account for the potential insertion of a character 
                                                     # on the i-th position of the first word to match a character 
                                                     # on the j-th spot of the second. 
                                       dp[i][j+1],   # Calculates the edit distance between first and second word's 
                                                     # suffixes starting at i+1 and j respectively, representing 
                                                     # the potential deletion of a character on the i-th spot of 
                                                     # the first word
                                       dp[i+1][j+1]) # Calculates the edit distance between suffixes starting at 
                                                     # i+1 (word1) and j+1 (word2) spots, representing the potential 
                                                     # replacement of the i-th character with a j-th one. 
    return dp[0][0]
 
