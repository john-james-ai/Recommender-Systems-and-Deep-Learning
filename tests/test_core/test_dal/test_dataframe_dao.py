#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : Recommender Systems: Towards Deep Learning State-of-the-Art                         #
# Version    : 0.1.0                                                                               #
# Python     : 3.10.6                                                                              #
# Filename   : /tests/test_core/test_dal/test_dataframe_dao.py                                     #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : https://github.com/john-james-ai/Recommender-Systems                                #
# ------------------------------------------------------------------------------------------------ #
# Created    : Wednesday December 28th 2022 02:38:04 pm                                            #
# Modified   : Sunday January 8th 2023 01:29:23 pm                                                 #
# ------------------------------------------------------------------------------------------------ #
# License    : MIT License                                                                         #
# Copyright  : (c) 2022 John James                                                                 #
# ================================================================================================ #
import inspect
from datetime import datetime
import pytest
import logging
import mysql.connector

from recsys.core.dal.dto import DTO
from recsys.core.dal.dao import DAO


# ------------------------------------------------------------------------------------------------ #
logger = logging.getLogger(__name__)
# ------------------------------------------------------------------------------------------------ #
double_line = f"\n{100 * '='}"
single_line = f"\n{100 * '-'}"


@pytest.mark.dao
@pytest.mark.dataframe_dao
class TestDataFrameDAO:  # pragma: no cover
    # ============================================================================================ #
    def reset_table(self, container):
        dba = container.dba.dataframe()
        dba.reset()

    # ---------------------------------------------------------------------------------------- #
    def get_dao(self, container) -> DAO:
        dao = container.dal.dataframe()
        return dao

    # ---------------------------------------------------------------------------------------- #
    def check_results(self, dto) -> None:
        assert dto.id is not None
        assert isinstance(dto, DTO)

    # ============================================================================================ #
    def test_setup(self, container, caplog):
        start = datetime.now()
        logger.info(
            "\n\nStarted {} {} at {} on {}".format(
                self.__class__.__name__,
                inspect.stack()[0][3],
                start.strftime("%I:%M:%S %p"),
                start.strftime("%m/%d/%Y"),
            )
        )
        logger.info(double_line)
        # ---------------------------------------------------------------------------------------- #
        self.reset_table(container)
        # ---------------------------------------------------------------------------------------- #
        end = datetime.now()
        duration = round((end - start).total_seconds(), 1)

        logger.info(
            "\nCompleted {} {} in {} seconds at {} on {}".format(
                self.__class__.__name__,
                inspect.stack()[0][3],
                duration,
                end.strftime("%I:%M:%S %p"),
                end.strftime("%m/%d/%Y"),
            )
        )
        logger.info(single_line)

    # ============================================================================================ #
    def test_create_exists(self, container, datasets, caplog):
        start = datetime.now()
        logger.info(
            "\n\nStarted {} {} at {} on {}".format(
                self.__class__.__name__,
                inspect.stack()[0][3],
                start.strftime("%I:%M:%S %p"),
                start.strftime("%m/%d/%Y"),
            )
        )
        logger.info(double_line)
        # ---------------------------------------------------------------------------------------- #
        dao = self.get_dao(container)
        dao.begin()

        for j, (name, dataframe) in enumerate(datasets[0].dataframes.items(), start=1):
            dto = dataframe.as_dto()
            dto.datasource_id = j
            dto = dao.create(dto)
            self.check_results(dto)
            logger.debug(dto)

        for i in range(1, 6):
            exists = dao.exists(i)
            logger.debug(exists)
            assert exists

        dao.rollback()

        dao.begin()

        for i in range(1, 6):
            exists = dao.exists(i)
            assert not exists
        dao.close()
        # ---------------------------------------------------------------------------------------- #
        end = datetime.now()
        duration = round((end - start).total_seconds(), 1)

        logger.info(
            "\n\tCompleted {} {} in {} seconds at {} on {}".format(
                self.__class__.__name__,
                inspect.stack()[0][3],
                duration,
                end.strftime("%I:%M:%S %p"),
                end.strftime("%m/%d/%Y"),
            )

        )
        logger.info(single_line)

    # ============================================================================================ #
    def test_create_commit(self, container, datasets, caplog):
        start = datetime.now()
        logger.info(
            "\n\nStarted {} {} at {} on {}".format(
                self.__class__.__name__,
                inspect.stack()[0][3],
                start.strftime("%I:%M:%S %p"),
                start.strftime("%m/%d/%Y"),
            )
        )
        logger.info(double_line)
        # ---------------------------------------------------------------------------------------- #
        dao = self.get_dao(container)

        for j, (name, dataframe) in enumerate(datasets[0].dataframes.items(), start=1):
            dto = dataframe.as_dto()
            dto.datasource_id = j
            dto = dao.create(dto)
            self.check_results(dto)
            logger.debug(dto)

        dao.rollback()

        for i in range(6, 11):
            assert dao.exists(i)

        # ---------------------------------------------------------------------------------------- #
        end = datetime.now()
        duration = round((end - start).total_seconds(), 1)

        logger.info(
            "\n\tCompleted {} {} in {} seconds at {} on {}".format(
                self.__class__.__name__,
                inspect.stack()[0][3],
                duration,
                end.strftime("%I:%M:%S %p"),
                end.strftime("%m/%d/%Y"),
            )
        )
        logger.info(single_line)

    # ============================================================================================ #
    def test_read(self, container, caplog):
        start = datetime.now()
        logger.info(
            "\n\nStarted {} {} at {} on {}".format(
                self.__class__.__name__,
                inspect.stack()[0][3],
                start.strftime("%I:%M:%S %p"),
                start.strftime("%m/%d/%Y"),
            )
        )
        logger.info(double_line)
        # ---------------------------------------------------------------------------------------- #
        dao = self.get_dao(container)

        for i in range(6, 11):
            dto = dao.read(i)
            assert isinstance(dto, DTO)
            self.check_results(dto)

        result = dao.read(99)
        assert result is None

        # ---------------------------------------------------------------------------------------- #
        end = datetime.now()
        duration = round((end - start).total_seconds(), 1)

        logger.info(
            "\n\tCompleted {} {} in {} seconds at {} on {}".format(
                self.__class__.__name__,
                inspect.stack()[0][3],
                duration,
                end.strftime("%I:%M:%S %p"),
                end.strftime("%m/%d/%Y"),
            )

        )
        logger.info(single_line)

    # ============================================================================================ #
    def test_read_all(self, container, caplog):
        start = datetime.now()
        logger.info(
            "\n\nStarted {} {} at {} on {}".format(
                self.__class__.__name__,
                inspect.stack()[0][3],
                start.strftime("%I:%M:%S %p"),
                start.strftime("%m/%d/%Y"),
            )
        )
        logger.info(double_line)
        # ---------------------------------------------------------------------------------------- #
        dao = self.get_dao(container)

        dtos = dao.read_all()
        assert isinstance(dtos, dict)
        for i, dto in dtos.items():
            assert dto.id == i

        # ---------------------------------------------------------------------------------------- #
        end = datetime.now()
        duration = round((end - start).total_seconds(), 1)

        logger.info(
            "\n\tCompleted {} {} in {} seconds at {} on {}".format(
                self.__class__.__name__,
                inspect.stack()[0][3],
                duration,
                end.strftime("%I:%M:%S %p"),
                end.strftime("%m/%d/%Y"),
            )

        )
        logger.info(single_line)

    # ============================================================================================ #
    def test_read_by_name_mode(self, container, caplog):
        start = datetime.now()
        logger.info(
            "\n\nStarted {} {} at {} on {}".format(
                self.__class__.__name__,
                inspect.stack()[0][3],
                start.strftime("%I:%M:%S %p"),
                start.strftime("%m/%d/%Y"),
            )
        )
        logger.info(double_line)
        # ---------------------------------------------------------------------------------------- #
        dao = self.get_dao(container)

        dto = dao.read_by_name_mode(name="dataframe_3_dataset_1", mode='test')
        assert isinstance(dto, DTO)
        self.check_results(dto)

        dto = dao.read_by_name_mode(name="dataframe_1", mode='skdi')
        assert dto is None

        # ---------------------------------------------------------------------------------------- #
        end = datetime.now()
        duration = round((end - start).total_seconds(), 1)

        logger.info(
            "\n\tCompleted {} {} in {} seconds at {} on {}".format(
                self.__class__.__name__,
                inspect.stack()[0][3],
                duration,
                end.strftime("%I:%M:%S %p"),
                end.strftime("%m/%d/%Y"),
            )

        )
        logger.info(single_line)

    # ============================================================================================ #
    def test_update(self, container, datasets, caplog):
        start = datetime.now()
        logger.info(
            "\n\nStarted {} {} at {} on {}".format(
                self.__class__.__name__,
                inspect.stack()[0][3],
                start.strftime("%I:%M:%S %p"),
                start.strftime("%m/%d/%Y"),
            )
        )
        logger.info(double_line)
        # ---------------------------------------------------------------------------------------- #
        dao = self.get_dao(container)
        dao.begin()
        dtos = dao.read_all()
        for i, dto in dtos.items():
            dto.description = "2brollback"
            dao.update(dto)

        dao.rollback()

        dtos = dao.read_all()
        for i, dto in dtos.items():
            assert not dto.description == "2brollback"

        dao.begin()
        for i, dto in dtos.items():
            dto.description = "2bsustained"
            dao.update(dto)
        dao.save()

        dtos = dao.read_all()
        for i, dto in dtos.items():
            assert dto.description == "2bsustained"
            dto.id = 8938
            with pytest.raises(mysql.connector.ProgrammingError):
                dao.update(dto)

        # ---------------------------------------------------------------------------------------- #
        end = datetime.now()
        duration = round((end - start).total_seconds(), 1)

        logger.info(
            "\n\tCompleted {} {} in {} seconds at {} on {}".format(
                self.__class__.__name__,
                inspect.stack()[0][3],
                duration,
                end.strftime("%I:%M:%S %p"),
                end.strftime("%m/%d/%Y"),
            )

        )
        logger.info(single_line)

    # ============================================================================================ #
    def test_delete(self, container, caplog):
        start = datetime.now()
        logger.info(
            "\n\nStarted {} {} at {} on {}".format(
                self.__class__.__name__,
                inspect.stack()[0][3],
                start.strftime("%I:%M:%S %p"),
                start.strftime("%m/%d/%Y"),
            )
        )
        logger.info(double_line)
        # ---------------------------------------------------------------------------------------- #
        dao = self.get_dao(container)
        dao.begin()
        dao.delete(8)
        assert not dao.exists(8)

        dao.rollback()

        assert dao.exists(8)

        with pytest.raises(mysql.connector.ProgrammingError):
            dao.delete(8743)

        # ---------------------------------------------------------------------------------------- #
        end = datetime.now()
        duration = round((end - start).total_seconds(), 1)

        logger.info(
            "\n\tCompleted {} {} in {} seconds at {} on {}".format(
                self.__class__.__name__,
                inspect.stack()[0][3],
                duration,
                end.strftime("%I:%M:%S %p"),
                end.strftime("%m/%d/%Y"),
            )

        )
        logger.info(single_line)
