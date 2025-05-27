import requests
from terminaltables import AsciiTable

def predict_rub_salary(salary):
        if salary["from"] and salary["to"]:
            average_salary = salary["from"] + salary["to"]
            return average_salary/2
        elif salary["from"]:
            return salary["from"]*1.2
        elif salary["to"]:
            return salary["to"]*0.8




def getting_statistics_from_hh():
    programming_languages = ["Python", "Java","JavaScript","Ruby" ,"PHP","C++","CSS", "C#"]
    hh_statistics = {}
    for programming_language in programming_languages:
        
        total_average_costs = []

        for page in range(13):

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
                    total_average_costs.append(predict_rub_salary(salary))
    
        if len(total_average_costs) != 0:
            average_salary = sum(total_average_costs) / len(total_average_costs)
        else:
            average_salary= 0
        
        hh_statistics[programming_language] = {
            "vacancies_found": page_response["found"],
            "vacancies_processed": len(total_average_costs),
            "average_salary": average_salary
        }
    return hh_statistics
