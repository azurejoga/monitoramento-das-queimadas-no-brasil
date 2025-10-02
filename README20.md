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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6a07fb9-c908-381b-a360-c3ae58349f83 | -3.69334 | -49.5696 | 2025-10-02 04:00:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bff88b08-9dcb-3706-b6bd-c1a9b06479cc | -3.81279 | -47.58408 | 2025-10-02 04:00:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65d6dd00-5cdd-3da6-bb06-77fe961d54e1 | -4.43018 | -40.75288 | 2025-10-02 04:00:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5513f904-6f00-3ba3-9b9e-8e2a6e4b339b | -4.84634 | -40.78945 | 2025-10-02 04:00:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5b8c60b9-36c6-3330-a872-e4448d7e2b3c | -5.27593 | -42.88548 | 2025-10-02 04:00:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| cad69899-eb8f-3757-9521-22e3623558fb | -4.42765 | -47.75542 | 2025-10-02 04:00:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 59e4131d-2b6d-38b5-b722-2bf0e7a59e5c | -3.81824 | -47.58209 | 2025-10-02 04:00:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 707d96d7-c78d-3641-87b0-5fa83a6b8e5c | -5.40948 | -37.69672 | 2025-10-02 04:00:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f6475185-934b-394c-b564-618deeed17ff | -2.42947 | -47.14442 | 2025-10-02 04:00:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 073fb170-5f52-39dc-87d9-ad8a2f7e2a52 | -3.82463 | -49.09757 | 2025-10-02 04:00:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 4278930e-387a-3f35-b355-7914f31f3bde | -3.82462 | -49.09739 | 2025-10-02 04:00:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a0247eea-1af2-39bd-a4e5-63c15e27c23e | -1.57811 | -47.31422 | 2025-10-02 04:00:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fb1ce5d6-c3d5-33cd-a68e-3ea6baba2902 | -3.78928 | -48.6273 | 2025-10-02 04:00:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e6107e1-7a68-3d16-ac4c-230f15a86758 | -3.46221 | -50.09305 | 2025-10-02 04:00:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9107cea5-c341-3451-b099-1f9a2763ffb7 | -5.81434 | -40.58788 | 2025-10-02 04:00:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8ef2ee8d-51af-3d98-bc0c-c9840a4f059c | -4.62896 | -49.37057 | 2025-10-02 04:00:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a4b39a5-098b-3a3d-9277-2eed81d9cc9a | -5.65926 | -38.30797 | 2025-10-02 04:00:00 | NOAA-21 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fac21b39-6eaf-3d82-8dff-84fb7102fc87 | -5.25171 | -42.89849 | 2025-10-02 04:00:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 9261c780-602d-3338-8ce1-4c72d630a2cd | -3.46547 | -50.09661 | 2025-10-02 04:00:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d215c262-2a0c-34b6-9333-5d79e2410c30 | -5.28072 | -42.76385 | 2025-10-02 04:00:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ec64f7b-ae2d-381b-be5d-d97389a8d66e | -1.57859 | -47.31122 | 2025-10-02 04:00:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f8f952c6-f3a4-3eaa-8a95-52fac9f355c2 | -5.41191 | -41.32443 | 2025-10-02 04:00:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| abff68e4-08f3-3f29-8e77-9dd84132701f | -5.4057 | -41.34181 | 2025-10-02 04:00:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 430a4689-173a-3d15-bc93-14a73edf6735 | -5.81856 | -42.84943 | 2025-10-02 04:00:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 16f2c2b4-bec5-3589-8038-9e025a5280b3 | -2.92592 | -48.30254 | 2025-10-02 04:00:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 777bcc24-bed0-3e3a-8830-0986af40f909 | -3.46816 | -50.09387 | 2025-10-02 04:00:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec0b0bbb-690a-3e50-85d4-9a7b056808c1 | -5.25622 | -42.91636 | 2025-10-02 04:00:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 47c8c913-99d0-3d86-9166-04088ca3ce95 | -5.64262 | -41.24315 | 2025-10-02 04:00:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4229b68c-3c6d-3684-bd3d-cadca4d24238 | -3.46152 | -50.09725 | 2025-10-02 04:00:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9f87cdb-3ef7-3e30-a1b9-44c4256124bb | -5.2389 | -43.74588 | 2025-10-02 04:00:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f72c2f08-d9b2-3b09-b9c6-65f9f9f69acc | -5.72154 | -42.46188 | 2025-10-02 04:00:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a127c69c-f172-3803-83d0-b14e127ade65 | -5.72156 | -42.68523 | 2025-10-02 04:00:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 7e91ddef-0485-3ad9-b076-7481a868d2fa | -5.1316 | -46.01733 | 2025-10-02 04:00:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e202717d-e5a1-32cd-b52c-4b3f54417395 | -3.517 | -44.03739 | 2025-10-02 04:00:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bab67f53-8b9f-33de-8725-064d340196df | -5.64598 | -41.24369 | 2025-10-02 04:00:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9fcee693-0fb5-37fa-87b1-3c7fd9ebbff8 | -3.4629 | -50.08891 | 2025-10-02 04:00:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e77be49-258e-32b7-a974-ca14792b6170 | -4.25819 | -48.56065 | 2025-10-02 04:00:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61cf1465-467e-3b70-aba6-087042a7c5f1 | -3.80923 | -51.31691 | 2025-10-02 04:00:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 43d00b42-36e2-3527-b662-e9c6200bb4ee | -11.84154 | -45.02021 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c44e588-d4ef-3e50-bc7a-7f8a2eb23bec | -10.92019 | -44.31043 | 2025-10-02 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c799432-1a7e-3e17-9982-bcbefd055dc1 | -11.81954 | -47.5922 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3d4399a8-6e67-37e4-aa77-853237106a7b | -6.04891 | -42.43624 | 2025-10-02 04:02:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f9c50c4d-82b0-3280-bf8a-b0f6f004ba0a | -11.46646 | -45.02213 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9146234a-246c-32a1-a118-4a12f06f5c54 | -9.93365 | -43.73094 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 31.3 |
| 6411ac11-9566-31fb-a727-98013d2f8f30 | -7.28809 | -37.0877 | 2025-10-02 04:02:00 | NOAA-21 | DESTERRO | PARAÍBA | Brasil | 2505402 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 453334e0-f7b3-3fda-8f41-e789c6036eb7 | -6.48774 | -44.28032 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 73a74a31-1f94-3035-89ba-44ea62efe835 | -6.79596 | -45.96793 | 2025-10-02 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39a87596-f402-3fcd-8e23-114b5593dace | -9.09248 | -45.84659 | 2025-10-02 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6259e97f-c43e-3ec0-a05b-13002ccbd1a6 | -9.94117 | -43.77433 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 65da9e3f-e650-3d60-a089-67e6589a17ba | -10.85674 | -45.40985 | 2025-10-02 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76502b7b-e2f7-31cd-a343-75a2c5a6e82f | -7.41951 | -45.19188 | 2025-10-02 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbf37fc9-94d3-349f-8ce4-ebca9b740163 | -12.2776 | -45.38095 | 2025-10-02 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6ff94683-2385-30bd-913c-13a5357724e3 | -10.22925 | -50.32895 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ff379661-e964-3509-aee6-a78563e0f08e | -13.01785 | -45.22141 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c1290638-8fee-3b08-ae6c-5d6dea53d984 | -10.85898 | -45.42003 | 2025-10-02 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be21e512-8303-3bad-8877-67ec18314a4c | -10.68775 | -48.55863 | 2025-10-02 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd91c7ae-fc48-3c94-979e-cb72633ccf66 | -6.12444 | -43.48906 | 2025-10-02 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9b8142d2-68fd-3f71-9d2c-7975afd349b2 | -9.96476 | -48.7847 | 2025-10-02 04:02:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 57420e85-ff1f-31a0-8234-10de8eea73aa | -10.822 | -46.61633 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 754e5b7b-f751-3792-abab-033d6a31bb09 | -11.78189 | -47.3942 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8838270a-3958-3a42-8fde-806635d2f8d8 | -9.94941 | -43.6791 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 07c8f6f4-4617-34ff-a5b4-a58ec8427ec9 | -10.35425 | -43.73491 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c2ed94ca-74eb-3e41-9c02-6de078e6f291 | -10.68907 | -48.57825 | 2025-10-02 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 420af214-b2de-30cb-82fd-0005b9dc8948 | -7.79179 | -42.50459 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 870cd429-9f7e-33a2-8d20-18de6f311707 | -12.84267 | -46.94146 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d755c71e-97d1-39f0-b36c-772622349f23 | -6.9599 | -45.31771 | 2025-10-02 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2136d259-51aa-37f0-8ae8-4ed8bb800e0f | -7.56047 | -42.65223 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 24351495-2600-38a7-9c98-43f38ce5aeac | -11.15563 | -47.19357 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| dc50a5d4-b5ac-3ec3-ad17-359a998341f3 | -11.01056 | -49.58321 | 2025-10-02 04:02:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6bcefb24-22da-3467-92d9-efa18e3f395a | -6.23947 | -45.32495 | 2025-10-02 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| eb38b5d4-9875-3d05-951d-bc58f4a8b932 | -12.85643 | -47.03158 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 27f904df-515d-3c70-8568-a921e152c718 | -10.82132 | -46.62019 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c0c77ae2-7226-36eb-b0e0-dc04a6c23fbb | -11.58136 | -47.0282 | 2025-10-02 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2c6ba7fb-7e7c-3653-bb50-db32355c8215 | -11.08232 | -47.81042 | 2025-10-02 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9d6522ca-7c68-3be0-9033-4d90b2af1c79 | -11.6725 | -45.32397 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d66c3e6-29ba-32ec-86d7-bcde1972c6f3 | -10.83659 | -46.63074 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f07f9805-7544-37ec-bd54-1d82dc3eb13f | -12.1882 | -47.90912 | 2025-10-02 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25b44c84-2dd1-34bf-998e-77dae8887f0e | -12.88772 | -46.92539 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24e0ff7f-f76c-3ce8-9ac0-ca73d8b9c073 | -10.82651 | -47.94817 | 2025-10-02 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5fa5a931-a8a5-36cc-97e2-9b85cf17e6d4 | -9.93767 | -43.70638 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51e03bde-42d2-34cc-8337-27831f33490c | -6.28418 | -44.0558 | 2025-10-02 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c9256447-f709-3616-b436-64a453108c0f | -10.24389 | -50.31027 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| df3d4946-55ac-318c-9f1e-3c483029168e | -7.55478 | -42.64341 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 462249b6-9a7c-35f7-ae5f-f0951e94cfdf | -10.81378 | -46.63881 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| edbc89e5-5e92-3997-ba14-4aea04a2aac3 | -6.32915 | -43.03656 | 2025-10-02 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc7a1d28-9e94-3aee-ab8b-2c6d976bfac1 | -6.3269 | -43.02774 | 2025-10-02 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2db82fe0-8717-35f3-a913-f096b3691158 | -11.06734 | -47.81683 | 2025-10-02 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 37d3bc73-4df3-312a-9a7e-2a8c4f53244e | -12.94462 | -46.43308 | 2025-10-02 04:02:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ddc889c3-cbe8-3d3f-9723-c26cca2728a7 | -11.81563 | -44.91111 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 25840de5-85fe-3b8c-b64e-bc7647011da1 | -12.81249 | -47.03947 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e9af7b8c-2b75-3966-9ebd-48574ae3c860 | -11.87126 | -45.02479 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 97c81566-202b-38a3-ba69-7558b3191436 | -11.81524 | -47.59121 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d5826ce2-90ce-3c20-bb74-5fdb9a750580 | -6.96875 | -45.34185 | 2025-10-02 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15f33565-2f64-3a2a-9767-366b7e7b8cc4 | -9.93499 | -43.72272 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6f8a7d3c-3ad5-3b3c-9923-f706155ebfbc | -9.93432 | -43.72683 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 31.3 |
| 872fa62a-8615-37bd-84c3-fbdfb3993448 | -11.00961 | -46.57053 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 522ba8f8-01db-3eef-a1dc-986194009261 | -6.66884 | -42.79846 | 2025-10-02 04:02:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2c4d61fe-3da8-3896-bd87-120b40083ccc | -11.61703 | -45.03568 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c7db36e-d58a-3c84-bd1a-75fdb1431b15 | -12.26069 | -47.8102 | 2025-10-02 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b3ea89b1-7f26-34e3-a99f-ecd201af4706 | -7.72234 | -46.22219 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README21.md)
