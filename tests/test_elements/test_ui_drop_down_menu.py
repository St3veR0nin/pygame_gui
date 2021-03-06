import os
import pytest
import pygame

from tests.shared_fixtures import _init_pygame, default_ui_manager, default_display_surface, _display_surface_return_none

from pygame_gui.ui_manager import UIManager
from pygame_gui.elements.ui_drop_down_menu import UIDropDownMenu


class TestUIDropDownMenu:

    def test_creation(self, _init_pygame, default_ui_manager):
        menu = UIDropDownMenu(options_list=['eggs', 'flour', 'sugar'],
                              starting_option='eggs',
                              relative_rect=pygame.Rect(100, 100, 200, 30),
                              manager=default_ui_manager)
        assert menu.image is not None

    def test_kill(self, _init_pygame, default_ui_manager):
        menu = UIDropDownMenu(options_list=['eggs', 'flour', 'sugar'],
                              starting_option='eggs',
                              relative_rect=pygame.Rect(100, 100, 200, 30),
                              manager=default_ui_manager)
        menu.kill()

        assert menu.alive() is False

    def test_update_closed(self, _init_pygame, default_ui_manager):
        menu = UIDropDownMenu(options_list=['eggs', 'flour', 'sugar'],
                              starting_option='eggs',
                              relative_rect=pygame.Rect(100, 100, 200, 30),
                              manager=default_ui_manager)
        menu.update(0.01)
        assert menu.image is not None

    def test_update_state_transition(self, _init_pygame, default_ui_manager):
        menu = UIDropDownMenu(options_list=['eggs', 'flour', 'sugar'],
                              starting_option='eggs',
                              relative_rect=pygame.Rect(100, 100, 200, 30),
                              manager=default_ui_manager)
        menu.current_state.should_transition = True
        menu.update(0.01)
        menu.current_state.menu_buttons[0].pressed = True
        menu.update(0.01)
        assert menu.image is not None

    def test_update_closed_state_close_button(self, _init_pygame, default_ui_manager):
        menu = UIDropDownMenu(options_list=['eggs', 'flour', 'sugar'],
                              starting_option='eggs',
                              relative_rect=pygame.Rect(100, 100, 200, 30),
                              manager=default_ui_manager)
        menu.current_state.should_transition = True
        menu.update(0.01)
        menu.current_state.close_button.pressed = True
        menu.update(0.01)
        assert menu.image is not None

    def test_update_open_state_finish(self, _init_pygame, default_ui_manager):
        menu = UIDropDownMenu(options_list=['eggs', 'flour', 'sugar'],
                              starting_option='eggs',
                              relative_rect=pygame.Rect(100, 100, 200, 30),
                              manager=default_ui_manager)
        menu.current_state.should_transition = True
        menu.update(0.01)
        menu.current_state.should_transition = True
        menu.update(0.01)
        menu.current_state.open_button.pressed = True
        menu.update(0.01)
        assert menu.image is not None

    def test_rebuild_from_theme_data_non_default(self, _init_pygame):
        manager = UIManager((800, 600), os.path.join("tests", "data",
                                                     "themes", "ui_drop_down_menu_non_default.json"))

        menu = UIDropDownMenu(options_list=['eggs', 'flour', 'sugar'],
                              starting_option='eggs',
                              relative_rect=pygame.Rect(100, 100, 200, 30),
                              manager=manager)
        menu.current_state.should_transition = True
        menu.update(0.01)
        menu.current_state.should_transition = True
        menu.update(0.01)
        manager.ui_theme.ui_element_misc_data['drop_down_menu']['expand_direction'] = 'down'
        menu.rebuild_from_changed_theme_data()
        assert menu.image is not None

    @pytest.mark.filterwarnings("ignore:Invalid value")
    @pytest.mark.filterwarnings("ignore:Colour hex code")
    def test_rebuild_from_theme_data_bad_values(self, _init_pygame):
        manager = UIManager((800, 600), os.path.join("tests", "data",
                                                     "themes", "ui_drop_down_menu_bad_values.json"))

        menu = UIDropDownMenu(options_list=['eggs', 'flour', 'sugar'],
                              starting_option='eggs',
                              relative_rect=pygame.Rect(100, 100, 200, 30),
                              manager=manager)
        assert menu.image is not None
