# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6acf94a-c839-3dc4-8f80-b02e9ce993e0 | -8.9041 | -60.5577 | 2026-08-22 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 9b93734a-1690-313f-80c0-85aebaa4549b | -6.5441 | -56.2508 | 2026-08-22 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 3401dffa-efd6-35d7-b6e6-d57dcbfdde3c | -6.9699 | -59.0658 | 2026-08-22 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| dbb030a8-4c97-31ae-9cc1-b602cb92bec7 | -6.0807 | -59.9465 | 2026-08-22 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 62a08af9-8819-3fd4-90b7-8f92a28a6a93 | -9.1722 | -59.4629 | 2026-08-22 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 177.2 |
| 5b1ad9e1-216d-38a5-8a4b-bde9b2ab1b26 | -9.12 | -61.6011 | 2026-08-22 14:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 34fa7a19-dd42-3fee-8a4b-3ff9fe66c88c | -9.6951 | -45.9572 | 2026-08-22 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 4c8a95ea-fb4d-3fb1-8b74-9a8dde2830f7 | -9.1536 | -59.464 | 2026-08-22 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| ddce1b07-d407-37c9-b42d-c570083a8ca9 | -5.9996 | -57.8249 | 2026-08-22 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| c94233cb-9d5d-36c2-84b4-c2ce2571124b | -6.3469 | -58.3361 | 2026-08-22 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 5ba05354-78e4-376e-8a2f-d888d5c2fda0 | -8.4088 | -62.6956 | 2026-08-22 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 77b7c196-1c83-3d82-8698-7ce52031f85e | -6.8569 | -59.4564 | 2026-08-22 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 126.1 |
| eeb8f46b-2c36-3ba7-aaa7-97cc2d81439b | -8.3904 | -62.6774 | 2026-08-22 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 213f489f-6123-3c36-b9b1-1c59b037975d | -6.254 | -55.391 | 2026-08-22 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 202.0 |
| 45a45014-a1c0-3e02-ad55-d1965ff5794c | -6.8569 | -59.4564 | 2026-08-22 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 146.0 |
| ed583a77-c587-3e8c-95fd-6786fa66e9e7 | -6.857 | -59.4371 | 2026-08-22 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.0 |
| d44a04ad-e020-3163-b1c3-9b617784474e | -6.8042 | -58.9954 | 2026-08-22 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 886032a6-f955-32bf-8358-555184f27bdf | -9.0536 | -60.435 | 2026-08-22 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| a1b26b3d-1534-39d6-a48d-d374ca1add89 | -6.5441 | -56.2508 | 2026-08-22 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 0c714a1b-16e9-3aae-8da2-41fea9fc6e77 | -10.9624 | -51.4214 | 2026-08-22 14:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 37ea5432-d17b-30cf-8564-d0de090803ac | -6.9499 | -59.3177 | 2026-08-22 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.1 |
| c7092866-7cdd-31ac-988e-b66ab2e2922a | -11.3475 | -46.0203 | 2026-08-22 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 168.4 |
| a5faa814-4936-3dbb-aa5b-ec450dad79af | -9.4744 | -48.2917 | 2026-08-22 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| d89d4fbe-17f6-3959-b5ad-66c1aed91772 | -6.6197 | -53.378 | 2026-08-22 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 002257e9-dac9-3e9f-a9d6-5d5af8f57d9e | -9.1909 | -59.4619 | 2026-08-22 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 104.5 |
| abe06e78-2822-3b20-98ac-b4d5d879de17 | -5.9996 | -57.8249 | 2026-08-22 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 88b46943-2232-3339-97da-5cb79d567145 | -13.9967 | -53.7062 | 2026-08-22 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 6c2dd8c6-ed0d-3b2e-bc70-976701f152ad | -6.8991 | -55.7176 | 2026-08-22 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 0c241ba8-89c1-3ec6-937b-a8dcbdecb829 | -6.9314 | -59.3377 | 2026-08-22 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 65845204-d13e-34c1-8b32-f74e63ca358d | -17.5891 | -44.6164 | 2026-08-22 14:30:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 103.1 |
| cd001606-53a4-3ef9-9472-2e735e5ef259 | -8.5216 | -54.8612 | 2026-08-22 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 69fcfc0c-bafa-3816-b702-573eb860ec2a | -11.3472 | -46.0431 | 2026-08-22 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 316.5 |
| 03ae78bc-5f45-30d4-b0f1-84d81ee434bd | -13.9778 | -53.6876 | 2026-08-22 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 167.2 |
| 633283d8-980e-3edc-9eb8-febd5876ccf5 | -8.9041 | -60.5577 | 2026-08-22 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| b7bdbcf1-650a-38c2-bf80-a6d86679f3f4 | -8.9938 | -50.7004 | 2026-08-22 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| e23b0511-d0cd-3338-93d3-57b427c12c76 | -7.344 | -55.6741 | 2026-08-22 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 25a3506f-f063-3f7f-b876-2dd53d089cd0 | -9.191 | -59.4425 | 2026-08-22 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 7bf39d98-5dc6-3176-85c4-56680e7423d3 | -13.997 | -53.6853 | 2026-08-22 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 174.1 |
| 41c46ca2-effe-3573-ad91-387f801c31b4 | -9.106 | -60.9127 | 2026-08-22 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 1aa73170-3a10-394a-b28d-cefd9472a195 | -13.5481 | -51.7403 | 2026-08-22 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| c6b309ba-d52e-3fbb-bde3-d2e45f2f2475 | -6.1285 | -57.8393 | 2026-08-22 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 161.7 |
| 014fdce3-6652-37bf-8e29-45bc819d856d | -6.5439 | -56.2706 | 2026-08-22 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 385bc2c2-c6a8-3bfe-9b4c-d86bb3d9b024 | -16.1279 | -43.6194 | 2026-08-22 14:30:00 | GOES-19 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 406.2 |
| 0eb9bb49-22c5-3cd6-9e04-ed0657240bdf | -6.8043 | -58.9761 | 2026-08-22 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 63dca908-4a36-3da7-b073-2878284605e4 | -8.5408 | -54.7995 | 2026-08-22 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 92b8f636-5c94-3f19-8377-71a962e56904 | -6.9315 | -59.3184 | 2026-08-22 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 136.3 |
| 6150c663-97d0-39bb-9fd4-520266ef2172 | -6.8568 | -59.4757 | 2026-08-22 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 112.3 |
| d0975876-bce9-37cb-94c0-1b24c5ac16e0 | -9.035 | -60.4359 | 2026-08-22 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 2036b53d-6d58-3441-9ebc-f0ca5d203285 | -9.6653 | -48.1187 | 2026-08-22 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| d426f4df-3619-3d96-adff-2ed8396490ad | -9.1201 | -61.582 | 2026-08-22 14:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 64.7 |
| f503d9c1-7afc-33e4-93d8-90a48e4047fb | -6.6195 | -53.3984 | 2026-08-22 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 942f801c-77a7-3344-b4e2-a5be91c84411 | -6.8571 | -59.4179 | 2026-08-22 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 75362ef1-d32d-3f56-bcb4-795a6ae55fa1 | -8.4088 | -62.6956 | 2026-08-22 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 28168f4b-72d5-35e5-ab90-8ce1f8bb863f | -13.9364 | -53.8798 | 2026-08-22 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 86faefb2-9fa4-3726-b766-9dd0655533c4 | -8.5218 | -54.8411 | 2026-08-22 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 147.9 |
| f00d2e82-b2c6-37ec-a597-10e8aa17aee4 | -14.5462 | -53.0527 | 2026-08-22 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 286094fd-6ba5-337b-870c-b2f7705c1ff0 | -11.625 | -46.5484 | 2026-08-22 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 157.7 |
| 1b4f9bdc-56b2-35ff-94dd-4fd75969151a | -10.8842 | -50.2183 | 2026-08-22 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| add20a11-787c-3a9e-86e5-ce477496c99e | -14.4285 | -53.1727 | 2026-08-22 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 60ae12e2-79e3-34f5-a44b-a2419f362369 | -8.5221 | -54.8007 | 2026-08-22 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 3593bfc9-604b-36ac-bdac-0999cfb1402e | -15.361 | -52.9253 | 2026-08-22 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 72f1ab57-d7fa-35d8-8ec4-a1506921e15b | -14.4288 | -53.1516 | 2026-08-22 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| a382caef-579e-3875-aae1-9894b08ae5a1 | -14.4126 | -52.9643 | 2026-08-22 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| b0caae4f-5646-37bf-9587-18d4e4338a7f | -8.4089 | -62.6767 | 2026-08-22 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 86.0 |
| bfeb8e97-7e87-3d5a-b5ad-57cc0801daaf | -17.6855 | -44.738 | 2026-08-22 14:30:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 2aa984ae-6eb5-34cf-b5b3-4b572f8ff2ea | -11.6442 | -46.5458 | 2026-08-22 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 172.9 |
| d6247bcd-b0dd-3c59-b9b1-1b6cf9437f4c | -9.12 | -61.6011 | 2026-08-22 14:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 71.9 |
| eacab145-8a98-395b-9dd2-d5abac67e482 | -10.277 | -50.3886 | 2026-08-22 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| ad1fc85c-6d2e-331b-815d-935f679a2888 | -6.0181 | -57.8047 | 2026-08-22 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| a14954e3-ebb9-3879-89c9-c9bc1fa6a5c2 | -9.0348 | -60.4551 | 2026-08-22 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 144.2 |
| 04a52ce4-fa3e-3371-a7cb-f77e8d39d5d9 | -15.4014 | -52.8352 | 2026-08-22 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 5683870b-72e3-3c3c-af6a-d1f6193d76cb | -11.6059 | -46.551 | 2026-08-22 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 238.3 |
| 6e67d5fe-cef0-356b-a584-b3d82992ef63 | -17.9144 | -44.3976 | 2026-08-22 14:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 13ff7727-eac3-33db-9f57-20a0628ced3d | -9.1724 | -59.4436 | 2026-08-22 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 9fe338b0-8aaa-3c4f-af51-cc70a5389a4a | -8.522 | -54.8209 | 2026-08-22 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 180.1 |
| f7dab2ba-19e6-3d11-ad86-6ac6cec17e2d | -6.8755 | -59.4364 | 2026-08-22 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 6fcd44d5-28fe-3bb0-86fd-46f083e80176 | -13.9973 | -53.6644 | 2026-08-22 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 6022e5ed-1daa-3e34-b488-08e5e7690915 | -11.3667 | -46.0177 | 2026-08-22 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 341.3 |
| 8c2782b1-9ef2-3d55-bf7b-118e91be45bc | -9.6951 | -45.9572 | 2026-08-22 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 165.3 |
| f424da67-e902-37e4-b929-18aef0843e46 | -10.7847 | -50.5706 | 2026-08-22 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 869af94a-a358-3576-9247-36b7276239c9 | -6.97 | -59.0465 | 2026-08-22 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 122.6 |
| 5599a752-7aa7-3a67-a2e8-90365ddc2373 | -10.2584 | -50.3692 | 2026-08-22 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 169.4 |
| d9b3768c-9f16-35e6-8144-0f8884e32d0b | -6.6382 | -53.377 | 2026-08-22 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| fd3f1005-cdce-3f3c-b1ee-8d5ea0a65333 | -6.5302 | -58.5227 | 2026-08-22 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| c55f03dc-847a-3ce1-bc39-d209f7d5427b | -5.9997 | -57.8054 | 2026-08-22 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| f518831a-7f6c-3039-bea9-8442526b2381 | -6.3654 | -58.3354 | 2026-08-22 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 134.8 |
| efc12f1a-d1a7-38eb-aa63-12f9a3811d03 | -8.9042 | -60.5385 | 2026-08-22 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 5a492d57-f4ac-3de9-8916-28245918e028 | -6.8756 | -59.4171 | 2026-08-22 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.7 |
| d1ae9a4a-a46e-3998-8cfa-ae599fea4303 | -9.1722 | -59.4629 | 2026-08-22 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 206.2 |
| 1daecfc4-4d9b-339f-b59c-14a80747658d | -16.1273 | -43.6437 | 2026-08-22 14:30:00 | GOES-19 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 211.9 |
| 82dbb8f5-7571-3bd7-9a97-104f9369079d | -9.0534 | -60.4542 | 2026-08-22 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 00285765-a8dc-33db-9580-d19d16631742 | -15.3415 | -52.928 | 2026-08-22 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| bed59386-c120-3a73-994c-8dbb6d093479 | -11.6254 | -46.5258 | 2026-08-22 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 206.1 |
| 41c0161a-6131-34f1-ade2-52f1d8e284ae | -6.5487 | -58.522 | 2026-08-22 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| d3b50dc4-5d05-3dd8-a037-4a4af8a5264e | -6.9699 | -59.0658 | 2026-08-22 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 95a792a4-6189-3190-89b2-24f0c53b18eb | -7.3625 | -55.673 | 2026-08-22 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 117fbfa6-b1a6-3a74-8b2d-fee3543b9884 | -8.3903 | -62.6963 | 2026-08-22 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 2047baac-e73d-3d59-a52d-ddc6cf4d4a35 | -6.3469 | -58.3361 | 2026-08-22 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 7e2db5f5-18da-380d-aa95-8a549d1ddbcc | -10.2584 | -50.3692 | 2026-08-22 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 4bd04a28-e865-3634-bc77-6d87dfd0e34a | -15.361 | -52.9253 | 2026-08-22 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |


[Clique aqui para ver as próximas entradas](README92.md)
