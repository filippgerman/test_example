from model.enum.work_time import WorkTimeEnum
from pydantic import BaseModel


class ReceivingTime(BaseModel):
    receiving_time: WorkTimeEnum
