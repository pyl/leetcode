class Solution:
    def trap(self, height: List[int]) -> int:
        mx = 0
        mxl = []
        mxr = []
        for x in height:
            if x > mx:
                mx = x
            mxl.append(mx)
        mx = 0
        for x in height[::-1]:
            if x > mx:
                mx = x
            mxr.append(mx)
        res = 0
        for i,x in enumerate(height):
            res += min(mxl[i], mxr[len(mxr)-1-i]) - x
        return res