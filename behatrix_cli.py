#!/usr/bin/env python3

"""
Behatrix
Behavioural Strings Analysis (BSA)).

Behavioral strings analysis with randomization test

Copyright 2017-2018 Olivier Friard

This file is part of Behatrix.

  Behatrix is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 3 of the License, or
  any later version.

  Behatrix is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program; if not see <http://www.gnu.org/licenses/>.

"""

import os
import sys
import argparse
import numpy as np
import concurrent.futures
import random
import version


SEPARATOR = "@%&£$"


def remove_comments(s):
    """
    remove comments (#) from text

    Args:
        s (string): text

    Returns:
        str: text without commented lines separated by \n
    """

    strings_list = []
    for x in s.split("\n"):
        if not x.startswith("#"):
            strings_list.append(x)
    return "\n".join(strings_list)


def behav_strings_stats(string, chunk=0, behaviors_separator=""):
    """
    extract some information from behavioral strings

    Args:
        string (str): behavioral strings
        chunk (int): limit analysis to the chunk first characters
        separator (str): string to use to split sequences in behaviors

    Returns:
        bool: 0 -> OK
        list: sequences

    return 0, sequences, d, nodes, starting_nodes, tot_nodes, tot_trans, tot_trans_after_node, behaviours
    """

    # replace space by underscore (_)
    # string = string.replace(" ", "_")

    # remove lines starting with #
    string = remove_comments(string)

    # check if behaviors are unique char
    if behaviors_separator:
        rows = string.split("\n")   # split text in list
        flagOne = False
    else:
        rows = string.replace(" ", "").split()
        flagOne = True

    sequences = []

    d = {}
    nodes = {}
    starting_nodes = {}

    min_chunk_length = 1e6

    not_alnum = []
    pos_not_alnum = 0
    line_count = 0

    for row in rows:
        # skip empty line
        if not row:
            continue

        if flagOne:
            r = list(row.strip())
        else:
            r = row.strip().split(behaviors_separator)

        if chunk:
            r = r[0:chunk]

        sequences.append(r)

        line_count += 1

        min_chunk_length = min(min_chunk_length, len(r))

        for node in r:
            if flagOne and not node.isalnum():
                not_alnum = [line_count, ord(node)]

            if node in nodes:
                nodes[node] += 1
            else:
                nodes[node] = 1

        for i in range(len(r) - 1):

            # starting node
            if i == 0:
                if r[i] in starting_nodes:
                    starting_nodes[r[i]] += 1
                else:
                    starting_nodes[r[i]] = 1

            if r[i] + SEPARATOR + r[i + 1] in d:

                d[r[i] + SEPARATOR + r[i + 1]] += 1

            else:
                d[r[i] + SEPARATOR + r[i + 1]] = 1

    # total number of transitions
    tot_trans = 0
    for i in d:
        tot_trans += d[i]

    # number of transitions after behavior
    tot_trans_after_node = {}

    for i in d:

        b1, b2 = i.split(SEPARATOR)

        if b1 in tot_trans_after_node:
            tot_trans_after_node[b1] += d[i]
        else:
            tot_trans_after_node[b1] = d[i]

    tot_nodes = 0
    for node in nodes:
        tot_nodes += nodes[node]

    behaviours = []

    # extract unique behaviors
    for seq in sequences:
        for c in seq:
            if c not in behaviours:
                behaviours.append(c)

    behaviours.sort()

    return 0, sequences, d, nodes, starting_nodes, tot_nodes, tot_trans, tot_trans_after_node, behaviours


