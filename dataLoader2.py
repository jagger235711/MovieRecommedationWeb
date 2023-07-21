import sqlite3

import pandas as pd


def create_table(conn):
    # 创建Movie表
    conn.execute("""
        CREATE TABLE IF NOT EXISTS Movie (
        mid INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        descri TEXT ,
        timelong TEXT ,
        issue TEXT ,
        shoot TEXT,
        language TEXT ,
        genres TEXT ,
        actors TEXT ,
        directors TEXT 
        );
    """)

    # 创建Rating表
    conn.execute("""
        CREATE TABLE IF NOT EXISTS Rating (
        uid INTEGER,
        mid INTEGER,
        score REAL,
        timestamp INTEGER,
        PRIMARY KEY (uid, mid)
        );
    """)

    # 创建Tag表
    conn.execute("""
        CREATE TABLE IF NOT EXISTS Tag (
        uid INTEGER,
        mid INTEGER,
        tag TEXT NOT NULL,
        timestamp INTEGER,
        PRIMARY KEY (uid, mid, tag)
        );
    """)


def import_data(conn, table_name, data_df, data_columns):
    data_df.columns = data_columns
    data_df.to_sql(table_name, conn, if_exists="replace", index=False)
    # data_df.to_sql(table_name, conn, if_exists="append")


def main():
    # 数据文件路径
    MOVIES_DATA_PATH = "extraStatics/ml-in-use/movies.csv"
    RATINGS_DATA_PATH = "extraStatics/ml-in-use/ratings.csv"
    TAGS_DATA_PATH = "extraStatics/ml-in-use/tags.csv"

    # 建立数据库连接
    connection = sqlite3.connect("movielens_in_use.db")

    # 创建表格
    create_table(connection)

    # 导入Movie数据
    movie_columns = ['mid', 'name', 'descri', 'timelong', 'issue',
                     'shoot', 'language', 'genres', 'actors', 'directors']
    movie_data = pd.read_csv(MOVIES_DATA_PATH, sep="\\^", header=None)
    import_data(connection, "Movie", movie_data, movie_columns)

    # 导入Rating数据
    rating_columns = ['uid', 'mid', 'score', 'timestamp']
    rating_data = pd.read_csv(RATINGS_DATA_PATH, header=None)
    import_data(connection, "Rating", rating_data, rating_columns)

    # 导入Tag数据
    tag_columns = ['uid', 'mid', 'tag', 'timestamp']
    tag_data = pd.read_csv(TAGS_DATA_PATH, header=None)
    import_data(connection, "Tag", tag_data, tag_columns)

    # 提交事务
    connection.commit()

    # 关闭连接
    connection.close()


if __name__ == "__main__":
    main()
