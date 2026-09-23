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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf74244a-1e67-353a-8181-62e56c2859e5 | -6.6317 | -43.73 | 2026-09-23 02:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 48.7 |
| d47e31fb-8df6-300e-802f-136872115a50 | -8.8294 | -44.2735 | 2026-09-23 02:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 7e2421da-c722-3825-b218-f32f65af58c1 | -8.8108 | -44.2525 | 2026-09-23 02:20:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 0ef76301-4984-3601-b72d-9c41585c803c | -12.3867 | -50.1731 | 2026-09-23 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| bec012d2-b80d-3e07-af83-dcbd6a3ee355 | -12.1672 | -50.8004 | 2026-09-23 02:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 59a362a5-2dc9-3a45-bb83-63103576ec11 | -3.2313 | -46.9596 | 2026-09-23 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| e8e78a76-84d5-3bdb-b58d-b33df3823c24 | -12.4212 | -46.9777 | 2026-09-23 02:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 09c6cdb4-21d5-3b7c-b71a-2e0753c44366 | -3.6763 | -60.5839 | 2026-09-23 02:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| a3b061a0-8d8e-3a07-ab8b-2269be2e680d | -6.6145 | -59.9464 | 2026-09-23 02:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| d55a1b94-8840-38bc-8ba7-5274d00982f6 | -12.3484 | -50.1779 | 2026-09-23 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 3be2e70b-0722-36bf-8ee1-0ba60aa432b8 | -12.3679 | -50.1539 | 2026-09-23 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 334.3 |
| 777190b4-ddbc-365b-a5b3-521f46f63fd3 | -8.4726 | -48.6927 | 2026-09-23 02:20:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 6cd1d13d-9d1e-37c6-bcbd-eace4294aff5 | -9.1024 | -61.4491 | 2026-09-23 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| a56249d6-a360-3a59-b2e7-1c14f66454bd | -3.6946 | -60.5835 | 2026-09-23 02:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 66f238f9-19cc-3450-890a-ab979fc59fff | -3.8648 | -58.8211 | 2026-09-23 02:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| fef436c4-067d-3ec3-b063-3fdc01ff2053 | -6.633 | -59.9457 | 2026-09-23 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 99.5 |
| d5e80bbb-d8bb-330c-8d7f-4ce3e76d1b24 | -4.0925 | -62.0874 | 2026-09-23 02:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 2944b48a-3447-3fdc-bcfc-1dacaf6c582f | -1.9271 | -58.2587 | 2026-09-23 02:20:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| c3c9b503-8d94-3a4e-95b6-28f3957cfae0 | -5.7754 | -45.1053 | 2026-09-23 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| dddb64d4-3683-3312-a188-325105f366dd | -3.6764 | -60.5649 | 2026-09-23 02:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 2e5eb81f-dd3e-3089-8745-0a43abafd0b9 | -3.2129 | -46.9383 | 2026-09-23 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 1c00c229-7812-32f2-a5c4-d662b25992bf | -6.6331 | -59.9265 | 2026-09-23 02:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 150.4 |
| c9757e19-3eb4-3588-9c3c-c76c1db3d9d8 | -12.387 | -50.1515 | 2026-09-23 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| abac5795-cd13-3d56-86a0-dfa6465f9680 | -10.3131 | -50.5128 | 2026-09-23 02:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| ecd95b3c-e1c0-31fa-83e4-36d9a4c070c8 | -5.7567 | -45.1067 | 2026-09-23 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 02d064a1-4053-3416-8f06-f08bb8db4fd7 | -9.1025 | -61.4299 | 2026-09-23 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| ccd016c0-6060-3e62-a32c-2a6734d0cda3 | -12.4216 | -46.9551 | 2026-09-23 02:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 80e99477-255e-3c97-9c15-a10ca33976da | -10.6094 | -53.9902 | 2026-09-23 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| a3289296-3894-3ce1-9bc2-744cd9389f30 | -12.3676 | -50.1755 | 2026-09-23 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 177.3 |
| 78b6f43f-bfb3-39aa-9fb7-056e944d76c4 | -12.1481 | -50.8026 | 2026-09-23 02:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 05de3dea-3b9d-3423-9cd2-cfdb511b5cfe | -8.4538 | -48.6944 | 2026-09-23 02:20:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 67.9 |
| d111de9a-6a63-3b70-971a-a2c9cfb32c12 | -6.6146 | -59.9272 | 2026-09-23 02:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 185.5 |
| 9972c3db-bd98-3a53-b2fd-cefadd0915d5 | -8.8294 | -44.2735 | 2026-09-23 02:20:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 824804b3-5019-3baf-ba0b-494e9f895ccb | -8.2616 | -54.7776 | 2026-09-23 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| f655bd97-3325-3009-9387-ab668f031bf5 | -12.3488 | -50.1563 | 2026-09-23 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 228.9 |
| abf119c5-c2a4-399d-a413-0025855d12e2 | -3.2314 | -46.9376 | 2026-09-23 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 124.2 |
| b4f0882c-84e7-3cf1-b465-41c5137c5ef8 | -8.8105 | -44.2757 | 2026-09-23 02:20:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 172.0 |
| 70a25816-da17-35a4-9c1e-0a22a955a7e6 | -11.8871 | -45.7623 | 2026-09-23 02:20:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 96801b56-5ac6-349e-9f33-40997f91a62e | -6.6148 | -59.908 | 2026-09-23 02:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 83.8 |
| d2c648fb-b720-3a1f-8060-13b1bed54329 | -5.6246 | -45.2518 | 2026-09-23 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| c82e6bf0-b3ca-31de-959a-e98984033da5 | -6.1109 | -57.684 | 2026-09-23 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 21c58268-4408-377d-be86-f2794d6f36ed | -6.3293 | -43.9411 | 2026-09-23 02:20:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 35.8 |
| b0c929fe-f0ea-37b8-a783-decf94eebf5c | -12.1192 | -45.6368 | 2026-09-23 02:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 6be5587e-bce7-34e0-a4df-65b4b3b322b0 | -3.6764 | -60.5649 | 2026-09-23 02:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 96712f13-f1fb-3b18-b7eb-40664352569b | -6.6331 | -59.9265 | 2026-09-23 02:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 151.9 |
| e1e1e308-a54c-3fd1-bc3d-2037eba0643b | -12.1188 | -45.6598 | 2026-09-23 02:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 49.2 |
| e71f2a59-3ed4-38a9-a804-1df572c2031d | -12.7958 | -50.8742 | 2026-09-23 02:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 615dcd73-3de3-3ff2-9cd8-cde0eb9f1776 | -12.738 | -50.9027 | 2026-09-23 02:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| cb93373b-62ba-3641-b16e-d262d50a616c | -6.633 | -59.9457 | 2026-09-23 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 95.0 |
| c67969a7-08ad-30c8-919c-08f4967a7943 | -8.8105 | -44.2757 | 2026-09-23 02:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 4329b38a-70c4-3789-8028-5b6f1e857c06 | -12.7384 | -50.8813 | 2026-09-23 02:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| d9a28adb-e9ff-3da8-835b-4f9631086736 | -12.1385 | -45.6339 | 2026-09-23 02:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 311a8f0b-bfa6-36de-8394-b96f566e84be | -6.6127 | -43.7549 | 2026-09-23 02:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 5379caf2-511f-393f-983e-b33f6c45e7c7 | -12.7572 | -50.9004 | 2026-09-23 02:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| b565be0a-5123-3706-9f90-38934fb69176 | -8.8108 | -44.2525 | 2026-09-23 02:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 7f98ed15-0e36-32cd-b34e-57cc56bbc54f | -12.8342 | -50.8695 | 2026-09-23 02:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 145.7 |
| b2b35dcc-c892-358e-b479-efb70167372a | -8.4538 | -48.6944 | 2026-09-23 02:30:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 70.0 |
| ed10c80f-b833-3d51-82ed-6585e3ae9387 | -8.2616 | -54.7776 | 2026-09-23 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 4a3d5802-e204-3a87-b5dd-d4c14f17b858 | -11.8871 | -45.7623 | 2026-09-23 02:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 9736d199-5de6-3a45-8253-97c5b2dbada9 | -12.7952 | -50.9171 | 2026-09-23 02:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 9d9578b0-cbc1-3df0-bd77-58f20e678899 | -11.304 | -51.3646 | 2026-09-23 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 368b5e89-6fa4-35cd-bc62-34832a314a79 | -5.7567 | -45.1067 | 2026-09-23 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| da6bfff4-074e-3f77-8255-fdca4045a719 | -12.4216 | -46.9551 | 2026-09-23 02:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 69ace575-7f98-3576-a95a-2ecfa2d10e49 | -8.935 | -61.495 | 2026-09-23 02:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 0a45c409-dd24-33aa-bccb-9e97fd0a44bb | -12.815 | -50.8718 | 2026-09-23 02:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 83250d52-03b9-35c5-aac0-fb93b4f743e6 | -3.6946 | -60.5835 | 2026-09-23 02:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 90.4 |
| d81a7358-424a-3660-824d-11a4ddba8e38 | -12.4212 | -46.9777 | 2026-09-23 02:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| ac8fb19b-ba17-38f4-b28d-f412b054abac | -9.1025 | -61.4299 | 2026-09-23 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| bd4e1547-e0ce-3f96-b1ba-8b23475dd536 | -6.6148 | -59.908 | 2026-09-23 02:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 79dfd1eb-7324-307e-81f8-51522b47cdc2 | -3.6763 | -60.5839 | 2026-09-23 02:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 8fd3d4a3-5d8a-31c6-a01e-04ab58882d88 | -9.1024 | -61.4491 | 2026-09-23 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| b2f92f52-2b46-37a7-ac6d-b8e7072fdf68 | -6.6129 | -43.7317 | 2026-09-23 02:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 41.6 |
| e93424fe-e3c7-3704-893e-be5f10506855 | -6.6146 | -59.9272 | 2026-09-23 02:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 182.4 |
| 4b022c12-7f2e-3213-b228-1d129d1e0e9f | -6.6145 | -59.9464 | 2026-09-23 02:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 58ccee55-e3ac-3992-936f-45135919af7d | -11.7107 | -50.7891 | 2026-09-23 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| e9147705-a4dc-3e7f-829d-64928ff37dd2 | -12.8143 | -50.9147 | 2026-09-23 02:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| aeb162f5-e3f6-3a59-b5ad-fbb911b2297f | -3.6947 | -60.5645 | 2026-09-23 02:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| fe23a294-d6b8-3a2c-91c7-92f526e13d4b | -12.8153 | -50.8504 | 2026-09-23 02:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 05f8dbd4-eb2d-3fb6-bb84-648960df1050 | -8.4726 | -48.6927 | 2026-09-23 02:30:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 108504d9-5d01-3a90-bda7-55500630f6b7 | -5.6246 | -45.2518 | 2026-09-23 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 817053e6-5963-3c9a-b899-192f8ebf216c | -5.7754 | -45.1053 | 2026-09-23 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 474480c8-5a21-34d3-91ec-8c8fe4c21cd8 | -3.2313 | -46.9596 | 2026-09-23 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 503257cf-e67d-3b47-9f93-2f68f63237fd | -8.9351 | -61.4759 | 2026-09-23 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 91e4be9e-63b2-348b-9dc8-f062bc7ff50c | -8.9164 | -61.4958 | 2026-09-23 02:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 3fb77972-e3cd-3bfc-b1c0-590bc7b74a3d | -3.8648 | -58.8211 | 2026-09-23 02:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| cbfbb588-e964-3fdd-ab30-c2ae3582a7f2 | -8.9165 | -61.4767 | 2026-09-23 02:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 57d77549-561b-32ef-80f5-8217314359bb | -6.1109 | -57.684 | 2026-09-23 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 26d74a65-0eda-3c2e-a09c-cc9cb00d96cd | -3.2314 | -46.9376 | 2026-09-23 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 114.5 |
| e60c3b69-e6f4-3430-b249-ca32456e832b | -6.61 | -43.7 | 2026-09-23 02:30:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b4e0d1f5-55b7-3c91-8d5c-fdf1ed07e00d | -6.61 | -43.83 | 2026-09-23 02:30:00 | MSG-03 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 70dcf0c3-a018-3d23-9030-54886a14a67b | -12.09 | -50.77 | 2026-09-23 02:30:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5a2c0fbe-063e-30d9-a15c-32880c4c76bf | -12.35 | -50.2 | 2026-09-23 02:30:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4ccd5ff2-6482-3f73-a098-e11562ede470 | -6.61 | -43.74 | 2026-09-23 02:30:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4629d855-7a34-3453-8cb4-a3d3a25e6357 | -6.58 | -43.69 | 2026-09-23 02:30:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b9acf35c-3fc1-3da8-9382-ba22a6e91f38 | -12.35 | -50.14 | 2026-09-23 02:30:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b1194d1e-9d6e-388a-9a1e-fa99acc6c94e | -6.58 | -43.74 | 2026-09-23 02:30:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2fdb0943-5d6c-30f9-bd48-467b0276d4d7 | -6.58 | -43.78 | 2026-09-23 02:30:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cb2f0cb4-85dc-3b25-8bc7-a58e21ecc1c9 | -6.61 | -43.79 | 2026-09-23 02:30:00 | MSG-03 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e973099b-e083-36b2-91d1-845144cc4e19 | -6.633 | -59.9457 | 2026-09-23 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 808b79a8-78ef-3380-ae76-9ab2d6e36ec9 | -3.2129 | -46.9383 | 2026-09-23 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |


[Clique aqui para ver as próximas entradas](README37.md)
