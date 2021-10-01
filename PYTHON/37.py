
class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c): 
        
 
       # code here 
       top=left=0
       bottom=r-1
       right=c-1
       mat=[]
       if(r==1 and c==1):
           return(matrix[0])
       if(r==1 and c>1):
           return(matrix[0])
       if(c==1 and r>1):
           for i in range(r):
               mat.append(matrix[i][0])
           return(mat)
       while(top<=bottom and left<=right):
           for i in range(left,right+1):
               mat.append(matrix[top][i])
           top+=1
           for i in range(top,bottom+1):
               mat.append(matrix[i][right])
           right-=1
           if(top<=bottom):
               for i in range(right,left-1,-1):
                   mat.append(matrix[bottom][i])
               bottom-=1
           if(left<=right):
               for i in range(bottom,top-1,-1):
                   mat.append(matrix[i][left])
               left+=1
       return(mat)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends