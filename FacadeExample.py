class ExternalServiceFacade:
    def __init__(self, service, adapter):
        self.service = service
        self.adapter = adapter

    def get_data(self):
        external_data = self.service.get_data()
        internal_data = self.adapter.map_data_to_internal_format(external_data)
        return internal_data

    def post_data(self, data):
        external_data = self.adapter.map_data_to_external_format(data)
        self.service.post_data(external_data)
