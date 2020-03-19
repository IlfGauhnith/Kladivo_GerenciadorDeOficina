from datetime import date, time, datetime

from data.SQLAlchemy_data_source import SQLAlchemyDataSource
from model import Mechanic, Employee, User, Truck, Part, PartsStock, Service
from model.address import Address
from model.client import Customer, Client, Company
from model.custom_exceptions import UniqueObjectViolated, IndexUnrelatedToAnyObject
from model.utilities import AccessLevel, ClientType
from sqlalchemy.orm import with_polymorphic


class AddressDataHandler:

    __db = SQLAlchemyDataSource()
    __db_session = __db.get_session()

    @classmethod
    def create(cls, street, zip_code, province, city, complement, number):
        address = Address(street=street, zip_code=zip_code, province=province, city=city,
                          complement=complement, number=number)
        if cls.exists(address):
            raise UniqueObjectViolated

        cls.__db_session.add(address)
        cls.__db_session.commit()

    @classmethod
    def get_by_id(cls, index):
        return cls.__db_session.query(Address).filter(Address.id == index).first()

    @classmethod
    def delete_by_id(cls, index):
        cls.__db_session.query(Address).filter(Address.id == index).delete()
        cls.__db_session.commit()

    @classmethod
    def exists(cls, address):

        query = cls.__db_session.query(Address)

        for row in query:
            if row.street == address.street and row.zip_code == address.zip_code:
                if row.province == address.province and row.city == address.city:
                    if row.complement == address.complement and row.number == address.number:
                        return True

        return False

    @classmethod
    def read_all(cls):
        return cls.__db_session.query(Address).all()


class CustomerDataHandler:

    __db = SQLAlchemyDataSource()
    __db_session = __db.get_session()

    @classmethod
    def create(cls, name, cpf, email, telephone1, address_id, telephone2=None):

        # Se AddressDataHandler.get_by_id() não achar um endereço, retornará None.
        if not AddressDataHandler.get_by_id(address_id):
            raise IndexUnrelatedToAnyObject

        customer = Customer(name=name, cpf=cpf, email=email, telephone1=telephone1, telephone2=telephone2,
                            address_id=address_id)

        if cls.exists(customer):
            raise UniqueObjectViolated

        cls.__db_session.add(customer)
        cls.__db_session.commit()

    @classmethod
    def get_by_id(cls, index):
        return cls.__db_session.query(Customer).join(Client).filter(Client.id == index).first()

    @classmethod
    def delete_by_id(cls, index):
        cls.__db_session.query(Customer).join(Client).filter(Client.id == index).delete()
        cls.__db_session.commit()

    @classmethod
    def exists(cls, customer):

        query = cls.__db_session.query(Customer)

        for row in query:
            if row.cpf == customer.cpf:
                return True

        return False

    @classmethod
    def read_all(cls):
        return cls.__db_session.query(Customer).join(Client).all()


class CompanyDataHandler:

    __db = SQLAlchemyDataSource()
    __db_session = __db.get_session()

    @classmethod
    def create(cls, company_name, cnpf, email, telephone1, address_id, telephone2=None):

        # Se AddressDataHandler.get_by_id() não achar um endereço, retornará None.
        if not AddressDataHandler.get_by_id(address_id):
            raise IndexUnrelatedToAnyObject

        company = Company(company_name=company_name, cnpj=cnpf, email=email, telephone1=telephone1,
                          telephone2=telephone2, address_id=address_id)

        if cls.exists(company):
            raise UniqueObjectViolated

        cls.__db_session.add(company)
        cls.__db_session.commit()

    @classmethod
    def get_by_id(cls, index):
        return cls.__db_session.query(Company).join(Client).filter(Client.id == index).first()

    @classmethod
    def delete_by_id(cls, index):
        cls.__db_session.query(Company).join(Client).filter(Client.id == index).delete()
        cls.__db_session.commit()

    @classmethod
    def exists(cls, company):

        query = cls.__db_session.query(Company)

        for row in query:
            if row.cnpj == company.cnpj:
                return True

        return False

    @classmethod
    def read_all(cls):
        return cls.__db_session.query(Company).join(Client).all()


