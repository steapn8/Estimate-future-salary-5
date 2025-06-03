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


def create_statistic_from_hh(programming_languages):
    hh_statistics = {}
    for programming_language in programming_languages:
        total_average_costs = []
        for page in count(0):
            payload = {
                "text":programming_language,
                "period":30,
                "area": 1,
                'page': page
            }

            url = 'https://api.hh.ru/vacancies'
            response = requests.get(url, params=payload)
            response.raise_for_status()
            
            page_response = response.json()
            
            for vacancy in page_response["items"]:
                salary = vacancy["salary"]
                if salary and salary["currency"] == "RUR":
                    total_average_costs.append(predict_rub_salary(salary["from"], salary["to"]))
            if page >= page_response["pages"]-1:
                break
    
        if len(total_average_costs):
            average_salary = sum(total_average_costs) / len(total_average_costs)
        else:
            average_salary= 0
        
        hh_statistics[programming_language] = {
            "vacancies_found": page_response["found"],
            "vacancies_processed": len(total_average_costs),
            "average_salary": average_salary
        }
    return hh_statistics