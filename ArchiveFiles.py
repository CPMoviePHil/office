from datetime import datetime
import os
import zipfile

class ArchiveFiles:
    directory_path = ''
    log_pattern = ''
    directory_path_s = []

    def set_pattern(self, pattern):
        self.log_pattern = pattern

    def get_current_dir(self):
        self.directory_path = os.path.dirname(os.path.realpath(__file__))
        return self.directory_path

    def set_directory_path_s(self, li):
        self.directory_path_s = li


    def get_file_date(self, the_filename):
        the_date_remove_log = the_filename.replace('log.log.', '')
        return datetime.strftime(datetime.strptime(the_date_remove_log, '%Y-%m-%d'), '%Y-%m-%d')

    def get_dirs_list_files_date(self):
        for dp in self.directory_path_s:
            temp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), dp))
            dirs = os.listdir(temp)
            counter = 0
            while counter < len(dirs):
                if len(dirs) % 3 != 0:
                    with zipfile.ZipFile(os.path.join(temp, dirs[counter] + '.zip'), 'w') as zf:
                        if counter + len(dirs) % 3 == len(dirs):
                            for k in dirs[counter:counter+len(dirs) % 3]:
                                zf.write(os.path.join(temp, k))
                        else:
                            for k in dirs[counter:counter + 3]:
                                zf.write(os.path.join(temp, k))
                    zf.close()
                else:
                    with zipfile.ZipFile(os.path.join(temp, dirs[counter] + '.zip'), 'w') as zf:
                        for k in dirs[counter:counter+3]:
                            zf.write(os.path.join(temp, k))
                    zf.close()
                counter += 3

    def get_datetime(self):
        pass


if __name__ == '__main__':
    af1 = ArchiveFiles()
    af1.set_directory_path_s(['scanner_logs', 'update_code_logs'])
    af1.get_dirs_list_files_date()
