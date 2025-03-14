# Задание 1. Логирование с использованием нескольких файлов
# напишите скрипт, который логирует разные типы сообщений в разные файлы.
# Логи уровня DEBUG и INFO должны сохраняться в debug_info.log, а логи уровня
# WARNING и выше — в warnings_errors.log.

import logging


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(message)s')

debug_info = logging.FileHandler('task_1_debug_info.log', encoding='utf8')
debug_info.setLevel(logging.DEBUG)
debug_info.setFormatter(formatter)
logger.addHandler(debug_info)

warnings_errors_handler = logging.FileHandler('task_1_warnings_errors.log', encoding='utf8')
warnings_errors_handler.setLevel(logging.WARNING)
warnings_errors_handler.setFormatter(formatter)
logger.addHandler(warnings_errors_handler)

logger.debug('В этот файл попадают все логи с уровнем DEBUG')
logger.info('В этот файл попадают все логи с уровнем INFO')
logger.warning('В этот файл попадают все логи с уровнем WARNING')
logger.error('В этот файл попадают все логи с уровнем ERROR')
logger.critical('В этот файл попадают все логи с уровнем CRITICAL')