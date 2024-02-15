from collections import OrderedDict
import random
from dammy.core import BaseGenerator
from mimesis import Address
from faker import Faker

fake = Faker()
Faker.seed(0)


class RandomAddress(BaseGenerator):
    def __init__(self):
        super(RandomAddress, self).__init__('VARCHAR(1024)')

    def generate_raw(self, dataset=None):
        # return random_address.random_address.real_random_address()
        return Address()


class SystemUniqueKey(BaseGenerator):
    def __init__(self):
        super(SystemUniqueKey, self).__init__('VARCHAR(36)')

    def generate_raw(self, dataset=None):
        return fake.ean(length=13)


class RandomInt(BaseGenerator):
    def __init__(self, lb, ub):
        super(RandomInt, self).__init__('BIGINT')
        self.lb = lb
        self.ub = ub

    def generate_raw(self, dataset=None):
        return fake.random_int(self.lb, self.ub)


class CompanyName(BaseGenerator):
    def __init__(self):
        super(CompanyName, self).__init__('VARCHAR(255)')

    def generate_raw(self, dataset=None):
        return fake.company()


class CountryName(BaseGenerator):
    def __init__(self):
        super(CountryName, self).__init__('VARCHAR(255)')

    def generate_raw(self, dataset=None):
        return fake.country()


class UserName(BaseGenerator):
    def __init__(self):
        super(UserName, self).__init__('VARCHAR(255)')

    def generate_raw(self, dataset=None):
        return fake.user_name()


class DateBetween(BaseGenerator):
    def __init__(self, lb, ub):
        super(DateBetween, self).__init__('BIGINT')
        self.lb = lb
        self.ub = ub

    def generate_raw(self, dataset=None):
        return str(fake.date_between(self.lb, self.ub))


class RandomAlphaNumeric(BaseGenerator):
    def __init__(self):
        super(RandomAlphaNumeric, self).__init__('VARCHAR(255)')

    def generate_raw(self, dataset=None):
        r = random.random()

        def alphaPlace(num):
            if (num <= 0.1):
                return fake.bothify('????-##?######')
            elif (num > 0.1 and num <= 0.2):
                return fake.bothify('##-????-#######')
            elif (num > 0.2 and num <= 0.3):
                return fake.bothify('??????#?#?-####')
            elif (num > 0.3 and num <= 0.4):
                return fake.bothify('####-##-##-??-####')
            elif (num > 0.4 and num <= 0.5):
                return fake.bothify('???-####-##-##-####')
            elif (num > 0.5 and num <= 0.6):
                return fake.bothify('00####-####')
            elif (num > 0.6 and num <= 0.7):
                return fake.bothify('49#####-??')
            else:
                return fake.bothify('??###-???####')

        return alphaPlace(r)


class PaymentMethodWithPct(BaseGenerator):
    def __init__(self):
        super(PaymentMethodWithPct, self).__init__('VARCHAR(255)')

    def generate_raw(self, dataset=None):
        return fake.random_element(
            elements=OrderedDict([
                # Generates "ACH" 42% of the time
                ("ACH", 0.42),
                ("Automated Clearing House", 0.2),
                ("CHK", 0.2),
                ("GE", 0.05),
                ("Giro - EFT", 0.02),
                ("System Check", 0.01),
                ("Wire Transfer", 0.01),
                ("IMPS", 0.01),
                ("NEFT", 0.01),
                ("UPI", 0.01),
                ("RTGS", 0.01),
                ("OTHER", 0.01),
                ("", 0.02),
            ])
        )


class PaymentMethod(BaseGenerator):
    def __init__(self):
        super(PaymentMethod, self).__init__('VARCHAR(255)')

    def generate_raw(self, dataset=None):
        return fake.random_element(
            elements=(
                "ACH",
                "Automated Clearing House",
                "CHK",
                "GE",
                "Giro - EFT",
                "System Check",
                "Wire Transfer",
                "IMPS",
                "NEFT",
                "UPI",
                "RTGS",
                "OTHER",
                ""
            )
        )


class PaymentStatusWithPct(BaseGenerator):
    def __init__(self):
        super(PaymentStatusWithPct, self).__init__('VARCHAR(255)')

    def generate_raw(self, dataset=None):
        return fake.random_element(
            elements=OrderedDict([
                ("Paid-Reconciled", 0.59),
                ("Paid-Unreconciled", 0.2),
                ("UnPaid-Reconciled", 0.17),
                ("UnPaid-Uneeconciled", 0.03),
                ("", 0.01)
            ])
        )


