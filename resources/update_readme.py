from resources.count_files import count_files


def resueltos_list(last):
    problems_solved = count_files()
    problem_url = 'https://projecteuler.net/problem='  # + 'nª problema'
    solved_url = 'https://github.com/MatiasPineda/projecteuler/blob/master/problems/'  # + f'problem{nªproblema}.py'
    resueltos = []
    for i in range(last + 1, problems_solved+1):
        resueltos.append(f'* Problema {i}: [Enunciado]({problem_url}{i}) - [Código]({solved_url}problem{i}.py)\n')
    return resueltos


def read_readme():
    readme_file = 'README.md'
    with open(readme_file, 'r') as f:
        data = f.readlines()
    return data


def update():
    readme_file = 'README.md'
    data = read_readme()
    inicio_lista = data.index('## Projectos Resueltos\n') + 2
    last_added = len(data) - inicio_lista
    with open(readme_file, 'a') as f:
        f.writelines(resueltos_list(last_added))



