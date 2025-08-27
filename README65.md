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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47734112-3eb7-39e3-939f-518de0b7034f | -9.27244 | -59.79157 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08b834cf-a5a4-3e6e-a165-9964c16f6155 | -6.81823 | -58.97525 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3b02817-80e7-3a84-9081-65c45ea9b6c9 | -9.79102 | -64.24181 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 18ab9f39-07f7-3a5d-bff4-83cdf5deab6e | -9.02164 | -65.72678 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9f77638c-7e19-30f8-81fb-903e1509b9fc | -9.80638 | -64.24446 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85997c2e-83e8-3c85-b99e-2dcc110bd293 | -9.40251 | -60.49925 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 59afac35-a281-39ed-849a-12a405c37d94 | -9.58476 | -55.38332 | 2025-08-27 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9007edf0-593a-3ed3-90f3-7c898c8354cc | -7.35693 | -59.66316 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cabad611-ef5b-313b-8649-a6e0c284c174 | -8.93227 | -65.94653 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5238bccf-76ea-322c-93bf-30b4137df9a7 | -7.73525 | -50.28528 | 2025-08-27 05:18:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5ba2eb9a-9287-30dd-83ae-fddc50c3030a | -9.17529 | -59.69441 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6a7e3b42-5c8a-353f-8ea8-5274d3c36616 | -9.8246 | -64.28967 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ca096228-b68f-3477-87e2-a83a0ab85d2a | -7.56061 | -63.84604 | 2025-08-27 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4079ded1-f234-3765-93b5-e0f32416780d | -9.67582 | -67.50206 | 2025-08-27 05:18:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce348484-e9dc-344c-8f93-eb54b49bcf1c | -10.24767 | -59.66554 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 289bbc34-25ef-39a7-a0a4-39ee473d0db8 | -7.03867 | -59.84716 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca849402-ba01-3b51-8664-a0ebe60e21c1 | -9.497 | -60.52521 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6722167-111a-3d62-924b-7a2a597046d2 | -5.62217 | -60.24175 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14e4f8d4-aebd-3563-8743-5fcd3c7d16ca | -7.74709 | -61.08226 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10eea78e-016e-3f76-9774-42bce90f5cd3 | -8.23425 | -61.45884 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7c02ba61-8688-3d16-8c55-477120cd03c4 | -5.45331 | -60.14972 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08783228-7fc2-3c7c-9d4e-a4eb9589eecb | -10.08501 | -62.90353 | 2025-08-27 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 755d6fe2-28b0-390c-b645-cf01fe1f3fc9 | -7.29555 | -57.63874 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4cd4604-ea79-36d8-8138-a73edacf2d49 | -9.41522 | -60.52648 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c6b063ce-3e20-30ee-a9cb-ff1cd9c26073 | -9.40306 | -60.51733 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d552a329-611f-3355-baf6-947971bced2c | -9.18292 | -59.44977 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 682be7ee-c4e6-3a28-8672-15ea104f80ec | -9.16549 | -59.51834 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d81bdbf1-d19f-30e5-a90c-15af301ac8a7 | -6.91837 | -52.85729 | 2025-08-27 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 663e73dd-9a9b-3918-ba74-3bdf08e6914f | -8.50341 | -69.79824 | 2025-08-27 05:18:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ebf62e27-2458-3210-8e8e-76899d4d4fd0 | -7.39389 | -64.34454 | 2025-08-27 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 801f8dcf-4c9f-3f90-aa0f-9a0eeb3aa304 | -10.79847 | -47.07479 | 2025-08-27 05:18:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| f8967844-1f00-3610-a4b9-3dbfeb24e9fc | -9.20216 | -59.43496 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fab4f4b6-a53f-341d-91de-9d5b7b01518c | -9.82928 | -64.28548 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6a6ccd9f-a890-38b6-9e3d-fcc6a7ee8290 | -9.02451 | -65.68566 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b187f140-105d-352d-aa74-686e6a59fd9f | -6.26376 | -60.01392 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06ec645f-ce94-31e6-9a7b-12ef8b9e6b5e | -6.84352 | -58.96503 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 4540c61b-c9de-30a7-bf73-a86d3dd909fc | -9.18864 | -59.52199 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 997ceab4-6f91-3439-bb38-dd4c602c358b | -8.85111 | -62.43852 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 425ba75c-ebe4-3b20-96bd-59c024c61343 | -10.28324 | -64.50388 | 2025-08-27 05:18:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 302812f8-2ad4-3063-a47e-60e85d3852b5 | -7.34701 | -59.6616 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c589a5be-9cd4-3880-a0ff-855645db448f | -9.16604 | -59.51487 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb0bd418-78dd-3455-b8f7-bdd99569e526 | -11.3173 | -55.21107 | 2025-08-27 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| db7b5210-ea92-327e-aa81-a5831c26be11 | -6.68267 | -58.53517 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6ae883c-b935-3fba-81fb-bc0429eeb1c1 | -12.76138 | -48.19646 | 2025-08-27 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 6755d162-8760-3dc9-b6c5-019a9691b4d0 | -6.69377 | -58.55117 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf28662b-a8f0-3249-85c8-b1e74cebcda4 | -6.62969 | -58.54832 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fadb2239-9b8a-3475-947a-f970c8023d47 | -7.54093 | -61.37963 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69d8b3c5-55ca-397a-8665-ff0a6f58c5aa | -11.31598 | -58.33376 | 2025-08-27 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 582aba9c-fde8-3d56-8c52-ce4ea153e916 | -8.33871 | -62.92634 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 730bbff2-4bf7-3c04-9e88-3c5ca0308a22 | -7.47445 | -61.33449 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ced2779-8f52-3b23-ae1d-4ed34db3e1df | -6.81984 | -58.96488 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 546aef8c-c2ce-38bf-abb1-8b86cea8490c | -9.23785 | -60.91484 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6430c863-72df-371a-816d-942bc4b0222b | -12.80269 | -48.1206 | 2025-08-27 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 60ec492f-4b4f-3e44-b3fa-5206af489414 | -6.77133 | -59.66629 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89ddbf46-5aa8-37df-ae54-c04aa3955dd7 | -9.09438 | -49.5645 | 2025-08-27 05:18:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6fafcefc-c7f7-3c9f-b659-23911ad3c165 | -9.26357 | -59.76168 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e1d53b8-1b88-37d7-a70a-032295e0c825 | -9.18365 | -59.51052 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54de07c1-ee5b-3bea-9f2f-bf07628d0ccc | -6.2492 | -60.02232 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 9bfa8e82-148c-374d-91d2-07fc39ced93f | -10.42053 | -57.69546 | 2025-08-27 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb03418e-16bd-3a00-bac0-1ddc4a7afcd6 | -6.79003 | -59.6337 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0f1abf7-8d84-313e-ab9c-2ac6d0687d8c | -11.37847 | -55.35911 | 2025-08-27 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d98a03c6-7957-30e2-8706-33ccb71d29bc | -7.3515 | -57.63612 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8313c38-a6fd-34dd-84ea-90108ab84b81 | -10.42111 | -57.6916 | 2025-08-27 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 011250e1-bb5a-39b1-8948-ae86a60ce07e | -9.16777 | -59.54717 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af87e02f-a20c-3a96-8438-b0b1afddf5a0 | -9.71078 | -62.4003 | 2025-08-27 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2338c82-cb94-329d-89ce-f86d24578ef6 | -8.69204 | -47.20507 | 2025-08-27 05:18:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2ffbf238-8d3a-349a-b5d3-5cfd50e4fd60 | -6.95425 | -60.08069 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c4e00f2-102a-3697-9cec-c9b6d47a3606 | -6.62051 | -53.32165 | 2025-08-27 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9057a830-6f52-3ac7-b2d4-8e388e100289 | -9.58087 | -55.38277 | 2025-08-27 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5b051fc9-559a-3a5f-8514-96d377230259 | -10.08857 | -62.90412 | 2025-08-27 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cb407c98-bf9c-35b0-ac73-88556e901277 | -9.28349 | -63.72163 | 2025-08-27 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 119bcae4-3cfa-3aef-86b8-ea9b1eede595 | -5.73332 | -59.88323 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d62fedb-48db-337a-8071-1855c26a3dea | -7.54034 | -61.38337 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d1694fd-ef2e-3e2b-b7dc-38243dd14896 | -9.65882 | -65.00281 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a55809a1-cb99-3e45-bda3-aebc887ded3c | -6.76857 | -59.6623 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 633e99c7-3b35-356b-9ab6-102b2d23a042 | -9.55985 | -55.38274 | 2025-08-27 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 02e97529-fa45-3528-8a42-27dcf0d3f7d8 | -9.44472 | -65.42142 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd4bf427-4391-38be-86a9-ed831d4ac6fc | -7.56448 | -63.84668 | 2025-08-27 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8825dc3b-fb60-3856-8800-0830a004ae28 | -8.88177 | -60.77698 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6174ea2d-8136-323d-8446-9b8c42b23176 | -8.96547 | -65.96841 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d92f3bd-e84a-3c4d-ab21-dec8ad9abf2e | -9.19363 | -60.8055 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| cff0ddf3-6729-365b-860b-defc5cc1008b | -8.9482 | -65.9579 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 54f6c6ff-16ec-3cc3-a512-fe636ec216d0 | -8.07635 | -61.54504 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2dccc6f0-b813-3841-9f08-29ba85a2c2c3 | -10.095 | -62.90945 | 2025-08-27 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 657a4a5f-c91e-31af-92d8-09f6dc0f5ff1 | -7.73972 | -61.08484 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e97eebc8-863f-34d9-a264-a337082fa0a5 | -9.39691 | -62.49657 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02e03c85-3603-3126-ae95-6434e1476745 | -10.32514 | -59.18507 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a33226d3-2c57-3e32-afd5-40ab38158f9f | -10.10759 | -57.76724 | 2025-08-27 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90e89434-d7bc-3731-a944-98d16bdeb012 | -10.76653 | -47.03533 | 2025-08-27 05:18:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 376bee14-66e4-3dc2-b918-daa29432a2c4 | -9.41359 | -62.48293 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8a2bb3f-eb9f-3e56-a786-ab03d5631db5 | -9.22725 | -60.91679 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 331f3701-4fbe-360b-8585-19e6def6f0da | -7.54512 | -63.84347 | 2025-08-27 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e6a5ddec-6cdc-3937-9cd8-0d5d9c9eba89 | -8.9634 | -65.94749 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| fb9bea04-4b9f-34ad-8cc7-76f410d5c9bd | -6.91501 | -59.35912 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9987351-7445-32f5-97bf-baf67aef170b | -8.10715 | -61.48472 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75d0c80b-ea4c-39cb-8037-2eee762c5287 | -7.1 | -59.21826 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 623a4ccd-da06-3023-82d3-d4b3215b4280 | -6.91724 | -59.36655 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97791176-35ef-343a-b5c6-26b0b6822113 | -9.27186 | -59.77367 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e662c6fb-2bf4-3acd-a3b2-8508401389f3 | -8.8498 | -62.44653 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f2422d1-59b2-3ee2-9f28-64b6ab9e77e6 | -5.61825 | -60.24478 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README66.md)
