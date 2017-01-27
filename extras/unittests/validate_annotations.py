import json
import os
import logging
from fileoperations.fileoperations import get_filenames_in_dir

logging.basicConfig()  # removes
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def test_metadata():
    """
    This test checks if the MBIDs in annotations.json and ./metadata folder
    are consistent
    """
    anno_mbids = json.load(open('./annotations.json'))
    anno_mbids = set(os.path.split(aa['mbid'])[-1] for aa in anno_mbids)

    meta_mbids = get_filenames_in_dir('./data', keyword='*.json')[2]
    meta_mbids = set(os.path.splitext(mm)[0] for mm in meta_mbids)

    pitch_mbids = get_filenames_in_dir('./data', keyword='*.json')[2]
    pitch_mbids = set(os.path.splitext(mm)[0] for mm in pitch_mbids)

    missing_meta = anno_mbids - meta_mbids
    if missing_meta:
        print("Missing MBIDS in the metadata files in ./data folder. "
              "Please add them!")
        for mm in missing_meta:
            print('   {}'.format(mm))

            assert False, "Mismatch between the MBIDs in annotations.json " \
                          "and the metadata files in ./data folder"

    missing_anno = meta_mbids - anno_mbids
    if missing_anno:
        print("Extra MBIDS in the metadata files in ./data folder. "
              "Please remove them!")
        for ma in missing_anno:
            print('   {}'.format(ma))

            assert False, "Mismatch between the MBIDs in annotations.json " \
                          "and the metadata files in ./data folder"

    missing_pitch = anno_mbids - pitch_mbids
    if missing_pitch:
        print("Missing MBIDS in the pitch files in ./data folder. "
              "Please add them!")
        for mp in missing_pitch:
            print('   {}'.format(mp))

            assert False, "Mismatch between the MBIDs in annotations.json " \
                          "and the pitch files in ./data folder"

    missing_anno = pitch_mbids - anno_mbids
    if missing_anno:
        print("Extra MBIDS in the pitch files in ./data folder. "
              "Please remove them!")
        for ma in missing_anno:
            print('   {}'.format(ma))

            assert False, "Mismatch between the MBIDs in annotations.json " \
                          "and the pitch files in ./data folder"
