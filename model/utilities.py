from enum import Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class MaintenancePlanTypes(Enum):
    BLUE_PLAN = 'BLUE_PLAN'
    GOLD_PLAN = 'GOLD_PLAN'


class AccessLevel(Enum):
    MECHANIC = 'MECHANIC'
    WORKSHOP_MANAGER = 'WORKSHOP_MANAGER'
    SYSTEM_ADMIN = 'SYSTEM_ADMIN'


class PaymentType(Enum):
    MAINTENANCEPLAN = 'MAINTENANCEPLAN'
    CASH = 'CASH'
    CREDITCARD = 'CREDITCARD'
    DEBITCARD = 'DEBITCARD'

class ClientType(Enum):
    CUSTOMER = 'CUSTOMER'
    COMPANY = 'COMPANY'