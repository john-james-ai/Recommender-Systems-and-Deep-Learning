#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : Recommender Systems: Towards Deep Learning State-of-the-Art                         #
# Version    : 0.1.0                                                                               #
# Python     : 3.10.6                                                                              #
# Filename   : /recsys/core/repo/datasource.py                                                     #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : https://github.com/john-james-ai/Recommender-Systems                                #
# ------------------------------------------------------------------------------------------------ #
# Created    : Thursday December 8th 2022 04:07:04 pm                                              #
# Modified   : Friday December 9th 2022 08:17:05 am                                                #
# ------------------------------------------------------------------------------------------------ #
# License    : MIT License                                                                         #
# Copyright  : (c) 2022 John James                                                                 #
# ================================================================================================ #
import pandas as pd
from dependency_injector.wiring import Provide, inject

from .base import Repo
from recsys.core.dal.dao import DAO
from recsys.core.entity.datasource import DataSource
from recsys.containers import Recsys
# ------------------------------------------------------------------------------------------------ #


class DataSourceRepo(Repo):
    """Repository base class"""

    @inject
    def __init__(self, dao: DAO = Provide[Recsys.dao.datasource_dao]) -> None:
        self._dao = dao

    def __len__(self) -> int:
        return len(self._dao)

    def add(self, datasource: DataSource) -> DataSource:
        """Adds an entity to the repository and returns the DataSource with the id added."""
        dto = datasource.as_dto()
        dto = self._dao.add(dto)
        datasource = DataSource.from_dto(dto)
        return datasource

    def get(self, id: str) -> DataSource:
        "Returns an entity with the designated id"
        dto = self._dao.get(id)
        return DataSource.from_dto(dto)

    def update(self, datasource: DataSource) -> None:
        """Updates a DataSource in the databases."""
        dto = datasource.as_dto()
        self._dao.update(dto=dto)

    def remove(self, id: str) -> None:
        """Removes an entity with id from repository."""
        self._dao.delete(id)

    def exists(self, id: str) -> bool:
        """Returns True if entity with id exists in the repository."""
        return self._dao.exists(id)

    def print(self) -> None:
        """Prints the repository contents as a DataFrame."""
        sources = self._dao.get_all()
        df = pd.DataFrame.from_dict(data=sources, orient='index', columns=['id', 'name', 'description', 'publisher', 'website', 'url'])
        print(df)
