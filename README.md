# Algorithm Visualiser

#### Python program that visualizes various sorting algorithms using a graphical user interface (GUI) built with PySide6 (a Python binding for Qt) and Matplotlib. 

It utilizes PySide6 for the GUI components and Matplotlib for creating bar chart visualizations of sorting algorithms. The main class, SortingVisualizer, includes implementations of Bubble Sort, Insertion Sort, Selection Sort, Merge Sort, Quick Sort, and Counting Sort. The GUI allows users to choose an algorithm from a combo box, displays information about the selected algorithm, and visualizes the sorting process on a dynamically updating bar chart. Each sorting algorithm is accompanied by a brief description of its technique, complexity, stability, and suitability for specific scenarios. 

![image](https://github.com/KalpanaSharma28/Algorithm_Visualiser_ks/assets/103998795/0eb3f14c-c628-4d15-8dd5-2c15e816f453)


#### GUI Setup:
The main window is created using PySide6's QMainWindow.
The GUI layout is designed using Qt Designer, and the design is loaded into the main window.
The main window contains widgets such as buttons, a combo box for selecting sorting algorithms, a text edit widget for displaying algorithm information, and a custom ChartWidget for displaying the bar chart.

![image](https://github.com/KalpanaSharma28/Algorithm_Visualiser_ks/assets/103998795/5f35091c-e37a-4620-ae8c-d337dc431260)

#### Array and Sorting:
Ui_MainWindow integrate the GUI.
Initializes with default settings, including an array of random integers to be sorted.
The populate_chart method updates the bar chart in the GUI based on the current state of the array.
Sorting algorithms are implemented, each with a method that updates the array state and calls update_chart to visualize the changes in the GUI.


#### Chart and Visuals:
Inherits from QWidget and includes a Matplotlib figure embedded in a Qt layout.
The update_chart method clears the existing chart, updates it with the new data, and redraws the canvas.
get_bar_colors is used to color the bars in the chart based on the normalized values of the array elements.
add_labels adds text labels on top of each bar in the chart, displaying the corresponding integer values.
When a sorting algorithm is selected from the combo box, relevant information about the algorithm is displayed in the text edit widget.

QApplication.processEvents() is used to ensure that the GUI remains responsive during the sorting process.
A short delay (time.sleep()) is added after each step to visualize the sorting process more clearly.

##### The code provides an interactive and educational tool for visualizing the behavior of different sorting algorithms. Users can observe how each algorithm performs on a randomly generated array and understand their characteristics, complexities, and suitability for different scenarios.

