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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56f1a81b-f99e-369f-87ec-37981df43521 | -8.9708 | -61.7033 | 2025-08-16 05:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 69.2 |
| f6d1fe5c-d822-3011-b549-80b0b1ab4577 | -6.9486 | -59.549 | 2025-08-16 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 2e37be62-67a4-3c95-9a99-4d08c4e683cc | -4.9118 | -43.257 | 2025-08-16 05:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| df1518c5-b2f0-3ee5-a2a4-215a9221e4c4 | -9.1708 | -59.6568 | 2025-08-16 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| b4ec19e5-dfe3-3da5-8235-6c0c3839e813 | -9.1709 | -59.6374 | 2025-08-16 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| fe38eaa2-5976-3e4a-96d8-5862cdb583f9 | -8.9709 | -61.6842 | 2025-08-16 05:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 7e89a821-2fe0-3a70-b289-e35751b23afa | -6.9303 | -59.5305 | 2025-08-16 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.1 |
| e467027d-d520-3495-bd30-3d5bf164bbee | -8.9893 | -61.7024 | 2025-08-16 05:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 395bf191-abdf-38cc-8fec-0417dc8f40b2 | -6.9487 | -59.5297 | 2025-08-16 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 1f93eff1-119f-32cc-8b9d-959de9cd974e | -7.9148 | -61.7478 | 2025-08-16 05:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 37f7b312-9a69-3359-8a33-e651e54ed600 | -14.9441 | -54.6959 | 2025-08-16 05:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| c361dd19-4f6d-33c4-a331-46aa1289ecd9 | -10.3898 | -53.4551 | 2025-08-16 05:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 49a3e163-b614-30a8-9878-8d55efb23fad | -6.9302 | -59.5497 | 2025-08-16 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 5f32f941-1b2c-3986-814b-866f99ff3d66 | -14.9628 | -54.7351 | 2025-08-16 05:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 12fca60d-c56e-3cec-afdf-691b3839c594 | -10.3896 | -53.4757 | 2025-08-16 05:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 8f2f9427-0d6d-3f5b-aa99-8a175e7f3532 | -14.9628 | -54.7351 | 2025-08-16 05:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 55.6 |
| b82e5c0e-f1e5-33ba-a0b9-334666728129 | -9.1709 | -59.6374 | 2025-08-16 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 4cb0684e-daff-395f-a3ec-640d46b3cb9c | -4.9118 | -43.257 | 2025-08-16 05:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 4d871a74-8860-3800-9d1e-07b54dd57afa | -9.1708 | -59.6568 | 2025-08-16 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| e7d36937-7713-33d2-a8ab-3d764ab86949 | -8.9709 | -61.6842 | 2025-08-16 05:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 2a4bdc32-bf26-3cde-99c9-f342d8e5e150 | -8.9708 | -61.7033 | 2025-08-16 05:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 6dd2d199-e5b3-3bf9-8c83-7bd11713dd3e | -6.9486 | -59.549 | 2025-08-16 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| bd0cd37e-d7df-34b5-82bf-1e47bcd25441 | -6.9487 | -59.5297 | 2025-08-16 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 002d9b39-5ef1-3e30-b716-877b32159e04 | -8.9893 | -61.7024 | 2025-08-16 05:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 600c1c48-937a-37ab-95df-d30b6858367a | -6.9302 | -59.5497 | 2025-08-16 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 5fe024ab-be56-3fba-bcf3-f24f850cd2fa | -14.9441 | -54.6959 | 2025-08-16 05:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| b07b19c9-3c9e-3f28-9856-30d2b477da32 | 2.16962 | -50.95489 | 2025-08-16 05:21:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3f05490-483c-3963-b0e5-b0f55b6e5cd4 | -6.93176 | -59.65211 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f953bd69-7170-3c6a-b3b5-ab7d260c928e | -8.98796 | -60.53559 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e5769136-8fb7-3c97-9c77-aae9a76efa22 | -9.84695 | -62.21928 | 2025-08-16 05:23:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bf237eb-0d25-3e84-b78c-159436d36cd1 | -8.99298 | -60.54718 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37fd3713-be59-35b5-b338-0fd13686a095 | -9.00289 | -60.52713 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d1c628b7-0195-3d6f-84a3-132c25c59229 | -8.56194 | -63.90257 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| baf12945-9574-3eef-af26-707f2c07b34f | -9.21318 | -59.65973 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d19aabd-4790-3ac2-89e3-8e14fd1dd1d8 | -6.94082 | -59.52578 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 043107de-bfe1-3690-bd41-76ae6bd2809d | -7.61572 | -63.33213 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 609be0f5-fe92-3925-b067-1c37de67d5b6 | -6.79334 | -59.82264 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b084731d-263d-3ded-ab4e-9049674ace6e | -6.93005 | -59.64093 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 828e72c5-86cc-3707-adf7-00c2cdef2a5b | -6.79946 | -59.82718 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f3f8a8e-0ba6-37ed-9a5e-2bc3cc736913 | -8.98912 | -60.55017 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a553bf59-09c5-336e-8bee-24597ccd1bee | -6.94479 | -59.54474 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d1643633-620e-34dc-8bc5-afaf3f431ded | -9.21207 | -59.66708 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d43dfd8-a292-3e08-b0bb-dac711a510ee | -8.54968 | -63.93331 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 451e34d8-546a-3423-bf2d-afb216772351 | -3.98727 | -47.88897 | 2025-08-16 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 774ff179-c584-38f6-816e-d5b00d9460e6 | -6.48805 | -62.93545 | 2025-08-16 05:23:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3dd1d67a-4bbe-3004-9e02-59bce1aeabc1 | -9.30811 | -63.73886 | 2025-08-16 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47f4996e-804b-3992-8424-a40c206b73ac | -9.16368 | -59.65958 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d58da4b-6a74-3e76-9c8f-6b7869e8f418 | -7.07704 | -60.14331 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4fa25da7-c154-3b13-b15b-244ad4680641 | -7.90361 | -61.7516 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b54979b-22ce-3a94-8a03-9d748d7ec704 | -6.95034 | -59.53094 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8e2a4a7e-ca80-3ac7-b577-0f4963c9a78c | -10.43044 | -60.27837 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 325b10d0-3245-388c-be6a-60c3e42ac2e4 | -7.45726 | -60.41046 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5f43860b-c78b-3231-8a52-eaf78d16ab4e | -11.65877 | -51.61963 | 2025-08-16 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c04c7362-12ab-33b8-b53e-68cb63aa8ff5 | -7.45572 | -59.93615 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d51401b4-d6df-31f9-87a1-4a5a9678c6ce | -8.96911 | -61.68275 | 2025-08-16 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 20.8 |
| becf72fd-b04d-36aa-b609-a31a2f90488c | -7.87866 | -61.82303 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f84aff4a-d0fe-3657-9969-a66c1e1cb84c | -7.96005 | -61.76053 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3790610f-2c65-30f2-a399-4d9e6a144a48 | -8.03671 | -61.5118 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a002452-57df-366e-8f52-2256b7a6f774 | -9.92157 | -63.18452 | 2025-08-16 05:23:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d5d2b7b-5c67-3e38-b2f3-d803e3c161e7 | -7.69784 | -63.32162 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1408139c-41fa-3d62-b552-c1a0f7b4ab10 | -3.49207 | -51.18898 | 2025-08-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73fd72b5-90ba-3046-a5a6-75cf02d5d955 | -8.98966 | -60.54665 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c72772a5-3c53-37bd-bb62-e6e32d0a1f9d | -7.31161 | -60.62553 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c31d8cfb-ea6e-30de-a683-94c366a41c37 | -10.01108 | -59.21907 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f6de25a-4f9c-3bd7-8239-6e0ea7dac10b | -6.62255 | -60.00455 | 2025-08-16 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0c94184b-3e5a-3d5e-b1e5-cea413dc8848 | -8.99393 | -60.49686 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 14fdf5e9-0297-3cf8-a3e3-096a0c9fe1a2 | -9.15238 | -59.66536 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23115f5d-0ce6-3921-8b34-6e3060dbeac2 | -7.61449 | -63.33984 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97ef032c-474c-38ae-b1cb-3a14ffbc87ea | -9.50196 | -60.5512 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 555e6eb0-0bf4-3487-8428-37209de43f66 | -7.91966 | -61.73621 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 97081536-4fa7-3a51-a3a1-1fd645acabe1 | -6.94089 | -59.54778 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c2b7f53-9bab-33e0-91cd-a15ab904736e | -9.04992 | -67.42164 | 2025-08-16 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 059867ef-dc76-38c7-ad01-7eac0c6cf70b | -10.42989 | -60.28201 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c503fe3b-cf16-35c3-b987-4ad52b50da9c | -7.53172 | -61.32761 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e665dfba-8365-39a6-b12e-375655622bb1 | -9.51079 | -60.5381 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b6916e7b-2867-332e-9296-03924fc6f6ac | -7.2522 | -57.62514 | 2025-08-16 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 78d1d43f-83b1-32b7-b249-3ec422a75c07 | -8.11171 | -61.20707 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2669955-09b7-3840-8f28-c07bde317f6f | -9.17243 | -59.65344 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c4945d92-d9d4-3a5a-9b0d-d9f5b021701e | -7.52728 | -61.31269 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| df4fb258-ee9e-345c-bd6e-3e1f8975f6e4 | -9.39696 | -60.54943 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aacba0bc-92d9-35ea-a69a-795ae14495f6 | -9.18995 | -59.65247 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fa2dabd0-8a99-31bd-b376-50d348a9706f | -7.5611 | -61.42117 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b46cf9a-1bd9-3140-ab67-83037688feb0 | -7.31215 | -60.62207 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8580fcfb-0d5c-340e-8fe8-e8822439334c | -9.20917 | -59.64029 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 83135430-8ef8-3c33-8c26-253905f353d5 | -8.11502 | -61.20758 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78052d22-70f9-3037-b8bc-fbb0eb08bdcc | -6.95253 | -59.51663 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00ba04af-e7cd-3f8d-bf6c-d52fc1e5c779 | -6.94863 | -59.51968 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 189f99c3-2327-319f-bf4b-5cf3a1250a11 | -7.9108 | -61.74916 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ca5a442b-1482-3a2f-a6f8-eb3de7489a53 | -7.94787 | -61.75144 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0c4acef-298a-35d4-8cec-65d4a6cd1db1 | -3.44703 | -48.96531 | 2025-08-16 05:23:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96686c3a-7535-3027-aeb2-40a34eb9e856 | -7.42716 | -60.03283 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3bf5979b-b94d-38db-88d5-8f84a0d64a01 | -8.99176 | -60.51096 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| aa39a104-7de8-3df6-8403-9015afb34764 | -9.21998 | -59.66075 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03e48c4f-0b99-31e4-a463-09f66e77d14d | -6.94698 | -59.53042 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46b5af9e-5322-3a92-b1ef-6ade509e3303 | -3.82235 | -47.74282 | 2025-08-16 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 89a49b53-cf01-30e5-9003-e739351f4c58 | -7.29176 | -60.62244 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 15e99df4-d160-31f2-9b7b-666dda3e6ec4 | -7.91799 | -61.74671 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 013436da-3183-308b-a275-dfd5d0be6876 | -8.11058 | -61.19268 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5988b05a-dc0e-30c0-a706-d5949d4df387 | -8.99129 | -60.53611 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 121dfa17-d360-3ba2-805e-dd5443717490 | -8.98511 | -60.50991 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |


[Clique aqui para ver as próximas entradas](README51.md)
