#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# (c) 2017 Precedent Communications
#          Robertas Reiciunas <robertas.reiciunas@precedent.com>

group = "agents/" + _("Agent Plugins")

register_rule(group,
    "agent_config:proxmox_qemu",
    DropdownChoice(
        title = _("Proxmox QEMU Status (Linux)"),
        help = _("This will deploy the agent plugin <tt>Proxmox QEMU</tt> for monitoring the status of QEMUs."),
        choices = [
            ( True, _("Deploy plugin for Proxmox QEMU") ),
            ( None, _("Do not deploy plugin for Proxmox QEMU") ),
        ]
    )
)


