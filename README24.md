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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6bb16cad-ef11-382b-be18-a04d9a3885c5 | -9.4699 | -67.09777 | 2025-09-23 05:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12b9bceb-a3d0-3867-a124-6186cb035287 | -9.44289 | -67.4193 | 2025-09-23 05:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 864d94c0-1c4a-32e6-b11c-80b8fb58db30 | -7.39169 | -70.1054 | 2025-09-23 05:40:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39ef70b6-eaf7-3dc7-9cd6-aea13ab74eef | -9.76613 | -65.05399 | 2025-09-23 05:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44ac45dd-a96a-3cf8-b304-6154467e169c | -10.05599 | -68.45803 | 2025-09-23 05:40:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfd2c6b7-f527-3d49-bed0-f52dc845afa3 | -9.45912 | -67.14127 | 2025-09-23 05:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7775a92-27f0-3920-ab96-e9da620d6d73 | -10.82036 | -61.41326 | 2025-09-23 05:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d6386443-ec00-3f7c-85ea-aa2bc0ff3f99 | -9.35638 | -66.51045 | 2025-09-23 05:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a803e38d-aee9-3ccd-9533-6607774dad4e | -15.91847 | -59.36914 | 2025-09-23 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04592a25-e1ff-372a-9da5-b1cb4200466c | -15.94733 | -59.48889 | 2025-09-23 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b953fe01-fafb-3833-b704-7ae47b179ace | -15.92142 | -59.37156 | 2025-09-23 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0b35400-8aae-3ced-8b58-7877138f5c4f | -15.966 | -59.48324 | 2025-09-23 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f48f56aa-a072-38de-a49b-31003fb40c21 | -15.92531 | -59.37668 | 2025-09-23 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 408ca199-877a-3401-bf14-3b8ab4c3a639 | -16.09348 | -56.94051 | 2025-09-23 05:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92ea04a8-677f-35b5-8250-991c978ff9da | -15.93645 | -59.39613 | 2025-09-23 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35f04999-b2db-3b64-a178-1fbc2540a674 | -15.83618 | -59.59006 | 2025-09-23 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6024acf-4a8c-367f-a601-dd7d3784575b | -15.94835 | -59.48079 | 2025-09-23 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c6931b6-d3b3-3fbb-86b8-191cb5a4385e | -15.73359 | -59.45374 | 2025-09-23 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8616f31c-338d-30b9-ac14-84ed4f27bbb1 | -15.73743 | -59.45885 | 2025-09-23 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95dbc192-b243-36a9-8887-0d02b912c58c | -15.91791 | -59.37344 | 2025-09-23 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2e1c928-de38-3f21-b5da-f2d787f7a84d | -15.73303 | -59.4582 | 2025-09-23 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 335c0836-2634-3cef-9e48-deaac04b4335 | -15.9655 | -59.48716 | 2025-09-23 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| af0a6e6e-19f5-3f1e-9192-065798dbeec4 | -15.92233 | -59.37421 | 2025-09-23 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f051cc9-d8f5-34e8-b63f-a389d6e8abea | -15.94392 | -59.4803 | 2025-09-23 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02b3acb6-94f4-3634-b7b5-2fff799bd57c | -15.95717 | -59.48205 | 2025-09-23 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a5cbf0c-8cd0-361b-9b02-f627e459a8e3 | -19.88172 | -52.96571 | 2025-09-23 05:42:00 | NPP-375D | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9d3c37a0-c34c-3620-b3c5-7f1b683196cb | -19.88874 | -52.96594 | 2025-09-23 05:42:00 | NPP-375D | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4534b9e5-9032-3e51-b294-48c32154a0d8 | -15.83126 | -59.59372 | 2025-09-23 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6307451-2c2c-3898-89af-411a53228b5d | -15.83181 | -59.58943 | 2025-09-23 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac5a8e9a-42a0-36f9-85f3-799caec27918 | -15.96109 | -59.48652 | 2025-09-23 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 90f03900-d5a4-3689-994d-1fda7c32e249 | -19.87679 | -52.96664 | 2025-09-23 05:42:00 | NPP-375D | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7b0cc1a4-6110-37d3-8b6d-f78b289d30ca | -15.95666 | -59.48606 | 2025-09-23 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b9751b2-c265-316b-ae2b-e59a2abe53b7 | -15.74349 | -59.44637 | 2025-09-23 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac903a20-972d-3a92-baec-ebc889691c68 | -15.92676 | -59.37486 | 2025-09-23 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a34c8974-40e5-3872-8627-a9cfac613970 | -19.88381 | -52.96687 | 2025-09-23 05:42:00 | NPP-375D | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| edeeb265-b9f9-3956-9558-8328b6f402d5 | -15.91404 | -59.36842 | 2025-09-23 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 649293c9-eb74-3493-9ceb-9c4d1bfccfe1 | -15.93092 | -59.36784 | 2025-09-23 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f47633cf-4df4-3605-bfcf-544d126ba8c7 | -15.94784 | -59.48481 | 2025-09-23 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f3b395a-3fe1-34d5-9323-be8a6f45bb9b | -15.94087 | -59.39687 | 2025-09-23 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8201ad1-85b2-31af-b593-6682d219acf4 | -15.84111 | -59.58634 | 2025-09-23 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91dc6de5-e58d-3801-9ad4-cc60564c6a66 | -15.83563 | -59.59434 | 2025-09-23 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7355ea45-2895-35dd-a556-124daf58d678 | -15.9616 | -59.48252 | 2025-09-23 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bbd9938e-ed31-393e-aaee-624d8d22a900 | -15.95615 | -59.49015 | 2025-09-23 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| df4b817d-b247-3408-b019-62517bd74a36 | -15.95173 | -59.48957 | 2025-09-23 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b018092c-81dd-3270-9cee-1b9c3521dcad | -15.94341 | -59.48437 | 2025-09-23 05:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2f29340-7f60-3226-916b-61874ecd677f | 0.15947 | -60.68192 | 2025-09-23 05:57:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 148b391f-1c2f-3dce-98ba-10d35c20c500 | -3.35626 | -59.43693 | 2025-09-23 05:57:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 284c3c43-cba2-389b-b069-19aeeced880a | 0.15861 | -60.67649 | 2025-09-23 05:57:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 78fa88bf-7820-382d-8985-c8cfe42db39d | 0.1635 | -60.67573 | 2025-09-23 05:57:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1713a05a-3cbc-3aba-96a9-bc98f8fdbc9a | -3.36244 | -59.43401 | 2025-09-23 05:57:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf6d1990-aa60-3c8c-a41d-33d0bac0ecc7 | -3.35065 | -59.43601 | 2025-09-23 05:57:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08b8b14f-8c9a-361a-ab3a-0ebb9d0cd5b2 | 0.16435 | -60.68113 | 2025-09-23 05:57:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4e2c08b-fc7f-339c-b61d-8a369ee1faae | 2.41022 | -60.70699 | 2025-09-23 05:57:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a0b5161b-f5bb-3a32-9a31-8cc544acb861 | -7.98693 | -70.90467 | 2025-09-23 05:59:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d48a424-35a8-31b3-af04-ce43a10f34ff | -6.34517 | -56.21013 | 2025-09-23 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a78913c-4b64-38e3-9e07-1bb8c1065714 | -7.37519 | -70.13435 | 2025-09-23 05:59:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c359073b-d2af-316e-abd6-828e70fcd9b2 | -7.54098 | -70.22489 | 2025-09-23 05:59:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98255cc8-9e75-3c52-b553-26048eda3277 | -7.83621 | -71.93056 | 2025-09-23 05:59:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 09682f17-8421-30f6-97af-0299c67e7ff6 | -7.68164 | -69.93434 | 2025-09-23 05:59:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c75dca1d-34f5-31ae-bb5b-1b701a38356c | -7.89196 | -70.1736 | 2025-09-23 05:59:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1f8f729-cca6-3233-8b8d-524d6fb49aa5 | -7.98969 | -70.90869 | 2025-09-23 05:59:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a854996b-088f-31da-8192-6d72d819b9d3 | -7.39719 | -70.10232 | 2025-09-23 05:59:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3cc13c0-e1d9-3e4a-96f0-7d72acee9026 | -7.55379 | -69.99237 | 2025-09-23 05:59:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09a5015d-b777-31e7-bb25-17513c0b267a | -7.37464 | -70.13781 | 2025-09-23 05:59:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 892a684b-4545-3780-9f8c-3748b57aee41 | -6.39287 | -67.95982 | 2025-09-23 05:59:00 | NOAA-20 | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d551075d-48c0-3799-9ee9-3ae62c7cfa51 | -7.55324 | -69.99585 | 2025-09-23 05:59:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9cd18e5d-222e-30c1-a5ee-a530646752e5 | -6.42448 | -67.91464 | 2025-09-23 05:59:00 | NOAA-20 | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9dc3adb-5c9e-3f70-a73f-4aec068f518b | -7.99193 | -70.85185 | 2025-09-23 05:59:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9612d31-3c6a-38c5-9faa-8459a89c38c0 | -7.99525 | -70.85238 | 2025-09-23 05:59:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31706a75-045a-3bef-a474-930d9eb50042 | -7.87836 | -71.75489 | 2025-09-23 05:59:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bcc098df-5e46-334c-82a3-b1105ad9a8c3 | -7.95582 | -70.09116 | 2025-09-23 05:59:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 873c5308-6695-3e8a-867c-21bdaee1ea52 | -6.33805 | -56.209 | 2025-09-23 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e51eb1a-6745-3f3b-8d40-67c6a70140f7 | -7.88115 | -71.75905 | 2025-09-23 05:59:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c2f65c9-cac8-3c00-ab73-6423a0ab1e9c | -7.37849 | -70.13487 | 2025-09-23 05:59:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 865f8769-f60c-3699-8c66-7461a8bc6c54 | -7.97036 | -70.88058 | 2025-09-23 05:59:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e26d6ec5-3aa0-3796-a35e-8bd0382d395f | -8.07107 | -70.33035 | 2025-09-23 05:59:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75794a6b-89ee-33d3-a2b1-161f907ebd45 | -8.06667 | -70.33676 | 2025-09-23 05:59:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b704aba9-78e7-33cb-90a7-98d00c0ca1bc | -6.33897 | -56.20205 | 2025-09-23 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bafef61e-6057-3fe9-999c-3acb5352d88c | -6.42391 | -67.9184 | 2025-09-23 05:59:00 | NOAA-20 | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d29750c-cd08-3e71-b718-3512de82b25e | -7.99025 | -70.9052 | 2025-09-23 05:59:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f284826c-3c77-3c55-80b6-4c6ab1497068 | -8.10394 | -70.18611 | 2025-09-23 05:59:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d608d185-dada-33fe-9b93-6f704558a56e | -8.06794 | -70.47926 | 2025-09-23 05:59:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3447424-2770-3ea0-85ee-0e104a9f523c | -7.55769 | -70.01077 | 2025-09-23 05:59:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13d29885-f674-3d42-82ac-f7dcd464be7d | -7.99138 | -70.85534 | 2025-09-23 05:59:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ac29bab-1b23-3a77-a285-9099004cf15d | -7.55438 | -70.01025 | 2025-09-23 05:59:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 79acb075-6575-384d-86c0-19cd01b50cc5 | -7.99356 | -70.90573 | 2025-09-23 05:59:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f810b312-d906-3cde-8682-468b518a66a7 | -6.347 | -56.19627 | 2025-09-23 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efa680b8-d363-3166-99c8-25da9d9ad2f0 | -6.59244 | -69.95024 | 2025-09-23 05:59:00 | NOAA-20 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9b57c2d-b40f-3f40-b428-e02b807286e4 | -7.93753 | -70.05632 | 2025-09-23 05:59:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 486f43f1-b639-3dcb-8ea3-c34903706115 | -7.88173 | -71.75543 | 2025-09-23 05:59:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ddf46a9-0c95-3d6c-a276-509df66f1272 | -8.07125 | -70.47978 | 2025-09-23 05:59:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76791808-dba9-37d0-a023-063a8905a51e | -8.6656 | -66.59104 | 2025-09-23 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8137c08-bf97-339a-81c6-1721ce60dc35 | -8.02981 | -70.07477 | 2025-09-23 05:59:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5653785d-8ba0-37c8-930a-3367a7686823 | -7.30378 | -70.06947 | 2025-09-23 05:59:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 544cc4dc-7e06-302c-b552-616def910fbd | -7.37795 | -70.13834 | 2025-09-23 05:59:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10c5a22e-0e5c-3530-bdf5-ad935012f641 | -8.09186 | -70.21979 | 2025-09-23 05:59:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c6949ae-f87d-387d-8b2e-2161edf02c9b | -7.91674 | -70.1455 | 2025-09-23 05:59:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c070e8d2-2802-3ad0-b6be-00f6eb0c0a4a | -7.98638 | -70.90816 | 2025-09-23 05:59:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55bf32fd-6b1f-362f-acab-caba1f51c1e1 | -6.33989 | -56.19505 | 2025-09-23 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 73c136f3-ea90-3ecb-b1af-c40c55565fb0 | -6.42104 | -67.91412 | 2025-09-23 05:59:00 | NOAA-20 | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README25.md)
