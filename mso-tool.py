#!/usr/bin/env python3

import os
import time
import subprocess
import sys
from os import listdir
import os.path, subprocess
from subprocess import STDOUT,PIPE
from subprocess import check_output
import argparse

class ActionRunToComplete(argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):
       # print(values)
        BuildAllocationGame(values)
        SolveMSO(values[-1])
        ComputeShapleyValues([values[0], values[-1]])

        """ print('Here I am, setting the ' \
             'values %r for the %r option...' % (values, option_string))  """
        setattr(namespace, self.dest, values)

class ActionBuildAllocation(argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):
       # print(values)
        BuildAllocationGame(values)
        """ print('Here I am, setting the ' \
             'values %r for the %r option...' % (values, option_string))  """
        setattr(namespace, self.dest, values)

class ActionSolveMSO(argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):
       # print(values)
        SolveMSO(values[0])
        """ print('Here I am, setting the ' \
             'values %r for the %r option...' % (values, option_string))  """
        setattr(namespace, self.dest, values)

class ActionComputeSV(argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):
        ComputeShapleyValues(values)
        """ print('Here I am, setting the ' \
             'values %r for the %r option...' % (values, option_string))  """
        setattr(namespace, self.dest, values)



def BuildAllocationGame(values):
    outdir = values[0]
    res = values[1]
    val = values[2]
    pub = values[3]
    try:        
	ans = check_output(['java', '-cp', 'ShapleyMSO.jar:commons-io-2.5.jar', "testparser.LedaNewParser", outdir, res, val, pub])
        #java -cp ShapleyMSO.jar:commons-io-2.5.jar testparser.LedaNewParser "/home/sequoia/out" "roma30res.csv" "roma30val.csv" "roma30expectedpub.csv"
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
    #stdout,stderr = proc.communicate(stdin)
    solution = ans.decode("utf8")
    print(solution)


def ComputeShapleyValues(values):
    print(values)
    outdir = values[0]
    instance = values[1]
    os.chdir("/home/")
    try:
        ans = check_output(['java', '-cp', '.:ShapleyMSO.jar:commons-io-2.5.jar', "sequoia.banzaf.ShapleyMSO", outdir, instance])

    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
    #stdout,stderr = proc.communicate(stdin)
    solution = ans.decode("utf8")
    print(solution)


def SolveMSO(instance):

    os.environ['SEQUOIA'] = "/home/sequoia"

    os.environ['LD_LIBRARY_PATH'] = os.environ['SEQUOIA'] + "/src/.libs/:.:/lib/"

    sequoia_home = os.path.expandvars("$SEQUOIA")

    #print("Sequoia home: " + sequoia_home)

    #workspace = "/home/francesco/istanzeAllocation/"+instance
    workspace = sequoia_home+"/out/"+instance

    out_dir = workspace+"/sequoia"

    #print("out_dir: " + out_dir)

    os.system("""rm -rf """+out_dir)

    os.system("""mkdir """+out_dir)

    os.chdir(sequoia_home+"""/src/""")

    #os.system("""cd """+sequoia_home+"""/src/""")

    #os.system(""" ./sequoia -T4 -f f3.mso -e CardCounting -g ../grafo_color_50_BNCMCR66M51H501M_70_I33.leda -c 1000000 """)

    for level in listdir(workspace+"/f1"):
        #print(level)

        if os.path.isdir(workspace+"/f1/"+level):
            for graph in listdir(workspace+"/f1/"+level):
                if graph != ".DS_Store" and "Icon" not in graph and graph != "color":
                    print("Instance: " + graph)
                    graph_path = workspace+"/f1/"+level+"/"+graph
                    start = time.time()
                    proc = subprocess.Popen(["./sequoia -T4 -f ../../fl.mso -e CardCounting -g " + graph_path + " -c 1000000"], stdout=subprocess.PIPE, shell=True)
                    (out, err) = proc.communicate()
                    output = out.decode("utf-8").strip()
                    end = time.time()
                    t = end - start
    #                print(output)
                    if "Solution" not in output:
                        print("Danger, no solution has been found!!!!")
                        print("Errors?",err)
                    else:
                        #print(out_dir+"/"+graph.strip(".leda")+".out")
                        f = open(out_dir+"/"+graph.strip(".leda")+".out","w+")
                        f.write(graph.split(".")[0].split("_")[4]+";")
                        f.write(output[output.find("Solution"):])
                        tempo = "\nExecution time: " + str(t)
                        f.write(tempo)
                        f.close()
                        print("Found solution!")
                        #print(output[output.find("Solution"):])
                    print()



    for level in listdir(workspace+"/f2"):
        #print(level)

        if os.path.isdir(workspace+"/f2/"+level):
            for graph in listdir(workspace+"/f2/"+level):
                if graph != ".DS_Store" and "Icon" not in graph and graph != "color":
                    print("Instance: " + graph)
                    graph_path = workspace+"/f2/"+level+"/"+graph
                    start = time.time()
                    proc = subprocess.Popen(["./sequoia -T4 -f ../../fl.mso -e CardCounting -g " + graph_path + " -c 1000000"], stdout=subprocess.PIPE, shell=True)
                    (out, err) = proc.communicate()
                    end = time.time()
                    t = end - start
                    output = out.decode("utf-8").strip()
    #                print(output)
                    if "Solution" not in output:
                        print("Danger, no solution has been found!!!!")
                        print("Errors?",err)
                    else:
                        #print(out_dir+"/"+graph.strip(".leda")+".out")
                        f = open(out_dir+"/"+graph.strip(".leda")+".out","w+")
                        f.write(graph.split(".")[0].split("_")[4]+";")
                        f.write(output[output.find("Solution"):])
                        tempo = "\nExecution time: " + str(t)
                        f.write(tempo)
                        f.close()
                        #print(output[output.find("Solution"):])
 	
			print("Found solution!")
                    print()

if __name__ == '__main__':

    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('-b', nargs='+', action=ActionBuildAllocation)
    my_parser.add_argument('-c', nargs='+', action=ActionComputeSV)
    my_parser.add_argument('-s', nargs=1, action=ActionSolveMSO)
    my_parser.add_argument('-a', nargs='+', action=ActionRunToComplete)

    args = my_parser.parse_args()

