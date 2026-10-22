
# GPS Navigation and Huffman File Compression

## 1. Introduction

This case study demonstrates two important applications of data structures and algorithms using Python.

The first application models a city map as a weighted graph and finds the shortest route between cities.

The second application demonstrates Huffman coding, a frequency-based data compression technique, and uses Python's built-in GZIP module to compress and decompress files.

## 2. Objectives

- Understand weighted graphs and graph representation.
- Implement Dijkstra's shortest-path algorithm.
- Perform Breadth-First Search (BFS).
- Understand Huffman trees and frequency-based encoding.
- Encode and decode text using Huffman codes.
- Compress and decompress files using GZIP.

## 3. Technologies Used

- Programming Language: Python
- Data Structures: Graph, Priority Queue, Queue, Binary Tree
- Algorithms: Dijkstra's Algorithm, BFS, Huffman Coding
- File Compression: Python gzip module
- IDE: Visual Studio Code

## 4. Part A: GPS / Navigation System

### Description

The city map is represented as a weighted graph.

- Vertices represent cities.
- Edges represent roads between cities.
- Weights represent road distances in kilometres.

The program uses Dijkstra's algorithm to find the shortest route between two cities.

BFS is used to visit connected cities level by level.

### Sample City Map

The program includes six sample cities: A, B, C, D, E, and F.

Example roads:
- A to B: 4 km
- A to C: 2 km
- B to C: 1 km
- B to D: 5 km
- D to E: 2 km
- E to F: 3 km

### Graph Algorithms

**Dijkstra's Algorithm:** Finds the minimum-distance route between two cities when road weights are non-negative.

**Breadth-First Search (BFS):** Traverses the graph by visiting neighbouring cities level by level.

## 5. Part B: Huffman Coding and File Compression

### Description

Huffman coding is a lossless compression technique that assigns variable-length binary codes to characters based on their frequencies.

- Characters that appear frequently generally receive shorter codes.
- Characters that appear less frequently generally receive longer codes.
- A binary tree is used to generate the codes.
- The encoded text can be decoded using the same Huffman tree.

The program also uses Python's built-in `gzip` module to compress files into `.gz` format and decompress them.

**Note:** The Huffman demonstration and GZIP file compression are separate operations. The `.gz` file is compressed by GZIP, not by the custom Huffman encoder.

## 6. Features

- Display the city map and road distances.
- Find the shortest route between two cities.
- Traverse cities using BFS.
- Display character frequencies.
- Generate Huffman codes.
- Encode and decode text.
- Compress files using GZIP.
- Decompress GZIP files.

## 7. How to Run

1. Install Python 3 on your computer.
2. Open the project folder in Visual Studio Code.
3. Save the Python code as `gps_huffman.py`.
4. Open the VS Code terminal.
5. Run the following command:

```bash
python gps_huffman.py
```

No additional Python packages are required.

## 8. Sample Output

### Shortest Route

Enter your choice: 2

Enter starting city (A-F): A

Enter destination city (A-F): F

Route: A -> C -> B -> D -> E -> F

Total Distance: 13 km

### Huffman Coding

Enter your choice: 4

Enter text for Huffman encoding: hello

The program displays:
- Character frequencies
- Huffman codes
- Encoded binary string
- Decoded text

The decoded text matches the original input.

## 9. Time Complexity

Let V represent the number of vertices, E the number of edges, and n the number of characters in the input text.

| Algorithm | Time Complexity |
|---|---|
| BFS | O(V + E) |
| Dijkstra using a heap | O((V + E) log V) |
| Huffman tree construction | O(n + k log k) |
| Huffman encoding | O(n) |

Here, k is the number of distinct characters. Huffman tree construction assumes the frequency table is built in O(n) time.

## 10. Applications

- GPS and route navigation systems
- Road network analysis
- Network routing
- Text compression
- File compression and storage
- Efficient data transmission

## 11. Conclusion

This case study demonstrates how graph algorithms can solve shortest-route problems and how Huffman coding can encode text based on character frequencies.

The project also demonstrates practical file compression and decompression using Python's GZIP module. It provides a basic understanding of graph traversal, shortest-path algorithms, binary trees, and lossless compression.
