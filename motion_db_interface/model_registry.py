import os
import importlib


class ModelRegistry:
    sample_methods = dict()
    instance = None
    def __init__(self) -> None:
        self.temp_module_dir = "temp_modules"
        self.dynamic_modules = dict()
    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = ModelRegistry()
        return cls.instance
    
    def load_dynamic_module(self, model_type, module_script):
        if model_type in self.dynamic_modules:
            return
        self.dynamic_modules[model_type] = module_script
        temp_module =self.temp_module_dir+os.sep+model_type
        os.makedirs(self.temp_module_dir, exist_ok=True)
        with open(temp_module + ".py", "wt") as file:
            file.write(module_script)
        importlib.import_module(self.temp_module_dir+"."+model_type)

    @classmethod
    def register_sample_method(cls, name, method):
        cls.sample_methods[name] = method

    def sample_motion_from_model(self, data_type, *args, **kwargs):
        return self.sample_methods[data_type](*args, **kwargs)
    