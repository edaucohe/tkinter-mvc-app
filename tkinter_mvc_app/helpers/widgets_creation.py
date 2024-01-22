from typing import Dict

import tkinter as tk

NAME_POS = 0
VALUE_POS = 1


def create_widgets(ttk, frame, model_attribut_names):
    # TODO To be sure about what parameters are necessaries to this function
    #  and conditions for creating widgets correctly.
    # TODO Also, I think it is in this part I need to ensure that user inputs
    #  are correctly entered.
    widgets = {}
    attributs: Dict = model_attribut_names()
    print("Atributos: ", attributs)
    for index, attribut in attributs.items():
        # Create labels
        label = ttk.Label(frame, text=attribut[NAME_POS], background="white")
        label.grid(row=index, column=0, sticky="nsew")

        if isinstance(attribut[VALUE_POS], bool):
            # Create check buttons
            checkbutton_value = tk.BooleanVar()
            check_box = ttk.Checkbutton(frame, variable=checkbutton_value)
            check_box.grid(row=index, column=1, sticky="nsew")
            value = checkbutton_value
        else:
            # Create entries
            entry = ttk.Entry(frame)
            entry.grid(row=index, column=1, sticky="nsew")
            value = entry

        widgets[index] = [label, value]

    return widgets

