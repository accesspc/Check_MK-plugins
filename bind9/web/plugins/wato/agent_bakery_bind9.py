#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

group = "agents/" + _("Agent Plugins")

register_rule(group,
    "agent_config:bind9",
    DropdownChoice(
        title = _("Bind9 statistics (Linux)"),
        help = _("This will deploy the agent plugin <tt>bind</tt> for monitoring the Bind9 statistics."),
        choices = [
            ( True, _("Deploy plugin for Bind9") ),
            ( None, _("Do not deploy plugin for Bind9") ),
        ]
    )
)

