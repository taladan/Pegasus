#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Menu Callsign:

EvMenu(caller, menu_data,
       startnode="start",
       cmdset_mergetype="Replace", cmdset_priority=1,
       auto_quit=True, auto_look=True, auto_help=True,
       cmd_on_exit="look",
       nodetext_formatter=dedent_strip_nodetext_formatter,
       options_formatter=evtable_options_formatter,
       node_formatter=underline_node_formatter,
       input_parser=evtable_parse_input,
       persistent=False,
       **kwargs)



 - `caller` (Object or Account): is a reference to the object using the menu. This object will
 get  a new [CmdSet](CmdSet) assigned to it, for handling the menu.

 - `menu_data` (str, module or dict): is a python path to a module with menu-node functions or the
 module itself. Alternatively you can give a Python dictionary `{"nodename":function, ...}`. How
 these node-functions should look is described in the next section.

 - `startnode` (str): is the name of the menu-node to start the menu at. Changing this means that
 you can jump into a menu tree at different positions depending on circumstance and thus possibly
 re-use menu entries.

 - `cmdset_mergetype` (str): This is usually one of "Replace" or "Union" (see [CmdSets](CmdSets).
 The first means that the menu is exclusive - the user has no access to any other commands while in
 the menu. The Union mergetype means the menu co-exists with previous commands (and may overload
 them, so be careful as to what to name your menu entries in this case).

 - `cmdset_priority` (int): The priority with which to merge in the menu cmdset. This allows for
 advanced usage.

 - `auto_quit`, `auto_look`, `auto_help` (bool): If either of these are `True`, the menu
 automatically makes a `quit`, `look` or `help` command available to the user. The main reason why
 you'd want to turn this off is if  you want to use the aliases "q", "l" or "h" for something in
 your menu. Nevertheless, at least `quit` is highly recommend - if `False`, the menu *must* itself
 supply an "exit node" (a node without any options), or the user will be stuck in the menu until
 the server reloads (or eternally if the menu is `persistent`)!

 - `cmd_on_exit` (str): This command string will be executed right *after* the menu has closed
 down. From experience, it's useful to trigger a "look" command to make sure the user is aware of
 the change of state; but any command can be used. If set to `None`, no command will be triggered
 after exiting the menu.

 - `nodetext_formatter` (callable) - this is used to format the main text (only) of each node.

 - `options_formatter` (callable) - this is used to format how node options are displayed

 - `node_formatter` (callable) - this formats the entire node, possibly after first being processed
 by the other formatters. Commonly used to put a frame around the node and similar.

 - `input_parser` (callable) - this is parsing the input from the user in respect to the node
 currently active and to respond correctly. Changing this can change the entire functionality of
 EvMenu. This doesn't usually need to be modified.

 - `persistent` (bool) - if `True`, the menu will survive a reload (so the user will not be kicked
 out by the reload - make sure they can exit on their own!)

 - All other keyword arguments will be available as initial data for the nodes. They will be
 available in all nodes as properties on `caller.ndb._menutree` (see below). These will also
 survive a `@reload` if the menu is `persistent`.


You don't need to store the EvMenu instance anywhere - the very act of initializing it will store
it as `caller.ndb._menutree` on the `caller`. This object will be deleted automatically when the
menu is exited and you can also use it to store your own temporary variables for access throughout
the menu. Currently though, temporary variables you store on a persistent `_menutree` as it runs
will *not* survive a `@reload`, only those you set as part of the original `EvMenu` call.
"""

def pegasus_node_formatter(nodetext, optionstext):
    pass

def pegasus_nodetext_formatter(nodetext):
    """Justifies text to 72 character width

    :return: nodetext formatted"""
    width = 72
    nodetext = justify(nodetext, width=width, align="c", indent=1)
    return dedent(nodetext).strip()
