# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# class AoneplusPipeline:
#     def process_item(self, item, spider):
#         print('=========================',item,"============================")
#         return item
    

import sqlite3

class SQLitePipeline:
    def open_spider(self, spider):
        self.conn = sqlite3.connect('products.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT,
                price TEXT,
                specification TEXT,
                categories TEXT,
                tag TEXT,
                sku TEXT
            )
        ''')
        self.conn.commit()

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        self.cursor.execute('''
            INSERT INTO products (name, price, specification, categories, tag, sku)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            item.get('name'),
            item.get('price'),
            '\n'.join(item.get('specification', [])),
            '\n'.join(item.get('categories', [])),
            item.get('tag'),
            item.get('sku')
        ))
        self.conn.commit()
        return item

