import tkinter as tk
from tkinter import messagebox, simpledialog

contacts = []

def refresh_list():
    listbox.delete(0, tk.END)
    for c in contacts:
        listbox.insert(tk.END, f"{c['name']} - {c['phone']}")

def clear_fields():
    for e in entries.values(): e.delete(0, tk.END)

def add_contact():
    c = {k:e.get() for k,e in entries.items()}
    if c['name'] and c['phone']:
        contacts.append(c)
        refresh_list()
        clear_fields()
    else:
        messagebox.showwarning("Missing","Name and phone are required")

def show_selected(_=None):
    if not listbox.curselection():return
    i=listbox.curselection()[0]
    for k in entries:
        entries[k].delete(0,tk.END)
        entries[k].insert(0,contacts[i][k])
    
def update_contact():
    if not listbox.curselection(): return
    i = listbox.curselection()[0]
    contacts[i] = {k: e.get() for k, e in entries.items()}
    refresh_list()


def delete_contact():
    if not listbox.curselection(): return
    i = listbox.curselection()[0]
    contacts.pop(i)
    refresh_list()
    clear_fields()


def search_contact():
    keyword = simpledialog.askstring("Search", "Enter name or phone:")
    if keyword:
        for i, c in enumerate(contacts):
            if keyword.lower() in c['name'].lower() or keyword in c['phone']:
                listbox.select_clear(0, tk.END)
                listbox.select_set(i)
                show_selected()
                return
            messagebox.showinfo("Not found", "Contact not found")

root = tk.Tk()
root.title("Contact Book")
root.geometry("400x400")

fields = ['name','phone','email','address']
entries =  {}
for i, f in enumerate(fields):
    tk.Label(root, text=f.capitalize()).grid(row=i, column=0,sticky='w',padx=10,pady=2)
    e = tk.Entry(root,width=30)
    e.grid(row=i,column=1)
    entries[f] = e 

tk.Button(root,text="Add",command=add_contact).grid(row=4,column=0,pady=5)
tk.Button(root,text="Update",command=update_contact).grid(row=4,column=1,sticky="w")
tk.Button(root,text="Delete",command=delete_contact).grid(row=4,column=1)
tk.Button(root,text="Search",command=search_contact).grid(row=4,column=1,sticky="e")

listbox = tk.Listbox(root, width=50)
listbox.grid(row=5, column=0, columnspan=2, pady=10)
listbox.bind("<<ListboxSelect>>", show_selected)

root.mainloop()


