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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 661ffa3a-6488-3836-975c-5d0f6358530e | -13.0119 | -45.1988 | 2025-08-22 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 727ea03b-8084-3b36-9b19-35570258730c | -3.2321 | -46.7836 | 2025-08-22 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| e8b50c62-e917-31aa-b92c-63cbb5324096 | -14.5947 | -54.8403 | 2025-08-22 00:00:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| cb9cd9e4-ad2e-3275-9496-4a5dcf68d766 | -4.9422 | -49.391 | 2025-08-22 00:00:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| be795352-fbf7-346d-8417-f49536cab413 | -9.5363 | -60.5644 | 2025-08-22 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 10d52747-225a-3f6f-ac8a-3b05b47567ff | -9.5365 | -60.5451 | 2025-08-22 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 154.3 |
| 03e77dab-c8be-3f82-86b9-b2dd59cdd93a | -14.8733 | -47.9472 | 2025-08-22 00:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 57.1 |
| baef9588-81b0-32e7-952b-3cdf02328d22 | -12.9921 | -45.2252 | 2025-08-22 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 142.6 |
| b4182f04-fbab-3cc3-84c1-d058ed1d515f | -15.505 | -48.4916 | 2025-08-22 00:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 001b44cb-c997-30cc-bc09-8869aa596705 | -14.7712 | -45.4289 | 2025-08-22 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 16069624-0003-391f-83a4-201feacb989c | -9.2095 | -59.4609 | 2025-08-22 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 29fb1031-f687-3f32-a433-09e9782bd85f | -9.5179 | -60.5461 | 2025-08-22 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 179.9 |
| 2675bf32-0826-324e-8856-432d682e4c8b | -13.0114 | -45.222 | 2025-08-22 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 124.5 |
| a5c7205c-4ece-3e5e-a5be-d1ef5c077183 | -12.9722 | -46.2617 | 2025-08-22 00:00:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 53.4 |
| ece2772a-1d68-33d7-bff7-c589407a9bf6 | -14.8928 | -47.9439 | 2025-08-22 00:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 67d2eae4-66ac-3f0e-9c6c-ff400e03b1e8 | -9.5177 | -60.5653 | 2025-08-22 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| cddc576b-4104-37c9-934a-56d03791cf76 | -14.7787 | -59.6559 | 2025-08-22 00:00:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| b59f8097-919a-37a2-9491-7a7abd5c6079 | -14.7717 | -45.4055 | 2025-08-22 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 158.8 |
| 0d531bc2-ad53-3c33-863c-7bd16740d92a | -8.8735 | -62.4305 | 2025-08-22 00:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 1d0e4fcf-d353-3bb7-96dc-2140ca94af96 | -12.9916 | -45.2484 | 2025-08-22 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 2d0bbbbd-5e3f-344e-a39c-ebcb8297932c | -14.7521 | -45.4091 | 2025-08-22 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| d07c5f64-1ede-3504-a05f-a9254201ac46 | -14.7516 | -45.4325 | 2025-08-22 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 14b058d0-c04d-3c09-84c5-8c885957217c | -8.8921 | -62.4297 | 2025-08-22 00:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 26.9 |
| d413b796-ce15-341a-b77d-6f819f94607f | -8.6129 | -62.6308 | 2025-08-22 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 30.3 |
| f620e666-2afd-3ab8-8350-19547a1c24b1 | -8.5944 | -62.6126 | 2025-08-22 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 80999937-5c1a-30c0-8ccb-cee9706724d0 | -13.0317 | -45.1724 | 2025-08-22 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 4b976f9f-b217-3feb-ab23-48a3aebee9a8 | -12.9528 | -46.2647 | 2025-08-22 00:00:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 84ca11f9-ab6b-37b0-a49b-c4f8d0c482e9 | -7.5922 | -63.4414 | 2025-08-22 00:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 51f9f166-fe92-3b0c-b2d5-cf122e6e5cef | -8.613 | -62.6118 | 2025-08-22 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 5c807cc6-bc68-3335-80b7-1e07375e01bd | -12.9925 | -45.202 | 2025-08-22 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| d6044980-b528-36f5-953a-103242ddc26a | -8.8736 | -62.4115 | 2025-08-22 00:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 28.5 |
| a488d7d1-ee47-3701-a63d-211a7915f352 | -12.9524 | -46.2876 | 2025-08-22 00:00:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 45.3 |
| e947e296-9f5b-3f5c-9aa2-7b8564e48af5 | -9.518 | -60.5268 | 2025-08-22 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| ec04597e-9bd7-38cc-affd-5cf32f0be6b7 | -13.0109 | -45.2453 | 2025-08-22 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 83edffa4-6d2d-3911-9e7c-43d741a0e67a | -8.8735 | -62.4305 | 2025-08-22 00:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 61930665-8e93-36bc-8015-27538ae3874f | -14.614 | -54.8381 | 2025-08-22 00:10:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 87.7 |
| ec2ec674-c576-3b81-9ab9-f76db7d52e9c | -14.8928 | -47.9439 | 2025-08-22 00:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 2104fb9b-71bc-3bd9-adf1-a0e91b560a76 | -12.9921 | -45.2252 | 2025-08-22 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 129.3 |
| ff3cc336-5b33-36e2-804e-07d1cfb26a9e | -13.0114 | -45.222 | 2025-08-22 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 917df1bc-b6cc-38c2-83f1-fed6d04f2669 | -3.2321 | -46.7836 | 2025-08-22 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 2ece9f5a-99d2-3765-bd72-6189d51768de | -14.5944 | -54.861 | 2025-08-22 00:10:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 609badd5-b01c-322b-9861-fcb72c8510d3 | -8.8921 | -62.4297 | 2025-08-22 00:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 9ad2990c-fcf9-363e-a63e-6ed342a7a298 | -9.5179 | -60.5461 | 2025-08-22 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 130.0 |
| 6626a86e-3395-3c21-9210-c3909fa3c537 | -14.5947 | -54.8403 | 2025-08-22 00:10:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 206.9 |
| ba5205b1-5de0-3115-b1e2-aa842bc06166 | -12.9528 | -46.2647 | 2025-08-22 00:10:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 3ecf7fbc-5202-3235-bd4d-f7af140ac885 | -8.5943 | -62.6315 | 2025-08-22 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 43167092-2e0c-3ca1-ad33-457fa0f37c48 | -12.9925 | -45.202 | 2025-08-22 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 3e504932-f4a0-38a1-9466-79eca01ee7f3 | -12.9916 | -45.2484 | 2025-08-22 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 45.7 |
| f03802c0-a143-3e42-993e-62b334756697 | -9.5363 | -60.5644 | 2025-08-22 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 28d5907d-cdc7-3f52-9cb4-d422375a5481 | -14.7521 | -45.4091 | 2025-08-22 00:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 3390b009-25f4-39b8-9fa8-f615a3b44704 | -8.613 | -62.6118 | 2025-08-22 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 66ebbc2f-d248-37e6-999d-2118a93d7377 | -14.5751 | -54.8632 | 2025-08-22 00:10:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 9778a43d-907e-3158-817d-6e8b8b609935 | -11.8185 | -44.2469 | 2025-08-22 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 1ddb1830-d922-3821-84ed-016195411643 | -13.0109 | -45.2453 | 2025-08-22 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 23ef786a-dff7-3b94-b859-586b9122b6ff | -14.5754 | -54.8425 | 2025-08-22 00:10:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 35fa5886-c02f-351d-992c-1a20f0de1c4b | -8.5944 | -62.6126 | 2025-08-22 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 4c954a27-a6b3-3f72-8699-5149ace5d7da | -9.2095 | -59.4609 | 2025-08-22 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 266c541b-077f-3278-ad69-b3428f92e6c2 | -9.518 | -60.5268 | 2025-08-22 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 0a82faad-1787-38e4-b9d3-aa4921870215 | -2.4685 | -47.7697 | 2025-08-22 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 9e83873a-022f-3c27-9c34-943d4d34173c | -8.6129 | -62.6308 | 2025-08-22 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 85581db3-1981-3cfc-8c3c-605cee4bd5ed | -14.6137 | -54.8588 | 2025-08-22 00:10:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 0c418914-b837-36cd-a66a-60646599ab9b | -9.5365 | -60.5451 | 2025-08-22 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 146.3 |
| e06c6407-2014-3c26-852f-9ac035f56871 | -8.8736 | -62.4115 | 2025-08-22 00:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 101faeed-3295-362d-b88b-dea1518dd922 | -13.0119 | -45.1988 | 2025-08-22 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| ec649428-e4a0-3a6f-9703-91a929fc69f0 | -14.8928 | -47.9439 | 2025-08-22 00:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 85.4 |
| c2a489d1-71ea-3d9c-9a70-66f16067db20 | -9.5179 | -60.5461 | 2025-08-22 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 134.1 |
| 76641a27-e536-3b35-ab2d-42a2fdd11648 | -13.0119 | -45.1988 | 2025-08-22 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| fd31aeb7-26a3-3e0d-b4d6-5379e301d808 | -14.8733 | -47.9472 | 2025-08-22 00:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 5cd1332f-2203-3cbf-9bfd-09fdad216b8b | -9.2095 | -59.4609 | 2025-08-22 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 326043b6-afdb-3a1d-87a4-5b0002cedf40 | -3.2321 | -46.7836 | 2025-08-22 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 7fa70df2-1b5c-3b7e-81f5-8aa5b43dd8aa | -9.5365 | -60.5451 | 2025-08-22 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 126.0 |
| dd79bd13-6a97-3539-88b5-0dd6984b2e2f | -12.9921 | -45.2252 | 2025-08-22 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| acffab84-d3ab-3a71-824c-7a973ab766ff | -9.518 | -60.5268 | 2025-08-22 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 3f3adaef-d50c-38b5-85f5-dbebf3da983a | -12.9925 | -45.202 | 2025-08-22 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 40.3 |
| f89cddad-d4ab-317b-aa01-a5ddfc7ef15f | -8.613 | -62.6118 | 2025-08-22 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.9 |
| aa7dfb49-025f-30bd-b50d-2300254d9c4c | -13.0109 | -45.2453 | 2025-08-22 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 7ac32558-8318-3c54-915d-6488b3ddb385 | -14.5947 | -54.8403 | 2025-08-22 00:20:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 15db1fa5-e1d8-3d47-a015-210a20aee024 | -2.4685 | -47.7697 | 2025-08-22 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 4636413d-5be4-32a7-8cc0-67fc1c348de4 | -8.8921 | -62.4297 | 2025-08-22 00:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 30.2 |
| bf6c42fa-8826-32ce-9c0a-f0cf09bb8836 | -12.9916 | -45.2484 | 2025-08-22 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 3032eebc-46fb-3a85-8abf-387a8a3c3a39 | -8.6129 | -62.6308 | 2025-08-22 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 80cfb629-2b3e-374c-9308-f87e2c44c8c4 | -8.5943 | -62.6315 | 2025-08-22 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 0b77267a-9af6-3cd1-b601-95cf5542f107 | -13.0114 | -45.222 | 2025-08-22 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 50d30315-0a0b-39b6-933c-d7497239eb81 | -12.9528 | -46.2647 | 2025-08-22 00:20:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| ad0ee467-eabc-3011-97e8-71bb2bc753a4 | -7.5922 | -63.4414 | 2025-08-22 00:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 13be63d5-04c8-3e64-8255-3f3f92d21591 | -8.5944 | -62.6126 | 2025-08-22 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 8f74af2f-1428-3caf-bf72-68aaf2012bad | -8.6129 | -62.6308 | 2025-08-22 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 3f0e06f3-33d7-3d81-ba98-f8f873f4562c | -9.5365 | -60.5451 | 2025-08-22 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 6d4a9801-dd7a-355b-873a-6c20eba5b3ba | -4.4011 | -44.0985 | 2025-08-22 00:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 64f804fb-3e19-3558-8ebb-9d9374839fe7 | -7.6183 | -46.2392 | 2025-08-22 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 2d45af23-25aa-3f48-9e44-97b2b59e5adc | -12.9916 | -45.2484 | 2025-08-22 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 1120bb93-53b6-39f1-ad8f-a23051728bd4 | -14.7712 | -45.4289 | 2025-08-22 00:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 96a6486d-8678-37a7-8bf0-018eef0760d8 | -9.518 | -60.5268 | 2025-08-22 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| a5671cf8-e0b5-3735-83e9-aec5a6407d21 | -8.613 | -62.6118 | 2025-08-22 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 5e8ebc75-c1a6-3630-a1f3-dd8b856ba5a2 | -9.5179 | -60.5461 | 2025-08-22 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 158.2 |
| 95071def-7cea-336f-b642-15d9204d3d3a | -13.0119 | -45.1988 | 2025-08-22 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 34.4 |
| b385d996-ef10-3bbe-8b71-3b9b778a71d1 | -12.9528 | -46.2647 | 2025-08-22 00:30:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 2238bb00-3759-31e7-98a9-a0f58733e65e | -8.5944 | -62.6126 | 2025-08-22 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 8c7474d1-501b-3ac8-837e-06e119c1e5a2 | -8.5943 | -62.6315 | 2025-08-22 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 23.7 |
| e58d952e-bfe7-3462-9ada-49708ad04fb6 | -13.0114 | -45.222 | 2025-08-22 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |


[Clique aqui para ver as próximas entradas](README2.md)
