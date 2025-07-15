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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1240f40e-7669-3898-91a5-a8753cb07f76 | -3.58075 | -47.5176 | 2025-07-15 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 72cac233-1a02-37ec-90ea-bb254927c6c0 | -7.6679 | -56.74906 | 2025-07-15 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bbaa1a74-f6cd-3396-aff9-45558d459084 | -9.35772 | -58.83904 | 2025-07-15 05:23:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75c9e0f9-d353-3b90-993b-8ff35768e2e3 | -9.78585 | -62.48978 | 2025-07-15 05:23:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62506623-c78e-3246-ac3b-51f06ee86349 | -4.22866 | -47.76973 | 2025-07-15 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 117c25f2-9113-3212-aee9-92336937a968 | -10.55393 | -54.25451 | 2025-07-15 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a3e92a67-eb8f-3fe8-aa4b-75bf52ea5b7f | -10.87763 | -54.05445 | 2025-07-15 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08fe5f74-fd59-3587-a03c-a79f44ec5ae6 | -10.05996 | -59.10762 | 2025-07-15 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 52afbb03-d90d-3b14-a536-29f7d05ab094 | -9.29827 | -63.72371 | 2025-07-15 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6abecb14-27a0-3b46-8b3a-89b3b63c0017 | -8.60923 | -47.44417 | 2025-07-15 05:23:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46b7476f-2ead-3069-8597-b812c6c05f59 | -10.50223 | -53.57695 | 2025-07-15 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19f24952-2e2c-3aeb-86f7-8f82e38956e3 | -7.19066 | -59.83973 | 2025-07-15 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70c6ba81-1ea6-3df2-8c8e-90e35c8271bb | -3.38201 | -47.47112 | 2025-07-15 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3d06ebc2-4572-39c5-856d-e1027d6c0e5d | -9.02277 | -61.22559 | 2025-07-15 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6bbc4e5-fe77-3aa7-a43d-924e24fe3ea8 | -3.58656 | -47.52438 | 2025-07-15 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| dea9874a-1e55-3eb5-893e-11bf2d4e147d | -8.30853 | -55.1037 | 2025-07-15 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0eb906be-9471-348c-b100-57231ca6a6f7 | -3.58738 | -47.51865 | 2025-07-15 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| df851c06-564e-3d21-8a5c-bcbd430a0750 | -4.03349 | -48.06807 | 2025-07-15 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa2f3fab-2075-3d17-88d7-a71819750565 | -9.80895 | -47.74773 | 2025-07-15 05:23:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 34d31fac-9b2e-3b1d-b382-ac8736d26384 | -10.87203 | -54.05946 | 2025-07-15 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 683a4e61-113c-3689-8f1b-a68fdb8783c3 | -4.27557 | -48.18417 | 2025-07-15 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1bc238d0-e50b-3b1f-8024-255b9edb4555 | -3.75769 | -47.11715 | 2025-07-15 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 06a5c92e-7866-3d75-98bb-013fee9cca6c | -10.09725 | -60.49733 | 2025-07-15 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4739af1e-ebcd-3947-ad2a-1f4383449bb4 | -9.01797 | -59.54632 | 2025-07-15 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 893bcc10-3cb8-3f25-8a67-f429e35ce422 | -9.02829 | -61.23358 | 2025-07-15 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bdd2ea7c-e825-31ec-ae20-e08cb0986d8d | -2.91917 | -48.24249 | 2025-07-15 05:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c718f4ca-f777-3402-9ff7-0b9c42e355b6 | -10.88242 | -54.05515 | 2025-07-15 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e4e1365e-09ee-3563-bbd4-f1cf9e500df3 | -9.24961 | -58.76256 | 2025-07-15 05:23:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2d4e39b-fa9b-3ee6-904b-19e04d9863e8 | -9.36122 | -58.83959 | 2025-07-15 05:23:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 625811b8-8354-37d6-9c31-39f07a1e1c0f | -3.51079 | -47.21725 | 2025-07-15 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7465277e-fb67-3806-90d1-f1ab9d719f17 | -10.54387 | -54.25807 | 2025-07-15 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4eb24af-2d5c-303f-bd06-9b69db946900 | -10.56642 | -49.14081 | 2025-07-15 05:23:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 06fa92b9-7ba4-34d6-b364-50cf60df0107 | -7.9011 | -61.52335 | 2025-07-15 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 17e457cb-7bff-3dbb-b212-2ac4d4a81090 | -2.92208 | -48.24082 | 2025-07-15 05:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61c9a35f-1c4f-3977-81f2-0feb4269c8ff | -4.01091 | -49.47258 | 2025-07-15 05:23:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d230e49f-81db-36ef-9e02-ee3682ae164d | -9.78919 | -62.49032 | 2025-07-15 05:23:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31a85d21-9084-339d-82aa-f29cd4f8581d | -2.92546 | -48.24352 | 2025-07-15 05:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0473faba-f475-3863-aa8c-42d23ead8d8c | -9.3548 | -58.83457 | 2025-07-15 05:23:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3c1e745-3315-3334-bea9-890cd182d646 | -10.1335 | -57.77473 | 2025-07-15 05:23:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24ae4417-4b10-30e3-b108-e0accd374b66 | -10.10059 | -60.49784 | 2025-07-15 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8fcc6e2-74f8-34f2-9189-f350038fc5b2 | -7.78258 | -61.36881 | 2025-07-15 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37eb6ee9-21bd-30e3-a663-1928540bc776 | -4.03995 | -48.06905 | 2025-07-15 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bcb1f7ec-bd70-3f70-81e1-66658c4c858f | -4.68476 | -48.86483 | 2025-07-15 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ec50539-8764-3ebc-87cf-ac2c0efa54fd | -9.33421 | -58.84406 | 2025-07-15 05:23:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cad31f1-2867-3d40-8955-8c263e23af84 | -10.06175 | -59.10888 | 2025-07-15 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a91c06ab-3bc9-3d9f-840e-0b5d437bcf3e | -10.87691 | -54.05978 | 2025-07-15 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d9bc89af-be58-3f3e-9a3d-c2a297d2c1b3 | -9.81272 | -47.7527 | 2025-07-15 05:23:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2b9f1780-959e-3287-b55e-1d27fb168a74 | -9.02001 | -61.2216 | 2025-07-15 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eeb871a1-6f75-35cb-a163-bb2b65d9e060 | -10.88848 | -54.04539 | 2025-07-15 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c6b154cc-46d5-3a2e-b56d-156c6e1fe847 | -9.29764 | -63.72758 | 2025-07-15 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7ace1bd1-87bd-35b0-bcb9-00d7801306c8 | -10.05478 | -59.1078 | 2025-07-15 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ccc439e1-5a97-3bfa-81e8-0e4ff5808ccb | -10.28777 | -47.61758 | 2025-07-15 05:23:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34130a06-d875-3515-aff7-f2ef2c3d2e37 | -10.67663 | -56.55524 | 2025-07-15 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 803b4e98-0e1b-3ae8-b57a-cab24e34f2c3 | -10.86252 | -54.05777 | 2025-07-15 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4f792c78-bd9e-3163-bb91-497d6fe30375 | -10.6726 | -56.5546 | 2025-07-15 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6474fcc8-4c6a-3d62-88b0-2e6d479ddeba | -8.38591 | -51.07695 | 2025-07-15 05:23:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4e4840f1-c61e-3e17-861f-f7bf0d900025 | -2.91288 | -48.24152 | 2025-07-15 05:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ba33a0f-7182-39c2-a539-9a115215e76b | -9.01562 | -61.22802 | 2025-07-15 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2c57daf-f1d2-38c6-a7d0-3c31085ba001 | -9.65954 | -63.44537 | 2025-07-15 05:23:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e23f700e-b500-3040-bc80-877167cfc903 | -8.59581 | -47.43557 | 2025-07-15 05:23:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5f31a466-051b-36eb-9fc1-e1f1e0aab850 | -9.01616 | -61.22454 | 2025-07-15 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 930605cb-ee5d-3641-b421-330d517f5a88 | -10.54923 | -54.25376 | 2025-07-15 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ada35dd6-3920-3a9c-8c3c-dace65f1b955 | -3.75681 | -47.12332 | 2025-07-15 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 886c63e9-718a-3d7a-8831-361adef19393 | -8.60292 | -47.43649 | 2025-07-15 05:23:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 885b1ef2-b31b-31ff-91d2-0ec4dfeba92a | -7.89167 | -61.47553 | 2025-07-15 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66fd7589-7fc3-3455-9917-720957ca5db3 | -10.06234 | -59.10499 | 2025-07-15 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b82627b-b816-3f40-a334-ab569df76a06 | -10.57366 | -49.13605 | 2025-07-15 05:23:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| b95655d5-afa3-3c2a-a82c-d7721ed636b7 | -10.13284 | -57.77924 | 2025-07-15 05:23:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a7a6817-da03-3939-aae9-3e5b51882855 | -9.7361 | -63.4073 | 2025-07-15 05:23:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c70c77b-ce44-3e46-890a-efe43374cd4b | -3.38118 | -47.47691 | 2025-07-15 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 38a16735-4a30-3920-9628-00fdd3ea1e8e | -9.97997 | -48.08174 | 2025-07-15 05:23:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2d76743c-e0d6-31d8-8b04-8da22b00b9c1 | -9.6461 | -65.73811 | 2025-07-15 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bb79c7b1-b1da-38f2-84ff-2cf4afcfb685 | -10.88299 | -54.05012 | 2025-07-15 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d2c009c0-40d1-3e3f-9a5a-20507661efef | -10.06053 | -59.10373 | 2025-07-15 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 31464dde-c868-380d-9a2c-a9529078d3ef | -10.05827 | -59.10833 | 2025-07-15 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4591fa5-e5f5-391d-ac41-35dec650b35a | -8.65066 | -47.75426 | 2025-07-15 05:23:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e28c9ad4-fb0a-3ff3-afdc-17f447a0fe40 | -10.49731 | -53.57618 | 2025-07-15 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55ad1040-f247-3d43-bf1f-60693f748367 | -10.28386 | -47.61485 | 2025-07-15 05:23:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ea0f6e0b-da1c-3acf-aa21-092a84875c5f | -4.03424 | -48.06272 | 2025-07-15 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e328f2e6-6b5d-32f5-a5e5-ec43f0adc0f9 | -9.35888 | -58.83117 | 2025-07-15 05:23:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 318eaea6-87d6-38cb-81e3-459c8ed211e3 | -2.92132 | -48.2458 | 2025-07-15 05:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a69f0caf-7427-3325-827c-54880e2d9362 | -9.29195 | -63.7187 | 2025-07-15 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 166befa4-58bd-3f0a-a334-aac6a90fdcff | -9.65612 | -63.44481 | 2025-07-15 05:23:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4c8b2d1-994e-3e9a-9add-3cb39d280202 | -9.01946 | -61.22507 | 2025-07-15 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11ba9b5a-a6e0-338b-917c-65ac3fd4a03b | -10.05944 | -59.10055 | 2025-07-15 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c38adb9-27ff-338d-a17f-52036e12e103 | -9.71648 | -61.28997 | 2025-07-15 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82533ae4-bf72-38bc-88ac-1d94af9b73c7 | -9.81351 | -47.74555 | 2025-07-15 05:23:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e33a6558-cb7e-3757-a03c-383e653faf58 | -2.91579 | -48.23985 | 2025-07-15 05:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 508a39a6-a340-3ef6-9840-2cdf189902af | -8.65147 | -47.74767 | 2025-07-15 05:23:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9bf2e504-f55e-3dc1-97f7-b0106ac0a4a5 | -10.05939 | -59.1115 | 2025-07-15 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4f83af96-a749-3eac-ad8f-d2dac76ad38f | -10.86723 | -54.05879 | 2025-07-15 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e22fca53-a8b4-33ca-8969-a8a5840d6880 | -4.01151 | -49.46829 | 2025-07-15 05:23:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21255887-0698-3c8a-ac52-c1e12417c3e1 | -10.96917 | -49.25243 | 2025-07-15 05:23:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de54c804-ae6f-325f-a137-725affcc3239 | -12.58201 | -56.98518 | 2025-07-15 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c96b3fa-d116-3930-9d8f-afbac0b3a098 | -15.08031 | -48.94534 | 2025-07-15 05:25:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 70d93171-8a81-3e24-ba1d-bfdc5a23c2fd | -7.03954 | -55.43602 | 2025-07-15 05:25:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef52458d-5ffc-31f6-94c7-19b15e7f95e7 | -18.44813 | -54.67463 | 2025-07-15 05:25:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44a9dc44-ccf6-33d6-9c0f-f662b4cbe437 | -6.87681 | -50.26787 | 2025-07-15 05:25:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 145ad8e3-f0ae-39a8-b87b-5e1b136bef91 | -10.98299 | -58.65918 | 2025-07-15 05:25:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9604fd94-46ba-3515-9abd-5effa43d00c5 | -14.49153 | -59.73272 | 2025-07-15 05:25:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README24.md)
