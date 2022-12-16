#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : Recommender Systems: Towards Deep Learning State-of-the-Art                         #
# Version    : 0.1.0                                                                               #
# Python     : 3.10.6                                                                              #
# Filename   : /recsys/core/repo/base.py                                                           #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : https://github.com/john-james-ai/Recommender-Systems                                #
# ------------------------------------------------------------------------------------------------ #
# Created    : Thursday December 8th 2022 04:23:19 pm                                              #
# Modified   : Wednesday December 14th 2022 03:18:10 am                                            #
# ------------------------------------------------------------------------------------------------ #
# License    : MIT License                                                                         #
# Copyright  : (c) 2022 John James                                                                 #
# ================================================================================================ #
from abc import abstractmethod

from recsys.core.entity.base import Entity
from recsys.core.services.base import Service
# ------------------------------------------------------------------------------------------------ #


class Repo(Service):
    """Repository base class"""

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def add(self, entity: Entity) -> Entity:
        """Adds an entity to the repository and returns the Entity with the id added."""

    @abstractmethod
    def get(self, id: str) -> Entity:
        "Returns an entity with the designated id"

    @abstractmethod
    def update(self, entity: Entity) -> None:
        """Updates an entity in the database."""

    @abstractmethod
    def remove(self, id: str) -> None:
        """Removes an entity with id from repository."""

    @abstractmethod
    def exists(self, id: str) -> bool:
        """Returns True if entity with id exists in the repository."""

    @abstractmethod
    def print(self) -> None:
        """Prints the repository contents as a DataFrame."""
