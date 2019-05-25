# Ingrid Rose Marquez
# ingridrose.marquez@gmail.com
# +353 83 310 4348
# pts19006
from tkinter import *
from tkinter import ttk
import tkinter.filedialog as fd
import string
import csv


class Calculations:
    '''Class holding conversion formulae and field value input handling.
    '''

    def update_weight_dict(self):
        '''Fills out self.weight_dict'''
        self.weight_dict = {
            'Stones': self.entry_stones.get(),
            'Pounds': self.entry_pounds.get(),
            'Kilograms': self.entry_kilograms.get(),
        }

    def update_height_dict(self):
        self.height_dict = {
            'Feet': self.entry_feet.get(),
            'Inches': self.entry_inches.get(),
            'Centimeters': self.entry_cm.get(),
        }

    def stones_convert(self):  # 1
        '''Checks input in corresponding stones entry field. If string, blank, or <=0, fields are reset.
        If values are correct, conversion is executed.
        If successfull, entry fields buttons are set to state = 'disabled'.
        Reset button set to = 'normal'
        '''
        user_input = self.entry_stones.get()
        try:
            stones_weight = float(user_input)
        except (ValueError, TypeError):
            self.label_weight.configure(text="Non-zero numbers only and/or click matching Convert button.")
            self.entry_stones.delete(0, END)
            self.entry_pounds.delete(0, END)
            self.entry_kilograms.delete(0, END)
            self.label_display.configure(text="")
        else:
            stones_weight = float(user_input)
            if stones_weight <= 0:
                self.label_weight.configure(text="Oops! Value must be > 0...")
                self.clear_weight()
                self.label_display.configure(text="")
            else:
                # stones
                self.entry_stones.delete(0, END)
                self.entry_stones.insert(0, '%.2f' % (stones_weight))
                self.entry_stones.configure(state=DISABLED)
                self.button_stones.configure(state=DISABLED)
                # pounds
                self.entry_pounds.delete(0, END)
                self.entry_pounds.insert(0, '%.2f' % (self.stones_to_pounds(stones_weight)))
                self.entry_pounds.configure(state=DISABLED)
                self.button_pounds.configure(state=DISABLED)
                # kilograms
                self.entry_kilograms.delete(0, END)
                self.entry_kilograms.insert(0, '%.2f' % (self.pounds_to_kilograms(self.stones_to_pounds(stones_weight))))
                self.entry_kilograms.configure(state=DISABLED)
                self.button_kilograms.configure(state=DISABLED)
                self.button_clear_weight.configure(state=NORMAL)
                self.label_weight.configure(text="Weight locked. Click 'Reset' to change or 'Calculate BMI' or 'Calculate BMI'.")
                self.label_display.configure(text="")
                # update self.weight_dict
                self.update_weight_dict()

    def pounds_convert(self):  # 2
        '''Checks input in corresponding lbs entry field. If string, blank, or <=0, fields are reset.
        If values are correct, conversion is executed.
        If successfull, entry fields buttons are set to state = 'disabled'.
        Reset button set to = 'normal'
        '''
        user_input = self.entry_pounds.get()
        try:
            pounds_weight = float(user_input)
        except (ValueError, TypeError):
            self.label_weight.configure(text="Non-zero numbers only and/or click matching Convert button.")
            self.entry_stones.delete(0, END)
            self.entry_kilograms.delete(0, END)
            self.entry_pounds.delete(0, END)
            self.label_display.configure(text="")
        else:
            pounds_weight = float(user_input)
            if pounds_weight <= 0:
                self.label_weight.configure(text="")
                self.label_weight.configure(text="Oops! Value must be > 0...")
                self.clear_weight()
                self.label_display.configure(text="")
            else:
                # pounds
                self.entry_pounds.delete(0, END)
                self.entry_pounds.insert(0, '%.2f' % (pounds_weight))
                self.entry_pounds.configure(state=DISABLED)
                self.button_pounds.configure(state=DISABLED)
                # stones
                self.entry_stones.delete(0, END)
                self.entry_stones.insert(0, '%.2f' % (self.pounds_to_stones(pounds_weight)))
                self.entry_stones.configure(state=DISABLED)
                self.button_stones.configure(state=DISABLED)
                # kg
                self.entry_kilograms.delete(0, END)
                self.entry_kilograms.insert(0, '%.2f' % (self.pounds_to_kilograms(pounds_weight)))
                self.entry_kilograms.configure(state=DISABLED)
                self.button_kilograms.configure(state=DISABLED)
                self.button_clear_weight.configure(state=NORMAL)
                self.label_weight.configure(text="Weight locked. Click 'Reset' to change or click 'Calculate BMI'.")
                self.label_display.configure(text="")
                # update self.weight_dict
                self.update_weight_dict()

    def kilograms_convert(self):  # 3
        '''Checks input in corresponding kg entry field. If string, blank, or <=0, fields are reset.
        If values are correct, conversion is executed.
        If successfull, entry fields buttons are set to state = 'disabled'.
        Reset button set to = 'normal'
        '''
        user_input = self.entry_kilograms.get()
        try:
            kilograms_weight = float(user_input)
        except (ValueError, TypeError):
            self.label_weight.configure(text="Non-zero numbers only and/or click matching Convert button.")
            self.entry_stones.delete(0, END)
            self.entry_pounds.delete(0, END)
            self.entry_kilograms.delete(0, END)
            self.label_display.configure(text="")
        if kilograms_weight <= 0:
            self.label_weight.configure(text="Oops! Value must be > 0...")
            self.clear_weight()
            self.label_display.configure(text="")
        else:
            # kg
            self.entry_kilograms.delete(0, END)
            self.entry_kilograms.insert(0, '%.2f' % (kilograms_weight))
            self.entry_kilograms.configure(state=DISABLED)
            self.button_kilograms.configure(state=DISABLED)
            # stones
            self.entry_stones.delete(0, END)
            self.entry_stones.insert(0, '%.2f' % (self.pounds_to_stones(self.kilograms_to_pounds(kilograms_weight))))
            self.entry_stones.configure(state=DISABLED)
            self.button_stones.configure(state=DISABLED)
            # pounds
            self.entry_pounds.delete(0, END)
            self.entry_pounds.insert(0, '%.2f' % (self.kilograms_to_pounds(kilograms_weight)))
            self.entry_pounds.configure(state=DISABLED)
            self.button_pounds.configure(state=DISABLED)
            self.button_clear_weight.configure(state=NORMAL)
            self.label_weight.configure(text="Weight locked. Click 'Reset' to change or click 'Calculate BMI'.")
            self.label_display.configure(text="")
            # update self.weight_dict
            self.update_weight_dict()

    def feet_convert(self):  # 4
        '''Checks input in corresponding feet entry field. If string, blank, or <=0, fields are reset.
        If values are correct, conversion is executed.
        If successfull, entry fields buttons are set to state = 'disabled'.
        Reset button set to = 'normal'
        '''
        user_input = self.entry_feet.get()
        try:
            feet_height = float(user_input)
        except (ValueError, TypeError):
            self.label_height.configure(text="Non-zero numbers only and/or click matching Convert button.")
            self.entry_feet.delete(0, END)
            self.entry_inches.delete(0, END)
            self.entry_cm.delete(0, END)
            self.label_display.configure(text="")
        else:
            feet_height = float(user_input)
            if feet_height <= 0:
                self.label_height.configure(text="Oops! Value must be > 0...")
                self.clear_height()
                self.label_display.configure(text="")
            else:
                # Ft
                self.entry_feet.delete(0, END)
                self.entry_feet.insert(0, '%.2f' % (feet_height))
                self.entry_feet.configure(state=DISABLED)
                self.button_feet.configure(state=DISABLED)
                # inch
                self.entry_inches.delete(0, END)
                self.entry_inches.insert(0, '%.2f' % (self.feet_to_inches(feet_height)))
                self.entry_inches.configure(state=DISABLED)
                self.button_inches.configure(state=DISABLED)
                # cm
                self.entry_cm.delete(0, END)
                self.entry_cm.insert(0, '%.2f' % (self.inches_to_cm(self.feet_to_inches(feet_height))))
                self.entry_cm.configure(state=DISABLED)
                self.button_cm.configure(state=DISABLED)
                self.button_clear_height.configure(state=NORMAL)
                self.label_height.configure(text="Height locked. Click 'Reset' to change or click 'Calculate BMI'.")
                self.label_display.configure(text="")
                # update height_dict
                self.update_height_dict()

    def inches_convert(self):  # 5
        '''Checks input in corresponding inches entry field. If string, blank, or <=0, fields are reset.
        If values are correct, conversion is executed.
        If successfull, entry fields buttons are set to state = 'disabled'.
        Reset button set to = 'normal'
        '''
        user_input = self.entry_inches.get()
        try:
            inches_height = float(user_input)
        except (ValueError, TypeError):
            self.label_height.configure(text="Non-zero numbers only and/or click matching Convert button.")
            self.entry_feet.delete(0, END)
            self.entry_inches.delete(0, END)
            self.entry_cm.delete(0, END)
            self.label_display.configure(text="")
        else:
            inches_height = float(user_input)
            if inches_height <= 0:
                self.label_height.configure(text="Oops! Value must be > 0...")
                self.clear_height()
                self.label_display.configure(text="")
            else:
                # inch
                self.entry_inches.delete(0, END)
                self.entry_inches.insert(0, '%.2f' % (inches_height))
                self.entry_inches.configure(state=DISABLED)
                self.button_inches.configure(state=DISABLED)
                # Ft
                self.entry_feet.delete(0, END)
                self.entry_feet.insert(0, '%.2f' % (self.inches_to_feet(inches_height)))
                self.entry_feet.configure(state=DISABLED)
                self.button_feet.configure(state=DISABLED)
                # cm
                self.entry_cm.delete(0, END)
                self.entry_cm.insert(0, '%.2f' % (self.inches_to_cm(inches_height)))
                self.entry_cm.configure(state=DISABLED)
                self.button_cm.configure(state=DISABLED)
                self.button_clear_height.configure(state=NORMAL)
                self.label_height.configure(text="Height locked. Click 'Reset' to change or click 'Calculate BMI'.")
                self.label_display.configure(text="")
                # update height_dict
                self.update_height_dict()

    def cm_convert(self):  # 6
        '''Checks input in corresponding cm entry field. If string, blank, or <=0, fields are reset.
        If values are correct, conversion is executed.
        If successfull, entry fields buttons are set to state = 'disabled'.
        Reset button set to = 'normal'
        '''
        user_input = self.entry_cm.get()
        try:
            cm_height = float(user_input)
        except (ValueError, TypeError):
            self.label_height.configure(text="Non-zero numbers only and/or click matching Convert button.")
            self.entry_feet.delete(0, END)
            self.entry_inches.delete(0, END)
            self.entry_cm.delete(0, END)
            self.label_display.configure(text="")
        else:
            cm_height = float(user_input)
            if cm_height <= 0:
                self.label_height.configure(text="Oops! Value must be > 0...")
                self.clear_height()
                self.label_display.configure(text="")
            else:
                # cm
                self.entry_cm.delete(0, END)
                self.entry_cm.insert(0, '%.2f' % (cm_height))
                self.entry_cm.configure(state=DISABLED)
                self.button_cm.configure(state=DISABLED)
                # ft
                self.entry_feet.delete(0, END)
                self.entry_feet.insert(0, '%.2f' % (self.inches_to_feet(self.cm_to_inches(cm_height))))
                self.entry_feet.configure(state=DISABLED)
                self.button_feet.configure(state=DISABLED)
                # inch
                self.entry_inches.delete(0, END)
                self.entry_inches.insert(0, '%.2f' % (self.cm_to_inches(cm_height)))
                self.entry_inches.configure(state=DISABLED)
                self.button_inches.configure(state=DISABLED)
                self.button_clear_height.configure(state=NORMAL)
                self.label_height.configure(text="Height locked. Click 'Reset' to change or click 'Calculate BMI'.")
                self.label_display.configure(text="")
                # update height_dict
                self.update_height_dict()

    def calculate_bmi(self):
        '''Gets value from metric kg & cm. def run_bmi has cleared and
        ensured the format can be converted to float.
        Makes sure all conversion results are floats, then calculates actual BMI.
        '''
        cm, kg = float(self.height_dict['Centimeters']), float(self.weight_dict['Kilograms'])
        try:
            bmi = kg / ((cm / 100) ** 2)
        except (ZeroDivisionError):
            self.label_display.configure(text="Oops! How did that zero value get in?")
            self.clear_weight()
            self.clear_height()
        else:
            return bmi

    def bmi_category(self, bmi):
        '''Determines category i.e. Underweight, Obese, etc.'''
        if bmi < 18.5:
            category = 'underweight'
        elif bmi >= 18.5 and bmi < 25:
            category = 'normal (healthy weight)'
        elif bmi >= 25 and bmi < 30:
            category = 'overweight'
        else:   # bmi must be over 30
            category = 'obese'
        return category
    # FORMULA
    # weight

    def stones_to_pounds(self, weight):
        '''Converts stones to lbs'''
        return weight * 14.000

    def pounds_to_stones(self, weight):
        '''Converts lbs to stones'''
        return weight * 0.071429

    def pounds_to_kilograms(self, weight):
        '''Converts Lbs to Kg: lbs / 2.2046'''
        return weight / 2.2046

    def kilograms_to_pounds(self, weight):
        '''Converts Kg to lbs. 1 lb = kg * 2.2046'''
        return weight * 2.2046

    # height
    def feet_to_inches(self, height):
        ''''Converts Ft to inch. 1 inch = ft * 12'''
        return height * 12.00

    def inches_to_feet(self, height):
        '''from cm Converts inch to feet. 1 Ft = inch * 12'''
        return height / 12.00

    def cm_to_inches(self, height):
        '''Converts cm to inch. 1 inch = cm * 0.39370'''
        return height * 0.39370

    def inches_to_cm(self, height):
        '''Converts inch to cm. 1 cm = inch / 0.39370'''
        return height / 0.39370


