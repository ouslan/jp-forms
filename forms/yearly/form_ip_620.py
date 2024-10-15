from sqlmodel import SQLModel, Field
from typing import Optional

class IP620Validator(SQLModel, table=True):
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
    patients_service_revenue_from_persons_1: float
    patients_service_revenue_from_persons_2: float
    patients_service_revenue_from_industries_business_1: float
    patients_service_revenue_from_industries_business_2: float
    contractual_adjustments_1: float
    contractual_adjustments_2: float
    net_patient_service_revenue_1: float
    net_patient_service_revenue_2: float
    other_incomes_1: float
    other_incomes_2: float
    other_incomes_rent_1: float
    other_incomes_rent_2: float
    other_incomes_interest_1: float
    other_incomes_interest_2: float
    other_incomes_capital_gain_loss_1: float
    other_incomes_capital_gain_loss_2: float
    other_incomes_operating_1: float
    other_incomes_operating_2: float
    total_incomes_1: float
    total_incomes_2: float
    total_expenses_1: float
    total_expenses_2: float
    expenses_salaries_wages_bonus_1: float
    expenses_salaries_wages_bonus_2: float
    expenses_interest_1: float
    expenses_interest_2: float
    expenses_rent_1: float
    expenses_rent_2: float
    expenses_food_patients_1: float
    expenses_food_patients_2: float
    expenses_free_food_to_employees_1: float
    expenses_free_food_to_employees_2: float
    expenses_uniforms_1: float
    expenses_uniforms_2: float
    expenses_depreciation_1: float
    expenses_depreciation_2: float
    expenses_bad_debts_1: float
    expenses_bad_debts_2: float
    expenses_donations_1: float
    expenses_donations_2: float
    expenses_sales_tax_1: float
    expenses_sales_tax_2: float
    expenses_machinery_1: float
    expenses_machinery_2: float
    expenses_on_other_purchases_1: float
    expenses_on_other_purchases_2: float
    expenses_licenses_1: float
    expenses_licenses_2: float
    expenses_other_operating_1: float
    expenses_other_operating_2: float
    net_profit_loss_1: float
    net_profit_loss_2: float
    net_profit_loss_income_tax_1: float
    net_profit_loss_income_tax_2: float
    net_profit_after_tax_1: float
    net_profit_after_tax_2: float
    sales_and_use_withheld_1: float
    sales_and_use_withheld_2: float
    name: str
    rank: str
