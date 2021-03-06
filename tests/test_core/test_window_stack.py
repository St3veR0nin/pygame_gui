import os
import pytest
import pygame

from tests.shared_fixtures import _init_pygame, default_ui_manager, default_display_surface, _display_surface_return_none

from pygame_gui.core.ui_window_stack import UIWindowStack
from pygame_gui.core.ui_window import UIWindow


class TestWindowStack:
    def test_creation(self, _init_pygame):
        UIWindowStack((800, 600))

    def test_add_window(self, _init_pygame, default_ui_manager):
        stack = UIWindowStack((800, 600))
        window = UIWindow(pygame.Rect(100, 100, 200, 200), manager=default_ui_manager, element_ids=[])
        stack.add_new_window(window)

        assert len(stack.stack) == 1

    def test_remove_window(self, _init_pygame, default_ui_manager):
        stack = UIWindowStack((800, 600))
        window = UIWindow(pygame.Rect(100, 100, 200, 200), manager=default_ui_manager, element_ids=[])
        window_2 = UIWindow(pygame.Rect(50, 50, 200, 200), manager=default_ui_manager, element_ids=[])
        window_3 = UIWindow(pygame.Rect(0, 0, 200, 200), manager=default_ui_manager, element_ids=[])
        stack.add_new_window(window)
        stack.add_new_window(window_2)
        stack.add_new_window(window_3)
        stack.remove_window(window)
        stack.remove_window(window_2)
        stack.remove_window(window_3)

        assert len(stack.stack) == 0

    def test_move_window_to_front(self, _init_pygame, default_ui_manager):
        stack = UIWindowStack((800, 600))
        window = UIWindow(pygame.Rect(100, 100, 200, 200), manager=default_ui_manager, element_ids=[])
        window_2 = UIWindow(pygame.Rect(50, 50, 200, 200), manager=default_ui_manager, element_ids=[])
        window_3 = UIWindow(pygame.Rect(0, 0, 200, 200), manager=default_ui_manager, element_ids=[])
        stack.add_new_window(window)
        stack.add_new_window(window_2)
        stack.add_new_window(window_3)
        stack.move_window_to_front(window)
        stack.move_window_to_front(window_3)
        stack.move_window_to_front(window_2)

        assert stack.stack[0] == window

    def test_is_window_at_top(self, _init_pygame, default_ui_manager):
        stack = UIWindowStack((800, 600))
        window = UIWindow(pygame.Rect(100, 100, 200, 200), manager=default_ui_manager, element_ids=[])
        window_2 = UIWindow(pygame.Rect(50, 50, 200, 200), manager=default_ui_manager, element_ids=[])
        window_3 = UIWindow(pygame.Rect(0, 0, 200, 200), manager=default_ui_manager, element_ids=[])
        stack.add_new_window(window)
        stack.add_new_window(window_2)
        stack.add_new_window(window_3)
        stack.move_window_to_front(window)
        stack.move_window_to_front(window_3)
        stack.move_window_to_front(window_2)

        assert stack.is_window_at_top(window_2) is True
        assert stack.is_window_at_top(window) is False
        assert stack.is_window_at_top(window_3) is False
