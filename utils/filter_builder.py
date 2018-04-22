#!/usr/bin/env python
# _*_ coding:utf-8 _*_


class FilterBuilder():
    def __init__(self):
        pass

    @staticmethod
    def dict_to_str(content):
        """
        build filter
        :param content:
        :return:
        """
        ret = []
        for k in content:
            ret.append(str(k)+"="+str(content[k]))
        return ','.join(ret)
