class Solution:
    def sort_by_pos(self, e):
        return e[0]

    def comp_time(self, target_dist, curr_dist, speed):
        return (target_dist-curr_dist)/speed

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = []
        pos_t = [(position[i], speed[i]) for i in range(len(position))]
        sorted_post = sorted(pos_t, key=self.sort_by_pos, reverse=True)

        for pos, speed  in sorted_post:
            st.append((pos, speed))
            if len(st)<2:
                continue
            bench_time = self.comp_time(target, st[-2][0], st[-2][1])
            curr_time = self.comp_time(target, st[-1][0], st[-1][1])
            if curr_time <= bench_time:
                st.pop()
        
        return len(st)

