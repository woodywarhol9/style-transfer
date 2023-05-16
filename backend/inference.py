import numpy as np
import config
import cv2


def inference(model, image):
    """
    입력 이미지와 추론 결과 함께 반환
    """
    model_name = f"{config.MODEL_PATH}/{model}.t7"
    model = cv2.dnn.readNetFromTorch(model_name)

    h, w = map(int, image.shape[:2])
    new_w = int((640 / h) * w)
    resized_img = cv2.resize(image, (new_w, 640), interpolation=cv2.INTER_AREA)
    # 입력 이미지 추론 위해 blob으로 변경
    input_blob = cv2.dnn.blobFromImage(
        resized_img,
        1.0,
        (new_w, 640),
        (103.93, 116.77, 123.68),  # (R, G, B)
        swapRB=False,
        crop=False,
    )
    model.setInput(input_blob)
    output = model.forward()
    # B, C, W, H -> C, W, H
    output = output.reshape(3, output.shape[2], output.shape[3])
    # mean-subtraction 되돌리기
    output[0] += 103.93
    output[1] += 116.77
    output[2] += 123.68
    # W, H, C
    output = output.transpose(1, 2, 0)
    return output, resized_img
