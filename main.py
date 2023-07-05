import sys
from numpy import array , set_printoptions
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QPushButton, QTabWidget, QGroupBox, QComboBox, QStyleFactory, QVBoxLayout
from PyQt6.QtGui import QDoubleValidator
from PyQt6.QtCore import Qt
from ITM_ArrowKey_Movement import ITM_ArrowKey_Movement # import for moving between input boxes with arrow keys


# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& Main Windows &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        
class ITM_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Matrix Calculator") # Window Title
        self.setGeometry(100, 100, 600, 800) # Dimensions of window
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus) # allows keyboard input - used for arrow keys
        self.tab_widget = QTabWidget() # create a tab widget
        
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ LAYOUT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #!##############################################################################
    #!################### Inverse Transformation Matrix ############################
    #!##############################################################################
  
  
        self.ITM_tab = QWidget() # creates a tab for the ITM
        self.tab_widget.addTab(self.ITM_tab, "Inverse Transformation Matrix") # adding it to the window

        # Create the group box for values
        self.ITM_input_group_box = QGroupBox('Enter Values') # A group to keep all the inputs in the same place
        self.ITM_input_layout = QGridLayout() # A grid layout for the inputs - resembles a transformation matrix
        self.ITM_input_group_box.setLayout(self.ITM_input_layout) # Add the grid layout to the group box

        # Create labels and input boxes for the matrix
        self.input_boxes = [] # empty list for the input boxes
        for i in range(4): 
            row = []
            for j in range(4):
                label = QLabel(f'T{i+1}{j+1}:') # Adds a label for each value in Transformation matrix
                line_edit = ITM_ArrowKey_Movement() # Make the input boxes equal to the import
                line_edit.setFixedSize(60, 30)  # Set the size of the input box
                line_edit.setValidator(QDoubleValidator())  # Restrict input to floats
                row.append(line_edit) # add the input box to the row list
                self.ITM_input_layout.addWidget(label, i, 3*j)  # Add the label to the layout
                self.ITM_input_layout.addWidget(line_edit, i, 3*j + 1)  # Add the input box to the layout
            self.input_boxes.append(row)

        # Create the layout for the tab
        self.ITM_layout = QGridLayout() # Create a Grid layout for the tab
        self.ITM_layout.addWidget(self.ITM_input_group_box)  # Add the group box to the layout

        # Button to get values
        self.ITM_results_button = QPushButton("Get Values")
        self.ITM_results_button.clicked.connect(self.ITM_get_values)
        self.ITM_layout.addWidget(self.ITM_results_button)
        
        # Button to get steps to answer
        self.ITM_Steps_to_answer_button = QPushButton("Steps to Answer")
        self.ITM_Steps_to_answer_button.clicked.connect(self.open_steps_to_answer_window)
        self.ITM_layout.addWidget(self.ITM_Steps_to_answer_button)
        self.new_window = None #? assigned the value to None here 
        
        #Button to clear input boxes
        self.ITM_clear_button = QPushButton("Clear")
        self.ITM_clear_button.clicked.connect(self.clear_input_boxes)
        self.ITM_layout.addWidget(self.ITM_clear_button)
        
        # QComboBox for theme selection
        self.theme_combo_box = QComboBox()
        self.theme_combo_box.addItem("Light Theme")
        self.theme_combo_box.addItem("Dark Theme")
        self.theme_combo_box.addItem("Sepia Theme")
        self.theme_combo_box.currentIndexChanged.connect(self.change_theme)
        self.ITM_layout.addWidget(self.theme_combo_box)
        
        # QComboBox for the style selection
        self.style_combo_box = QComboBox()
        self.styles = QStyleFactory.keys()
        self.fusion_index = self.styles.index("Fusion")
        self.style_combo_box.addItems(self.styles)
        self.style_combo_box.setCurrentIndex(self.fusion_index)
        self.style_combo_box.currentIndexChanged.connect(self.change_style)
        self.ITM_layout.addWidget(self.style_combo_box)
        
        # Label to display answer
        self.ITM_display_result_label = QLabel()
        self.ITM_display_result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ITM_display_result_label.setStyleSheet("font-size: 20pt")
        self.ITM_layout.addWidget(self.ITM_display_result_label)

        # Set the layout for the tab
        self.ITM_tab.setLayout(self.ITM_layout)

        #!##############################################################################
        #!########################## Basic Matrix Operations ###########################
        #!##############################################################################
        
        self.tab2 = QWidget()
        self.tab_widget.addTab(self.tab2, "Basic Matrix Operations")

        #!##############################################################################
        #!############################### Tab 3 ########################################
        #!##############################################################################
        
        self.tab3 = QWidget()
        self.tab_widget.addTab(self.tab3, "Tab 3")

        
        self.setCentralWidget(self.tab_widget) # makes the tab_widget the main widget of the application 
        

    #~~~~~~~~~~~~~~~~~~~~~~ LOGIC ~~~~~~~~~~~~~~~~~~~
    def ITM_get_values(self):
        global r11_text, r12_text, r13_text, px_text, r21_text, r22_text, r23_text, py_text, r31_text, r32_text, r33_text, pz_text
        r11_text = self.input_boxes[0][0].text()
        r12_text = self.input_boxes[0][1].text()
        r13_text = self.input_boxes[0][2].text()
        px_text = self.input_boxes[0][3].text()

        r21_text = self.input_boxes[1][0].text()
        r22_text = self.input_boxes[1][1].text()
        r23_text = self.input_boxes[1][2].text()
        py_text = self.input_boxes[1][3].text()

        r31_text = self.input_boxes[2][0].text()
        r32_text = self.input_boxes[2][1].text()
        r33_text = self.input_boxes[2][2].text()
        pz_text = self.input_boxes[2][3].text()

        try:  # Check if the input boxes are not empty
            if r11_text and r12_text and r13_text and px_text and r21_text and r22_text and r23_text and py_text and r31_text and r32_text and r33_text and pz_text:
                
                global r11, r12, r13, px, r21, r22, r23, py, r31, r32, r33, pz, px_new, py_new, pz_new #? needed for steps to answer 
                r11 = float(r11_text)
                r12 = float(r12_text)
                r13 = float(r13_text)
                px =  float(px_text)
                r21 = float(r21_text)
                r22 = float(r22_text)
                r23 = float(r23_text)
                py =  float(py_text)
                r31 = float(r31_text)
                r32 = float(r32_text)
                r33 = float(r33_text)
                pz =  float(pz_text)
                px_new = -((px*r11)+(py*r21)+(pz*r31))
                py_new = -((px*r12)+(py*r22)+(pz*r32))
                pz_new = -((px*r13)+(py*r23)+(pz*r33))
                
                matrix = array([[r11, r21, r31, px_new], 
                                [r12, r22, r32, py_new],
                                [r13, r23, r33, pz_new],
                                [0, 0, 0, 1]])
                
                
                set_printoptions(precision=4, suppress=True, formatter={'float_kind':'{:0.2f}'.format}) # limits to 4 decimal places #! needs work
                matrix_string = str(matrix).lstrip('[').rstrip(']') # removes extra square brackets - it removes more than required
                matrix_string = f"[{matrix_string}]" # adds the missing square brackets 
                self.ITM_display_result_label.setText(matrix_string)
                    
        except ValueError:
            self.ITM_display_result_label.setText("Values not entered")

        except ZeroDivisionError:
            self.ITM_display_result_label.setText("'a' cannot be zero")

        except Exception:
                self.ITM_display_result_label.setText("An error occurred")
                
    
    # opens Steps to answer window
    def open_steps_to_answer_window(self):
        if self.new_window is None: 
            self.new_window = ITM_Steps_to_answer_new_Window()
            self.new_window.ITM_steps_to_answer()
            self.new_window.show()
        else:
            self.new_window.close()
            self.new_window = None
            
    # clear the input boxes as well as the result        
    def clear_input_boxes(self):
        self.ITM_display_result_label.setText('')
        for row in self.input_boxes:
            for line_edit in row:
                line_edit.clear()
    #~~~~~~~~~~~~~~~~~~~~~~~~ THEME ~~~~~~~~~~~~~~~~~~~~~~~~~~
    def change_theme(self, index):
        if index == 0:
            # light theme
            self.setStyleSheet("background-color: #FFFFFF; color: #000000;")

        elif index == 1:
            # dark theme
            self.setStyleSheet("background-color: #121212; color: #FFFFFF;")
            
        elif index == 2:
            # sepia theme
            self.setStyleSheet("background-color: #F5DEB3; color: #704214;")

    #~~~~~~~~~~~~~~~~~~~~~~~~ STYLE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def change_style(self, index):
        # Store the selected style index
        self.selected_style_index = index
        styles = QStyleFactory.keys()
        selected_style = styles[self.selected_style_index]
        QApplication.setStyle(selected_style)
        
                
