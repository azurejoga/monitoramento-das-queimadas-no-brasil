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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1fae082-afa3-38ce-8bb6-a76c3b03e191 | -1.50148 | -54.95007 | 2024-12-01 04:21:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 923c4b11-554c-39fb-9960-06f2ee6312ec | -2.67728 | -46.6008 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34d25126-c05b-3a38-8a91-f001cae4a9c7 | -3.97653 | -46.75426 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f9e05e33-ecfd-3b80-b2d1-5ff03ad9b10a | -3.09642 | -54.29361 | 2024-12-01 04:21:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5b13efff-85b7-3945-83b1-6a6a51a2e5da | -3.02465 | -52.35509 | 2024-12-01 04:21:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 656ae989-4518-3d9d-a894-67fbd97b4a73 | -2.52863 | -54.07339 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f8fa35b-22a2-3af6-849e-e90950de2a87 | -2.56242 | -46.40205 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1af2396b-da34-338c-86a6-4467d41ed910 | -1.99981 | -50.40276 | 2024-12-01 04:21:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d64ca697-2ca9-32f1-92d2-e453e33c86e6 | -3.81956 | -46.55061 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a79f394d-531b-38b1-be62-b1df0587b794 | -1.3259 | -55.67111 | 2024-12-01 04:21:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9638c188-bec5-3b87-a496-de40c5cf4e34 | -2.99541 | -51.062 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a9de16b1-bfb1-30ff-9860-596e7ed9558e | -0.00783 | -51.16583 | 2024-12-01 04:21:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4e8348e4-b68f-3dd3-b3e2-a96896846ef7 | -3.65572 | -50.71152 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3cd302a-ca7b-3c69-8605-314bf85cd53b | -3.69639 | -47.12472 | 2024-12-01 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3de8e824-a0dc-3341-83a7-8ecd41551b83 | -2.55672 | -46.56275 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d359d288-13ee-337a-adbb-9f8568340284 | -1.27002 | -54.55642 | 2024-12-01 04:21:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84ecf53b-4954-3a0e-b153-501265f14f1c | -1.24945 | -54.54829 | 2024-12-01 04:21:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ddfcaa18-1015-3e91-a39a-d3b3e64bcd94 | -3.07518 | -53.80411 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ad35b800-c931-313a-8093-adea40264828 | -2.74732 | -51.75135 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 85ebd945-0cd3-3f27-8c4d-fd55621b53bf | -1.66726 | -45.75089 | 2024-12-01 04:21:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18da38c3-8dd9-36b0-bdf3-fcbcf47a680f | -2.08236 | -46.67157 | 2024-12-01 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb1b6979-197a-3c43-b89e-c1583d658c2c | -3.7672 | -47.71379 | 2024-12-01 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 857edd05-49b5-31d3-829b-39dacfa5d8fd | -2.60444 | -46.57812 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 290d602e-18f3-34c1-be6d-2c40b94ceec9 | -3.20273 | -46.56196 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb184c76-2603-3075-8774-d7d4ee72eb06 | -2.65906 | -51.87593 | 2024-12-01 04:21:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 61bb7e12-d5b9-34ab-9ad3-a7b9d8c1ac12 | -3.99292 | -46.65111 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d06bbd1e-ce80-3ba0-ad87-c0545ffbde5d | 0.07311 | -51.48685 | 2024-12-01 04:21:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 969b8f3f-ce17-393a-9d6e-ca26279f1180 | -1.26324 | -51.74797 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 50045d17-e20b-3eda-9c2d-0136bd5ff153 | -1.71551 | -52.62989 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b02bef81-ddc3-3f90-a64f-beb98364941e | -0.17302 | -51.36052 | 2024-12-01 04:21:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb221dcd-ffd4-3233-83c7-cb2e722a1f87 | -1.70415 | -52.4725 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1decabb6-7133-3dee-a071-2a5fb7605d36 | -4.79277 | -43.24105 | 2024-12-01 04:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04566d20-5417-30d8-adb3-76e720db01a6 | 1.1559 | -55.99328 | 2024-12-01 04:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 37dd4439-0739-3fc2-aa0c-67dfd44c7e30 | -4.498 | -43.91349 | 2024-12-01 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50c7e2c2-3059-315f-aef8-5ac2790ecd14 | -1.26479 | -54.55116 | 2024-12-01 04:21:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0125d28a-ab83-3e60-ace9-1461a0ec0503 | -4.55474 | -43.30631 | 2024-12-01 04:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 7e4d1205-fd07-3d1e-bacd-d72f263668d2 | -3.27341 | -50.20865 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 132b4e1b-036b-357f-9c1d-545806da3a26 | -2.51366 | -51.82924 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 92509ac4-b857-3d4b-b575-6994b454837d | -3.25983 | -48.76864 | 2024-12-01 04:21:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 33eb2cc7-da28-3a55-b36d-fa4b1e528372 | -3.99637 | -46.65171 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf34afd6-371c-3c67-be17-e64d95f6ef14 | -3.60222 | -50.37569 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 790894f2-456f-3316-b46f-7d3722b2dabd | -3.26353 | -45.37188 | 2024-12-01 04:21:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 379dc06b-acdc-393c-aae4-246ea11d142d | -3.03589 | -50.24004 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d41b3154-b0cd-37e4-ab21-644b4ecc2cfd | -2.85619 | -54.09636 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 592e5abb-e0aa-3493-bb79-171eb8421380 | -4.55584 | -43.29922 | 2024-12-01 04:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| f34190aa-1624-3434-8c43-78571d33716f | -2.23083 | -46.39106 | 2024-12-01 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 353c73a0-010c-39fe-b3f5-3cfe1f154b09 | -4.21772 | -47.71328 | 2024-12-01 04:21:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 130e572e-d39f-3e88-955d-870db340f60a | -1.25476 | -54.55327 | 2024-12-01 04:21:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a94c159a-756d-3f00-99bb-5c803e972c4a | -1.08392 | -46.7765 | 2024-12-01 04:21:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90865484-1bcb-3dca-a097-fa851b2171d5 | -3.21417 | -53.12063 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c638448b-03f4-3163-8bd7-2661e1614b1e | -2.91064 | -54.11668 | 2024-12-01 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cfe8a84e-768b-3c52-a76d-e06130e86403 | -1.70659 | -52.44337 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3eff1bd-5cc4-39d1-965c-9b5ec68d0c9e | -1.05074 | -51.75735 | 2024-12-01 04:21:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 50cb3b37-c5e2-30fb-9c5b-46ddf3c61c08 | -3.10242 | -50.36375 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa0bf016-cc5a-31aa-9b3e-a5b8e9b4ec33 | -4.28125 | -46.29361 | 2024-12-01 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e4708ef-4c51-3dc8-a7e7-ed729ea5ef97 | -1.43241 | -53.39755 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5eebdf6c-4877-3e27-bd43-3fded48c1e44 | -1.24621 | -54.55288 | 2024-12-01 04:21:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83dba8c3-636c-379a-a314-140eabbfb687 | -2.83597 | -46.85771 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58404a60-d4ff-328d-8168-b438087c81e2 | -2.12215 | -46.58077 | 2024-12-01 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cca19157-3e57-388d-be3b-30ea4674673c | -3.05774 | -51.05547 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 964d6579-0c2a-35e0-940b-3027471182d1 | -2.4671 | -46.57689 | 2024-12-01 04:21:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05d65e8c-2fc3-36f1-9d6b-a2854a726085 | -4.10685 | -46.91238 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 441f3c9c-c06a-3190-858a-7ae4a531e7b4 | -2.98702 | -45.57228 | 2024-12-01 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 8a8685d0-ef03-305c-b5f8-6a9719d0bb84 | -4.53118 | -45.74077 | 2024-12-01 04:21:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 183cc57d-57b7-3c02-9d58-cb9179a8bbed | -2.88378 | -50.73766 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1039882-2fba-37ca-a09b-80a3d788e32a | -1.66568 | -53.77358 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 35dece19-1014-3836-a9da-10d85535e278 | -1.24875 | -54.5527 | 2024-12-01 04:21:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48996b42-74b6-3691-88db-3ad4d8cd3d67 | -2.76705 | -51.69032 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d5495f89-e726-3b4b-bd37-2ceed9a79e24 | -1.25294 | -54.54908 | 2024-12-01 04:21:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d89daeb7-519c-3ef6-8d83-6e8782461a15 | -2.68016 | -46.60522 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| da77f068-267a-3072-994a-bb258e48749c | -1.15016 | -48.32832 | 2024-12-01 04:21:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 981cd338-be53-3bde-99f8-30cdea438b41 | -1.25467 | -51.7907 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 019ed2ad-3da8-398a-b5b1-4141114cc6d3 | -1.33607 | -55.85042 | 2024-12-01 04:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c876645e-7ab1-3caa-918c-24cac20cb300 | -3.25165 | -50.75549 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a4cf6d68-2540-3df9-b029-7f59b0e02b82 | -2.8167 | -45.20474 | 2024-12-01 04:21:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0160ded1-3f8d-3a27-b02e-cf309ceeaf52 | -2.97973 | -45.57482 | 2024-12-01 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3dc9d1ce-b07f-328d-96a8-2743b1f2b2b8 | -1.96992 | -46.46296 | 2024-12-01 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b93443a5-5132-3f9d-ba48-f549fbc2d859 | -4.74976 | -43.71426 | 2024-12-01 04:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 989a6d4c-36e6-355b-9f8d-9fc6a9a2557a | -3.26687 | -45.3724 | 2024-12-01 04:21:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b41cef54-6f2d-3e26-8558-53c5d636dc1a | -2.98366 | -45.57176 | 2024-12-01 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2059bd23-87d5-36c4-890a-32d447765abc | -1.03668 | -51.7408 | 2024-12-01 04:21:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bd4fe464-63ef-32dc-825d-38b12eb56ca4 | -3.31528 | -50.14082 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e34e5358-c55e-3646-a993-44ab1beefec2 | -3.29415 | -47.03214 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70f111fc-5b55-3ff6-8a15-3dd308909452 | -3.3708 | -51.53826 | 2024-12-01 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2ce68aa8-8a26-3180-aa5d-9caeac6cd68a | -1.70466 | -52.46945 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f13172d-e353-3cd5-a198-5d497fe85b1a | -1.60866 | -46.23064 | 2024-12-01 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54f8f69e-3b62-3b95-a316-dac3ca0af02f | -4.04247 | -46.93398 | 2024-12-01 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75bb6a15-ba87-39ed-8c6a-5fa3b8f32aa4 | -3.63248 | -40.85876 | 2024-12-01 04:21:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 299556ae-97c3-39fe-8a19-ce909422f7fc | -2.59805 | -46.57318 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7384e71-d5e0-3f2c-ac30-4c110badc203 | -2.80947 | -53.05821 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ecf169be-aa09-3a71-8da7-e9c91ecd8ee9 | -1.72199 | -46.24756 | 2024-12-01 04:21:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8799bdd5-4c50-3d9b-9ad4-9349b116c3a5 | -3.93754 | -46.7086 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efabfe77-da5e-32d5-a8f9-052298f93ea4 | -2.96983 | -53.4536 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7b67ff0-a075-3a6f-adec-4fc166b12323 | -2.58479 | -51.72599 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5f0e510-2638-3fce-9f56-23c0404d2e05 | -1.72912 | -46.22513 | 2024-12-01 04:21:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af3444b3-69da-3579-b676-3d26f2d1f507 | -3.69737 | -50.1673 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bb6bd0ca-1ae0-3798-9077-078bc764a3bb | -1.33048 | -55.8442 | 2024-12-01 04:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d90dec0-e1ae-3e7c-a865-7722c104d3a5 | -2.59071 | -47.02998 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 630a1f3b-a080-321b-a4d0-4ab58dfbd269 | -3.90696 | -42.41602 | 2024-12-01 04:21:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f74e886c-dc6c-349e-ad0f-29f392d318a7 | -3.98084 | -46.72715 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README26.md)
