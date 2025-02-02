from base import *
# from reloader import reload


def settings(settings: dict={},read=False,Write=False,file: str='') -> dict:
    if Write:
        with open(file,'w') as f:
            f.write(Filter(settings).GetResult())
    if read:
        with open(file,'r') as f:
            js_obj = json.loads(f.read())

        return js_obj




# prerun directory setup
dir_alias = getcwd()
li_sliced = dir_alias.split('\\')
dir_alias = dir_alias.removesuffix(li_sliced[-1])





global file
global rel_ready
file = ""
setting_file = f"{dir_alias}Data\\settings\\settings.json"
pre_def_styles = f"{dir_alias}Data\\pre_defined_styles\\styles.json"
# rel_ready = False








class BaseSettingsLoader:
    def __init__(self) -> None:
        self.dict_set = settings(read=True,file=setting_file)
        self.auto_save = self.dict_set['auto_save']
    def settings_writer(self):
        settings(settings={
            "windows_color": app.s3.elements['winscol'].text if app.s3.elements['winscol'].text != '' else app.s3.setting['windows_color'],
            "border_color": app.s3.elements['bordcol'].text if app.s3.elements['bordcol'].text != '' else app.s3.setting['border_color'],
            "text_color": app.s3.elements['textcol'].text if app.s3.elements['textcol'].text != '' else app.s3.setting['text_color'],
            "buttons_color": app.s3.elements['btncol'].text if app.s3.elements['btncol'].text != '' else app.s3.setting['buttons_color'],
            "auto_save": BaseSettings.auto_save
        },Write=True,file=setting_file)

BaseSettings = BaseSettingsLoader()


