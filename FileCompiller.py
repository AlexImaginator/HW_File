class FileCompiller:
    def __init__(self, *files_list):
        self.files_list = files_list

    def compile_files(self, result_file):
        if result_file in self.files_list:
            print('Ошибка. Имена исходного и целевого файлов совпадают.')
        else:
            total_list = []
            for file in self.files_list:
                with open(file, encoding='utf-8') as readed_file:
                    read_file_content_list = readed_file.readlines()
                    res_file_content_list = [file + '\n',
                                             str(len(read_file_content_list)) + '\n',
                                             *read_file_content_list,
                                             '\n']
                    total_list.append(res_file_content_list)
            total_list.sort(key=len)
            with open(result_file, 'w', encoding='utf-8') as res_file:
                for list in total_list:
                    res_file.writelines(list)
            print(f'Файлы объединены в {result_file}')
