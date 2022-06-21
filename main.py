import pytorch_lightning
import yaml

if __name__ == '__main__':
    print("the coolest project ever")

    print(yaml.dump({'coolProject': 'yes'}))

    pytorch_lightning_version = pytorch_lightning.__version__

    print(pytorch_lightning_version)

    print("checkpoint")
