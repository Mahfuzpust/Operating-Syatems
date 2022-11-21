
"""
1. Sort the processes by burst time
2. Sort the processes by arrival time
3. Calculate everything for first process
4. Where we got a time range
5. Find the last index which belongs to the time range
6. Sort the processes by burst time (current index to last finding index)
7. Calculate everything for the next process
8. Repeat until all processes are done(4-7)
"""


class Process:
    def __init__(self, pid, arrival, burst, priority):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.waiting = 0
        self.turnaround = 0
        self.service = 0
        self.priority = priority


class LJF:
    def __init__(self, processes):
        self.processes = processes
        self.n = len(processes)
        self.avg_waiting = 0
        self.avg_turnaround = 0

    def get_sort_end_index(self, start_index, arrival_time_rane):
        # 5. Find the last index which belongs to the time range
        """
        if process arrival time is greater than the arrival time range
        then we can stop the loop
        """

        for x in range(start_index, self.n):
            if self.processes[x].arrival > arrival_time_rane:
                return x
        return self.n
        

    def ljf(self):
        # 1. Sort the processes by burst time
        self.processes.sort(key=lambda x: x.priority, reverse=True)
        # 2. Sort the processes by arrival time
        self.processes.sort(key=lambda x: x.arrival)

        # 3. Calculate everything for first process
        self.processes[0].service = self.processes[0].arrival + self.processes[0].burst
        self.processes[0].turnaround = self.processes[0].service - self.processes[0].arrival
        self.processes[0].waiting = self.processes[0].turnaround - self.processes[0].burst

        for x in range(1, self.n):
            # 4. Where we got a time range (time range is first process completion time)
            # 5. Find the last index which belongs to the time range
            sort_end_index = self.get_sort_end_index(x, self.processes[x-1].service)

            # 6. Sort the processes by burst time (current index to last finding index)
            self.processes[x:sort_end_index] = sorted(self.processes[x:sort_end_index], key=lambda x: x.priority, reverse=True)
            
            # 7. Calculate everything for the next process
            if self.processes[x-1].service > self.processes[x].arrival:
                self.processes[x].service = self.processes[x-1].service + self.processes[x].burst
            else:
                self.processes[x].service = self.processes[x].arrival + self.processes[x].burst
            self.processes[x].turnaround = self.processes[x].service - self.processes[x].arrival
            self.processes[x].waiting = self.processes[x].turnaround - self.processes[x].burst

        self.avg_waiting = sum([x.waiting for x in self.processes])/self.n
        self.avg_turnaround = sum([x.turnaround for x in self.processes])/self.n





if __name__ == '__main__':
    # processes id
    pids = [1, 2, 3, 4]
    # processes arrival time
    arrivals = [0, 5, 3, 9]
    # processes burst time
    bursts = [1, 9, 3, 6]
    priority = [1, 2, 3, 4]

    processes = []
    for i in range(len(pids)):
        processes.append(Process(pids[i], arrivals[i], bursts[i], priority[i]))

    ljf = LJF(processes)
    ljf.ljf()

    print(f"""
    {'Process':<10}{'Arrival':<10}{'Burst':<10}{'Priority':<10}{'Waiting':<10}{'Turnaround':<10}{'Service':<10}""")
    for x in range(0, ljf.n):
        print(f"{ljf.processes[x].pid:<10}{ljf.processes[x].arrival:<10}{ljf.processes[x].burst:<10}{ljf.processes[x].priority:<10}{ljf.processes[x].waiting:<10}{ljf.processes[x].turnaround:<10}{ljf.processes[x].service:<10}")
    print(f"""
    Average Waiting Time: {ljf.avg_waiting}
    Average Turnaround Time: {ljf.avg_turnaround}""")