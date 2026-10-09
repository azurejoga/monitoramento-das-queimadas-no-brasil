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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5dc4826e-963e-3280-bef0-0b0e6e7492b3 | -7.11606 | -42.54365 | 2026-10-09 04:25:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| dbac8f36-f8f1-3536-a8e1-3d80b54e7b60 | -3.03918 | -54.27406 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c31b40b-22c3-3b73-8dcb-471311f01145 | -3.09429 | -53.93935 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 456d2a67-8c3c-361a-aa2c-c18ae435f83f | -2.34119 | -48.86742 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8405abac-1d18-3426-90b8-74b7c17f1d6c | -6.51393 | -47.38639 | 2026-10-09 04:25:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0e6280ae-e49e-3ee2-8966-f6881aff9402 | -6.85103 | -41.76067 | 2026-10-09 04:25:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c5da0ef8-8468-3529-a3c1-16aee198fcfc | -3.08595 | -53.95882 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f440da57-ce9f-3a85-8649-829ef43878ae | 1.69225 | -55.60639 | 2026-10-09 04:25:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d39519fc-934a-3602-b5a6-f21c261c6157 | -5.66398 | -46.23065 | 2026-10-09 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c52356c4-40a2-3b16-812d-69034ccec5a3 | -4.97927 | -46.04193 | 2026-10-09 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ea706ce-389d-3172-9488-6acd3df0e2f6 | -3.0005 | -53.91574 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 73ae5334-7135-344c-8eff-ce6ae5d0873a | -2.48184 | -56.08982 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e7878054-77e6-32e9-b0b6-fe7b8832cbab | -6.4996 | -44.36705 | 2026-10-09 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5323e40d-91f6-3eb2-ae95-f641c8d52a96 | -2.93759 | -53.92361 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf34a690-be42-3b5f-a8b2-52f61391b7a5 | -3.77557 | -58.58793 | 2026-10-09 04:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 33c74256-e254-3d91-b896-3b467a906088 | -3.17163 | -50.59801 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22fe6a96-b6c9-3030-a25b-93d5298e9c56 | -3.11397 | -54.16026 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f5b8c025-274a-3b45-a93c-28caa7ea1128 | -3.17103 | -50.45575 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6456b2cc-76ba-372b-a76d-9e831e90cb01 | -6.81937 | -39.54554 | 2026-10-09 04:25:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6c957491-7935-367d-8895-94a05a1ee74d | -6.22028 | -44.15246 | 2026-10-09 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f87cd21d-8d71-364f-b189-cf9450cc4219 | -4.66446 | -55.94929 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f5a6960d-de0c-3316-b250-44a9a86c7780 | -3.30827 | -54.7028 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 624ae181-7265-3546-ba95-75e397051678 | -3.60119 | -54.56657 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 547cba16-d295-3db3-807f-084429607a4b | -4.91895 | -55.85695 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 839aca01-ee88-3dcc-b387-c5d9e890cf8a | -3.54691 | -55.52127 | 2026-10-09 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7d1e88b-5fd2-359e-bf8c-0fe107e5d05d | -3.08453 | -53.96741 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd66b31e-bff8-33e5-aef3-845d83c8f42d | -3.25624 | -54.01846 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b05945de-9e6a-3b4b-b7ad-f49d4c777d68 | -3.08273 | -54.2645 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c4a87ea9-c200-3708-bf32-2a74e79f018f | -3.08049 | -53.96079 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3282238-8bcf-3fe4-9f09-81bce5f2e6bd | -3.18522 | -50.5896 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ec6b3a36-b068-36b3-accf-6cb3995dc731 | -6.33144 | -43.83222 | 2026-10-09 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f046ad6f-e835-3861-bea4-65752ddef1b7 | -2.73996 | -54.12449 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a3ac80a-ee70-3bbc-8453-5928fd72e856 | -3.11475 | -53.78408 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4e7303d8-6304-3651-af3c-d46f9fe9de9d | -3.50109 | -54.61511 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a3b2a40-cee2-3ed2-a269-8aa3be1e4ee8 | -3.45419 | -45.26016 | 2026-10-09 04:25:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12070274-763d-31e3-a661-2c0ac8d0e7f4 | -3.16765 | -50.5974 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d030b63-7d59-375d-be98-8910ab799129 | -1.54661 | -54.56144 | 2026-10-09 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9cbcc665-7876-3ac2-862b-fb150b0ca7cb | -3.01519 | -54.04288 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce220089-cf30-3e53-924f-69360184e505 | -3.22019 | -53.89361 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4a9f0f6-3019-341e-bddb-c5ade8c5ddc3 | -4.9329 | -45.72767 | 2026-10-09 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eda499be-d596-356c-881c-26239131b0fe | -3.10095 | -53.96133 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74d3fc80-d713-3ff1-8582-c163898bb4a0 | -6.90098 | -45.89024 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 78166db8-2d06-3edb-a64b-6a1ed87bc7d5 | -2.98035 | -54.07063 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e66225d7-cbef-3bb1-a111-d8b5a184b9a1 | -3.00179 | -54.76412 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cbef41bd-8182-3efd-97e9-ae6af935c03d | -5.3947 | -45.90626 | 2026-10-09 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e856966d-aa8a-3754-a693-2f49f5ebcf3b | -3.27745 | -50.39251 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b28f0536-cc4e-36bb-b642-5e2cd8c8b14c | -2.74143 | -54.11549 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f00cf4d-442a-34ce-94d7-3dd2f579c84a | -4.4632 | -55.40364 | 2026-10-09 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bcee5b99-8b37-32d0-8170-29f0b60941c5 | -3.26956 | -54.0621 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30d7d71d-32fb-3ef7-b561-cb936ff5bac7 | -5.09068 | -46.22105 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| adf05857-af74-3bd1-934e-b9aa3b8203dd | -3.52274 | -50.34762 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 786818f5-a65b-317f-969f-48a7eb494cb7 | -2.7516 | -54.11716 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e82a3d08-76a1-3ab7-a0a5-c1a841c693e8 | -5.07082 | -46.19686 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ab779a8-7f84-3e11-92c9-e84e27ae41b5 | -3.04392 | -54.15042 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 88ac3ac9-d527-377a-b02b-641c2c928d72 | -5.96013 | -46.38317 | 2026-10-09 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4d2f3977-7083-333d-832a-64aa08d49030 | -1.77674 | -55.02219 | 2026-10-09 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| eb020df3-47e9-33bb-b625-3ef17a21fafc | -3.72897 | -53.70191 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| c84f183c-860f-38e0-b68d-fc628b46d051 | -2.48174 | -46.01799 | 2026-10-09 04:25:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d46cf26-f621-3f94-8108-1ad007c47e24 | -3.41766 | -43.00498 | 2026-10-09 04:25:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b97e9264-6428-3fdd-b3eb-7acb4afd10c1 | -5.24294 | -48.39383 | 2026-10-09 04:25:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a780693-9df1-39f4-8110-e16576e2f66f | -3.26907 | -54.06504 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12edf7cd-1098-3454-ac53-f491aa4bd595 | -4.12667 | -55.03633 | 2026-10-09 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cca1cb1a-bf15-3b43-8750-ef26c8e0c2c3 | -3.10833 | -53.94759 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 062b892d-8c23-359a-8b91-507d2f48d984 | -3.98594 | -59.35166 | 2026-10-09 04:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0069d461-f026-3941-84a2-691601f14d54 | -5.43901 | -45.68687 | 2026-10-09 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87d0e889-f082-3e10-8777-878da3b360a4 | -4.5159 | -44.03405 | 2026-10-09 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 54e5e9b4-7d33-3f0d-ad47-059a9f255255 | -6.00211 | -40.95646 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 76d66213-ebff-3686-a49b-4137a23741f8 | -3.28847 | -54.04131 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9254465a-9aa1-3101-b34a-38a3fd906dcf | -3.10596 | -53.96211 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f05445e-f798-3914-b6b3-9892d4e83484 | -2.9974 | -53.90336 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c5285603-ec17-357c-a174-1223442c76e6 | -3.11202 | -54.17177 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fc2ff761-8afe-3a3c-9463-dc229dbb142e | -3.79115 | -50.79801 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0199d6f4-82c1-38eb-a7e3-53c56482b1b6 | -4.61135 | -42.39779 | 2026-10-09 04:25:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 034706aa-53b0-3407-ae17-e6957c7ab99b | -3.02272 | -54.18378 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4c9b2052-1a76-336c-8799-803a1750f5f5 | -3.11252 | -54.16884 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 538a238a-aa6d-3f0e-89d4-a655880537aa | -2.73339 | -54.13266 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee91a15b-d268-3ad4-8b22-136749239ec5 | -3.53071 | -54.66197 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cb708e86-a4a8-3e7d-9586-4a25e3d71bdd | -4.74509 | -55.67973 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 633821a0-87d6-35cf-93d4-bf49e7673001 | -3.89729 | -59.44584 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 17515a0e-e866-3951-b565-bdd70c6a8fc1 | -4.03976 | -54.22728 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 995e9ca4-8f33-3b7c-ab9b-9e98361456c2 | -3.21564 | -53.89018 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bffd2a3a-24fd-367c-9f0c-bc5740ac820b | -2.90209 | -57.21714 | 2026-10-09 04:25:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1bf3b0fb-7316-3821-bc36-5411f6b72b30 | -5.41818 | -45.86402 | 2026-10-09 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b51d8192-5c1e-3809-8fbf-17eea9d6e450 | -3.0147 | -54.04581 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86da2912-241b-395c-95bb-11336f0ccd80 | 0.53179 | -50.89695 | 2026-10-09 04:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 19.8 |
| e02e4446-5579-300c-a3a7-dbb10896b11e | -2.09284 | -50.40961 | 2026-10-09 04:25:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0424b7d8-ab5a-3ca5-84ae-19d84b0d0e16 | -5.80886 | -50.17113 | 2026-10-09 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3b57372-5388-3399-ae49-5d904a901bfb | -6.24952 | -45.33015 | 2026-10-09 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5ddf91a-cea6-3703-abdd-7a493fe71618 | -4.7319 | -55.65833 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65b2505a-b3f8-305d-a959-55fa536d9b75 | -5.9942 | -40.98184 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| cd6d0f2b-ee67-3f3b-a153-62b561102793 | -4.74091 | -55.67132 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 657905e6-974a-309b-8969-15cd93d2cc85 | -2.90071 | -54.02354 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 181586ff-f2fb-3886-ae1d-48da56f47da7 | -4.29537 | -54.8064 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0686435e-23c1-3e25-82a4-29c88ae6689d | -3.16989 | -50.58368 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2da0c7a2-9bcf-3184-a759-cd934dc9a540 | -5.35178 | -44.84661 | 2026-10-09 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7a68338-6f56-350b-80bb-81108bc8871f | -5.339 | -50.98697 | 2026-10-09 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c22b09f-71e6-3d17-a2fe-427299bd1b73 | -3.57412 | -54.69478 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| b7e8fbe1-bb04-34ba-abb5-d77113b10753 | -3.09142 | -53.95681 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab87a385-ba2b-3935-9771-d0162c55e640 | -6.89767 | -45.88972 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9d37f3fc-b759-3846-8186-85fb6283ed15 | -2.39641 | -51.30223 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README80.md)
