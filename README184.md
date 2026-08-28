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

## Dados Diários - Página 184

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4edc3d0e-0ac7-38e6-b0fa-c41c03d9a4d0 | -6.7652 | -63.054 | 2026-08-28 20:50:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 93.3 |
| ba5fcd67-39ff-3c4b-922c-4f6960906b61 | -14.1788 | -48.7481 | 2026-08-28 20:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 112.3 |
| c19f86bf-29d0-333f-831a-bf68e5324b2d | -7.5516 | -70.0146 | 2026-08-28 20:50:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 9ffdd5c6-4cbb-3300-ba21-96d9e216d894 | -8.5968 | -54.7957 | 2026-08-28 20:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |
| edabf442-408b-3dd1-a912-33d1b3b4bd8c | -14.4664 | -58.5091 | 2026-08-28 20:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 806debd3-8dd6-38ad-85c2-59e29ce5ec96 | -7.2993 | -49.9676 | 2026-08-28 20:50:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 806a2d8e-972e-3364-ab82-d71945a7ddb9 | -14.9193 | -56.3237 | 2026-08-28 20:50:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 0fc1fe62-3521-370c-ab6c-49b4f2c4d5ca | -8.6013 | -70.2009 | 2026-08-28 20:50:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 72.5 |
| d6eff7c2-5ba5-3f3d-83b2-b48b0da1f743 | -6.7698 | -55.6844 | 2026-08-28 20:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| ccc59be2-c2cc-353b-a127-158606392e80 | -11.2292 | -51.2879 | 2026-08-28 20:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| c17f58ff-fdad-3c9c-99b2-54fac764eb32 | -14.4057 | -50.0537 | 2026-08-28 20:50:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 951700c0-8b05-3835-b8a6-85949341f045 | -11.7167 | -54.5244 | 2026-08-28 20:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 158.4 |
| c1fe162f-50ae-32b5-b4b0-8a3db39e65e6 | -11.1916 | -51.2708 | 2026-08-28 20:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 154.2 |
| a76f0546-430f-39d1-8673-5bc347842181 | 0.1367 | -60.412 | 2026-08-28 20:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 60930431-4be5-311e-ab1d-c2c8c60f563a | -20.9207 | -57.5723 | 2026-08-28 20:50:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 76.9 |
| ba739807-e63b-3bba-a4dc-bd6b4f5f9c6b | -7.529 | -61.3635 | 2026-08-28 20:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 119.3 |
| abff7761-a034-3ab4-982f-f8a167a5ab01 | -7.5516 | -69.9963 | 2026-08-28 20:50:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 0f7cf004-8580-309a-a71b-648003581e29 | -11.1726 | -51.2728 | 2026-08-28 20:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 1e533c27-3527-3b3d-83f2-fb8e4b7025f8 | -7.5478 | -61.3056 | 2026-08-28 20:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 198.0 |
| 46b5ee6a-71b8-30ab-9ab2-51cd2d0e032d | -7.5477 | -61.3247 | 2026-08-28 20:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 23e16f51-6e76-3fc6-b1e0-9305037db7cb | -8.5971 | -54.7553 | 2026-08-28 20:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 61754514-9dd1-3b43-b599-bef3a6e84f51 | -12.3799 | -50.6038 | 2026-08-28 20:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 914b1337-975a-381d-b054-02aca71a7702 | 0.1549 | -60.412 | 2026-08-28 20:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 74.1 |
| d0300c43-71b4-3bc2-a20b-534dbd05e33e | -8.5366 | -55.2625 | 2026-08-28 20:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| ad4bff9c-7c6e-31bb-9ff1-96d4f9ca6a6a | -7.2807 | -49.969 | 2026-08-28 20:50:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 1f8da41a-6c43-39bb-a110-2a1e9c581558 | -9.1238 | -61.0269 | 2026-08-28 20:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 74f22590-6efb-31e0-8df0-3bbc38299dac | -9.4329 | -51.6926 | 2026-08-28 20:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 33e78685-69ca-3055-8a12-98738baa0bf9 | -14.1597 | -53.1219 | 2026-08-28 20:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 3b4e0ba9-76b2-3ff2-a9e2-b1af70648dfe | -6.0005 | -57.6689 | 2026-08-28 20:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 9d5943e4-13de-3f70-97b5-984c17bfd534 | -14.4856 | -58.5074 | 2026-08-28 20:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 279.7 |
| c615faba-3481-35fc-909a-c8d1fa31d444 | -5.2446 | -43.7457 | 2026-08-28 20:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 220.3 |
| 993e7b8f-b783-3c72-ae63-5964e0e59fdb | -10.7596 | -54.0384 | 2026-08-28 20:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 114.9 |
| e4ed8201-f76e-3a18-94c4-f52a8da28f54 | -6.7248 | -59.9998 | 2026-08-28 20:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 7ba10ede-6deb-344e-a588-71c097e23180 | -5.8894 | -57.7708 | 2026-08-28 20:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 224.7 |
| f8d02186-9c1e-32d8-95e7-9b50ecea3d32 | -9.8739 | -60.2955 | 2026-08-28 20:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 174.5 |
| ef26db2b-e615-3a01-919e-995629fba488 | -3.6216 | -60.547 | 2026-08-28 20:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| bcab2121-8c10-3c70-abcb-64e611545a52 | -14.1982 | -48.7451 | 2026-08-28 20:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 0272a9cb-7bb6-39db-9bdd-03879dcacb54 | -3.913 | -60.9395 | 2026-08-28 20:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| cfad2251-9d98-3c77-9b81-d55cd169b79f | -6.7514 | -55.6654 | 2026-08-28 20:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 154.7 |
| a0dd0537-211c-3f78-a2aa-42af25335359 | -6.0004 | -57.6884 | 2026-08-28 20:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 18e32c99-e800-31f8-83e7-0cd5e7c6a071 | -4.5507 | -44.0668 | 2026-08-28 20:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 8901d394-a9df-372a-b103-d3ba58b506fe | -12.3803 | -50.5823 | 2026-08-28 20:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 6e37491a-2709-38f7-811c-66228fc7c8b2 | -8.5785 | -54.7566 | 2026-08-28 20:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 23aab707-ca08-387c-8e00-969c73f4fb8a | -2.7304 | -47.0424 | 2026-08-28 20:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 546267c8-6030-31f9-af13-015d48e68b9d | -5.982 | -57.6697 | 2026-08-28 20:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 86e27bb0-7246-325a-9099-862eedb0bf4a | -4.175 | -54.5761 | 2026-08-28 20:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 7524f2db-50b6-3c68-a02f-268682cabe99 | -5.4177 | -43.1986 | 2026-08-28 20:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| f8834da0-552b-345d-8803-0a15368455c3 | -14.2027 | -52.8432 | 2026-08-28 20:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 178.1 |
| dc201cf3-f57e-3494-9b50-7e7cad1052cd | -7.5663 | -61.2858 | 2026-08-28 20:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| b05dcfb0-d17e-34ab-be72-7dc6edb85ba7 | -8.0303 | -47.9926 | 2026-08-28 20:50:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 68101711-dc53-325f-a0bf-9a340778cfae | -5.8895 | -57.7513 | 2026-08-28 20:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 291.4 |
| 70bdc490-b709-363f-8988-ce0dded0bf75 | -11.7165 | -54.5449 | 2026-08-28 20:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 135.4 |
| 2c59309f-f94f-302a-91d7-f3dbd3d6df6d | -14.2031 | -52.8221 | 2026-08-28 20:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 70516483-6a51-3055-a743-b2c455e41547 | -4.5694 | -44.0657 | 2026-08-28 20:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 299.2 |
| d63b76f7-0c2f-3418-8147-4d81451304ac | -6.7513 | -55.6853 | 2026-08-28 20:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 72a5f381-6aa8-3e8b-a019-013a5207f92a | -8.8219 | -70.638 | 2026-08-28 20:50:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 68.1 |
| e8ff04e0-d8c0-379e-80a0-a53151f41c58 | -5.871 | -57.7715 | 2026-08-28 20:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 3754c63c-4c71-3b79-a5a0-a172a29cad15 | -7.5289 | -61.3825 | 2026-08-28 20:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 952d933a-d619-3833-aa23-08f87fd79b64 | -14.9389 | -56.3011 | 2026-08-28 20:50:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 121.4 |
| a075316c-2524-31a8-910d-56eefd5ef0d4 | -7.5662 | -61.3049 | 2026-08-28 20:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 282.1 |
| ae0595fd-abc2-3105-b752-9c3a43d51b64 | -7.5661 | -61.3239 | 2026-08-28 20:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 133.4 |
| d98ca014-e4a8-3d50-9b17-a61d572bb0da | -7.4919 | -61.403 | 2026-08-28 20:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| b6de7674-c853-3727-8d1d-95ad37c81bf8 | -14.9011 | -52.6267 | 2026-08-28 20:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 9cd5af7f-7579-3764-bd3a-a4ca20543bb0 | -9.1523 | -49.9853 | 2026-08-28 20:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 39973812-0d6d-3e1c-8c91-4107c5478f7b | -5.9079 | -57.7506 | 2026-08-28 20:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 131.6 |
| f8d97825-b8f1-396b-8bee-a5e87e944c01 | -9.8028 | -46.373 | 2026-08-28 20:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 166.1 |
| 448951be-5926-38a6-92e0-997ff090ce5a | -9.1239 | -61.0078 | 2026-08-28 20:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 115.8 |
| ade7a545-27a9-398d-8795-85cadb30a451 | -9.8031 | -46.3505 | 2026-08-28 20:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 56060164-adda-3af4-a883-607eb68e3b10 | -7.4953 | -55.2862 | 2026-08-28 20:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 992526df-ead4-3a0e-a22a-b084948834f2 | -5.9819 | -57.6892 | 2026-08-28 20:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 8eb8c8c4-37dc-3842-ab30-373abe996e34 | -6.77 | -55.6445 | 2026-08-28 20:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 7b236f61-2009-38d1-89f6-bf21d63a8d28 | -9.0198 | -57.5574 | 2026-08-28 20:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 37fb03d0-a77d-30f3-b940-a0749ca21695 | -4.1934 | -54.5755 | 2026-08-28 20:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 169.4 |
| dcb1aa99-9f1d-3950-a65b-9d194556301f | -8.5969 | -54.7755 | 2026-08-28 20:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 151.7 |
| a2209dd6-fcfa-394b-b829-5813fb79c474 | 0.1549 | -60.393 | 2026-08-28 20:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 109.2 |
| f73be8c0-431e-3f19-ab55-e9da7d9bf9d2 | -10.5523 | -59.6161 | 2026-08-28 20:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| e53b62b6-c636-3f8d-ab16-6a8d91702ae1 | -4.5695 | -44.0427 | 2026-08-28 20:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| e85ed7a7-88ad-36e5-a16a-d838decc7646 | -6.9336 | -58.9514 | 2026-08-28 20:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 122.4 |
| d904846e-0539-3347-afc3-eb8832a6b6e7 | -14.4859 | -58.4874 | 2026-08-28 20:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 220.8 |
| 56a60267-c02f-3fc3-8010-4fe4e54f960f | -9.1424 | -61.026 | 2026-08-28 20:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 543bc668-9496-357d-87d3-e8571f5ae832 | -6.7699 | -55.6644 | 2026-08-28 20:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 355.8 |
| 9af97734-211f-3929-b358-5584166b6bb8 | -8.6012 | -70.2192 | 2026-08-28 20:50:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 122.1 |
| 90eda625-971d-39e6-bfba-908c8765e79e | -9.9708 | -53.9419 | 2026-08-28 20:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 457e4367-881a-3895-a5cf-fc510e7f5669 | -6.3279 | -44.0797 | 2026-08-28 20:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| a954f096-bdfe-3e63-b750-55b71aefe2e0 | -2.7119 | -47.043 | 2026-08-28 20:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 7a4e2e3d-3024-3043-a3df-75ab0be7363d | -3.6033 | -60.5474 | 2026-08-28 20:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 105.7 |
| a7c8c224-05b9-386a-8bde-c1dd38e07d87 | -10.7407 | -54.0401 | 2026-08-28 20:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 87f36f3c-7ea7-377d-9f44-417de2beec58 | -6.6397 | -53.173 | 2026-08-28 20:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 728ac637-d64c-3abd-9b32-c5f9a5ffdd2e | -5.2634 | -43.7444 | 2026-08-28 20:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| fdadd6a1-000d-305f-bf99-99d8ca03254a | -6.9521 | -58.9506 | 2026-08-28 20:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.1 |
| b8349fc3-0a02-3140-a9ba-1a647870a598 | -4.1935 | -54.5555 | 2026-08-28 20:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| fe117837-d0b2-363f-9edf-acd272181231 | -14.1784 | -48.7703 | 2026-08-28 20:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 51116035-ce2c-37d3-a737-4281f5b27fa4 | -12.7797 | -44.2576 | 2026-08-28 20:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 138.8 |
| a271170a-0638-3a37-ac98-55db63c871f2 | -12.7603 | -44.2608 | 2026-08-28 20:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 147.3 |
| cb744475-2943-32aa-bc5e-8568c2f03edc | -10.4085 | -61.1915 | 2026-08-28 20:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 28891096-a060-3ab7-bcaf-a5abda203052 | -9.8737 | -60.3149 | 2026-08-28 20:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| f596c190-eb35-3e2c-b353-2211a5323b93 | -8.0115 | -47.9943 | 2026-08-28 20:50:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 6c3bce5f-6199-3f37-bfd3-db54bf0ed367 | -8.5783 | -54.7768 | 2026-08-28 20:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| a78a62e3-1a9f-3848-b7f2-f1d861f3bd54 | -6.7504 | -58.7268 | 2026-08-28 20:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| be3b8e48-ec7f-377b-ac55-5e5106f367c5 | -5.8711 | -57.752 | 2026-08-28 20:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |


[Clique aqui para ver as próximas entradas](README185.md)
