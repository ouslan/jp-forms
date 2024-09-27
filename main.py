from forms.yearly.form_ip_110 import IP_110FormView, IP110Validator

def main() -> None:

    external_data = {
        "company_name": "John Doe1",
        "address": "123 Main Street",
        "email": "name@test.com",
        "liaison_officer": "John Doe2",
        "ssn": "123456789",
        "tel": "123456789",
        "fax": "123456789",
        "legal_form": "John Doe3",
        "cfc": "John Doe4",
        "business_type": "John Doe5",
        "business_function": "John Doe6",
        "branches": "John Doe7",
        "closing_date": "John Doe8",
        "start_year": 2021,
        "end_year": 2023,
        "incomes_services_revenues_1": 1.0,
        "incomes_services_revenues_2": 1.0,
        "incomes_industries_1": 1.0,
        "incomes_industries_2": 1.0,
        "incomes_persons_1": 1.0,
        "incomes_persons_2": 1.0,
        "incomes_sale_merchandise_1": 1.0,
        "incomes_sale_merchandise_2": 1.0,
        "incomes_rents_1": 1.0,
        "incomes_rents_2": 1.0,
        "incomes_interests_1": 1.0,
        "incomes_interests_2": 1.0,
        "incomes_capital_gain_loss_1": 1.0,
        "incomes_capital_gain_loss_2": 1.0,
        "others_incomes_1": 1.0,
        "others_incomes_2": 1.0,
        "total_income_1": 1.0,
        "total_income_2": 1.0,
        "expenses_1": 1.0,
        "expenses_2": 1.0,
        "expenses_salaries_wages_bonus_1": 1.0,
        "expenses_salaries_wages_bonus_2": 1.0,
        "expenses_interests_1": 1.0,
        "expenses_interests_2": 1.0,
        "expenses_rents_1": 1.0,
        "expenses_rents_2": 1.0,
        "expenses_depreciation_1": 1.0,
        "expenses_depreciation_2": 1.0,
        "expenses_bad_debts_1": 1.0,
        "expenses_bad_debts_2": 1.0,
        "expenses_donation_1": 1.0,
        "expenses_donation_2": 1.0,
        "expenses_sales_tax_1": 1.0,
        "expenses_sales_tax_2": 1.0,
        "expenses_machinery_1": 1.0,
        "expenses_machinery_2": 1.0,
        "other_purchases_1": 1.0,
        "other_purchases_2": 1.0,
        "licenses_1": 1.0,
        "licenses_2": 1.0,
        "other_expenses_1": 1.0,
        "other_expenses_2": 1.0,
        "total_expenses_1": 1.0,
        "total_expenses_2": 1.0,
        "net_profit_1": 1.0,
        "net_profit_2": 1.0,
        "net_profit_income_tax_1": 1.0,
        "net_profit_income_tax_2": 1.0,
        "profit_after_tax_1": 1.0,
        "profit_after_tax_2": 1.0,
        "withheld_tax_1": 1.0,
        "withheld_tax_2": 1.0,
        "signature": "John Doe11",
        "rank": "John Doe12",
    }
    data = IP110Validator(**external_data)
    form = IP_110FormView(data)
    form.incert_to_db()

if __name__ == "__main__":
    main()
