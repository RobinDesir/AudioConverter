#! /usr/bin/env python
#
# -*- coding: utf-8 -*-

from os import getcwd


def init():
    global original_extension
    global new_extension
    global bitrate
    global logerr_file
    global check_files
    global path_to_folder
    
    global dir_to_create
    global new_folder
    
    global nb_converted_file
    global nb_files
    global file_converted

    global queue_dir
    global queue_file

    global files_to_convert
    global files_to_check

    global files_not_converted
    global nb_files_not_converted

    global skip_folder
    
    original_extension     = ""               # Must not be null
    new_extension          = ""               # Optional, default : mp3
    bitrate                = ""               # Optional, default : 128k
    logerr_file            = "logerr.txt"
    check_files            = False
    path_to_folder         = getcwd()         # Optional, default is the current folder
    dir_to_create          = ""
    new_folder             = None
    
    nb_converted_file      = 0
    nb_files               = 0
    file_converted         = 0
    
    files_not_converted    = []
    nb_files_not_converted = 0
    
    queue_dir              = ""
    queue_file             = ""
    
    files_to_convert       = []
    files_to_check         = []
    
    skip_folder            = False