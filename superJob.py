import requests
from itertools import count

def predict_rub_salary(salary_from, salary_to):
    if salary_from and salary_to:
        average_salary = salary_from + salary_to
        return average_salary/2
    elif salary_from:
        return salary_from*1.2
    elif salary_to:
        return salary_to*0.8


def create_statistic_from_sj(programming_languages, sj_id):
    headers = { "X-Api-App-Id": sj_id}

    sj_statistics = {}
    for programming_language in programming_languages:
        for page in count(0):
            payload = {
                "catalogues": "Разработка, программирование",
                "town": "Москва",
                "keyword": f"Программист {programming_language}",
                "page": page
            }

            total_average_costs_superjob = []
            
            url = 'https://api.superjob.ru/2.0/vacancies/'


            response = requests.get(url, params=payload, headers=headers)
            response.raise_for_status()
            vacancy = response.json()["objects"]


            for profession in vacancy:
                if  profession["currency"] == "rub" and profession["payment_from"] or profession["currency"] == "rub" and profession["payment_to"]:
                    total_average_costs_superjob.append(predict_rub_salary(profession["payment_from"], profession["payment_to"]))
            if not response.json()["more"]:
                break
        if len(total_average_costs_superjob):
            average_salary = sum(total_average_costs_superjob) / len(total_average_costs_superjob)
        else:
            average_salary= 0
        

        sj_statistics[programming_language] = {
            "vacancies_found": response.json()["total"],
            "vacancies_processed": len(total_average_costs_superjob),
            "average_salary": average_salary
        }
    return sj_statistics