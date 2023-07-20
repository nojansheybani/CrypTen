import crypten
import torch
from onnx2torch import convert

crypten.init()
torch.set_num_threads(1)

ALICE = 0
BOB = 1

path = "/ms1mv3_r34.onnx"
plaintext_model = convert(path)

dummy_input = torch.empty((1, 3, 112, 112))
private_model = crypten.nn.from_pytorch(plaintext_model, dummy_input)
private_model.encrypt(src=ALICE)
print(plaintext_model)
print("Model successfully encrypted:", private_model.encrypted)