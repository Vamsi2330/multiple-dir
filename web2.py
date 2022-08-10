import os


def loo():
    for j in range(1, 5):
        directory = "vamsi " + str(j)
        parent_dir = "D:/pycharm projects/"

        path = os.path.join(parent_dir, directory)

        os.mkdir(path)
        print(f"Directory {directory} created ")


for i in range(0, 5):
    loo()
