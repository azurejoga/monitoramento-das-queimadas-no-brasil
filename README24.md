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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c188fc0d-cf55-3f2c-821a-64198cf119ba | -7.29006 | -55.30764 | 2025-07-27 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c67256a-4b31-3440-9866-c1bbdd3d5c5a | -8.07191 | -63.86567 | 2025-07-27 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8004d07c-4101-3ab3-b81a-c5a610bb9beb | -6.64035 | -58.85332 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ff570a95-3342-37c5-9f5d-d7179456046e | -6.65228 | -58.84389 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e56fc87b-c359-3600-b3af-bde3df184b15 | -6.54052 | -56.19062 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1fd556ad-d536-3746-9284-99103c3ca232 | -18.22337 | -54.54659 | 2025-07-27 05:27:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ddcdbb2f-d211-3601-be43-9415839db978 | -18.00073 | -53.17286 | 2025-07-27 05:27:00 | NPP-375D | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 26d64e8b-955b-3847-9a20-c422c02e16e4 | -17.9888 | -53.17927 | 2025-07-27 05:27:00 | NPP-375D | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3188910-301d-39e6-a649-32c67eab6a12 | -13.45497 | -60.97871 | 2025-07-27 05:27:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a92e240-e0b5-3944-a36d-9a0e69779fe1 | -17.98924 | -53.17512 | 2025-07-27 05:27:00 | NPP-375D | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6723d802-b24a-377b-9f70-2350c96c09e9 | -17.98369 | -53.17437 | 2025-07-27 05:27:00 | NPP-375D | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19e1ab67-21ed-311a-a32d-f30a60a8b513 | -17.99478 | -53.1759 | 2025-07-27 05:27:00 | NPP-375D | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30b07587-2762-3870-a695-52ba57604c49 | -16.25125 | -58.39856 | 2025-07-27 05:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b618346a-e76b-386c-93ac-e47996779b2c | -16.68467 | -49.12963 | 2025-07-27 05:27:00 | NPP-375D | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f81597d1-a877-35b2-bff0-9dfb3759d6a9 | -15.0387 | -49.25936 | 2025-07-27 05:27:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16ecb39c-44f0-3c65-8760-5e46c1e769a5 | -18.39665 | -53.32048 | 2025-07-27 05:27:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a94f714-5404-382e-a90b-85d7829902a4 | -18.22304 | -54.54962 | 2025-07-27 05:27:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 83c2afbb-d384-37d7-8435-40f4b0f8c62b | -18.22491 | -54.54996 | 2025-07-27 05:27:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f2e41dd6-b9ed-328f-8475-07de316dffaa | -16.41184 | -48.92447 | 2025-07-27 05:27:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3512233f-7a3a-32ad-99b0-49ef989ad376 | -21.42136 | -54.13105 | 2025-07-27 05:27:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78a8f33b-d150-33f3-b6be-8523535116e9 | -16.40474 | -48.92421 | 2025-07-27 05:27:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 46f774d7-1c5c-3721-8caa-af9a8ae28fda | -16.408 | -48.92311 | 2025-07-27 05:27:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 442aa6ab-247e-3fcd-89a8-10c778427366 | -18.39704 | -53.31676 | 2025-07-27 05:27:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c340115e-1901-3409-8613-9e648292c014 | -16.40731 | -48.93024 | 2025-07-27 05:27:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 73c04754-a6d3-3231-baa7-acef0814212a | -18.22526 | -54.54691 | 2025-07-27 05:27:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a714bff-e9fb-3890-abf9-fe271d278449 | -18.00031 | -53.17677 | 2025-07-27 05:27:00 | NPP-375D | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bcc1308b-76dd-34c9-b0e0-ffa5ec933668 | -15.03933 | -49.25306 | 2025-07-27 05:27:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 056a45f3-6850-3271-b192-c4f1f8fb2060 | -17.99436 | -53.17994 | 2025-07-27 05:27:00 | NPP-375D | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b8d8764-ac02-30aa-9dc3-308d2c682ddd | -17.98326 | -53.17858 | 2025-07-27 05:27:00 | NPP-375D | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8645b8d-87ec-35f3-8496-194e4db21d7f | -21.60423 | -57.58117 | 2025-07-27 05:29:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68f9f107-a0b6-3979-8565-8acfe4d8eea2 | -21.60443 | -57.57929 | 2025-07-27 05:29:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc092021-6a41-38d8-a3ea-22a1b2ca97b9 | -21.60879 | -57.57988 | 2025-07-27 05:29:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a72f5ce9-de00-3b72-8dbc-1b21c0b1ef9e | -23.06522 | -49.67364 | 2025-07-27 05:29:00 | NPP-375D | IPAUSSU | SÃO PAULO | Brasil | 3520905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5c8a232a-6c59-3a57-ba6e-a31977d1bce2 | -21.60909 | -57.5774 | 2025-07-27 05:29:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0dda53d6-815a-3cc8-9f8f-4583a8a919ea | -23.07244 | -49.67374 | 2025-07-27 05:29:00 | NPP-375D | IPAUSSU | SÃO PAULO | Brasil | 3520905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f747e257-0360-3bc0-9a86-45698c7c1b62 | -21.60859 | -57.58176 | 2025-07-27 05:29:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3cf84ea8-6cf5-3eec-8cd8-66e195d15697 | -6.639 | -58.8475 | 2025-07-27 05:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 87.3 |
| db8387ff-ba1e-39f4-a51d-8b71d2489671 | -6.6389 | -58.8669 | 2025-07-27 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| dda58e48-e415-3c17-8017-b47d73c8b6ca | -6.6575 | -58.8468 | 2025-07-27 05:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| c5aba34f-f9bc-30f3-9513-9eb79e1c8183 | -6.6575 | -58.8468 | 2025-07-27 05:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 3605d383-f666-3d92-937a-60bbbcaae237 | -6.639 | -58.8475 | 2025-07-27 05:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| c248c48d-21e9-3ba6-984f-e4fe67082231 | -6.6389 | -58.8669 | 2025-07-27 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 9923f364-414b-3983-96fa-814077b02d14 | -6.66753 | -58.84696 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ff53202-8bce-3056-bac4-60200c8ebd65 | -6.64625 | -58.85455 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 29860e26-8f9b-31d4-b946-9d96d6b93668 | -6.632 | -58.84695 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 04fbf5ac-6619-39f9-86ae-d87366c47292 | -9.02348 | -59.76879 | 2025-07-27 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 061813dc-9eef-33b4-9093-a52908d7fad9 | -6.6455 | -58.85844 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 47c91ec9-55ce-364e-90c4-db46c4bc1790 | -7.49712 | -63.82074 | 2025-07-27 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56dccd3b-6a45-33a7-a733-295c02f30f36 | -6.49306 | -56.20339 | 2025-07-27 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e121252-23d6-320c-b4c0-582888c03fad | -6.65487 | -58.82734 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fddb5b4e-7a85-3e60-86ab-70e5172f1a1d | -5.91881 | -61.30506 | 2025-07-27 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bb34a30-8265-388f-a132-d0d847613dce | -6.67494 | -58.83036 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88c711be-86cb-3bf7-a3c1-54f947f578c7 | -6.66531 | -58.82595 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5f19aa4-3652-3a5a-9d7d-48a3f2b800b5 | -6.62497 | -58.8603 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8b83bcaf-7a32-310b-bb48-4e38904706ab | -6.65869 | -58.83679 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3002df46-a60d-3fae-b954-87e900f20e19 | -6.67335 | -58.8419 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9443194-2dc0-3e29-ab0d-137ecdcdcd22 | -6.68418 | -58.83765 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e06daa40-4bea-3cef-894e-d7becbf67c90 | -7.60515 | -61.21648 | 2025-07-27 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 201ac2c5-ab8b-329c-97d2-86fcb55165df | -6.64917 | -58.83433 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0ee8ed5-0dba-34b7-994f-5df4ce6f4017 | -6.66132 | -58.85485 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 16afa7bb-b496-33a1-85de-e55020fd5b01 | -6.63283 | -58.84118 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d89e02b9-8f34-3f62-ae37-153dcdc0f24e | -6.65545 | -58.8264 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 871e508a-15c9-3e45-9779-864d61fcb35b | -6.67717 | -58.85121 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7db6f50c-34d9-3db6-8f49-4d7dbc4808c2 | -6.64708 | -58.84883 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 30955277-0ebe-3ee3-8f92-d25e17f46437 | -6.65503 | -58.82929 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97cdd8f0-073f-3607-927a-19dd74757fc9 | -6.65419 | -58.83509 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3889567-ae59-35f8-826b-37834e44011a | -6.67033 | -58.82668 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6eb28af-36f4-348d-878b-6cb978f27749 | -9.4617 | -57.85165 | 2025-07-27 05:48:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e9e2f34-1bde-392d-bb75-0b7671847be1 | -6.63038 | -58.85819 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 33f76c72-59fc-33aa-b826-6ec8be70fbb2 | -6.67797 | -58.84545 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7379fff-e7f0-3661-b3a6-c2bfd25fb770 | -10.0419 | -59.10297 | 2025-07-27 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 003d394a-c39e-368c-b038-3128d43c8457 | -8.49715 | -64.03043 | 2025-07-27 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b7d968a-9b7b-3f8c-a43a-3c8e90d73dc7 | -6.65627 | -58.85597 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e147c5a1-fd81-3016-8254-eeda543f8cc1 | -6.64786 | -58.84112 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24dddfac-55d0-3331-9c01-a70bded34604 | -6.68339 | -58.84332 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f50b61f9-e5d1-3745-97b4-9873bf1b0c78 | -6.68079 | -58.82517 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8868141f-bc6b-34e2-9202-b5f727e489a3 | -6.67414 | -58.83617 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc6c81ba-dd27-3e1d-89ea-ecffe09aaf60 | -6.66491 | -58.82887 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15d84a25-6ff1-3fdf-ae31-babba8e9cd82 | -7.49282 | -63.8245 | 2025-07-27 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45c6f890-b667-310b-b20a-c4ec9c762dd0 | -6.65949 | -58.831 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b9f40b2-0248-3c09-a70f-3f105093dd11 | -10.03822 | -59.10139 | 2025-07-27 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36885de3-0141-3983-8f8c-c00856f22e13 | -7.56154 | -61.41132 | 2025-07-27 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5b55b99b-55d7-3d37-9ee5-40422eb51202 | -6.63998 | -58.82707 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60337b1b-1033-3c87-970d-e6611433e2f2 | -6.66451 | -58.83175 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1dd26c7c-4e97-3c5f-b171-da82f718eb12 | -6.6571 | -58.84841 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2b3322c-0c30-371f-9e14-2a8ddd82cd1c | -6.67837 | -58.84261 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6747d7b0-ba39-3d97-b0f4-bdcaed82560b | -6.64205 | -58.8482 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c1210361-c3fc-3689-8628-1f59de383233 | -6.65043 | -58.82564 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1935a633-ab67-3031-9b8a-0505c4786e09 | -6.64875 | -58.83724 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e7fad79-90ee-314d-9378-817855aa2007 | -6.68037 | -58.82817 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f243e642-dff5-3470-ab7f-6071a0ba461f | -8.07092 | -63.85836 | 2025-07-27 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90978151-3202-36bb-9e1a-edb4159158d6 | -6.64906 | -58.83238 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84329d53-6639-3a4f-b5eb-8c8f1b752466 | -6.66952 | -58.83251 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e02e0d8e-b986-3872-a39f-f37812538b44 | -6.66291 | -58.84336 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d7378f0-61d4-3f0c-bf63-9b4d2ff9f7ae | -6.64826 | -58.83821 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd61f7e5-0891-3f8f-a717-1aa95d61d2e5 | -6.6513 | -58.8534 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 83e52647-3c8f-3159-9802-078da298c2ea | -7.56697 | -61.40395 | 2025-07-27 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6f1eeafc-1bbb-3078-a47d-5d6873fffb48 | -6.63537 | -58.82347 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68a418be-7a01-3dca-a01b-49b5debef319 | -9.02419 | -59.76354 | 2025-07-27 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3562a1f8-558a-375b-bce1-7a2ba37909be | -6.64289 | -58.84241 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README25.md)
