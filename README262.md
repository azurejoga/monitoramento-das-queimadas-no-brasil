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

## Dados Diários - Página 262

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83eb25e5-fc56-3f6e-9e68-07f5053fef73 | -6.1484 | -51.927 | 2026-10-07 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 118.3 |
| f1862082-e920-3c7a-bec1-9260e24eb9a3 | -8.629 | -67.0667 | 2026-10-07 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 0121c6ad-c88a-3c9e-be49-263bb98c9f91 | -5.9644 | -40.9627 | 2026-10-07 19:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 96.6 |
| dcedec42-c6ea-360b-a569-2e0ca927b94d | -5.9951 | -43.5973 | 2026-10-07 19:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 63b819ae-a0f5-33c0-8e9a-15a3e429b1cc | -3.6049 | -54.5736 | 2026-10-07 19:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 34189ccb-8265-3c0b-9d3e-644c27c50d3e | -3.7166 | -54.2297 | 2026-10-07 19:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 3e18b643-4430-3902-b3e1-4f41b12a82a5 | -9.3395 | -65.4451 | 2026-10-07 19:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 102.6 |
| f3a45e8c-0568-381a-b32e-f01d737e99de | -6.3353 | -43.3365 | 2026-10-07 19:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 428f3bc8-30d4-334a-a176-a8d719f1eaaf | -4.2558 | -46.3855 | 2026-10-07 19:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 180bac39-bd81-38ed-be40-f741b0f02c01 | -6.5852 | -53.0331 | 2026-10-07 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| aa1a228c-18c9-347e-aa10-aaa058cec0c1 | -6.3541 | -43.3349 | 2026-10-07 19:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 123.2 |
| d3718455-ce94-3457-8724-2ca8e6cd018a | -1.9848 | -56.7037 | 2026-10-07 19:40:00 | GOES-19 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| ad3ef23d-623d-3e36-979c-57cd78ad5a1b | -3.0547 | -54.2478 | 2026-10-07 19:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| e80f0b5b-2078-31ea-ab6f-8b7f6060f73d | -3.7789 | -45.2459 | 2026-10-07 19:40:00 | GOES-19 | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 6a4d0c92-2169-3dc1-932b-13e66f8512e0 | -5.9699 | -46.3714 | 2026-10-07 19:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| cc64bd38-3278-38a7-a599-84853816aada | -5.6931 | -53.5073 | 2026-10-07 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 098acac4-6f8a-3341-9023-f855ef63164e | -11.6186 | -43.6433 | 2026-10-07 19:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| db488c97-13b4-39b8-9ba5-16f7fdcb9ce7 | -11.7143 | -43.652 | 2026-10-07 19:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 3cc85cd1-8223-3af4-b119-6c37f7f0bc97 | -8.2184 | -46.3396 | 2026-10-07 19:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 806bcbdc-e310-3f68-82e0-f87d93ed4c83 | -6.9143 | -43.6583 | 2026-10-07 19:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 2022fbeb-f9a9-30f8-9042-3c795f304d0a | -6.9944 | -48.6629 | 2026-10-07 19:40:00 | GOES-19 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 812ed204-0358-3aed-8eb2-3576faedf2dc | -5.6934 | -53.4667 | 2026-10-07 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 33bf9dc1-117e-31db-91ae-60801a703596 | -3.2357 | -50.1805 | 2026-10-07 19:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 72109f4f-7502-3bba-9cc0-7b3d610c63ee | -6.8952 | -43.6833 | 2026-10-07 19:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 161.7 |
| 1ab1ed75-a223-3d21-8b2e-50cf5a430e03 | -6.8764 | -43.685 | 2026-10-07 19:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 79823df7-9c46-3e0c-863d-fe204153c572 | -5.6748 | -53.4879 | 2026-10-07 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 66aa3e78-c584-36fd-8ce7-71b5549ed897 | -4.3045 | -50.77 | 2026-10-07 19:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 2cf735c0-b7a0-3b55-97ca-4bfc22b41073 | -11.6382 | -43.6166 | 2026-10-07 19:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| b2425c5a-4c82-3cad-bc2f-e9372da91ab8 | -8.5366 | -67.069 | 2026-10-07 19:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 120.3 |
| 3ce0b89d-3c2d-3e25-b0e1-3b063b4c473a | -5.9512 | -46.3727 | 2026-10-07 19:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 9951d5a0-6f79-3798-96d7-5da770a2d564 | -9.5004 | -66.7831 | 2026-10-07 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 09b621a5-a277-3935-b303-1e3a808139d9 | -0.5993 | -49.4293 | 2026-10-07 19:40:00 | GOES-19 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 081891c4-d497-3139-bc4d-ef784849bdd4 | -3.8152 | -45.4019 | 2026-10-07 19:40:00 | GOES-19 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 9114ac4e-75d2-34f3-abfe-17b6231e595a | -3.5875 | -54.3138 | 2026-10-07 19:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| f298cb35-208e-32d3-84c8-ff27d633086e | -2.9327 | -58.3204 | 2026-10-07 19:40:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 7f8b01be-d44e-3efd-bc31-aa5067d8b6ba | -4.777 | -55.7104 | 2026-10-07 19:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| fb19dc0b-3ec1-3a10-a613-685c67400a21 | -6.6037 | -53.0321 | 2026-10-07 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 116.9 |
| deadac0e-6044-3b48-8436-dc37ae78c0a9 | -3.9662 | -56.1316 | 2026-10-07 19:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 6ca89800-51c5-3bc5-baf0-82a4059da20d | -1.562 | -47.7465 | 2026-10-07 19:40:00 | GOES-19 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 228.5 |
| efe3f693-042c-3922-b22f-40a63a0e31fd | -3.1101 | -54.1661 | 2026-10-07 19:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 460.1 |
| 0b194c7d-d0a1-3b04-b394-6fef5d1650e8 | -5.372 | -44.1751 | 2026-10-07 19:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 201f21ce-5dd5-3c67-9eac-91f83ae71558 | -8.6293 | -66.9926 | 2026-10-07 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 102.7 |
| f14c1582-67db-3864-a3fc-a61b2ca4c17b | -3.2738 | -54.6626 | 2026-10-07 19:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| c8622633-d73f-3027-9b51-26e08df87889 | -4.9422 | -55.8035 | 2026-10-07 19:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| d47b7f7e-a119-343b-81cf-b3aa566dd30d | -9.0407 | -65.9215 | 2026-10-07 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 137.5 |
| c689504e-0a12-34ac-8771-3d25d7efc4ad | -2.6859 | -49.0539 | 2026-10-07 19:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 410cd52d-799a-3f1e-b5ed-81cdc3553550 | -1.1094 | -54.1601 | 2026-10-07 19:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 194.8 |
| 40992a74-e5e2-3333-b097-e732d4d21abb | -4.7585 | -55.7308 | 2026-10-07 19:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| b57b35de-1406-3a2b-be22-dd0d81394bc3 | -5.7489 | -53.4641 | 2026-10-07 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 27cc426b-3578-3f0a-bdd9-9c196d8c9f50 | -6.4021 | -52.7159 | 2026-10-07 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| a3866f8c-25a2-3769-a6f6-b7cc2ca9a8e2 | -3.1787 | -50.5597 | 2026-10-07 19:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 29316da7-67c8-3241-856d-ac8f8ef7979e | -9.4751 | -64.3336 | 2026-10-07 19:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 110.4 |
| ae214c23-b446-311e-9ac2-cf841377a0e9 | -3.5866 | -54.5542 | 2026-10-07 19:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| b90e2e84-a953-3e06-ad01-d9d1ce4f172f | -6.0447 | -53.49 | 2026-10-07 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 2b3e330c-fe04-3c11-8296-ff294b35cabe | -3.1462 | -54.3658 | 2026-10-07 19:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 9a8d6b8e-7fbe-3c66-9dbd-64cd2e8603c6 | -11.619 | -43.6196 | 2026-10-07 19:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 218.5 |
| 272621fa-051a-363d-9fdb-f9a1350ea678 | -4.3471 | -43.8021 | 2026-10-07 19:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 476e4cf5-d9a9-3760-af27-3bf8f8c098ef | -9.9596 | -43.5045 | 2026-10-07 19:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 69b356e7-cf29-3850-9c9d-56f50395c8bd | -3.2137 | -42.953 | 2026-10-07 19:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 2d334663-e0e3-3d44-a696-9cc1602658ee | -3.7481 | -51.2079 | 2026-10-07 19:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 092dfa38-88be-3f95-8855-59791a60b2dd | -3.3637 | -50.4701 | 2026-10-07 19:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 400.5 |
| 3413156a-10e2-3439-b507-50fb92143b17 | -9.0592 | -65.9209 | 2026-10-07 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 160.4 |
| 9324b163-0af3-3d17-bbde-60342fc26220 | -7.3747 | -46.2161 | 2026-10-07 19:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| c93395a7-378a-3bf8-ab12-72b0f306e2ab | -3.4762 | -50.0883 | 2026-10-07 19:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 138.7 |
| 749d7def-1487-3d57-aa3a-d3dc7fe4dd63 | -3.2451 | -57.8693 | 2026-10-07 19:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 8c8527bc-a289-3b37-a4bc-8faeb37bf432 | -3.295 | -53.8597 | 2026-10-07 19:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 76a7f113-2e6c-3f8b-95d9-4f3e44de1d7f | -3.2957 | -49.1202 | 2026-10-07 19:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 1a62094b-70c4-319f-97b4-af988b0830c3 | -8.555 | -67.0871 | 2026-10-07 19:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 5d26dafb-db52-3bb6-93b7-50827f6f1bf1 | -6.1244 | -47.9227 | 2026-10-07 19:40:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 6c894f6a-440c-38ed-83ed-51c464d437ed | -10.9938 | -45.4985 | 2026-10-07 19:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.6 |
| f881f45e-d937-3630-8245-26fcc28f4ad7 | -6.3163 | -43.3614 | 2026-10-07 19:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 1ee3bdd1-59eb-33cc-b82c-68e02d519c3e | -3.11 | -54.1862 | 2026-10-07 19:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 248.6 |
| 56073dc1-46d8-39bc-89a4-727e99902f0a | -7.6767 | -72.296 | 2026-10-07 19:40:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 263.8 |
| ce230cc9-06f9-33cc-bade-860684ddcf53 | -3.2949 | -53.8798 | 2026-10-07 19:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 47ad4d82-232c-3ec0-81c3-012edc09fb22 | -3.3134 | -53.8592 | 2026-10-07 19:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 213.8 |
| d01c4618-5d9a-3f60-afc0-5cf7ac64e7c0 | -5.6932 | -53.487 | 2026-10-07 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 327.7 |
| fa9d8a97-56b3-3c87-be2d-ea09ea34a879 | -6.1482 | -51.9477 | 2026-10-07 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 697749a8-1e5d-32a0-aa9b-0dffdb9e41fe | -5.9772 | -43.5057 | 2026-10-07 19:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| ddefc23a-a3ff-3291-b6c7-05b143288f7f | -7.5762 | -40.359 | 2026-10-07 19:40:00 | GOES-19 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 188.6 |
| 81cf73ac-e771-35af-9e19-ca67fe95833f | -9.0406 | -65.9401 | 2026-10-07 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 148.9 |
| e7d8c88f-ef5b-30f1-9a48-3508c1b42e6d | -6.6039 | -53.0116 | 2026-10-07 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 78975b7b-26e4-3a03-936d-c88305782e82 | -4.1574 | -44.2726 | 2026-10-07 19:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| db3fa734-0459-3032-9ef3-4678079b81a1 | -5.9835 | -40.9367 | 2026-10-07 19:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 171.2 |
| 30fe20cd-7c11-3717-bce1-f364e8ecf849 | -3.6603 | -54.512 | 2026-10-07 19:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| e726f5c7-3b2a-366d-879c-42503f4028db | -12.1922 | -44.7953 | 2026-10-07 19:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| cc349380-fcb7-3789-ac4f-51344bb8408e | -4.067 | -54.0378 | 2026-10-07 19:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| aa093f0c-08d8-3e18-b99c-fbc85a4c1767 | 1.7488 | -55.5663 | 2026-10-07 19:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 7b3194b1-d3dd-367c-9956-ab9616556d76 | -3.2554 | -54.6631 | 2026-10-07 19:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 16e3d787-2448-38dc-9a11-a6b653915ce7 | -8.2181 | -46.362 | 2026-10-07 19:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 99afc107-f561-301b-98a8-69fe5fe20b06 | -8.5365 | -67.0876 | 2026-10-07 19:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 93.9 |
| bf376c68-f4fc-3a85-a2af-f731a8f1ddd7 | -3.1102 | -54.146 | 2026-10-07 19:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 152.5 |
| 4b14e483-ef69-3769-8e6d-05fd5091c996 | -7.3935 | -46.2144 | 2026-10-07 19:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 126.0 |
| acf8a715-d20c-3308-8abe-065c36e60e8b | -4.2744 | -46.3846 | 2026-10-07 19:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 80.3 |
| b5268efe-e41c-33a3-95e5-87d8df09b5da | -6.6224 | -53.0105 | 2026-10-07 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 190cf333-ce9f-3d92-9cc0-f0e1c1475c0e | -11.6181 | -43.6669 | 2026-10-07 19:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| a63a6179-e5e5-3be9-b650-12b4f45d20a0 | -5.9838 | -40.9123 | 2026-10-07 19:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 98.4 |
| cdb9e1f9-1f0c-382f-9f7e-77f1ab22378d | -9.8821 | -44.8402 | 2026-10-07 19:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 5761f323-8da3-3e00-85c2-5e81e72259d6 | -7.1825 | -52.6283 | 2026-10-07 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 123.0 |
| ec526609-f238-3437-bd51-73f4d7a6ad59 | -9.4819 | -66.7836 | 2026-10-07 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 78dcd221-e366-3388-9d9f-98f530629ad5 | -6.8292 | -39.5472 | 2026-10-07 19:40:00 | GOES-19 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 88.2 |


[Clique aqui para ver as próximas entradas](README263.md)
