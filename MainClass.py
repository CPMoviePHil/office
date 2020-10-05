from datetime import datetime, timedelta
import os
import re


class MainClass:
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

    def get_dir_list_file(self):
        pass

    def get_last_day_date(self, day):
        last_3_date = datetime.today() - timedelta(day)
        return datetime.strftime(last_3_date, '%Y-%m-%d')

    def get_file_date(self, the_filename):
        the_date_remove_log = the_filename.replace('log.log.', '')
        return datetime.strftime(datetime.strptime(the_date_remove_log, '%Y-%m-%d'), '%Y-%m-%d')

    def run_deleting_file(self):
        for dp in self.directory_path_s:
            temp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), dp))
            dirs = os.listdir(temp)
            for v in dirs:
                if self.file_matching(v):
                    if self.get_last_day_date(3) > self.get_file_date(v):
                        self.del_the_file(os.path.join(temp, v))
                else:
                    pass

    def file_matching(self, filename):
        if re.match(self.log_pattern, filename):
            return True
        else:
            return False

    def del_the_file(self, filename):
        os.remove(filename)

    def get_datetime(self):
        pass


if __name__ == '__main__':
    main1 = MainClass()
    main1.set_directory_path_s(['scanner-lock'])
    main1.set_pattern(r"log.log.(\d{4})-(\d{2})-(\d{2})$")
    main1.run_deleting_file()
