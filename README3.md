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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd68c067-29fb-32e2-96f0-8ef9a8d18e65 | -15.7729 | -41.28268 | 2024-10-25 00:24:00 | TERRA_M-M | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| d494c3bf-6bc0-3a89-a49d-854dd2987354 | -15.43369 | -41.14372 | 2024-10-25 00:24:00 | TERRA_M-M | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 35deaa37-55d2-3eac-87a4-ab5d04077a7e | -15.21413 | -44.73962 | 2024-10-25 00:24:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 18.5 |
| ff15a18d-c4c8-3ae1-9ba5-5e0a19cb84dd | -15.03431 | -42.29801 | 2024-10-25 00:24:00 | TERRA_M-M | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 093d4b6b-a338-3a1b-98aa-0205e4a95bbb | -15.03291 | -42.28723 | 2024-10-25 00:24:00 | TERRA_M-M | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| f536ee58-bfb2-311c-889e-c88906305c82 | -14.95296 | -43.17355 | 2024-10-25 00:24:00 | TERRA_M-M | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 7caa7131-d1f5-3e63-b10f-78de92f56b1f | -14.95139 | -43.16117 | 2024-10-25 00:24:00 | TERRA_M-M | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 56c83c28-2581-33e6-a223-d06efb89944c | -1.0445 | -47.6237 | 2024-10-25 00:25:11 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| f00b1f4c-bfcc-38d1-bdec-2df1f9b15cc2 | -1.1834 | -53.6771 | 2024-10-25 00:25:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 27281493-1166-30e7-9c37-ec848f8bfcd3 | -1.1834 | -53.6569 | 2024-10-25 00:25:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| a61e894a-0a03-3824-acc2-506e40e5bd04 | -2.6192 | -52.4564 | 2024-10-25 00:25:20 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| b8d23cd3-f3cb-3872-9376-6967793431bd | -2.6193 | -52.4359 | 2024-10-25 00:25:20 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 90b1cb00-56e1-3ee3-b65b-52714de787f1 | -2.6297 | -49.247 | 2024-10-25 00:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 115.0 |
| c81264f0-2d98-3b0a-a982-436f859bf760 | -2.6376 | -52.4559 | 2024-10-25 00:25:20 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 643d49bd-a662-31cc-b7b6-1331f0ec9074 | -2.6482 | -49.2465 | 2024-10-25 00:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| ad39a57e-c888-3c6d-982a-47e9c8a94059 | -2.796 | -49.2636 | 2024-10-25 00:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| e0e84de4-13d4-3810-94ff-f320a13e0ac9 | -2.796 | -49.2424 | 2024-10-25 00:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 136.0 |
| 73b862d1-c9ea-31d0-bed8-698478f530f1 | -2.8144 | -49.2631 | 2024-10-25 00:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 226.0 |
| af87c5be-9b16-340f-9952-239186c33b86 | -2.8145 | -49.2418 | 2024-10-25 00:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 271.9 |
| 7fd05e92-71f4-31e5-801a-1e058c7e7a70 | -2.9578 | -50.4198 | 2024-10-25 00:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 6b1a76c3-5d36-371e-9aae-4d06deb43df5 | -3.1071 | -45.7232 | 2024-10-25 00:25:23 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 3dd9dfcc-9411-31f8-a03d-f80a25045e26 | -3.1072 | -45.7009 | 2024-10-25 00:25:23 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 144.0 |
| 7eb010ae-5118-3c5c-9ff6-d9bd1bb7db21 | -3.1257 | -45.7225 | 2024-10-25 00:25:23 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 75.5 |
| f4854b74-6fa9-344a-85c2-b1b4072320a9 | -3.1258 | -45.7002 | 2024-10-25 00:25:23 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 1bbfdd01-2d23-35d8-868c-a5b0ee55ec4b | -3.2368 | -45.8077 | 2024-10-25 00:25:23 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 99f525bb-6ff0-3cb6-8f2f-735099efb892 | -3.2552 | -45.8293 | 2024-10-25 00:25:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 5813aa02-e16f-37d4-b16b-6ecff82242d9 | -3.2553 | -45.807 | 2024-10-25 00:25:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 284.1 |
| e5c1b6e2-dc21-37ed-91ee-d2054e70bce4 | -3.3124 | -49.5235 | 2024-10-25 00:25:24 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| d993549a-9775-3bf6-8aae-9b7762f6b288 | -3.4047 | -49.5415 | 2024-10-25 00:25:24 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 2e24f320-8f37-36c9-9194-a7eccf1fcde7 | -3.4048 | -49.5203 | 2024-10-25 00:25:24 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 831d5a9e-d336-31f6-be49-1314fd15d55b | -3.4605 | -45.6645 | 2024-10-25 00:25:25 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 99.4 |
| ee29d2fd-d5d7-3879-8bfa-130b1da04434 | -3.4791 | -45.6637 | 2024-10-25 00:25:25 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 93.3 |
| f041ea6c-657f-32fb-b841-5386fb5c35cb | -3.9394 | -46.445 | 2024-10-25 00:25:27 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 71.9 |
| fc9e3257-b33b-3ce0-8679-7887a2729e05 | -3.9396 | -46.4229 | 2024-10-25 00:25:27 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 3fd02047-0532-308b-8d96-121a2ce7295d | -3.958 | -46.4442 | 2024-10-25 00:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 73c5b422-5361-3938-b764-e4b62be36bc9 | -3.9581 | -46.422 | 2024-10-25 00:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 106.3 |
| cf0af4c0-2ec1-3d96-8ed6-b1519af55a8a | -4.2427 | -48.5689 | 2024-10-25 00:25:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 8bab8b35-3fbd-3b58-9af2-fcee444f82ce | -4.2429 | -48.5474 | 2024-10-25 00:25:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 129.5 |
| e6ffec0b-2c69-352c-b8aa-cbe07a84a965 | -4.244 | -48.3535 | 2024-10-25 00:25:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| c3f0a7a3-f12b-3db2-a549-e27e12bd38b9 | -4.2441 | -48.332 | 2024-10-25 00:25:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 11feeb64-1753-385e-a5d9-7504d4870df8 | -4.5231 | -48.2108 | 2024-10-25 00:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| db6d6aaf-0a5f-32ba-a1e2-e5d94c3f1316 | -4.58 | -48.0132 | 2024-10-25 00:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| a123f09d-95d6-393b-a8f0-49f2c38ac68d | -4.8423 | -45.0309 | 2024-10-25 00:25:32 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 53fb68d8-3621-3d8e-b7af-45bd7bd6efb7 | -5.6589 | -47.9093 | 2024-10-25 00:25:37 | GOES-16 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 58.5 |
| c5dcfcd0-a668-3548-a509-21cd99b3d4df | -6.5219 | -60.0457 | 2024-10-25 00:25:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 133.3 |
| 453cb70d-c603-379c-9312-223beca44037 | -6.522 | -60.0266 | 2024-10-25 00:25:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 117.5 |
| c5eb5512-bb99-337c-a688-cd6ffe7bfb30 | -6.6472 | -47.8642 | 2024-10-25 00:25:43 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 4b0ea325-d179-3160-a8a0-f560ff0125ef | -7.9046 | -63.7129 | 2024-10-25 00:25:51 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 3642aa1b-e612-3fc7-96c8-7f1a2090d449 | -7.923 | -63.7123 | 2024-10-25 00:25:51 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 32381944-0751-3e1e-b91e-d6c3af46d4ce | -8.9064 | -48.544 | 2024-10-25 00:25:56 | GOES-16 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 89.8 |
| dc25a614-8148-3b73-a484-b33887d33b97 | -9.6498 | -35.8492 | 2024-10-25 00:25:59 | GOES-16 | COQUEIRO SECO | ALAGOAS | Brasil | 2702207 | 27 | 33 | nan | nan | nan | Mata Atlântica | 65.6 |
| 6f15d0d2-c363-33c3-9844-792549d8c469 | -10.43651 | -48.07146 | 2024-10-25 00:26:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| e9c02ed8-1f6d-3da6-b6b0-a77de549eac5 | -10.42089 | -47.53136 | 2024-10-25 00:26:00 | TERRA_M-M | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| a492568d-63ec-3f58-8252-69be61afc021 | -10.25039 | -46.53519 | 2024-10-25 00:26:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 2a58e68b-358a-3b4d-947a-0613f8c5be58 | -10.24735 | -46.54119 | 2024-10-25 00:26:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 7a33c457-7b50-330d-aa30-236ab5c3d14f | -10.24504 | -46.5228 | 2024-10-25 00:26:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 8ceeeaa0-876e-3883-8517-6be91844e2d0 | -10.17113 | -47.90756 | 2024-10-25 00:26:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 1ce90d33-451d-3611-8f7e-188f1c367826 | -5.94469 | -39.68428 | 2024-10-25 00:26:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 178d945a-1ae4-31e3-bbe6-24f75ba75e0e | -14.12348 | -44.3139 | 2024-10-25 00:26:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 9499b6b5-6346-30c0-bc32-ae46b78c7dc0 | -14.12176 | -44.29956 | 2024-10-25 00:26:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 60dd62ba-3caa-3e11-8845-6d10c5dce29f | -9.6537 | -35.85962 | 2024-10-25 00:26:00 | TERRA_M-M | COQUEIRO SECO | ALAGOAS | Brasil | 2702207 | 27 | 33 | nan | nan | nan | Mata Atlântica | 109.3 |
| 4434c337-3c6a-35e1-8e36-1fede79337b1 | -9.35703 | -43.37272 | 2024-10-25 00:26:00 | TERRA_M-M | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 16f2f75a-3ef6-3fa0-ab7f-e3c2ea6704eb | -9.34743 | -43.37403 | 2024-10-25 00:26:00 | TERRA_M-M | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| ed4b1f6f-812e-339e-9c3d-d06dcf6ff8c4 | -8.67122 | -40.97377 | 2024-10-25 00:26:00 | TERRA_M-M | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 7.0 |
| db4ba62b-a083-3e17-83e6-0ef94a154318 | -8.66998 | -40.96489 | 2024-10-25 00:26:00 | TERRA_M-M | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 28.6 |
| 2a41767b-3db6-3992-9cab-22a612626b6b | -8.05092 | -41.15069 | 2024-10-25 00:26:00 | TERRA_M-M | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 3d287f1a-581e-3993-afae-6bed01329a9a | -7.79467 | -43.16987 | 2024-10-25 00:26:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 3e2c624b-cdc3-3a27-ab94-d2d797cbd1e6 | -7.68049 | -35.09564 | 2024-10-25 00:26:00 | TERRA_M-M | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 67.6 |
| ee4c09e3-c404-384d-a8dd-1f0d1af4158c | -7.67762 | -35.07739 | 2024-10-25 00:26:00 | TERRA_M-M | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 48.2 |
| 71b8e225-93e1-3896-9d07-0c9335f77251 | -7.27746 | -43.63909 | 2024-10-25 00:26:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| d9bb5fa8-31d8-3929-8826-580796c3340a | -6.95428 | -42.4814 | 2024-10-25 00:26:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 33.8 |
| 4ee10b22-fc82-3c5d-b126-36a000efbbe8 | -6.69 | -43.58968 | 2024-10-25 00:26:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2500a994-0582-3328-871a-679a36c0be9d | -6.64262 | -35.17582 | 2024-10-25 00:26:00 | TERRA_M-M | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 76.7 |
| d5bbf132-32d0-3ebb-baf7-0fe30043d49e | -6.64159 | -35.18172 | 2024-10-25 00:26:00 | TERRA_M-M | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 44.4 |
| 96aad1ec-e41e-365e-baa1-b71f627b91d3 | -6.63968 | -35.1573 | 2024-10-25 00:26:00 | TERRA_M-M | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 17.8 |
| 74ca715d-fe66-35b1-ae5f-c940d7c8b81c | -6.63879 | -35.16316 | 2024-10-25 00:26:00 | TERRA_M-M | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 43.1 |
| de35f7a7-7077-36c5-9279-6083512887f4 | -6.59057 | -42.24419 | 2024-10-25 00:26:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 9cf38ced-8a32-3a4b-b042-e6a4f7e59696 | -6.4612 | -41.77638 | 2024-10-25 00:26:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 6776c411-59ac-3ddb-9ab2-dee971f85055 | -14.48178 | -45.50156 | 2024-10-25 00:26:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 0a0db1b8-172e-33cf-9091-1f07fa0b5dd4 | -14.4797 | -45.48373 | 2024-10-25 00:26:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 3a243271-e819-3f66-9341-56c6f1e5ff68 | -14.31472 | -44.57587 | 2024-10-25 00:26:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| cd370b55-5018-3799-adaa-f304294dc206 | -14.31324 | -44.56716 | 2024-10-25 00:26:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 35427e5b-3b34-3232-9413-2866eb227a8a | -14.25161 | -43.26583 | 2024-10-25 00:26:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 34.2 |
| 8ead91cf-dec6-37fd-bcc9-65f42124d4bf | -14.25091 | -43.27264 | 2024-10-25 00:26:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 7cee4352-7cc5-3270-8313-f07603ea97a1 | -14.25003 | -43.25359 | 2024-10-25 00:26:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 13.7 |
| e530b4ae-2e98-33c9-9012-7c09caaf5dde | -14.24942 | -43.26038 | 2024-10-25 00:26:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 54.6 |
| afffe457-5c15-33c9-ba42-f44fedcf94c3 | -14.16256 | -44.17954 | 2024-10-25 00:26:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 9d582058-a80f-3471-b6e5-8d9e20f2545e | -14.14773 | -44.23867 | 2024-10-25 00:26:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| e6f61dac-e2e0-3122-9160-466b08c5d073 | -14.1252 | -44.32831 | 2024-10-25 00:26:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3bd6b7db-631d-3ca1-9cb8-2406eff4d633 | -14.10068 | -44.21585 | 2024-10-25 00:26:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5ab08776-095d-3533-9e3d-b789630eafd6 | -13.88212 | -43.09013 | 2024-10-25 00:26:00 | TERRA_M-M | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| c0aa087d-e80f-3aae-bebe-15c5a73d636b | -13.88066 | -43.0784 | 2024-10-25 00:26:00 | TERRA_M-M | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| e661acfe-fef6-30c4-b28f-8f7d389bdd17 | -13.77092 | -43.17731 | 2024-10-25 00:26:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 7db763a2-468f-3575-8f57-ba6d5afa7a97 | -13.75187 | -43.60289 | 2024-10-25 00:26:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| eb3018fe-5eca-3702-bdb2-584f686453b6 | -13.64957 | -44.29635 | 2024-10-25 00:26:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 7f714db8-8d39-3531-88c7-ca39a99cf893 | -13.64274 | -44.30552 | 2024-10-25 00:26:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 9d5eda9d-78cf-3a59-b412-6fe5918d4800 | -13.57976 | -42.30584 | 2024-10-25 00:26:00 | TERRA_M-M | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 6445d7d6-e9bc-39af-a529-4d338d7e1328 | -13.28896 | -43.96198 | 2024-10-25 00:26:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 5e308f87-83bc-3b1c-a4bb-583928c14be2 | -13.08633 | -43.08672 | 2024-10-25 00:26:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 60c13642-c3ab-3864-ac56-33153f393937 | -12.90032 | -45.07589 | 2024-10-25 00:26:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 24.4 |


[Clique aqui para ver as próximas entradas](README4.md)
