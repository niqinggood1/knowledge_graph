#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：knowledge_graph 
@File    ：neo4.py
@IDE     ：PyCharm 
@Author  ：patrick
@Date    ：2023/3/15 18:01 
'''
from typing import Text, Dict
from py2neo import Node, Relationship, Graph, NodeMatcher, RelationshipMatcher

class Neo4jDB(object):
    def __init__(self,
                 host: Text,
                 port: int,
                 username: Text,
                 password: Text):
        self.ip = f"http://{host}/:{str(port)}"
        self.username = username
        self.password = password

    def get_client(self):
        graph = Graph(self.ip, username=self.username, password=self.password)
        return graph

    def find_node_matcher(self,
                  graph:Graph,
                  label:Text,
                  condition:Dict):
        n = "_.name=" + "\"" + condition["name"] + "\""
        #     matcher = NodeMatcher(graph)
        return NodeMatcher(graph=graph).match(label).where(n) #**condition

    def find_node_one(self,
                      graph:Graph,
                      label: Text,
                      condition: Dict):
        return self.find_node_matcher(graph=graph,
                                      label=label,
                                      condition=condition).first()

    def find_node_all(self,
                      graph: Graph,
                      label: Text,
                      condition: Dict
                      ):
        return self.find_node_matcher(graph=graph,
                                      label=label,
                                      condition=condition).all()

    def find_relation_matcher(self,
                      graph:Graph,
                      node1:Node,
                      node2:Node,
                      r_type:Text,
                      condition:Dict):
        return RelationshipMatcher(graph).match((node1, node2), r_type=r_type).where(**condition)

    def find_relation_one(self,
                          graph: Graph,
                          node1: Node,
                          node2: Node,
                          r_type: Text,
                          condition: Dict
                          ):
        return self.find_relation_matcher(graph=graph,
                                          node1=node1,
                                          node2=node2,
                                          r_type=r_type,
                                          condition=condition).first()

    def find_relation_all(self,
                          graph: Graph,
                          node1: Node,
                          node2: Node,
                          r_type: Text,
                          condition: Dict
                          ):
        return self.find_relation_matcher(graph=graph,
                                          node1=node1,
                                          node2=node2,
                                          r_type=r_type,
                                          condition=condition).all()

    def add_node(self,
                 graph:Graph,
                 label:Text,
                 properties:Dict):

        if "name" not in properties:
            raise ValueError
        condition = {"name": properties["name"]}

        if self.find_node_one(graph=graph, label=label, condition=condition):
            return None
        n = graph.create(Node(label, **properties))
        return n

    def add_relation(self,
                     graph:Graph,
                     label1:Text,
                     label2:Text,
                     properties:Dict,
                     r_type:Text,
                     node1_condition:Dict,
                     node2_condition:Dict):
        node1 = self.find_node_one(graph=graph, label=label1, condition=node1_condition)
        node2 = self.find_node_one(graph=graph, label=label2, condition=node2_condition)
        if node1 is None or node2 is None:
            return None

        ## 判断是否存在关系
        if self.find_relation_one(graph=graph, node1=node1, node2=node2, r_type=r_type, condition={}):
            return None

        n = graph.create(Relationship(node1, r_type, node2, **properties))
        return n

    def update_properties(self,
                          graph:Graph,
                          label:Text,
                          properties:Dict,
                          condition:Dict):

        nodes = self.find_node_all(graph=graph, label=label, condition=condition)
        for n in nodes:
            n.update(**properties)
            graph.push(n)

    def delete_all(self, graph:Graph):
        graph.delete_all()

    def delete_node(self, node:Node):
        graph.delete(node)

    def delete_relation(self, rel:Relationship):
        graph.delete(rel)

    def find_by_id(self, graph:Graph, id:int):
        return NodeMatcher(graph)[id]

  
  