def check_exclusion_list(exclusion_str, sequences, behaviors_separator=""):
    """
    check the transition exclusion strings
    format must be like:
    a:bc
    or
    a:b|c

    Args:
        exclusion_str (str): exclusion strings (format must be a:bc or a:b|c
        sequences (list): list of sequences
        behaviors_separator (str): string to be used to split sequences in behaviors

    Returns:
        dict: keys: "error_code": 0 or 1
                    "exclusion_list": {"a": ["b", "c"]}
    """

    exclusion_list = {}

    if exclusion_str:
        rows = exclusion_str.split("\n")

        for row in rows:
            if row.strip() and ":" in row:
                s1, s2 = row.strip().split(":")
                if s1 and s2:
                    if s1 not in exclusion_list:
                        exclusion_list[s1] = []
                    if behaviors_separator and behaviors_separator in s2:
                        exclusion_list[s1] += s2.split(behaviors_separator)
                    else:
                        exclusion_list[s1] += list(s2)

        # test if behavioral strings do not contain an excluded transition
        for seq in sequences:
            for i in range(len(seq) - 1):
                if seq[i] in exclusion_list and seq[i + 1] in exclusion_list[seq[i]]:
                    return {"error_code": 1,
                            "message": "The behavioral strings contain an excluded transition: {} -> {}".format(seq[i], seq[i + 1]),
                            "exclusion_list": {}}

    return {"error_code": 0, "exclusion_list": exclusion_list}


def draw_diagram(cutoff_all,
                 cutoff_behavior,
                 unique_transitions,
                 nodes,
                 tot_nodes,
                 tot_trans,
                 tot_trans_after_node,
                 starting_nodes=[],
                 edge_label="percent_node",   # fraction_node/percent_node/percent_total
                 transparent_background=False,
                 include_first=True,
                 decimals_number=3,
                 significativity=None,
                 behaviors=[]):

        """
        create code for GraphViz
        return string containing graphviz code
        """


        def f_edge_label(edge_label, node1, node2, di, tot_trans_after_node_i0, tot_trans, decimals_number, pen_width=1):

            if edge_label == 'fraction_node':

                return '"{node1}" -> "{node2}" [label = "{di}/{tot_transition_after_node}" pen_width={pen_width}];\n'.format(
                    node1=node1,
                    node2=node2,
                    di=di,
                    tot_transition_after_node_i0=tot_transition_after_node_i0,
                    pen_width=pen_width)

            elif edge_label == 'percent_node':
                return '"{node1}" -> "{node2}" [label = "{percent} %" pen_width={pen_width}];\n'.format(
                    node1=node1,
                    node2=node2,
                    percent=round(di / tot_trans_after_node[i0] * 100, decimals_number)
                            if decimals_number else round(di / tot_trans_after_node[i0] * 100),
                    pen_width=pen_width
                    )

            elif edge_label == 'percent_total':
                return '"{node1}" -> "{node2}" [label = "{percent} %" pen_width={pen_width}];\n'.format(
                    node1=node1,
                    node2=node2,
                    percent=round(di / tot_trans * 100.0, decimals_number)
                            if decimals_number else round(di / tot_trans * 100.0),
                    pen_width=pen_width
                )

        def width(p):
            if p <= 0.001:
                return 6
            elif p <= 0.005:
                return 3
            else:
                return 1

        if significativity is not None:
            print(significativity)

        out = 'digraph G {\n'

        # make png transparent
        if transparent_background:
            out += 'graph [bgcolor="#ffffff00"]\n'

        if cutoff_all:

            for i in unique_transitions:

                if unique_transitions[i] / tot_trans * 100.0 >= cutoff_all:

                    i0, i1 = i.split(SEPARATOR)

                    if i0 in starting_nodes:
                        node1 = "{} ({})".format(i0, starting_nodes[i0])
                    else:
                        node1 = "{}".format(i0)

                    if i1 in starting_nodes:
                        node2 = "{} ({})".format(i1, starting_nodes[i1])

                    else:
                        node2 = "{}".format(i1)

                    out += f_edge_label(edge_label, node1, node2, unique_transitions[i],
                                        tot_trans_after_node[i0], tot_trans, decimals_number,
                                        pen_width(significativity[behaviors.index(i0), behaviors.index(i1)]))

        elif cutoff_behavior:

            for i in unique_transitions:

                i0, i1 = i.split(SEPARATOR)

                if unique_transitions[i] / tot_trans_after_node[i0] * 100 >= cutoff_behavior:

                    if i0 in starting_nodes and include_first:
                        node1 = "{} ({})".format(i0, starting_nodes[i0])
                    else:
                        node1 = "{}".format(i0)

                    if i1 in starting_nodes and include_first:
                        node2 = "{} ({})".format(i1, starting_nodes[i1])

                    else:
                        node2 = "{}".format(i1)

                    out += f_edge_label(edge_label, node1, node2, unique_transitions[i], tot_trans_after_node[i0], tot_trans, decimals_number)

        else:

            for i in unique_transitions:

                i0, i1 = i.split(SEPARATOR)

                if i0 in starting_nodes:
                    node1 = "{} ({})".format(i0, starting_nodes[i0])
                else:
                    node1 = "{}".format(i0)

                if i1 in starting_nodes:
                    node2 = "{} ({})".format(i1, starting_nodes[i1])

                else:
                    node2 = "{}".format(i1)

                print(i0, i1,significativity[behaviors.index(i0), behaviors.index(i1)])

                pen_width = width(significativity[behaviors.index(i0), behaviors.index(i1)]) if significativity is not None else 1

                out += f_edge_label(edge_label, node1, node2, unique_transitions[i],
                                    tot_trans_after_node[i0], tot_trans, decimals_number,
                                    pen_width)


        out += '}\n'

        print(out)
        return out


