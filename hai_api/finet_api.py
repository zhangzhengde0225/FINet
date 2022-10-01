
import os, sys
from pathlib import Path

import hai
from hai import AbstractModule, AbstractInput, AbstractOutput, AbstractQue
from hai import MODULES, SCRIPTS, IOS, Config

pydir = Path(os.path.abspath(__file__)).parent  # current directory path of this file

from . import finet_configs
from .finet_configs import hyp
from FINet.train import run as run_train
from FINet.test import run as run_test


@MODULES.register()
class FINet(AbstractModule):
    name = 'FINet'  # Specify the name of your model explicitly
    description = '2022 Foggy Insulator Detection Network'  # Specify the description of your model

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """
        Please set the default train/eval/infer configurations of your model here
        """
        self._train_cfg = finet_configs.get_train_config()
        self._infer_cfg = finet_configs.get_inference_config()    
        self._eval_cfg = finet_configs.get_evaluate_config()
        self._mapping = finet_configs.mapping()
        # self.mapping must be None or a dict, in which the key is the unified HAI config name, and the value is the original config name


        # self.config.merge(hyp)
        # The default config can be a dict, json, yaml, a python config file or a config object from argparse
        # and it will be converted to a Config object automatically by the framework
        
    
    def _init_model(self):
        """
        Please implement your model initialization here
        return: model
        """
        raise NotImplementedError(f'{self.name}._init_model() is not implemented, plese check the api: "{self.__module__}"')

    def train(self, *args, **kwargs):
        """
        Please implement your model training here
        for example:
            run_train(self.mapped_config)
        """
        return run_train(self.mapped_config)
        # raise NotImplementedError(f'{self.name}.train() is not implemented, plese check the api: "{self.__module__}"')

    def infer(self, *args, **kwargs):
        """
        Please implement your model inference here
        """
        raise NotImplementedError(f'{self.name}.infer() is not implemented, plese check the api: "{self.__module__}"')

    def evaluate(self, *args, **kwargs):
        """
        Please implement your model evaluation here
        """
        return run_test(self.config)
        # raise NotImplementedError(f'{self.name}.evaluate() is not implemented, plese check the api: "{self.__module__}"')