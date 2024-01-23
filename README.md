# Algorithm_Visualiser_ks

#### Python program that visualizes various sorting algorithms using a graphical user interface (GUI) built with PySide6 (a Python binding for Qt) and Matplotlib. 

It utilizes PySide6 for the GUI components and Matplotlib for creating bar chart visualizations of sorting algorithms. The main class, SortingVisualizer, includes implementations of Bubble Sort, Insertion Sort, Selection Sort, Merge Sort, Quick Sort, and Counting Sort. The GUI allows users to choose an algorithm from a combo box, displays information about the selected algorithm, and visualizes the sorting process on a dynamically updating bar chart. Each sorting algorithm is accompanied by a brief description of its technique, complexity, stability, and suitability for specific scenarios. 

![image](https://github.com/KalpanaSharma28/Algorithm_Visualiser_ks/assets/103998795/0eb3f14c-c628-4d15-8dd5-2c15e816f453)


#### GUI Setup:
The main window is created using PySide6's QMainWindow.
The GUI layout is designed using Qt Designer, and the design is loaded into the main window.
The main window contains widgets such as buttons, a combo box for selecting sorting algorithms, a text edit widget for displaying algorithm information, and a custom ChartWidget for displaying the bar chart.
