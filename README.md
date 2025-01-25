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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d774415-4d2b-3f8b-be35-84ad548887ab | -7.4756 | -35.18 | 2025-01-25 00:00:00 | GOES-16 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 80.1 |
| 9d050552-ed69-3d71-8d92-96c2b3ee9aa7 | -20.6537 | -55.7098 | 2025-01-25 00:00:00 | GOES-16 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 61.7 |
| c169f77e-07c2-3803-9c2a-1b6df8bb0371 | -17.8594 | -40.0741 | 2025-01-25 00:00:00 | GOES-16 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 79.1 |
| 3ec268b1-2a58-3619-8bf1-8cafc84a6c13 | -7.4752 | -35.2075 | 2025-01-25 00:00:00 | GOES-16 | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 195.8 |
| dfb80b5d-958d-337a-aa7a-6e52ff72e027 | -20.6334 | -55.713 | 2025-01-25 00:00:00 | GOES-16 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 174abf94-8765-37a4-9076-8be81482fa5f | -8.2665 | -35.933102 | 2025-01-25 00:02:00 | METOP-C | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| e4edf42c-d848-3daf-ba66-89a817059215 | -7.3916 | -42.763401 | 2025-01-25 00:02:00 | METOP-C | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f9e39c4e-133d-3687-9bb6-768242b47789 | -10.5316 | -36.9473 | 2025-01-25 00:02:00 | METOP-C | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 720faa91-e719-3f01-8ee9-d516df58e6e9 | -5.5629 | -35.532902 | 2025-01-25 00:02:00 | METOP-C | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 25bc1fcf-d306-3707-ad91-3fa49e181c8b | -9.4081 | -35.783199 | 2025-01-25 00:02:00 | METOP-C | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9726ee51-2f47-37dc-b90f-30006acd65b7 | -5.5648 | -35.540699 | 2025-01-25 00:02:00 | METOP-C | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| e3a0b254-5c08-34dc-aa80-e5a038e28e32 | -7.466 | -35.2001 | 2025-01-25 00:02:00 | METOP-C | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 884610c4-12d0-3a76-91e1-f0a2e3477607 | -10.5348 | -36.961201 | 2025-01-25 00:02:00 | METOP-C | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 67b48ee3-2630-37a0-bd6f-abf1614294ae | -7.724 | -35.024101 | 2025-01-25 00:02:00 | METOP-C | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ec23b128-33ea-39af-b743-442ca833475a | -8.3859 | -35.3825 | 2025-01-25 00:02:00 | METOP-C | AMARAJI | PERNAMBUCO | Brasil | 2600906 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0b32c24c-7bd1-35d0-a4d5-7afda6a38214 | -9.8611 | -36.449501 | 2025-01-25 00:02:00 | METOP-C | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b8ccdafc-8d8c-3163-b2ee-27fc2f126b84 | -9.513 | -35.834999 | 2025-01-25 00:02:00 | METOP-C | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ddb5c2e7-8e7b-387b-9ae2-f9df00d7eec3 | -8.4605 | -37.810398 | 2025-01-25 00:02:00 | METOP-C | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 7c78da5f-46d4-3d37-8e1a-d57bf9d4b99d | -9.8305 | -36.048 | 2025-01-25 00:02:00 | METOP-C | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| edc8ebe6-cb15-3c9c-bc39-d9a785ffe955 | -7.4776 | -35.205601 | 2025-01-25 00:02:00 | METOP-C | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ae8ae7f4-dc18-3395-a960-12de48bcac07 | -9.8709 | -36.447201 | 2025-01-25 00:02:00 | METOP-C | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| aa9d1e33-7ec2-3d49-aced-2a2d3046e105 | -10.507 | -42.418499 | 2025-01-25 00:02:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 318a3634-e5c5-3525-a31a-e9be49fb4c68 | -9.8725 | -36.454201 | 2025-01-25 00:02:00 | METOP-C | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6182a861-bc74-33fd-86e1-260482db6b8b | -9.5146 | -35.842201 | 2025-01-25 00:02:00 | METOP-C | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 945223ea-7358-3e6f-8648-3cb18f6408b6 | -8.4719 | -37.815102 | 2025-01-25 00:02:00 | METOP-C | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 74422a82-1c99-38fc-a690-8694252fe151 | -8.3744 | -35.377201 | 2025-01-25 00:02:00 | METOP-C | PRIMAVERA | PERNAMBUCO | Brasil | 2611408 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7f832379-1190-3c5c-8435-b5bf8f79976c | -21.984501 | -42.119801 | 2025-01-25 00:02:00 | METOP-C | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dee728e5-99c1-34ae-8afc-b700783dd73c | -21.9872 | -42.135799 | 2025-01-25 00:02:00 | METOP-C | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| df9ebc7f-d729-33a3-93f0-b0a2bbca8896 | -17.854601 | -40.054699 | 2025-01-25 00:02:00 | METOP-C | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f44f532f-a73d-3487-b0ce-7ccc155cca43 | -12.9017 | -45.064999 | 2025-01-25 00:02:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 80e7af45-7b19-3bb1-8a63-3f232d0283c3 | -7.7142 | -35.026402 | 2025-01-25 00:02:00 | METOP-C | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 35cbcf1b-91d2-3044-94a8-805e2fdab20b | -8.4703 | -37.808201 | 2025-01-25 00:02:00 | METOP-C | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| d57c4a19-b785-3590-a3b1-8c7c06dbde89 | -10.5547 | -37.5042 | 2025-01-25 00:02:00 | METOP-C | FREI PAULO | SERGIPE | Brasil | 2802304 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| de992381-b883-33c9-b48a-878e25050c48 | -10.5332 | -36.9543 | 2025-01-25 00:02:00 | METOP-C | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5604ec37-62c8-3ead-bdbc-e2f1c797f4bf | -7.4739 | -35.189999 | 2025-01-25 00:02:00 | METOP-C | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8b824e49-b9ee-3638-94c3-04e178b09418 | -7.4678 | -35.207901 | 2025-01-25 00:02:00 | METOP-C | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bc7a529c-27f6-3865-865e-279d8edae8b1 | -8.3842 | -35.374901 | 2025-01-25 00:02:00 | METOP-C | PRIMAVERA | PERNAMBUCO | Brasil | 2611408 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e9675388-10af-3041-b3bb-ab61b7b8d63b | -17.856701 | -40.064999 | 2025-01-25 00:02:00 | METOP-C | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 902dd251-2ea1-37ea-959c-fad2285d3911 | -21.974701 | -42.1217 | 2025-01-25 00:02:00 | METOP-C | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 26202574-2f81-33df-92de-3b42c9f9bd6e | -17.846901 | -40.067101 | 2025-01-25 00:02:00 | METOP-C | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 32a283ec-0676-3074-864e-045bf22f2fb3 | -7.4758 | -35.1978 | 2025-01-25 00:02:00 | METOP-C | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4255712b-f110-3017-94ba-46f4497aced3 | -12.2094 | -37.954102 | 2025-01-25 00:02:00 | METOP-C | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 17c285d8-3242-382c-994e-a94dd282b689 | -9.8289 | -36.040901 | 2025-01-25 00:02:00 | METOP-C | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9d84cc14-4cf9-34e6-858c-d74fc07d4181 | -11.0529 | -45.374298 | 2025-01-25 00:02:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 49b09396-0ba2-3418-aa95-bfe32657c444 | -12.9052 | -45.083199 | 2025-01-25 00:02:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2b46249c-0b90-366c-b172-12fe4c14407c | -6.078 | -35.397701 | 2025-01-25 00:02:00 | METOP-C | MONTE ALEGRE | RIO GRANDE DO NORTE | Brasil | 2407807 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 3a4852a5-25e0-383a-87a3-ebef35348ef0 | -10.4972 | -42.420601 | 2025-01-25 00:02:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 32a059c1-12f7-33d1-81ae-83391da523ad | -8.3048 | -39.5439 | 2025-01-25 00:02:00 | METOP-C | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 982b786a-db71-3007-9422-2d8dbf1bf24a | -11.0494 | -45.356499 | 2025-01-25 00:02:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a7f4bf36-eb2f-316d-bd95-d47601e41526 | -10.5531 | -37.4972 | 2025-01-25 00:02:00 | METOP-C | FREI PAULO | SERGIPE | Brasil | 2802304 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cded3f9d-b827-313b-a67a-d699ac2456ce | -9.3031 | -36.0425 | 2025-01-25 00:02:00 | METOP-C | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 712ba291-af14-3846-b159-257bc7862145 | -7.71 | -35.184399 | 2025-01-25 00:02:00 | METOP-C | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e44961f0-3c69-3dbf-952d-14bdf8c4db8b | -8.4621 | -37.817299 | 2025-01-25 00:02:00 | METOP-C | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| d9aa4ea3-4414-3f32-85a9-a644b30a74ed | -7.7124 | -35.018501 | 2025-01-25 00:02:00 | METOP-C | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| eb890b36-e568-3e4d-bc17-112577ddfd2e | -7.7222 | -35.016201 | 2025-01-25 00:02:00 | METOP-C | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8664e954-6129-3eec-be94-ecdee0185a87 | -7.7118 | -35.1922 | 2025-01-25 00:02:00 | METOP-C | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 90ebcbf8-90a9-3845-be2e-61fe317e3a53 | -17.844801 | -40.056801 | 2025-01-25 00:02:00 | METOP-C | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0077fd59-d6cf-31b7-a8df-1e204e4eaf2d | -9.3014 | -36.035301 | 2025-01-25 00:02:00 | METOP-C | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f0a4d194-b585-325a-8f6e-5b1ca2318710 | -7.7105 | -35.010601 | 2025-01-25 00:02:00 | METOP-C | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2b29328b-9e30-346d-93aa-091f11c00b3c | -9.8627 | -36.456501 | 2025-01-25 00:02:00 | METOP-C | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 35bf1d5b-0507-38c5-93c8-1df5ebef6794 | -12.211 | -37.9613 | 2025-01-25 00:02:00 | METOP-C | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 51868d0a-b829-3bf0-9f6f-83892d841995 | -9.8695 | -36.4591 | 2025-01-25 00:10:00 | GOES-16 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 70.7 |
| c02806ac-9167-34b8-a572-a741fc79f3a3 | -17.8594 | -40.0741 | 2025-01-25 00:10:00 | GOES-16 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 152.1 |
| e532e460-bdc7-3022-a15c-58ff49e3c936 | -9.8502 | -36.4624 | 2025-01-25 00:10:00 | GOES-16 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 69.6 |
| 1aee8f07-02f1-39b7-832a-7f0a4b1337d9 | -7.7075 | -35.0099 | 2025-01-25 00:10:00 | GOES-16 | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 85.5 |
| 2af2a801-75ee-392a-b376-1ca43cf86212 | -20.6334 | -55.713 | 2025-01-25 00:10:00 | GOES-16 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 6c310f12-7f9c-3da9-ae7b-d1b046b2ee44 | -7.7266 | -35.0071 | 2025-01-25 00:10:00 | GOES-16 | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 73.8 |
| dd9fe9f5-8b0a-3e27-bfc9-a61095da10a6 | -17.8391 | -40.0798 | 2025-01-25 00:10:00 | GOES-16 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 89.3 |
| 4f7ce4ba-2ca9-3143-b9e9-416e137d50d0 | -7.7071 | -35.0375 | 2025-01-25 00:10:00 | GOES-16 | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 69.4 |
| 01b5f276-6d8b-333e-8778-57f9e4a35a4c | -20.6334 | -55.713 | 2025-01-25 00:20:00 | GOES-16 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 92f8cfe5-00a1-3c1d-aef1-595fbbed66a8 | -20.6334 | -55.713 | 2025-01-25 00:30:00 | GOES-16 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 06b5c120-3869-3538-9075-e170f97bb6e6 | -15.253 | -60.2095 | 2025-01-25 00:40:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 96988303-1f1f-3cbf-96bd-dd29308ce8d1 | -20.6334 | -55.713 | 2025-01-25 00:40:00 | GOES-16 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 77.9 |
| d1d1c099-4fe9-3cf1-bbc6-2b5face1f2ee | -13.2212 | -50.459202 | 2025-01-25 00:40:00 | METOP-B | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 86e73655-72db-31f9-ad84-fe81d044d8ea | -15.255 | -60.188999 | 2025-01-25 00:40:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e289d8b9-0b9e-3be1-b6cc-6a2b4e4869aa | -11.0517 | -45.375401 | 2025-01-25 00:40:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2104e897-4c54-32f1-9a72-98cd949af603 | -11.0479 | -45.3605 | 2025-01-25 00:40:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ff7d451b-b789-3083-94ba-b4391a17ae90 | -12.5336 | -48.312698 | 2025-01-25 00:40:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9857cd50-b50d-369e-aefa-62c0ae1ab5fe | -20.6348 | -55.695301 | 2025-01-25 00:43:00 | METOP-B | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f8a916a3-ef20-3a69-9b80-250141318adb | -21.184401 | -48.621899 | 2025-01-25 00:43:00 | METOP-B | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1b0f04f2-629c-3e6c-bea8-e21a3c7a4887 | -18.844 | -52.479801 | 2025-01-25 00:43:00 | METOP-B | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 1a33bf16-1480-3293-a564-2f3a34ffbe23 | 3.7437 | -60.0951 | 2025-01-25 00:43:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| df27f7b7-c870-3343-a737-69cd778e58e1 | -20.6327 | -55.6842 | 2025-01-25 00:43:00 | METOP-B | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9d4e2178-6300-3608-882f-588d87685cfd | -20.644501 | -55.693298 | 2025-01-25 00:43:00 | METOP-B | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 080ff142-ce99-33f0-b867-456baccd5eee | -18.845501 | -52.4874 | 2025-01-25 00:43:00 | METOP-B | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| cd71a5bf-398e-3c1e-af7b-53b832e7f6c5 | -19.8515 | -53.903801 | 2025-01-25 00:43:00 | METOP-B | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| adaf5b26-84bb-344b-b169-92bc0ff32434 | -19.381201 | -53.5467 | 2025-01-25 00:43:00 | METOP-B | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ec4a561b-f38c-31ff-bc7b-e822b186d681 | -20.646601 | -55.704399 | 2025-01-25 00:43:00 | METOP-B | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3bc966a2-0a1e-36de-a4e0-4798ba89d47a | -9.2627 | -60.285599 | 2025-01-25 00:43:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8cb8e929-649c-3fe6-b5f7-eeb64097618a | -20.642401 | -55.682201 | 2025-01-25 00:43:00 | METOP-B | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 557db697-0242-3fed-acab-3d022589daa4 | -21.1861 | -48.629601 | 2025-01-25 00:43:00 | METOP-B | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d2d1440c-434c-3270-97cb-f8b4309638f7 | -21.270201 | -50.647301 | 2025-01-25 00:43:00 | METOP-B | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f92fbfd2-3c15-3341-b09c-ce0507afaa13 | -21.0851 | -56.380901 | 2025-01-25 00:43:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 954eb98e-13b3-3ea1-8052-dce2d6d85f1a | -15.253 | -60.2095 | 2025-01-25 00:50:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| dbdb40b9-9a43-35e4-a463-ea47ba6a5d2a | -20.6334 | -55.713 | 2025-01-25 00:50:00 | GOES-16 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 38ec8d3c-0ad3-3138-8411-ad9a743f6146 | -15.2528 | -60.2293 | 2025-01-25 00:50:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 01a81ce6-5ec3-3d5b-8478-d4de35e4233a | -27.84454 | -49.82068 | 2025-01-25 00:54:00 | TERRA_M-M | BOCAINA DO SUL | SANTA CATARINA | Brasil | 4202438 | 42 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 218401cd-5bdc-3218-8dfa-eb9664d312c1 | -19.05502 | -52.85768 | 2025-01-25 00:56:00 | TERRA_M-M | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 495cb0c0-c5c1-3624-9515-14363741e3ac | -21.18821 | -48.63762 | 2025-01-25 00:56:00 | TERRA_M-M | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.8 |
| 3e43d128-da81-320a-8fb3-d634ac5c4c3e | -18.84537 | -52.49825 | 2025-01-25 00:56:00 | TERRA_M-M | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |


[Clique aqui para ver as próximas entradas](README2.md)
