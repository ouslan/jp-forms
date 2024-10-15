from sqlmodel import Field, SQLModel
from typing import Optional

class IP210Validator(SQLModel, table=True):
    """
    Schema for IP-210 form

    Parameters:
    -----------
    **args: Arguments given by the form

    Returns:
    --------
    None
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
    closing_date: str
    start_year: int
    end_year: int
    incomes_services_revenues_1: float
    incomes_services_revenues_2: float
    incomes_industries_1: float
    incomes_industries_2: float
    incomes_persons_1: float
    incomes_persons_2: float
    incomes_sale_merchandise_1: float
    incomes_sale_merchandise_2: float
    incomes_rents_1: float
    incomes_rents_2: float
    incomes_interests_1: float
    incomes_interests_2: float
    incomes_capital_gain_loss_1: float
    incomes_capital_gain_loss_2: float
    others_incomes_1: float
    others_incomes_2: float
    total_income_1: float
    total_income_2: float
    expenses_1: float
    expenses_2: float
    expenses_salaries_wages_bonus_1: float
    expenses_salaries_wages_bonus_2: float
    expenses_interests_1: float
    expenses_interests_2: float
    expenses_rents_1: float
    expenses_rents_2: float
    expenses_depreciation_1: float
    expenses_depreciation_2: float
    expenses_bad_debts_1: float
    expenses_bad_debts_2: float
    expenses_donation_1: float
    expenses_donation_2: float
    expenses_sales_tax_1: float
    expenses_sales_tax_2: float
    expenses_machinery_1: float
    expenses_machinery_2: float
    other_purchases_1: float
    other_purchases_2: float
    licenses_1: float
    licenses_2: float
    other_expenses_1: float
    other_expenses_2: float
    total_expenses_1: float
    total_expenses_2: float
    net_profit_1: float
    net_profit_2: float
    net_profit_income_tax_1: float
    net_profit_income_tax_2: float
    profit_after_tax_1: float
    profit_after_tax_2: float
    withheld_tax_1: float
    withheld_tax_2: float
    signature: str
    rank: str
