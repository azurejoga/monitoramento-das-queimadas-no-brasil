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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d78c8e1-f27f-3da9-9f66-632e8da6c9ff | -3.05103 | -49.52153 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e93bcf26-0df9-3719-9235-2ca5ad290931 | -1.04552 | -52.41896 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 65cbe5fa-1ff9-3813-8a2f-e6c538882ddc | -2.53466 | -47.3288 | 2024-11-30 04:40:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a5b023b5-c61c-334a-8be9-f99ea7e64571 | -4.07003 | -46.69115 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3d234bb-2f08-3695-843d-f947f18d421e | -3.05298 | -54.04698 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef3b697e-f3bd-3922-b417-d8202406c57d | -3.73808 | -51.83598 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e923c2cf-e684-3dea-9a82-b6f7773a799c | -3.20789 | -50.21184 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| edb75d90-809c-3ec8-b6f4-cf6bf9b21859 | -3.97704 | -46.65818 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51b0dba0-4f5c-37aa-a97b-460112b2299f | -1.10463 | -48.37095 | 2024-11-30 04:40:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdf86439-dcf3-35ed-a8d0-798eafd1e9cc | -4.14165 | -50.65733 | 2024-11-30 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30cc6600-8b68-31e2-b05e-777252e11595 | -1.1608 | -53.58533 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 64eb4ebb-ef6b-3f6c-bdb5-5cbcf120e428 | -2.75128 | -46.09932 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bbc964e4-c08f-3bce-bae8-01593b0a74aa | -2.44503 | -53.62142 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ac1cd419-f568-38b8-bdcb-caddb9610477 | -6.94712 | -42.78548 | 2024-11-30 04:40:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| add84281-d67e-373f-af66-d0e26cb69c44 | -1.69125 | -46.78875 | 2024-11-30 04:40:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| d876ef36-7817-380a-af16-af01851caf62 | -3.30195 | -50.37194 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e5d91f46-4eee-33a8-9409-3e9dd8915d19 | -4.14404 | -48.24632 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 764dd298-2a26-3e07-8192-e48d5f4df81c | -3.59822 | -50.0022 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6f7f179-fd7c-3e91-9e81-e088072a1314 | -1.56767 | -52.00069 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90ec83b0-1ebd-3cce-8dfe-1a44f274b7a8 | -3.38416 | -50.69532 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a8145ef-c5ca-3c4c-9d1e-9441b0cc2971 | -2.62499 | -46.07311 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93a4c61c-fbb7-39b9-96e0-36776c5e07bc | -1.76135 | -53.64338 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0386e4a2-f714-3b14-b587-48e0a0670fdc | -3.86567 | -46.90739 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bbe81e57-7e3f-3a85-ab6f-513c4d3c8455 | -2.77451 | -50.30859 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d21ebe9e-9b09-3c99-81ad-1aacc9dff9ee | -2.24482 | -48.25671 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0ad7c164-8bd5-38ca-b094-65c99d869219 | -2.35469 | -49.01287 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 5bcab28a-66b2-392f-82ca-ce8e8ef9e9b7 | -2.69298 | -46.86769 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c12a719b-c20b-3c50-95ab-a51e9dfc7208 | -1.6942 | -52.46259 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 89b86e7f-d1fa-3366-948c-2eb1b608caa8 | -3.60041 | -49.98819 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 124.2 |
| b8b71def-4114-3626-9714-2732bd429ff0 | -4.67575 | -46.37379 | 2024-11-30 04:40:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 43a5ba10-06ad-3734-b4de-3ab015e3288b | -2.5914 | -53.98465 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c4ee9663-176f-35d3-a40c-cf2fa7475c98 | -3.27958 | -50.29548 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ada53f75-e618-3352-8c7a-2449159e5467 | -2.95097 | -48.59298 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45a05965-11b0-34a7-85aa-1b0a13977dbc | -3.31259 | -50.50211 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20cb991a-f63d-3461-8ba9-c1d5214d6ba1 | -3.97453 | -46.7446 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcdcd82c-f0a2-3165-80ae-6a07a95bbd3d | -3.69485 | -47.1271 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86b4b6dd-ca0c-3efe-be25-c14ba558879a | -4.13912 | -48.93714 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0360b4f2-7390-34d9-bd82-f6e0d1f0cbb4 | -1.39316 | -51.98964 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5fbe30c0-32e0-31cf-9fa4-b363ca930ff4 | -6.64591 | -47.91623 | 2024-11-30 04:40:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46f0c4fd-4375-3e4a-a077-e11ecaa42150 | -2.24833 | -46.45152 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15ebdb3a-0db7-38e0-aba0-b4bfd8714a54 | -2.6106 | -48.15845 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9024b5d0-6211-3fbf-a6a8-04390794e888 | -3.29148 | -51.151 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d989a202-b56d-3cbe-b60c-3e0258b1e258 | -3.03964 | -51.78049 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f14623a4-8863-342f-bd19-74ee88b4a31b | -3.06303 | -50.3315 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4510ef28-871e-34ed-89ae-7d7b911b5d51 | -2.48184 | -49.05089 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 604b722f-25ec-3710-963e-5e895e163c36 | -3.7001 | -51.80159 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e9fd21d3-5360-3a48-a327-a6b81a43bcdb | -0.99638 | -51.72476 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4adfb5f1-32bd-384f-ae37-cacbd5a71440 | -1.59058 | -52.2837 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6e9d0bd7-24f5-3df1-a06f-afe3c046bc23 | -3.68288 | -47.1366 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab1c36de-f0fb-36e2-9924-0b6728101944 | -2.75405 | -51.66082 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e1395d1-3abd-37f0-9aa8-ade147842212 | -3.96816 | -46.7397 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a5aea992-7c34-32c8-89c6-f859d2b2acfb | -2.60641 | -46.56697 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b69f51ef-3473-3491-ac4e-cf68e40e9905 | -3.38663 | -50.11629 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5766533-42bd-373c-aa99-60dd43899e29 | -1.4353 | -55.24676 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 106b6d94-cd39-301a-9153-a238de773029 | -1.76191 | -53.63987 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d2579452-0fc0-3126-9088-2e568736b74b | -3.25546 | -53.63401 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 54e62a4c-d349-387b-beba-d0b5647a7204 | -2.10058 | -50.1344 | 2024-11-30 04:40:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 086993a1-7f50-3a09-966d-4ec0f7940aa6 | -2.78729 | -52.98676 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 43949f7c-d3c4-3dc2-a90b-064a7f1fa706 | -3.25687 | -53.62681 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| d685263f-1b17-3bad-a5fd-ea4116aaed16 | -3.27834 | -50.43426 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 198222ba-609c-3e7d-8aff-1a8328e5bc43 | -1.61368 | -52.35524 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 44b10bd2-e5ba-3760-a360-4dc6a5a2d9d7 | -3.14109 | -48.53072 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b24d7ac-df16-3a03-a115-aa9036a6877b | -2.1579 | -48.79205 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c86eb4b9-1022-32ae-a0a4-45c560c9647b | -3.85862 | -50.11862 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ddbfc10-b1dc-3fd2-9e33-b9f36cea3b33 | -3.21881 | -54.18446 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 55de6231-8f0c-3793-9434-aa55f01462a8 | -2.27782 | -46.4444 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d4f03fd-6c93-3f97-a1ec-b2b966a0c400 | -1.25387 | -51.63496 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ada56897-e390-3cc3-b97e-3c53c5bfe5ee | -2.73439 | -47.97466 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3563fd4c-cbef-3b53-a5bf-78ee60c9e5ed | -2.26603 | -50.35532 | 2024-11-30 04:40:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e323ef75-9daa-3594-ac10-88c83b5352bd | -2.08532 | -48.40819 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 288e2ac8-ee29-374f-a255-ea0b4628cbae | -4.08551 | -47.02895 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f89d1159-239b-3e16-8ee3-b1cf9e257bb0 | -3.74224 | -51.83256 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 152e0c64-84a9-3a57-916a-1c8efda6a202 | -4.05706 | -46.82302 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1e686486-cc57-3dc2-9821-fc3b329e8b2e | -2.58849 | -53.97686 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8628198f-dec7-3425-a3d0-852803841053 | -2.96055 | -53.89507 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0921c31-61d9-38aa-88bd-6e993c256dfe | -3.87897 | -51.97557 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23fec1d9-89d7-37bc-a67e-fa1b42420bfa | -3.57924 | -50.33503 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf8288d2-b3fa-3ea8-ab6a-f1c758d744ae | -3.64468 | -51.42242 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd2d4319-4934-3892-bc35-8a8dd507bd80 | -3.94256 | -49.90974 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 635da147-45ac-3497-b4e8-9d12eb22aa70 | -2.45794 | -46.57159 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c10b655f-75b6-3e58-b115-778a97dfd9fe | -2.03768 | -54.67166 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f67d8de7-7c64-303e-b0a1-bd6d500dd280 | -1.78576 | -52.74397 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8af4aa71-28fe-3c41-b419-70e513f7a815 | -3.76114 | -49.93858 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 07994e90-a887-352c-b9c6-a2ebe4c2cfad | -3.0502 | -48.52376 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a33b5780-36be-33c2-8cd9-10a9d94846e0 | -1.18822 | -51.76951 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 65b1149e-0b44-3990-b882-bafb023ba17b | -2.84503 | -46.88269 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c694bcb1-fc03-35dc-bce1-e1e78063f24f | -3.26357 | -50.09731 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a9719cc1-0e02-3fcd-926e-e2cd461d9852 | -2.94917 | -47.99321 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc80c77b-af9f-36bc-a202-9872825ca059 | -2.8753 | -48.09597 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e529f2f4-4dde-3f56-b1a2-d478587a9585 | -3.76472 | -50.17597 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 89d5a7e1-58b1-3a9f-9281-4957151e7c7d | -3.24147 | -46.42389 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26bd806c-e00a-344f-83f1-571473c764b5 | -3.25287 | -46.51292 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8c327f9-7c1d-3984-b297-d8523443c693 | -5.52638 | -45.40565 | 2024-11-30 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d4060496-4e00-3b26-aa3d-f70e9237ca7c | -3.2482 | -53.63068 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 40c5a7cc-01cc-366a-b651-299837a28c91 | -1.63778 | -53.86696 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 9852e40a-55e0-3a32-b280-536d7ee26b74 | -2.72411 | -46.11138 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1567809-d8fe-3923-a915-36db7a911125 | -2.72349 | -48.65575 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7aaa7615-1f54-387c-81fd-9b2f1fcb9c2e | -1.60406 | -48.70213 | 2024-11-30 04:40:00 | NOAA-21 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12fd1965-00e8-3c8a-8336-8e96847aff9a | -3.61343 | -49.86153 | 2024-11-30 04:40:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dcbde0ce-df55-3af3-b44f-80ec3c1e9581 | -2.47331 | -50.36859 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README65.md)