class PaymentStatus(BaseGenerator):
    def __init__(self):
        super(PaymentStatus, self).__init__('VARCHAR(255)')

    def generate_raw(self, dataset=None):
        return fake.random_element(
            elements=(
                "Paid-Reconciled",
                "Paid-Unreconciled",
                "UnPaid-Reconciled",
                "UnPaid-Uneeconciled",
                ""
            )
        )


class VendorTypeWithPct(BaseGenerator):
    def __init__(self):
        super(VendorTypeWithPct, self).__init__('VARCHAR(255)')

    def generate_raw(self, dataset=None):
        return fake.random_element(
            elements=OrderedDict([
                ('Finance Company', 0.05),
                ('Govt Agency', 0.025),
                ('Insurance', 0.001),
                ('Office Supplies', 0.2),
                ('Outside Services', 0.01),
                ('Parts Supplier', 0.35),
                ('Professional Services', 0.1),
                ('Sales Tax Agency', 0.01),
                ('Service Provider', 0.2),
                ('Sub Contractor', 0.2),
                ('Unknown', 0.001),
                ('Utilities', 0.05),
                ('Employee', 0.05)
            ])
        )


class VendorType(BaseGenerator):
    def __init__(self):
        super(VendorType, self).__init__('VARCHAR(255)')

    def generate_raw(self, dataset=None):
        return fake.random_element(
            elements=(
                'Finance Company',
                'Govt Agency',
                'Insurance',
                'Office Supplies',
                'Outside Services',
                'Parts Supplier',
                'Professional Services',
                'Sales Tax Agency',
                'Service Provider',
                'Sub Contractor',
                'Unknown',
                'Utilities',
                'Employee'
            )
        )


class PaymentTypeWithPct(BaseGenerator):
    def __init__(self):
        super(PaymentTypeWithPct, self).__init__('VARCHAR(255)')

    def generate_raw(self, dataset=None):
        return fake.random_element(
            elements=OrderedDict([
                ("Partial", 0.05),
                ("Final",  0.8),
                ("Additional", 0.01),
                ("Down Payment", 0.01),
                ("Deferred", 0.2),
            ])
        )


class PaymentType(BaseGenerator):
    def __init__(self):
        super(PaymentType, self).__init__('VARCHAR(255)')

    def generate_raw(self, dataset=None):
        return fake.random_element(
            elements=(
                "Partial",
                "Final",
                "Additional",
                "Down Payment",
                "Deferred"
            )
        )


class BankAccountTypeWithPct(BaseGenerator):
    def __init__(self):
        super(BankAccountTypeWithPct, self).__init__('VARCHAR(255)')

    def generate_raw(self, dataset=None):
        return fake.random_element(
            elements=OrderedDict([
                ("Savings Account", 0.3),
                ("Current Account", 0.60),
                ("Recurring Deposit Account", 0.01),
                ("Fixed Deposit Account", 0.01),
                ("DEMAT Account", 0.01),
                ("Non-Resident Account", 0.01),
                ("Foreign Account", 0.01),
                ("Other", 0.01)
            ])
        )


class BankAccountType(BaseGenerator):
    def __init__(self):
        super(BankAccountType, self).__init__('VARCHAR(255)')

    def generate_raw(self, dataset=None):
        return fake.random_element(
            elements=(
                "Savings Account",
                "Current Account",
                "Recurring Deposit Account",
                "Fixed Deposit Account",
                "DEMAT Account",
                "Non-Resident Account",
                "Foreign Account",
                "Other"
            )
        )


class DigitalContact(BaseGenerator):
    def __init__(self):
        super(DigitalContact, self).__init__('VARCHAR(255)')

    def generate_raw(self, dataset=None):
        website = str(fake.profile()['website'])
        return fake.random_element(
            elements=OrderedDict([
                (fake.phone_number(), 0.85),
                (fake.phone_number(), 0.14),
                (website, 0.01)
            ])
        )


class DistributorCategoryWithPct(BaseGenerator):
    def __init__(self):
        super(DistributorCategoryWithPct, self).__init__('VARCHAR(255)')

    def generate_raw(self, dataset=None):
        return fake.random_element(
            elements=OrderedDict([
                ("Channel-Partner", 0.59),
                ("Retailer", 0.2),
                ("Urban-Distributor", 0.17),
                ("Rural-Distributor", 0.03),
                ("", 0.01)
            ])
        )


class DistributorType(BaseGenerator):
    def __init__(self):
        super(DistributorType, self).__init__('VARCHAR(255)')

    def generate_raw(self, dataset=None):
        return fake.random_element(
            elements=(
                "Direct",
                "Indirect",
                "Exclusive",
                "Intensive",
                "Selective",
                "Dual",
                "Reverse"
            )
        )


