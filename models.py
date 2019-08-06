from matplotlib import pyplot as plt
import pandas as pd
import time
import io


def create_scatter(data):
    data = data.replace(',', '\t').replace(' ', '\t')
    df = pd.read_csv(io.StringIO(data), sep='\t')
    plt.plot(df,'o-',alpha=0.5)

    filename = time.strftime('%Y%m%d%H%M%S') + ".png"
    save_path = "./static/result/" + filename
    url = "result/" + filename
    plt.savefig(save_path)
    plt.close()

    return url


def select_all(con):
    cur = con.execute('select id, title, data, img, created from results order by id desc')
    return cur.fetchall()


def select(con, pk):
    cur = con.execute('select id, title, data, img, created from results where id=?', (pk,))
    return cur.fetchone()


def insert(con, title, data, img):
    cur = con.cursor()
    cur.execute('insert into results (title, data, img) values (?, ?, ?)', [title, data, img])

    pk = cur.lastrowid
    con.commit()

    return pk


def delete(con, pk):
    cur = con.cursor()
    cur.execute('delete from results where id=?', (pk,))
    con.commit()