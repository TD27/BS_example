import bspump
import bspump.trigger
import bspump.common
import bspump.elasticsearch

class SamplePipeline2(bspump.Pipeline):

		def __init__(self, app, pipeline_id):
			super().__init__(app, pipeline_id)

			self.Svc = app.get_service("bspump.PumpService")
			#app.PubSub.subscribe("Application.tick!", example)

			self.build(
				bspump.common.InternalSource(app, self),
				#SampleProcessor(app, self),
				#SampleGenerator(app, self),
				bspump.common.PrintProcessor(app, self),
				bspump.elasticsearch.ElasticSearchSink(app, self, "ESConnection2", config={"index": "bs_acs"})
			)

def example(message):
	print("Hi")
