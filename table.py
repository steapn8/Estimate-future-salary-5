from terminaltables import AsciiTable
from superJob import create_statistic_from_sj
import os
from hh import create_statistic_from_hh
from dotenv import load_dotenv


def creat_table(companie_statistics, title):
    table_data = [
            ['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата'],
        ]
    for language, statistics  in companie_statistics.items():
        table_data.append([language, statistics["vacancies_found"], statistics["vacancies_processed"], statistics["average_salary"]])
    table = AsciiTable(table_data, title)
    return table.table

def main():
    programming_languages = ["Python", "Java","JavaScript","Ruby" ,"PHP","C++","CSS", "C#"]
    hh = create_statistic_from_hh(programming_languages)
    hh_table = creat_table(hh, "HeadHunter Moscow")
    print(hh_table)
    load_dotenv()
    sj_id =  os.getenv('ID_SJ')
    sj = create_statistic_from_sj(programming_languages, sj_id)
    sj_table = creat_table(sj, "SuperJob Moscow")
    print(sj_table)


if __name__ == "__main__":
    main()