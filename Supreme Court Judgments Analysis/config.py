import tkinter as tk


class Config:
    ALL_DATA_DIR_NAME = "data"  # the data directory in this current path , it will be created if u dont have
    EACH_QUERY_FILES_DIR_NAME = "pdfs"  # for each query it will create a folder and put its downloaded files into this folder name
    EACH_QUERY_CSV_FILE_DIR_NAME = "csv"  # for each query it will create a folder and in this folder we will keep the proccessed dataframe csv of this query
    CHROMEDRIVER_PATH = "/usr/bin/chromedriver"  # your path to chrome
    DOWNLOAD = False  # can keep at true its doesnt redownload , but it still open sellinum
    MAX_FILES_TO_DOWNLOAD_FROM_QUERY = 20  # max of files to download for the chosen query , its doesnt iterate , for the same query if the files already downloaded , it wont redownload, if u put bigger number it just add the files you didnt have
    TEST = True  # not asking for input
    QUERY_TEST_INPUT = None


def handle_submit():
    config.QUERY_TEST_INPUT = entry.get()
    root.destroy()


config = Config()

# GUI for the user query
if not config.TEST:
    root = tk.Tk()
    root.title("Query Input")

    label = tk.Label(root, text="Enter your query:")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    submit_button = tk.Button(root, text="Submit", command=handle_submit)
    submit_button.pack()

    root.mainloop()
