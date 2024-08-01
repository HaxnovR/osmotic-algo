# Osmotic Computing Framework

This repository implements a framework for simulating task scheduling in an osmotic computing or fog cluster computing environment. It leverages a hybrid scheduling approach that combines Round Robin (RR) and Shortest Job Next (SJN) algorithms to optimize task allocation and execution across a network of fog servers.

### Key Features:

- **Task Generation:** Randomly generates tasks with varying execution times and server affinities (representing preference for specific fog servers).
- **Worker Simulation:** Creates a pool of fog servers with on/off states.
- **Hybrid RR-SJN Scheduling:** Implements a two-phase scheduling strategy:
    - **Phase 1: Round Robin (RR):** Initially distributes tasks equally among available servers using RR.
    - **Phase 2: Shortest Job Next (SJN):** Applies SJN scheduling to remaining tasks on each server, prioritizing those with the shortest execution times.
- **Osmotic Layer:** Provides a mechanism for task assignment based on server affinities (not implemented in the current version).

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/osmotic-computing-framework.git
   ```
2. **Install Dependencies:**
   Ensure you have Python 3.x and any additional libraries required (check requirements.txt if present).
3. **Run the Script:**
   ```bash
   python main.py
   ```

**User Input:**

The script prompts for the following user inputs:

- **Time Quantum:** Define the time slice for each task in RR scheduling.
- **Total Servers:** Specify the number of fog servers in the network.
- **Total Tasks:** Indicate the number of tasks to be generated.

**Output:**

The script displays the following information:

- Worker (server) details: server number and status (active/inactive).
- Task details: task ID, execution time, and server affinity (if implemented).
- Task execution order: Lists the order of task execution on each server, including task ID, execution time, and server number.

**Implementation Details:**

- **`Task` Class:** Represents a task with an ID, execution time, and (optional) server affinity.
- **`Worker` Class:** Represents a fog server with an application number and status.
- **`osmoticLayer` Class:** Currently serves as a placeholder for future osmotic layer functionality.
- **`round_robin` Function:** Implements the Round Robin scheduling algorithm.
- **`shortest_job_next` Function:** Implements the Shortest Job Next scheduling algorithm.
- **`hybrid_rr_sjn` Function:** Combines RR and SJN scheduling for task allocation.
- **`randomProcessGenerator` Function:** Generates random tasks with varying execution times and server affinities.
- **`randomWorkerGenerator` Function:** Creates a pool of fog servers with random initial states.
- **`printWorkerInfo` Function:** Displays information about individual fog servers.
- **`printTask` Function:** Prints details of all generated tasks.

**Future Enhancements:**

- Implement the osmotic layer to consider server affinities during task assignment.
- Incorporate support for different task types and priorities.
- Explore other scheduling algorithms or develop a hybrid approach that adapts dynamically.
- Add visualization tools to depict task execution and resource utilization.
