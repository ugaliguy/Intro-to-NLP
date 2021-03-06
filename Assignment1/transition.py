#!/usr/bin/env python

class Transition(object):
    """
    This class defines a set of transitions which are applied to a
    configuration to get the next configuration.
    """
    # Define set of transitions
    LEFT_ARC = 'LEFTARC'
    RIGHT_ARC = 'RIGHTARC'
    SHIFT = 'SHIFT'
    REDUCE = 'REDUCE'

    def __init__(self):
        raise ValueError('Do not construct this object!')

    @staticmethod
    def left_arc(conf, relation):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """
        # raise NotImplementedError('Please implement left_arc!')
        # return -1
        if not conf.buffer or not conf.stack:
            return -1
        s = conf.stack[-1]
        # check that s is not the ROOT
        if s == 0:
            return -1
        # check that s is not already a dependant of some other word
        if any(s == wj for wi, l, wj in conf.arcs):
            return -1
        # take an item from the buffer, but do not pop it
        b = conf.buffer[0]
        conf.stack.pop()
        conf.arcs.append((b, relation, s))

    @staticmethod
    def right_arc(conf, relation):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """
        if not conf.buffer or not conf.stack:
            return -1

        # You get this one for free! Use it as an example.

        idx_wi = conf.stack[-1]
        idx_wj = conf.buffer.pop(0)

        conf.stack.append(idx_wj)
        conf.arcs.append((idx_wi, relation, idx_wj))

    @staticmethod
    def reduce(conf):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """
        # raise NotImplementedError('Please implement reduce!')
        # return -1
        if not conf.stack:
            return -1
        s = conf.stack[-1]

        if any(s == wi for wk, l, wi in conf.arcs):
            conf.stack.pop()
        else:
            return -1

    @staticmethod
    def shift(conf):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """
        # raise NotImplementedError('Please implement shift!')
        # return -1
        if not conf.buffer:
            return -1

        conf.stack.append(conf.buffer.pop(0))
