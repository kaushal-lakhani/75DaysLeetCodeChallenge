class Solution:
    def trap(self, arr: List[int]) -> int:
        st = []
        n = len(arr)
        water = 0
        lfr = []
        rtl = []

        for i in range(n-1,-1,-1):
            canBeFilled = 0
            while st and st[-1][0] < arr[i]:
                st.pop()
            
            if st:
                info = st[-1]
                canBeFilled = max(canBeFilled, info[1]+info[0]-arr[i])

            lfr.insert(0,canBeFilled)
            st.append((arr[i],canBeFilled))
        
        st = []
        for i in range(n):
            canBeFilled = 0
            while st and st[-1][0] < arr[i]:
                st.pop()
            
            if st:
                info = st[-1]
                canBeFilled = max(canBeFilled, info[1]+info[0]-arr[i])

            rtl.append(canBeFilled)
            st.append((arr[i],canBeFilled))

        water = 0
        for i in range(n):
            water += min(rtl[i],lfr[i])
        
        return water