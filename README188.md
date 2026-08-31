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

## Dados Diários - Página 188

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17af0462-bb26-3149-b4ad-fb2d46187bf4 | -6.1796 | -55.4542 | 2026-08-31 18:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 9ac84398-3860-33be-ac7b-c1f7b3f60974 | -3.1267 | -61.1811 | 2026-08-31 18:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 171.6 |
| 49f12c38-2e26-340b-a5b8-36ec07fe59e5 | -9.1719 | -59.5017 | 2026-08-31 18:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| c0442925-dc89-3525-b439-b15bf410149b | -3.1997 | -61.1799 | 2026-08-31 18:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| e6440fbb-3c3f-364c-81b8-bfdb40fafe3c | -6.3875 | -54.7646 | 2026-08-31 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 4e4a5f54-e8c5-3e8b-a465-2dc7e8410227 | -11.2478 | -45.1425 | 2026-08-31 18:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 33b27ce9-4497-33a0-bd51-a0afc6415758 | -2.8377 | -43.5962 | 2026-08-31 18:40:00 | GOES-19 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| dcc11460-a355-32d9-9e30-3d8f05462bd2 | -9.19 | -59.5783 | 2026-08-31 18:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 85a3c758-98ad-3fc0-8acc-cd85e936f1b9 | -8.8207 | -71.243 | 2026-08-31 18:40:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 6f02ed98-2276-3475-8042-122cd379d7ae | -7.6253 | -55.2787 | 2026-08-31 18:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 9722407c-c574-3d8a-baf2-23014bd7200f | -7.7938 | -44.084 | 2026-08-31 18:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 2b3edf3d-ae41-338b-a476-a9790fa15d91 | -13.1839 | -55.6479 | 2026-08-31 18:40:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 49.2 |
| d84a381c-1f65-331d-b21e-fb5f2052ac2e | -11.1995 | -55.1008 | 2026-08-31 18:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 85a40837-6dd9-37ef-bd17-8da5e0f2fc2a | -6.9521 | -58.9506 | 2026-08-31 18:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 3bea799d-3477-39fc-a5c1-0b3c765b4c9c | -9.1711 | -59.618 | 2026-08-31 18:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| a69f2536-3254-3a90-b0b2-316a00b9671b | -8.9873 | -65.4379 | 2026-08-31 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 055a03e6-80e3-3701-8f1f-55db6777f923 | -7.4735 | -61.3846 | 2026-08-31 18:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 9c75ca69-adfb-37a2-a6b1-aaa224f99f14 | -9.4908 | -57.0144 | 2026-08-31 18:40:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| f65267ab-e8c8-392f-ae0e-b63f326bc3a8 | -11.2103 | -45.1017 | 2026-08-31 18:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 5adffb8f-310c-3337-b970-15e6af7f74e1 | -12.9032 | -45.8382 | 2026-08-31 18:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 8146b012-af19-37cc-aef7-7bc91934ddcf | -9.0431 | -65.3988 | 2026-08-31 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| dd8c3204-2084-341a-84c2-95c6c64e92eb | -11.7973 | -47.6672 | 2026-08-31 18:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 3b456beb-628f-3d4c-9120-b4298efa243e | -3.1839 | -60.1559 | 2026-08-31 18:40:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 38565b68-090f-396f-88cb-0d96fdd28b6c | -11.4828 | -58.5159 | 2026-08-31 18:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 04d27c51-7b60-3246-9f03-9d37e9573ab6 | -8.8706 | -66.7636 | 2026-08-31 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 208.2 |
| a179040c-a739-3ab3-a9e1-3cdb110ddc3d | -12.0733 | -44.999 | 2026-08-31 18:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 819ad189-e9af-380b-b49d-301ac24b51a6 | -5.2548 | -55.8907 | 2026-08-31 18:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| b00d64a6-575c-336d-b8c8-08fba9057a21 | -9.6075 | -61.0222 | 2026-08-31 18:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 37.9 |
| aa27a96d-6f3e-3375-8549-7a6df76da129 | -9.12 | -61.6011 | 2026-08-31 18:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 729f993e-41ca-36d8-a2a3-1b1b6ef24655 | -12.9589 | -45.944 | 2026-08-31 18:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 140.8 |
| ad63ef5f-d95d-3d6e-829a-276546f30d01 | -13.967 | -54.395 | 2026-08-31 18:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 50263102-567e-3a30-91c3-4024971ab75a | -6.1109 | -57.684 | 2026-08-31 18:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 11a6d39b-6d0e-32f9-94f8-1d4c29bed0e4 | -15.653 | -56.3854 | 2026-08-31 18:40:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 0e5a99a7-c82a-359b-9b89-9fc04690dfc7 | -10.9865 | -48.3869 | 2026-08-31 18:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| a029ff34-9fd7-3b09-8236-2b9f2bf4baff | -9.173 | -59.3659 | 2026-08-31 18:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| b632ac6a-0514-3436-a014-45d43cc2960b | -9.208 | -65.8044 | 2026-08-31 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 257896a4-610c-3d29-9c86-5e52f5993ab4 | -11.2506 | -53.9941 | 2026-08-31 18:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| cea23867-f718-39d4-8317-a9eb43336a4a | -9.02 | -57.5377 | 2026-08-31 18:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 59079390-6578-3a0b-ac83-8f568cdbcdfd | -9.0058 | -65.4373 | 2026-08-31 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 107.3 |
| d28818bf-bc69-3755-a164-9fe8f8fcd71e | -7.4734 | -61.4037 | 2026-08-31 18:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 82.0 |
| e6f44648-aa40-3331-902e-0a3e2fc5cba0 | -8.9295 | -62.3712 | 2026-08-31 18:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 60.7 |
| a273ab59-2f15-3c95-801a-84fb3f9e69a2 | -5.9636 | -57.6704 | 2026-08-31 18:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 14dfc727-b70c-3f2d-9e2a-01d1563219b6 | -6.77 | -55.6445 | 2026-08-31 18:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 07f194fb-b8fe-3115-8905-4e60aa9e86a3 | -3.6847 | -64.6138 | 2026-08-31 18:50:00 | GOES-19 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| e950e07f-3583-3631-bc9b-c54c0c3c2659 | -8.8521 | -66.7641 | 2026-08-31 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 130.0 |
| 08e38d97-38be-3555-b3f0-79cf272e1a18 | -5.8692 | -52.0868 | 2026-08-31 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| f6f50107-7072-3ba4-b49a-91de321958ab | -9.9708 | -53.9419 | 2026-08-31 18:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 121.2 |
| dc2d1025-1073-3a4b-a123-0f4a007d1b65 | -15.653 | -56.3854 | 2026-08-31 18:50:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 3110f363-bf36-318f-96fb-307e6a416b94 | -7.1435 | -72.864 | 2026-08-31 18:50:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| e5b0a7fb-72ce-3165-8a1c-73ec86c021b6 | -6.6792 | -52.864 | 2026-08-31 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| ed008f7a-9c80-3047-82e1-b68d2411f2f7 | -6.1294 | -57.6833 | 2026-08-31 18:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 365fbebe-635d-31a3-a16c-dede82942274 | -7.4734 | -61.4037 | 2026-08-31 18:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 1470aeab-e3f9-34c8-a0e4-9b68f59fdcb8 | -8.5363 | -67.1617 | 2026-08-31 18:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 26bc0380-d923-3e17-8dda-d61613a4b4db | -3.4002 | -61.3276 | 2026-08-31 18:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 83c2623b-bb5f-3d9f-8a33-7c80ed1c4766 | -12.0733 | -44.999 | 2026-08-31 18:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 82976734-271b-3207-9558-3f40b658bcb5 | -11.1995 | -55.1008 | 2026-08-31 18:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 7bcbd8e8-8e69-3cb5-b7a3-b985fc0ec39d | -10.3205 | -49.9567 | 2026-08-31 18:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 23190933-a565-3665-9096-6f0bf8915dcc | -4.1515 | -60.7068 | 2026-08-31 18:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 123.1 |
| 49d92e45-d09a-37c7-ba26-b9ae4c995eed | -10.3199 | -49.9996 | 2026-08-31 18:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 3f33e08a-f065-3826-b848-3ed05cd8fa42 | -7.2934 | -60.5713 | 2026-08-31 18:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.4 |
| e0ef8da3-358e-3fdd-ae38-3a91ce67bdfc | -3.1267 | -61.1811 | 2026-08-31 18:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 154.3 |
| b318fdd3-4d59-3623-9a30-e609c40cda6d | -10.4963 | -59.6001 | 2026-08-31 18:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 406330d1-833c-3dfb-898e-c6232884258f | -8.4896 | -70.6243 | 2026-08-31 18:50:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 66.3 |
| eef46f19-6792-3d77-bfe7-aa3725db1308 | -5.9451 | -57.6906 | 2026-08-31 18:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 120.8 |
| baae2c97-b432-302c-a504-9a0d5d6b9a62 | -9.1719 | -59.5017 | 2026-08-31 18:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 5ef7a42f-b09b-3193-97f6-0155bba2c20d | -9.6676 | -47.9429 | 2026-08-31 18:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 5d0c89ca-22c3-3022-86a4-45c179dac1eb | -5.2547 | -55.9105 | 2026-08-31 18:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 654f396e-0225-3bad-a54c-6a4791db159f | -6.6765 | -58.7492 | 2026-08-31 18:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 768d6474-156d-3368-9b1b-1ade7e220f24 | -11.6967 | -54.6081 | 2026-08-31 18:50:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 09df0c7c-18c7-38bb-93dc-dbe5facc124d | -9.8927 | -60.2752 | 2026-08-31 18:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| c551f538-feb2-3ead-8380-333868a8b12e | -11.5279 | -45.5162 | 2026-08-31 18:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| a568dd39-bf4b-33b6-a876-550877dc7853 | -14.2792 | -52.8758 | 2026-08-31 18:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 147.7 |
| e3d61ed4-32e7-34d9-980b-9eaab9a14d46 | -8.8644 | -68.5034 | 2026-08-31 18:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| c45c4aa5-4c73-35c6-b308-c084a2db46e6 | -11.7973 | -47.6672 | 2026-08-31 18:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 4ab8ce52-2564-3f42-9366-2d4bd983d231 | -10.3388 | -49.9977 | 2026-08-31 18:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 3e1e7d2c-0b7c-30ba-8e53-76f7fe572cb0 | -8.3601 | -70.8641 | 2026-08-31 18:50:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 8e34d6b0-b8fb-31e5-832d-246f60b7950d | -9.1459 | -60.5266 | 2026-08-31 18:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 2e6538e1-c7c5-3a9a-90b4-f701f61c3779 | -5.8537 | -57.5576 | 2026-08-31 18:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| a2acccc9-fc34-3869-8de1-5cecd376e606 | -8.9481 | -62.3704 | 2026-08-31 18:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 68.4 |
| e34d4688-d49a-3af7-987c-39795234730a | -14.5871 | -54.0944 | 2026-08-31 18:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| cd40fae3-5731-3d9d-bb79-aeb777f72f47 | -15.8844 | -56.4819 | 2026-08-31 18:50:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 5fc5b985-f05e-30e4-851a-9d6952a11f22 | -2.8565 | -43.5723 | 2026-08-31 18:50:00 | GOES-19 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| ceb1d8ce-f34e-343d-8783-87ba7136c417 | -3.4002 | -61.3465 | 2026-08-31 18:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 4686b4be-9760-364c-8300-0dc8464e4155 | -9.1419 | -61.1027 | 2026-08-31 18:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| fefd42f2-d874-3062-a070-b45850358ee6 | -2.6741 | -59.3628 | 2026-08-31 18:50:00 | GOES-19 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| a62bd4cc-a5f0-3e3c-a2f8-cab1f2286f83 | -10.1321 | -45.8825 | 2026-08-31 18:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 17c3c1fb-1ede-3a79-ab1e-fdede0acae2b | -2.6559 | -59.3631 | 2026-08-31 18:50:00 | GOES-19 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| c8bbf2bb-0971-3458-80fc-5276645f63f0 | -6.9177 | -55.6967 | 2026-08-31 18:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 70d87c77-5fc9-32bb-b69f-e3ab0e9ec64e | -12.0929 | -44.9728 | 2026-08-31 18:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 016572d7-9ad7-3662-bff8-58baeb24b2b6 | -9.971 | -53.9214 | 2026-08-31 18:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| be9040ed-082c-3697-a014-eca795aaaa5e | -2.6888 | -43.5785 | 2026-08-31 18:50:00 | GOES-19 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 7789320b-5662-3952-a5f8-13d542b61203 | -9.0245 | -65.3994 | 2026-08-31 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| cdc807a2-53c5-3549-bed1-b3ab96e7fd3e | -6.9521 | -58.9506 | 2026-08-31 18:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| c0326a16-7614-37a9-831e-2eeca61b1855 | -11.2506 | -53.9941 | 2026-08-31 18:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| b9e467de-5892-3666-b2ac-c61fafcf5120 | -3.4185 | -61.3273 | 2026-08-31 18:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| b9486824-185d-3348-bae1-266235fcc7d4 | -10.5644 | -46.1683 | 2026-08-31 18:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 59d5f932-d2a5-35bd-855b-463758125be6 | -3.6398 | -60.5656 | 2026-08-31 18:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 97.8 |
| fde6ff99-950c-30c6-af39-b6b68d49d07b | -9.0612 | -65.4916 | 2026-08-31 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 79aba850-02e6-33b4-ad0a-36d4fc01e2f8 | -10.7856 | -50.5066 | 2026-08-31 18:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| c41dbaac-4c22-3324-a664-0a586cad99a4 | -15.2468 | -56.3695 | 2026-08-31 18:50:00 | GOES-19 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |


[Clique aqui para ver as próximas entradas](README189.md)
