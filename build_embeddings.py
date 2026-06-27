import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import os
import numpy as np
from PIL import Image
import torch
from torchvision import models, transforms
#import torch
#from torchvision import models

model = models.resnet18(weights=None)
state = torch.load("weights/resnet18-f37072fd.pth",map_location="cpu")
model.load_state_dict(state)
model.eval()

# --- модель ---
#model = models.resnet18(pretrained=True)
#model = models.resnet18(weights=None)
model = torch.nn.Sequential(*list(model.children())[:-1])
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

def embed_image(img_path):
    img = Image.open(img_path).convert("RGB")
    x = transform(img).unsqueeze(0)

    with torch.no_grad():
        emb = model(x).squeeze().numpy().flatten()

    return emb

data_dir = "data/EuroSAT_RGB"

embeddings = []
labels = []
paths = []

#  ограничиваем для скорости (важно для старого ноутбука)
MAX_PER_CLASS = 30

for cls in os.listdir(data_dir):
    cls_path = os.path.join(data_dir, cls)

    if not os.path.isdir(cls_path):
        continue

    count = 0

    for file in os.listdir(cls_path):
        if count >= MAX_PER_CLASS:
            break

        path = os.path.join(cls_path, file)

        try:
            emb = embed_image(path)
            embeddings.append(emb)
            labels.append(cls)
            paths.append(path)
            count += 1
        except:
            continue

np.save("embeddings.npy", embeddings)
np.save("labels.npy", labels)
np.save("paths.npy", paths)

print("Embeddings created:", len(embeddings))



