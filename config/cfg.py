import os
import json
import torch
import argparse
from config.logger import Logger

class Config(object):
    def __init__(self):
        self.logger = Logger()
        self.config = None
        
    def save_config(self, path):
        with open(path, 'w') as f:
            json.dump(self.config, f, indent=2)
        self.logger.debug("Config saved to file {}".format(path))

    def load_config(self, path, verbose=True):
        with open(path) as f:
            self.config = json.load(f)

        self.logger.debug("Config loaded from file {}".format(path))

    def print_config(self):
        debug = "Running with the following configs:\n"
        for k,v in self.config.items():
            debug += "\t{} : {}\n".format(k, str(v))
        self.logger.debug("\n" + debug + "\n")

    def args2config(self):
        parser = argparse.ArgumentParser()
        # dataset parameter
        parser.add_argument('--data_dir', type=str, default='dataset/')
        
        # model parameter
        parser.add_argument('--h_dim', type=int, default=200) 

        # Loss function and Optimizer parameter
        parser.add_argument('---lr', type=float, default=0.5)
        parser.add_argument('--optimizer', choices=['sgd', 'adagrad', 'adam', 'adamax'], default='sgd', help='Optimizer: sgd, adagrad, adam or adamax.')

        # train parameter
        parser.add_argument('--batch_size', type=int, default=32)
        parser.add_argument('--epochs', type=int, default=100)
        parser.add_argument('--save_dir', type=str, default='./saved_models')
        parser.add_argument('--id', type=str, default='00', help='Model ID under which to save models.')
        parser.add_argument('--save_epochs', type=int, default=5, help='Save model checkpoints every k epochs.')
        parser.add_argument('--monitor', type=str, default='off', help='configuration to monitor model performance and save best')
        
        # other
        parser.add_argument('--cuda', type=bool, default=torch.cuda.is_available())
        parser.add_argument('--config_file', type=str, default='./config.json')
        
        args = parser.parse_args()
        self.config = vars(args)
        # self.print_config()
        # self.save_config(self.config['config_file'])