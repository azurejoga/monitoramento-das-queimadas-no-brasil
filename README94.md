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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96f8c053-c88a-31ef-9ea9-45db6ee590c9 | -14.34234 | -53.35865 | 2025-08-28 12:36:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 47b27575-36c0-37eb-8010-0c75d567b0fa | -12.89528 | -48.1217 | 2025-08-28 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| cda2df90-e0ee-346f-8b0f-b38b94609c80 | -14.32196 | -53.24439 | 2025-08-28 12:36:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 712cd024-5b9f-31cf-991a-6e8333aa96f1 | -13.0085 | -56.90271 | 2025-08-28 12:36:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 4a711f60-e575-3d9c-8bd1-ec0365c743e8 | -13.55389 | -46.90211 | 2025-08-28 12:36:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 30.6 |
| b12bf8ba-d8f8-3396-98e4-3ef91ec3f4cf | -14.36322 | -52.07791 | 2025-08-28 12:36:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 493eed9c-93e4-3faf-a59b-715018153703 | -15.57712 | -53.9871 | 2025-08-28 12:36:00 | TERRA_M-T | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e4f31f34-613c-3cc1-b74c-bca539662c0d | -16.98496 | -47.25864 | 2025-08-28 12:36:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 95085183-207b-3f16-86c0-75dd98c5e60c | -13.73358 | -51.90517 | 2025-08-28 12:36:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 58e9bf30-28ae-3859-b16c-f20a4192ee34 | -12.39935 | -45.04621 | 2025-08-28 12:36:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 15e21180-8ec0-3250-bbec-a5c294c4c334 | -12.7857 | -48.17822 | 2025-08-28 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| e70e21e6-f7dc-34c7-b4a9-6169491273a4 | -12.40222 | -45.04004 | 2025-08-28 12:36:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| c5b9b238-d616-3146-9ac3-88775bb9742e | -13.08378 | -46.32778 | 2025-08-28 12:36:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 62e4cef7-29aa-355e-80e8-110afdcb574b | -12.68437 | -48.17148 | 2025-08-28 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 805b7804-8975-37d3-bca7-48e8b8ea3328 | -13.73487 | -51.89611 | 2025-08-28 12:36:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cdbfdc92-4312-3ffb-a015-98386b800bfb | -12.96313 | -44.5757 | 2025-08-28 12:36:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 1573e580-99f8-398f-b5ee-b1e0b8dba708 | -18.03154 | -44.4123 | 2025-08-28 12:36:00 | TERRA_M-T | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 8f129f8a-e59f-391a-a3ae-cb1af555e677 | -20.10138 | -47.78123 | 2025-08-28 12:38:00 | TERRA_M-T | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 6aa5ffbb-5fad-3aa9-a2f2-d84e08f88dd0 | -20.10732 | -47.77539 | 2025-08-28 12:38:00 | TERRA_M-T | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 296.0 |
| 4d2ac770-f104-3f46-a31f-cee39c5c8344 | -21.28372 | -48.35106 | 2025-08-28 12:38:00 | TERRA_M-T | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 6d27d514-4d8e-338b-871c-b4aeb76e5b8d | -20.10536 | -47.79257 | 2025-08-28 12:38:00 | TERRA_M-T | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 212.9 |
| bb62df33-25b4-3a55-bbd6-609924f13660 | -20.1133 | -47.78246 | 2025-08-28 12:38:00 | TERRA_M-T | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 281.6 |
| bf318db5-26e4-3a74-b6f9-118105ef312f | -12.8805 | -48.1186 | 2025-08-28 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 98cf015a-f4a2-3233-9f90-5dd0fe821d7a | -12.6878 | -48.1677 | 2025-08-28 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 63e16cb6-7406-3ccb-998a-dfcf4443029f | -6.3881 | -45.6018 | 2025-08-28 12:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 7ac9aea2-22f8-31f2-bfba-75715d199620 | -12.3993 | -45.0183 | 2025-08-28 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| b40f8ba6-e4a3-3ec5-90c7-407f280f799d | -13.0863 | -46.3352 | 2025-08-28 12:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 577d2efd-ed24-329a-afa5-7cf8905540c5 | -11.3521 | -43.5423 | 2025-08-28 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 178.1 |
| 27193399-5f3a-3a3e-a4e2-a294d0887eec | -6.4355 | -44.5764 | 2025-08-28 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 92572914-60d6-3b8e-bb24-df22695f41fd | -11.3329 | -43.5452 | 2025-08-28 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 03360f4a-3c72-37ee-9596-4711d61d6fb6 | -6.8769 | -43.6385 | 2025-08-28 12:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| ddee08f2-5b01-3637-a16a-60056850a603 | -6.1593 | -44.0703 | 2025-08-28 12:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 122.2 |
| fb80ab2d-d52d-3d99-990b-97850e6ecbb5 | -7.3196 | -46.109 | 2025-08-28 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| c578749e-0ea7-38b7-b082-26ad9351bf63 | -13.0859 | -46.358 | 2025-08-28 12:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 64.1 |
| b1bce135-8fd9-36d0-a413-2b43280d7374 | -6.8772 | -43.6152 | 2025-08-28 12:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 788a9141-c52e-3ebc-ba52-711abe2fc8e2 | -6.1595 | -44.0472 | 2025-08-28 12:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 212.6 |
| d7a815d6-7bfb-3a39-9afc-9fe1bc2751bf | -12.8224 | -48.1489 | 2025-08-28 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 60ac6563-cdb4-3d58-94ed-c6773c5588ae | -7.233 | -45.4413 | 2025-08-28 12:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 8f9c493a-c589-3179-a0a4-5617ba4bf7a0 | -11.5703 | -46.3978 | 2025-08-28 12:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| ab579b92-641d-3281-b98f-fc94a34a65e6 | -11.5894 | -46.3952 | 2025-08-28 12:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 535dcc4e-8e8e-3cd7-908e-5076879dd111 | -10.3709 | -45.1686 | 2025-08-28 12:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 66.5 |
| a3b58628-9e28-318e-949a-8b63b9740105 | -10.308 | -46.8068 | 2025-08-28 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 24df30d8-84d1-34d2-83af-a31b6c0edcb6 | -6.4543 | -44.5749 | 2025-08-28 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 00c08f12-eba8-3a80-8b52-b6a2eb51c8b7 | -28.60884 | -50.12893 | 2025-08-28 12:40:00 | TERRA_M-T | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| f5f5451c-225c-310d-8ee0-3eadb2753266 | -28.60846 | -50.13938 | 2025-08-28 12:40:00 | TERRA_M-T | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| fd10eb5f-5599-3f64-8f13-d84b0b20954b | -9.7433 | -47.9348 | 2025-08-28 12:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| af550e25-e461-335c-ae46-bba6ee196480 | -6.4355 | -44.5764 | 2025-08-28 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 364c1722-7df5-3431-abe0-156cac673777 | -12.7071 | -48.1651 | 2025-08-28 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 1ba094d0-084b-3428-b594-8e5c0504ea30 | -6.4543 | -44.5749 | 2025-08-28 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| c3f3e0dc-c2c0-3d84-b5b2-7fc5ed025d95 | -12.9002 | -48.0936 | 2025-08-28 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 959e235d-f87c-38a1-8511-7bf1b54e3bbf | -11.3526 | -43.5187 | 2025-08-28 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| f4596e95-eb5e-33dc-91f5-df15a0443771 | -11.3329 | -43.5452 | 2025-08-28 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 217.9 |
| 9ae4054a-20ad-3296-857c-5f9f63828ea9 | -6.2755 | -43.6907 | 2025-08-28 12:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| ee5a8e4a-4fac-387a-9d19-52118f84d055 | -11.1523 | -54.3104 | 2025-08-28 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.6 |
| cfb7e884-e64d-300b-9944-f6379253474c | -10.308 | -46.8068 | 2025-08-28 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 3a08b2a9-28f0-3966-9b39-7ac1e7d3a274 | -7.3196 | -46.109 | 2025-08-28 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 088ec227-2f7f-35df-9864-b5ee5f6b6e5f | -12.8998 | -48.1158 | 2025-08-28 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 7cceb85e-b38f-3df8-b407-262aee231e3b | -12.7836 | -48.1766 | 2025-08-28 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| d4280232-fbf4-3681-adf1-fe3904c3b7cb | -6.8769 | -43.6385 | 2025-08-28 12:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 30c28682-3456-3aa6-997c-b8734ef48355 | -12.8032 | -48.1516 | 2025-08-28 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| cb062a97-b4bc-35db-8b7c-f64bb473e7c1 | -12.8224 | -48.1489 | 2025-08-28 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| aa052789-8ce2-309d-ba99-e4ac6a331611 | -7.233 | -45.4413 | 2025-08-28 12:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 62ef1ad6-4545-3295-ae45-5c7986f41915 | -6.1595 | -44.0472 | 2025-08-28 12:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 157.3 |
| c30c06f6-1438-3d3a-95e9-37218665d047 | -12.8028 | -48.1739 | 2025-08-28 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 9180518e-7593-34e4-bc6d-8531dcb80d06 | -6.8772 | -43.6152 | 2025-08-28 12:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 146.1 |
| ff0a72eb-cb0f-3adb-8997-a3e02ecc5c1a | -6.1593 | -44.0703 | 2025-08-28 12:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 3fcf7aa6-a0bf-396e-a605-c3f272346425 | -13.4208 | -46.9864 | 2025-08-28 12:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 292e2f30-f529-3307-8126-ae6d6b4703bd | -6.3881 | -45.6018 | 2025-08-28 12:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 676d2776-c647-3472-8909-a12b1442f7e3 | -8.2705 | -45.1605 | 2025-08-28 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 3b76efba-26ad-3a17-ba56-2d5bb538da25 | -6.896 | -43.6135 | 2025-08-28 12:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 843fce0a-edbd-3c40-a90e-156e2d6d2372 | -14.3303 | -53.2898 | 2025-08-28 12:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 2093b360-c223-36d2-9aaf-13feec112f97 | -9.4372 | -48.2518 | 2025-08-28 12:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| a68a69a0-6114-38d0-aaed-39a3ff437142 | -11.3521 | -43.5423 | 2025-08-28 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 327.5 |
| 4ed118fe-4b01-34c7-91c2-7a857aaddb9e | -13.0859 | -46.358 | 2025-08-28 12:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 8086567d-8cce-353c-bba9-09414f04402e | -13.0863 | -46.3352 | 2025-08-28 12:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 99.4 |
| d05248b7-2bd1-3543-a0bc-4d2bd477921e | -6.1595 | -44.0472 | 2025-08-28 13:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 172.0 |
| f3ef997f-8a02-3d42-8804-b58b9923abf0 | -6.4355 | -44.5764 | 2025-08-28 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 4af049f8-a071-31c6-a464-51f6314145e4 | -8.5251 | -47.4205 | 2025-08-28 13:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| fbd35f46-30ab-3a54-9690-d84a0c4b1843 | -13.4208 | -46.9864 | 2025-08-28 13:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| baaf7a04-dad6-3680-82ca-c4eaab5fee4b | -13.4427 | -46.8473 | 2025-08-28 13:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 6bec5b01-2a27-3d29-af6f-3253176c7ef5 | -11.1523 | -54.3104 | 2025-08-28 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 96f0f1ec-a8b2-336a-aedc-db3c05609033 | -9.2632 | -65.8959 | 2025-08-28 13:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 5602e134-1f52-359d-bdc8-40168147a5e0 | -11.3329 | -43.5452 | 2025-08-28 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 156.3 |
| 3d4ce837-9c7d-331c-b573-e4d417ea9850 | -12.8032 | -48.1516 | 2025-08-28 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| fd57e436-91ae-3fdd-a835-ab7001dea909 | -12.6878 | -48.1677 | 2025-08-28 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| b1a46078-240f-3821-84ce-835e2b0b186a | -7.3196 | -46.109 | 2025-08-28 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 522ed049-3740-37df-97dd-a8283ce36200 | -6.2755 | -43.6907 | 2025-08-28 13:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| f912cfea-fc95-3717-be00-92dae571cfd4 | -13.0859 | -46.358 | 2025-08-28 13:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 3c497d1e-be86-3515-8ccc-5da8881e93d0 | -11.3526 | -43.5187 | 2025-08-28 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 1ae8be03-f2d9-3a5a-bbbe-d4f18c75454f | -6.8769 | -43.6385 | 2025-08-28 13:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 266839eb-bf5d-3d05-89af-4f94cab90e5a | -11.3521 | -43.5423 | 2025-08-28 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 318.5 |
| f23839e8-cd18-3496-be1a-c9ad72526fff | -13.0863 | -46.3352 | 2025-08-28 13:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 856a6564-3868-3eb8-8e6f-fc17f062ec61 | -6.8583 | -43.6169 | 2025-08-28 13:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 0b5d082c-6ee0-3bb8-bb66-41f6e01073d5 | -12.8224 | -48.1489 | 2025-08-28 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| a4b87971-4291-3e1e-b592-b3f9f9c61841 | -12.8028 | -48.1739 | 2025-08-28 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| b72bf322-30db-37d9-b354-2c9b794fb502 | -6.8772 | -43.6152 | 2025-08-28 13:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 1f3e6885-9611-3532-95b5-a61361877171 | -6.4543 | -44.5749 | 2025-08-28 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| bc29e215-9c8a-3ea6-a1ea-b177773ceb1f | -9.6816 | -48.3139 | 2025-08-28 13:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 73c4ec23-f8ba-384c-b8c5-4eaee409039f | -6.1593 | -44.0703 | 2025-08-28 13:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 116.9 |
| afe6f89c-74f0-3943-8175-3e14716ed684 | -7.233 | -45.4413 | 2025-08-28 13:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |


[Clique aqui para ver as próximas entradas](README95.md)
