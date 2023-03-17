#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：knowledge_graph 
@File    ：test_neo4.py
@IDE     ：PyCharm 
@Author  ：patrick
@Date    ：2023/3/15 17:34 
'''
# from py2neo import Node, Relationship, Graph, NodeMatcher, RelationshipMatcher
#
# # 建立一个节点
# def create_node(graph, label, attrs):
#     n = "_.name=" + "\"" + attrs["name"] + "\""
#     matcher = NodeMatcher(graph)
#     # 查询是否已经存在，若存在则返回节点，否则返回None
#     value = matcher.match(label).where(n).first()
#     # 如果要创建的节点不存在则创建
#     if value is None:
#         node = Node(label, **attrs)
#         n = graph.create(node)
#         return n
#     return None
#
# # 建立两个节点之间的关系
# def create_relationship(graph, label1, attrs1, label2, attrs2, r_name):
#     value1 = match_node(graph, label1, attrs1)
#     value2 = match_node(graph, label2, attrs2)
#     if value1 is None or value2 is None:
#         return False
#     r = Relationship(value1, r_name, value2)
#     graph.create(r)
# # 查询节点
# def match_node(graph, label, attrs):
#     n = "_.name=" + "\"" + attrs["name"] + "\""
#     matcher = NodeMatcher(graph)
#     return matcher.match(label).where(n).first()
#
#
#     graph = Graph("http://localhost:7474/", auth=("neo4j", "123456"))
#     a = Node("Person", name="Alice",    sex="female",   ID="222")
#     b = Node("Person", name="Bob",      sex="male",     ID="123")
#     ab = Relationship(a, "KNOWS", b)
#     graph.create(   ab )
#
#     macher1 = NodeMatcher(  graph   )
#     macher2 = RelationshipMatcher(  graph   )
#     node1 = macher1.match(  "Person", ID="123"    )  # 匹配ID为123的节点
#     node2 = macher2.match(  r_type="KNOWS").limit(25)  # 找出关系类型为KNOWS的前25个关系
#
#     result1 = list(node1)
#     print(result1)
#     result2 = list(node2)
#     print(result2)
from neo4 import Neo4jDB
import pandas as pd
if __name__ == '__main__':
    #7687
    neo4j = Neo4jDB('127.0.0.1',port=7474, username='patrick', password='patrick')
    graph = neo4j.get_client( ) #:7474/db/data/
    neo4j.add_node(graph, '深股通', {'name':'深股通','名字': '深股通'})
    neo4j.add_node(graph, '沪股通', {'name':'沪股通','名字': '沪股通'})

    # stock = pd.read_csv('stock_basic.csv', encoding="gbk")
    # holder = pd.read_csv('holders.csv')
    # concept_num = pd.read_csv('concept.csv')
    # concept = pd.read_csv('stock_concept.csv')
    # sh = pd.read_csv('sh.csv')
    # sz = pd.read_csv('sz.csv')
    # corr = pd.read_csv('corr.csv')
    #
    # stock['行业'] = stock['行业'].fillna('未知')
    # holder = holder.drop_duplicates(subset=None, keep='first', inplace=False)

    exit( )
    for i in concept_num.values:
        # a = Node('概念', 概念代码=i[1], 概念名称=i[2])
        # print('概念代码:' + str(i[1]), '概念名称:' + str(i[2]))
        #graph.create( a )
        neo4j.add_node(graph, '概念',{'name': '概念', '概念代码': i[1] ,'概念名称': i[2] }  )

    for i in stock.values:
        Neo4jDB.add_node(graph, '股票', {'TS代码': i[1], '股票名称':i[3], '行业':i[4]   })

    for i in holder.values:
        Neo4jDB.add_node(graph, '股东', {'TS代码': i[1], '股东名称':i[1], '持股数量':i[2] ,'持股比例':i[3] })


    #   https://github.com/jm199504/Financial-Knowledge-Graphs
    exit()
    
  
  