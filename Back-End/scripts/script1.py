import subprocess
import sys
import os
import argparse
import json
from img_valid import valid_img
from ocrolib.common import glob_all

parser=argparse.ArgumentParser(description='Starts chain of script execution for image processing')
parser.add_argument('files',nargs='+')
parser.add_argument('--threshold',type=float,default=0.2,
                    help='baseline threshold, default: %(default)s')
parser.add_argument('--minscale',type=float,default=12.0,
                    help='minimum scale permitted, default: %(default)s')
parser.add_argument('--usegauss',action='store_true',
                    help='use gaussian instead of uniform, default: %(default)s')
parser.add_argument('--maxcolseps',type=int,default=3,
                    help='maximum # whitespace column separators, default: %(default)s')
args=parser.parse_args()
args.files= glob_all(args.files)

#file = open("./../processed-images/" + sys.argv[1] + ".json" , "w+")
# file.write('{"info":"data about image"}')
# file.close();


def print_retcode(retcode):
    '''Prints code returned by script execution'''

    if retcode < 0:
        print("Child was terminated by signal %d"%(-retcode))
    else:
        print("Child returned %d"%(retcode))

def create_exec_string(step):
    '''
    Creates a string containing the script to be executed with specific parameters
    step = 1 => first script to be executed (ocropus-nlbin)
    step = 2 => second script to be executed (ocropus-gpageseg)
    '''
    output_folder = 'temp_files'

    if step == 1:
        ''' ocropus-nlbin -n -t 0.5 -z 0.5 -e 1.0 -b 0.1 -p 80 -r 20 -m 2 --lo 5 --hi 90 --skewsteps 8 -o \'output\' '''
        input_path = args.files
        exec_string = './ocropus-nlbin '
        if type(input_path) == list:
            for file in input_path:
                if valid_img(file):
                    exec_string += file + ' '
                else:
                    return False
        else:
            if valid_img(input_path):
                exec_string += input_path + ' '
            else:
                return False

    elif step == 2:
        ''' ocropus-gpageseg -n --minscale 12.0 --maxlines 300 --scale 0 --hscale 1.0 --vscale 1.0 --threshold 0.2 --noise 8 --usegauss False \
        --maxseps 0 --sepwiden 10 --maxcolseps 3 --csminheight 10 --gray False -p pdb'''
        input_path = output_folder+'/????.bin.png '
        exec_string = 'python ./ocropus-gpageseg '
        exec_string += input_path + ' '


    exec_string += '-n' + ' '
    if step == 1:
        exec_string += '-o ' + output_folder
    elif step == 2:
        exec_string += '--minscale %.1f '%(args.minscale)
        exec_string += '--threshold %.1f '%(args.threshold)
        if args.usegauss:
            exec_string += '--usegauss '
        exec_string += '--maxcolseps %d '%(args.maxcolseps)

    return exec_string

try:
    retcode = subprocess.call('rm -r temp_files/*',shell=True)
except Exception as e:
    pass
try:
    exec_string = create_exec_string(1)
    if not exec_string:
        raise Exception('Invalid file')
    retcode = subprocess.call(exec_string,shell=True)
    #print_retcode(retcode)
    retcode=0
    if retcode == 0:
        exec_string = create_exec_string(2)
        #prelucrare
        retcode = subprocess.call(exec_string,shell=True)

        coordinates_file = open('column_indexes.txt','r')
        coordinates_line = coordinates_file.readlines()
        coordinates_file.close()
        data=dict()
        data['columns']=[]
        data['others']=[]
        data_type=0
        for coordinates in coordinates_line :
            coordinates=coordinates.strip('\n').split(' ')
            # print(coordinates)
            coordinates=[int(coordinates[0]),int(coordinates[1]),int(coordinates[2]),int(coordinates[3])]
            data['columns'].append(coordinates)
            # elif data_type != 0:
            #     data['others'].append(coordinates)
        json_data = json.dumps(data)

        try:
            file_name=os.path.basename(sys.argv[1])
            file = open("./../processed-images/" + file_name.split('.')[0]+ ".json" , "w")
            file.write(json_data)
            file.close();
        except Exception as e:
            print(e)
            # print_retcode(retcode)

except OSError as e:
    print("Execution failed: "+ e)
