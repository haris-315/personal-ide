# from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from os import remove,system,startfile,getcwd
from kivy.graphics import Line
from kivy.graphics import Color
import subprocess
from kivy.uix.colorpicker import get_color_from_hex
import json
from filter_for_json import *
# from pygments.lexers import get_lexer_for_filename
from kivy.uix.button import Button
from kivymd.tools.hotreload.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.chip import MDChip,MDChipText
import threading
import prerunconfig
from pygame import mixer
import keyboard
from essentials import *