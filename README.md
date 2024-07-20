# Carousel
Circular Doubly Linked List Carousel

This project implements a Circular Doubly Linked List (CDLL) in Python, designed to manage a carousel-like data structure. The CDLL allows for efficient navigation through elements in both forward and backward directions, making it ideal for applications like image carousels, playlist management, or any scenario requiring cyclic iteration over elements.

Features
Circular Structure: The list's next pointer of the last node points to the first node, and the previous pointer of the first node points to the last node, forming a continuous loop.
Doubly Linked: Each node maintains a reference to both the next and the previous node, allowing traversal in both directions.
Dynamic Sizing: The list can grow dynamically until a specified maximum size is reached, offering flexibility in handling varying data loads.
Efficient Insertions and Deletions: Nodes can be added or removed at any position in the list with constant time complexity.