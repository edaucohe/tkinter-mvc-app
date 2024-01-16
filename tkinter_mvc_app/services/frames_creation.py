from typing import Dict


def create_frames(ttk, frame, model_attribut_names):
    attributs: Dict = model_attribut_names()
    print("Atributos: ", attributs)
    for index, attribut in attributs.items():
        # Create labels
        label = ttk.Label(frame, text=attribut[0], background="white")
        label.grid(row=index, column=0, sticky="nsew")

        if isinstance(attribut[1], bool):
            # Create check buttons
            check_box = ttk.Checkbutton(frame)
            check_box.grid(row=index, column=1, sticky="nsew")
        else:
            # Create entries
            entry = ttk.Entry(frame)
            entry.grid(row=index, column=1, sticky="nsew")

# create_frames()
