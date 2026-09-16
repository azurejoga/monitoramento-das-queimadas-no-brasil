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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d0d1d83-1359-3a2d-95be-d000ef890794 | -7.65406 | -67.16302 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20831268-eed2-3d82-aef0-b468f1a92532 | -10.14185 | -61.18372 | 2026-09-16 05:55:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3e2c435-9423-3361-a30e-554a954302bb | -13.37976 | -57.02626 | 2026-09-16 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c32dd3f0-a3e3-3127-a661-809dee689819 | -10.39758 | -61.19819 | 2026-09-16 05:55:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc39ed78-66f8-3e12-a219-799c39c4c238 | -6.93004 | -63.13244 | 2026-09-16 05:55:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41770b0d-f3a8-3b4b-9ea2-ab461f55d697 | -9.05757 | -65.92173 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d5ae1f3d-9858-3609-a460-d1da9c1bb5a2 | -8.83098 | -62.47558 | 2026-09-16 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0408a83a-f339-3c5e-a6db-a4f5a2eba827 | -8.37034 | -54.72849 | 2026-09-16 05:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e514d81a-0a97-3ec6-b1fb-8e2c5b9bf199 | -2.70061 | -57.61773 | 2026-09-16 05:55:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ea161ef-09e1-32e9-8251-941524de5923 | -7.65242 | -67.17343 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad77df8a-b95a-3f6c-877c-49107f940d61 | -8.64272 | -66.59458 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c90e0c1-b330-3c08-9bcd-c76d45a28c77 | -8.83046 | -62.47924 | 2026-09-16 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74dd3bd6-5c07-3e10-9176-fd8b3735c04c | -9.38378 | -60.31018 | 2026-09-16 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2d75a00e-ab5a-3596-a8d3-bdb132d7ff47 | -9.83615 | -57.70564 | 2026-09-16 05:55:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d6d99bc-9c08-3cb5-b13f-5e6ec4c3ec83 | -8.71737 | -62.82724 | 2026-09-16 05:55:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5891a710-8bae-31f1-b554-47847f225293 | -7.55229 | -62.33091 | 2026-09-16 05:55:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6515f846-294e-3be7-9b3d-3fa3bae36038 | -7.64413 | -67.16145 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2630d303-0d0e-3f24-9f65-0ada6a645c97 | -8.64606 | -66.59511 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc08858f-c17c-319c-8ad3-0d24698f1cf7 | -9.04018 | -65.9195 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e51c41b-62d9-30ba-9235-d7be3376d866 | -9.09422 | -61.01575 | 2026-09-16 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 13b67be2-d240-3729-bb3d-0b1720cae864 | -7.65075 | -67.1625 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eeea7e56-5f86-3ddc-98cf-d7c70ecc3e46 | -8.66371 | -66.50322 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65eac8af-8b66-3e70-ac13-c0ea6c198bc5 | -11.80988 | -60.46122 | 2026-09-16 05:55:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3cd8c6b3-d294-3591-86f3-9cedbfe76b43 | -8.59983 | -64.10094 | 2026-09-16 05:55:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 26a2dd04-314a-3a46-871d-4af669c8e24d | -9.40639 | -62.7156 | 2026-09-16 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0fad9a10-071b-34f3-9b4a-1e0221bc5170 | -11.81404 | -60.4674 | 2026-09-16 05:55:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aea7b4b6-9599-3a1d-b7b4-8645682db922 | -9.05645 | -65.92914 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 18449081-e86b-32a4-86b1-39b7faa8943a | -8.53905 | -64.00849 | 2026-09-16 05:55:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcc71bf4-793e-3def-add3-2c3fb687f5c4 | -7.64744 | -67.16197 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52c64658-b754-30e1-90c4-0fb17d088c00 | -8.87914 | -62.51558 | 2026-09-16 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7db96baf-3cef-375e-b1f6-ad3a4691b3c9 | -9.06723 | -65.92702 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e68d7a99-cd13-347e-ad72-2b9c0b274a56 | -9.10017 | -65.93974 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 143dc956-521e-3bca-a82f-7a88ad5ae32d | -8.70489 | -62.54471 | 2026-09-16 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e614a7a2-a20c-304b-a83a-75ecaaa80cb9 | -8.70539 | -62.54113 | 2026-09-16 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 593bfb5b-fa9b-3c7a-ba38-3d1506deb141 | -3.05524 | -57.14875 | 2026-09-16 05:55:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 786068f5-ef30-3cf7-a059-75921390cea4 | -7.61057 | -67.24502 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83778101-d565-3a62-9605-e4ecee2e7c23 | -9.72609 | -64.9096 | 2026-09-16 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6e3147e0-a06d-398d-a1e5-44a171594aaf | -2.57854 | -55.99766 | 2026-09-16 05:55:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b3107bd-bffe-3c85-90d0-2d682477c994 | -9.06042 | -65.92596 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 15d6ec8d-8e8e-3a67-8368-c19df4f146a3 | -11.19266 | -55.03136 | 2026-09-16 05:55:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 503d2c17-247c-3921-943c-fb71394a8fc8 | -9.36105 | -56.93568 | 2026-09-16 05:55:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 220704df-1cea-301e-b5dd-e139d7404cf0 | -9.08973 | -61.01508 | 2026-09-16 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 13439ed9-77dc-3fe8-bb87-eefd4ed4df90 | -11.80502 | -60.46051 | 2026-09-16 05:55:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1dd18606-5875-38d6-b43c-ba598ff58ff4 | -10.69671 | -54.17369 | 2026-09-16 05:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5454d2f5-5a9b-391c-9075-94ed03fd5a90 | -9.32996 | -65.92476 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b05686a-99c4-3aa9-9cc1-99564bef99f4 | -9.56492 | -59.31713 | 2026-09-16 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e572f766-4e5f-3e17-a353-b7f9dad04205 | -8.60414 | -64.09716 | 2026-09-16 05:55:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7bf4f95c-3141-38d4-90ac-9fc06335f4c8 | -7.64082 | -67.16093 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e11ba5a7-fbe4-3ec0-9a9c-5d0d05def106 | -7.79847 | -66.91552 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef8c815a-4dcc-3253-85c0-c1d6cebb2f16 | -7.6194 | -67.25352 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04f2640e-775f-35ac-a54a-5f993211d14e | -3.10941 | -57.68498 | 2026-09-16 05:55:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1abd581-ab24-37d5-9cd7-580102d4e6ea | -9.15351 | -68.22404 | 2026-09-16 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 047e0184-f8ee-3d0d-ada4-1ea06986fa91 | -9.13203 | -65.84579 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c4b8efa1-50d5-3c5d-88b2-113ff282832d | -10.28903 | -68.85682 | 2026-09-16 05:55:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2eeb9f4-439a-3cdd-8f0b-91e3983341b8 | -8.36631 | -54.72998 | 2026-09-16 05:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02c62c00-d5a7-3f4b-b3a9-0ce4e5e2809a | -7.65628 | -67.17049 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| efd72bba-4383-34e5-9a86-27bc438791c0 | -7.65297 | -67.16997 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 250ed38b-ebba-3f59-9459-2658b8050744 | -11.19104 | -55.03711 | 2026-09-16 05:55:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1d7e92a7-e46c-318c-bde6-02da582d2dad | -9.40742 | -62.70855 | 2026-09-16 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2b6ccdf5-1998-362b-9aab-af45683db733 | -7.6458 | -67.17239 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09e28b00-279d-3d2d-8484-31de700aadcd | -9.41094 | -62.71268 | 2026-09-16 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d007c560-f465-3a7a-b3e8-8f51d5004c42 | -7.63918 | -67.17134 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d3edb82-34c1-3382-9534-ffc5cc851006 | -7.61554 | -67.25646 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9732c291-0632-3def-bf59-988ce3645883 | -2.57914 | -55.99361 | 2026-09-16 05:55:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 812f337e-c42c-3cbc-8ade-4842eafb6f17 | -8.65757 | -66.4986 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2201ee4d-d9cb-38f0-b0f3-7a1d35a06cf7 | -9.11982 | -59.51072 | 2026-09-16 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bca060fd-772e-30b2-992a-4f66f22b23be | -2.69967 | -57.62392 | 2026-09-16 05:55:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f336d9b5-e8ad-3f4e-8f6c-6b1ebd4c149d | -3.17389 | -58.64954 | 2026-09-16 05:55:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ceb23af7-f84a-3a9d-84a3-39bbba64c79d | -8.49028 | -64.03247 | 2026-09-16 05:55:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12ddae82-7956-3130-937a-ee2edc2ef051 | -9.12463 | -65.84844 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c33fb59d-4d98-36e3-aaa2-3572d82fc0d3 | -10.65893 | -58.76805 | 2026-09-16 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c12fa2aa-10fc-3545-91a3-1184acad3a83 | -9.10073 | -65.93604 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0132e948-789b-3829-9684-6865542d89f0 | -8.63507 | -63.00651 | 2026-09-16 05:55:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08dc284b-7b4d-3cfd-b94a-397cb8443c2e | -7.64911 | -67.17291 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acc8559a-e9cb-3d98-bf15-ef189ffb80dd | -7.64358 | -67.16492 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 087f1382-cc9b-39b2-b1ea-e0b6dd02c750 | -7.55632 | -62.33151 | 2026-09-16 05:55:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| facf99ba-a158-39b6-bc5a-1b00ca509072 | -3.16094 | -58.63673 | 2026-09-16 05:55:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a64ac919-3658-3952-877b-544f419d0dc7 | -9.78742 | -63.93052 | 2026-09-16 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ead5567-5c00-30fe-bc8e-5c86b5017375 | -9.21898 | -60.29838 | 2026-09-16 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb35e072-d292-35e5-b1f3-64d318c1a976 | -9.04699 | -65.92057 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 365c4fdd-d68d-31a6-aa6d-004228fa8ed5 | -9.4069 | -62.71208 | 2026-09-16 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce0864a3-e23b-3487-8e3d-ffdf8acce590 | -10.32104 | -59.14718 | 2026-09-16 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d07574d5-9e91-3de8-adc3-a193b03c6ba9 | -7.65683 | -67.16702 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 71c23b70-f76d-3d20-8211-e69fe986cc3b | -9.1013 | -65.93234 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c8647c56-3245-32bb-9762-20f5a96ce9e3 | -7.65737 | -67.16355 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b7ff212-04d3-36cf-b507-440ae8d6d60b | -2.70302 | -57.53223 | 2026-09-16 05:55:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7d0d1a34-0dc1-32b1-a680-120e32e898ff | -8.65384 | -66.58907 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64da69b3-30b6-356d-9a6e-7fca10d6246a | -10.32147 | -59.14396 | 2026-09-16 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 828fe1d3-bc3c-38a6-8637-8211452f2490 | -8.64826 | -66.5809 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 699de3be-b922-3f2a-8075-2848f7bcc90e | -8.65329 | -66.59261 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 576c9f8d-40ac-3e6a-9b42-bf07f165186a | -9.03677 | -65.91898 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df7eaf52-6494-322f-b236-a144429f5cb8 | -8.83453 | -62.47981 | 2026-09-16 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a9dc8533-d489-320b-85e4-9ae5d2064abf | -9.21194 | -65.96458 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce8b04d7-14f5-348b-8d7e-5e9a94777b6f | -8.65105 | -66.58498 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c13fb58a-83dd-3e30-b42a-dddb99197c72 | -7.61388 | -67.24554 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7bb84c9-65be-3880-a7d1-9465fe2e6aad | -9.55229 | -68.25985 | 2026-09-16 05:55:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1fa4a993-7889-3ec8-96af-2361db35cf66 | -8.71041 | -62.84716 | 2026-09-16 05:55:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 39ca7e41-6fda-31ae-8cfc-ae97964f0c49 | -9.67854 | -65.79726 | 2026-09-16 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 381a7e93-d0a1-3f12-af52-56e854eae94c | -9.10186 | -65.92864 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bdfb68ce-53b0-3505-aafc-94eba7fd6c0d | -9.41146 | -62.70913 | 2026-09-16 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README65.md)
