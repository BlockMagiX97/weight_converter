import tkinter

def convert(to, weight):
    match to.lower():
        case "grams":
            return weight * 1000
        case "lbs":
            return weight * 2.20462262185

def update(list_label, units, weight):
    for i in range(len(units)):
        weight_after = convert(units[i], weight)
        # Change text
        list_label[i].config(text=f"{weight_after} {units[i]}")


root = tkinter.Tk()



root.mainloop()
