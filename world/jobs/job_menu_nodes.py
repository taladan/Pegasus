#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Nodes for the jobs system menus"""

def root(text, raw_string):
    pass

### Create a job manually
def create(text, raw_string):
    """+job/create - spawn job creation menu
    ```
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║  Job Creation........1 ...........................2 Mygamename...........3  ║
    ╠═════════════════════════════════════════════════════════════════════════════╣
    ║  1. Title..........................A                                        ║
    ║  2. Bucket.........................B                                        ║
    ║  3. Options........................C                                        ║
    ║  4. Message........................D                                        ║
    ║                                                                             ║
    ╠═════════════════════════════════════════════════════════════════════════════╣
    ║ ╭─────────────────────────────────────────────────────────────────────────╮ ║
    ║ │ ....................................................................... │ ║
    ║ │ ....................................................................... │ ║
    ║ │ ....................................................................... │ ║
    ║ │ ....................................................................... │ ║
    ║ │ ....................................................................... │ ║
    ║ │ ....................................................................... │ ║
    ║ │ ....................................................................... │ ║
    ║ │ ......................................................................4 │ ║
    ║ ╰─────────────────────────────────────────────────────────────────────────╯ ║
    ╚═════════════════════════════════════════════════════════════════════════════╝
    ```

    Menu variables
    ---
    1. System
    2. Menu Title
    3. Gamename
    4. Menu text

    Menu Options
    ---
    A. Title ~:> if title is not None, dbsave
    B. Bucket ~:> if exists and player can post, dbsave
    C. Options ~:> enter options menu
    D. Message ~:> if msg is not None, dbsave


    |Option|DB Variable                   |
    |------|------------------------------|
    |Title |`ndb._menutree.title`         |
    |Bucket|`ndb._menutree.bucket`        |
    |Tags  |`ndb._menutree.tagged_players`|
    |Msg   |`ndb._menutree.message`       |


    Jobs Limits and legend
    ---
    job_number = 1
    message_line_length = 75
    message_line_count = 18+??
        pass
    """

    def clear(caller, raw_string):
        pass

    def search(caller, raw_string):
        pass

    def views(caller, raw_string):
        pass

    def player_input(caller, raw_string):
        import inspect
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        node = calframe[1][3]
        input = raw_string
        options = {"key": "_default",
                   "goto": node}
        return text, options
