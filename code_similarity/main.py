import os
import itertools
from .methods import *


def start_methods(projects):
    projects_files = {}
    for project in projects:
        print(f'Проект: {project}')
        project_files = {}
        for path, dirs, files in os.walk(project):
            for file in files:
                absolute_path = f'{path}/{file}'
                if 'venv' not in absolute_path and absolute_path.endswith('.py'):
                    project_files[absolute_path[len(project):]] = absolute_path
        print(f'Кол-во файлов: {len(project_files)}')
        print("----------------------------------------------------------")
        projects_files[project] = project_files

    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print()
    print()

    for project_1, project_2 in itertools.combinations(projects, 2):
        results_sum = 0
        files_count = len(projects_files[project_1]) + len(projects_files[project_2])
        for key in projects_files[project_1]:
            if key in projects_files[project_2]:
                file_1 = projects_files[project_1].get(key)
                file_2 = projects_files[project_2].get(key)

                sorted_file_1 = file_sorting(file_1)
                sorted_file_2 = file_sorting(file_2)
                result_from_files = counting(sorted_file_1, sorted_file_2)

                results_sum += result_from_files
                print(f"Процент плагиата между файлами {key} равен: {result_from_files * 100} %")
                print("----------------------------------------------------------")

        main_result = (results_sum / (files_count / 2)) * 100

        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print()
        print()
        print(f"Общий процент плагиата между проетами {project_1} и {project_2}: {main_result} %")


