import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name, edges):
        self.vertices[name] = edges

    def dijkstra(self, start):
        # Ініціалізація відстаней. Для початкової вершини відстань 0, для інших - нескінченність.
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start] = 0

        # Ініціалізуємо пріорітетну чергу для визначення наступної вершини, яку потрібно обробити.
        priority_queue = [(0, start)]

        while priority_queue:
            # Вибираємо вершину з найменшою відстанню з пріорітетної черги.
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # Якщо поточна відстань більша за зареєстровану, пропускаємо вершину.
            if current_distance > distances[current_vertex]:
                continue

            # Обходимо сусідні вершини поточної вершини.
            for neighbor, weight in self.vertices[current_vertex].items():
                distance = current_distance + weight

                # Якщо знайдено коротший шлях до сусідньої вершини, оновлюємо відстань.
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances


# Приклад використання:
graph = Graph()
graph.add_vertex('A', {'B': 1, 'C': 4})
graph.add_vertex('B', {'A': 1, 'C': 2, 'D': 5})
graph.add_vertex('C', {'A': 4, 'B': 2, 'D': 1})
graph.add_vertex('D', {'B': 5, 'C': 1})

start_vertex = 'A'
distances = graph.dijkstra(start_vertex)
print(f"Шляхи від вершини {start_vertex}: {distances}")
