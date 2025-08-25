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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5f16438-9055-3ee2-aac1-33534f29536a | -9.26367 | -59.78431 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| efba0588-0fd9-3f45-8b09-647718e40635 | -12.05978 | -63.14808 | 2025-08-25 01:28:00 | TERRA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0fae4256-83c6-37e7-b42b-aa5532cb2671 | -9.19551 | -59.51287 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 447e76ec-d6b2-359b-9f3a-0c60a5d3d93d | -8.23509 | -61.42968 | 2025-08-25 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 17.4 |
| f7d76d65-5a68-3cfd-9c23-935c54d3f7bd | -9.24973 | -59.62038 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f48cbc54-4e06-3023-92ae-f540a370f6de | -8.89426 | -62.46697 | 2025-08-25 01:28:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 71b8d3d6-1fa6-3847-a93b-f97c1798229d | -7.5313 | -63.81386 | 2025-08-25 01:28:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 51f6e5b5-6b11-39a1-9d7f-ba95ca6cc436 | -9.22885 | -59.67568 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cf992bd1-d7a7-3594-bdec-f0d5261b7eea | -7.91781 | -63.06599 | 2025-08-25 01:28:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| da3102bf-0771-3844-8028-9baa938beb31 | -8.69278 | -62.88043 | 2025-08-25 01:28:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| d4687068-3454-3851-b2d1-3a631814ee40 | -8.87655 | -62.46949 | 2025-08-25 01:28:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b5aedbab-97c7-33b3-a100-ff1342df2feb | -9.17371 | -60.7697 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9d1aaffd-fe40-3a20-926e-79b12d76008d | -8.21932 | -61.39194 | 2025-08-25 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 21.2 |
| e756cb75-e0b0-3f33-af92-3efad8ae9174 | -7.62313 | -62.7326 | 2025-08-25 01:28:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 48e10007-31ea-369c-8de4-29d792adfc45 | -8.99349 | -65.41257 | 2025-08-25 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 314de4b4-7891-3e1b-be74-e20395c8db8d | -8.21806 | -61.38292 | 2025-08-25 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 0c2e050f-184d-3e7f-91fe-c4ea39508a15 | -9.08631 | -65.72238 | 2025-08-25 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 2c120eff-2e5c-33fa-92a7-91a740a2c151 | -9.81133 | -64.27008 | 2025-08-25 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 74945af2-8408-3cc2-9e41-0c00d2a8c1ca | -7.79401 | -61.56964 | 2025-08-25 01:28:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 914ca178-508a-3677-9cfb-9c0e1f29e2b2 | -9.17131 | -60.81716 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 97485464-64a6-38f0-837c-d1e5e8d88658 | -8.97476 | -65.42723 | 2025-08-25 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 07486ac6-6bb6-382e-b151-93f49672465d | -7.6219 | -62.72369 | 2025-08-25 01:28:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 74.6 |
| b1d96cb2-1c01-3dd2-af90-7f9c4de5c2e3 | -8.67372 | -62.87391 | 2025-08-25 01:28:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6853296b-4dff-3861-8bef-2321ca38dec8 | -10.24064 | -59.66121 | 2025-08-25 01:28:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9dc4e520-73a7-3a5b-99f0-9e26f8155025 | -10.41825 | -64.43698 | 2025-08-25 01:28:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 9c54fcbe-fdae-3856-95dd-88066ee46161 | -8.91589 | -62.42745 | 2025-08-25 01:28:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 2acdcf53-0c36-3503-9ba1-f9e2a141d458 | -10.00484 | -67.84779 | 2025-08-25 01:28:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 2c08b447-5b2e-37f9-be60-071f17532688 | -8.88295 | -62.45036 | 2025-08-25 01:28:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 209b6b5c-e344-3500-bd2d-2f88bc117e87 | -8.1217 | -62.8781 | 2025-08-25 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 15.5 |
| d8ab875d-53c8-30a0-beb4-152c3105bf84 | -10.25357 | -59.11708 | 2025-08-25 01:28:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| cdce0978-8bed-397d-909e-d846d485d5de | -8.99503 | -65.42448 | 2025-08-25 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 75cffa91-a184-3e5c-8614-63455e86cb06 | -9.1554 | -62.35698 | 2025-08-25 01:28:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9caf0b45-e416-3023-8921-aee54d1d21a7 | -7.54428 | -63.84092 | 2025-08-25 01:28:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 108170f1-5270-3a3e-9b1d-f44895e63f5a | -9.04645 | -65.74029 | 2025-08-25 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 3770ffce-4f90-37f6-aec0-c9e77764dee6 | -13.1343 | -53.7418 | 2025-08-25 01:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 669c6ce0-3e34-3f22-828d-f56234dbec46 | -5.0992 | -43.2211 | 2025-08-25 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 47.1 |
| fe782791-2a90-3742-9cfa-0f9b381c6364 | -13.1534 | -53.7397 | 2025-08-25 01:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 242.7 |
| 9690cb1e-0c28-3647-8597-0c6b8b06e8fd | -9.6553 | -59.6302 | 2025-08-25 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| a30bbbab-22b1-30df-b7a9-7190366e7732 | -8.8734 | -62.4495 | 2025-08-25 01:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 146.5 |
| 249ca1e5-36c6-33cf-a77e-663f2f5e6b9f | -8.9875 | -65.4006 | 2025-08-25 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 8253a535-2c32-37ae-af1f-546e72c186fe | -9.0246 | -65.3807 | 2025-08-25 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 6a6baa56-ec9e-30bb-b698-211ea85eb556 | -9.0416 | -65.7163 | 2025-08-25 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 33.6 |
| a0dd0ce3-931b-3054-acb8-6cd93d259545 | -5.1181 | -43.1964 | 2025-08-25 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 9ef17be4-4adf-3de4-bc8d-401604ad2afc | -8.9874 | -65.4192 | 2025-08-25 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 188.4 |
| ce653511-2105-3c4a-863e-654e12f82436 | -9.0972 | -65.7145 | 2025-08-25 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 33.4 |
| ac999e7b-0125-3bb5-a4ae-622549ebb60e | -5.0994 | -43.1977 | 2025-08-25 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 5f7496f9-9865-3b07-b257-ce733cb73ac3 | -9.0415 | -65.7349 | 2025-08-25 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 35.1 |
| db3d23ac-c0ae-33d7-98b0-132a310edf5c | -5.118 | -43.2198 | 2025-08-25 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 69539598-4611-3740-bf83-cb034755e845 | -6.8412 | -58.9746 | 2025-08-25 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 8c75d94d-b654-3b70-99d5-1c3d4f1fe745 | -6.823 | -58.9367 | 2025-08-25 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| c787a86a-5b29-39ad-aedc-fbd6bd04e0a0 | -6.8229 | -58.956 | 2025-08-25 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 163.7 |
| 569b76c9-8a2e-3607-8d47-1f51d2973b0f | -9.006 | -65.4 | 2025-08-25 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 059a07c2-4595-3ad0-82bf-3407a8faf30e | -8.8918 | -62.4677 | 2025-08-25 01:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 64.1 |
| d6c86ddc-f331-3972-8425-07b047eaac83 | -6.8413 | -58.9552 | 2025-08-25 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 177.7 |
| 34598674-456f-3169-b4b2-e3f2827e730a | -9.0971 | -65.7332 | 2025-08-25 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 458e0e68-5c7d-3982-a64a-ce10beb976be | -9.1722 | -59.4629 | 2025-08-25 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 8c58a442-5d25-3608-8ebc-09faaa9f72e7 | -22.5518 | -46.8053 | 2025-08-25 01:30:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 98.3 |
| dd6d9114-3c49-398c-9572-87412dbcdb7c | -20.3907 | -46.7384 | 2025-08-25 01:30:00 | GOES-19 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 86.4 |
| e5b6f973-131b-3efa-b70e-fc30d5d84779 | -10.2572 | -59.1081 | 2025-08-25 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 87708142-388a-3930-a416-bcad6b9dd6e6 | -6.8228 | -58.9753 | 2025-08-25 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| f38151ca-d438-34ca-a939-7594c7f8b36e | -7.6326 | -62.7243 | 2025-08-25 01:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| ae1b076c-6000-3207-b14f-2eeee316c1bb | -3.4439 | -49.051 | 2025-08-25 01:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 187b809b-0b9a-3973-a6fe-e48eab9c0182 | -8.5758 | -62.6323 | 2025-08-25 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 117.3 |
| adac8f2b-a76a-3069-b3a5-0df874f08add | -8.9689 | -65.4198 | 2025-08-25 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 3367684c-e34a-397d-a77d-b1dc6d12a2a3 | -13.1537 | -53.7189 | 2025-08-25 01:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 111.9 |
| a035af7a-62e8-32a0-9ad1-579a4ec04a9f | -8.5943 | -62.6315 | 2025-08-25 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 108.9 |
| bad60f82-523e-3586-8ae2-c305ecbf54cb | -8.8733 | -62.4685 | 2025-08-25 01:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 127.8 |
| 1da7750b-c2f8-3f22-abb0-22d8c50c7c1a | -9.1909 | -59.4619 | 2025-08-25 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 336155b6-5b29-315d-868d-12ed76a87087 | -9.0061 | -65.3813 | 2025-08-25 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 5b2cfb41-de4a-3c2e-9536-984c39ffa067 | -6.8414 | -58.9359 | 2025-08-25 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 977a5833-b632-3dae-93b6-b4c5f6000353 | -3.4254 | -49.0517 | 2025-08-25 01:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 783b4bd7-ba32-3199-b241-fcbe8ef5c19c | -9.06 | -65.7344 | 2025-08-25 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 7b9963e5-97c6-39cf-900f-10570a1bcc46 | -8.8919 | -62.4487 | 2025-08-25 01:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 0e60dd79-fd72-3710-a198-d9961967c5bc | -9.0601 | -65.7157 | 2025-08-25 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 30.9 |
| bfd8e936-82e4-3c75-8647-44eae9f259bc | -2.92402 | -53.70566 | 2025-08-25 01:30:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| b3597922-7138-37aa-b345-f0854662f7db | -4.96114 | -55.8289 | 2025-08-25 01:30:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 797b264f-154f-3c9d-913c-35cca6821d5e | -3.83862 | -55.96024 | 2025-08-25 01:30:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| bacab095-4510-3b93-978d-92773f82d6b8 | -5.75442 | -57.58803 | 2025-08-25 01:30:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 633dad86-9a9d-3a7e-b5a1-ae3c185149e7 | -2.9345 | -53.71099 | 2025-08-25 01:30:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| a2ac9b01-a978-332c-b590-e835af431c3c | -3.84472 | -55.96595 | 2025-08-25 01:30:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 6b24aa57-064e-3926-9ce7-d18e5de774f9 | -3.84206 | -55.98261 | 2025-08-25 01:30:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 06a6a42f-a622-3391-9277-88bcb8777ed2 | -5.7487 | -63.1705 | 2025-08-25 01:30:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1a02c75b-781e-3848-a76d-f7599650bc67 | -9.0972 | -65.7145 | 2025-08-25 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 24.3 |
| b62f1d76-28d0-3cfe-becb-fbb5de2af66f | -10.5937 | -44.331 | 2025-08-25 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 8f84c1ae-2ede-383b-99e9-33f53f034cff | -8.8733 | -62.4685 | 2025-08-25 01:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 166.7 |
| c89eb081-b358-3db5-8a58-cd8c6beeff32 | -22.5307 | -46.8109 | 2025-08-25 01:40:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.4 |
| a4162cbb-edbd-3995-8c90-534a3efce33d | -6.8413 | -58.9552 | 2025-08-25 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 0b343421-fd71-36c8-bbc5-38b3ae899b75 | -9.1722 | -59.4629 | 2025-08-25 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 6ca2a098-fdd0-3985-bbeb-ef01020cd0ce | -3.4254 | -49.0517 | 2025-08-25 01:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| d4a66d6a-2694-3aa3-8b77-a4a5f65902db | -9.06 | -65.7344 | 2025-08-25 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 30.6 |
| be86bb3c-59a4-31ca-801b-45db2bbf02b0 | -9.0971 | -65.7332 | 2025-08-25 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 24.2 |
| c77a4ad8-023b-30e4-93fa-7c1683265cfd | -9.0416 | -65.7163 | 2025-08-25 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 3d012b29-1aaf-3af8-a446-73aea3984a0f | -13.1537 | -53.7189 | 2025-08-25 01:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 9be40348-4980-3630-873a-3ce2b0ec1dd3 | -5.0992 | -43.2211 | 2025-08-25 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 0f3c9a9c-775a-374a-a6f5-689112e6d099 | -13.1343 | -53.7418 | 2025-08-25 01:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 67f8101a-abf0-315d-8d6f-746452447096 | -9.0415 | -65.7349 | 2025-08-25 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 932dfdad-b49b-3e6d-8e27-80fbd850e10f | -22.5518 | -46.8053 | 2025-08-25 01:40:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 139.3 |
| 66da3054-ec3f-38ea-a332-eeeeda5423d6 | -5.1181 | -43.1964 | 2025-08-25 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 87ae50fa-5588-34f4-a016-53e529379262 | -6.8229 | -58.956 | 2025-08-25 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 5cbbfc31-f999-3907-8b6d-3472835a1575 | -5.0994 | -43.1977 | 2025-08-25 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 116.7 |


[Clique aqui para ver as próximas entradas](README13.md)
