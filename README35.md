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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83c07d6c-2c5c-39be-a1c5-9ea6fa7b13d7 | -8.88983 | -71.29075 | 2026-09-05 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4e8d8d52-0fe8-3be4-aa22-0634887bd890 | -10.19466 | -69.06029 | 2026-09-05 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9914ec60-9a10-37b8-890f-959519b11d30 | -8.82697 | -70.79421 | 2026-09-05 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6584011a-1f6f-3b60-904c-3c3b782a1b43 | -12.00871 | -64.89135 | 2026-09-05 06:01:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6aaaeac7-8572-354e-843f-e266cc565def | -10.22738 | -68.65347 | 2026-09-05 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a5417ad-31ce-3225-b9ef-2bf732fda39b | -9.53471 | -68.63521 | 2026-09-05 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afdabda8-af5a-34e0-a846-158004593623 | -8.74839 | -69.2296 | 2026-09-05 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 969a6c58-73ff-3928-8304-7b6ae91dfeaa | -8.52941 | -70.48907 | 2026-09-05 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20e1800c-3bf0-3ee1-8789-e62a4b78d56c | -7.26002 | -61.0994 | 2026-09-05 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 015aeba9-cbe8-33a0-8c7f-ba8d89377e05 | -8.63189 | -67.02138 | 2026-09-05 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e596f6ef-2389-3e63-a915-ee1001a2c0c0 | -9.64972 | -69.00555 | 2026-09-05 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb44530f-7baa-38bd-8d13-bab1ac59df66 | -9.18726 | -68.26922 | 2026-09-05 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1f93026-f38b-3486-9a5d-27eb89dd8593 | -10.19798 | -69.06081 | 2026-09-05 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d5bbe81-318d-3c86-b1d7-ba815ab19598 | -9.1377 | -67.80882 | 2026-09-05 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1dda8e27-0080-3c46-9335-5d8295a971b0 | -8.62382 | -67.00452 | 2026-09-05 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1f26685-a48c-33fa-99da-3eb611c77c6e | -9.46737 | -67.4199 | 2026-09-05 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d5cc3f78-7fb7-38ff-be94-dd2160df21e3 | -7.29145 | -73.10532 | 2026-09-05 06:01:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 67a3d31a-5a0c-317c-b5ad-aee297814eec | -9.18447 | -68.26512 | 2026-09-05 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23a23ac8-9d19-30bf-90d5-a0fb02f2ad20 | -8.55528 | -70.47854 | 2026-09-05 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4acc8f30-e229-361a-8594-c3ce0b8878ad | -9.2667 | -71.66853 | 2026-09-05 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 68e93ae3-7295-3eaf-87c4-81c60d5309f7 | -10.33768 | -68.00294 | 2026-09-05 06:01:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6cf430d-c9cf-3baa-adf3-aeeda141a31d | -8.63246 | -67.01756 | 2026-09-05 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8e876f6-1de0-3803-b432-20365f092ef8 | -7.39262 | -72.80069 | 2026-09-05 06:01:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee7e5822-a056-34d1-aebb-f98199afc4b8 | -9.52085 | -68.63662 | 2026-09-05 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58b21003-b8f2-3786-a9b3-d9c047782540 | -9.53138 | -68.63469 | 2026-09-05 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b9880e9-45eb-3d15-8334-10f4a9a1737a | -10.16281 | -69.34931 | 2026-09-05 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 564d1782-59df-3846-99ad-08363003cde2 | -10.20623 | -69.00816 | 2026-09-05 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7766229-9703-3f9d-b6a0-6d880ad3bbbf | -9.18502 | -68.26157 | 2026-09-05 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22afc304-d803-389b-898b-749443edd21f | -11.90717 | -64.99261 | 2026-09-05 06:01:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 97914937-44cb-3aa7-8d01-fb5f4cd43d16 | -8.62728 | -67.00506 | 2026-09-05 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13b1fede-73d0-3a7e-aefc-b86f1df847c4 | -7.26412 | -61.10548 | 2026-09-05 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42f21887-f5de-3522-8876-d7b8487fdb3f | -8.86801 | -68.49036 | 2026-09-05 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41ceb427-7e38-3c77-b6a4-2a8674679d3d | -9.04027 | -70.73498 | 2026-09-05 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a97d4e8-828c-37e6-a3ab-5e343251b430 | -10.209 | -69.0122 | 2026-09-05 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c2f09f5-8985-31f0-af08-cdfea100eb9b | -8.87261 | -68.61337 | 2026-09-05 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25fba12d-e838-3375-b057-c296bd624c34 | -9.53526 | -68.63169 | 2026-09-05 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b869d935-38dd-33b1-9005-6f1275a3497f | -10.16612 | -69.34984 | 2026-09-05 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6f96067-37f3-3c66-b1ee-2870d9a68e76 | -9.13433 | -67.80828 | 2026-09-05 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cefeb0d8-0799-3ef4-8d6a-111aa002eb39 | -8.54134 | -67.15902 | 2026-09-05 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b86e010d-bb3c-348c-8d23-a31f5dfd96b7 | -9.84393 | -68.97935 | 2026-09-05 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2a8712df-2bd4-3c67-ba0a-d520c1a9e45d | -9.78273 | -65.29964 | 2026-09-05 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5b6fa3f-6827-39b9-97b2-04a03680314a | -8.97194 | -69.27639 | 2026-09-05 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 42c3da85-1880-378b-9c5d-ebfe046a92ef | -9.13151 | -67.80412 | 2026-09-05 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 32178d25-9bfc-316f-8184-5d85838098fe | -9.27845 | -67.99001 | 2026-09-05 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65c74429-6dca-37e4-9860-4b0d6fd389d1 | -8.79068 | -68.96181 | 2026-09-05 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a886e77-fa97-3c7e-8bd4-6e9e36f7f97d | -8.51136 | -71.39407 | 2026-09-05 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa71a272-db1c-3aca-8e56-b54729d06e52 | -9.44395 | -68.27966 | 2026-09-05 06:01:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c7bc7a97-6c3f-33a0-a53d-e34e8f70c570 | -8.54477 | -67.15955 | 2026-09-05 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b87acf6-9398-3857-8ec6-4a84d88fec58 | -8.49538 | -70.6132 | 2026-09-05 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 381f5109-acbe-3211-8036-238ea0232a80 | -9.44392 | -68.25773 | 2026-09-05 06:01:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e1b9f20e-7ad0-3659-a84c-2eaf167250d4 | -8.86468 | -68.48984 | 2026-09-05 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9524670b-f20f-3390-beb3-ee79b1dcc967 | -10.60639 | -69.14082 | 2026-09-05 06:01:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 312a3e90-74ce-3b07-ac19-b4f1602f67ca | -9.18781 | -68.26565 | 2026-09-05 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ea9590a-6c49-3be3-b75e-c1ddc020b60b | -7.38887 | -72.80006 | 2026-09-05 06:01:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0fba34e-3c69-3c53-9636-c32d132f0d6c | -14.52551 | -59.80103 | 2026-09-05 06:03:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d308b8b-4228-3f8a-b8f7-49cfda403a76 | -14.52483 | -59.80681 | 2026-09-05 06:03:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cace190-6ef6-344e-ace8-75e6af190a84 | -5.346 | -56.0454 | 2026-09-05 06:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 4a9326e3-739a-36ea-af3c-055790e10474 | -6.6698 | -59.9443 | 2026-09-05 06:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 111.6 |
| d6559084-23e3-3542-9cfa-f9c1985ba5ba | -3.7645 | -61.7737 | 2026-09-05 06:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 0178656f-071e-39dd-bdfc-fe0bec11c22c | -5.3277 | -56.0263 | 2026-09-05 06:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 162eb296-7897-35c0-9045-8723b0645a40 | -3.7827 | -61.7733 | 2026-09-05 06:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 5d106dc9-368b-3336-99b4-3d8680193919 | -6.6697 | -59.9635 | 2026-09-05 06:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| fc2fc8ec-4574-3a38-bdcd-03a442e3b566 | -6.6513 | -59.9642 | 2026-09-05 06:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 6076d9b7-5684-3a93-8297-802a84888cf5 | -5.3462 | -56.0256 | 2026-09-05 06:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 3b184e9b-a94f-3cc6-b7a8-e875a0e729a1 | -6.6514 | -59.945 | 2026-09-05 06:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 166.3 |
| 721eab1b-caeb-3c3f-a85e-6a4a0a179bf0 | -6.6697 | -59.9635 | 2026-09-05 06:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 7480813b-4e04-3410-9f81-dc46cb60375b | -3.7827 | -61.7733 | 2026-09-05 06:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 4834ceb0-bf9e-3a85-b4cc-c772acc4304e | -5.346 | -56.0454 | 2026-09-05 06:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 65ee9266-e0c4-3e4e-aa50-5e70cc7f9405 | -6.6513 | -59.9642 | 2026-09-05 06:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 4935a3f9-120e-3107-8c12-0941d75f1455 | -5.3462 | -56.0256 | 2026-09-05 06:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| b10eeb13-a93a-3970-887b-1514be303b10 | -6.6698 | -59.9443 | 2026-09-05 06:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 2480f9a9-e57a-30c2-ad03-3561f0060ce0 | -3.7645 | -61.7548 | 2026-09-05 06:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| fac51d12-f454-3c6f-ba0b-1cf8d1134ff9 | -6.6514 | -59.945 | 2026-09-05 06:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 150.9 |
| 5b85d266-8adb-3ec4-93be-b93b4d491fca | -3.7645 | -61.7737 | 2026-09-05 06:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 40f8bbbe-4f68-3bbc-ae7c-7a11dd6d7882 | -3.7645 | -61.7548 | 2026-09-05 06:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 24a3f537-e595-3f73-88b4-8ae8680191db | -5.3277 | -56.0263 | 2026-09-05 06:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| e3011db2-be62-356a-bafc-4b6f8c272c9e | -6.6514 | -59.945 | 2026-09-05 06:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 171.6 |
| 18dc56bf-e90f-3a87-96ed-5788b1df29f2 | -6.6513 | -59.9642 | 2026-09-05 06:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.6 |
| c7ef19a1-f3f3-3153-8f36-38179c6b9586 | -6.6697 | -59.9635 | 2026-09-05 06:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 097f7839-8d0d-3ba5-b036-18cb011c83d0 | -3.7827 | -61.7733 | 2026-09-05 06:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 9a7b8cd4-b526-3fae-af74-1a555f17ef51 | -6.6698 | -59.9443 | 2026-09-05 06:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 7e87fd21-3690-347c-8b29-14aaf1d440f1 | -3.7645 | -61.7737 | 2026-09-05 06:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 7f9638e0-0e97-3edb-a7f2-91f3df41beda | -5.346 | -56.0454 | 2026-09-05 06:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 97291356-270c-3d7d-aeee-227336ff34b8 | -5.3462 | -56.0256 | 2026-09-05 06:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| b5a58795-d1af-3516-8dfc-701422191e22 | -5.3462 | -56.0256 | 2026-09-05 06:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 21661700-1c58-3962-ac15-e13bf1e9d6ee | -6.6698 | -59.9443 | 2026-09-05 06:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 110.1 |
| b982cea8-6763-310f-8958-598aa3b427d0 | -5.3277 | -56.0263 | 2026-09-05 06:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 5be77289-ee1b-3927-84f1-bcbc83283f22 | -6.6697 | -59.9635 | 2026-09-05 06:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 851ecd29-8783-3f1f-8038-ec5f9528c0fe | -6.6513 | -59.9642 | 2026-09-05 06:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 9f199bfc-34b3-3c0e-93be-e7a2f2b2616a | -6.6514 | -59.945 | 2026-09-05 06:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 8c951703-8cba-3ff5-94c0-060a4821219e | -2.80891 | -48.67593 | 2026-09-05 06:42:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 3c1dac0a-6db7-3a4a-8db2-185723d49d9f | -4.67095 | -55.6244 | 2026-09-05 06:44:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 8fd772b9-90a7-3450-90f1-d865503a4ffc | -5.3467 | -56.02708 | 2026-09-05 06:44:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 9e066545-0a44-3073-bebc-19fe9acd1350 | -6.11737 | -47.23421 | 2026-09-05 06:44:00 | AQUA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 0babc668-1450-3450-9e89-b6ba910fd567 | -12.43749 | -43.4172 | 2026-09-05 06:44:00 | AQUA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 23b39e7b-ac35-3020-875a-97b2b8bb8add | -11.96026 | -43.29139 | 2026-09-05 06:44:00 | AQUA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 60b382f0-cc62-37d7-b0aa-dbc5880f875b | -6.12613 | -47.23551 | 2026-09-05 06:44:00 | AQUA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 675608d4-ccfd-3c50-97af-47b1a647ab07 | -11.96004 | -43.30017 | 2026-09-05 06:44:00 | AQUA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| b5000c4b-2bf6-30db-9f2a-05cc1652e637 | -12.44445 | -43.2754 | 2026-09-05 06:44:00 | AQUA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 4ce848f8-73e3-3dbd-8e25-7b0597b2bf36 | -5.76971 | -45.06087 | 2026-09-05 06:44:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |


[Clique aqui para ver as próximas entradas](README36.md)
