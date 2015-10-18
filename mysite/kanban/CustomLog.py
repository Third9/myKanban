# -*- coding: utf-8 -*-

__author__ = 'KwonH'
__date__ = '2015.05.06'

import logging
import logging.handlers

class CustomLog() :
	def __init__(self, logger_name) :		
		self.logger = logging.getLogger(logger_name)

		# create formatter
		file_fomatter = logging.Formatter('[%(levelname)s | %(module)s/%(funcName)s] %(asctime)s \n >> %(message)s')
		stream_fomatter = logging.Formatter('[%(levelname)s | %(filename)s:%(lineno)s] %(asctime)s \n >> %(message)s')

		stream_handler = logging.StreamHandler()
		# stream_handler.setLevel(logging.DEBUG)
		file_handler = logging.FileHandler('./{logger_name}.log'.format(logger_name=logger_name))
		# file_handler.setLevel(logging.INFO)

		# Formatter Setting
		stream_handler.setFormatter(stream_fomatter)
		file_handler.setFormatter(file_fomatter)
		

		# 로거 인스턴스에 스트림 핸들러와 파일핸들러를 붙인다.
		self.logger.addHandler(stream_handler)
		self.logger.addHandler(file_handler)
		

		# 로거 인스턴스로 로그를 찍는다.
		self.logger.setLevel(logging.DEBUG)

	def _get_logger(self) :
		return self.logger
