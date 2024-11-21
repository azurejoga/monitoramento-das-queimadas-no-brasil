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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8327e065-1787-3f86-ad4e-a90b8a802366 | -2.01685 | -54.53289 | 2024-11-21 04:08:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| efc5d272-589c-3d46-92d7-437f7c6b8ff6 | -2.62546 | -48.06937 | 2024-11-21 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 19f5f252-c621-38ef-89b3-f72512c320fd | -3.42253 | -49.22571 | 2024-11-21 04:08:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2114570c-130d-3cca-96b4-2b818b4bc49e | -3.2683 | -50.62194 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89d21e76-f630-3552-aace-a3339d789a93 | -3.12519 | -45.44976 | 2024-11-21 04:08:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d653ec4e-3ec0-3a61-ab63-31549aea9451 | -6.21562 | -46.21882 | 2024-11-21 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6d3937c1-88e8-3a95-a460-7adf17812930 | -1.26869 | -51.60586 | 2024-11-21 04:08:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| df263191-07ca-3350-a3a8-3325535f28e4 | -2.83116 | -46.67945 | 2024-11-21 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d7a9cce-8d9f-30eb-87c4-7723c3301da0 | -2.24897 | -49.20204 | 2024-11-21 04:08:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a14ab1f9-0ecc-3c9d-a20c-31fd4966bae6 | -2.83659 | -51.82535 | 2024-11-21 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e135de4a-a7bc-3f5c-8644-a294e94fd7b2 | -3.2788 | -53.83112 | 2024-11-21 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ff660035-f24d-3dbe-b03a-6c1a2f065637 | -4.07143 | -50.90206 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b50c7c4a-1e44-3784-af33-067419aa661e | -2.33059 | -45.66484 | 2024-11-21 04:08:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 725522a2-a0a2-302f-be58-4f94344c444d | -2.84382 | -46.68145 | 2024-11-21 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76bf24c7-33c4-3aae-b342-f28a8068b17c | -4.96737 | -45.51676 | 2024-11-21 04:08:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba7a381b-c877-34c4-b01d-93ddd234c163 | -5.10285 | -43.17148 | 2024-11-21 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c694eaca-5eed-37d6-a16d-cc4c90e6b53e | -6.207 | -46.22262 | 2024-11-21 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6b6c840c-3c38-379d-a242-cb2a9bb71918 | -2.84742 | -49.15722 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 28a0fbd8-64d3-3d94-bc6f-974df35c28bd | -3.07171 | -49.20159 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2e008beb-2b53-37dd-a92f-80fea21cb8ba | -2.84788 | -49.15436 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d9551d94-f491-355e-bb5d-b21ebb1f72d5 | -4.14728 | -43.87625 | 2024-11-21 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 380bb60a-100f-3a15-b991-9a29d28f1bdb | -6.61788 | -42.38499 | 2024-11-21 04:08:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 505f8ebf-a1bc-354e-a5b0-b58b3fdfd460 | -4.58166 | -38.00164 | 2024-11-21 04:08:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 716dfe5b-7d23-3050-9037-2cb14be7a5c3 | -5.92934 | -44.72685 | 2024-11-21 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8d00a28-8cd2-3d14-925a-0533c03fd1e9 | -2.77028 | -45.95238 | 2024-11-21 04:08:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ddc68bde-1338-30c6-8ef4-fcc9d9763fa7 | -2.55713 | -46.05734 | 2024-11-21 04:08:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63bc8e71-a28a-3036-b25b-dbb6303beedb | -3.46449 | -50.0098 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 510920e6-90a6-3cc9-8133-010b40cd6d9e | -4.06446 | -46.83215 | 2024-11-21 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 340cd8d4-5364-3d47-a56a-abe736c6674c | -3.40242 | -50.25611 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6704898f-42ff-369c-8617-1280902357df | -3.28456 | -53.83772 | 2024-11-21 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3db4e21d-4020-31f5-a481-c0809d9f665f | -1.7924 | -48.45051 | 2024-11-21 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 783153ac-3713-3feb-a3ef-aa6cd53e0dd7 | -3.29961 | -50.22587 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c60703c-5a8e-3b33-a833-9f33e167a468 | -3.46449 | -50.00914 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa72c3fb-6011-3c2a-a677-1f031320e01a | -3.06197 | -44.341 | 2024-11-21 04:08:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 527ba927-da0e-3e9d-8cbf-4d21091c1b2b | -2.6427 | -45.76497 | 2024-11-21 04:08:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b19c86e-2e9c-38c6-95c9-0779d0ac89ff | -6.30352 | -45.33998 | 2024-11-21 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed750675-3528-3290-9ac1-61f683a60a9c | -5.12291 | -44.10145 | 2024-11-21 04:08:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c917b71b-599e-3b3c-9088-955ff71cd494 | -1.71104 | -52.72614 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 37468fbe-4b0e-35a6-9d12-6ac00e3994a3 | -2.36841 | -53.841 | 2024-11-21 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 16530477-2855-3567-92c1-77ff0e8bec7b | -3.8139 | -47.79424 | 2024-11-21 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| dbc3a55e-5d1e-3b16-b96a-c380ce9ec61d | -3.3312 | -50.25506 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 121b178a-55cf-3a9f-9ebd-ce664bbd4b7f | -0.25148 | -51.03579 | 2024-11-21 04:08:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f1c41647-47a3-3982-bd94-d80907f98b1f | -4.47777 | -43.19793 | 2024-11-21 04:08:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb1426d7-d964-3ec1-908e-3e0380b19c7a | -2.20977 | -47.99305 | 2024-11-21 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cdcfbe93-7baf-3677-9910-ca760f51777a | -6.2148 | -46.22381 | 2024-11-21 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6becba36-2f82-3efc-a59d-b5909b0c2f67 | -4.3482 | -46.14151 | 2024-11-21 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e07bba8a-4183-3c31-8ab1-8afb331ce2d7 | -6.2109 | -46.22323 | 2024-11-21 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0f49907c-0cf8-38a7-90c2-96b37d1bc178 | -2.62642 | -48.48272 | 2024-11-21 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1804f696-7fd5-31d2-8152-a3cebb8e832f | -6.63782 | -35.04564 | 2024-11-21 04:08:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 00ff313a-e596-3eed-9dc4-2340643541b4 | -3.68191 | -50.22276 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0e91e193-16f0-3547-a766-85bf690dcdec | -5.47049 | -46.53421 | 2024-11-21 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 10f36224-a41a-37d7-8450-2b9ef5702fb7 | -3.3292 | -50.49738 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9668ee15-ae28-3610-82c9-504b6f424c5b | -1.2697 | -51.61116 | 2024-11-21 04:08:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9cf66a01-bace-3dee-8028-f86d2d3803a0 | -1.64248 | -52.61115 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a01fdf1b-245d-321c-98ab-4b0498c185fb | -3.12907 | -45.45037 | 2024-11-21 04:08:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3f5d748-2753-3de2-9e8f-60e55dde5911 | -4.4294 | -45.62239 | 2024-11-21 04:08:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97f7730b-78b2-307d-8c21-72a5fb78ec4d | -3.46437 | -54.56604 | 2024-11-21 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bbee3a3e-1916-394f-a028-cf4fe02cb36b | -3.19398 | -54.32073 | 2024-11-21 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3033e3d1-688c-36bf-94db-2ece08374be8 | -1.14029 | -53.66428 | 2024-11-21 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e14c88d3-5967-35b7-9238-950b9069c2dc | -4.4836 | -44.76191 | 2024-11-21 04:08:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2056e511-daca-35be-b4de-4f0bc606ede0 | -2.47439 | -49.17537 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 812ccf69-0ad9-360e-bcf5-a0e4680c59de | -4.66407 | -46.40385 | 2024-11-21 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f2dea43-0a1c-3cad-a6b0-eb281a143e54 | -3.00705 | -50.99826 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b2efba65-3c9b-3818-9d40-8e044e21a770 | -3.68829 | -50.21729 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8f7e3295-b9c4-3438-853f-3747e4a5e921 | -2.63808 | -46.20344 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1a5f9254-c701-3b6a-b704-8d2c57cc9448 | -3.5177 | -53.80297 | 2024-11-21 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1bbed81f-0ba8-30f9-8621-33a02aefdeb4 | -4.24756 | -49.08568 | 2024-11-21 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9486e8cb-a725-365b-96ca-96a5c303bd28 | -2.25117 | -48.16463 | 2024-11-21 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7bb0b48e-e118-374e-ab03-dc517d517862 | -2.24918 | -46.82366 | 2024-11-21 04:08:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ac3effd-aa9a-3b1c-910c-475bf4c547f9 | -4.07088 | -51.03711 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5949962-e0f2-3f21-929c-2299765e6798 | -3.49906 | -48.22619 | 2024-11-21 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4605d772-1848-359a-b245-527d13450907 | -3.47358 | -54.54724 | 2024-11-21 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 48ad966d-3c63-3a3b-8c49-b68e8b22b996 | -5.7406 | -44.27635 | 2024-11-21 04:08:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 516d9808-57a1-3134-9337-39c8000fe5cf | -3.26888 | -50.61837 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8bd22bbd-04e8-392f-b49b-f4918d0ef29b | -3.54382 | -50.53479 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5a38364a-9922-3de9-b3f9-b4dc729293b3 | -3.28558 | -53.83183 | 2024-11-21 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5440c5c4-113f-3467-8732-3f84fae55d62 | -4.25093 | -46.12233 | 2024-11-21 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| f574f880-0b62-377c-a6ee-7904d50e59cf | -5.10625 | -43.17201 | 2024-11-21 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a3e68f1d-fa71-304e-821c-4500bcb541fb | -2.01621 | -51.17402 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a96ded59-554b-315d-8af5-e190352c09d4 | -3.18356 | -46.26466 | 2024-11-21 04:08:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 428a2bce-2f81-384e-97ff-a1fc6a7fbf32 | -3.27734 | -48.79762 | 2024-11-21 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7ac3a76-b463-3236-92a2-c9c1a1b7746e | -2.83966 | -51.82567 | 2024-11-21 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cf94ddd6-a3dc-331d-aa93-79b9a56ff112 | -3.80932 | -52.369 | 2024-11-21 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8d49900a-a872-33c8-bb76-c21a3c0365b1 | -3.28248 | -53.84971 | 2024-11-21 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f9196159-1b0e-348e-8fda-aacf1a934261 | -0.89739 | -51.72582 | 2024-11-21 04:08:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e62f0298-b16c-3ac7-b0ca-b45694b58079 | -0.2941 | -51.60315 | 2024-11-21 04:08:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12b04759-cd3d-36a2-8742-d82dbf1e6adf | -5.30373 | -43.08009 | 2024-11-21 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52aedecd-f354-3ac5-ac94-eb5796a49029 | -2.08235 | -46.28793 | 2024-11-21 04:08:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 108d53a4-abd0-3074-93bb-7e966341db05 | -1.40877 | -52.1105 | 2024-11-21 04:08:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 73270f35-e4ce-31c1-a019-71c38311595e | -3.46975 | -50.01061 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8f1d8161-b6ea-376e-af9d-247d120a223d | -0.89127 | -51.72487 | 2024-11-21 04:08:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51a36418-6e14-3ef2-b8e2-b2b2356e7d71 | -3.09902 | -53.17134 | 2024-11-21 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e03d56fe-6eaf-32f1-b0da-5a614b9e2f7d | -2.74276 | -51.72606 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7dbf79b4-aa79-3bdb-a955-74125217a7d0 | -2.5577 | -46.05373 | 2024-11-21 04:08:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 766c2989-27ae-3897-9049-dcb170fd5944 | -5.65457 | -45.20043 | 2024-11-21 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6b4640c-7429-38b9-aed9-20e8d732bca4 | -5.24157 | -42.63383 | 2024-11-21 04:08:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d62bf754-debe-3eed-b214-b1ca329c5e1b | -3.09854 | -49.44616 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79e4587b-db62-3611-b1dd-7aaa03fc8aae | -3.5372 | -51.60595 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 507eaa4c-f229-326f-8ac2-555bede37903 | -1.37843 | -46.51476 | 2024-11-21 04:08:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d9ddbf39-7214-37b1-9049-9f3fc8b8d7f7 | -4.78615 | -37.76046 | 2024-11-21 04:08:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README15.md)
