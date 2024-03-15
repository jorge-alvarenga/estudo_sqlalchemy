'''from infra.repository.config_circuito_repository import ConfigCircuitoRepository


repo = ConfigCircuitoRepository()
repo.insert(Contrato='Tste',Circuito='P1-MQA3',EndPoint='teste',SecretCompress='teste',ReconnectTime= '180',isActive=True)
'''

import database_count

repo = database_count.ConfigCircuitoRepository()
repo.insert(circuito="P1-MQA3-CH0",dt_insert='19/04/1988',camera_id='1',bound_box="[198,166,122]",count=1,upload=False)

print('teste')