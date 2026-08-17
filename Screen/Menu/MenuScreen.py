import arcade
import MenuWidget

from arcade.gui import(
    UIManager,
    UITextureButton,
    UIAnchorLayout,
    UIView,
    UIButtonRow,
    UILabel,
    UIBoxLayout,
)

class PauseMenu(UIAnchorLayout):
    def __init__(self):
        super().__init__()
    

class MenuView(UIView):
    def __init__(self):
        super().__init__()
        self.background_color = arcade.uicolor.BLACK
        
        root = self.add_widget(UIAnchorLayout())
        
        #Setup navigation area
        nav_area = UIAnchorLayout(vertical=True, size_hint=())
        
        
        self.ui = UIManager()
        
    def on_show_view(self):
        self.ui.enable()
    
    def on_hide_view(self):
        self.ui.disable()
        
    def on_draw(self):
        self.clear(color=arcade.uicolor.WHITE)
        
        self.ui.draw()
