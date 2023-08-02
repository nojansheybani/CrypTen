import logging
import time

import crypten
import crypten.mpc as mpc
import crypten.communicator as comm
import torch
from examples.meters import AverageMeter
from onnx2torch import convert

crypten.init()
torch.set_num_threads(1)

ALICE = 0
BOB = 1
onnx_model_path = '/ms1mv3_r34.onnx'
torch_model = convert(onnx_model_path)

@mpc.run_multiprocess(world_size=2)
def run():
    dummy_input = torch.empty(1, 3, 112, 112)
    private_model = crypten.nn.from_pytorch(torch_model, dummy_input)
    private_model.encrypt(src=ALICE)
    print("Model successfully encrypted:", private_model.encrypted)

    # # Load data to Bob
    data_enc = crypten.cryptensor(dummy_input, src=BOB)
    private_model.eval()
    output_enc = private_model(data_enc)

    output = output_enc.get_plain_text()
    print(output)

run()