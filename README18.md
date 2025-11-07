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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a00f7f62-81bf-3d3f-9dd7-267dce3c92e8 | -9.52588 | -66.72706 | 2025-11-07 06:07:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f613cf04-6390-3728-87f8-40fec8d2a9b1 | -9.23485 | -67.61171 | 2025-11-07 06:07:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a30dd0d8-0f86-3cab-b237-21de54e62770 | -11.99788 | -63.94765 | 2025-11-07 06:07:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11d4ad3f-e338-3dd0-89ff-7f165668e2d8 | -9.60926 | -67.14522 | 2025-11-07 06:07:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2cc51d91-ae55-3fee-b378-1a66e847ae69 | -12.02178 | -63.92506 | 2025-11-07 06:07:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f07b73f-485f-3072-9847-5773925dd6e4 | -11.96557 | -64.03883 | 2025-11-07 06:07:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c32f103a-4969-3244-935b-d75f4065ac61 | -9.64319 | -64.73724 | 2025-11-07 06:07:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3b1f5be-aa71-330a-873e-086f1f24f844 | -7.70676 | -73.12228 | 2025-11-07 06:07:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88765619-2fb1-33d0-900e-bbcb8dab72a6 | -11.9931 | -63.94379 | 2025-11-07 06:07:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c2e36ab-e610-3503-95d3-b35b28cacaa2 | -9.55734 | -66.74326 | 2025-11-07 06:07:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bcdd95e0-cc89-3cdb-97a0-afa6591e7f3e | -7.70619 | -73.12587 | 2025-11-07 06:07:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27f1c6c6-5abf-3a58-a1e6-c6440ea2c551 | -9.60776 | -67.1559 | 2025-11-07 06:07:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b240709f-fe14-31bb-be84-e9bc6cdf5404 | -11.99827 | -63.94452 | 2025-11-07 06:07:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd415d05-a79a-342c-a72a-34d3738fcc65 | -9.64249 | -64.74239 | 2025-11-07 06:07:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ccf763e-7a1f-38fd-b4ee-bf2701a9e748 | -9.66365 | -66.84547 | 2025-11-07 06:07:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d0a7b23-b7e0-3123-be3a-723d9fca09de | -12.02138 | -63.92823 | 2025-11-07 06:07:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d8554dd3-d375-33df-bc34-bdb9da4a3a56 | -9.60876 | -67.14879 | 2025-11-07 06:07:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 230cc0d0-c0b0-3936-81e2-22d63f12a786 | -9.50881 | -66.76787 | 2025-11-07 06:07:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 876c9d1e-e1c0-375a-ac9e-f65637464fc3 | -9.66776 | -66.84605 | 2025-11-07 06:07:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8137585e-3a17-3284-97eb-dfb9da74a01c | -9.60826 | -67.15234 | 2025-11-07 06:07:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 942872ec-f007-35bd-9841-0d9e03b77204 | -9.52295 | -66.72803 | 2025-11-07 06:07:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcfc26cc-1fe2-333d-8b47-f1bca84893de | -10.86471 | -69.30881 | 2025-11-07 06:07:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b0e9cbd-2926-3f0b-a193-8575eac90b75 | -3.60656 | -43.51268 | 2025-11-07 06:07:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5fa4d504-b961-32f2-b763-198add32ff21 | -5.27688 | -47.15821 | 2025-11-07 06:07:00 | AQUA_M-M | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b85dd58e-4658-3c50-94cc-16cc75d4b0be | -4.11417 | -48.01148 | 2025-11-07 06:07:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| b7d028fe-24e6-38be-b9c8-060d7745834d | -5.09004 | -44.79126 | 2025-11-07 06:07:00 | AQUA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 494a1b89-060b-3b97-b58e-e496f2a3c903 | -3.60297 | -43.51775 | 2025-11-07 06:07:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e325b5b4-841d-3f0f-b3bb-1d9c6fb03b8a | -3.34555 | -53.21634 | 2025-11-07 06:07:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 326c78f7-0a74-3338-89ac-ab4ed50e7466 | -2.69617 | -45.0852 | 2025-11-07 06:07:00 | AQUA_M-M | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c4d9739e-ab28-3614-9c5e-38ca555e7044 | -3.60027 | -49.44384 | 2025-11-07 06:07:00 | AQUA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 40a87605-ec8d-32a4-8f5d-d8ce4fa4aeaf | -3.59249 | -49.4326 | 2025-11-07 06:07:00 | AQUA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 3d30c174-d5b1-37a1-a66c-b91d43fdb57f | -3.59098 | -49.44244 | 2025-11-07 06:07:00 | AQUA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d22701c3-d799-374a-ab95-910ad5fce933 | -2.61718 | -49.2286 | 2025-11-07 06:07:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d015bdbb-6301-3a6e-a2ac-a722e10acd65 | -5.0885 | -44.80205 | 2025-11-07 06:07:00 | AQUA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| a5203f13-6d12-3000-aa55-c509fc2309eb | -2.72814 | -47.39454 | 2025-11-07 06:07:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 62da7f04-3a25-388c-b973-288e11cc882a | -3.77011 | -43.99822 | 2025-11-07 06:07:00 | AQUA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 30f44abc-9010-3e23-b28b-183501ae34be | -5.26807 | -47.15693 | 2025-11-07 06:07:00 | AQUA_M-M | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 8aa7c773-3454-372e-8116-508b4ccea65c | -3.7684 | -44.00989 | 2025-11-07 06:07:00 | AQUA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 02cdc189-18e8-3f48-a069-d6916a6f8e55 | -4.11284 | -48.0203 | 2025-11-07 06:07:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 5f80982d-e57d-373d-b40e-1916107fa2bf | -2.99994 | -45.14394 | 2025-11-07 06:07:00 | AQUA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 60653a49-b30f-3e14-9934-a98076ab42b8 | -4.45322 | -46.42908 | 2025-11-07 06:07:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 632e3a80-462d-3de7-8791-f480562bef3d | -4.93726 | -47.45721 | 2025-11-07 06:07:00 | AQUA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 90382f73-cee1-3e9b-ad3b-67d7d5751db2 | -3.42977 | -45.35711 | 2025-11-07 06:07:00 | AQUA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 5fd3f57a-6582-3fae-bc39-a89ac66f2700 | -5.27555 | -47.16704 | 2025-11-07 06:07:00 | AQUA_M-M | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1d9910ae-824f-309c-a3fd-5925746986a4 | -4.71399 | -46.42038 | 2025-11-07 06:07:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6a101ad4-ebd4-3420-a487-fb57382530e1 | -2.69764 | -45.07539 | 2025-11-07 06:07:00 | AQUA_M-M | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 8530c4f9-f68e-3cc4-91b8-c6738825f8cc | -4.45187 | -46.43806 | 2025-11-07 06:07:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 22.2 |
| e3adc394-6150-3a0f-beb5-298010626658 | -4.67649 | -46.3032 | 2025-11-07 06:07:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 63235a7d-ee1d-3fdd-8b03-d57bc3b8ddc0 | -4.29276 | -45.89495 | 2025-11-07 06:07:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3dc75a1e-9f4d-3dac-8434-7f9351a4249f | -4.71264 | -46.42943 | 2025-11-07 06:07:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c5f3d2a9-b7e0-31a6-a068-f6418add87c4 | -6.27025 | -43.6782 | 2025-11-07 06:07:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| aac0eea8-21b4-3f1c-8ce4-6172d3ae0823 | -3.34746 | -53.2238 | 2025-11-07 06:07:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| fe1321aa-0603-3275-b4f5-656a09e98cc6 | -2.99851 | -45.15376 | 2025-11-07 06:07:00 | AQUA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 7d627bf3-01ab-3be0-896d-8d6ae0893101 | -3.52706 | -47.55027 | 2025-11-07 06:07:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 91ce1fa7-a75c-3d7b-8255-72823a90455e | -3.00922 | -45.14529 | 2025-11-07 06:07:00 | AQUA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 14311c09-4bc9-3115-8a6a-5d7a1d7585ca | -3.00778 | -45.15512 | 2025-11-07 06:07:00 | AQUA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 23721dd7-dd4b-3b2c-880c-167c66a0cf3e | -6.25952 | -43.67668 | 2025-11-07 06:07:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 90340bcf-7d6c-3231-9fa7-8f6d7d6585da | -6.69416 | -39.96995 | 2025-11-07 06:07:00 | AQUA_M-M | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 16ad7ce4-dad4-3d1e-a152-28ca4e18b3c2 | -4.29415 | -45.88551 | 2025-11-07 06:07:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 23.4 |
| b63c0ec5-afea-3b5b-b0d6-448ad13b8c7e | -2.93949 | -49.35183 | 2025-11-07 06:07:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1948ca62-d766-3d73-8e41-94ecbb157f0c | -3.12654 | -45.22889 | 2025-11-07 06:07:00 | AQUA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 1c4deccc-1e1a-3f59-b6a8-ae49d31dcb9a | -2.25863 | -47.8761 | 2025-11-07 06:07:00 | AQUA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e48d005a-9a1b-3c98-85d2-66d584ac7455 | -3.52838 | -47.54153 | 2025-11-07 06:07:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| f4c485c2-b393-317f-be1d-4535dfba556f | -3.12799 | -45.21915 | 2025-11-07 06:07:00 | AQUA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 33ad0c87-7ecc-3ea2-be77-b9bb16dcf6a3 | -5.26674 | -47.16576 | 2025-11-07 06:07:00 | AQUA_M-M | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 556884bd-b039-30c3-bb67-d20d4f011898 | -9.00318 | -51.09718 | 2025-11-07 06:09:00 | AQUA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 01fcc8ae-c77b-3d08-94ab-235a78cabd3a | -7.70645 | -73.12282 | 2025-11-07 06:37:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebe671e0-faff-3651-89ed-7bb5bd5e62ca | -7.70592 | -73.12647 | 2025-11-07 06:37:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fcb68f6c-8732-378b-8765-00395b6c52ea | -3.89955 | -40.42021 | 2025-11-07 11:36:00 | TERRA_M-M | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 1d6dac72-7f09-30d0-ad36-cfc15107a55a | -4.58925 | -38.46267 | 2025-11-07 11:36:00 | TERRA_M-M | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| a8affc61-f5ad-3ac5-b686-bd67acb4a3cc | -5.58372 | -35.69618 | 2025-11-07 11:36:00 | TERRA_M-M | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 3e1d8fb5-a087-3932-9863-03cf01fcdff8 | -4.46142 | -39.33638 | 2025-11-07 11:36:00 | TERRA_M-M | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 18.8 |
| f045aaf2-6109-3152-b67b-8b417f1fc70e | -5.58232 | -35.70608 | 2025-11-07 11:36:00 | TERRA_M-M | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 21306ed8-5cc0-323c-9486-b69459d52a7e | -4.4811 | -38.94965 | 2025-11-07 11:36:00 | TERRA_M-M | CAPISTRANO | CEARÁ | Brasil | 2302909 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| d2e81f56-88da-3814-b9fc-39d698462f97 | -7.86879 | -37.91955 | 2025-11-07 11:38:00 | TERRA_M-M | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 84e242f1-8ba5-31ce-ae60-3f10742686f4 | -6.58619 | -41.3848 | 2025-11-07 11:38:00 | TERRA_M-M | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 23.6 |
| dcf537dc-9fd5-34bb-bd2b-1685f8c433d3 | -6.63588 | -39.80701 | 2025-11-07 11:38:00 | TERRA_M-M | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| f4c21949-3ce5-3e72-b804-137b78428608 | -7.85998 | -37.91832 | 2025-11-07 11:38:00 | TERRA_M-M | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 12.3 |
| a741f1c8-6731-3588-8d07-fd3189a1cc4a | -7.80577 | -38.0461 | 2025-11-07 11:38:00 | TERRA_M-M | TRIUNFO | PERNAMBUCO | Brasil | 2615706 | 26 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 4d7e009c-772e-3972-9168-7f65fd7629a9 | -11.17821 | -39.49543 | 2025-11-07 11:38:00 | TERRA_M-M | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| f77ebe74-e5b0-366e-a70e-0d3fd7f1895e | -7.63051 | -37.65036 | 2025-11-07 11:38:00 | TERRA_M-M | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 00ee34b0-aab6-30f8-8198-d65d926974e7 | -6.30158 | -37.78295 | 2025-11-07 11:38:00 | TERRA_M-M | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 48b7ec95-6642-387c-9f9b-049abc0bcf69 | -11.40217 | -39.34847 | 2025-11-07 11:38:00 | TERRA_M-M | VALENTE | BAHIA | Brasil | 2933000 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 6a4cb736-c9a2-383e-8578-c9d0db4bf003 | -8.2553 | -35.94689 | 2025-11-07 11:38:00 | TERRA_M-M | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 3e8aa3aa-99c2-31fb-a507-df35f71d5225 | -7.74154 | -37.72359 | 2025-11-07 11:38:00 | TERRA_M-M | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 2f1436c8-4d04-3315-82a8-b53cdb9a7019 | -8.12092 | -35.5048 | 2025-11-07 11:38:00 | TERRA_M-M | GRAVATÁ | PERNAMBUCO | Brasil | 2606408 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| b07238f9-5551-387e-b6e5-7e723ddcfb57 | -6.68232 | -38.54736 | 2025-11-07 11:38:00 | TERRA_M-M | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | 9.5 |
| c6e11b89-66ce-3d34-8c4e-d211e039b6e1 | -11.34296 | -39.8173 | 2025-11-07 11:38:00 | TERRA_M-M | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a976bd33-0d0b-3323-87dc-e386efa10d26 | -7.69604 | -37.64782 | 2025-11-07 11:38:00 | TERRA_M-M | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 7.2 |
| a880aa7a-1629-395c-a4b2-1dc9c7518c92 | -8.51673 | -41.08211 | 2025-11-07 11:38:00 | TERRA_M-M | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 31.8 |
| 400864a8-7696-3078-9d5c-d338ad5a6437 | -6.68103 | -38.55621 | 2025-11-07 11:38:00 | TERRA_M-M | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | 59.6 |
| a391907b-b84f-36e5-9833-d3af05de6509 | -10.67551 | -40.52347 | 2025-11-07 11:38:00 | TERRA_M-M | ANTÔNIO GONÇALVES | BAHIA | Brasil | 2901809 | 29 | 33 | nan | nan | nan | Caatinga | 55.0 |
| 2c35f1b5-973a-38f8-a1bc-1a0b8b90648c | -7.80704 | -38.03723 | 2025-11-07 11:38:00 | TERRA_M-M | TRIUNFO | PERNAMBUCO | Brasil | 2615706 | 26 | 33 | nan | nan | nan | Caatinga | 23.1 |
| e8925de3-0890-3d03-9e2a-fa91f5354f2d | -8.36232 | -40.30145 | 2025-11-07 11:38:00 | TERRA_M-M | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 11.9 |
| afa97de8-48de-37c7-b072-9ad9602c234b | -7.6796 | -37.69997 | 2025-11-07 11:38:00 | TERRA_M-M | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 70216d85-c74b-300c-8695-61662c6f3633 | -8.52154 | -41.07818 | 2025-11-07 11:38:00 | TERRA_M-M | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 84.3 |
| f3a371ff-a108-33cc-b7db-7dd3df9c9133 | -7.60798 | -38.84058 | 2025-11-07 11:38:00 | TERRA_M-M | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 10.1 |
| ffedacd4-c00a-3dcc-a3b4-d063c2a7d312 | -7.74395 | -37.95893 | 2025-11-07 11:38:00 | TERRA_M-M | PRINCESA ISABEL | PARAÍBA | Brasil | 2512309 | 25 | 33 | nan | nan | nan | Caatinga | 5.8 |
| aa6b4fdd-39f3-38bd-b9c8-0932499e722c | -8.32517 | -41.06328 | 2025-11-07 11:38:00 | TERRA_M-M | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 9239aa80-122c-3422-9bdf-b198bd87182e | -11.17691 | -39.50439 | 2025-11-07 11:38:00 | TERRA_M-M | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |


[Clique aqui para ver as próximas entradas](README19.md)
