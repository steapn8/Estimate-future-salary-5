import requests


def predict_rub_salary_for_superJob(profession):
    if profession["payment_from"] and profession["payment_to"]:
        average_salary = profession["payment_from"] + profession["payment_to"]
        return average_salary/2
    elif profession["payment_from"]:
            return profession["payment_from"]*1.2

    elif profession["payment_to"]:
        return profession["payment_to"]*0.8


def getting_statistics_from_sj(programming_languages):
    headers = { "X-Api-App-Id": "v3.h.4897191.9fafc4ef87e76003bd7bd7580f2e22b9db15309f.30e05339034c9cae603df3f7c36b1d1b69b1035b"}

    sj_statistics = {}
    for programming_language in programming_languages:
        payload = {
            "catalogues": "Разработка, программирование",
            "town": "Москва",
            "keyword": f"Программист {programming_language}"
        }

        total_average_costs_superjob = []
        
        url = 'https://api.superjob.ru/2.0/vacancies/'


        response = requests.get(url, params=payload, headers=headers)
        response.raise_for_status()
        professions = response.json()["objects"]


        for profession in professions:
            if  profession["currency"] == "rub":
                if profession["payment_from"] or profession["payment_to"]:
                    total_average_costs_superjob.append(predict_rub_salary_for_superJob(profession))

        if len(total_average_costs_superjob) != 0:
            average_salary = sum(total_average_costs_superjob) / len(total_average_costs_superjob)
        else:
            average_salary= 0
        

        sj_statistics[programming_language] = {
            "vacancies_found": response.json()["total"],
            "vacancies_processed": len(total_average_costs_superjob),
            "average_salary": average_salary
        }
    return sj_statistics
