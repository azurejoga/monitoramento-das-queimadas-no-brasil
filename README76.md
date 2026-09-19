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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b81f088d-5e92-33a1-8e07-5ac0c479a942 | -3.76894 | -52.20328 | 2026-09-19 04:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0956c962-b3ca-348b-a7b3-75b5a5442d1b | -5.89143 | -49.78496 | 2026-09-19 04:57:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5bac510-6aeb-385b-b9d1-d2e54afc14a4 | -8.77854 | -48.69678 | 2026-09-19 04:57:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 060e5160-8701-31fd-bde9-e015178c5f87 | -6.58396 | -44.15828 | 2026-09-19 04:57:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95f80840-98bb-3d8d-93a7-1178925ec602 | -10.52284 | -46.71785 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31657fe2-5589-3295-b4a0-bf82dbebb959 | -3.72719 | -54.64497 | 2026-09-19 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cd41adb-3dc7-3a94-9e13-9e22ed1d5c30 | -5.85924 | -51.93686 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bf253a1f-df4b-3c72-a524-2e1893e619fb | -6.58485 | -44.15207 | 2026-09-19 04:57:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 963a83e3-5fcd-34ce-99c6-751d9d9f3d2d | -8.45571 | -45.71255 | 2026-09-19 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 99ae7fca-2a3c-33ec-9162-2dcb54e1836a | -10.18184 | -48.51835 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ed1a734-a9b4-3df9-88cc-e4df82ca2ff8 | -9.91099 | -46.58144 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cf89335b-33ce-35c9-ba52-46b6541ff524 | -6.36898 | -58.3095 | 2026-09-19 04:57:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2ede12c-61e2-3dce-8e89-f334dd0ab06f | -7.15492 | -47.5164 | 2026-09-19 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 580db9e4-6e14-3281-988d-8ddefe9c1d4f | -9.35896 | -48.29266 | 2026-09-19 04:57:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a4b1080-43e5-3a78-b7ba-0121c1d2c983 | -8.11604 | -54.81325 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c08b0bcc-ae91-3386-923a-3a4bbe180bdd | -10.53397 | -46.73905 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| a4fc85b8-cbbe-3c95-92c2-04b992055e34 | -3.37612 | -52.79508 | 2026-09-19 04:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ead887c4-38f4-314d-a590-99435ca30ae0 | -6.6974 | -59.95507 | 2026-09-19 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07f2204b-4f01-3419-85e3-304b04362f85 | -3.37443 | -50.44285 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4106038d-ccc9-32a4-b342-6416dac82adf | -3.6426 | -58.62146 | 2026-09-19 04:57:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 424965e1-ba53-39c9-a822-425638670556 | -3.72832 | -49.04427 | 2026-09-19 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 376113a8-8852-310d-8a02-7ace3252f779 | -8.23719 | -45.60261 | 2026-09-19 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e1b7d9ef-23a6-3be8-a64e-fe71ccf20521 | -9.55416 | -46.59323 | 2026-09-19 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a61d714-8aa2-3440-9694-c222fa438510 | -9.67777 | -48.32894 | 2026-09-19 04:57:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 29c00636-5969-3409-b464-650cda12cf62 | -11.0757 | -48.30651 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 072d17e1-5f9d-3230-b65f-8344d77a664c | -10.80134 | -48.11664 | 2026-09-19 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 260661f0-346d-3ffe-bb42-781638ac43a7 | -10.83633 | -50.91294 | 2026-09-19 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d51bc3b9-906d-3b0e-a4c4-c01f50116130 | -5.91306 | -46.33015 | 2026-09-19 04:57:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2da5828b-551e-3c7d-b09d-9f92b1b34dba | -9.15511 | -59.45516 | 2026-09-19 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5589895b-379b-38e3-89e1-b933e70fd29e | -7.29241 | -44.52706 | 2026-09-19 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3bac13db-2ac1-36fe-8840-53ff324821e9 | -6.44532 | -59.99528 | 2026-09-19 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 01caaca5-8712-36d8-8e3f-351270edf243 | -8.38268 | -47.20293 | 2026-09-19 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89adb943-cf77-3fb1-a428-bb4a6cefef92 | -9.89124 | -46.55449 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 14dfbf0b-2ef4-380e-b142-2ac0e0693f49 | -3.37157 | -50.46105 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aba71a5a-eadb-3170-a233-074249689df7 | -4.49149 | -55.4929 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88f83de1-de59-331a-a887-713795db7e71 | -3.0371 | -51.37364 | 2026-09-19 04:57:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ba5f26c1-c065-36f6-9899-c18a3c37acc3 | -7.77439 | -44.87151 | 2026-09-19 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 152b90d5-bca0-3dc6-bd0c-b71d5e2ef8ab | -9.69978 | -54.82757 | 2026-09-19 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61cb67e6-1c1c-3a3e-af86-97edc2c38963 | -10.32096 | -45.30966 | 2026-09-19 04:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4179c2a6-4303-38fd-acdc-81c48669f099 | -8.73388 | -52.35752 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe78d00c-4ee9-3314-bed3-72d9c0789e1a | -4.48721 | -55.49643 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9727bacc-9a03-330d-a4de-fe1634a534a1 | -4.18496 | -49.40615 | 2026-09-19 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 695c7485-b9e1-3d0d-b6d2-139f8971dcf4 | -9.24453 | -45.93714 | 2026-09-19 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fe041824-78cb-360e-b547-eadf563d1e03 | -4.56996 | -54.92097 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44fa818c-9811-3b12-b5e5-34bb9e0048c7 | -3.37271 | -50.45379 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b1194ee-7099-3b6e-9d56-dd25a44d7820 | -6.0981 | -57.62926 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 703ecb89-80cb-3801-9c4c-91d0c429e079 | -11.06311 | -48.2754 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de244e47-5b4b-33f6-a9ba-49254eea01fa | -5.1875 | -49.33278 | 2026-09-19 04:57:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f010b3b2-8d3e-375d-8abc-a1f4c1c263ac | -6.97573 | -42.1812 | 2026-09-19 04:57:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1507a35f-15bf-3a5a-a90c-f72c66247b19 | -8.37601 | -47.2188 | 2026-09-19 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0709b926-05fd-30dc-89d5-672633926f85 | -4.06159 | -56.24912 | 2026-09-19 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7c06a79e-bba6-341d-986a-853801b28d09 | -6.447 | -59.9856 | 2026-09-19 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0ba322cb-94ff-306b-97f1-7ddf0f2a6c03 | -8.08846 | -50.96648 | 2026-09-19 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9470230d-db4b-323c-9d55-285ea490705d | -10.91762 | -48.42099 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc27908a-df15-3710-8b4b-390ae326b7cc | -9.95679 | -46.55214 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8a689165-a5e6-3572-a5c5-f200d22e0b8f | -11.32494 | -47.35806 | 2026-09-19 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d77a1008-65fc-3ed9-907b-0e7d4b89f227 | -9.72661 | -47.12543 | 2026-09-19 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88472328-b176-3c06-abeb-8e9d8d870541 | -7.02348 | -44.65568 | 2026-09-19 04:57:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 96400ef8-c588-388a-a7de-9b5cce7baa3e | -8.78143 | -48.67664 | 2026-09-19 04:57:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0366922b-b480-31e1-9abe-a7c8dad0b958 | -8.89582 | -62.44651 | 2026-09-19 04:57:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 635dd9d6-35ff-3f4b-b628-beb7386443ba | -8.77333 | -44.22997 | 2026-09-19 04:57:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84f57185-c67a-34df-bf19-ccdd627e1dd9 | -3.67196 | -53.74991 | 2026-09-19 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79a20dae-c8a9-32eb-8c75-a538d0d3ecc4 | -5.25342 | -50.9742 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0cd9dc20-03f4-395e-90e5-4bf2f5095664 | -4.35968 | -55.43056 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b15bf2b6-3453-3ce1-9367-367eee710a39 | -3.51934 | -50.79313 | 2026-09-19 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4e1c9780-d298-3536-8874-a313f562091e | -6.24382 | -57.80826 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 817b7881-c6f1-325c-9c29-333e6f068712 | -5.74653 | -57.58728 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a699377f-6625-3476-b356-85dcfe2812bc | -5.83776 | -52.03001 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6dcc6e2a-9216-3569-9467-cba7bc7ca4a4 | -7.60561 | -45.43635 | 2026-09-19 04:57:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 20e7c75e-ea77-3680-8be8-db8ebd41cf83 | -9.94945 | -46.53674 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b17c2ed6-95a1-307a-a6a4-923a2565f8eb | -8.50323 | -57.63073 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6472e2ce-f385-31f4-896f-e479aae97de0 | -10.8021 | -50.90443 | 2026-09-19 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35a88b27-4690-3772-86fe-c85ae89a91bb | -11.32647 | -47.68077 | 2026-09-19 04:57:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 949ea53a-9cb6-33b3-bddb-f46b8bbf4974 | -8.42748 | -54.73232 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 963a5b1d-534b-3e2d-8e30-69201d20d2d0 | -4.28146 | -48.5888 | 2026-09-19 04:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb75e018-3131-368f-95e6-b2b2cd7e0081 | -5.89018 | -49.79301 | 2026-09-19 04:57:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 08c09b37-9fb4-3b35-a817-37013e9db320 | -9.97453 | -50.27216 | 2026-09-19 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69f67048-6542-3eb9-94a4-fc58bae8a704 | -6.36836 | -58.31328 | 2026-09-19 04:57:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| be2e74d7-e739-37e3-af40-933083a94328 | -4.80594 | -56.08917 | 2026-09-19 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c7a7ea6-b842-3247-8577-2119a291eb41 | -9.80268 | -48.32351 | 2026-09-19 04:57:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c1f1fa24-bcbe-3f1e-8042-39c00e06bc12 | -4.5471 | -54.92888 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92d86836-a9dd-352a-a04a-2650870e5968 | -7.76269 | -46.73419 | 2026-09-19 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2d06c3e5-e912-3aca-ac17-d5b641d3c868 | -3.72471 | -49.04372 | 2026-09-19 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a97acbe8-1836-34ef-85d2-7499b370789f | -11.04511 | -48.31245 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f4ccb97d-489d-3da2-89a3-033615264e6a | -5.89045 | -49.78363 | 2026-09-19 04:57:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c6a8416-3bb6-3390-be18-7f7ea6b0a707 | -11.07914 | -48.28245 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 74ad13c1-2c3f-32ee-91a5-a00d44bbcc66 | -6.37209 | -58.29064 | 2026-09-19 04:57:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3e2de2f-f148-3c09-96c7-725baa0d02f3 | -11.12268 | -45.29824 | 2026-09-19 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 580703c4-7cb4-303d-aefe-f6a8b9b3adc4 | -9.60782 | -45.38264 | 2026-09-19 04:57:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d59417d0-78e3-391c-912f-f89a6e3926e6 | -8.49557 | -57.62925 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 30ef2e39-94be-341e-8fe7-8938ffbf2d05 | -7.14725 | -47.42321 | 2026-09-19 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 84bf1d9b-912e-314a-a7af-8e1e1186f650 | -10.53267 | -46.7484 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| b5776a15-afc6-35fd-9931-446ee633dea7 | -5.85769 | -52.03312 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 04b5b11a-932a-3ff0-bd41-a13f10fe5aca | -7.83564 | -55.41176 | 2026-09-19 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc39e3c9-a23d-344d-a81c-087e1cc0daae | -3.73355 | -54.64991 | 2026-09-19 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ce0dce6c-08c9-3b76-a576-58a4f6102624 | -4.50481 | -54.96276 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b1fc5b3e-a962-3b56-871b-debbcfa14bfc | -7.57655 | -57.68662 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fe107120-8fc6-3a94-b53e-3b94af9309f6 | -9.88266 | -46.54854 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 039f132d-f9de-332a-bae7-f71e0bb29264 | -5.89402 | -49.78421 | 2026-09-19 04:57:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ed298202-e987-39a4-b611-04e46d1b09ad | -9.91685 | -46.57314 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README77.md)
