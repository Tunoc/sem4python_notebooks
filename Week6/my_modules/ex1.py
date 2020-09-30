# Exercise 1
# create a module containing a class with the following methods:
# 1. init(self, url_list)
# 2. download(url, filename) raises NotFoundException when url returns 404
# 3. multi_download() uses threads to download multiple urls as text and stores filenames as a property
# 4. iter() returns an iterator
# 5. next() returns the next filename ( and stops when there are no more)
# 6. urllist_generator() returns a generator to loop through the urls
# 7. avg_vowels(text) - a rough estimate on readability returns average number of vowels in the words of the text
# 8. hardest_read() returns the filename of the text with the highest vowel score(use all the cpu cores on the computer for this work.
from os import path
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
import urllib
#import webget as webget
from webget import download
# I'm forced to use sys.path.append to tell python that this is where my "webget" file is - Error occurs otherwise.
import sys
sys.path.append("my_modules")


resourcePath = "./my_resources/"


class exercise6_1:
    """
    Download books
    """

    # 1
    def __init__(self, url_list):
        self.url_list = url_list
        self.filenames = []

    # 4
    def __iter__(self):
        """
        iter() returns an iterator
        """
        self.curr_iter_id = 0
        return self

    # 5
    def __next__(self):
        """
        next() returns the next filename ( and stops when there are no more)
        """
        if self.curr_iter_id == len(self.filenames):
            raise StopIteration  # signals "the end"
        else:
            self.curr_iter_id += 1
            return self.filenames[self.curr_iter_id - 1]

    # 2
    def download(self, url, filename):
        """
        download(url, filename) raises NotFoundException when url returns 404
        """
        # print("url", url)
        # print("filename", filename)

        # If run from terminal use this line.
        filename = resourcePath + filename
        try:
            download(url, filename)
            return(filename)
        except urllib.error.HTTPError as e:
            print(e)

    # 3
    def multi_download(self, url_list):
        """
        multi_download() uses threads to download multiple urls as text and stores filenames as a property
        """
        for url in url_list:
            tmp = urllib.parse.urlparse(url)
            # print(tmp[2])
            # print(tmp[2].split("/"))
            # print(tmp[2].split("/")[-1])
            # [-1] <- Gives us the last element of the array.
            self.filenames.append(tmp[2].split("/")[-1])
        workers = multiprocessing.cpu_count()
        with ThreadPoolExecutor(workers) as ex:
            result = ex.map(self.download, url_list, self.filenames)
        return result

    # 6
    def urllist_generator(self):
        """
        urllist_generator() returns a generator to loop through the urls
        """
        for url in self.url_list:
            yield url

    # 7
    def avg_vowels(self, text):
        """
        avg_vowels(text) - a rough estimate on readability returns average number of vowels in the words of the text
        """
        avg_vowels = 0
        if text:
            text = text.strip()
            vowel_counter = map(text.lower().count, "aeiouyæøå")
            word_count = len(text.split(" "))
            if word_count == 0:
                return 0
            vowel_sum = 0
            for letter_count in vowel_counter:
                vowel_sum += letter_count
            avg_vowels = round(vowel_sum/word_count, 2)
        return avg_vowels

    # 8
    def hardest_read(self):
        """
        hardest_read() returns the filename of the text with the highest vowel score(use all the cpu cores on the computer for this work.
        """
        workers = multiprocessing.cpu_count()
        with ProcessPoolExecutor(workers) as ex:
            result = ex.map(self.avg_vowels,
                            self.__readTextFile__(self.filenames))
        res = dict(zip([filename for filename in self.filenames], [
                   avg for avg in result]))
        return max(res, key=res.get)

    def __readTextFile__(self, file_names):
        for file in file_names:
            # If run from terminal use this line.
            final_path = resourcePath + file
            with open(final_path, "r", encoding="utf8", errors="ignore") as file_object:
                yield file_object.read()


if __name__ == '__main__':
    resourcePath = "../my_resources/"
    urls = []
    urls.append("https://www.gutenberg.org/files/1342/1342-0.txt")
    urls.append("https://www.gutenberg.org/files/84/84-0.txt")
    urls.append("https://www.gutenberg.org/files/25344/25344-0.txt")

    # init example
    # ex1 = exercise6_1([])
    ex1 = exercise6_1(urls)

    # download example
    # ex1.download("https://www.gutenberg.org/files/1342/1342-0.txt",
    #              "../my_resources/1342-0.txt")

    # multi download & filename as property example
    ex1.multi_download(ex1.url_list)
    # print(ex1.filenames)

    # iter & next example
    # https://www.w3schools.com/python/python_iterators.asp
    # iter_test = iter(ex1)
    # for file in iter_test:
    #     print(file)
    #     # Same as using "print(next(iter_test))" 3 times in a row.

    # urllist_generator() example
    # for url in ex1.urllist_generator():
    #    print(url)
    # Alternative:
    # [print(x) for x in ex1.urllist_generator()]

    # avg_vowels(text) example
    # tmp = ex1.avg_vowels("This 'er' ein very \nunderlig, Satz")
    # print(tmp)

    # hardest_read() example
    # tmp = ex1.hardest_read()
    # print(tmp)
