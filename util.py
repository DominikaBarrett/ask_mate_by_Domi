
from data_manager import read_csv_file, write_csv_file


def read_csv_file(filename):
    new = {}
    with open(filename, 'r') as data:
        for line in csv.DictReader(data):
            new[int(line['id'])] = {}
            id_number = int(line['id'])
            del line['id']
            new[id_number] = line
    return new


# do poniższej listy trzeba będzie dodać kolumnę "image" na końcu gdy dodawanie zdjęć będzie gotowe
csv_columns = ["id", "submission_time", "view_number", "vote_number", "title", "message"]


def write_csv_file(filename, dictionaries, write_method="a"):
    """
    params: nazwa pliku, lista słowników, opcjonalnie metoda zapisu: w/a
    returns: nothing
    potwierdzam, działa <3
    """
    with open(filename, write_method) as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        if write_method == "w":
            writer.writeheader()
        for data in dictionaries:
            writer.writerow(data)



def get_question_by_id(question_id):
    data_id_question = read_csv_file('sample_data/question.csv')

    # message = data_id_question[iD]['message']
    # title = data_id_question[iD]['title']
    return data_id_question.get(question_id, None)


# print(get_question_by_id(1))


def get_answers_by_question_id(question_id):
    question_id = int(question_id)
    data_file = read_csv_file('sample_data/answer.csv')
    result = {}
    print(type(question_id))
    for i in data_file:
        print(type(data_file[i]['question_id']))
        if int(data_file[i]['question_id']) == question_id:
            result[i] = data_file[i]
    return result


def delete_question(question_id):
    question = read_csv_file('sample_data/question.csv')
    print(question, question.keys())
    result = []
    for i in question:
        if i != question_id:
            tmp = question[i]
            tmp.pop('image', None)
            tmp.update({'id': i})
            result.append(tmp)
    print('///\n', result)
    left_question = write_csv_file('sample_data/question.csv', result, "w")
    return left_question

def id_maker(dict_id):
    if len(dict_id) == 0:
        ide = 1
    else:
        max_key = max(dict_id, key=int)
        ide = max_key + 1
    return int(ide)

# def get_all_questions():
#     data_file = open_file('sample_data/movie_questions.csv')
#     return data_file
