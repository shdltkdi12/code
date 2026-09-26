class SnapshotArray:

    def __init__(self, length: int):
        self.dic = defaultdict(list)
        self.snap_id = 0
        for i in range(length):
            self.dic[i].append([0,0])
        

    def set(self, index: int, val: int) -> None:
        snapshot_list = self.dic[index][-1]
        if snapshot_list[0] == self.snap_id:
            # in place edit
            self.dic[index][-1][1] = val
        else:
            # append
            self.dic[index].append([self.snap_id, val])
        print(self.dic)
    def snap(self) -> int:
        self.snap_id +=1
        return self.snap_id -1

    def get(self, index: int, snap_id: int) -> int:
        snapshot_list = self.dic[index]
        idx = bisect.bisect_left(snapshot_list, snap_id, key=lambda x: x[0])
        ans = 0 if idx == len(snapshot_list) else self.dic[index][idx][1]
        return ans


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
