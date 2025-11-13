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
| fdf7a56f-c3c4-3585-8cee-2804b73eac15 | -3.15625 | -49.16357 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f40db0b2-415b-3a61-a532-b7baf24bcd9b | -3.81962 | -45.29885 | 2025-11-13 04:42:00 | NPP-375D | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 06000697-1c98-3f09-8029-fefea2ef765a | -6.6907 | -47.79992 | 2025-11-13 04:42:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51ff1371-c523-3789-9ee5-b543f43b02c2 | -4.1092 | -48.01365 | 2025-11-13 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc68ed46-39e2-3ec2-899d-27346657e85c | -3.67291 | -45.69081 | 2025-11-13 04:42:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23649abb-a10a-39bb-9cfa-ecedfa3d8a92 | -5.25551 | -46.17944 | 2025-11-13 04:42:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d3ac138-a319-3920-ac6a-4b3ce7b0e03e | -6.29144 | -41.73889 | 2025-11-13 04:42:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f9791ef2-4f74-328d-a453-82c48894e84a | -4.25002 | -43.78572 | 2025-11-13 04:42:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6cb4da23-0a54-38b0-81c9-1facb7fd6317 | -3.86187 | -49.79543 | 2025-11-13 04:42:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 93a9c67d-b423-3886-9ebc-3322c4f3b916 | -4.20607 | -50.09552 | 2025-11-13 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80ac12a4-761b-3d4c-a001-990558081ef4 | -4.14778 | -47.65726 | 2025-11-13 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 662ab156-d25a-3c7c-a9a4-d1fb4d12e200 | -3.86298 | -49.7884 | 2025-11-13 04:42:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1329d22f-64ed-3dc9-80e7-e6747c73de5d | -2.85786 | -51.28073 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a044326e-ce7a-3162-a869-691be3ce9b44 | -3.84544 | -50.06115 | 2025-11-13 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 73ae2ab9-afdd-39d2-aa5b-38ef8cfea890 | -4.7758 | -42.71355 | 2025-11-13 04:42:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 907b0cc3-8c3a-3c39-8190-d4f0c43b9699 | -3.09553 | -49.27123 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e21ed17a-67d0-3300-8529-011c62cbe52c | -4.74413 | -50.72923 | 2025-11-13 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00e2c3d0-9358-3514-8dd6-9381610f8a6a | -5.36399 | -45.07871 | 2025-11-13 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52596e89-5afc-3837-b2af-189e9f47e5bc | -7.11001 | -42.37002 | 2025-11-13 04:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a8be5b08-f2c2-3a1f-a032-af384e88a2dc | -4.00888 | -48.80201 | 2025-11-13 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0ae16e4-4a59-339a-be94-5afce054f72e | -4.33272 | -44.00172 | 2025-11-13 04:42:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb949331-ddc8-3fa0-8d1d-580bed0e8e35 | -4.30693 | -48.24184 | 2025-11-13 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b23915f7-c5e9-37d4-88d7-581f6ecff8d3 | -6.28892 | -41.73948 | 2025-11-13 04:42:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5a2b6fd1-45ff-389e-81f4-a7e5ff0527b1 | -4.77524 | -46.44423 | 2025-11-13 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ed9fdab2-157b-38ff-ae41-93cef38fc146 | -1.67962 | -54.23103 | 2025-11-13 04:42:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e94eb604-7930-3588-a560-6453606b4093 | -4.10586 | -48.01313 | 2025-11-13 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef4d00a4-dae4-3e52-9b51-43fdbe481ca7 | -2.63327 | -52.0834 | 2025-11-13 04:42:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe267828-a482-39f3-a399-ce91e0a84803 | -7.45552 | -42.57161 | 2025-11-13 04:42:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 313cc1e8-911b-30cb-9eb9-f100ed156598 | -5.44221 | -44.65504 | 2025-11-13 04:42:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 02980492-a753-3e5f-b641-ec2ccf0e1317 | -3.21188 | -50.19625 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4d97b1b4-1e00-3bc3-b2ca-419752d39cff | -7.13487 | -41.87821 | 2025-11-13 04:42:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e41e39bb-a1eb-3d11-b6ce-8b34a7164364 | -4.71731 | -46.44862 | 2025-11-13 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 9a7f3b57-c5f6-36e5-b08d-a1665aad8952 | -6.47332 | -48.36507 | 2025-11-13 04:42:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d0abf9e-30b0-322d-9d4d-ba659e717f27 | -4.73144 | -46.72881 | 2025-11-13 04:42:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68f6f951-455f-37b3-8363-ad5dc52ddc10 | -6.1023 | -41.58063 | 2025-11-13 04:42:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 76cb644c-6204-355f-b9ba-32914ddd1205 | -1.19828 | -50.5811 | 2025-11-13 04:42:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3566d758-19f5-3b58-9f2e-eb3efadfe946 | -2.86592 | -51.47264 | 2025-11-13 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c0c6501a-8f67-3749-ad18-c0ff0437c8ed | -4.77136 | -42.71289 | 2025-11-13 04:42:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0cfe4955-9000-326c-a144-b49e56535e8b | -5.03521 | -49.56649 | 2025-11-13 04:42:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b396dbb2-ddc2-3a66-8eb0-d1174be35daa | -5.60936 | -41.06882 | 2025-11-13 04:42:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7cb0119e-d14e-385d-a2a1-498eeaafd30b | -3.58543 | -50.10765 | 2025-11-13 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e608090d-387b-3e07-9046-7464569337ca | -3.82622 | -49.52475 | 2025-11-13 04:42:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 32b36e93-5674-3571-b0e6-9854579c6c7a | -4.17357 | -48.78579 | 2025-11-13 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bd4df84f-4489-321d-9112-c6fdf3a42a79 | -4.36605 | -48.70625 | 2025-11-13 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6e73ae83-d499-3daf-b397-fe6cce390934 | -4.51644 | -50.77574 | 2025-11-13 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aacd1e5f-7a7e-318b-84b6-befdff7743ec | -3.2925 | -52.11248 | 2025-11-13 04:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 800f9573-9a0c-31f0-a4be-366315da912c | -5.45097 | -47.69413 | 2025-11-13 04:42:00 | NPP-375D | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5e2b8f9-d2a0-3e0e-bc05-fd01b32c4fce | -3.86521 | -49.79597 | 2025-11-13 04:42:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 87cbe606-f728-3957-a4c1-b1690999527c | -2.45592 | -49.26626 | 2025-11-13 04:42:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0295b13e-774a-35a4-82e1-82b324dad068 | -5.76141 | -46.52413 | 2025-11-13 04:42:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 78ba0319-12d3-3dfa-ab51-9e863d01ed94 | -7.22435 | -47.98216 | 2025-11-13 04:42:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91ab2bc1-d9d2-3607-911a-164f66efb4c1 | -5.35759 | -45.40803 | 2025-11-13 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a9f2fb59-a96c-31ba-bee6-f2691c0136d8 | -7.0085 | -46.53357 | 2025-11-13 04:42:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c843c66d-6dc3-3a3c-81fe-b9b3754430b3 | -5.26669 | -42.99703 | 2025-11-13 04:42:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 447eecbb-11a0-323f-bf59-fa621dd04f1b | -4.09807 | -48.01911 | 2025-11-13 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 463f7436-68d6-35c4-8b53-c63d47853b72 | -5.60114 | -46.25723 | 2025-11-13 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4cd8b8e8-d992-3b4e-bdcd-b07333b6df2f | -3.51695 | -49.2589 | 2025-11-13 04:42:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32dc2164-b053-397e-aafc-3a22b9568cd5 | -6.48339 | -48.36666 | 2025-11-13 04:42:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9228660-0fb6-39e7-bf03-c127f155b464 | -3.35293 | -48.38785 | 2025-11-13 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd18f85e-91d4-3beb-8cf3-c61632f1c06a | -2.31443 | -48.45113 | 2025-11-13 04:42:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bac843f2-c42d-3f58-a895-6813e3b1b7cc | -4.61165 | -49.29028 | 2025-11-13 04:42:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d7ef9ab4-04eb-3868-846b-0de909357731 | -3.34323 | -48.39008 | 2025-11-13 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54684d7e-6a1b-3264-9a90-bc9f3eaa78b5 | -2.29059 | -47.8741 | 2025-11-13 04:42:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4a1a736-675e-31c5-9735-b93fc185dda8 | -5.86213 | -47.58458 | 2025-11-13 04:42:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9023a40b-dbcc-316d-a4c3-48067e8aeac0 | -5.63896 | -41.07295 | 2025-11-13 04:42:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b87e8cac-ed29-3d41-8e19-a55a155b38a3 | -3.09055 | -49.28112 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0cb72848-2103-34b2-b8b7-18fd1d7e444f | -6.57089 | -48.73076 | 2025-11-13 04:42:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7c796d1-228e-3b58-87e3-cc4ca5b467e9 | -4.01443 | -48.80995 | 2025-11-13 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 89a0b04a-a266-37c9-b392-29cbcfb57dbd | -7.22235 | -39.9528 | 2025-11-13 04:42:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b36b7e16-fda3-360d-aad1-a18e5480c056 | -7.25987 | -45.37455 | 2025-11-13 04:42:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a87015c-2b51-3d32-9a48-f87383f61aad | -5.44266 | -44.65868 | 2025-11-13 04:42:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1f683838-14bd-3a6d-b020-3329b769c935 | -3.35015 | -48.38388 | 2025-11-13 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7a7eef43-01c4-3a98-826e-788ce0b2ef9d | -3.259 | -50.03096 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 06c78b66-a5bf-3b2f-b206-1ad44dd7676f | -4.21453 | -48.56909 | 2025-11-13 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| d984b4cf-4d2c-3f41-a9eb-3bb3abb9e7de | -7.81584 | -41.77088 | 2025-11-13 04:42:00 | NPP-375D | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ab3895b8-2a55-3efe-9210-f7a201fb1965 | -3.15567 | -50.26506 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0f7fc065-62a3-3720-950a-1c166ef0b28e | -2.04567 | -48.65218 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f8b8ddb3-4646-37dc-810d-3538b53053d6 | -5.72785 | -44.8309 | 2025-11-13 04:42:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72e2b820-4742-3928-a891-132d9af4ef18 | -3.68093 | -54.55592 | 2025-11-13 04:42:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b9aa0aa6-e56f-3cc3-af48-111eb3eb8220 | -6.29069 | -41.74401 | 2025-11-13 04:42:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f8980fd5-a2a0-3897-acdc-6c42190f7f77 | -3.22575 | -45.59077 | 2025-11-13 04:42:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 76828bbe-7074-303d-a4b7-f618b68a5856 | -3.45719 | -44.16243 | 2025-11-13 04:42:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4dd78a0e-c0f5-37d8-87c1-48026fdf3f15 | -4.20999 | -50.09251 | 2025-11-13 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 516f7141-94f8-3b7f-8ac7-e0a7ec70318e | -3.29584 | -52.11135 | 2025-11-13 04:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12679457-3e1a-39e1-b616-522127ba1bd6 | -3.85908 | -49.79139 | 2025-11-13 04:42:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50abf6ed-3914-3b7f-8a55-9087a15dc96f | -3.15508 | -50.26868 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c555ae9e-ce2a-34fb-ad41-652755c93958 | -3.24044 | -50.03902 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb80e227-7e03-373e-a966-957b351c8afe | -5.72055 | -46.50555 | 2025-11-13 04:42:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6bd04f8-4753-35a4-a4cd-60faa833cc80 | -3.10039 | -49.27914 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad117ee4-1ab0-3f20-b60e-42a98c6da9fb | -4.00816 | -48.97868 | 2025-11-13 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cead2d83-a07f-37c9-bcab-c203d893757f | -5.64515 | -41.07009 | 2025-11-13 04:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f0e24540-826e-3f53-bc17-a96a8ce47ca5 | -3.03644 | -50.28789 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7d745ab1-df51-3e59-97af-feb08b390a1d | -4.39432 | -43.08398 | 2025-11-13 04:42:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2b126fc-128a-3388-ae09-40f047fa0359 | -5.7041 | -51.44679 | 2025-11-13 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 475e5850-8780-30a6-b871-cf4b13ab9525 | -5.64452 | -41.07439 | 2025-11-13 04:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3b467e73-b2d7-3d04-a632-1d496acec8cb | -5.08938 | -40.23793 | 2025-11-13 04:42:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a065b301-01e8-38aa-a186-7f2fc731c976 | -3.48626 | -49.96469 | 2025-11-13 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 14cc286f-4f70-3489-92d2-a85d6d1f99a2 | -4.69138 | -48.63689 | 2025-11-13 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 665c3ef6-2c81-3875-91d9-316144c20035 | -7.81854 | -41.78798 | 2025-11-13 04:42:00 | NPP-375D | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 67790689-f0dd-3d38-967e-a681b1d25ee9 | -7.40274 | -43.32446 | 2025-11-13 04:42:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README25.md)