class MechanicDataHandler:

    __db = SQLAlchemyDataSource()
    __db_session = __db.get_session()
    __mechanic_loaded = with_polymorphic(User, [Employee, Mechanic])

    @classmethod
    def create(cls, name, photo_file_path, login, password):
        # O password já chega encriptado nesse nível.
        mechanic = Mechanic(name=name, photo_file_path=photo_file_path, login=login, password=password,
                            access_level=AccessLevel.MECHANIC)

        if cls.exists(mechanic):
            raise UniqueObjectViolated

        cls.__db_session.add(mechanic)
        cls.__db_session.commit()

    @classmethod
    def get_by_id(cls, index):
        return cls.__db_session.query(cls.__mechanic_loaded).filter(cls.__mechanic_loaded.id == index).first()

    @classmethod
    def delete_by_id(cls, index):
        cls.__db_session.query(cls.__mechanic_loaded).filter(cls.__mechanic_loaded.id == index).delete()
        cls.__db_session.commit()

    @classmethod
    def read_all(cls):
        return cls.__db_session.query(cls.__mechanic_loaded).all()

    @classmethod
    def exists(cls, mechanic):
        query = cls.__db_session.query(User).join(Employee)

        for row in query:
            if row.password == mechanic.password:
                if row.login == mechanic.login:
                    return True

        return False


class WorkshopManagerDataHandler:

    __db = SQLAlchemyDataSource()
    __db_session = __db.get_session()

    @classmethod
    def create(cls, name, photo_file_path, login, password):
        # O password já chega encriptado nesse nível.
        manager = Employee(name=name, photo_file_path=photo_file_path, login=login, password=password,
                           access_level=AccessLevel.WORKSHOP_MANAGER)

        if cls.exists(manager):
            raise UniqueObjectViolated

        cls.__db_session.add(manager)
        cls.__db_session.commit()

    @classmethod
    def get_by_id(cls, index):
        return cls.__db_session.query(User).join(Employee).filter(User.id == index).first()

    @classmethod
    def delete_by_id(cls, index):
        cls.__db_session.query(User).join(Employee).filter(User.id == index).delete()
        cls.__db_session.commit()

    @classmethod
    def read_all(cls):
        return cls.__db_session.query(User).join(Employee).all()

    @classmethod
    def exists(cls, manager):
        query = cls.__db_session.query(User).join(Employee)

        for row in query:
            if row.login == manager.login:
                if row.password == manager.password:
                    return True

        return False


class TruckDataHandler:
    __db = SQLAlchemyDataSource()
    __db_session = __db.get_session()

    @classmethod
    def create(cls, client_id, model, engine, rear_axle, license_plate, mileage, is_maintenance_plan, client_type,
               maintenance_plan_type=None):
        if client_type is ClientType.CUSTOMER:
            if not CustomerDataHandler.get_by_id(client_id):
                raise IndexUnrelatedToAnyObject

        if client_type is ClientType.COMPANY:
            if not CompanyDataHandler.get_by_id(client_id):
                raise IndexUnrelatedToAnyObject

        truck = Truck(client_id=client_id, model=model, engine=engine, rear_axle=rear_axle, license_plate=license_plate,
                      mileage=mileage, is_maintenance_plan=is_maintenance_plan,
                      maintenance_plan_type=maintenance_plan_type)

        if cls.exists(truck):
            raise UniqueObjectViolated

        cls.__db_session.add(truck)
        cls.__db_session.commit()

    @classmethod
    def get_by_id(cls, index):
        return cls.__db_session.query(Truck).filter(Truck.id == index).first()

    @classmethod
    def delete_by_id(cls, index):
        cls.__db_session.query(Truck).filter(Truck.id == index).delete()
        cls.__db_session.commit()

    @classmethod
    def read_all(cls):
        return cls.__db_session.query(Truck).all()

    @classmethod
    def exists(cls, truck):
        query = cls.__db_session.query(Truck)

        for row in query:
            if row.license_plate == truck.license_plate:
                return True

        return False

