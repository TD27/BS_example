import bspump
import bspump.elasticsearch

from .pipelines.pipeline import SamplePipeline
from .pipelines.pipeline2 import SamplePipeline2

class SampleApp(bspump.BSPumpApplication):

	def __init__(self):
		super().__init__()

		self.Svc = self.get_service("bspump.PumpService")

		self.Svc.add_connection(
			bspump.elasticsearch.ElasticSearchConnection(self, "ESConnection2", config={
				"bulk_out_max_size": 100,
				'url': 'http://localhost:9200',
			}))
		self.Svc.add_connection(
			bspump.elasticsearch.ElasticSearchConnection(self, "ESConnection1", config={
				"bulk_out_max_size": 100,
				'url': 'http://localhost:3343',
			}))

		self.Svc.add_pipeline(SamplePipeline(self, "SamplePipeline"))
		self.Svc.add_pipeline(SamplePipeline2(self, "SamplePipeline2"))


		self.PubSub.publish("neco!")
