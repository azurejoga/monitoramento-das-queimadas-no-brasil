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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60cc228e-aca7-3e03-9cc9-6a810ba1c3ec | -20.39684 | -48.80267 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4adb462d-24dd-32ab-98b9-f3ed8bba4551 | -20.39662 | -48.82716 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 69.6 |
| efc2b3b5-0af6-3be6-b301-66c5552cedba | -20.39649 | -48.83109 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 55.9 |
| dab1ebf5-579f-366d-8970-ad63e854170b | -20.39628 | -48.80273 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f7c0f092-2117-3a59-b732-f0562b97472d | -20.39599 | -48.8066 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a1afaa4d-e9dd-3e11-8bc4-d4bc408a9ec6 | -20.39576 | -48.83102 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 86.6 |
| e4ec65ef-5e33-3399-9b8f-3e7bf2f8fcb8 | -20.39541 | -48.80665 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1b59d5f0-f048-3280-8b93-ef835ade501f | -20.39514 | -48.81057 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 07a280ba-e87e-3e47-9869-9d933a05ea17 | -20.39453 | -48.81061 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 38e4fddd-1dac-3109-adfe-230d1cfc8510 | -20.3943 | -48.81448 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7821f32d-02b8-38a9-864e-324231e909f1 | -20.39366 | -48.81449 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4b82981f-4de2-3621-8db5-9d9d8a3edc50 | -20.39347 | -48.81832 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6983c029-fdd7-337c-bf02-ca53139e5a83 | -20.39304 | -48.79354 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e0cd10e6-6dc6-366d-89c6-a161accea302 | -20.39281 | -48.81832 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 40458f1f-5242-35e3-ba1f-335ba2599ffe | -20.39264 | -48.82215 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 6ec59be6-8cd3-3cbb-b222-3cb16de515ba | -20.39253 | -48.79365 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5b602b81-b6c7-3875-ba40-25e77c1b52bb | -20.39219 | -48.79749 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3ee29ae6-7db1-34f0-bce9-cecc983d41ab | -20.39196 | -48.82215 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 33fc20d8-fa93-3f16-ba35-9b90613333ed | -20.39182 | -48.826 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 39066eb7-d208-3731-bdd3-aee7de0a66c6 | -20.39166 | -48.79758 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| effd754a-f426-37ac-bd5a-1c374982ed61 | -20.3911 | -48.82599 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 8b8a6992-32a7-3d17-9074-b7f15c5542ab | -20.39098 | -48.82988 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 21b22d0b-5a0e-373a-b451-d9f2eb05424c | -20.41336 | -48.85603 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a6c61fb2-5eef-34a8-a067-a6b67329b0fb | -20.41247 | -48.86005 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e2b3cbd-e718-38ec-b2e0-59d3df41de34 | -20.41159 | -48.86406 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0e9e003-e20e-38b0-976d-1202760a27f8 | -20.41071 | -48.86802 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a3349b5-febd-3282-8894-a0ebabc9282b | -20.40984 | -48.87195 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82f982b0-5c92-37a4-a88c-19984cd059d4 | -20.40961 | -48.84681 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 51526d9b-5725-3cbd-afd2-6dd09eecb8cd | -20.40875 | -48.85071 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8eee74a-2361-3a7c-b9ae-ae5b386bdbb5 | -20.40788 | -48.85461 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b83f07d5-26c0-3640-bac6-63687ac0976b | -20.407 | -48.85862 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9f39a50c-239c-318c-ae2e-ce15b43d61f6 | -20.40668 | -48.83394 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5b5da611-d3ea-3ec3-bf7b-0e4b2085aacc | -20.40582 | -48.83782 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4f1a1620-954e-3124-a67c-b24d9208cc3d | -20.40496 | -48.84171 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 47340a58-7cab-310c-9b50-1f27a316c96e | -20.4041 | -48.8456 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 449dc0d8-2017-3a6c-9e15-67cb1a19c998 | -20.40349 | -48.87444 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1fe8dabb-65d1-3953-abb5-8bfe857b7568 | -20.40325 | -48.84943 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41fb0537-bceb-36b2-baa9-97eb5d285fe0 | -20.40263 | -48.87831 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd0280c1-275a-3f8f-8e51-ab6e4e55b0de | -20.40239 | -48.85327 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 22b16482-56d7-3d6d-b2bb-a8d000cd20e2 | -20.40178 | -48.88217 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f23ee408-c48b-353b-8352-0d94093bf79a | -20.40151 | -48.85725 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 63c18422-f9b4-31eb-bf5a-d03a81e85c25 | -20.40121 | -48.83252 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 6f09308c-3f55-3419-8d9e-d3f27b917afb | -20.40092 | -48.88602 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94a08e9e-3a44-33e4-bb16-3afa64c6f3c8 | -20.40062 | -48.86128 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b77b3ff2-70f6-32b4-b2e4-d49ea3184eef | -20.40035 | -48.8364 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 6a27aaee-9532-360f-8cfe-3b191598d000 | -5.5716 | -44.8927 | 2024-10-08 03:45:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 4c0dad50-beed-3c3d-ba1d-b4f4debed702 | -5.5718 | -44.87 | 2024-10-08 03:45:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| bb561499-481f-3212-90a1-edaa9dad0570 | -9.445 | -66.7289 | 2024-10-08 03:46:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 9c3bbff2-aaee-3461-a4c5-a368cecdf2ba | -10.6256 | -55.9154 | 2024-10-08 03:46:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| da8d641e-36ec-347a-b820-bb3640a076fd | -10.8754 | -63.9169 | 2024-10-08 03:46:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 4208b62d-d58d-3879-9748-3229a63d209e | -10.8755 | -63.8979 | 2024-10-08 03:46:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 63.9 |
| c4aa86a6-0b5e-36a0-8646-2740691c83c0 | -10.8941 | -63.916 | 2024-10-08 03:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 03a4a862-4a74-3ea4-934c-bba932257604 | -11.2888 | -51.0909 | 2024-10-08 03:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 88e7ad59-ef3c-39e7-b05d-474aa89d8925 | -11.2891 | -51.0697 | 2024-10-08 03:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 168.1 |
| a5b00519-4f90-3d6d-8329-30dcabc293b6 | -11.3078 | -51.0889 | 2024-10-08 03:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 528808bf-c8fb-3a15-9c00-4ed49b1f5098 | -11.3081 | -51.0676 | 2024-10-08 03:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 309.6 |
| 596ea97d-acd8-394e-b3fc-72b7aef2dbcf | -11.3084 | -51.0464 | 2024-10-08 03:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 7f171f9b-7235-35c1-a1c6-78e7da9a7861 | -11.3093 | -50.9826 | 2024-10-08 03:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 05f8b9f9-7702-3a91-89ec-ba2fa555c88b | -11.3271 | -51.0656 | 2024-10-08 03:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 5825f9c7-b836-3576-8a10-3fe9f5488482 | -11.5232 | -65.1559 | 2024-10-08 03:46:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 59277e43-c562-3fe3-ad55-a4b1044cdcb4 | -11.5233 | -65.137 | 2024-10-08 03:46:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.6 |
| f6680ddc-cb45-3fc4-bf40-411cdf2ea30a | -12.5717 | -53.0753 | 2024-10-08 03:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 143.9 |
| c0cdedda-9f70-3084-90aa-22143be6ed23 | -12.572 | -53.0544 | 2024-10-08 03:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 121.7 |
| a8b60922-cdc6-330a-b064-33676b29bde6 | -12.5907 | -53.0732 | 2024-10-08 03:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 2cdd7c13-00e0-3feb-a2f0-0b406b190e98 | -12.591 | -53.0524 | 2024-10-08 03:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 84da6beb-6c2f-3a77-911f-4cfb746f3d78 | -16.571 | -46.4553 | 2024-10-08 03:46:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 35042937-bad4-3abc-852a-6b3232f0b776 | -16.4365 | -57.2575 | 2024-10-08 03:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.9 |
| 8a1891bb-4cb0-3d96-b1b9-84bba73820a5 | -16.8045 | -57.4402 | 2024-10-08 03:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.7 |
| f88f5bb5-b76e-3268-87dd-a5243aa77a66 | -16.8048 | -57.4197 | 2024-10-08 03:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.7 |
| 11e44dbc-d3b9-3e8a-92da-e503cfe0a8d7 | -16.9211 | -57.4881 | 2024-10-08 03:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.8 |
| 057844e6-5ad1-3ff2-a516-4caf554275c2 | -17.1274 | -56.828 | 2024-10-08 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.3 |
| 71e641fa-42df-3e75-871d-85cceb0cf922 | -16.9407 | -57.4859 | 2024-10-08 03:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.2 |
| a4a65766-421c-3ee4-96f8-eea8260d1ff6 | -16.941 | -57.4654 | 2024-10-08 03:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.4 |
| f25262bd-2ad4-396c-967b-974a5d8aed41 | -16.9924 | -56.7003 | 2024-10-08 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.3 |
| ce8f91b9-fd65-34b5-9630-38a4b01db64c | -16.9927 | -56.6797 | 2024-10-08 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.6 |
| b3317a9d-5167-3d6f-b3fe-e3cdd60c3756 | -17.0989 | -57.3857 | 2024-10-08 03:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.5 |
| 4b1a185b-10c3-3ce2-b1de-fad42a496bca | -17.0123 | -56.6773 | 2024-10-08 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.8 |
| 93a5d8a6-d483-3a7d-90a7-b3ba7272644b | -17.0992 | -57.3651 | 2024-10-08 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.0 |
| 4b65e018-2f9e-3ff9-925b-f215de4b0d74 | -17.1175 | -57.4449 | 2024-10-08 03:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.6 |
| 67566674-8727-3533-af37-0a46475f5c1d | -17.1178 | -57.4244 | 2024-10-08 03:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 116.8 |
| 2a1da7f1-f246-301a-807b-c5b0a04c47be | -17.1375 | -57.4221 | 2024-10-08 03:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 34.4 |
| fb4584f3-8b6a-3aa8-9f62-4dc8e9c2777a | -17.1471 | -56.8256 | 2024-10-08 03:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.0 |
| bf65c804-8657-3227-896c-96fdbf6826b9 | -17.1474 | -56.805 | 2024-10-08 03:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 37.3 |
| ec19c20d-e82c-31e4-9593-21ef621039da | -18.4931 | -53.4457 | 2024-10-08 03:46:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 81.6 |
| e46a5cbb-c506-3484-82e3-b6159ef0e23b | -18.5499 | -52.6391 | 2024-10-08 03:46:50 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 99.3 |
| ebb84b2b-83f1-3c95-bae1-65cb3cd7ba3a | -20.393 | -43.966 | 2024-10-08 03:46:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 75.9 |
| 085e8ab1-9fbc-303c-b038-417c7f741b86 | -20.3938 | -43.9412 | 2024-10-08 03:46:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 161.4 |
| 2d1dbdbe-973f-3c8c-a4d7-b8a7f1104a66 | -20.4144 | -43.9356 | 2024-10-08 03:46:58 | GOES-16 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 146.9 |
| ea92ff01-f516-3ffb-9463-c3b7bd750d51 | -22.18718 | -49.97187 | 2024-10-08 03:47:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 4ebaf3c3-7741-3ddf-9eae-03212ec62444 | -22.18661 | -49.96905 | 2024-10-08 03:47:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9e4e5b10-bd12-34e2-b1e6-27d6b2e0f045 | -22.18564 | -49.97332 | 2024-10-08 03:47:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| eeefa1cb-7375-3fbe-8c4f-cf0057859ce1 | -23.14441 | -49.8209 | 2024-10-08 03:47:00 | NOAA-20 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4ef14e7f-2473-323a-9ea7-f2083906b563 | -23.14361 | -49.82438 | 2024-10-08 03:47:00 | NOAA-20 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a7677520-c221-3e23-9724-34c18d67a247 | -23.31552 | -51.62888 | 2024-10-08 03:47:00 | NOAA-20 | ASTORGA | PARANÁ | Brasil | 4102109 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 45a89366-4e89-3944-a013-91c970608ffd | -23.31431 | -51.6339 | 2024-10-08 03:47:00 | NOAA-20 | ASTORGA | PARANÁ | Brasil | 4102109 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 6db3daf0-2db4-3073-a490-df4a169823fe | -23.00639 | -50.41585 | 2024-10-08 03:47:00 | NOAA-20 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 2d19333e-3725-3186-8e6c-d63a757b5ed9 | -23.00537 | -50.42017 | 2024-10-08 03:47:00 | NOAA-20 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| e40953d1-84b3-32c1-bed2-bee7f8e52e90 | -22.8183 | -51.56112 | 2024-10-08 03:47:00 | NOAA-20 | CENTENÁRIO DO SUL | PARANÁ | Brasil | 4105102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 375c389c-907c-3270-aeab-99e429237810 | -23.1189 | -52.41096 | 2024-10-08 03:47:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bd8861c1-0fd4-3870-8f6f-34b92f3f916e | -23.11744 | -52.41689 | 2024-10-08 03:47:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |


[Clique aqui para ver as próximas entradas](README46.md)
