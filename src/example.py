def initialise_logger(output_file:Union[str, bytes, os.PathLike], mode:Optional[str]="both")->None:
    """
    Setup logging to console and file simultanenously. The process is described here:
    Logging to Console and File In Python

    :param output_file: log file to use. Frequently we set this to:
    .. highlight:: python
    .. code-block:: python

            logname = __file__.replace("./", "").replace(".py", "")
            os.path.join("logs", "{}.log".format(logname)) 
        
    :param mode: `both` or `file only` selects whether output is sent to file and console, or file only
    
    :return: No return value
    """
