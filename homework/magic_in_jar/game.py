import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import math

# Рецепты: 2 элемента -> новый элемент
combinations = {
    frozenset(["Вода", "Земля"]): "Грязь",
    frozenset(["Огонь", "Вода"]): "Пар",
    frozenset(["Огонь", "Земля"]): "Лава",
    frozenset(["Воздух", "Вода"]): "Облако",
    frozenset(["Воздух", "Огонь"]): "Энергия",
    frozenset(["Воздух", "Земля"]): "Пыль",
    frozenset(["Лава", "Земля"]): "Вулкан",
    frozenset(["Облако", "Вода"]): "Дождь",
    frozenset(["Дождь", "Земля"]): "Растение",
    frozenset(["Огонь", "Пыль"]): "Метеор",
    frozenset(["Метеор", "Облако"]): "Звездопад",
    frozenset(["Лава", "Вода"]): "Камень",
    frozenset(["Камень", "Огонь"]): "Металл",
    frozenset(["Металл", "Огонь"]): "Наковальня",
    frozenset(["Растение", "Вода"]): "Водоросли",
    frozenset(["Растение", "Земля"]): "Дерево",
    frozenset(["Дерево", "Огонь"]): "Уголь",
    frozenset(["Уголь", "Огонь"]): "Алмаз",
    frozenset(["Песок", "Огонь"]): "Стекло",
    frozenset(["Камень", "Воздух"]): "Песок",
}

ASSET_FILES = {
    "Вода": "water.png",
    "Огонь": "fire.png",
    "Земля": "earth.png",
    "Воздух": "air.png",
    "Грязь": "mud.png",
    "Пар": "steam.png",
    "Лава": "lava.png",
    "Облако": "cloud.png",
    "Энергия": "energy.png",
    "Пыль": "dust.png",
    "Вулкан": "volcano.png",
    "Дождь": "rain.png",
    "Растение": "plant.png",
    "Метеор": "meteor.png",
    "Звездопад": "shooting_stars.png",
    "Камень": "stone.png",
    "Металл": "metal.png",
    "Наковальня": "anvil.png",
    "Водоросли": "algae.png",
    "Дерево": "tree.png",
    "Уголь": "coal.png",
    "Алмаз": "diamond.png",
    "Песок": "sand.png",
    "Стекло": "glass.png",
}

class Element:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        key = frozenset([self.name, other.name])
        if key in combinations:
            return Element(combinations[key])
        return None

    def decompose(self):
        for elements, result in combinations.items():
            if result == self.name:
                return tuple(elements)
        return None

    def __str__(self):
        return self.name

class AlchemyGame:
    def __init__(self):
        self.elements = {
            "Вода": Element("Вода"),
            "Огонь": Element("Огонь"),
            "Земля": Element("Земля"),
            "Воздух": Element("Воздух"),
        }

    def combine(self, name1, name2):
        if name1 not in self.elements or name2 not in self.elements:
            return None, False
        result = self.elements[name1] + self.elements[name2]
        if result is None:
            return None, False
        is_new = result.name not in self.elements
        self.elements[result.name] = result
        return result, is_new

    def show_elements(self):
        return list(self.elements.keys())

class AlchemyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Магия в банке")
        self.root.geometry("1180x760")
        self.root.configure(bg="#0b0f1a")
        self.root.resizable(False, False)

        self.game = AlchemyGame()
        self.max_attempts = 40
        self.attempts_left = self.max_attempts
        self.items = {}
        self.images = {}
        self.drag_data = {"name": None, "x": 0, "y": 0}

        self.canvas = tk.Canvas(root, width=1180, height=760, bg="#303030", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.load_assets()
        self.draw_hud()
        self.spawn_start_elements()

    def load_assets(self):
        assets_dir = os.path.join(os.path.dirname(__file__), "assets")
        for name, filename in ASSET_FILES.items():
            path = os.path.join(assets_dir, filename)
            if os.path.exists(path):
                img = Image.open(path).convert("RGBA").resize((86, 86), Image.LANCZOS)
                self.images[name] = ImageTk.PhotoImage(img)

    def draw_hud(self):
        self.title_text = self.canvas.create_text(24, 18, anchor="nw", text="Магия в банке", fill="#ffd36a", font=("Arial", 24, "bold"))
        self.counter_text = self.canvas.create_text(24, 58, anchor="nw", text="", fill="#eeeeee", font=("Arial", 14))
        self.attempts_text = self.canvas.create_text(24, 84, anchor="nw", text="", fill="#ffb3b3", font=("Arial", 14, "bold"))
        self.hint_text = self.canvas.create_text(24, 112, anchor="nw", text="Перетащи один элемент на другой, чтобы смешать", fill="#c9c9c9", font=("Arial", 12))
        self.update_hud()

    def update_hud(self):
        total = len(set(combinations.values()) | {"Вода", "Огонь", "Земля", "Воздух"})
        self.canvas.itemconfig(self.counter_text, text=f"Открыто: {len(self.game.elements)} / {total}")
        self.canvas.itemconfig(self.attempts_text, text=f"Попытки: {self.attempts_left} / {self.max_attempts}")

    def spawn_start_elements(self):
        positions = {
            "Огонь": (110, 230),
            "Вода": (280, 360),
            "Земля": (480, 240),
            "Воздух": (700, 350),
        }
        for name, (x, y) in positions.items():
            self.create_element_view(name, x, y)

    def create_element_view(self, name, x, y):
        if name in self.items:
            return
        image = self.images.get(name)
        if image:
            icon_id = self.canvas.create_image(x, y, image=image, tags=("element", name))
        else:
            icon_id = self.canvas.create_text(x, y, text="?", fill="white", font=("Arial", 42), tags=("element", name))

        label_id = self.canvas.create_text(x, y + 70, text=name, fill="white", font=("Arial", 19), tags=("element", name))
        self.items[name] = {"icon": icon_id, "label": label_id, "x": x, "y": y}
        for item_id in (icon_id, label_id):
            self.canvas.tag_bind(item_id, "<ButtonPress-1>", self.start_drag)
            self.canvas.tag_bind(item_id, "<B1-Motion>", self.drag)
            self.canvas.tag_bind(item_id, "<ButtonRelease-1>", self.end_drag)
        self.update_hud()

    def get_name_by_item(self, item_id):
        for tag in self.canvas.gettags(item_id):
            if tag != "element":
                return tag
        return None

    def start_drag(self, event):
        if self.attempts_left <= 0:
            return
        item = self.canvas.find_closest(event.x, event.y)[0]
        name = self.get_name_by_item(item)
        if not name:
            return
        self.drag_data = {"name": name, "x": event.x, "y": event.y}
        self.canvas.tag_raise(self.items[name]["icon"])
        self.canvas.tag_raise(self.items[name]["label"])

    def drag(self, event):
        name = self.drag_data["name"]
        if not name:
            return
        dx = event.x - self.drag_data["x"]
        dy = event.y - self.drag_data["y"]
        self.canvas.move(self.items[name]["icon"], dx, dy)
        self.canvas.move(self.items[name]["label"], dx, dy)
        self.items[name]["x"] += dx
        self.items[name]["y"] += dy
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

    def end_drag(self):
        name = self.drag_data["name"]
        if not name:
            return
        target = self.find_collision(name)
        if target is not None:
            self.try_combine(name, target)
        self.drag_data["name"] = None

    def find_collision(self, dragged_name):
        x1, y1 = self.items[dragged_name]["x"], self.items[dragged_name]["y"]
        for name, data in self.items.items():
            if name == dragged_name:
                continue
            x2, y2 = data["x"], data["y"]
            if math.hypot(x1 - x2, y1 - y2) < 92:
                return name
        return None

    def try_combine(self, a, b):
        self.attempts_left -= 1
        result, is_new = self.game.combine(a, b)
        x = (self.items[a]["x"] + self.items[b]["x"]) // 2
        y = (self.items[a]["y"] + self.items[b]["y"]) // 2

        if result is None:
            self.flash_text("Ничего не вышло", x, y - 92, "#ff9c9c")
        elif is_new:
            self.create_element_view(result.name, x, y)
            self.flash_text(f"Новый элемент: {result.name}", x, y - 92, "#ffd36a")
        else:
            self.flash_text(f"Уже открыто: {result.name}", x, y - 92, "#cfcfcf")

        self.update_hud()
        self.check_end()

    def flash_text(self, text, x, y, color):
        text_id = self.canvas.create_text(x, y, text=text, fill=color, font=("Arial", 18, "bold"))
        self.root.after(1300, lambda: self.canvas.delete(text_id))

    def check_end(self):
        total = len(set(combinations.values()) | {"Вода", "Огонь", "Земля", "Воздух"})
        if len(self.game.elements) >= total:
            messagebox.showinfo("Победа", "Ты открыл все элементы!")
        elif self.attempts_left <= 0:
            messagebox.showinfo("Конец игры", "Попытки закончились. Запусти игру заново, чтобы попробовать ещё раз.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AlchemyApp(root)
    root.mainloop()