class FileCreationPopup(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.elements = self.ids
        
    def createfile(self):
        try:
            with open(f'{app.s1.elements["chooser"].path}\\{self.elements["createfile"].text}',"x") as f:
                f.close()
            app.s1.fileview_updater()
        except Exception as e:
            print(e)

class CMDChip(MDChip):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.theme_bg_color = "Custom"
        self.focus_color = None
    def on_active(self, instance_check, active_value: bool) -> None:
        super().on_active(instance_check, active_value)
        self.add_marked_icon_to_chip()





class CMDCard(MDCard):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.theme_bg_color = "Custom"
        self.md_bg_color = app.styler.brc
class CMDLabel(MDLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text_color = app.styler.fgc


class Style:
    def __init__(self, **kwargs):
        self.start_cls = settings(read=True,file=setting_file)
        self.fgc = get_color_from_hex(self.start_cls['text_color'])
        self.bgc = get_color_from_hex(self.start_cls['buttons_color'])
        self.brc = get_color_from_hex(self.start_cls['border_color'])
        self.wbc = get_color_from_hex(self.start_cls['windows_color'])


class Theming(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.elements = self.ids
        self.border_col = ''
        self.window = Window
        self.classes = self.cls
        self.setting = settings(read=True,file=setting_file)
        self.windows_color = app.styler.wbc
        self.text_color = app.styler.fgc
        self.buttons_color = app.styler.bgc
        self.border_color = app.styler.brc
        app.s1.window.clearcolor = self.windows_color
        app.s2.window.clearcolor = self.windows_color
        self.window.clearcolor = self.windows_color
    def apply_style(self):
        BaseSettings.settings_writer()
        self.border_color = get_color_from_hex(self.elements['bordcol'].text)
        self.windows_color = get_color_from_hex(self.elements['winscol'].text)
        self.text_color = get_color_from_hex(self.elements['textcol'].text)
        self.buttons_color = get_color_from_hex(self.elements['btncol'].text)

        if self.border_color != []:
            try:
                app.s1.classes['brdr'].background_color = self.border_color
                app.s2.classes['brdr'].background_color = self.border_color
                app.s3.classes['brdr'].background_color = self.border_color
            except Exception as e:
                print(e)
            
        if self.windows_color != []:
            try:
                app.s1.window.clearcolor = self.windows_color
                app.s2.window.clearcolor = self.windows_color
                app.s3.window.clearcolor = self.windows_color
            except Exception as e:
                print(e)

        if self.buttons_color != []:
            try:
                app.styler.bgc = self.buttons_color
                app.styler.bgc = self.buttons_color
                app.styler.bgc = self.buttons_color
                
                
                
            except Exception as e:
                print(e)
        if self.buttons_color != []:
            try:
                app.styler.fgc = self.text_color
                app.styler.fgc = self.text_color
                app.styler.fgc = self.text_color
            except Exception as e:
                print(e)
        # if self.buttons_color != [] or self.border_color != []:
    def back_to_home_screen(self):
        self.manager.transition.direction = 'down'
        self.manager.current = 'first'


class Screen1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.elements = self.ids
        self.window = Window
        self.chooser = self.elements['chooser']
        self.classes = self.cls

    def on_touch_down(self, touch):
        super().on_touch_down(touch)
        # self.chooser.selection = []
    def go_to_editor_screen(self):
        global file
        self.file:list = self.chooser.selection
        file = self.file[0] if self.file != [] else ''
        self.manager.transition.direction = 'left'
        self.manager.current = 'second' if self.file != [] else 'first'
        app.s2.showcontent()
    
    def go_to_theme_changer(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'third'


    def fileview_updater(self):
        self.path_befor_del:str = self.chooser.path
        alias_path = self.path_befor_del.split("\\")
        self.chooser.path = self.path_befor_del.removesuffix(alias_path[-1])
        self.chooser.path = self.path_befor_del
    
    def file_info(self):
        try:
            self.file_size = self.chooser.get_nice_size(self.chooser.selection[0])
            self.file_path:str = self.chooser.selection[0]
            self.alias_f_n = self.file_path.split("\\")[-1]
            self.elements['filename'].text = "FileName:\n"+self.alias_f_n
            self.elements['filetype'].text = "FileType:\n   "+self.alias_f_n[self.alias_f_n.find('.'):] if '.' in self.alias_f_n else "FileType:\n   "+"N\\A"
            self.elements['filesize'].text = "FileSize:\n   "+self.file_size
            # self.elements['titlepath'].text = 'FilePath:'
            self.elements['filepath'].text = "FilePath:\n   "+self.file_path
            threading.Thread(target=self.search_highlighting()).start()
        except Exception as e:
            print(e)



    def deletefile(self):
        try:
            self.file_if_del = self.chooser.selection[0]
            remove(self.file_if_del)
            self.fileview_updater()
            self.chooser.selection = []
        except Exception as e:
            print(f"Error: {e}")


    def createfile(self):
        popup_secne = FileCreationPopup()
        creation_window = Popup(title="Create New File.", content=popup_secne,size_hint=(None,None),size=(200,200))
        creation_window.open()

    def search_highlighting(self):
        try:
            # self.lexer_def = get_lexer_for_filename(self.chooser.selection[0])
            # if self.lexer_def:
            #     app.s2.elements['editor'].lexer = self.lexer_def
            print("hi")
        except Exception as e:
            print(e)
            pass






class Screen2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.elements = self.ids
        self.window = Window
        self.elements['terminalctrl'].text = "Open Terminal"
        self.editor = self.elements['editor']
        self.elements['auto_save'].active = BaseSettings.auto_save
        self.auto_close_elements = {
            "(" : ")",
            "[" : "]",
            "{" : "}",
            '"' : '"',
            "'" : "'",
            "`" : "`"
        }

    def on_touch_down(self, touch):
        super().on_touch_down(touch)
        if self.elements['auto_save'].collide_point(int(touch.x),int(touch.y)):
            BaseSettings.auto_save = not BaseSettings.auto_save
            BaseSettings.settings_writer()


    def go_to_selection_screen(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'
        app.title = "IDE"


    def showcontent(self):
        # if self.response.file_existance_check(file) == None:
        #     print("file not supported!")
    
        app.title = file
        with open(file,'r') as f:
            self.editor.text = f.read()
        

    def savecontent(self):
        with open(file,'w') as f:
            f.write(self.editor.text)
    
    def auto_save(self):
        pass

    def suggestions(self):
        pass
    def runfile(self):
        if BaseSettings.auto_save:
            self.savecontent()
        self.response = prerunconfig.Configure(file)
        if self.response.controller == "ready":

            self.response.run()
        else:
            print("run not supported!")
    


class Myapp(MDApp):
    def build(self):
        self.terminal_is_act = False
        # self.theme_cls.theme_style = "Dark"
        Window.bind(on_key_down=self.Kb_engine)
        self.styler = Style()
        mixer.init()
        self.sound = mixer.Sound("../Data/audios/kps.wav")
        sm = ScreenManager()
        self.s1 = Screen1()
        self.s2 = Screen2()
        self.s3 = Theming()
        sm.add_widget(self.s1)
        sm.add_widget(self.s2)
        sm.add_widget(self.s3)
        # self.sound_thread.daemon = True
        # self.sound_thread.start()

        return sm


    # Function to play sound on keypress

    def Kb_engine(self,inst,keyboard, keycode, text, modifiers):
        self.special_keys = modifiers
        # hotkey control
        if self.s2.editor.focus:
            self.sound.play()
        
        # delete word with ctrl+backspace
        # no text check
        if self.s2.editor.cursor_col != 0:
            if self.s2.editor.cursor_index() != 0:
                self.ntc = self.s2.editor.text[self.s2.editor.cursor_index()-1:self.s2.editor.cursor_index()]
                if self.ntc not in rem_with_ctrl:
                    if 'ctrl' in modifiers and keycode == 42:
                        editor = self.s2.editor
                        text:str = editor.text

                        ci = editor.cursor_index()
                        text_part = text[:ci]
                        global working_line
                        global final
                        global splitter
                        try:
                            line_spl_text:list = text_part.split("\n")
                            working_line = line_spl_text[len(line_spl_text)-1]
                            for char in str(working_line[::-1]):
                                if char in rem_with_ctrl:
                                    splitter = char

                            if splitter not in working_line:
                                # text_part = text_part+" %$#@!!^&"
                                removed_text = text_part.removesuffix(working_line) + ''

                                final = text.replace(text_part,removed_text)
                                editor.text = final
                            else:
                                space_spl_text:list = text_part.split(splitter)
                                removed_text = working_line.removesuffix(space_spl_text[-1])
                                text_part_fin = text_part.replace(working_line,removed_text)
                                final = text.removeprefix(text_part)
                                
                                final = text_part_fin+final+splitter
                                editor.text = final
                                # editor.do_cursor_movement("cursor_left",control=True)
                                # editor.cursor = col,row-space_spl_text[-1]
                        except Exception as e:
                            print(e)
                            removed_text = '\n'
                            final = text.replace(text_part,removed_text)
                        
                            # self.s2.editor.text = final


        self.key = text
        # AutoClosing
        if self.s2.editor.focus:
            if 'shift' in modifiers:
                if  self.key == "'":
                    self.key = '"'
                elif self.key == "9" or self.key == 9:
                    self.key = '('
                elif self.key =="[":
                    self.key = '{'
            if self.key in self.s2.auto_close_elements.keys():
                self.s2.editor.insert_text(self.s2.auto_close_elements[self.key])
                self.s2.editor.cursor = (self.s2.editor.cursor[0]-1,self.s2.editor.cursor[1])
   


app = Myapp()
app.title = "IDE"

app.run()