class EmployeeType(BaseGenerator):
    def __init__(self):
        super(EmployeeType, self).__init__('VARCHAR(255)')

    def generate_raw(self, dataset=None):
        return fake.random_element(
            elements=OrderedDict([
                ('Regular', 0.75),
                ('Contract', 0.20),
                ('Independent Contractor', 1.5),
                ('On-Call', 0.02),
                ('Volunteer', 0.01),
                ('Temporary', 0.03)
            ])
        )


class EmployeeCategory(BaseGenerator):
    def __init__(self):
        super(EmployeeCategory, self).__init__('VARCHAR(255)')

    def generate_raw(self, dataset=None):
        return fake.random_element(
            elements=OrderedDict([
                ('Fulltime', 0.75),
                ('Parttime', 0.20)
            ])
        )


class MaritalStatus(BaseGenerator):
    def __init__(self):
        super(MaritalStatus, self).__init__('VARCHAR(255)')

    def generate_raw(self, dataset=None):
        return fake.random_element(
            elements=OrderedDict([
                ('Married', 0.60),
                ('Single', 0.35),
                ('Divorced', 0.05),
                ('Widowed', 0.01),
            ])
        )


class PayScale(BaseGenerator):
    def __init__(self):
        super(PayScale, self).__init__('VARCHAR(255)')

    def generate_raw(self, dataset=None):
        return fake.random_element(
            elements=OrderedDict([
                ('Grade-1', 0.10),
                ('Grade-2', 0.20),
                ('Grade-3', 0.25),
                ('Grade-4', 0.30),
                ('Grade-5', 0.10),
                ('Grade-6', 0.04),
                ('Grade-7', 0.01),
            ])
        )


class Department(BaseGenerator):
    def __init__(self):
        super(Department, self).__init__('VARCHAR(255)')

    def generate_raw(self, dataset=None):
        return fake.random_element(
            elements=OrderedDict([
                ('Sales', 0.13),
                ('IT', 0.15),
                ('R&D', 0.14),
                ('Admin', 0.13),
                ('Marketing', 0.11),
                ('Accounting', 0.10),
                ('Finance', 0.10),
                ('HR', 0.09),
                ('Customer Support', 0.05),
            ])
        )


class StoreType(BaseGenerator):
    def __init__(self):
        super(StoreType, self).__init__('VARCHAR(255)')

    def generate_raw(self, dataset=None):
        return fake.random_element(
            elements=(
                'Single-location Retail',
                'Chain Stores',
                'Franchise',
                'Department Store',
                'Grocery Store',
                'Super/Hyper Market',
                'Discount Retailer',
                'Outlet Retailer',
                'Warehouse Store',
                'Convenience Store',
                'Internet Retailer',
                'Mom and Pop',
                'Speciality Store',
                'Direct Marketing ',
                'Automatic Vending Machine'
            )
        )


class StoreCategory(BaseGenerator):
    def __init__(self):
        super(StoreCategory, self).__init__('VARCHAR(255)')

    def generate_raw(self, dataset=None):
        return fake.random_element(
            elements=(
                "Furniture Stores",
                "Home Furnishings Stores",
                "Automotive Dealers",
                "Electronics & Appliance Stores",
                "Building Material & Supplies Dealers",
                "Lawn & Garden Equipment and Supplies Stores",
                "Grocery Stores",
                "Specialty Food Stores",
                "Beer, Wine & Liquor Stores",
                "Health & Personal Care Stores",
                "Gasoline Stations",
                "Clothing Stores",
                "Shoe Stores",
                "Jewelry, Luggage & Leather Goods Stores",
                "Sporting Goods, Hobby & Musical Instrument Stores",
                "Book Stores & News Dealers",
                "Department Stores",
                "General Merchandise Stores",
                "Florists",
                "Office Supplies, Stationery & Gift Stores",
                "Used Merchandise Stores",
                "Other Miscellaneous Store Retailers"
            )
        )


class CustomerProfile(BaseGenerator):
    def __init__(self):
        super(CustomerProfile, self).__init__('VARCHAR(255)')

    def generate_raw(self, dataset=None):
        return fake.random_element(
            elements=(
                "Bargain Hunter",
                "Browser",
                "Showroomer",
                "Impulse Buyer",
                "Mission Driven",
                "Indecisive Patron",
                "Educated Consumer",
                "Loyal Customer",
                "Wanderer",
                "Gift Giver"
            )
        )
