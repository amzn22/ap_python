import os
import itertools
import sys
import pycode_similar
from .methods import *


def start_methods():
    projects = sys.argv[1:]
    projects_files = {}
    for project in projects:
        print(f'Проект: {project}')
        project_files = {}
        for path, dirs, files in os.walk(project):
            for file in files:
                absolute_path = os.path.join(path, file)
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


def start_lib():
    projects = sys.argv[1:]
    projects_files = {}
    for project in projects:
        print(f'Проект: {project}')
        project_files = {}
        for path, dirs, files in os.walk(project):
            for file in files:
                absolute_path = os.path.join(path, file)
                if 'venv' not in absolute_path and absolute_path.endswith('.py'):
                    fs = open(absolute_path)
                    project_files[absolute_path.removeprefix(project)] = fs.read()
                    fs.close()
        print(f'Кол-во файлов: {len(project_files)}')
        projects_files[project] = project_files
    for project1, project2 in itertools.combinations(projects, 2):
        plagiarised_files = []
        for file in projects_files[project1]:
            if file in projects_files[project2]:
                _, differences_list = pycode_similar.detect([projects_files[project1][file],
                                                             projects_files[project2][file]],
                                                            diff_method=pycode_similar.UnifiedDiff,
                                                            keep_prints=False,
                                                            module_level=True)[0]
                total_lines = 0
                plagiarised_lines = 0
                for difference in differences_list:
                    total_lines += difference.total_count
                    plagiarised_lines += difference.plagiarism_count

                if plagiarised_lines / total_lines > 0.7:
                    plagiarised_files.append(file)

        plagiarism = len(plagiarised_files) / min(len(projects_files[project1]), len(projects_files[project2]))
        if plagiarism > 0.7:
            print(f'НАЙДЕН ПЛАГИАТ. Проекты "{project1}" и "{project2}" схожи на {plagiarism * 100}%!')



