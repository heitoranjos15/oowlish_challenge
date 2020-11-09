from config import enviroment


def paginate_customers(full_data, page=1, max_values=10):
    first_customer = (page - 1) * max_values
    last_customer = page * max_values
    customers = full_data[first_customer:last_customer]
    if customers:
        return {
            'customers': customers,
            'actual_page': page,
            'values': max_values,
            'next_page': f"{enviroment.api_host}/customers/page/{page + 1}"
        }
