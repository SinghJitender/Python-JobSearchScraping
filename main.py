# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # import builtwith
    # builtwith.parse("https://www.naukri.com")
    # print_hi('PyCharm')
    # import requests
    # from bs4 import BeautifulSoup
    # r = requests.get("https://www.linkedin.com/")
    # c = BeautifulSoup(r.text,features="html.parser")
    # print(r.text)
    # #print(c.text)
    # #print(c.title.text)

    #
    # import xlsxwriter
    # import datetime
    # filename = r"Job_Search_%s.xlsx" % str(datetime.datetime.now().strftime("%Y_%m_%d_%I_%M_%p"))
    # location = r"C:\Users\Jitender\PycharmProjects\JobScraping\Data\%s" % filename
    # wb = xlsxwriter.Workbook(location)
    # sheet = wb.add_worksheet()
    # sheet.write_row(0,0,data=['ID', 'Title', 'Company', 'Ratings', 'Link', 'Match Percentage'])
    # wb.close()

    #print("-"*50)

    import matplotlib.pyplot as plt
    x = [1,2,3,4,5,6,7]
    y = [2,4,6,8,10,12,14]
    plt.plot(x,y)
    plt.show()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
