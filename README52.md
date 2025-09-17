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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cbf8127b-9a09-3c4d-b03f-8f0b871e817d | -8.99962 | -63.66303 | 2025-09-17 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2f88953-e1af-382a-ba15-732c72aba5b2 | -7.53762 | -63.38441 | 2025-09-17 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35ad4761-d507-3647-9a49-232eec6d0e2a | -4.92518 | -47.86737 | 2025-09-17 05:23:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f29d01bc-7b85-3acd-8f57-31dda072136b | -11.07449 | -49.75613 | 2025-09-17 05:23:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fef18009-acb5-371a-8fbe-927788b4fa62 | -4.13316 | -51.08301 | 2025-09-17 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da24157d-e4b2-3a85-b134-06afdb55c29d | -3.19742 | -54.97704 | 2025-09-17 05:23:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fb258301-ae17-304c-8211-f2b18140150c | -10.79388 | -50.72361 | 2025-09-17 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 987f48d9-1b08-3c68-b379-0567c78735f9 | -8.65702 | -62.67306 | 2025-09-17 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f92185c3-2c05-34d6-81ad-3632d13d9a9e | -2.70993 | -54.95559 | 2025-09-17 05:23:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6671630-014a-3b5f-8e44-4a22dba42193 | -8.77974 | -62.83419 | 2025-09-17 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ead6c26-6df3-3fac-bebc-33a7966e02f4 | -11.07388 | -49.76134 | 2025-09-17 05:23:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ddffa536-187e-37b1-b896-d20d9ff17c28 | -2.37618 | -47.63626 | 2025-09-17 05:23:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f119b0cd-9b43-38e2-b6d2-36199acadc8b | -5.67063 | -51.35859 | 2025-09-17 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fdf8039-6796-3ba4-9383-32915d83451f | -7.53424 | -63.60518 | 2025-09-17 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20d94410-ad0d-3d96-9a3c-1b2595a4760e | -5.80351 | -53.44301 | 2025-09-17 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4f9e34c-75b1-3bde-be39-00c28d7a3648 | -8.72502 | -62.4404 | 2025-09-17 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76e9a495-4257-314c-85cf-2be875a48a4c | -7.53825 | -63.38055 | 2025-09-17 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b11f917a-6e6c-3005-84e3-d8e2193012ff | -7.56803 | -67.38397 | 2025-09-17 05:23:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0677827-7e18-3c7c-8c8d-2a55888760ad | -8.43312 | -55.64309 | 2025-09-17 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a48478ba-3aa6-3bbe-b063-d7cd40698f3a | -2.91991 | -48.30383 | 2025-09-17 05:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| a7b0a945-73c3-3710-b4c0-fe5c74671454 | -3.18027 | -48.81197 | 2025-09-17 05:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c68626c7-bdbc-392a-84cf-74793e4449ed | -10.80484 | -50.70634 | 2025-09-17 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| acaf57c8-1024-32ba-b7ca-e6d180fff64f | -7.56877 | -67.37961 | 2025-09-17 05:23:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8a2bba3-4d50-382e-96d7-8450254ef86f | -4.92028 | -47.86689 | 2025-09-17 05:23:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 723d9199-8b62-3680-9eca-a51389661fe5 | -8.84798 | -62.92786 | 2025-09-17 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 637b5c19-c9df-300f-a678-f83845d9b1ae | -3.6905 | -49.01677 | 2025-09-17 05:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1a761a82-a4ef-3dd4-8673-5ad0c128894b | -5.31398 | -55.88001 | 2025-09-17 05:23:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 541057e0-87a0-3e11-a4ff-2e5beec942ea | -10.42538 | -50.65757 | 2025-09-17 05:23:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6d9e59a-198a-318f-a17a-594d94b350cc | -2.9222 | -48.30361 | 2025-09-17 05:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 47f7511b-9f01-3ba9-aef6-bdd30a6c5ae4 | -3.32097 | -54.93116 | 2025-09-17 05:23:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 629a4e16-9acb-3167-a7ba-31dde2119a91 | -9.4738 | -54.46816 | 2025-09-17 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f6989e60-bad5-3e8f-91a2-21f1b43070b4 | -2.83124 | -48.66249 | 2025-09-17 05:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 50a2e347-0300-3128-b03a-90d900af2a85 | -9.48098 | -48.27242 | 2025-09-17 05:23:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 26045880-a901-3243-87e5-1d9946c3a2ae | -8.23233 | -71.03082 | 2025-09-17 05:23:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89ee08d3-8f7f-3a2a-8589-0d71da8bc1c1 | -10.81147 | -50.65271 | 2025-09-17 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 712a6c76-1333-369f-91d9-6d12c05ee1e0 | -11.59625 | -49.8197 | 2025-09-17 05:23:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0696225d-b0a5-358b-8a12-58b0ef1ba6c2 | -8.71776 | -62.44291 | 2025-09-17 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 57b92b4d-1463-3e1a-998a-c387f268738d | -7.50787 | -63.72366 | 2025-09-17 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6ecfd6f-2ed4-31d8-8113-87a80f40a2b9 | -5.63661 | -51.71152 | 2025-09-17 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09d10612-4987-31d8-b084-d971048a058d | -10.81363 | -50.65819 | 2025-09-17 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 38508b45-6e32-3acc-b340-85ec31fac583 | -2.92062 | -48.29878 | 2025-09-17 05:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| b1e875d0-0f3e-36af-8a25-2b97ec3fde22 | -7.50433 | -63.72308 | 2025-09-17 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf37fc94-fd17-32cf-8477-76cc378d564e | -8.65365 | -62.67252 | 2025-09-17 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5e8778b4-abd5-33c7-a240-75276d93b22f | -11.351 | -50.86125 | 2025-09-17 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 01358b4a-4fbe-3de2-b92c-a598fb8428d7 | -10.62817 | -48.75299 | 2025-09-17 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6c9edf06-004c-3e31-9b2c-cf12b460b08b | -10.80429 | -50.71079 | 2025-09-17 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3b7dc47f-ecc0-37b0-b839-ea6a836bd56b | -7.48102 | -63.77712 | 2025-09-17 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfdcf698-0d47-357b-8ee5-b276e7cc7f21 | -9.07321 | -50.31584 | 2025-09-17 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d273937f-444f-3f65-829b-19309f57643a | -8.71498 | -62.43879 | 2025-09-17 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 89e439ec-0a9a-3c58-8fb2-26490b94bb1a | -4.92684 | -47.86805 | 2025-09-17 05:23:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7027c4f2-95b3-3df1-adc7-cde1c1dd5812 | -8.77915 | -62.83784 | 2025-09-17 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f042b5b8-dbe6-3517-8eb0-45e7c04079d7 | -10.81415 | -50.65369 | 2025-09-17 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3b7448a8-91d1-3187-91d3-29c346dd6ddf | -3.50867 | -48.44683 | 2025-09-17 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 21a778f1-c493-3a11-b1d7-248a4e28a681 | -9.00246 | -63.66747 | 2025-09-17 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d76cf8f2-e781-3146-8150-b16075867545 | -9.00309 | -63.66359 | 2025-09-17 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46f32c03-b4e9-3a9a-8485-3cb6175236d6 | -8.71833 | -62.43933 | 2025-09-17 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 54050882-c1b0-3c9c-9fac-a6ad9a52b019 | -3.19342 | -54.97639 | 2025-09-17 05:23:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cd8eaa5-2e63-3b02-82bb-bc7716ab760e | -2.38347 | -47.63177 | 2025-09-17 05:23:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| afc5aba5-6e3c-3fb2-8976-f6d66ef468ef | -3.23828 | -46.78872 | 2025-09-17 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 217f724d-ca7a-3997-8b9a-b7cd1cee5a21 | -2.26 | -47.84503 | 2025-09-17 05:23:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e43bdcfb-b79f-3471-9013-a3d2e44c5d81 | -8.77577 | -62.8373 | 2025-09-17 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df5edfa1-ef00-3cf3-91f1-8b9f93f915fe | -8.6497 | -62.6756 | 2025-09-17 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07bffc2c-9d76-3ba4-9fe6-d98634bce52d | -9.07977 | -50.31212 | 2025-09-17 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 442d702f-8fec-3a37-98d7-08dcd4a08055 | -5.63707 | -51.70832 | 2025-09-17 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e847f80-64fa-347f-af9c-daa8dd1a32cb | -5.61399 | -51.72128 | 2025-09-17 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8609dbf-d039-380f-841d-1264293a42ea | -7.53712 | -63.60971 | 2025-09-17 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ef341f3-959c-3667-9c78-b5bb75ecb0ca | -2.92295 | -48.29861 | 2025-09-17 05:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 64532254-6a51-3d77-be34-6eabffbc958b | -7.47747 | -63.77655 | 2025-09-17 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ed0dd1f-d046-3557-8927-ac5f7419f21e | -6.91712 | -63.02675 | 2025-09-17 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d54f0a0a-1327-30e9-8107-675d0c91662f | -10.80789 | -50.70743 | 2025-09-17 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 35fad392-4fb9-3313-bd11-e31ac6348206 | -10.63148 | -48.75466 | 2025-09-17 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 943165da-4145-394f-afda-1346be689ba7 | -4.36071 | -54.75491 | 2025-09-17 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb700d8e-0e40-35dd-8481-64ef4563a9e1 | -3.11684 | -59.92881 | 2025-09-17 05:23:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a5376f10-c8cf-3a0d-89b1-ba4b032d2b2a | -5.80882 | -53.43895 | 2025-09-17 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f3f6fc3-8dc1-36be-846c-d261bc5822aa | -8.71889 | -62.43575 | 2025-09-17 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c8999b53-aeb8-3d13-8bb1-e4286fd2b4ac | -8.43261 | -55.64666 | 2025-09-17 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56b05ee0-341b-3038-9deb-de5eb4be654e | -10.80192 | -50.7066 | 2025-09-17 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a53ad6b9-6241-37ad-ab7e-689224e438f2 | -6.92057 | -63.0273 | 2025-09-17 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca467237-6cf0-3af3-8819-72106c359781 | -10.79613 | -50.72776 | 2025-09-17 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 741cb626-e9d3-3cb3-95db-8b2abc049471 | -9.84507 | -55.24832 | 2025-09-17 05:23:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 797e9d3c-2a80-3ada-a9da-e7a7fe02db64 | -9.55809 | -66.7342 | 2025-09-17 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d0c60231-de75-3b9c-9c14-6c68300f5e4b | -7.5114 | -63.72424 | 2025-09-17 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c16a4688-1ed3-305a-b224-b9e90da3639a | -9.55873 | -66.7305 | 2025-09-17 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a27e870a-1446-364e-a273-cbe7cfb9efef | -6.9165 | -63.03056 | 2025-09-17 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf8cccca-6d4d-3110-8a2e-e37f217d5daf | -3.18519 | -48.81251 | 2025-09-17 05:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b47c9192-fc66-367e-98fd-549eac7926c9 | -11.60262 | -49.82051 | 2025-09-17 05:23:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1fd06d3a-b98c-3f77-ab5c-7c6c26db09bb | -2.3766 | -47.63616 | 2025-09-17 05:23:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2ab40d70-634f-39a1-ab5c-230532154c35 | -2.98193 | -60.98395 | 2025-09-17 05:23:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4388ccb1-0350-3d86-be6f-743bf3937dda | -8.8474 | -62.93154 | 2025-09-17 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 394f429a-0491-3c63-a482-0a0c0297e989 | -7.71245 | -55.45134 | 2025-09-17 05:25:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26a8faa9-2182-30c9-92b7-1ebe0ca21624 | -12.37915 | -51.40929 | 2025-09-17 05:25:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4fc184b9-029b-395c-bc72-24db26425abe | -7.89069 | -48.16017 | 2025-09-17 05:25:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5af4b2fc-03c6-3b44-900b-8558bb76a45c | -13.14709 | -51.61082 | 2025-09-17 05:25:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22b0bb20-46c7-34f2-a87b-be43388510a6 | -7.61122 | -47.47008 | 2025-09-17 05:25:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ff5cb499-cafe-3f18-ac94-b93b5ac1d56e | -12.59338 | -62.96283 | 2025-09-17 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b0301d72-d6b1-3357-b819-051f452d35fc | -10.62666 | -69.48049 | 2025-09-17 05:25:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58008743-8e57-37e2-b3e7-3a4359ebab0f | -18.02779 | -50.94434 | 2025-09-17 05:25:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 28.0 |
| c3a69a05-406e-360b-a12f-3028fb049473 | -13.98952 | -51.67813 | 2025-09-17 05:25:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b7b909dc-1ac2-31bf-9814-f0c828c54187 | -12.5967 | -62.96338 | 2025-09-17 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 353a030b-8606-34df-84a8-334493284a33 | -15.83639 | -59.48156 | 2025-09-17 05:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README53.md)
