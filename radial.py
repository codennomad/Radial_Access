import tkinter as tk
import math
import keyboard
import mouse
import json
import subprocess 
import os
from tkinter import ttk, messagebox

class RadialMenu:
    '''A radial Menu implementation using Tkinter'''
    def __init__(self, root):
        """Initialize the radial menu with main window and configuration."""
        self.root = root
        self.root.overrideredirect(True)
        self.root.attributes('-topmost', True)
        self.root.attributes('-alpha', 0.95)
        self.root.withdraw()
        
        # Create transparent background window to capture clicks
        self.background_window = tk.Toplevel(root)
        self.background_window.withdraw()
        self.background_window.attributes('-alpha', 0.01)
        self.background_window.attributes('-topmost', True)
        self.background_window.overrideredirect(True)
        self.background_window.bind('<Button-1>', lambda e: self.hide_menu())
        
        self.root.attributes('-alpha', 1.0)
        self.root.attributes('-transparentcolor', 'black')
        
        # Color scheme
        self.bg_color = 'black'
        self.slice_color = '#2E2E2E'
        self.hover_color = '#3E3E3E'
        self.line_color = '#484848'
        
        # Menu dimensions
        self.size = 450
        self.canvas = tk.Canvas(
            root, 
            width=self.size, 
            height=self.size, 
            bg=self.bg_color, 
            highlightthickness=0
        )
        self.canvas.pack()
        
        self.load_config()
        self.create_radial_menu()
        
        # Bind events
        self.canvas.bind('<Button-1>', self.handle_click)
        self.canvas.bind('<Motion>', self.handle_hover)
        self.canvas.bind('<Leave>', self.handle_leave)
        self.root.bind('<Escape>', lambda e: self.hide_menu())
        self.canvas.bind('<Button-3>', lambda e: self.hide_menu())
        
        # Bind middle mouse click
        mouse.on_middle_click(self.show_menu)
        
    def create_radial_menu(self):
        """Create the radial menu UI with slices and text."""
        center_x = self.size / 2
        center_y = self.size / 2
        outer_radius = self.size * 0.45  # Fixed multiplication operator
        inner_radius = self.size * 0.15  # Fixed multiplication operator
        
        # Create outer circle
        self.canvas.create_oval(
            2, 2, 
            self.size-2, self.size-2, 
            fill=self.bg_color, 
            outline=self.line_color
        )
        
        # Create slices
        for i, option in enumerate(self.options):
            start_angle = (2 * math.pi * i) / len(self.options) - math.pi / 2
            end_angle = (2 * math.pi * (i + 1)) / len(self.options) - math.pi / 2
            
            # Create slice points
            points = [center_x, center_y]
            steps = 20
            
            for step in range(steps + 1):
                angle = start_angle + (end_angle - start_angle) * step / steps
                points.extend([
                    center_x + outer_radius * math.cos(angle),
                    center_y + outer_radius * math.sin(angle)  # Added missing y-coordinate
                ])
                
            # Create slice
            self.canvas.create_polygon(
                points,
                fill=self.slice_color,
                outline=self.line_color,
                width=1,
                tags=f'slice_{i}'
            )
            
            # Add text
            text_angle = (start_angle + end_angle) / 2
            text_radius = outer_radius * 0.6
            text_x = center_x + text_radius * math.cos(text_angle)
            text_y = center_y + text_radius * math.sin(text_angle)
            
            self.canvas.create_text(
                text_x, text_y,
                text=option['item'],  # Fixed dictionary access
                fill='white',
                font=('Segoe UI', 9, 'bold'),  # Increased font size for better readability
                anchor='center',
                tags=f'text_{i}'
            )
            
            # Draw dividing lines
            self.canvas.create_line(
                center_x, center_y,
                center_x + outer_radius * math.cos(start_angle),
                center_y + outer_radius * math.sin(start_angle),
                fill=self.line_color,
                width=1
            )
            
    def load_config(self):
        """Load menu configuration from JSON file."""
        try:
            with open('radial_config.json', 'r', encoding='utf-8') as f:
                config = json.load(f)
                self.options = [
                    {
                        'item': item['nome'],
                        'type': item['tipo'],
                        'cmd': item['comando']
                    } 
                    for item in config['opcoes']
                ]
        except FileNotFoundError:
            messagebox.showerror("Error", "Configuration file (radial_config.json) not found!")
            self.root.quit()
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Error reading configuration file!")
            self.root.quit()
            
    def show_menu(self):
        """Display the radial menu centered on mouse position."""
        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Configure background window
        self.background_window.geometry(f"{screen_width}x{screen_height}+0+0")
        self.background_window.deiconify()
        
        # Get mouse position and center menu
        x = self.root.winfo_pointerx()
        y = self.root.winfo_pointery()  # Fixed method name
        self.root.geometry(f"{self.size}x{self.size}+{x-self.size//2}+{y-self.size//2}")  # Fixed size reference
        self.root.deiconify()
        self.root.lift()
        
    def hide_menu(self):
        """Hide both the radial menu and background window."""
        self.root.withdraw()
        self.background_window.withdraw()
        
    def handle_click(self, event):
        """Handle mouse click events on menu items."""
        clicked_items = self.canvas.find_closest(event.x, event.y)
        if clicked_items:
            tags = self.canvas.gettags(clicked_items[0])
            for tag in tags:
                if tag.startswith("slice_"):
                    index = int(tag.split("_")[1])
                    option = self.options[index]  # Fixed dictionary access
                    self.hide_menu()
                    self.execute_command(option['type'], option['cmd'])
                    break
                
    def handle_hover(self, event):
        """Handle hover effects on menu items."""
        items = self.canvas.find_closest(event.x, event.y)
        if items:
            for i in range(len(self.options)):
                self.canvas.itemconfig(f"slice_{i}", fill=self.slice_color)
            tags = self.canvas.gettags(items[0])
            for tag in tags:
                if tag.startswith("slice_"):
                    self.canvas.itemconfig(tag, fill=self.hover_color)
                    break
                
    def handle_leave(self, event):
        """Reset hover effects when mouse leaves menu."""
        for i in range(len(self.options)):
            self.canvas.itemconfig(f"slice_{i}", fill=self.slice_color)
            
    def execute_command(self, tipo, comando):
        """Execute the command associated with a menu item."""
        try:
            if tipo == "processo":
                if os.path.exists(comando):
                    subprocess.Popen(comando)
                else:
                    subprocess.Popen(comando, shell=True)
            elif tipo == "tecla":
                keyboard.send(comando)
        except Exception as e:
            messagebox.showerror("Error", f"Error executing command: {str(e)}")

if __name__ == '__main__':
    root = tk.Tk()
    app = RadialMenu(root)
    root.mainloop()