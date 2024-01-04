"""
Calculator App using Flet Framework

Overview:
This is a simple calculator app built with Python and the Flet framework. It supports basic arithmetic operations, percentage calculation, and toggling between positive and negative numbers.

Key Features:
- Responsive user interface with Flet framework components.
- Error handling for division by zero.
- Basic arithmetic operations (+, -, *, /) and additional functions (% and +/-).
- Clear and concise code structure with reusable components.
"""

# Import necessary Flet components
import flet
from flet import (Column,
                  Container,
                  ElevatedButton,
                  Page,
                  Row,
                  Text,
                  UserControl,
                  border_radius,
                  colors,
                  )
# Define the CalculatorApp class, which inherits from UserControl
class CalculatorApp(UserControl):
    def build(self):
        # Initialize the calculator state
        self.reset()
        # Create a Text control to display the result
        self.result = Text(value='0', color=colors.WHITE, size=20)
        
        # Return the main Container with the calculator layout
        return Container(
            width=300,
            bgcolor=colors.BLACK,
            border_radius=border_radius.all(20),
            padding=20,
            content=Column(
                # Rows of buttons for different operations
                # Each button has a specific background color, text, and data attribute
                # The on_click attribute is set to the button_clicked method
                # Buttons are organized in Rows and Columns for a clean layout
                controls=[
                    Row(
                        controls=[self.result],
                        alignment='end'
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text='AC',
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data='AC',
                            ),
                            ElevatedButton(
                                text='+/-',
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data='+/-',
                            ),
                            ElevatedButton(
                                text='%',
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data='%',
                            ),
                            ElevatedButton(
                                text='/',
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data='/',
                            ),
                            
                        ],
                        
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text='7',
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data='7',
                            ),
                            ElevatedButton(
                                text='8', 
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data='8',
                            ),
                            
                            ElevatedButton(
                                text="9",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="9",
                            ),
                            ElevatedButton(
                                text='*',
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data='*',
                            )
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text='4',
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data='4',
                            ),
                            ElevatedButton(
                                text="5",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="5",
                            ),
                            ElevatedButton(
                                text='6',
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data='6',
                            ),
                            ElevatedButton(
                                text='-',
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data='-',
                            ),
                        ],
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text='1',
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data='1',
                            ),
                            ElevatedButton(
                                text='2',
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data='2',
                            ), 
                            ElevatedButton(
                                text='3',
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data='3',
                            ), 
                            ElevatedButton(
                                text='+',
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data='+',
                            )
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text='0',
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=2,
                                on_click=self.button_clicked,
                                data='0',
                            ),
                            ElevatedButton(
                                text='.',
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data='.',
                            ), 
                            ElevatedButton(
                                text='=',
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data='=',
                            )
                        ]
                    )
                ]
            )
        )
        
    # Method to handle button clicks
    def button_clicked(self, e):
        # Extract data from the clicked button
        data = e.control.data
        
        # Handle different button actions based on data
        # Update the result display and calculator state accordingly

        if self.result.value == 'Error' or data == 'AC':
            self.result.value = '0'
            self.reset()
        elif data in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.' ):
            if self.result.value == '0' or self.new_operand == True:
                self.result.value = data
                self.new_operand = False
                
            else:
                self.result.value = self.result.value + data
        elif data in ('+', '-', '*', '/'):
            self.result.value = self.calculate(
                self.operand1, 
                float(self.result.value), 
                self.operator
                )
            self.operator = data
            if self.result.value == 'Error':
                self.operand1 = '0'
            
            else:
                self.operand1 = float(self.result.value)
                
            self.new_operand = True
            
        elif data in ('='):
            self.result.value = self.calculate(
                self.operand1, 
                float(self.result.value), 
                self.operator
            )
            self.reset()
            
        elif data in ('%'):
            self.result.value = float(self.result.value) / 100
            self.reset()
            
        elif data in ('+/-'):
            if float(self.result.value) > 0:
                self.result.value = '-' + str(self.result.value)
            elif float(self.result.value) < 0:
                self.result.value = str(self.format_number(abs(float(self.result.value))))
                
        self.update()
    
    # Method to format numbers based on whether they are integers or floats
    def format_number(self, num):
        # Logic to check if the number is an integer or a float and format accordingly
        if num % 1 == 0:
            return int(num)
        else:
            return num

    # Method to perform arithmetic calculations
    def calculate(self, operand1, operand2, operator):
        # Use try-except block to handle potential errors, such as division by zero
        try:
            if operator == "+":
                return self.format_number(operand1 + operand2)

            elif operator == "-":
                return self.format_number(operand1 - operand2)

            elif operator == "*":
                return self.format_number(operand1 * operand2)

            elif operator == "/":
                if operand2 == 0:
                    return "Error"
                else:
                    return self.format_number(operand1 / operand2)
        except ZeroDivisionError:
            return "Cannot divide by zero"
        
    # Method to reset the calculator state
    def reset(self):
        self.operator = "+"
        self.operand1 = 0
        self.new_operand = True

# Main function to run the calculator app
def main(page: Page):
    page.title = "Calc App"

    # create application instance
    calc = CalculatorApp()

    # add application's root control to the page
    page.add(calc)

# Run the Flet app with the specified port and target function
flet.app(port=8550, target=main, view=flet.AppView.WEB_BROWSER)
            
        
    