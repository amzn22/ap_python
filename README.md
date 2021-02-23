# Anti-plagiarism on Python
##### [Ссылка на презентацию проекта](https://docs.google.com/presentation/d/1pwM77KrHbaE-vN94Jh-8vWR_oQB6jHfMTrfVR9SoYE4/edit#slide=id.p)

Наш проект - это инструмент для проверки плагиата в исходном коде на Python. На вход подаются папки с исходным кодом нескольких проектов. Программа проверяет каждый проект с каждым. В качестве результата она будет выдавать сообщение,  в каких парах был найден плагиат и процент похожих файлов. 


### Фичи и особенности проекта:

* Названия переменных не будут учитываться. То есть, если произошло изменение только названий переменных, это будет считается плагиатом.
* Переносы, пробелы, комментарии учитываться не будут.
* Если встретились файлы, которые программа ранее уже проверяла, повторно обрабатываться они уже не будут.

### Архитектура:

* Программе подается список всех проектов (папки с файлами). При считывании файлов проекта будут учитываться файлы только с расширением .py и не будут учитываться системные файлы (например .idea и _pycache_).
* При сравнивании файлов и при определенном проценте найденного плагиата, алгоритм будет отмечать файлы как схожие или нет. Сами проекты будут считаться схожими, если определенный процент файлов будут отмечены, как  плагиат.
* После отработки алгоритма, программа выведет список всех схожих пар проектов и процент плагиата.

### Запуск проекта:

* Проект запускается через консоль с помощью команды python start.py project_1 project_2 (где project_1 и project_2 - это пути к проектам)
