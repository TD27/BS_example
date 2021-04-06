import bspump


class SampleGenerator(bspump.Generator):
	def __init__(self, app, pipeline):
		super().__init__(app, pipeline)

		self.svc = app.get_service("bspump.PumpService")

		self.MyInternalSource = self.svc.locate("SamplePipeline2.*InternalSource")


	async def generate(self, context, event, depth):
		#print(event)
		await self.MyInternalSource.put_async({}, event)