def create_observed_transition_matrix(sequences, behaviours):
    """
    create the matrix of observed transitions
    """
    observed_matrix = np.zeros((len(behaviours), len(behaviours)))

    for seq in sequences:
        for i in range(len(seq) - 1):
            if seq[i] in behaviours and seq[i + 1] in behaviours:
                observed_matrix[behaviours.index(seq[i]), behaviours.index(seq[i + 1])] += 1

    return observed_matrix


def permutations_test(nrandom: int,
                      sequences,
                      behaviours,
                      exclusion_list,
                      block_first,
                      block_last,
                      observed_matrix: np.array,
                      no_repetition: bool=False):
    """
    permutations test

    Args:
        nrandom (int): number of random permutations
        sequences (list): list of sequences
        behaviours (list): list of unique observed behaviours
        block_first (bool): avoid that 1st behavior be permuted
        block_last (bool): avoid that last behavior be permuted
        observed_matrix (np.array): matrix of observed transitions number

    Returns:
        count_tot
        risu (numpy array)
    """

    def strings_permutation(space: list,
                            sequences: list,
                            exclusion_list: list,
                            block_first: bool,
                            block_last: bool,
                            no_repetition: bool=False):
        """
        create permutations of sequences following exclusions list, block first/last behavior

        Args:
            space (list): list of all behaviors ocuurences
            sequences (list): list of behavioral sequences
            exclusion_list (dict): dict of excluded behaviors
            block_first (bool):

        """

        space = list(space)
        perm_sequences = []

        for seq in sequences:

            if block_first:
                newseq = [seq[0]]
                element = seq[0]
            else:
                newseq = []
                element = ""

            for c in seq[int(block_first):len(seq) - int(block_last)]:

                if element in exclusion_list:
                    lspazio3 = list(space)
                    # remove element that are not permitted
                    for i in exclusion_list[element]:
                        # remove all excluded behaviors
                        lspazio3 = list([x for x in lspazio3 if x != i])

                    lspazio2 = list(lspazio3)
                else:
                    lspazio2 = list(space)

                if lspazio2:
                    new_element = random.choice(lspazio2)

                    # remove extracted behavior
                    space.remove(new_element)

                else:
                    return []

                # check penultimate element
                if block_last and len(newseq) == len(seq) - 2:   # DO NOT REPEAT LAST BEHAVIOUR

                    while (new_element in exclusion_list) and (seq[-1] in exclusion_list[new_element]):
                        if lspazio2:
                            new_element = random.choice(lspazio2)
                        else:
                            return []

                        # remove last behaviour choosen and last behaviour from original string
                        lspazio2 = list(space)

                        if element in lspazio2:
                            lspazio2 = list([x for x in lspazio2 if x != element])

                        if seq[-1] in lspazio2:
                            lspazio2 = list([x for x in lspazio2 if x != seq[-1]])

                newseq.append(new_element)
                element = new_element

            if block_last:
                newseq += seq[-1]

            perm_sequences.append(newseq)

        return perm_sequences


    space = []
    for sequence in sequences:
        space += sequence[int(block_first):len(sequence) - int(block_last)]

    # modifiy exclusions list to avoid repetitions
    if no_repetition:
        for behavior in behaviours:
            if behavior not in exclusion_list:
                exclusion_list[behavior] = []
            if behavior not in exclusion_list[behavior]:
                exclusion_list[behavior].append(behavior)

    count, count_tot = 0, 0

    results = np.zeros((len(behaviours), len(behaviours)))

    while True:

        permuted_sequences = strings_permutation(space, sequences, exclusion_list, block_first, block_last)

        count_tot += 1

        if permuted_sequences:
            count += 1

            # analysis
            permuted_transitions_matrix = np.zeros((len(behaviours), len(behaviours)))

            for seq in permuted_sequences:
                for i in range(len(seq) - 1):
                    '''if seq[i] in behaviours and seq[i + 1] in behaviours:'''
                    permuted_transitions_matrix[behaviours.index(seq[i]), behaviours.index(seq[i + 1])] += 1

            results = results + (permuted_transitions_matrix >= observed_matrix)

        if count == nrandom:
            break

    return count_tot, results