class ITM_Steps_to_answer_new_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Steps to Answer")
        self.setGeometry(100, 100, 600, 800)
        self.steps_to_answer_window_layout = QGridLayout()

        font_size = 10
        self.transformation_matrix_standard_label = QLabel(self) # General trnasformation matrix
        self.transformation_matrix_standard_label.setStyleSheet(f"font-size: {font_size}pt")
        self.steps_to_answer_window_layout.addWidget(self.transformation_matrix_standard_label, 0, 0)

        self.rotation_matrix_label = QLabel(self) # rotation matrix
        self.rotation_matrix_label.setStyleSheet(f"font-size: {font_size}pt")
        self.steps_to_answer_window_layout.addWidget(self.rotation_matrix_label, 1, 0)
        
        self.position_vector_label = QLabel(self) # position vector
        self.position_vector_label.setStyleSheet(f"font-size: {font_size}pt")
        self.steps_to_answer_window_layout.addWidget(self.position_vector_label, 2, 0)
        
        self.bottom_row_matrix_label = QLabel(self) # Bottom row matrix
        self.bottom_row_matrix_label.setStyleSheet(f"font-size: {font_size}pt")
        self.steps_to_answer_window_layout.addWidget(self.bottom_row_matrix_label, 3, 0)
        
        self.transformation_matrix_standard_with_values_label = QLabel(self) # Transformation matrix with inputted values
        self.transformation_matrix_standard_with_values_label.setStyleSheet(f"font-size: {font_size}pt")
        self.steps_to_answer_window_layout.addWidget(self.transformation_matrix_standard_with_values_label, 4, 0)

        self.inverse_transformation_matrix_formula_label = QLabel(self) # Formula for inverse transformation matrix
        self.inverse_transformation_matrix_formula_label.setStyleSheet(f"font-size: {font_size}pt")
        self.steps_to_answer_window_layout.addWidget(self.inverse_transformation_matrix_formula_label, 5, 0)

        self.inverse_transformation_matrix_formula_with_values_label = QLabel(self) # Inverse transformation matrix with values
        self.inverse_transformation_matrix_formula_with_values_label.setStyleSheet(f"font-size: {font_size}pt")
        self.steps_to_answer_window_layout.addWidget(self.inverse_transformation_matrix_formula_with_values_label, 6, 0)

        central_widget = QWidget()
        central_widget.setLayout(self.steps_to_answer_window_layout)
        self.setCentralWidget(central_widget)

    def ITM_steps_to_answer(self):
        try:
            transformation_matrix_standard = str(array([['r11', 'r12', 'r13', 'px'], 
                                                        ['r21', 'r22', 'r23', 'py'],
                                                        ['r31', 'r32', 'r33', 'pz'],
                                                        ['0', '0', '0', '1']]))
            self.transformation_matrix_standard_label.setText(f"This is the general transformation matrix \n{transformation_matrix_standard} \n")
            
            rotation_matrix = str(array([['r11', 'r12', 'r13'],
                                         ['r21', 'r22', 'r23'],
                                         ['r31', 'r32', 'r33']]))
            self.rotation_matrix_label.setText(f"It comprises of the rotation matrix \n {rotation_matrix} \n")
            
            position_vector = str(array([['px'],
                                         ['py'],
                                         ['py']]))
            self.position_vector_label.setText(f"The position vector in column matrix form \n {position_vector} \n")
            
            bottom_row_matrix = str(array(['0','0','0','1']))
            self.bottom_row_matrix_label.setText(f"and a bottom row matrix always in the form [0,0,0,1] \n {bottom_row_matrix} \n")
            
            transformation_matrix_standard_with_values = str(array([[r11_text, r12_text, r13_text, px_text], 
                                                                [r21_text, r22_text, r23_text, py_text],
                                                                [r31_text, r32_text, r33_text, pz_text],
                                                                ['0', '0', '0', '1']]))
            self.transformation_matrix_standard_with_values_label.setText(f"These are the inputted values \n {transformation_matrix_standard_with_values} \n")

            inverse_transformation_matrix_formula = str(array([["r11", 'r21', 'r31', '-(px*r11)+(py*r21)+(pz*r31)'], 
                                                               ['r12', 'r22', 'r32', '-(px*r12)+(py*r22)+(pz*r32)'],
                                                               ['r13', 'r23', 'r33', '-(px*r13)+(py*r23)+(pz*r33)'],
                                                               ['0', '0', '0', '1']]))
            self.inverse_transformation_matrix_formula_label.setText(f"This is the inverse transformation matrix formula. Notice how the rotation matrix is transposed \n {inverse_transformation_matrix_formula} \n")

            inverse_transformation_matrix_formula_with_values = str(array([[r11, r21, r31, px_new], 
                                                                           [r12, r22, r32, py_new],
                                                                           [r13, r23, r33, pz_new],
                                                                           [0, 0, 0, 1]]))

            self.inverse_transformation_matrix_formula_with_values_label.setText(f"This is the inverse transformation matrix:\n{inverse_transformation_matrix_formula_with_values}")

        except ValueError:
            self.ITM_display_result_label.setText("Values not entered")
            print("Error 1")
        except ZeroDivisionError:
            #self.ITM_display_result_label.setText("'a' cannot be zero")
            print("Error 2")
        except Exception:
            #self.ITM_display_result_label.setText("An error occurred")
            print("Error 3")
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ITM_MainWindow()
    app.setStyle("Fusion")
    window.show()
    sys.exit(app.exec())
