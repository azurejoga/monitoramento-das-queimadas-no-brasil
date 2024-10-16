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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9885079-3847-387c-b042-03a36d9348b9 | -19.59476 | -56.97274 | 2024-10-16 06:01:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 394.5 |
| 80e6e9dd-5f59-32a8-8ef4-280eb235628a | -19.59337 | -56.98254 | 2024-10-16 06:01:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 208.8 |
| bdb0e32a-f143-3dd7-ae05-dd02be09678e | -19.59199 | -56.99235 | 2024-10-16 06:01:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 35ba6d62-614a-349e-a6dd-17a2601634d6 | -19.58706 | -56.96152 | 2024-10-16 06:01:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.4 |
| 9c980b77-f5d8-3454-af51-7db942825497 | -19.58568 | -56.97134 | 2024-10-16 06:01:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.5 |
| 77e00a2d-8192-38f8-8241-cd977ceda617 | -19.5843 | -56.98114 | 2024-10-16 06:01:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.1 |
| 2209cdd7-3169-3be2-837f-5a1a5d4a6fd0 | -19.57936 | -56.9503 | 2024-10-16 06:01:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| ba55ac34-699c-3465-b0d6-b0ad39afa6d8 | -19.57798 | -56.96012 | 2024-10-16 06:01:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.9 |
| 8025a37a-ac3e-3587-869b-30d2e1b66e05 | 1.0016 | -52.2164 | 2024-10-16 06:05:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 861c850a-843c-35b3-b539-cc83fc255716 | -7.77917 | -66.96184 | 2024-10-16 06:12:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac344c1b-3090-3b25-b81d-7a753356c5f0 | -8.45541 | -66.9602 | 2024-10-16 06:12:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a7802a8-bdf0-355d-9691-f73d09981429 | -8.45478 | -66.96472 | 2024-10-16 06:12:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 56efbcad-f0d2-3774-ae17-5752b272ffdb | -8.45415 | -66.96928 | 2024-10-16 06:12:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 41085d25-f38c-384f-b49a-e5846f542844 | -8.45089 | -66.95957 | 2024-10-16 06:12:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e44e8b7a-0ab0-3b16-957a-44abb80d7f14 | -8.45027 | -66.96412 | 2024-10-16 06:12:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 00778c93-d6a4-3388-be6a-5b7df81e0e89 | -7.60609 | -67.35862 | 2024-10-16 06:12:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b96d5b4-4428-3c9c-a613-d683217bf7c5 | -8.79335 | -67.62842 | 2024-10-16 06:12:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a2ef523-5575-3f05-95ae-77fe9a096fb7 | -8.78902 | -67.62781 | 2024-10-16 06:12:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f7e980a-b335-3c9c-80a3-355b8121a7fb | -9.17437 | -65.39272 | 2024-10-16 06:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01ff6763-9fd0-35f7-8b78-a90af5c1abda | -9.17397 | -65.39569 | 2024-10-16 06:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc2e6fef-1e25-38ce-bfff-dbf2f61788ac | -9.17356 | -65.39864 | 2024-10-16 06:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 416f4c78-9c18-38a6-8e4e-829cd4ac1119 | -9.17315 | -65.4016 | 2024-10-16 06:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97e49d1c-2373-3f6f-9ab4-699b94a04479 | -9.17275 | -65.39182 | 2024-10-16 06:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24b6a456-319b-381c-9478-0bb7eda3d6b4 | -9.17274 | -65.40456 | 2024-10-16 06:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b550048d-e411-3fd8-939a-5bc537906f2e | -9.17236 | -65.39478 | 2024-10-16 06:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c2b5e3d4-6a05-3ed0-926f-f8b0ab01b996 | -9.17234 | -65.40752 | 2024-10-16 06:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81291be5-d5ac-35b1-a13a-b4d09a137c40 | -9.17198 | -65.39775 | 2024-10-16 06:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 72219f8b-dc92-3a22-a9d2-87114a39f0fa | -9.17159 | -65.40071 | 2024-10-16 06:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1130acf0-3b02-3ac7-86b5-2727e93f9c4d | -9.17121 | -65.40368 | 2024-10-16 06:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 65e820e2-6769-3af5-badf-9d09a207c06d | -9.17082 | -65.40665 | 2024-10-16 06:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e779a59-70aa-3bc4-96e1-9bb5b038737a | -9.16848 | -65.39795 | 2024-10-16 06:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf4f97f3-feeb-3173-9f30-ef9181c64e17 | -9.16807 | -65.40091 | 2024-10-16 06:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c56f4f6-c9b7-32fe-92bb-640a9caa661f | -9.16767 | -65.40388 | 2024-10-16 06:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd54d0f3-5f7b-39a1-9f8b-eb9b16c65f14 | -9.1669 | -65.39703 | 2024-10-16 06:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e24c7a01-3dbc-3009-9e57-c3ee97660abe | -9.16651 | -65.4 | 2024-10-16 06:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0b9d747c-5787-379d-a214-1e2d6303a9bc | -8.61821 | -70.0356 | 2024-10-16 06:12:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b5f55cdc-be19-3db2-9289-56fcc1c18242 | -8.6145 | -70.03504 | 2024-10-16 06:12:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5f0c9759-1ac8-37a8-bb33-2566a246ccc7 | -8.61384 | -70.03948 | 2024-10-16 06:12:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aaf5f8b9-6ef6-38de-91a8-f9119387a4c3 | -8.03729 | -70.17223 | 2024-10-16 06:12:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed5c2f41-2c39-35e2-92c1-844222724d56 | -8.03216 | -70.20641 | 2024-10-16 06:12:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3ea6374-4b3b-3926-84fe-f70998f6bbf4 | -8.26855 | -71.13512 | 2024-10-16 06:12:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87789d0d-6b46-336d-9868-f130b747ed9f | -8.0886 | -70.88757 | 2024-10-16 06:12:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a96c56d3-471b-3fa0-bf69-0ffe72db01c7 | -8.02465 | -70.90289 | 2024-10-16 06:12:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1aadd7b0-4ce2-32bd-b5e9-82956ec60beb | -8.02112 | -70.90236 | 2024-10-16 06:12:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60d18df7-3f63-33a8-b2c8-7b89ef948858 | -8.00837 | -70.81898 | 2024-10-16 06:12:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5062bc14-b9a7-319f-bf82-fdb9ab6d198f | -7.96416 | -70.8978 | 2024-10-16 06:12:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 757b470e-a26c-37e1-adf9-8f363bec94f9 | -7.95224 | -71.38042 | 2024-10-16 06:12:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 60cbc6e3-d652-3ce8-b5ba-4c12ace32d27 | -7.93608 | -71.5325 | 2024-10-16 06:12:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9dd0c460-c914-352b-b827-576b7e1e2c97 | -7.93551 | -71.53625 | 2024-10-16 06:12:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f2184ad6-c2db-39f5-ad9e-6d07e608ba62 | -7.92122 | -71.5609 | 2024-10-16 06:12:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad30cc2a-a16e-3325-8041-51565520893b | -7.91779 | -71.56036 | 2024-10-16 06:12:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 34c2b300-dd77-3f6e-9e34-082a30b485fa | -7.82389 | -72.83215 | 2024-10-16 06:12:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 643e32ea-bb69-353e-89a0-3235b7ade0d5 | -7.80912 | -73.10114 | 2024-10-16 06:12:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe78ddc5-0538-3b70-876b-ffe1d6626ba0 | -7.80092 | -72.91439 | 2024-10-16 06:12:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4a28a8e8-0fc5-3036-8d81-ca4351229177 | -7.75837 | -72.28672 | 2024-10-16 06:12:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbdbe55b-7622-36a4-924d-209547854a8e | -7.75502 | -72.28622 | 2024-10-16 06:12:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b06ab7e-96d0-39ea-8934-12af69c876f2 | -7.75447 | -72.28979 | 2024-10-16 06:12:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4755b4c4-cdca-3bda-834c-b48c77091624 | -7.73901 | -72.91871 | 2024-10-16 06:12:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 637a2ae7-b29c-3875-9fee-50e16b01ab26 | -7.72445 | -72.83779 | 2024-10-16 06:12:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e0cc96bd-5984-3486-8501-6177517d663a | -7.40906 | -72.61693 | 2024-10-16 06:12:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7a93027-3a3f-34d2-9008-204c3a0e5336 | -7.40627 | -72.6129 | 2024-10-16 06:12:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f2d7511-600a-30f6-a890-e81f76d89966 | -7.40241 | -72.61589 | 2024-10-16 06:12:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a176966-8a79-3db6-bb21-465407758ec5 | -7.40186 | -72.61939 | 2024-10-16 06:12:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c4e36cec-87d6-3854-a560-0e00a1b3f2a0 | -7.36668 | -72.628 | 2024-10-16 06:12:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6be5520e-ddb8-3d75-a553-3cf670371397 | -7.32632 | -72.44897 | 2024-10-16 06:12:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cba26fbb-ade5-3cbd-a71e-830c7fe18bac | -7.32577 | -72.4525 | 2024-10-16 06:12:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b33848eb-f3fa-34a1-8a16-e00273466546 | -8.17983 | -72.92315 | 2024-10-16 06:12:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56f0f8fd-40e6-3c1a-88b2-1a41c4fc5272 | -8.17929 | -72.92664 | 2024-10-16 06:12:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6c55eae-22d3-3411-99db-8493e2764f4b | -9.99264 | -66.86098 | 2024-10-16 06:14:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b655805a-a3f3-3c9b-8992-cd67987c64dd | -9.76767 | -67.30417 | 2024-10-16 06:14:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e450aaca-1ad2-3574-9589-d2cbd4aaa561 | -9.89707 | -67.5946 | 2024-10-16 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4dfe3c8-a15c-3984-8873-9e8092f31505 | -9.7807 | -67.94132 | 2024-10-16 06:14:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 530944d1-93e3-3c03-8d7b-c49011bd0fc9 | -9.78012 | -67.94537 | 2024-10-16 06:14:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3eb5fbc9-288d-38d9-859e-aa08d8bd0f27 | -9.71146 | -67.47827 | 2024-10-16 06:14:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64990a12-5bb3-3851-ad84-6aa3cf47e8d2 | -9.68252 | -67.58944 | 2024-10-16 06:14:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fee45809-3f35-3f93-a708-7c6d717bf91c | -9.19209 | -67.21084 | 2024-10-16 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d309ca35-bb67-3d04-ade0-137f235614ef | -9.59268 | -66.78137 | 2024-10-16 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3937221-4a70-37ca-a885-2d5f06f707fd | -9.47814 | -66.55206 | 2024-10-16 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a540e45-e507-3e74-bc06-6b5b3ba66e16 | -9.45303 | -67.14626 | 2024-10-16 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab01b428-b0eb-391e-8204-e7d94f9c3242 | -9.45239 | -67.15081 | 2024-10-16 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fe8a01c9-cd7f-358a-8dcb-9517e0caf98c | -9.44908 | -67.0752 | 2024-10-16 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c1d1cdb-07ed-397e-bbaf-fc4840923212 | -9.44788 | -67.15015 | 2024-10-16 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fd00d927-6ed1-36ee-b444-63cf7821484f | -9.44518 | -67.06996 | 2024-10-16 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f77f2f60-005a-3ac7-8339-d183c2c6006e | -9.44063 | -67.06932 | 2024-10-16 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45873481-11a7-34ef-a371-32e38395365e | -10.41969 | -67.57313 | 2024-10-16 06:14:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53b104cb-20b9-3a77-912c-aad28a977f79 | -10.1151 | -67.23576 | 2024-10-16 06:14:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 017c33f3-8b04-3a37-807a-03dd02399151 | -10.11358 | -67.2374 | 2024-10-16 06:14:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f96a918-9013-3aac-935f-a7992d3b7338 | -10.09978 | -67.35085 | 2024-10-16 06:14:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 142ad26b-03ba-32ac-b456-ca6f58d6c7d8 | -10.09741 | -67.35225 | 2024-10-16 06:14:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fc4a9bbb-ad15-3bb4-9db5-1ab37fda44a2 | -10.09672 | -67.22572 | 2024-10-16 06:14:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a9c59a0-fa90-3f6d-8d94-1288122de612 | -10.00059 | -66.90691 | 2024-10-16 06:14:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 28bb5ca3-c744-3715-99b1-350d83f78010 | -9.40082 | -67.84495 | 2024-10-16 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53793445-9940-3b54-a0f1-339fc3ef736d | -9.40026 | -67.84904 | 2024-10-16 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0ea1b28-0ebc-3bb4-8160-06473c072527 | -9.15156 | -68.68195 | 2024-10-16 06:14:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0f568b38-a99c-392f-9980-b022717c72cf | -9.15134 | -68.68221 | 2024-10-16 06:14:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee448b0f-66ef-39bc-bcfb-4511e41ef2ca | -9.15081 | -68.68581 | 2024-10-16 06:14:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5379ca1-6196-38d7-af64-33bf09202341 | -9.1475 | -68.68134 | 2024-10-16 06:14:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9f6287b8-e962-3e70-9216-e00da885aa8f | -9.1246 | -68.63789 | 2024-10-16 06:14:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33f79e3b-d8f9-3112-9e5b-d5097d7e6dcd | -9.66489 | -68.57513 | 2024-10-16 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d512131f-8b45-3bf6-a6e8-974ba7f4b6d3 | -9.64574 | -68.96727 | 2024-10-16 06:14:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README73.md)
