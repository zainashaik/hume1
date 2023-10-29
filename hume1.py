from hume import HumeBatchClient
from hume.models.config import FaceConfig

client = HumeBatchClient("p5hIRUVXHGy3QbOJYBDqh153XCPIFlT7ScbmZ97auTRD36yy")
urls1 = ["https://hume-tutorials.s3.amazonaws.com/faces.zip"]
config = FaceConfig()
job = client.submit_job(urls1, [config])

print(job)
print("Running...")

details = job.await_complete()
job.download_predictions("predictions1.json")
print("Predictions downloaded to predictions.json")