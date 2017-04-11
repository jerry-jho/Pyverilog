import platform
import os
_this_path_ = os.path.realpath(os.path.dirname(__file__))
os.environ['IVERILOG'] = os.path.realpath(_this_path_ + '/verilog/' + platform.system() + '/bin/iverilog -B ' + _this_path_ + '/verilog/' + platform.system() + '/lib/ivl')
#os.environ['IVERILOG'] = os.path.realpath('C:/iverilog/bin/iverilog.exe')