class Interface(Calculations):
    '''Class for Tk Object and setup for fields & buttons'''

    def __init__(self, root):
        # === DATA === #
        self.weight_dict = {}
        self.height_dict = {}
        self.name_dict = {}
        self.bmi_data = {}
        self.file_name = ''
        # === FRAMES === #
        self.name_frame = ttk.LabelFrame(root, text='Enter your details:')
        self.name_frame.pack(fill=BOTH, padx=2, pady=2)
        self.weight_frame = ttk.LabelFrame(root, text='Weight')
        self.weight_frame.pack(fill=BOTH, padx=2, pady=2)
        self.height_frame = ttk.LabelFrame(root, text='Height')
        self.height_frame.pack(fill=BOTH, padx=2, pady=2)
        self.bmi_frame = ttk.LabelFrame(root, text='BMI Result')
        self.bmi_frame.pack(fill=BOTH, padx=2, pady=2)
        # === LABELS === #
        # name
        self.label_name = Label(self.name_frame, text='Name:')
        self.label_name.grid(row=0, column=0, padx=5, pady=5, sticky=E)
        # weight scale names
        # stones
        self.label_stones = Label(self.weight_frame, text='Stones:')
        self.label_stones.grid(row=0, column=0, padx=5, pady=5, sticky=E)
        # pounds
        self.label_pounds = Label(self.weight_frame, text='Pounds:')
        self.label_pounds.grid(row=0, column=2, padx=5, pady=5, sticky=E)
        # kilograms
        self.label_kilograms = Label(self.weight_frame, text='Kilograms:')
        self.label_kilograms.grid(row=0, column=4, padx=5, pady=5, sticky=E)
        # weight validation display
        self.label_weight = Label(self.weight_frame)
        self.label_weight.grid(row=2, column=0, columnspan=5, padx=5, pady=10, sticky=W + E + N + S)
        self.label_weight.configure(text='Enter your weight in one of the boxes & convert')
        # weight validation display
        self.label_height = Label(self.height_frame)
        self.label_height.grid(row=2, column=0, columnspan=5, padx=5, pady=10, sticky=W + E + N + S)
        self.label_height.configure(text='Enter your height in one of the boxes & convert')
        # height scale names
        # feet
        self.label_feet = Label(self.height_frame, text='Feet:')
        self.label_feet.grid(row=0, column=0, padx=5, pady=5, sticky=E)
        # inches
        self.label_inches = Label(self.height_frame, text='Inches:')
        self.label_inches.grid(row=0, column=2, padx=5, pady=5, sticky=E)
        # centimeters
        self.label_cm = Label(self.height_frame, text='Centimeters:')
        self.label_cm.grid(row=0, column=4, padx=5, pady=5, sticky=E)
        # BMI analysis display
        self.label_bmi = Label(self.bmi_frame, width=60, bg='#99e6e6' ,wraplength=450, justify=LEFT)
        self.label_bmi.grid(row=0, column=0, columnspan=9, padx=10, pady=10, sticky=W)
        # Error messages to user
        self.label_display = Label(self.bmi_frame, bg='#ffda8f', width=60, wraplength=450, justify=LEFT)
        self.label_display.grid(row=1, column=0, columnspan=9, padx=10, pady=10, sticky=W)
        # === ENTRY BOXES === #
        # name box
        self.text_name = StringVar()
        self.text_name.set('')
        self.entry_name = ttk.Entry(self.name_frame, textvariable=self.text_name, width=20)
        self.entry_name.grid(row=0, column=1, columnspan=3, padx=5, pady=5, sticky=W)
        # height
        # feet
        self.text_feet = StringVar()
        self.text_feet.set('')
        self.entry_feet = ttk.Entry(self.height_frame, textvariable=self.text_feet, width=10)
        self.entry_feet.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        # inches
        self.text_inches = StringVar()
        self.text_inches.set('')
        self.entry_inches = ttk.Entry(self.height_frame, textvariable=self.text_inches, width=10)
        self.entry_inches.grid(row=0, column=3, padx=5, pady=5, sticky=W)
        # centimeters
        self.text_cm = StringVar()
        self.text_cm.set('')
        self.entry_cm = ttk.Entry(self.height_frame, textvariable=self.text_cm, width=10)
        self.entry_cm.grid(row=0, column=5, padx=5, pady=5, sticky=W)
        # weight entry boxes
        # stones
        self.text_stones = StringVar()
        self.text_stones.set('')
        self.entry_stones = ttk.Entry(self.weight_frame, textvariable=self.text_stones, width=10)
        self.entry_stones.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        # pounds
        self.text_pounds = StringVar()
        self.text_pounds.set('')
        self.entry_pounds = ttk.Entry(self.weight_frame, textvariable=self.text_pounds, width=10)
        self.entry_pounds.grid(row=0, column=3, padx=5, pady=5, sticky=W)
        # kilograms
        self.text_kilograms = StringVar()
        self.text_kilograms.set('')
        self.entry_kilograms = ttk.Entry(self.weight_frame, textvariable=self.text_kilograms, width=10)
        self.entry_kilograms.grid(row=0, column=5, padx=5, pady=5, sticky=W)
        # === BUTTONS === #
        # stones
        self.button_stones = ttk.Button(self.weight_frame, text='Convert Stones >>', command=self.stones_convert)
        self.button_stones.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=W)
        # pounds
        self.button_pounds = ttk.Button(self.weight_frame, text='< Convert Pounds >', command=self.pounds_convert)
        self.button_pounds.grid(row=1, column=2, columnspan=2, padx=5, pady=5)
        # kilograms
        self.button_kilograms = ttk.Button(self.weight_frame, text='<< Convert Kilograms', command=self.kilograms_convert)
        self.button_kilograms.grid(row=1, column=4, columnspan=2, padx=5, pady=5, sticky=E)
        # buttons
        # feet
        self.button_feet = ttk.Button(self.height_frame, text='Convert Feet >>', command=self.feet_convert)
        self.button_feet.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=W)
        # inches
        self.button_inches = ttk.Button(self.height_frame, text='< Convert Inches >', command=self.inches_convert)
        self.button_inches.grid(row=1, column=2, columnspan=2, padx=5, pady=5)
        # centimeters
        self.button_cm = ttk.Button(self.height_frame, text='<< Convert Centimeters ', command=self.cm_convert)
        self.button_cm.grid(row=1, column=4, columnspan=2, padx=4, pady=5, sticky=E)
        # clear weight
        self.button_clear_weight = ttk.Button(self.weight_frame, text='Reset', state=DISABLED, command=self.clear_weight)
        self.button_clear_weight.grid(row=2, column=5, columnspan=1, padx=5, pady=5, sticky=E)
        # clear height
        self.button_clear_height = ttk.Button(self.height_frame, text='Reset', state=DISABLED, command=self.clear_height)
        self.button_clear_height.grid(row=2, column=5, columnspan=1, padx=5, pady=5, sticky=E)
        # bmi calculate
        self.button_calc_bmi = ttk.Button(self.bmi_frame, text='Calculate BMI', command=self.run_bmi)
        self.button_calc_bmi.grid(row=2, column=0, columnspan=1, padx=5, pady=10, sticky=W + E + N + S)
        # clear data
        self.button_restart = ttk.Button(self.bmi_frame, text='Restart', command=self.reset)
        self.button_restart.grid(row=2, column=2, columnspan=1, padx=5, pady=10, sticky=W + E + N + S)
        # IO buttons - save
        self.button_save = ttk.Button(self.bmi_frame, text='Save', state=DISABLED, command=self.save)
        self.button_save.grid(row=2, column=4, columnspan=1, padx=5, pady=10, sticky=W + E + N + S)
        # IO buttons - save as
        self.button_save_as = ttk.Button(self.bmi_frame, text='Save As', state=DISABLED, command=self.save_as)
        self.button_save_as.grid(row=2, column=6, columnspan=1, padx=5, pady=10, sticky=W + E + N + S)

    def clear_bmi_display(self):
        '''Clears BMI frame labels'''
        self.label_bmi.configure(text='')
        self.label_display.configure(text='')

    def clear_weight(self):
        '''Enables all weight entry fields and clears current input values.
        After successful reset of entry fields, button is disabled.
        Becomes enabled after convert is triggered and is successful.
        '''
        self.weight_dict.clear()
        # stones
        self.button_stones.configure(state=NORMAL)
        self.entry_stones.configure(state=NORMAL)
        self.entry_stones.delete(0, END)
        # lbs
        self.button_pounds.configure(state=NORMAL)
        self.entry_pounds.configure(state=NORMAL)
        self.entry_pounds.delete(0, END)
        # kg
        self.button_kilograms.configure(state=NORMAL)
        self.entry_kilograms.configure(state=NORMAL)
        self.entry_kilograms.delete(0, END)
        self.button_clear_weight.configure(state=DISABLED)
        # weight frame label
        self.label_weight.configure(text='Enter your weight in one of the boxes & convert')
        # bmi
        self.clear_bmi_display()
        # disable save buttons
        self.button_save.configure(state=DISABLED)
        self.button_save_as.configure(state=DISABLED)

    def clear_height(self):
        self.height_dict.clear()
        # stones
        self.button_feet.configure(state=NORMAL)
        self.entry_feet.configure(state=NORMAL)
        self.entry_feet.delete(0, END)
        # lbs
        self.button_inches.configure(state=NORMAL)
        self.entry_inches.configure(state=NORMAL)
        self.entry_inches.delete(0, END)
        # kg
        self.button_cm.configure(state=NORMAL)
        self.entry_cm.configure(state=NORMAL)
        self.entry_cm.delete(0, END)
        self.button_clear_height.configure(state=DISABLED)
        # height frame label
        self.label_height.configure(text='Enter your height in one of the boxes & convert')
        # bmi
        self.clear_bmi_display()
        # disable save buttons
        self.button_save.configure(state=DISABLED)
        self.button_save_as.configure(state=DISABLED)

    def reset(self):
        '''Enables all weight & height & name entry fields and clears current input values.
        '''
        # clear weight and height
        self.clear_weight()
        self.clear_height()
        # clear BMI frame
        self.clear_bmi_display()
        # clear name and label
        self.entry_name.configure(state=NORMAL)
        self.entry_name.delete(0, END)
        # disable save buttons
        self.button_save.configure(state=DISABLED)
        self.button_save_as.configure(state=DISABLED)
        # enable BMI Calculate btton
        self.button_calc_bmi.configure(state=NORMAL)

    def run_bmi(self):
        '''Checks if there are entries in the name field, one of the height and name fields.
        If yes, proceeds to check if convert is successful;
        all weight & height conv btns & entry fields = 'disabled.'
        If all conditions met, move to calculate BMI
        '''
        self.label_display.configure(text='')
        self.name_dict = {
            'Name': self.entry_name.get(),
        }
        name = [self.entry_name.get()]  # convert to list to easily combine with height & weight lists
        w_fields = [
            self.entry_stones.get(),
            self.entry_pounds.get(),
            self.entry_kilograms.get(),
        ]
        h_fields = [
            self.entry_feet.get(),
            self.entry_inches.get(),
            self.entry_cm.get(),
        ]
        w_f_fields = w_fields + h_fields
        n_w_f_fields = w_f_fields + name
        # all/most combinations of field entry being forgotten
        if not any(n_w_f_fields):
            self.label_display.configure(text="Oops! You didn't input anything.")
        elif not any(w_fields) and not any(name):
            self.label_display.configure(text="Oops! You forgot to input your name & weight.")
        elif not any(h_fields) and not any(name):
            self.label_display.configure(text="Oops! You forgot to input your name & height.")
        elif not any(name) and any(w_f_fields):
            self.label_display.configure(text="Oops! You forgot to input your name.")
        elif not any(w_f_fields) and any(name):
            self.label_display.configure(text="Oops! You forgot to input your weight & height.")
        elif not any(w_fields):
            self.label_display.configure(text="Oops! You forgot to input your weight.")
        elif not any(h_fields):
            self.label_display.configure(text="Oops! You forgot to input your height.")
        # check if set convert buttons are executed successfully; dictionary not empty
        elif not self.weight_dict and not self.height_dict:
            self.label_display.configure(text="Oops! You forgot to convert weight & height.")
        elif not self.weight_dict and self.height_dict:
            self.label_display.configure(text="Oops! You forgot to convert weight.")
        elif not self.height_dict and self.weight_dict:
            self.label_display.configure(text="Oops! You forgot to convert height.")
        else:   # try to calculate BMI
            self.entry_name.configure(state=DISABLED)   # stop furthr changes to name
            user = self.name_dict['Name']
            bmi = float(self.calculate_bmi())
            category = self.bmi_category(bmi)
            self.label_bmi.configure(text=f"{user}, your BMI is {bmi: .2f} which is {category}.")
            # build dictionary
            self.bmi_data.update(self.name_dict)
            self.bmi_data.update(self.weight_dict)
            self.bmi_data.update(self.height_dict)
            self.bmi_data['BMI'] = f'{bmi: .2f}'
            self.bmi_data['Category'] = category
            self.button_calc_bmi.configure(state=DISABLED)
            self.button_save.configure(state=NORMAL)
            self.button_save_as.configure(state=NORMAL)

    def get_csv_name(self):
        replacers = ['\\', '/', ':']
        f = str(self.file_name)
        for r in replacers:
            f = f.replace(r, ' ')
            chunks = f.split(' ')
        name = chunks[len(chunks) - 1]
        return name

    def save_as(self):
        '''Becomes clickable only when BMI is successfully calculated'''
        self.file_name = fd.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[
                ("Data files", ".csv"),
                ("all files", ".*"),
            ]
        )
        try:
            self.write_file()
        except FileNotFoundError:
            self.label_display.configure(text='Please input a file name.')
        else:
            csv_name = self.get_csv_name()
            root.title(f'BMI Calculator - {csv_name}')
            self.label_display.configure(text=f'Results saved in {self.file_name}')

    def save(self):
        '''Becomes clickable only when BMI is successfully calculated'''
        print(self.file_name)
        self.label_display.configure(text='')
        if not self.file_name:
            self.save_as()
        else:
            self.write_file()
            self.label_display.configure(text=f'Re-saved file {self.file_name}')

    def write_file(self):
        '''Convert self.bmi_data into csv'''
        with open(file=self.file_name, mode='w', newline='') as csv_file:
            csv_fields = list(self.bmi_data.keys())
            csv_values = list(self.bmi_data.values())
            writer = csv.writer(csv_file)
            writer.writerow(csv_fields)
            writer.writerow(csv_values)


if __name__ == "__main__":
    root = Tk()
    app = Interface(root)
    root.title('BMI Calculator')
    root.resizable(False, False)
    root.mainloop()
