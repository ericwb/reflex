"""Stub file for rangeslider.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Dict, Union, overload, List, Optional
from reflex.components.libs.chakra import ChakraComponent
from reflex.components.component import Component
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain

class RangeSlider(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, value: Optional[Union[Var[List[int]], List[int]]] = None, default_value: Optional[Union[Var[List[int]], List[int]]] = None, direction: Optional[Union[Var[str], str]] = None, focus_thumb_on_change: Optional[Union[Var[bool], bool]] = None, is_disabled: Optional[Union[Var[bool], bool]] = None, is_read_only: Optional[Union[Var[bool], bool]] = None, is_reversed: Optional[Union[Var[bool], bool]] = None, min_: Optional[Union[Var[int], int]] = None, max_: Optional[Union[Var[int], int]] = None, min_steps_between_thumbs: Optional[Union[Var[int], int]] = None, **props) -> "RangeSlider": ...  # type: ignore

class RangeSliderTrack(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "RangeSliderTrack": ...  # type: ignore

class RangeSliderFilledTrack(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "RangeSliderFilledTrack": ...  # type: ignore

class RangeSliderThumb(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, index: Optional[Union[Var[int], int]] = None, **props) -> "RangeSliderThumb": ...  # type: ignore