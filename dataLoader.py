'''
将ml-latest-small的数据导入数据库，初始数据来自movieLens
'''
import sqlite3

import pandas as pd


def create_tables(conn):
    # 创建movies表
    conn.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            movieId INTEGER PRIMARY KEY,
            title TEXT,
            genres TEXT
        );
    """)

    # 创建ratings表
    conn.execute("""
        CREATE TABLE IF NOT EXISTS ratings (
            userId INTEGER,
            movieId INTEGER,
            rating REAL,
            timestamp INTEGER
        );
    """)

    # 创建tags表
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tags (
            userId INTEGER,
            movieId INTEGER,
            tag TEXT,
            timestamp INTEGER
        );
    """)
    # 创建links表
    conn.execute("""
            CREATE TABLE IF NOT EXISTS links (
                movieId INTEGER PRIMARY KEY,
                imdbId INTEGER,
                tmdbId INTEGER
            );
        """)


def insert_data(conn, table_name, data_df):
    data_df.to_sql(table_name, conn, if_exists='append', index=False)


def main():
    # 数据文件路径
    MOVIES_DATA_PATH = "extraStatics/ml-latest-small/movies.csv"
    RATINGS_DATA_PATH = "extraStatics/ml-latest-small/ratings.csv"
    TAGS_DATA_PATH = "extraStatics/ml-latest-small/tags.csv"
    LINKS_DATA_PATH = "extraStatics/ml-latest-small/links.csv"

    # 创建SQLite数据库连接
    conn = sqlite3.connect("movielens.db")

    # 创建表
    create_tables(conn)

    # 读取并插入movies数据
    movies_data = pd.read_csv(MOVIES_DATA_PATH)
    insert_data(conn, "movies", movies_data)

    # 读取并插入ratings数据
    ratings_data = pd.read_csv(RATINGS_DATA_PATH)
    insert_data(conn, "ratings", ratings_data)

    # 读取并插入tags数据
    tags_data = pd.read_csv(TAGS_DATA_PATH)
    insert_data(conn, "tags", tags_data)

    # 读取并插入links数据
    links_data = pd.read_csv(LINKS_DATA_PATH)
    insert_data(conn, "links", links_data)

    # 提交更改并关闭连接
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
