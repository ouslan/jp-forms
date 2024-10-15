from sqlmodel import Field, SQLModel
from typing import Optional

class IP540Validator(SQLModel, table=True):
    """
    Schema for IP-540 Validator form
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    company_name: str
    address: str
    email: str
    liaison_officer: str
    ssn: str
    tel: str
    fax: str
    legal_form: str
    cfc: str
    business_type: str
    business_function: str
    branches: str
    branches_yes: str
    closing_date: str
    start_year: int
    end_year: int

    incomes_services_rendered_1: float
    incomes_services_rendered_2: float
    incomes_from_persons_1: float
    incomes_from_persons_2: float
    incomes_from_industries_and_businesses_1: float
    incomes_from_industries_and_businesses_2: float
    incomes_sale_merchandise_1: float
    incomes_sale_merchandise_2: float
    incomes_rent_machinery_and_equipment_1: float
    incomes_rent_machinery_and_equipment_2: float
    incomes_rent_land_and_building_1: float
    incomes_rent_land_and_building_2: float
    incomes_interests_1: float
    incomes_interests_2: float
    incomes_capital_gain_or_loss_1: float
    incomes_capital_gain_or_loss_2: float
    incomes_other_operating_income_1: float
    incomes_other_operating_income_2: float

    expenses_salaries_wages_bonus_1: float
    expenses_salaries_wages_bonus_2: float
    expenses_interests_1: float
    expenses_interests_2: float
    expenses_rent_1: float
    expenses_rent_2: float
    expenses_depreciation_1: float
    expenses_depreciation_2: float
    expenses_bad_debts_1: float
    expenses_bad_debts_2: float
    expenses_donations_1: float
    expenses_donations_2: float
    expenses_other_donations_1: float
    expenses_other_donations_2: float
    expenses_sales_taxes_1: float
    expenses_sales_taxes_2: float
    expenses_purchases_machinery_1: float
    expenses_purchases_machinery_2: float
    expenses_other_purchases_1: float
    expenses_other_purchases_2: float
    expenses_licenses_1: float
    expenses_licenses_2: float

    net_profit_1: float
    net_profit_2: float
    profit_income_tax_1: float
    profit_income_tax_2: float
    profit_after_income_tax_1: float
    profit_after_income_tax_2: float
    sales_tax_withheld_1: float
    sales_tax_withheld_2: float

    name: str
    rank: str
