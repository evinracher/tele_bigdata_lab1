from mrjob.job import MRJob

class MyMRJob(MRJob):

    def mapper(self, _, line):
        idemp, sector, salary, year = line.split(',')
        yield idemp, sector
        
    def reducer(self, idemp, sectors):
        sectors_emp = []
        for sec in sectors:
            sectors_emp.append(sec)
        yield idemp, sectors_emp

if __name__ == '__main__':
    MyMRJob.run()
