import os
class OutputFile:
    def __init__(self, name = ''):
        self.name = name


    def output_file(self, fileDir, value_time, sensor_value):
        dirName = "../outputData/" + fileDir
        os.chdir(dirName)
        self.time = value_time
        self.sensor_value = sensor_value

        file_name = self.name + str(value_time) + '.txt'

        with open(file_name, 'a') as f:
            f.write(str(self.sensor_value))
            f.flush()
