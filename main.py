from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.treeview import TreeView, TreeViewNode, TreeViewLabel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import kivy

kivy.require("2.2.1")

Window.size = (400, 800)

# class LogInApp(MDApp):
#     def build(self):
#         global screen_manager
#         screen_manager = ScreenManager()
#         #self.manager = ScreenManager(transition = NoTransition())
#         screen_manager.add_widget(Builder.load_file("pre-splash.kv"))
#         screen_manager.add_widget(Builder.load_file("login.kv"))
#         return screen_manager
        
#     def on_start(self):
#         Clock.schedule_once(self.login, 7)
        
#     def login(self, *args):
#         screen_manager.current = "login"

class TreeViewApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical')
        self.treeview = TreeView(root_options=dict(text="Treeview"))

        # Add your treeview to the root widget
        self.root.add_widget(self.treeview)

        # Add buttons for add, remove, and export
        add_button = Button(text="Add Item")
        remove_button = Button(text="Remove Item")
        export_button = Button(text="Export to Excel")

        add_button.bind(on_release=self.add_item)
        remove_button.bind(on_release=self.remove_item)
        export_button.bind(on_release=self.export_to_excel)

        self.root.add_widget(add_button)
        self.root.add_widget(remove_button)
        self.root.add_widget(export_button)

        return self.root

    def add_item(self, instance):
        new_node = TreeViewNode(text="New Item")
        label = TreeViewLabel(text="Sub Item")

        # Add the label to the node
        new_node.add_widget(label)

        # Add the node to the treeview
        self.treeview.add_node(new_node)


    def remove_item(self, instance):
        # Add logic to remove items from the treeview
        pass
    
    def edit_item(self, instance):
        if selected_node := self.treeview.selected_node:
            # Create a TextInput widget to replace the TreeViewLabel for editing
            text_input = TextInput(text=selected_node.text)
            text_input.bind(on_text_validate=lambda instance: self.finish_editing(selected_node, text_input))

            # Replace the label with the text input
            selected_node.remove_widget(selected_node.label)
            selected_node.label = text_input
            selected_node.add_widget(text_input)

    def finish_editing(self, node, text_input):
        # Get the edited text from the TextInput
        edited_text = text_input.text

        # Update the text of the TreeViewLabel
        node.label.text = edited_text

        # Remove the TextInput and restore the label
        node.remove_widget(text_input)
        node.add_widget(node.label)


    def export_to_excel(self, instance):
        # Add logic to export treeview data to Excel
        pass




if __name__  == '__main__':
    # LogInApp().run()
    TreeViewApp().run()