def main():

    parser = argparse.ArgumentParser(description="Behatrix command line utility")
    parser.add_argument("-v", action="store_true", dest='version', help='Behatrix version')
    parser.add_argument("--strings", action="store", dest='strings', help='Path of file containing behavioral strings')

    parser.add_argument("--output", action="store", dest='output', help='Path of output files')
    parser.add_argument("--exclusions", action="store", dest='exclusions', help='Path of file containing exclusions')
    parser.add_argument("--n_random", action="store", dest='nrandom', help='Number of permutations', type=int, default=0)
    parser.add_argument("--n_cpu", action="store", dest='n_cpu', help='Number of CPU to use for permutations test', type=int, default=0)
    parser.add_argument("--block_first", action="store_true", dest='block_first', help='block first behavior during permutations test')
    parser.add_argument("--block_last", action="store_true", dest='block_last', help='block last behavior during permutations test')
    parser.add_argument("--no_repetition", action="store_true", dest='no_repetition', help='exclude repetitions during permutations test')

    parser.add_argument("--quiet", action="store_true", dest='quiet', default=False, help='Do not print results on terminal')

    args = parser.parse_args()

    if args.version:
        print("version {} - {}".format(version.__version__, version.__version_date__))
        sys.exit()

    if not args.strings:
        print("The 'strings' argument is required\n")
        parser.print_usage()
        print()
        sys.exit()
    else:
        if not os.path.isfile(args.strings):
            print("{} is not a file\n".format(args.strings))
            sys.exit()

    with open(args.strings) as f_in:
        behav_str = f_in.read()

    (return_code, sequences,
     unique_transitions, nodes, starting_nodes, tot_nodes,
     tot_trans, tot_trans_after_node, behaviours) = behav_strings_stats(behav_str, chunk=0)


    if args.nrandom:
        nrandom = args.nrandom
    else:
        nrandom = 0

    if nrandom:

        if args.exclusions:
            if not os.path.isfile(args.exclusions):
                print("{} is not a file\n".format(args.exclusions))
                sys.exit()
            else:
                with open(args.exclusions) as f_in:
                    exclusion_str = f_in.read()
        else:
            exclusion_str = ""

        result = check_exclusion_list(exclusion_str, sequences)
        if not result["error_code"]:
            exclusion_list = result["exclusion_list"]
        else:
            print(result["message"])
            return

        block_first = 1 if args.block_first else 0
        block_last = 1 if args.block_last else 0


    if not args.quiet:

        print("\nBehaviours list:\n================\n{}\n".format("\n".join(behaviours)))

        print("Statistics\n==========")
        print('Number of different behaviours: {}'.format(len(behaviours)))
        print('Total number of behaviours: {}'.format(tot_nodes))
        print('Number of different transitions: {}'.format(len(unique_transitions)))
        print('Total number of transitions: {}'.format(tot_trans))

        print('\nBehaviours frequencies:\n=======================')

        for behaviour in sorted(behaviours):
            countBehaviour = 0
            for seq in sequences:
                countBehaviour += seq.count(behaviour)

            print("{behaviour}\t{freq:.3f}\t{countBehaviour} / {tot_nodes}".format(behaviour=behaviour,
                                                                                   freq=countBehaviour / tot_nodes,
                                                                                   countBehaviour=countBehaviour,
                                                                                   tot_nodes=tot_nodes))

    observed_matrix = create_observed_transition_matrix(sequences, behaviours)

    if not args.quiet:
        print("\nObserved transition matrix:\n===========================\n{}".format(observed_matrix))

    if args.output:
        file_name = '{fileName}.observed_transitions.tsv'.format(fileName=args.output)
    else:
        file_name = '{fileName}.observed_transitions.tsv'.format(fileName=args.strings)

    np.savetxt(file_name, observed_matrix, fmt='%d', delimiter='\t')


    with open(file_name, mode="r", encoding="utf-8") as f_in:
        rows = f_in.readlines()

    with open(file_name, mode="w", encoding="utf-8") as f_out:
        f_out.write('\t' + '\t'.join(behaviours) + '\n')
        c = 0
        for row in rows:
            f_out.write((behaviours)[c] + '\t' + row)
            c += 1


    if nrandom:

        if args.n_cpu:
            num_proc = args.n_cpu
        else:
            num_available_proc = os.cpu_count()
            if num_available_proc <= 2:
                num_proc = 1
            else:
                num_proc = num_available_proc - 1

        results = np.zeros((len(behaviours), len(behaviours)))
        with concurrent.futures.ProcessPoolExecutor() as executor:
            lst = []
            n_required_randomizations = 0
            for i in range(num_proc):

                if i < num_proc - 1:
                    n_random_by_proc = nrandom // num_proc
                else:
                    n_random_by_proc = nrandom - n_required_randomizations

                lst.append(executor.submit(permutations_test,
                                           n_random_by_proc,
                                           sequences, behaviours,
                                           exclusion_list,
                                           block_first,
                                           block_last,
                                           observed_matrix,
                                           args.no_repetition))

                n_required_randomizations += n_random_by_proc

            print("\nnumber of required randomizations: ", n_required_randomizations)

            nb_randomization_done = 0

            for l in lst:
                nb_randomization_done += l.result()[0]
                results += l.result()[1]


        print("Number of done randomizations: {}".format(nb_randomization_done))

        if not args.quiet:
            print("\nRandomized transition matrix:\n===========================\n{}".format(results / nrandom))

        if args.output:
            file_name = '{fileName}.randomized_transitions.{nrandom}.tsv'.format(fileName=args.output, nrandom=nrandom)
        else:
            file_name = '{fileName}.randomized_transitions.{nrandom}.tsv'.format(fileName=args.strings, nrandom=nrandom)

        np.savetxt(file_name, results / nrandom, fmt='%f', delimiter='\t')

        with open(file_name, mode='r', encoding='utf-8') as f:
            rows = f.readlines()

        with open(file_name, mode='w', encoding='utf-8') as f:
            f.write('\t' + '\t'.join(list(behaviours)) + '\n')
            c = 0
            for row in rows:
                f.write((behaviours)[c] + "\t" + row)
                c += 1



if __name__ == '__main__':
    main()