class PartDataHandler:

    __db = SQLAlchemyDataSource()
    __db_session = __db.get_session()

    @classmethod
    def create(cls, name, description, price, ean13):
        part = Part(name=name, description=description, price=price, ean13=ean13)

        if cls.exists(part):
            raise UniqueObjectViolated

        cls.__db_session.add(part)
        cls.__db_session.commit(part)

    @classmethod
    def get_by_id(cls, index):
        return cls.__db_session.query(Part).filter(Part.id == index).first()

    @classmethod
    def delete_by_id(cls, index):
        cls.__db_session.query(Part).filter(Part.id == index).delete()
        cls.__db_session.commit()

    @classmethod
    def exists(cls, part):
        query = cls.__db_session.query(Part)

        for row in query:
            if row.ean13 == part.ean13:
                return True

        return False

    @classmethod
    def read_all(cls):
        return cls.__db_session.query(Part).all()

class PartsStockDataHandler:

    __db = SQLAlchemyDataSource()
    __db_session = __db.get_session()

    @classmethod
    def create(cls, part_id, quantity):
        part = PartDataHandler.get_by_id(part_id)

        if not part:
            raise IndexUnrelatedToAnyObject

        stock = PartsStock(part_id=part_id, quantity=quantity)

        if cls.exists(stock):
            raise UniqueObjectViolated

        cls.__db_session.add(stock)
        cls.__db_session.commit()

    @classmethod
    def get_by_id(cls, index):
        return cls.__db_session.query(PartsStock).filter(PartsStock.id == index).first()

    @classmethod
    def get_by_part_id(cls, part_id):
        return cls.__db_session.query(PartsStock).filter(PartsStock.part_id == part_id).first()

    @classmethod
    def delete_by_id(cls, index):
        cls.__db_session.query(PartsStock).filter(PartsStock.id == index).delete()
        cls.__db_session.commit()

    @classmethod
    def delete_by_part_id(cls, part_id):
        cls.__db_session.query(PartsStock).filter(PartsStock.part_id == part_id).delete()
        cls.__db_session.commit()

    @classmethod
    def exists(cls, stock):
        query = cls.__db_session.query(PartsStock)

        for row in query:
            if row.part_id == stock.part_id:
                return True

        return False

    @classmethod
    def read_all(cls):
        return cls.__db_session.query(PartsStock).all()

class ServiceDataHandler:

    __db = SQLAlchemyDataSource()
    __db_session = __db.get_session()

    @classmethod
    def create(cls, mechanic_id, delivery_prevision_date, delivery_prevision_hour, effective_delivered_date,
               effective_delivered_hour, service_description, total_charge, payment_type):

        mechanic = MechanicDataHandler.get_by_id(mechanic_id)

        if not mechanic:
            raise IndexUnrelatedToAnyObject

        service = Service(mechanic_id=mechanic_id, entry_date=date.today(), entry_time=datetime.now().time(),
                          delivery_prevision_date=delivery_prevision_date, delivery_prevision_hour=delivery_prevision_hour,
                          effective_delivered_date=effective_delivered_date, effective_delivered_hour=effective_delivered_hour,
                          service_description=service_description, total_charge=total_charge, payment_type=payment_type)

        if cls.exists(service):
            raise UniqueObjectViolated

        cls.__db_session.add(service)
        cls.__db_session.commit()

    @classmethod
    def get_by_id(cls, index):
        return cls.__db_session.query(Service).filter(Service.id == index).first()

    @classmethod
    def delete_by_id(cls, index):
        cls.__db_session.query(Service).filter(Service.id == index).delete()
        cls.__db_session.commit()

    @classmethod
    def exists(cls, service):
        query = cls.__db_session.query(Service)

        for row in query:
            if row.entry_date is service.entry_date:
                if row.entry_time is service.entry_time:
                    return True

        return False

    @classmethod
    def read_all(cls):
        return cls.__db_session.query(Service).all()