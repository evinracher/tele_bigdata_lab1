from mrjob.job import MRJob

class MyMRJob(MRJob):

    def mapper(self, _, line):
        idemp, sector, salary, year = line.split(',')
        try:
            salary = float(salary)
        except ValueError:
            pass
        else:
            yield sector, salary
        
    def reducer(self, sector, salaries):
        sum_sal = 0
        count = 0
        for salary in salaries:
            sum_sal = sum_sal + salary
            count = count + 1
        yield sector, sum_sal/count

if __name__ == '__main__':
    MyMRJob.run()
