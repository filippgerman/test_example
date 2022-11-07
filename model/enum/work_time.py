from enum import Enum


class WorkTimeEnum(str, Enum):
    morning = '10:00-13:00'
    afternoon = '13:00-16:00'
    evning = '16:00-19:00'
