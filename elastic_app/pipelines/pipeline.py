import bspump
import bspump.trigger
import bspump.common
import bspump.elasticsearch

from .generators import SampleGenerator

class SamplePipeline(bspump.Pipeline):

		def __init__(self, app, pipeline_id):
			super().__init__(app, pipeline_id)

			self.Svc = app.get_service("bspump.PumpService")
			app.PubSub.subscribe("Application.tick!", example)
			self.MyInternalSource = self.Svc.locate("SamplePipeline2.*InternalSource")
			print(self.MyInternalSource)

			self.build(
				bspump.elasticsearch.ElasticSearchSource(app, self, "ESConnection1", config={"index": "bs_acs*"}).on(bspump.trigger.PubSubTrigger(app, "Application.run!", pubsub=app.PubSub)),
				#SampleProcessor(app, self),
				SampleGenerator(app, self),
				#bspump.common.PrintProcessor(app, self),
				bspump.common.NullSink(app, self)
			)

def example(message):
	print("Hi")
