# ============================================================================
# FILE: context.py
# AUTHOR: Shougo Matsushita <Shougo.Matsu at gmail.com>
# License: MIT license
# ============================================================================

import typing


class Context(typing.NamedTuple):
    args: typing.List[str] = []
    auto_cd: bool = False
    columns: str = ''
    cursor: int = 0
    direction: str = ''
    fnamewidth: int = 0
    listed: bool = False
    profile: bool = False
    search: str = ''
    split: str = 'no'
    toggle: bool = False
    targets: typing.List[dict] = []
    winwidth: int = 0
