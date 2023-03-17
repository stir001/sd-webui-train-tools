# -*- coding: UTF-8 -*-

import os
import glob
from liasece_sd_webui_train_tools.util import *

save_project_path = os.path.join("outputs", "train_tools", "projects")

# list all projects in the save_project_path
def load_project_list() -> list:
    res = []
    for path in glob.iglob(str(save_project_path)+"/*", recursive=True):
        if os.path.isdir(path):
            printD("load_project_list:", path)
            res.append(os.path.basename(path))
    return res

def get_project_path(project: str) -> str:
    if project == "":
        return ""
    return str(os.path.join(str(save_project_path), str(project)))

def get_project_version_root_path(project: str) -> str:
    project_path = get_project_path(project)
    if project_path == "":
        return ""
    return str(os.path.join(project_path, "versions"))

def get_project_version_path(project: str, version: str) -> str:
    version_root_path = get_project_version_root_path(project)
    if version == "":
        return ""
    return str(os.path.join(version_root_path, str(version)))

def get_project_version_dataset_path(project: str, version: str) -> str:
    project_version_path = get_project_version_path(project, version)
    if project_version_path == "":
        return ""
    return str(os.path.join(str(project_version_path), "dataset"))

def get_project_version_dataset_origin_path(project: str, version: str) -> str:
    project_version_dataset_path = get_project_version_dataset_path(project, version)
    if project_version_dataset_path == "":
        return ""
    return str(os.path.join(str(project_version_dataset_path), "origin"))

def get_project_version_dataset_processed_path(project: str, version: str) -> str:
    project_version_dataset_path = get_project_version_dataset_path(project, version)
    if project_version_dataset_path == "":
        return ""
    return str(os.path.join(str(project_version_dataset_path), "processed"))

def get_project_version_checkpoint_path(project: str, version: str) -> str:
    project_version_path = get_project_version_path(project, version)
    if project_version_path == "":
        return ""
    return str(os.path.join(str(project_version_path), "checkpoint"))

# list all projects in the save_project_path
def load_project_list() -> list:
    tmp = []
    for path in glob.iglob(str(save_project_path)+"/*", recursive=True):
        if os.path.isdir(path):
            printD("load_project_list:", path)
            tmp.append((os.path.basename(path), os.path.getctime(path)))
    tmp = sorted([x for x in tmp], key=lambda x: x[1], reverse=True)
    return [x[0] for x in tmp]

# list all projects in the save_project_path
def load_project_version_list(project: str) -> list:
    from_path = get_project_version_root_path(project)
    if from_path == "":
        return []
    tmp = []
    for path in glob.iglob(from_path+"/*", recursive=True):
        if os.path.isdir(path):
            printD("load_project_version_list:", path)
            tmp.append((os.path.basename(path), os.path.getctime(path)))
    tmp1 = sorted([x for x in tmp], key=lambda x: x[1], reverse=True)
    return [x[0] for x in tmp]