class BaseDataLoader(object):
    """
    Nonuse torch.utils.data
    """
    def __init__(self, filename, batch_size, shuffle, logger):
        """
        Initialization data file path, batch data size, shuffle data
        Read data from data file
        Preprocess the data
        Spilt the data according to batch_size
        """
        pass
    def __len__(self):
        """
        How many batch
        """
        raise NotImplementedError
    def __getitem__(self, index):
        """
        Return batch_size data pairs
        """
        raise NotImplementedError
    def __read_data(self,):
        pass
    def __preprocess_data(self,):
        pass