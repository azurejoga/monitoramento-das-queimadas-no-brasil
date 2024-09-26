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
| 9027b7e7-1b8f-383c-abe4-67154f265a28 | -8.89336 | -53.02884 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cfc27376-6a37-30a3-b782-f7f7156a4a46 | -8.89109 | -53.02102 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d6249287-b6f3-301c-a3ce-e00fcd9bf602 | -8.89053 | -53.02468 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0ff422a1-556a-34ac-aaa2-c3b539dedabd | -8.88997 | -53.02836 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a9a1a86a-9f97-35b3-99f7-d094fbd15baa | -8.84394 | -51.98874 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c484752-a2ad-3450-868f-64621de942e1 | -8.8404 | -51.98827 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 355c96d7-764a-3e53-92ad-5f0702c81191 | -8.80284 | -51.99852 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfb971ba-3309-3c05-b834-4f62881b6c70 | -8.80225 | -52.00249 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4722913-da77-3b8c-b534-549e4ebcf31b | -8.7263 | -52.04921 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 418e5ae7-796d-3f3b-b0e4-b5512427c401 | -8.72572 | -52.05309 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f3330202-021e-3f59-85bf-21e100c767e5 | -8.72339 | -52.04474 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8bf47fe5-a682-38d0-8b4e-18fe87b03225 | -8.72279 | -52.04868 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2e56877c-8afd-3c52-b68f-8a82f22332bb | -8.71248 | -51.99758 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb9a6f5c-d9a3-31fd-a89b-c99353991141 | -8.63097 | -53.14195 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b572175-f3cc-3d00-9661-4b0a038454d2 | -8.47526 | -53.22491 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9ff2ee1-fc30-34fa-85cf-902ee689a983 | -8.47471 | -53.22853 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6482d7bc-29cf-3c42-b3df-aa056dd4398c | -8.47416 | -53.23214 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2544fc8-6153-389f-b823-3ab9ab594c6a | -8.473 | -53.22507 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc181b0c-551e-37ad-910d-faac1fd878a8 | -4.03466 | -54.19483 | 2024-09-26 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7df28c0-01f3-3b03-aecf-f96795c47089 | -8.47189 | -53.23227 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c2a4dd7-713a-321c-a519-229ed3eb486f | -8.4702 | -53.22095 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93c40ebe-94cc-3b3f-a714-59fcb43d6e29 | -8.46964 | -53.22456 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bf9ad91e-7d10-3e9d-be5f-384c2cf075ca | -8.46909 | -53.22816 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b09401f1-782b-3357-aa86-26eb4e8b3c42 | -8.46628 | -53.22403 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b24eb879-5be9-3ef9-8d0f-ac7fdf913c41 | -8.17756 | -53.14981 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52176c5f-fa1b-3f0f-8519-b8365177b1dc | -8.1742 | -53.14927 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27ac6c89-177b-3dd6-ae68-402cf06d31a7 | -8.11453 | -53.16609 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52df6c5c-cb1d-37ac-b27e-0bc210ef72d0 | -8.10445 | -53.16452 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68dc1084-9219-3f1f-a4c5-b004859d2b40 | -8.05416 | -53.17883 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bcdd47c2-d519-3ee6-bb1c-52033596632f | -8.05136 | -53.17469 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c4f159b-547c-3386-89b3-2ee16909f44d | -8.05081 | -53.17831 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f64aafad-7ba3-3f82-9c49-b87bbf74d22f | -8.048 | -53.17417 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d605f9cc-2f67-336c-9f28-ee2fcd7772a0 | -8.04745 | -53.17779 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83b6e349-732d-3c0e-abbe-55ffe0d14bba | -8.04509 | -53.17783 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8ddfd2e-c86a-377e-8be6-d5b41a49d327 | -8.04174 | -53.17727 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86676adf-66ae-3a8c-b88b-aa9574fbadb3 | -9.57269 | -53.40792 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d83ee386-e416-3bb1-80a8-9436e08e4062 | -9.56871 | -53.38875 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 070132fd-c0e0-35a8-98cf-96239bb9db88 | -9.56596 | -53.4069 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 792621a8-93d4-39ad-990c-02ec9be4ec1c | -9.56479 | -53.39187 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4f0a390-b78c-3d92-946c-e5046cccde40 | -9.56424 | -53.39551 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87aa38e8-251f-3894-a11c-5a026b6b3cf5 | -9.56369 | -53.39914 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 152eb7e4-97c4-39f9-8c2b-725049898522 | -9.56314 | -53.40277 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a2552a3-5330-351c-b73e-4e4bef2b0a63 | -9.56259 | -53.40639 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed9ab7e7-edac-3505-a47b-5f207456cdc2 | -9.77073 | -53.18453 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e69cdf6b-7799-3ae8-8cbb-60542c5719ac | -9.75038 | -53.18138 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e53d0564-90ab-3b0c-b78c-083e8a9c91b2 | -9.74699 | -53.18086 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49e10d13-3b1d-3eb2-a993-a7e369546dc7 | -9.72668 | -53.20031 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d51612d3-754c-3b54-8ea2-9fed669c5faf | -9.72612 | -53.20398 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe549e15-5be0-32ce-8431-0fe8b9b833a6 | -9.72557 | -53.20766 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fa4698d-6d05-3603-b7e6-13e7ce4af282 | -9.72329 | -53.19978 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 52c2560e-9299-3f8f-96c5-55526941bcba | -9.72273 | -53.20346 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26b0d20a-5a4f-3094-9c7d-70dbaed06868 | -9.7199 | -53.19925 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fec45a3a-1caa-35aa-bc84-6da1302645c6 | -9.6748 | -53.19206 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bab07c61-3ddb-345d-bf45-08fa4066b6f5 | -9.67141 | -53.19153 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12f84999-a3c6-35c0-bc90-4a934e4bf8ac | -9.67085 | -53.19521 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ddef7725-987f-352e-af1c-8bbd6f4f4f11 | -9.66802 | -53.191 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2820147d-3bfb-399e-8999-477d9c758c01 | -9.66463 | -53.19048 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e9fe859-8cc7-3f8a-859e-5143d5dc8803 | -9.66125 | -53.18995 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1e00096-0aed-39dc-a644-9b542f74ec6b | -9.65786 | -53.18942 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3c82b26-f35e-34c3-92d7-08e99bd9ea4a | -9.65166 | -53.20729 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b218b14-f1d3-3de3-9442-5f775a97749a | -9.6511 | -53.21097 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 83a749ad-b29b-365e-b26f-2e14603878af | -9.6494 | -53.1994 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3641fa3f-88e8-3183-8456-ffc4c5760607 | -9.64883 | -53.20309 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6177caf0-b1da-3f97-965d-f62260d6d489 | -9.64657 | -53.19518 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59debfe5-0f2d-3bce-b7e5-e92eaf974e81 | -9.64038 | -53.21304 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aae36a2e-be26-3f35-a9e8-6b3f55c50dbc | -9.63478 | -53.24971 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d218b87-ec03-3456-af58-3e13648cc2db | -9.63249 | -53.21933 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab218c34-b242-3758-adf9-4f2a1503b118 | -9.63196 | -53.24551 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| edb7aa25-ae53-30da-8140-840b4b788cd6 | -9.63193 | -53.223 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 54d8199f-d316-33e2-af29-9daffc84f83b | -9.63137 | -53.22667 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f7997b42-4a86-3591-9382-b9e5d8a7b3c6 | -9.63026 | -53.23399 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4baaa0ab-df0e-34d5-bc68-258f6fa480be | -9.62914 | -53.24131 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65d8c69a-9c80-3e58-8956-77299def4df5 | -9.62855 | -53.22247 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12622070-0c5c-3962-b08a-092ebf1dd06e | -9.62687 | -53.23346 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| becb4693-7bfa-3c9d-8b9e-2ec9bccdd5b0 | -9.62632 | -53.23712 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bbfabae-9fbd-3e50-92ef-057545363a16 | -9.62576 | -53.24078 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e9caccc-7cbd-39af-94ac-d5b6860a3940 | -9.62293 | -53.23659 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7fcb122-ee17-34e1-8fe5-be56d151287a | -9.64043 | -53.25809 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a3298ee-44e9-3b8e-8527-9b783d7ab4ca | -9.63705 | -53.25756 | 2024-09-26 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ed4caaf-7aaa-31f2-b80c-6a645b771de9 | -9.62635 | -53.25962 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e592df27-f280-32e3-9f12-274b17fd0e04 | -9.62297 | -53.25909 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba9150cc-5d05-34b9-a98a-859de628a451 | -9.61903 | -53.26223 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 015ddefa-7691-3468-a2d5-bd95b8cc967e | -9.61847 | -53.26589 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d89c2398-a54b-39d2-bb93-4bf54c013a97 | -9.6168 | -53.27689 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff8877ef-3d3b-3231-9ca7-d69a1c7e95d3 | -9.61624 | -53.28055 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22273081-068a-3b84-abe8-a2a86a7e3231 | -9.61509 | -53.26536 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63858fed-b871-32af-9393-a4709aaeaef3 | -9.61453 | -53.26902 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ffa97ef-e9ea-3a2f-8a60-2ee24bde5606 | -9.60388 | -53.29356 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9fdc6a6-5d11-3c57-bc7d-be3c683867ef | -9.60333 | -53.29721 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79ce4a32-cbaa-3fae-ae3e-04486261875a | -9.59996 | -53.29667 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d7808c1-cd2a-3036-97cf-e786f8f17674 | -9.58927 | -53.29874 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 394afd99-995a-3582-a357-65606712e493 | -9.58872 | -53.30238 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7743931d-40e7-3930-b0f4-e9c308d46a41 | -9.58086 | -53.30863 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8483232f-96ec-3e32-b008-013019d0e71d | -9.58031 | -53.31227 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba98f96c-47e2-3d49-9c34-d5a9d444bec0 | -9.57975 | -53.31594 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76b0a38a-f81a-3aa4-80dd-0219f57f08f9 | -9.57362 | -53.33366 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21df1a30-7031-3cf5-a158-27899b5a6780 | -9.57306 | -53.33731 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bebfff2-3c1e-37de-8e01-41cc83f10888 | -9.56803 | -53.34771 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e82e56a6-416d-33f5-8ac0-4c2c70a1a94c | -9.56755 | -53.3737 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13179401-29d5-384f-9569-8321e8a297c3 | -9.56748 | -53.35135 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README95.md)
