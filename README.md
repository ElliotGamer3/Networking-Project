# Info

# Running information
To run, use the command `python main.py`

# File Structure

Code is hosted in the src folder. the tests folder contains a copy of the src file structure and a folder for each corresponding file in the src folder that contains tests for the file. For example, a file in the src directory with the path of `/src/foo/bar.py` would have tests 1 and 2 located at `/tests/foo/bar/bar_1_test.py` and `/tests/foo/bar/bar_2_test.py`.


# Simulation Information

## Costs

The manner in which costs of actions are determined in the simulation is by assuming a constant cost for actions that occur with in the simulation and tracking the cost against the system as a whole. This method is not a perfect method but allows for a easy way to calculate the cost to the system based on different scenarios and methods. Below is an example.

### Example

Cost Assumtions
- Sending data costs 1 unit
- Collecting/Reading data costs 1 unit (we will assume listening is free)
- interpreting data costs 5 units
- creating data costs 3 units per second

Method 1)
For a 3 node system a method that sends to all nodes results in the following costs for the nodes (a,b,c)
A: 1 Sending cost
B: 1 Reading cost, 5 Interpreting Cost, 6 Total Cost
C: 1 Reading Cost, 5 Interpreting Cost, 6 Total Cost
Resulting in a System cost of 13 units and a average node cost of 4.333 units

Method 2)
Compared to the same system but a method that only sends data to the node it needs:
A: 1 Sending Cost
B: 0 Cost
C: 1 Reading Cost, 5 Interpreting Cost, 6 Total Cost
Resulting in a System cost of 7 units and an average node cost of 2.333 units

In this example, method 2 would be a better method due to the lower average node cost.

Therefore, the method used to determine costs in the simulation favors a system that is more effecint based on the amount of work that must be done by each node.

## Cost Shortcomings

There are a few shortcomings in calculating costs in the manner. The main one being that if there is a scenario in which a small number of nodes are being heavly used while a large number of nodes can never be used thus lowering the average. To minimize this, there will be an assumption that all nodes must have the potential to be used. In other words, every node can be reached in the system. Additonally, the costs can also consider the system to be the current node and all direct connections to the node.

For example in the following complete system:

A <-> B <-> C <-> D

The node A has a system of: A <-> B
The node B has a system of: A <-> B <-> C
The node C has a system of: B <-> C <-> D
The node D has a system of: C <-> D

- The costs of each of these systems will be refered to as a each node's System Cost. It is the average of all the node's cost in a node's system. (incluse of the cost of the node the system is for.) For example, The system cost of node B is the average cost of node A, B, and C.
- The cost of all the nodes, A <-> B <-> C <-> D, is called the Complete System Cost. It is the average of all the node's costs.
- The System Cost is the average of each node's System Cost. It is different from the Complete system cost. For example, in the system above the system cost is (A's system cost + B's system cost + C's system cost + D's system cost) / 4. Where the complete system cost is (A's cost + B's cost + C's cost + D's cost) / 4. 
