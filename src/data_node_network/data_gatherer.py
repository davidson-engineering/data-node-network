#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Matthew Davidson
# Created Date: 2024-01-23
# Copyright © 2024 Davidson Engineering Ltd.
# ---------------------------------------------------------------------------
"""A data gatherer node server for the data node network."""
# ---------------------------------------------------------------------------

import logging
import time
import random

from data_node_network.server import (
    NodeServerTCP,
    NodeServerTCP,
)
from data_node_network.configuration import (
    config_global,
    node_commands,
)

config = config_global["node_network"]
READ_LIMIT = config["read_limit"]

logger = logging.getLogger("data_node_network.nodes")


class GathererNodeTCP(NodeServerTCP):
    def __init__(
        self,
        host="localhost",
        port=0,
        name=None,
        node_id=None,
    ):
        super().__init__(
            host=host,
            port=port,
            name=name,
            node_id=node_id,
            node_type="data-gatherer",
        )
        self.command_menu = node_commands["data-gatherer"]

    async def handle_request(self, request):
        response = self.command(request)
        return response

    def get_data(self):
        data = self.gather_data()
        data = self.process_data(data)
        return data

    def gather_data(self):
        raise NotImplementedError("Subclasses must implement handle_client method")

    def process_data(self, data):
        raise NotImplementedError("Subclasses must implement handle_client method")

    def time(self):
        return {f"node-{self.node_id}_time": time.time()}

    def get_status(self):
        return "Node is running"

    def get_node_info(self):
        return {
            "node_id": self.node_id,
            "node_address": self.node_address_str,
            "node_type": "data-gatherer",
            "node_status": self.node_status,
            "time": time.time(),
        }

    def start_logging(self):
        return "Logging started"

    def stop_logging(self):
        return "Logging stopped"

    def reset_node(self):
        return "Node reset"

    def get_file(self):
        return "File"

    def get_file_list(self):
        return "File list"

    @property
    def node_status(self):
        return "Node status"
