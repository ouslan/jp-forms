from pydantic import BaseModel
from ..dao.db import DAO
import polars as pl

class IP210Validator(BaseModel):
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
    busines_function: str
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
    income_interests_1: float
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
    expenses_donation_2; float
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

def IP_210(request):
    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get("company_name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        liaison_officer = request.POST.get("liaison_officer")
        ssn = request.POST.get("ssn")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")
        legal_form = request.POST.get("legal_form")
        cfc = request.POST.get("cfc")
        business_type = request.POST.get("business_type")
        business_function = request.POST.get("business_function")
        branches = request.POST.get("branches")
        closing_date = request.POST.get("closing_date")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")
        income_operations_12 = request.POST.get("income_operations_12")
        income_operations_13 = request.POST.get("income_operations_13")
        income_interests_12 = request.POST.get("income_interests_12")
        income_interests_13 = request.POST.get("income_interests_13")
        incomes_rents_12 = request.POST.get("incomes_rents_12")
        incomes_rents_13 = request.POST.get("incomes_rents_13")
        income_rent_land_12 = request.POST.get("income_rent_land_12")
        income_rent_land_13 = request.POST.get("income_rent_land_13")
        other_income_12 = request.POST.get("other_income_12")
        other_income_13 = request.POST.get("other_income_13")
        total_incomes_12 = request.POST.get("total_incomes_12")
        total_incomes_13 = request.POST.get("total_incomes_13")
        total_income_12 = request.POST.get("total_income_12")
        total_income_13 = request.POST.get("total_income_13")

        salaries_2012 = request.POST.get("salaries_2012")
        salaries_2013 = request.POST.get("salaries_2013")
        expenses_interests_12 = request.POST.get("expenses_interests_12")
        expenses_interests_13 = request.POST.get("expenses_interests_13")
        depreciation_12 = request.POST.get("depreciation_12")
        depreciation_13 = request.POST.get("depreciation_13")
        expenses_rent_12 = request.POST.get("expenses_rent_12")
        expenses_rent_13 = request.POST.get("expenses_rent_13")
        bad_debts_12 = request.POST.get("bad_debts_12")
        bad_debts_13 = request.POST.get("bad_debts_13")
        donations_12 = request.POST.get("donations_12")
        donations_13 = request.POST.get("donations_13")
        sales_tax_12 = request.POST.get("sales_tax_12")
        sales_tax_13 = request.POST.get("sales_tax_13")
        machinery_12 = request.POST.get("machinery_12")
        machinery_13 = request.POST.get("machinery_13")
        other_purchases_12 = request.POST.get("other_purchases_12")
        other_purchases_13 = request.POST.get("other_purchases_13")
        licenses_12 = request.POST.get("licenses_12")
        licenses_13 = request.POST.get("licenses_13")
        other_expenses_12 = request.POST.get("other_expenses_12")
        other_expenses_13 = request.POST.get("other_expenses_13")
        total_expenses_12 = request.POST.get("total_expenses_12")
        total_expenses_13 = request.POST.get("total_expenses_13")
        net_profit_12 = request.POST.get("net_profit_12")
        net_profit_13 = request.POST.get("net_profit_13")
        income_tax_12 = request.POST.get("income_tax_12")
        income_tax_13 = request.POST.get("income_tax_13")
        profit_after_tax_12 = request.POST.get("profit_after_tax_12")
        profit_after_tax_13 = request.POST.get("profit_after_tax_13")
        withheld_tax_12 = request.POST.get("withheld_tax_12")
        withheld_tax_13 = request.POST.get("withheld_tax_13")
        signature = request.POST.get("signature")
        rank = request.POST.get("rank")

        data = [
            pl.Series("company_name", [company_name], dtype=pl.String),
            pl.Series("address", [address], dtype=pl.String),
            pl.Series("email", [email], dtype=pl.String),
            pl.Series("liaison_officer", [liaison_officer], dtype=pl.String),   
            pl.Series("ssn", [ssn], dtype=pl.String),
            pl.Series("tel", [tel], dtype=pl.String),
            pl.Series("fax", [fax], dtype=pl.String),
            pl.Series("legal_form", [legal_form], dtype=pl.String),
            pl.Series("cfc", [cfc], dtype=pl.String),
            pl.Series("business_type", [business_type], dtype=pl.String),
            pl.Series("business_function", [business_function], dtype=pl.String),
            pl.Series("branches", [branches], dtype=pl.String),
            pl.Series("closing_date", [closing_date], dtype=pl.String),
            pl.Series("start_year", [start_year], dtype=pl.String),
            pl.Series("end_year", [end_year], dtype=pl.String),
            pl.Series("income_operations_12", [float(income_operations_12)], dtype=pl.Float64),
            pl.Series("income_operations_13", [float(income_operations_13)], dtype=pl.Float64),
            pl.Series("income_interests_12", [float(income_interests_12)], dtype=pl.Float64),
            pl.Series("income_interests_13", [float(income_interests_13)], dtype=pl.Float64),
            pl.Series("incomes_rents_12", [float(incomes_rents_12)], dtype=pl.Float64),
            pl.Series("incomes_rents_13", [float(incomes_rents_13)], dtype=pl.Float64),
            pl.Series("income_rent_land_12", [float(income_rent_land_12)], dtype=pl.Float64),
            pl.Series("income_rent_land_13", [float(income_rent_land_13)], dtype=pl.Float64),
            pl.Series("other_income_12", [float(other_income_12)], dtype=pl.Float64),
            pl.Series("other_income_13", [float(other_income_13)], dtype=pl.Float64),
            pl.Series("total_incomes_12", [float(total_incomes_12)], dtype=pl.Float64),
            pl.Series("total_incomes_13", [float(total_incomes_13)], dtype=pl.Float64),
            pl.Series("total_income_12", [float(total_income_12)], dtype=pl.Float64),
            pl.Series("total_income_13", [float(total_income_13)], dtype=pl.Float64),
            pl.Series("salaries_2012", [float(salaries_2012)], dtype=pl.Float64),
            pl.Series("salaries_2013", [float(salaries_2013)], dtype=pl.Float64),
            pl.Series("expenses_interests_12", [float(expenses_interests_12)], dtype=pl.Float64),
            pl.Series("expenses_interests_13", [float(expenses_interests_13)], dtype=pl.Float64),
            pl.Series("depreciation_12", [float(depreciation_12)], dtype=pl.Float64),
            pl.Series("depreciation_13", [float(depreciation_13)], dtype=pl.Float64),
            pl.Series("expenses_rent_12", [float(expenses_rent_12)], dtype=pl.Float64),
            pl.Series("expenses_rent_13", [float(expenses_rent_13)], dtype=pl.Float64),
            pl.Series("bad_debts_12", [float(bad_debts_12)], dtype=pl.Float64),
            pl.Series("bad_debts_13", [float(bad_debts_13)], dtype=pl.Float64),
            pl.Series("donations_12", [float(donations_12)], dtype=pl.Float64),
            pl.Series("donations_13", [float(donations_13)], dtype=pl.Float64),
            pl.Series("sales_tax_12", [float(sales_tax_12)], dtype=pl.Float64),
            pl.Series("sales_tax_13", [float(sales_tax_13)], dtype=pl.Float64),
            pl.Series("machinery_12", [float(machinery_12)], dtype=pl.Float64),
            pl.Series("machinery_13", [float(machinery_13)], dtype=pl.Float64),
            pl.Series("other_purchases_12", [float(other_purchases_12)], dtype=pl.Float64),
            pl.Series("other_purchases_13", [float(other_purchases_13)], dtype=pl.Float64),
            pl.Series("licenses_12", [float(licenses_12)], dtype=pl.Float64),
            pl.Series("licenses_13", [float(licenses_13)], dtype=pl.Float64),
            pl.Series("other_expenses_12", [float(other_expenses_12)], dtype=pl.Float64),
            pl.Series("other_expenses_13", [float(other_expenses_13)], dtype=pl.Float64),
            pl.Series("total_expenses_12", [float(total_expenses_12)], dtype=pl.Float64),
            pl.Series("total_expenses_13", [float(total_expenses_13)], dtype=pl.Float64),
            pl.Series("net_profit_12", [float(net_profit_12)], dtype=pl.Float64),
            pl.Series("net_profit_13", [float(net_profit_13)], dtype=pl.Float64),
            pl.Series("income_tax_12", [float(income_tax_12)], dtype=pl.Float64),
            pl.Series("income_tax_13", [float(income_tax_13)], dtype=pl.Float64),
            pl.Series("profit_after_tax_12", [float(profit_after_tax_12)], dtype=pl.Float64),
            pl.Series("profit_after_tax_13", [float(profit_after_tax_13)], dtype=pl.Float64),
            pl.Series("withheld_tax_12", [float(withheld_tax_12)], dtype=pl.Float64),
            pl.Series("withheld_tax_13", [float(withheld_tax_13)], dtype=pl.Float64),
            pl.Series("signature", [signature], dtype=pl.String),
            pl.Series("rank", [rank], dtype=pl.String)
        ]
        
        df = pl.DataFrame(data)
        DAO().insert_forms(df, "IP_210", 13)
        
        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-210.html")
