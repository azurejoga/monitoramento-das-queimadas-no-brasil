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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f6dbe15-dc32-36f8-bff4-8f1fd8830ee7 | -10.95489 | -45.42002 | 2026-10-05 04:59:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c677f98-f8d5-3319-9901-eb5a700ad3c4 | -9.40141 | -65.8915 | 2026-10-05 04:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b37da504-a90e-3deb-a81c-67890680c41e | -9.13679 | -65.90763 | 2026-10-05 04:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4787cc4f-db16-39ff-8acd-ac7f5cd20726 | -10.96517 | -45.42019 | 2026-10-05 04:59:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5e45d0c-f0c7-3742-8791-01ab10081f9d | -10.96987 | -45.42356 | 2026-10-05 04:59:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 887ad4c8-febe-3989-92d2-04febf6a9f20 | -10.53135 | -48.06445 | 2026-10-05 04:59:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce52746a-0e60-3601-9dfd-9dc47d62c86b | -9.11496 | -64.36458 | 2026-10-05 04:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff4ba963-4547-3a3b-89fb-43c80a5523ab | -10.95103 | -45.41018 | 2026-10-05 04:59:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1de2ad1-424c-3a53-8955-fa9d02f5fe1e | -9.1559 | -63.16861 | 2026-10-05 04:59:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01d6791e-d4ba-3134-9e7e-4894a5c60f15 | -12.87923 | -61.72625 | 2026-10-05 04:59:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96451b6a-1686-3a22-b12b-91736be241f2 | -9.02927 | -67.55971 | 2026-10-05 04:59:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2c89a99-57c5-3aa7-ba1e-de794fcfdb12 | -12.21143 | -57.12284 | 2026-10-05 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 34a7b300-e76b-3053-a187-61a332e5ee6e | -8.35393 | -62.83795 | 2026-10-05 04:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3d67f53-2eb1-37ff-a66d-41f515e9095a | -8.3579 | -62.81668 | 2026-10-05 04:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a93560d-89ea-352a-b885-4806fef7ccda | -8.34727 | -62.83799 | 2026-10-05 04:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d3aadf7-b878-3ee7-b367-fa7c0d9b5eb5 | -9.15731 | -63.16172 | 2026-10-05 04:59:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed83eedd-ffec-37ba-a5ef-40db91d1a282 | -12.87379 | -61.71745 | 2026-10-05 04:59:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e079bc3-f896-329e-ac3f-4976c564a8e7 | -8.35326 | -62.84151 | 2026-10-05 04:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7eeda8d4-3a08-31d9-af49-923ce6e73cd9 | -8.33827 | -62.83128 | 2026-10-05 04:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a3b7b1db-3c94-30a7-8dd1-94292848bc01 | -8.34782 | -62.84048 | 2026-10-05 04:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d34382eb-e327-3ae9-bfe5-b34c6d8c040d | -12.87286 | -61.72248 | 2026-10-05 04:59:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e6e7b17-40f6-3397-bd04-7134f1f48211 | -9.40037 | -65.89693 | 2026-10-05 04:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17752777-5699-3caa-a47d-9b29ec202499 | -11.04712 | -62.57927 | 2026-10-05 04:59:00 | NOAA-20 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d445999-1605-31b4-9b65-b3db94e99b98 | -10.95358 | -60.91384 | 2026-10-05 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f494a98b-2c7d-3f26-8cc6-e2b36e4a0e97 | -13.73831 | -48.48204 | 2026-10-05 04:59:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a90139c-8149-3452-9fb7-fc6a7b8354b0 | -9.02213 | -67.55821 | 2026-10-05 04:59:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3094886-7e4f-3afd-9004-99f7f9a4353a | -8.84431 | -62.85592 | 2026-10-05 04:59:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c70db1f0-5fa1-353c-97dd-360d1d0edda5 | -8.34791 | -62.83443 | 2026-10-05 04:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b5348d1-fba6-3085-bc97-d1c6ca6d2f49 | -10.95448 | -45.42316 | 2026-10-05 04:59:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 474ce56d-3fa6-3cef-947e-e493244ff1f9 | -8.34439 | -62.8227 | 2026-10-05 04:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39523ca9-d5af-3ad1-b421-e9772368944b | -12.15831 | -60.74957 | 2026-10-05 04:59:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 169762da-584b-33d4-8ade-ddc5b44a3eb2 | -15.63292 | -56.44468 | 2026-10-05 05:01:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f7fab3ef-0ead-32c9-b56a-4b6f94707a02 | -1.46272 | -53.59729 | 2026-10-05 05:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d92001ab-2318-3132-b605-072103d834b6 | -0.38465 | -52.00478 | 2026-10-05 05:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8257e32d-2802-3894-835a-8b2b938356ff | 1.87097 | -55.7677 | 2026-10-05 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 450d40ca-9b04-3e10-9f01-3b15adff1d42 | 0.4413 | -60.5308 | 2026-10-05 05:40:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 92701f2a-9b5c-32ae-baef-b87f58f328b5 | -1.19822 | -53.38869 | 2026-10-05 05:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2888c0ec-278a-3af1-95cf-aeda88ed96f3 | -0.39296 | -52.03946 | 2026-10-05 05:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 24f57820-40cf-3862-8c43-7ab0c1e643f0 | 3.10053 | -60.60301 | 2026-10-05 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d5a8794-d29a-3324-9928-c799ab7e0a81 | -0.39463 | -52.02855 | 2026-10-05 05:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4959b1f0-07f8-3018-8034-a388ed95e728 | 1.7229 | -55.64528 | 2026-10-05 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db6cb843-80ae-313e-9292-b38349dba5af | 2.07504 | -50.8908 | 2026-10-05 05:40:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 739e903d-2fad-366d-8297-29ef80d1c598 | 1.72874 | -55.65007 | 2026-10-05 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| aa352c4d-448f-3eac-911c-e3f832963a62 | 1.82511 | -55.54606 | 2026-10-05 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96f93122-684d-33f9-9e7e-be9ccadb6c5b | 1.72964 | -55.6556 | 2026-10-05 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b9214c7d-575a-3d97-a272-1698e68a0d87 | 0.44265 | -60.53932 | 2026-10-05 05:40:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1cc2bc92-04a6-3b93-92b6-e43f63858d0a | -1.10457 | -54.15036 | 2026-10-05 05:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0d5d9195-0737-3227-bbcf-218c95dd2ffd | 2.002 | -50.92749 | 2026-10-05 05:40:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93f2ba75-4b1a-36ea-b982-6fd2b7c4d5dc | 1.80029 | -55.55004 | 2026-10-05 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae6e5b37-1267-3ab3-a5d3-f6012da0564b | -0.38413 | -52.01056 | 2026-10-05 05:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b58e9a0-5eb1-3550-95d7-1b0618153009 | -0.39627 | -52.01785 | 2026-10-05 05:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9600a734-519e-343b-9811-4ac6ed90aac5 | 3.0999 | -60.59904 | 2026-10-05 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a108f65b-b257-3f7f-bdb2-0a3a5d16d016 | 1.22305 | -59.97194 | 2026-10-05 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6591f75-0d2d-3fa1-b0e9-8a6e69acfc8d | 1.80526 | -55.54931 | 2026-10-05 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffa8b1ed-1cf1-31e0-b555-aed106e6d054 | 2.09953 | -50.74493 | 2026-10-05 05:40:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7a250df1-31c1-3506-8bfe-ec4ed67c3273 | 3.10839 | -60.56097 | 2026-10-05 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 51548265-1f1b-3fb0-8bc7-8efdd4b95852 | -1.19224 | -53.38755 | 2026-10-05 05:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 276b4960-676a-3987-82b6-f8fbb2f25993 | 3.08971 | -60.58028 | 2026-10-05 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 469191f7-f81e-3a4c-8eff-912971d1d6f6 | -0.40064 | -52.02914 | 2026-10-05 05:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 93e0a715-1c34-35ee-aae7-d2d3b24d9752 | 3.09033 | -60.58426 | 2026-10-05 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5e3f05dc-d473-3972-97f9-1f991905e46b | -0.40192 | -52.0242 | 2026-10-05 05:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9731e5f1-a323-317e-968e-53d9ae193866 | 0.31499 | -60.44349 | 2026-10-05 05:40:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3713fdd8-c494-36de-be56-170d9ee53809 | 2.0874 | -50.88247 | 2026-10-05 05:40:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 167957e0-0394-3647-b7dd-506ca3cdf92b | -0.39243 | -52.03904 | 2026-10-05 05:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07384118-b344-3fba-ba34-724862c04ffe | 1.89884 | -55.78543 | 2026-10-05 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4f568b56-0b0c-30b3-9dd2-28ceeb1f8af0 | -0.40756 | -52.03056 | 2026-10-05 05:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ed00c70d-5b0b-35f3-9e70-c499aabc70df | 2.10308 | -50.74864 | 2026-10-05 05:40:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a2d3a47-633e-3b34-9a88-54a1e70de510 | -1.09982 | -54.10546 | 2026-10-05 05:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bfa504af-448c-322e-826c-7aded8a0836b | 2.08074 | -50.88369 | 2026-10-05 05:40:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 506277e2-bfcd-35d4-b0f3-bd5581cc56f9 | 1.07791 | -59.69342 | 2026-10-05 05:40:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c233c97-6547-39c5-800a-66825040d5b1 | 2.00574 | -50.92758 | 2026-10-05 05:40:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5573161e-172e-327a-bad0-c3f898d5d7a0 | 1.86247 | -55.80808 | 2026-10-05 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 16bda514-8d42-3235-86b9-0aaf8147ac0f | 1.82602 | -55.5517 | 2026-10-05 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0bf12ea9-813b-3077-9f17-eb40dd89b78d | -0.39546 | -52.02317 | 2026-10-05 05:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 977745e9-ef17-334b-befc-bca86e5624ba | -0.39025 | -52.01123 | 2026-10-05 05:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 597a16ce-b9ab-38d0-bec2-1de8e5bb8b00 | -1.09803 | -54.11701 | 2026-10-05 05:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8043d4a7-841e-3388-a2fe-b8a113db9133 | 1.73188 | -55.6381 | 2026-10-05 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c06605c-d21d-3840-bf60-886ef61408b6 | 3.57872 | -61.34359 | 2026-10-05 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d7ceca9-8fba-3da1-80ed-259a60857622 | -1.46206 | -53.60167 | 2026-10-05 05:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b5817beb-c290-3393-9d84-e1c785ec75b8 | 1.7247 | -55.65636 | 2026-10-05 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 289c2750-93b5-3b98-8f52-6eadb5a39f7d | -0.39977 | -52.03458 | 2026-10-05 05:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95bc5908-779d-3217-91f1-22a595e291f0 | 0.31431 | -60.43916 | 2026-10-05 05:40:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| df4be06f-4dca-366c-ad52-b4a3048b8c67 | -1.33315 | -54.22325 | 2026-10-05 05:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 979495ca-f9de-3441-be3b-18a7c80cfa32 | 1.72784 | -55.6445 | 2026-10-05 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5a69d024-1db7-394a-8bd5-2809b6243aff | -1.09411 | -54.10441 | 2026-10-05 05:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d006a3f8-c932-3063-87a3-a4362bc714de | 1.73368 | -55.64927 | 2026-10-05 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 58dace2d-1766-3307-abb6-ab2167fb8176 | 1.86334 | -55.81344 | 2026-10-05 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 27550686-cca6-3f56-9181-7bfef20e4fef | -1.09864 | -54.11304 | 2026-10-05 05:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6e9dbb6-952e-3437-8392-9206fe362f17 | -0.4011 | -52.02956 | 2026-10-05 05:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e8ae1038-2434-3e48-a9a5-25ac8acdc4ca | 3.10076 | -60.62737 | 2026-10-05 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 919cb483-315e-3711-85fd-beabd8ade557 | 1.7238 | -55.65083 | 2026-10-05 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| ffdb4cf5-7be8-3e20-a492-e9c0ffc6f8d6 | -1.10663 | -54.14853 | 2026-10-05 05:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e293b13c-3d91-323c-b2e8-f94bbbe6982b | 0.44198 | -60.53506 | 2026-10-05 05:40:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 11.7 |
| bcea525b-d41f-3f49-becf-8e86a17ffcff | -0.3938 | -52.034 | 2026-10-05 05:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9e1639cb-fc76-3080-a168-6e61590e9781 | -1.09923 | -54.10923 | 2026-10-05 05:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3633912f-9eae-36be-8535-650a928a79fb | -0.39331 | -52.03359 | 2026-10-05 05:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f0c54106-704d-3503-abea-dcc4a18604ec | -1.09292 | -54.11213 | 2026-10-05 05:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 59afe7b6-5751-35f8-9c94-abcdcd42de4c | 1.79531 | -55.55075 | 2026-10-05 05:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9332448-22ae-30ce-83cf-5aa9e2d40dc4 | 1.21932 | -59.97252 | 2026-10-05 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 981edcc9-c417-3d6d-bb20-ade57504ca83 | 2.09077 | -50.87977 | 2026-10-05 05:40:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README49.md)
