import tkinter as tk
from entity.contact import Contact


class ListboxWithSearch:

    def __init__(self, root, contacts: list[Contact]):

        # key index(在控件里的编号) value Contact
        self.index_contact_map = {}

        self.frame = tk.LabelFrame(root, text="请选择导出联系人")
        self.tool_frame = tk.Frame(self.frame)
        self.tool_frame.pack()

        self.search_label = tk.Label(self.tool_frame, text="搜索：")
        self.search_label.pack(side='left')

        self.re = tk.Entry(self.tool_frame, width=10)
        self.re.pack(side='left')
        self.re.bind("<KeyRelease>", self.filter)

        self.select_all_button = tk.Button(self.tool_frame, text="全选", command=self.select_all)
        self.select_all_button.pack(side='left', padx="10")

        self.invert_select_button = tk.Button(self.tool_frame, text="反选", command=self.invert_select)
        self.invert_select_button.pack(side='left', padx="2")

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.lb = tk.Listbox(self.frame, selectmode='multiple', height=20, width=30, exportselection=False,
                             yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.lb.yview)

        self.lb.bind('<<ListboxSelect>>', self.on_select)

        self.lb.pack()
        self.contacts = contacts


        for index, contact in enumerate(contacts):
            text = f'{contact.nickName}({contact.remark})' if contact.remark else f'{contact.nickName}'
            self.lb.insert(index, text)
            self.index_contact_map[index] = contact

    def select_all(self, event=None):
        for index in self.index_contact_map.keys():
            self.lb.select_set(index)
        self.on_select()

    def on_select(self, event=None):
        selection = self.lb.curselection()
        self.frame.config(text=f"已选择{len(selection)}个联系人")

    def invert_select(self, event=None):
        """反选"""
        selected = self.lb.curselection()
        for index in self.index_contact_map.keys():
            if index in selected:
                self.lb.selection_clear(index)
            else:
                self.lb.select_set(index)
        self.on_select()

    def get_contacts(self, event=None):
        contacts = []
        selected = self.lb.curselection()
        for index in selected:
            contacts.append(self.index_contact_map.get(index))
        return contacts

    def filter(self, event=None):
        p = self.re.get()
        if p:
            for index, contact in self.index_contact_map.items():
                text = f'{contact.nickName}({contact.remark})' if contact.remark else f'{contact.nickName}'
                if p in text:
                    self.lb.yview(index)
                    break
