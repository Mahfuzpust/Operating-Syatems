class Process:
    def __init__(self, pid, burst):
        self.pid = pid
        self.burst = burst
        self.waiting = 0
        self.turnaround = 0
        self.service = 0


class SJFT:
    def __init__(self, processes, quantum):
        self.processes = processes
        self.avg_waiting = 0
        self.avg_turnaround = 0
        self.quantum = quantum
        self.time = 0
    
    
    def sjft(self):
        self.processes.sort(key=lambda x: x.burst)
        for x in range(0, len(self.processes)):
            self.processes[x].service = self.time + self.processes[x].burst
            self.processes[x].turnaround = self.processes[x].service
            self.processes[x].waiting = self.processes[x].turnaround - self.processes[x].burst
            self.time = self.processes[x].service
            self.avg_waiting += self.processes[x].waiting
            self.avg_turnaround += self.processes[x].turnaround

        self.avg_waiting /= len(self.processes)
        self.avg_turnaround /= len(self.processes)
        







if __name__ == '__main__':
    # processes id
    pids = [1, 2, 3]
    bursts = [10, 5, 8]
    quantum = 1

    processes = []
    for i in range(len(pids)):
        processes.append(Process(pids[i], bursts[i]))

    sjft = SJFT(processes, quantum)
    sjft.sjft()

    print(f"""
    {'Process':<10}{'Burst':<10}{'Waiting':<10}{'Turnaround':<10}""")
    for x in range(0, len(processes)):
        print(f"{sjft.processes[x].pid:<10}{sjft.processes[x].burst:<10}{sjft.processes[x].waiting:<10}{sjft.processes[x].turnaround:<10}")
    print(f"""
    Average Waiting Time: {sjft.avg_waiting}
    Average Turnaround Time: {sjft.avg_turnaround}""")