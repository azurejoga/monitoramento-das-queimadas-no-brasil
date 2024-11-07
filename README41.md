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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8664417-8d14-3f5c-9ab7-0a1d056a455e | -2.72348 | -54.15122 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7eb4c8d9-5805-3b7c-ad0b-4bd39310f2cb | -3.15566 | -50.2121 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| da8a37ea-2ff6-3495-9ab9-8c18f66922f8 | 1.35217 | -50.93663 | 2024-11-07 05:10:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8640b401-080a-3317-9ccf-bd81b3a888da | -2.82702 | -52.91797 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 672d1a09-4ba9-3eda-9370-bfd2a094139c | -4.37716 | -48.5836 | 2024-11-07 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 50088a9e-1249-36a4-a62d-c87132193159 | -2.6127 | -51.29931 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89ac4f71-47c7-3845-893c-c6443cf7bfa6 | -3.01662 | -53.44043 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7abb61a8-fba4-35ce-abd7-6b65a42c2054 | -2.82634 | -52.92236 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4b5b710-b50d-3acd-a209-134117b3e6c5 | -2.2815 | -53.79836 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bce8cb7e-a685-3178-84c9-075aad6dd404 | -2.82127 | -52.93057 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9618515e-6fb4-3d4a-b0b1-01453a1a91f1 | -1.42523 | -54.53967 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4422042-e332-3136-b7b1-04d2d4fb81ec | -3.04588 | -53.27162 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 50b60238-63a4-394f-809a-37ea37e28e1b | -3.22519 | -50.37631 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 08d0f00e-7e1c-37ab-9ad3-87f6a567eacb | -3.1187 | -51.10708 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 477cc62f-57b0-39a8-9eed-58abe9cda842 | -2.24304 | -53.67118 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| c81ce12e-f38f-3daa-9cfe-32ccec54eb86 | -1.95231 | -53.07411 | 2024-11-07 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7411c9d9-4bf5-3e61-856f-830a16c6cf1c | -3.22387 | -50.38499 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4e3d9caa-e3d2-3892-b3ab-3edfefeadbed | -2.28324 | -53.81075 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| bbd6c3ae-f378-38a7-9bbb-d2fb491284c6 | -2.80387 | -51.49481 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 216b64de-3960-36c3-8697-55d6a135337a | -3.58511 | -50.23211 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1fca9171-5a2f-3453-8e36-44ba6bc2cde3 | -1.95286 | -53.07233 | 2024-11-07 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6a6b22a-f535-3653-bda4-1e1f77bd9f26 | -1.40597 | -54.55178 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e2cda5f-8a15-3648-92b5-693301b66249 | -2.23887 | -53.67465 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 64c0be17-07ba-3ff7-8ad9-e9c4e40e6448 | -3.33164 | -49.02975 | 2024-11-07 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49eb3e44-a1cb-39a5-8ef7-4c530d594435 | -1.12008 | -53.62349 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58460f6d-d2d7-3f71-95f3-685afe488671 | -2.07488 | -53.56446 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ae349e8-68ed-3ac7-bd27-0b2f4492a5bc | -2.3159 | -53.88042 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a671fda7-3f04-3ba3-8608-7c4e2fb224c4 | -2.61736 | -51.29631 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ad1317bf-ac57-3cc8-82f6-9e89639ff924 | -2.20732 | -53.71482 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 33010516-40a0-3e83-9805-c3987a759cd4 | -3.01443 | -53.23156 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9485ddb9-c2ba-32ed-bf81-224947dea8fd | -3.15042 | -50.20843 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 833440d6-d908-3139-8dc5-a2fe357399be | -1.15296 | -53.73652 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 40b96ee5-b4ef-3b46-81b6-baa5ca22f761 | -3.65792 | -50.25382 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e2ae6d25-ab0e-3c56-b947-037a56077f1c | -4.66999 | -46.33221 | 2024-11-07 05:10:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6fb2aa6f-42c8-35af-85ae-b2256e382606 | -2.02224 | -53.29819 | 2024-11-07 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 61e4afde-9770-3598-8bc3-3530d8eceda1 | -1.05973 | -53.65905 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8a2006b-92fb-3c35-a29b-fb693fb33d44 | -1.53555 | -54.25677 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77a85c5f-9fd9-3fe9-af2d-896acf0c5f3f | -3.37008 | -49.76057 | 2024-11-07 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a02ac27-5360-32c9-b2aa-ad24fe29e8ba | -3.59137 | -50.27084 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f69e7c8-fdd3-30c6-844c-dce181a29cc7 | -2.82399 | -52.91294 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a71f6484-1c1f-36fb-a157-4a2bf1de8dfc | -1.1948 | -53.51329 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59a71813-c62c-37db-b216-6d254be65c62 | -1.46669 | -54.38376 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61851eeb-9050-3043-b726-11ed8f229ad5 | -2.83723 | -52.90122 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c15e9fab-8c71-3998-a6c2-b7ceb7aa50fd | -3.25221 | -50.46574 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 03562280-f6a7-34f5-9ba6-69652a705a4d | -1.13434 | -53.7179 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b616678f-fe5f-372f-b1cb-054e2e1badf4 | -1.2392 | -51.77303 | 2024-11-07 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 965de2f1-6fbb-3cc1-98ea-d6e4dfebd5f7 | -2.81727 | -54.08568 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 62916fd8-47fe-3a69-aec3-37988d9827c7 | -1.52636 | -52.14935 | 2024-11-07 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dc1c2cd9-3d6e-3435-b70f-00298c74d2fd | -4.67345 | -46.33434 | 2024-11-07 05:10:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2a34d19-fe36-36e7-a01c-5961fb44dd05 | -3.73009 | -52.27229 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bef29c74-9c20-3f39-be18-06e77c1049cc | -2.83141 | -52.91418 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b70a6995-0787-30cd-b4ae-02e2fc1768ef | -1.2218 | -54.53813 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2012a27c-3b88-38ac-9c35-8e8716e7e757 | -2.92027 | -51.04393 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9991701b-2281-3feb-9261-35597c16e413 | -2.67195 | -53.02248 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 06c8b8ce-8dd2-33c9-bd46-756fc0e4f4f3 | -2.87522 | -53.96595 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96d39360-00aa-3387-a72f-6f0681af1d87 | -2.28114 | -53.7995 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ccff1cca-797c-3fb5-ac67-43e30f06f88e | -2.8277 | -52.91359 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8685c2f-de03-35c0-99e9-41994cd8257f | -1.23538 | -54.54023 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54fed35a-5a24-3ac7-be80-c7241b2ee229 | -2.58376 | -54.00339 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2dcc77c-9d21-32f4-82f3-f166f6c90dca | -3.02717 | -54.08754 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99139c2f-ce1f-3f42-956a-28119ba89b11 | -3.51256 | -50.47121 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c2f479ed-f2bc-38c1-9f7b-aa6d75755e36 | -2.72816 | -54.14407 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4855123f-d66a-3d88-bda2-64ea97e22d32 | -1.34882 | -54.62201 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2e24f94-dd66-3f16-8e8d-e533ed479769 | -2.55738 | -54.00452 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04e29d1d-cd99-31da-90ab-d45fc03324e4 | -3.02695 | -53.27307 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 481b1126-1cdd-3abf-bf5c-a54df102a9a9 | -2.93229 | -51.04971 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a57a7651-aa18-3217-b5fd-999a4c5d7271 | -3.45465 | -50.37434 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 509f4d37-e411-3371-b3dc-327618e9b2a5 | -3.58823 | -50.22947 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| b71e5194-52a8-32e9-aa24-222cb5699ae0 | -1.12661 | -53.60429 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d3e7406-9d31-3a32-b229-583a47bb86ee | -2.17295 | -53.7025 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c6a671b-cc1d-37fd-9c7d-a8147174b96a | -3.29495 | -50.08183 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5fa3033c-e346-3d5a-9e7d-3231d1b9e00b | -3.8025 | -52.19132 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c01a256-ff44-3d1a-8118-06bf63a1ab00 | -2.61086 | -51.75624 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f63391dd-71e0-325e-91f2-1b7d5688bfdc | -1.13725 | -53.72229 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 536a1d7f-e581-3e4b-a6d8-67ca76164912 | -2.66886 | -49.87178 | 2024-11-07 05:10:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 36a3abfe-a061-3964-ac85-293d9dc43172 | -2.62091 | -51.30055 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 3273b3d9-9aa0-36aa-b985-0593d31522fe | -2.84095 | -52.90179 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a087e879-fdfd-3555-ae28-4149d399794f | 4.33927 | -59.83473 | 2024-11-07 05:10:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f80ab6d2-6512-3ca8-a6ff-ce12c4b438e6 | -1.50545 | -53.49584 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81c80602-1a19-3c17-8322-154b44d90860 | -2.83872 | -51.34796 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2204efd-fc9c-3680-ab1e-4dcb8b648b32 | -2.9197 | -51.04781 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c89ed8d-ecd7-3205-ba9a-4426ea0a8106 | -1.3929 | -52.18438 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd9822ba-6c11-3c84-8427-93b861d3842a | -4.39653 | -49.77298 | 2024-11-07 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1feac65f-7dfe-37b6-ad68-e26e0985cf0e | -5.03082 | -46.84311 | 2024-11-07 05:10:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| eb323eaa-ea04-3f28-9f3d-74430686d142 | -1.29643 | -54.6693 | 2024-11-07 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b7783d9-d19b-31c3-8bad-6173a9cd0663 | -3.45549 | -52.01392 | 2024-11-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04fdab05-bb26-321f-88ab-d3c54ab153d6 | -3.53384 | -51.59933 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3b44c80-4506-3fcf-8db2-01172118a9e7 | -3.09137 | -53.7129 | 2024-11-07 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44c27892-2491-3cda-b8d4-bb96410dd69e | -3.12537 | -51.11329 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1504946-99aa-3d30-9d92-35c6ae277930 | -2.72058 | -54.14685 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0466bf05-fcd5-3a58-ae35-93e3806ac021 | -2.82223 | -52.949 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f97d4777-cb13-3302-a570-b8da947d9f6f | -1.29981 | -54.66984 | 2024-11-07 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6feb0d8b-1227-38b9-b04f-22459c6c1299 | -3.03189 | -53.26506 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd1026d0-f6ec-38d0-8def-e79d1a5de98b | -3.76986 | -51.77346 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab87dbd8-927b-3b94-af49-586595362c24 | -2.8527 | -51.77936 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a93b1d5e-7766-33f6-b194-c54eb6d8a36f | -1.19518 | -53.69579 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fc00e0f4-37b6-37f0-a498-19fa91a370a4 | -1.346 | -54.61788 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce44888a-2888-3971-932e-75e3089589b7 | -1.51451 | -52.09908 | 2024-11-07 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5ffe6a0c-2231-32de-b6db-174cfc0aca36 | -3.47952 | -49.68631 | 2024-11-07 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ce7b3f8-574d-337c-82a1-630e29abd39f | -1.20668 | -54.20439 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README42.md)
