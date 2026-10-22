
import heapq
from collections import deque, Counter
import gzip
import os


# ==========================================
# PART 1: GPS / NAVIGATION SYSTEM
# ==========================================

class CityMap:
    def __init__(self):
        self.graph = {}

    def add_road(self, city1, city2, distance):
        self.graph.setdefault(city1, [])
        self.graph.setdefault(city2, [])

        self.graph[city1].append((city2, distance))
        self.graph[city2].append((city1, distance))

    def display_map(self):
        print("\n--- City Map ---")
        for city, roads in self.graph.items():
            connections = ", ".join(
                f"{neighbor} ({distance} km)"
                for neighbor, distance in roads
            )
            print(f"{city}: {connections}")

    def shortest_path(self, start, destination):
        if start not in self.graph or destination not in self.graph:
            print("City not found in the map.")
            return

        distances = {city: float("inf") for city in self.graph}
        previous = {city: None for city in self.graph}
        distances[start] = 0

        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_city = heapq.heappop(
                priority_queue
            )

            if current_distance > distances[current_city]:
                continue

            if current_city == destination:
                break

            for neighbor, weight in self.graph[current_city]:
                new_distance = current_distance + weight

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current_city
                    heapq.heappush(
                        priority_queue, (new_distance, neighbor)
                    )

        if distances[destination] == float("inf"):
            print("No route available between these cities.")
            return

        path = []
        city = destination

        while city is not None:
            path.append(city)
            city = previous[city]

        path.reverse()

        print("\n--- Shortest Route ---")
        print("Route:", " -> ".join(path))
        print("Total Distance:", distances[destination], "km")

    def bfs(self, start):
        if start not in self.graph:
            print("City not found.")
            return

        visited = set()
        queue = deque([start])
        visited.add(start)

        print("\nBFS Traversal:")

        while queue:
            city = queue.popleft()
            print(city, end=" ")

            for neighbor, _ in self.graph[city]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        print()


# ==========================================
# PART 2: HUFFMAN CODING
# ==========================================

class HuffmanNode:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency


def build_huffman_tree(text):
    if not text:
        return None

    frequency = Counter(text)
    heap = []

    for char, count in frequency.items():
        heapq.heappush(heap, HuffmanNode(char, count))

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        parent = HuffmanNode(
            None, left.frequency + right.frequency
        )
        parent.left = left
        parent.right = right

        heapq.heappush(heap, parent)

    return heap[0]


def generate_codes(root, prefix="", codes=None):
    if codes is None:
        codes = {}

    if root is None:
        return codes

    if root.char is not None:
        codes[root.char] = prefix or "0"
        return codes

    generate_codes(root.left, prefix + "0", codes)
    generate_codes(root.right, prefix + "1", codes)

    return codes


def huffman_encode(text, codes):
    return "".join(codes[char] for char in text)


def huffman_decode(encoded_text, root):
    if root is None:
        return ""

    # Special case: text contains only one unique character.
    if root.char is not None:
        return root.char * len(encoded_text)

    decoded = []
    current = root

    for bit in encoded_text:
        current = current.left if bit == "0" else current.right

        if current.char is not None:
            decoded.append(current.char)
            current = root

    return "".join(decoded)


def compress_file():
    filename = input("Enter text file name to compress: ").strip()

    if not os.path.isfile(filename):
        print("File not found.")
        return

    output_file = filename + ".gz"

    try:
        with open(filename, "rb") as source:
            data = source.read()

        with gzip.open(output_file, "wb") as compressed:
            compressed.write(data)

        print("File compressed successfully!")
        print("Compressed file:", output_file)
        print("Original size:", len(data), "bytes")
        print(
            "Compressed size:",
            os.path.getsize(output_file),
            "bytes"
        )

    except OSError as error:
        print("Compression error:", error)


def decompress_file():
    filename = input("Enter .gz file name to decompress: ").strip()

    if not os.path.isfile(filename):
        print("File not found.")
        return

    if not filename.endswith(".gz"):
        print("Please enter a .gz file.")
        return

    output_file = filename[:-3] + "_decompressed"

    try:
        with gzip.open(filename, "rb") as source:
            data = source.read()

        with open(output_file, "wb") as destination:
            destination.write(data)

        print("File decompressed successfully!")
        print("Output file:", output_file)

    except (OSError, EOFError) as error:
        print("Decompression error:", error)


def demonstrate_huffman():
    text = input("Enter text for Huffman encoding: ")

    if not text:
        print("Please enter some text.")
        return

    root = build_huffman_tree(text)
    codes = generate_codes(root)
    encoded = huffman_encode(text, codes)
    decoded = huffman_decode(encoded, root)

    print("\nCharacter Frequencies:")
    for char, count in sorted(Counter(text).items()):
        print(repr(char), ":", count)

    print("\nHuffman Codes:")
    for char, code in sorted(codes.items()):
        print(repr(char), ":", code)

    print("\nEncoded Binary String:", encoded)
    print("Decoded Text:", decoded)


# ==========================================
# MAIN MENU
# ==========================================

def main():
    city_map = CityMap()

    # Sample city map: road distances in kilometres
    city_map.add_road("A", "B", 4)
    city_map.add_road("A", "C", 2)
    city_map.add_road("B", "C", 1)
    city_map.add_road("B", "D", 5)
    city_map.add_road("C", "D", 8)
    city_map.add_road("C", "E", 10)
    city_map.add_road("D", "E", 2)
    city_map.add_road("D", "F", 6)
    city_map.add_road("E", "F", 3)

    while True:
        print("\n========== CASE STUDY ==========")
        print("1. Display City Map")
        print("2. Find Shortest Route")
        print("3. BFS City Traversal")
        print("4. Huffman Encoding and Decoding")
        print("5. Compress File using GZIP")
        print("6. Decompress GZIP File")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            city_map.display_map()

        elif choice == "2":
            start = input("Enter starting city (A-F): ").strip().upper()
            destination = input(
                "Enter destination city (A-F): "
            ).strip().upper()

            city_map.shortest_path(start, destination)

        elif choice == "3":
            start = input("Enter starting city (A-F): ").strip().upper()
            city_map.bfs(start)

        elif choice == "4":
            demonstrate_huffman()

        elif choice == "5":
            compress_file()

        elif choice == "6":
            decompress_file()

        elif choice == "7":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
