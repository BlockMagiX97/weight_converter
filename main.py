import tkinter

units = ["Grams", "Lbs"]

def convert(to, weight):
    # Converts kgs to lbs and grams
    match to.lower():
        case "grams":
            return weight * 1000
        case "lbs":
            return weight * 2.20462262185

def update(list_label, units, weight):
    # Updates output labels
    try:
        for i in range(len(units)):
            weight_after = convert(units[i], float(weight))
            # Change text
            list_label[i].config(text=f"{weight_after} {units[i]}")
    except ValueError:
        list_label[0].config(text="Insert a valid number")
        for label in list_label[1:]:
            label.config(text="")

# Graphical part
root = tkinter.Tk()

inputFrame = tkinter.Frame(root)
outputFrame = tkinter.Frame(root)

listLabels = [tkinter.Label(outputFrame), tkinter.Label(outputFrame)]

weightEntry = tkinter.Entry(inputFrame)
weightEntry.insert(0, "Insert a weight in kgs")
weightEntry.pack(side=tkinter.LEFT)

updateButton = tkinter.Button(inputFrame , text="UPDATE", command=lambda: update(listLabels, units, weightEntry.get()))
updateButton.pack(side=tkinter.RIGHT)

# Adds labels to the screen
for label in listLabels:
    label.pack()

inputFrame.pack()
outputFrame.pack()

root.mainloop()
