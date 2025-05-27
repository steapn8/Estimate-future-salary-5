from terminaltables import AsciiTable
from superJob import getting_statistics_from_sj
from hh import getting_statistics_from_hh


def creat_table(companie_statistics, title):
    table_data = [
            ['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата'],
        ]
    for language, statistics  in companie_statistics.items():
        table_data.append([language, statistics["vacancies_found"], statistics["vacancies_processed"], statistics["average_salary"]])
    table = AsciiTable(table_data, title)
    print(table.table)


def main():
    programming_languages = ["Python", "Java","JavaScript","Ruby" ,"PHP","C++","CSS", "C#"]
    hh = getting_statistics_from_hh(programming_languages)
    creat_table(hh, "HeadHunter Moscow")
    sj = getting_statistics_from_sj(programming_languages)
    creat_table(sj, "SuperJob Moscow")


if __name__ == "__main__":
    main()