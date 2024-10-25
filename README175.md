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

## Dados Diários - Página 175

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 183ec7ae-32bd-31b3-9ca9-3322c9148cf9 | -6.99282 | -45.29402 | 2024-10-25 16:52:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 64084d90-be0a-3755-91eb-3f3f395211ee | -8.05476 | -45.48462 | 2024-10-25 16:52:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 5d79bf54-6b6e-39ed-b7ee-c22d1ca008ee | -8.05124 | -45.48772 | 2024-10-25 16:52:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4637cf14-6750-36fd-a83a-08548b537f53 | -8.05084 | -45.48527 | 2024-10-25 16:52:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a0b282e6-8646-3e22-a2b2-4da9c502b6c1 | -8.05039 | -45.48265 | 2024-10-25 16:52:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b0c86693-0921-3d1e-916a-6557703bab53 | -8.04733 | -45.48837 | 2024-10-25 16:52:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 85b2c083-4af5-3898-9f2c-9b7abc1994ba | -8.04693 | -45.48594 | 2024-10-25 16:52:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 695f928e-c7cc-3263-a7bb-0b25250228d5 | -8.04647 | -45.48331 | 2024-10-25 16:52:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 742b37d3-82c3-3034-9914-404de3267719 | -7.83549 | -45.42675 | 2024-10-25 16:52:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c35be5b4-ca31-342c-be98-b1f55f329179 | -7.83238 | -45.43231 | 2024-10-25 16:52:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5c0e65d4-9eca-3f89-b440-0639743479ad | -7.65211 | -45.38739 | 2024-10-25 16:52:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| ba9f5992-c52b-3a09-b68f-d8df596dd6e4 | -7.64813 | -45.38794 | 2024-10-25 16:52:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 22f015dc-9f62-3be5-82ae-9db52ed3ba1d | -7.9481 | -45.69466 | 2024-10-25 16:52:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c5774fc6-7728-3375-9e5a-3ffdf398e7c5 | -7.93727 | -45.70142 | 2024-10-25 16:52:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 03ecd354-f4a0-3271-8fdd-a511611ab1da | -7.814 | -45.5876 | 2024-10-25 16:52:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 14c9bbd0-f1aa-3067-80cc-6531b5ddb28b | -7.8093 | -45.58342 | 2024-10-25 16:52:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 18afdca7-91cf-3114-ac35-106a6a9b1f5c | -7.60278 | -46.1013 | 2024-10-25 16:52:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f55b4f75-0931-38ca-86e9-660c3fdb4916 | -7.55052 | -46.21044 | 2024-10-25 16:52:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 8b69be9e-d11e-3bcb-817a-d7154b9b1ae6 | -7.5391 | -45.85271 | 2024-10-25 16:52:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 01443995-fec0-3ec5-a5eb-ceeb1aaefe76 | -7.53832 | -45.84787 | 2024-10-25 16:52:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 82235b4f-484e-362d-b2bd-182b06021a31 | -7.53753 | -45.84302 | 2024-10-25 16:52:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 73a5ee4d-b1d7-37fa-b005-127d262e47c3 | -7.53674 | -45.83817 | 2024-10-25 16:52:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 741db293-1fe6-33b5-b496-004d2a11b3cb | -7.53595 | -45.8333 | 2024-10-25 16:52:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 187a7abf-b99a-305d-90f7-355803786925 | -7.53525 | -45.85337 | 2024-10-25 16:52:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 50fb19a6-b999-36a2-94fa-9e044b8a424b | -7.4936 | -45.86518 | 2024-10-25 16:52:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 37e9a787-5939-3250-989e-740a9ffc7fb9 | -7.49267 | -45.97866 | 2024-10-25 16:52:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b4ae1a51-b7c2-3fdc-abbc-1875dff65faf | -7.49118 | -45.85053 | 2024-10-25 16:52:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9be9b20f-61e2-38ec-89cf-43409ba306b3 | -7.49038 | -45.84569 | 2024-10-25 16:52:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 39abcf53-fc42-3611-b16d-9c981c5d76c4 | -7.48508 | -45.86156 | 2024-10-25 16:52:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3f228fdb-1539-31ec-b1ed-806c2c5e12f1 | -7.47026 | -45.84399 | 2024-10-25 16:52:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1fd16644-d483-3f13-ab6a-22d0a923bd36 | -7.46639 | -45.84463 | 2024-10-25 16:52:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 02a6fdd1-896e-3938-97c3-05d9ededf69c | -7.41843 | -45.75393 | 2024-10-25 16:52:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 36.9 |
| c19a81d9-840c-365c-b216-236287090b7c | -7.41752 | -45.55259 | 2024-10-25 16:52:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| a0180de1-4aeb-3ddf-b449-ed5ef210f80a | -7.41438 | -45.55473 | 2024-10-25 16:52:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 208f9f36-dc3a-324c-ae5a-aa9d18ca2d66 | -7.41044 | -45.55536 | 2024-10-25 16:52:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ab310d17-3900-3a8b-8382-f4f412022fe2 | -7.40965 | -45.55387 | 2024-10-25 16:52:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 21572bc4-1ae4-303b-8fb8-41fc4f0f57e4 | -7.40946 | -45.67396 | 2024-10-25 16:52:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 076279dc-b9e1-3622-aa60-13a4a257c815 | -7.19296 | -46.63854 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 4f62c292-6324-3168-a0b5-41ba08573f64 | -7.19011 | -46.62107 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 41b2c9a4-b9cc-3ed1-88b7-f7e46e4c458d | -7.18865 | -46.61204 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 197eefad-f3c4-3aa6-921e-1ea000d660fd | -7.18567 | -46.61715 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 9ce6daeb-0fca-3294-b839-de4a7c328952 | -7.18494 | -46.61267 | 2024-10-25 16:52:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| cdf33f92-608f-3bb3-8783-ea947ba6b9ee | -7.11661 | -46.62702 | 2024-10-25 16:52:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3dd59026-f4a8-3e9d-a83f-3322b612639d | -7.10502 | -46.5786 | 2024-10-25 16:52:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1a23b620-4fd9-3a84-92eb-22769ff92a5c | -7.07802 | -46.78645 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b2d91800-e9ab-30a7-b114-9ef5b9079b4f | -7.07745 | -46.59687 | 2024-10-25 16:52:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| c0e1394c-c137-3292-a816-de7fda84fa65 | -7.07373 | -46.59747 | 2024-10-25 16:52:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 694cd1ea-05ce-37e0-a007-1e741554b3c5 | -7.07301 | -46.59303 | 2024-10-25 16:52:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 83ed13bc-baeb-3cbd-b852-5d6c82e93e95 | -7.0723 | -46.75152 | 2024-10-25 16:52:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 69af006a-49ca-3961-8d60-6991dbb74d71 | -6.9954 | -46.66828 | 2024-10-25 16:52:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0b351553-e86c-30a3-a9ac-c0de1790fc97 | -6.96915 | -45.63891 | 2024-10-25 16:52:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f27fb76a-5bbd-31f0-adf0-c9f09653536a | -6.96522 | -45.63963 | 2024-10-25 16:52:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2304a69c-f46d-3ad4-8f8a-5c8e25b415f2 | -6.95519 | -45.24203 | 2024-10-25 16:52:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 19c24d05-d6ac-3a2d-a7c3-c2f6b1b48333 | -6.93989 | -45.4835 | 2024-10-25 16:52:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f4d791ff-e104-3f58-a021-dad53d5f0b83 | -6.93893 | -46.36716 | 2024-10-25 16:52:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 00054932-1ebc-32e6-aeb6-aa5d3a697fd5 | -9.13965 | -47.10042 | 2024-10-25 16:52:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| b852c5fa-1972-3387-a899-62f20677e6c9 | -6.93251 | -45.48843 | 2024-10-25 16:52:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 38c3e732-2f3f-37ad-afa6-2f57527c9b10 | -6.91041 | -45.97327 | 2024-10-25 16:52:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 2aad5db8-6922-3411-be3e-c101ac3fdd4a | -6.90962 | -45.9684 | 2024-10-25 16:52:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 56ac2127-e7a6-310b-bef9-0999a0d25783 | -6.85911 | -45.90248 | 2024-10-25 16:52:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| d8df1cd3-ec3b-305e-837b-f929479fed05 | -6.85521 | -45.90299 | 2024-10-25 16:52:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e4435f09-373b-3cf2-a6af-523137676a7f | -6.83285 | -46.21465 | 2024-10-25 16:52:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b47b7cff-02d9-3900-b8d2-dc8e4f2f46c6 | -6.82903 | -46.21526 | 2024-10-25 16:52:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| f1bc23d9-45ee-3e56-b4f7-260e5ca7f843 | -6.80743 | -45.28622 | 2024-10-25 16:52:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b8529df7-6911-37fa-b184-8f2ab74695b2 | -6.80293 | -45.5111 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 34f403bd-64df-3c1f-bc18-2c3fd403f289 | -6.80252 | -46.48103 | 2024-10-25 16:52:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| f7e45ccd-8ca5-3009-a597-6c598131c7ab | -6.80215 | -46.48446 | 2024-10-25 16:52:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 7448d1a5-9505-3532-8b7f-3cd58e5c6484 | -6.80143 | -46.47989 | 2024-10-25 16:52:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 1b3c4974-cff0-3f68-bb8b-b4ac9c441efb | -6.79877 | -46.50497 | 2024-10-25 16:52:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e46174ab-efcc-35df-921b-863ef209227e | -6.79877 | -46.48164 | 2024-10-25 16:52:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 1d7d5287-9073-34c2-bdc9-d4039d830ec6 | -6.79754 | -46.50389 | 2024-10-25 16:52:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4c175d0d-f7d8-384c-ac2d-be162cacacb3 | -6.78699 | -45.63644 | 2024-10-25 16:52:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f946a36a-f4b5-31c8-93eb-a3e12117574b | -6.77823 | -45.63265 | 2024-10-25 16:52:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 87d16b1c-8f81-341d-99d3-6b39bf348269 | -6.76799 | -45.42383 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 07f489bd-3886-3bdc-9fbc-0a2ed367a53c | -6.76741 | -45.42032 | 2024-10-25 16:52:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| e4df370f-cf16-393c-9b29-e48022f0f2ab | -6.73934 | -45.66164 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 05091ca2-bd52-3aba-bef2-85f7875d03b4 | -6.72507 | -46.19649 | 2024-10-25 16:52:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49bc8090-03eb-36d9-b624-d4273bdfd2e0 | -6.70505 | -46.0476 | 2024-10-25 16:52:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5250e649-7a0c-3391-a667-726ecaf2a140 | -6.63337 | -46.30177 | 2024-10-25 16:52:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5f56872f-d1df-3bbd-a324-3f4187aecb02 | -6.63122 | -46.11643 | 2024-10-25 16:52:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3e86b4c3-be00-3eaa-a688-aa9501f55471 | -6.62956 | -46.30233 | 2024-10-25 16:52:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1a1ee59a-9312-30bb-957d-7fd79d033b37 | -6.59225 | -46.24099 | 2024-10-25 16:52:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c7c62abd-7141-3c5e-beb3-31a2f0a6767a | -6.57013 | -46.24953 | 2024-10-25 16:52:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| de5accf3-1484-34e2-80c8-332282f11f25 | -6.56713 | -46.32644 | 2024-10-25 16:52:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 75d16d85-e675-30e4-a428-5c2a20577ab1 | -6.56634 | -46.25038 | 2024-10-25 16:52:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1ffe0c5e-a04a-3c09-ba81-c9b2a120f474 | -8.92048 | -45.72889 | 2024-10-25 16:52:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4dc8171f-521d-3c8f-855b-de5572a57648 | -8.91744 | -45.7342 | 2024-10-25 16:52:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 042b4750-dc90-3007-800c-6bb70a88d226 | -8.75996 | -45.86429 | 2024-10-25 16:52:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6f6c9173-4abb-3343-bec1-992e733f9d54 | -8.7599 | -45.86263 | 2024-10-25 16:52:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 24adb136-d3c0-3e2b-8d77-eb8a7efa8dd6 | -8.75613 | -45.86471 | 2024-10-25 16:52:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7da84ece-a2e2-3a11-8bba-b2783b75ee63 | -8.75608 | -45.86305 | 2024-10-25 16:52:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| cce8d1e8-7b40-300f-b42d-07f3abc201bc | -8.75227 | -45.86354 | 2024-10-25 16:52:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 81f031cb-4e24-3fae-b27a-84ef7e607794 | -8.5986 | -45.73246 | 2024-10-25 16:52:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b47418b2-d45d-3a49-ba17-fa14db85c8ab | -9.15886 | -46.65994 | 2024-10-25 16:52:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 8ee92839-f547-3eb6-bec5-066561ccc3bb | -9.15818 | -46.65577 | 2024-10-25 16:52:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a6d9c5be-5aea-30e6-ae3a-402c9328a22b | -9.15524 | -46.6605 | 2024-10-25 16:52:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 293fb439-62b2-3070-b7f6-32a5bcd1dd15 | -9.14383 | -47.10385 | 2024-10-25 16:52:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 13d2815b-db87-397f-9b2e-e5b3e5f4d368 | -9.14339 | -46.94196 | 2024-10-25 16:52:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 747e6f26-8ece-3243-9e4e-9b59317ad350 | -9.1403 | -47.10442 | 2024-10-25 16:52:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 60183b4f-cfab-3c1b-9680-9cd81900ff43 | -9.1284 | -47.09812 | 2024-10-25 16:52:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |


[Clique aqui para ver as próximas entradas](README176.md)
