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
| 80350f23-5ad4-3d85-b9a8-0308fcfa3e13 | -13.38624 | -40.4746 | 2024-10-22 00:03:00 | TERRA_M-M | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| f5de2d32-b3eb-3630-a615-a62d1efc45de | -10.75181 | -37.02588 | 2024-10-22 00:05:00 | TERRA_M-M | SANTO AMARO DAS BROTAS | SERGIPE | Brasil | 2806602 | 28 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| b7417702-5d12-36ed-9900-d249abc35446 | -10.30382 | -36.64376 | 2024-10-22 00:05:00 | TERRA_M-M | SANTANA DO SÃO FRANCISCO | SERGIPE | Brasil | 2806404 | 28 | 33 | nan | nan | nan | Mata Atlântica | 25.9 |
| 950cda45-4a4c-3b90-b060-c386975cba8a | -10.30253 | -36.63423 | 2024-10-22 00:05:00 | TERRA_M-M | SANTANA DO SÃO FRANCISCO | SERGIPE | Brasil | 2806404 | 28 | 33 | nan | nan | nan | Mata Atlântica | 77.2 |
| b8d4067f-fa8e-31ac-bca2-e9d02c2c4369 | -10.29987 | -36.68349 | 2024-10-22 00:05:00 | TERRA_M-M | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |
| 90f282f6-0ea7-3eba-817c-f376756378c4 | -10.29857 | -36.67385 | 2024-10-22 00:05:00 | TERRA_M-M | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| cc1f4e7f-8d33-3030-900c-0952ce141d5f | -10.24601 | -36.35326 | 2024-10-22 00:05:00 | TERRA_M-M | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 49.2 |
| e8857163-7014-3b87-a63c-a906a805aa99 | -10.24474 | -36.34391 | 2024-10-22 00:05:00 | TERRA_M-M | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 60.5 |
| a39656e2-d7b3-3d1a-8e1a-5cb283c3eaf6 | -9.7897 | -36.31537 | 2024-10-22 00:05:00 | TERRA_M-M | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 519bd83b-8cc9-391b-8a53-54c1846e2c2e | -8.99221 | -37.15343 | 2024-10-22 00:05:00 | TERRA_M-M | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 14.4 |
| d169cb17-e4c5-39cc-9650-592649c5e0e9 | -1.165 | -53.6571 | 2024-10-22 00:05:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 9e987d0d-3dca-3bdb-85a5-4c7066b89a1e | -1.1834 | -53.6771 | 2024-10-22 00:05:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 30f0a621-e66b-3cdc-9741-a99434f96c63 | -1.1834 | -53.6569 | 2024-10-22 00:05:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| fb180377-601c-3f2e-8daa-e4baa5f6af85 | -2.5123 | -45.8773 | 2024-10-22 00:05:20 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 6b7965fd-1bc5-351f-988f-0536fe489313 | -2.7867 | -58.1492 | 2024-10-22 00:05:22 | GOES-16 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 7ee8c994-1f2a-31d7-84c6-13e0798a8667 | -2.7868 | -58.1299 | 2024-10-22 00:05:22 | GOES-16 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| c1acfb3a-673a-3ada-8b08-b4df0e79694f | -2.8482 | -45.4637 | 2024-10-22 00:05:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 991148d3-57ae-3bf7-9166-63438160ecd4 | -2.8668 | -45.4631 | 2024-10-22 00:05:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 100.9 |
| e2de88fa-681f-3cfa-b8dd-c0e1db4ea581 | -2.8703 | -54.4725 | 2024-10-22 00:05:22 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| d3092801-410d-3f33-9dca-86ad064565ec | -3.0581 | -53.2395 | 2024-10-22 00:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| cbbd8967-6b96-385a-961c-6db5bd8cffb3 | -3.0837 | -51.2708 | 2024-10-22 00:05:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| bbe7ada9-de04-3246-8627-130dd97a306e | -3.0838 | -51.25 | 2024-10-22 00:05:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| ff5724c7-191b-325d-8101-69cf6aa50ccd | -3.0917 | -54.1867 | 2024-10-22 00:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 50888ac3-3464-3040-b93e-600dbf305fdd | -3.0917 | -54.1666 | 2024-10-22 00:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 139.3 |
| 37fa013f-e813-3efc-bea5-26a93bc3ceee | -3.0918 | -54.1465 | 2024-10-22 00:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 1c5de3a0-b291-324d-95b0-da053cd6fc1a | -3.11 | -54.1862 | 2024-10-22 00:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 723dba9e-1921-3416-8605-4bd03d356179 | -3.1101 | -54.1661 | 2024-10-22 00:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 150.1 |
| 8309d419-db17-399a-9aa2-be2dc8f23c21 | -3.1102 | -54.146 | 2024-10-22 00:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 631dc904-fb0e-3124-8f50-82455cab43aa | -3.4576 | -54.6377 | 2024-10-22 00:05:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 8d680a17-1ea9-3b57-99a2-6d4297131eac | -3.9977 | -46.0202 | 2024-10-22 00:05:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 76.2 |
| b8c1360d-e029-3bb9-9140-e48208448abc | -4.0163 | -46.0193 | 2024-10-22 00:05:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 71.8 |
| c120692b-3b41-3481-baa9-0991f3d5d83d | -4.4655 | -42.9112 | 2024-10-22 00:05:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 7c5b44cc-b4f7-3b2c-8308-dd6dd7b59466 | -4.5386 | -45.8139 | 2024-10-22 00:05:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 67.4 |
| ddb3bb2e-9c51-3833-87f6-c49986d3686b | -4.5388 | -45.7915 | 2024-10-22 00:05:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 61.9 |
| e87e4a6e-19bd-3d30-b569-2285d62fbb96 | -4.5572 | -45.8128 | 2024-10-22 00:05:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 190.5 |
| 3b3c83d7-e627-3f87-a75a-45f6a422428c | -4.5574 | -45.7905 | 2024-10-22 00:05:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 146.3 |
| c840be8b-3068-38cb-bb56-4da56bc7a974 | -4.5759 | -45.8118 | 2024-10-22 00:05:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 4932b600-faa0-3312-becb-2c7032a03535 | -4.576 | -45.7894 | 2024-10-22 00:05:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 92.1 |
| e2cebf8f-da89-32cf-8ff7-1fd12bad549b | -4.6301 | -46.0545 | 2024-10-22 00:05:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 26d67a1a-9e42-387e-b842-34215c2c671a | -5.2305 | -43.1886 | 2024-10-22 00:05:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| b86bd317-6e9f-31e3-bdd5-bcbe3219be36 | -5.5905 | -44.8687 | 2024-10-22 00:05:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 87e6d8c4-2404-3ec8-a177-f09d37531ca1 | -5.9036 | -45.4127 | 2024-10-22 00:05:39 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 83a69b3c-fca9-3932-baf3-b4de144296b4 | -5.9223 | -45.4114 | 2024-10-22 00:05:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| a2aacb2f-c292-3836-bd8f-7b40c7e0fedb | -6.2334 | -44.1565 | 2024-10-22 00:05:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 44684c0d-d689-3fef-b072-d129eb4512ba | -6.2336 | -44.1335 | 2024-10-22 00:05:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| e3108699-a456-3951-be9e-4eed26de6726 | -6.2522 | -44.155 | 2024-10-22 00:05:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 00d8cef1-bf17-3591-8240-51612444cd45 | -6.2524 | -44.132 | 2024-10-22 00:05:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 7777f948-1bc8-35a1-95d2-4194b7234b15 | -7.8245 | -61.3709 | 2024-10-22 00:05:51 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 156872dd-189e-3a44-b036-614c527d1ee8 | -10.1822 | -68.1764 | 2024-10-22 00:06:05 | GOES-16 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 4f3d2e8b-9b12-38b3-93ed-6fdf0f03e4fe | -14.3029 | -59.3399 | 2024-10-22 00:06:27 | GOES-16 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| af0b7cea-a47a-3924-a64b-b7943eb9f62d | -14.3031 | -59.32 | 2024-10-22 00:06:27 | GOES-16 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| b63e4d7b-b4fc-3a8a-8580-d2194ab43112 | -14.322 | -59.3382 | 2024-10-22 00:06:27 | GOES-16 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 9ae71a00-de5a-36b1-9d3d-6f13ba57c408 | -4.46139 | -42.89527 | 2024-10-22 00:07:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 178c6679-8a2c-3941-9696-9cd829638068 | -2.49372 | -45.87335 | 2024-10-22 00:07:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 29.4 |
| ec724d97-9f7d-3a5c-a9fc-088c5f740f9d | -2.50161 | -45.8788 | 2024-10-22 00:07:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 1e0136b8-6a88-3f16-b78f-1f2097478ff1 | -2.50976 | -45.87112 | 2024-10-22 00:07:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 06d4c480-5b40-3a73-887f-91fff4bd3313 | -2.5142 | -45.90433 | 2024-10-22 00:07:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 5d8c45bc-8fa1-30f9-ad63-0ac3465d52fa | -2.80321 | -45.78085 | 2024-10-22 00:07:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 38.6 |
| c2d68f4f-f6b7-3a76-a297-ec9683ea1f91 | -4.41428 | -43.95284 | 2024-10-22 00:07:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| ded27bf3-6e81-3b82-b802-c0d329064807 | -4.41089 | -43.95969 | 2024-10-22 00:07:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 230e2ae6-622e-3712-99ad-0a19b03a435a | -3.52834 | -43.62046 | 2024-10-22 00:07:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 1cf9e51a-8c3e-3910-b7ed-d2f1574ad6e1 | -3.41924 | -42.71673 | 2024-10-22 00:07:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 7913c13a-291f-3725-8d79-26d76fa02a09 | -6.24653 | -44.1626 | 2024-10-22 00:07:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 7fe7a6ca-f8b5-3397-8d95-1ceb67a7afe8 | -6.24606 | -44.15618 | 2024-10-22 00:07:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 127.8 |
| bf41599a-5a70-3920-9a18-38d342f57088 | -6.24303 | -44.1354 | 2024-10-22 00:07:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 124.6 |
| fb7c6557-436b-33ac-93ba-e1d74bacf719 | -6.24277 | -44.12899 | 2024-10-22 00:07:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 16a3b256-5df1-36ac-9d2a-cac508c1839e | -6.22817 | -44.13738 | 2024-10-22 00:07:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 1ae2a924-9a38-375f-b491-cc83bff5a127 | -5.58179 | -44.89851 | 2024-10-22 00:07:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 5d95b693-7a1c-3cef-ae88-8ca7769cccc3 | -5.57776 | -44.8668 | 2024-10-22 00:07:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 9c4f82f4-c17d-31a8-bb08-88849d8c7a92 | -4.5582 | -45.81099 | 2024-10-22 00:07:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 341.4 |
| 88f73548-cb74-39d4-b210-7b6917a780ce | -4.55206 | -45.81745 | 2024-10-22 00:07:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 205.3 |
| 87611817-6681-3b29-a8ee-85800e70a202 | -4.54738 | -45.782 | 2024-10-22 00:07:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 9572f781-6957-3a85-ba1b-11d68dca1b09 | -4.01861 | -46.03133 | 2024-10-22 00:07:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 37.0 |
| a817594d-8b76-3f75-9d29-21fc1d0b7db8 | -4.00192 | -46.03299 | 2024-10-22 00:07:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 0b421976-cc7e-3233-bde4-a8d8f56608a9 | -3.64228 | -45.25247 | 2024-10-22 00:07:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 2536ccad-c45e-39ff-b2d1-17116838b214 | -3.45278 | -44.27614 | 2024-10-22 00:07:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 8eca76c6-aed4-3a2d-be3a-9ef8a47db832 | -3.45019 | -44.28183 | 2024-10-22 00:07:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 653a88c8-246f-349c-bcc2-69b6f1bc795e | -3.32988 | -44.17564 | 2024-10-22 00:07:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| c19f1a3b-3793-353f-9a8a-c68687647123 | -3.16447 | -45.64199 | 2024-10-22 00:07:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 33cca88f-4ab4-37cf-a05a-0f3f0261e1d5 | -3.15769 | -45.63633 | 2024-10-22 00:07:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 21.1 |
| dd60e9ab-4b17-3ba0-8ab8-b4f062c0c58c | -2.99441 | -45.61094 | 2024-10-22 00:07:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 0a8da78b-5351-3665-808e-00d9a2ca327c | -2.99227 | -45.6377 | 2024-10-22 00:07:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 21.8 |
| c1165ed8-b7e1-3871-8880-cd50950ea421 | -2.98808 | -45.60542 | 2024-10-22 00:07:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 9d1eac57-efcb-3611-a725-5b509ac5aa01 | -2.97858 | -45.61312 | 2024-10-22 00:07:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 34.6 |
| af3e0908-f821-34e2-ac4f-ce2fa310f130 | -2.86307 | -45.46759 | 2024-10-22 00:07:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 716116e2-9574-3b8c-a4c0-e22f7877deba | -2.85276 | -45.47402 | 2024-10-22 00:07:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 160.5 |
| 361ddf56-aa96-3c67-b73d-44b087de7b85 | -2.84852 | -45.44284 | 2024-10-22 00:07:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 34.6 |
| f8e43e9e-d72d-3f7c-b447-e15e9ff441fb | -5.55084 | -35.57941 | 2024-10-22 00:07:00 | TERRA_M-M | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 17.9 |
| d84fc398-03a9-313e-bb18-972665a0f969 | -5.54323 | -35.58953 | 2024-10-22 00:07:00 | TERRA_M-M | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 8d848015-9f9b-372d-abdc-1e8f4c81ba37 | -5.55209 | -35.58828 | 2024-10-22 00:07:00 | TERRA_M-M | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 8baa49a1-744a-3bf2-9864-3d4f91d5fc5e | -5.58943 | -42.93149 | 2024-10-22 00:07:00 | TERRA_M-M | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 3b21aa54-9829-3c8f-9db4-06cfaf5047e4 | -5.69964 | -43.14323 | 2024-10-22 00:07:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 22.9 |
| e61f59a3-cda3-32da-8b2a-162ef1c87802 | -5.8431 | -39.34059 | 2024-10-22 00:07:00 | TERRA_M-M | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 10.7 |
| b76e3bb4-887d-3081-96ce-6d91b1a77e99 | -5.84466 | -39.35235 | 2024-10-22 00:07:00 | TERRA_M-M | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| f22d20f9-9286-3e1b-ba44-21d1a09012c0 | -5.858 | -43.75159 | 2024-10-22 00:07:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 133f40e6-9706-33b9-96ec-de7873c09fe7 | -5.86099 | -43.74471 | 2024-10-22 00:07:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 161505ff-6360-3b2d-8632-b1a6eea8aae6 | -6.72624 | -40.47903 | 2024-10-22 00:07:00 | TERRA_M-M | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 15.5 |
| e43df566-e823-3f08-acee-917693d53a4b | -6.71445 | -37.05837 | 2024-10-22 00:07:00 | TERRA_M-M | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 544773f0-5501-3eab-a749-6ee08ec72a1f | -6.67183 | -38.58403 | 2024-10-22 00:07:00 | TERRA_M-M | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 5d8560cb-3a21-3794-bfa4-e6a9f4a23d6e | -6.62795 | -35.1789 | 2024-10-22 00:07:00 | TERRA_M-M | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |


[Clique aqui para ver as próximas entradas](README2.md)
