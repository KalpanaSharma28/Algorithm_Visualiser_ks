import sys
import time
import random
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from ui_window import Ui_MainWindow


class SortingVisualizer(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.array_size = 15
        self.array = [random.randint(1, 100) for _ in range(self.array_size)]
        self.sorted_array = sorted(self.array.copy())

        self.chart_widget = ChartWidget(self)
        self.verticalLayout.addWidget(self.chart_widget)

        self.populate_chart()

        self.sort_button.clicked.connect(self.start_sorting)
        self.reset_button.clicked.connect(self.reset)
        self.textEdit.setReadOnly(True)
        self.textEdit.setText(
            """
            <ul>
                <li>Technique: Repeatedly compares adjacent elements and swaps them if they're in the wrong order. Like bubbles rising to the top, larger elements gradually 'float' to the end.</li>
                <li>Complexity: O(n^2) - Slow for large datasets.</li>
                <li>Stability: Stable - preserves the relative order of equal elements.</li>
                <li>Good for: Simple to understand and implement, good for small datasets.</li>
            </ul>
            """
        )

    def populate_chart(self):
        self.chart_widget.update_chart(self.array)

    def start_sorting(self):
        algorithm = self.algorithm_combo.currentText()

        if algorithm == "Bubble Sort":
            para = ( """
            <ul>
                <li>Technique: Repeatedly compares adjacent elements and swaps them if they're in the wrong order. Like bubbles rising to the top, larger elements gradually 'float' to the end.</li>
                <li>Complexity: O(n^2) - Slow for large datasets.</li>
                <li>Stability: Stable - preserves the relative order of equal elements.</li>
                <li>Good for: Simple to understand and implement, good for small datasets.</li>
            </ul>
            """)
            self.textEdit.setText(para)
            self.bubble_sort()

        elif algorithm == "Insertion Sort":
            para = ("""
            <ul>
                <li>Technique: Builds a sorted sub-array on the left, repeatedly inserting the next element from the unsorted part at its correct position in the sorted sub-array.</li>
                <li>Complexity:  O(n^2) - Slow for large datasets, but best-case O(n) for already sorted or nearly sorted data.</li>
                <li>Stability: Stable - preserves the relative order of equal elements.</li>
                <li>Good for: Efficient for small or partly sorted datasets, simple to understand.</li>
            </ul>
            """)
            self.textEdit.setText(para)
            self.insertion_sort()

        elif algorithm == "Selection Sort":
            para = ("""
            <ul>
                <li>Technique: Finds the minimum element in the unsorted sub-array and swaps it with the first element. Repeat for the remaining sub-array.</li>
                <li>Complexity: O(n^2) - Slow for large datasets.</li>
                <li>Stability: Unstable - may change the relative order of equal elements.</li>
                <li>Good for: Simple to understand, good for small datasets.</li>
            </ul>
            """)
            self.textEdit.setText(para)
            self.selection_sort()

        elif algorithm == "Merge Sort":
            para = ("""
            <ul>
                <li>Technique: Divide and conquer approach. Splits the array into halves, recursively sorts each half, then merges the sorted halves back together in order.</li>
                <li>Complexity: O(n log n) - Efficient for large datasets.</li>
                <li>Stability: Stable - preserves the relative order of equal elements.</li>
                <li>Good for: Fast for large datasets, works well with linked lists.</li>  
            </ul>
            """)
            self.textEdit.setText(para)
            self.merge_sort()

        elif algorithm == "Quick Sort":
            para = ("""
            <ul>
                <li>Technique: Divide and conquer approach. Picks a pivot element and partitions the array based on it (elements less than pivot on one side, greater on the other). Recursively sorts each partition.</li>
                <li>Complexity: O(n log n) on average, but O(n^2) worst-case.</li>
                <li>Stability: Unstable - may change the relative order of equal elements.</li>
                <li>Good for: Generally fast for large datasets, efficient in-place sorting.</li>
            </ul>
            """)
            self.textEdit.setText(para)
            self.quick_sort()

        elif algorithm == "Counting Sort":
            para = """
            <ul>
                <li>Technique: Counts the occurrences of each element in the array, then places them back in their sorted order based on their counts.</li>
                <li>Complexity: O(n + k), where n is the array size and k is the range of values (assuming a limited range).</li>
                <li>Stability: Can be stable or unstable depending on implementation.</li>
                <li>Good for: Efficient for arrays with a limited range of integer values.</li>
            </ul>
            """
            self.textEdit.setText(para)
            self.counting_sort()

    def bubble_sort(self):
        for i in range(self.array_size):
            for j in range(0, self.array_size - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    self.update_chart()
                    QApplication.processEvents()
                    time.sleep(1)

    def insertion_sort(self):
        for i in range(1, self.array_size):
            key = self.array[i]
            j = i - 1
            while j >= 0 and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                j -= 1
                self.update_chart()
                QApplication.processEvents()
                time.sleep(1)
            self.array[j + 1] = key

    def selection_sort(self):
        for i in range(self.array_size):
            min_index = i
            for j in range(i + 1, self.array_size):
                if self.array[j] < self.array[min_index]:
                    min_index = j
            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
            self.update_chart()
            QApplication.processEvents()
            time.sleep(1)

    def merge_sort(self):
        for step in self._merge_sort(self.array):
            self.array = step
            self.update_chart()
            QApplication.processEvents()
            time.sleep(0.3)

    def _merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        yield from self._merge_sort(left_half)
        yield from self._merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        yield arr

    def quick_sort(self):
        self._quick_sort(self.array, 0, len(self.array) - 1)

    def _quick_sort(self, arr, low, high):
        if low < high:
            pivot_index = self._partition(arr, low, high)
            self._quick_sort(arr, low, pivot_index - 1)
            self._quick_sort(arr, pivot_index + 1, high)
            self.update_chart()
            QApplication.processEvents()
            time.sleep(0.3)

    def _partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def counting_sort(self):
        max_value = max(self.array)
        count = [0]*(max_value + 1)

        for value in self.array:
            count[value] += 1

        i = 0
        for value in range(max_value + 1):
            for _ in range(count[value]):
                self.array[i] = value
                i += 1
                self.update_chart()
                QApplication.processEvents()
                time.sleep(0.3)

    def reset(self):
        self.array = [random.randint(1, 100) for _ in range(self.array_size)]
        self.populate_chart()

    def update_chart(self):
        self.chart_widget.update_chart(self.array)


class ChartWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        layout = QVBoxLayout(self)
        layout.addWidget(self.canvas)

    def update_chart(self, data):
        self.ax.clear()
        bars = self.ax.bar(range(len(data)), data, color=self.get_bar_colors(data))
        self.add_labels(bars)
        self.canvas.draw()

    def get_bar_colors(self, data):
        norm_data = [(value - min(data)) / (max(data) - min(data)) for value in data]
        return plt.cm.get_cmap('viridis')(norm_data)

    def add_labels(self, bars):
        for bar, value in zip(bars, self.ax.patches):
            height = bar.get_height()
            self.ax.text(bar.get_x() + bar.get_width() / 2, height,
                         f'{int(height)}', ha='center', va='bottom', color='black')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SortingVisualizer()
    window.resize(700, 600)
    window.show()
    sys.exit(app.exec())
