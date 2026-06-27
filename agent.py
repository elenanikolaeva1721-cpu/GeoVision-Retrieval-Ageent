
import numpy as np
from PIL import Image
import torch
import numpy as np
from torchvision import models, transforms
from sklearn.metrics.pairwise import cosine_similarity
import torch
from torchvision import models

model = models.resnet18(weights=None)
state = torch.load("weights/resnet18-f37072fd.pth",map_location="cpu")
model.load_state_dict(state)
model.eval()
#print("OK")
  
class GeoVisionAgent:

    def __init__(self):
        self.embeddings = np.load("embeddings.npy")
        print("embeddings shape:", self.embeddings.shape)
        print("embeddings size:", self.embeddings.size)

        self.labels = np.load("labels.npy", allow_pickle=True)
        self.paths = np.load("paths.npy", allow_pickle=True)

        #model = models.resnet18(pretrained=True)
        
        #model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
        self.model = torch.nn.Sequential(*list(model.children())[:-1])
        self.model.eval()

        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor()
        ])

    def embed(self, img):
        img = img.convert("RGB")  # 

        x = self.transform(img).unsqueeze(0)

        with torch.no_grad():
             emb = self.model(x).squeeze().numpy().flatten()

        return emb
    
       
    def query(self, img):
        emb = self.embed(img)


        print(np.array(self.embeddings).shape)
        sims = cosine_similarity([emb], self.embeddings)[0]

        top_idx = np.argsort(sims)[-5:][::-1]

        results = []

        for i in top_idx:
            results.append({
                "label": self.labels[i],
                "path": self.paths[i],
                "score": float(sims[i])
            })

        return results

    def interpret_results(self, results):

        top = results[0]
        score = top["score"]

        if score >= 0.85:
            confidence = "High"
        elif score >= 0.75:
            confidence = "Medium"
        else:
            confidence = "Low"

        labels = [r["label"] for r in results[:5]]

        forest_like = [
            "Forest",
            "HerbaceousVegetation",
            "Pasture"
        ]

        if sum(label in forest_like for label in labels) >= 3:

            summary = (
                "The image appears to represent a vegetation-rich region."
            )

        elif "Industrial" in labels[:2]:

            summary = (
                "The image appears to contain industrial or human-made infrastructure."
            )

        elif "River" in labels[:2]:

            summary = (
                "The image appears to contain a water-related landscape."
            )

        else:

            summary = (
                "The scene contains mixed visual patterns and may belong to multiple categories."
            )

        return {
            "prediction": top["label"],
            "confidence": confidence,
            "summary": summary,
            "score": score
        }
 
