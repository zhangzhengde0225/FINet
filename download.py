"""
this script used to download and unzip the datasets, and trainging logs and weights
"""

import os, sys
import argparse
from hai_api import hai



class FINetDownload(object):
    def __init__(self) -> None:
        self.uaii = hai.UAII()
        pass

    
    def __call__(self, opt):
        name = opt.name
        assert name in ['SFID', 'logs'], f'Invalid name: {name} to download'
        if name == 'SFID':
            self.download_dataset(save_dir=opt.save_dir)
        elif name == 'logs':
            self.download_logs()

    def download_dataset(self, name='SFID', version='latest', save_dir='.'):
        
        # dowload datasets
        # os.system(f'hai dataset')
        save_dir = os.path.join(save_dir, 'data')
        f_path, success = self.uaii.download_dataset(
            name=name, 
            version=version,
            extract=True,
            save_dir=save_dir,
            )
        

    def download_logs(self):
        # download logs
        url = "https://ihepbox.ihep.ac.cn/ihepbox/index.php/s/0tZtSS5sp0tnqAN/download"
        md5 = None
        fname = "runs.zip"
        
        f_path, success = hai.general.get_file(
            origin=url,
             fname=fname,
             file_hash=md5,
             datadir='.',
             hash_algorithm='md5',
             extract=True,
             force_download=False,
             archive_format='auto'
        )

        pass

    def set_envs(self):
        # set envs
        pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('name', type=str, default='SFID', help='dataset name')
    parser.add_argument('--save-dir', type=str, default='.', help='save directory')
    opt = parser.parse_args()

    finetd = FINetDownload()

    finetd(opt)

    