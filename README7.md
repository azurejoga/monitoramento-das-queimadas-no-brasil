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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa74ee84-b8c3-3168-ba94-550294b7194a | -2.68892 | -47.35721 | 2026-08-04 04:17:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26905c02-a578-327b-a9c2-42587084655c | -1.63162 | -54.46466 | 2026-08-04 04:17:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 476775c4-97a8-3bcc-b23f-2ee507054751 | -4.64087 | -43.13237 | 2026-08-04 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 24bc601e-7cb2-336f-a337-833e95a19368 | -4.64472 | -43.12944 | 2026-08-04 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5a7a7fa-d300-3ebc-b84e-1176d1793919 | -4.31374 | -38.49307 | 2026-08-04 04:17:00 | NOAA-20 | CHOROZINHO | CEARÁ | Brasil | 2303956 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6840e949-b610-3de8-a7fc-b8cd953eb9b2 | -6.29837 | -43.82177 | 2026-08-04 04:17:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b78d5079-62b2-3335-90db-075c84b9ec38 | -5.54793 | -45.79569 | 2026-08-04 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ec0aa0c5-a411-3d67-91b7-e7aecda9993b | -6.4749 | -42.22749 | 2026-08-04 04:17:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f792cc57-9d3f-3ee8-9f1a-6325c15e4656 | -5.42334 | -43.42682 | 2026-08-04 04:17:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ab4d1cba-1830-3c7d-a310-bb4593d5e326 | -5.63024 | -45.91489 | 2026-08-04 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 17a4bdad-ed50-3ce6-9e1a-f9337f9148e6 | -4.366 | -47.76653 | 2026-08-04 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| bef3fb41-0334-3ab6-a200-d3be13c7c62a | -4.36749 | -47.76722 | 2026-08-04 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 72130204-cf37-3ee6-87dc-ebcbf0d7fe52 | -2.95737 | -50.35984 | 2026-08-04 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe15e40e-47cd-3615-9ff5-f50450650960 | -5.14567 | -46.20153 | 2026-08-04 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 98a6c246-878f-38a2-8f01-3db835a3020e | -5.63378 | -45.9155 | 2026-08-04 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7b7500e1-d3d1-36be-8b1d-77abede6d456 | -3.11621 | -47.91619 | 2026-08-04 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12ed7f9b-ac58-3fcb-83dc-d52afb0e8daf | -2.74818 | -48.7684 | 2026-08-04 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be1de14a-f124-34dd-8665-e77bf4a436df | -4.4592 | -47.9159 | 2026-08-04 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6a9b116f-822f-314a-b64b-6038cb4e3fad | -5.34503 | -41.01407 | 2026-08-04 04:17:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d255b115-8f7b-3847-9f40-bb7613d3f6ba | -3.24371 | -47.92811 | 2026-08-04 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 202f5fd7-1383-3f39-a421-0b1aed3426a8 | -3.57857 | -50.2641 | 2026-08-04 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4ef07a9-f221-3162-9329-98dbd7e3902d | -3.669 | -49.46657 | 2026-08-04 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| ef69e02a-8603-35cf-9411-67cae9dc4dd5 | -5.42624 | -47.38018 | 2026-08-04 04:17:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b4a6051-e2a8-354b-9e16-0f29cfe6e165 | -2.16575 | -47.86946 | 2026-08-04 04:17:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f08487f4-2681-33d7-abc4-9a9a0bde5eca | -2.96318 | -50.35524 | 2026-08-04 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 025cd89a-6ff7-3c6f-badf-707beaec8cd2 | -2.73162 | -48.70454 | 2026-08-04 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 30272ac0-84fd-39db-9cfd-4c25d7431ffd | -5.62604 | -45.91833 | 2026-08-04 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a4892c8-fd87-3d9e-a98f-fd965a639d4d | -2.81508 | -52.29143 | 2026-08-04 04:17:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 95bb01bd-a1dc-3476-9334-f02646f72481 | -5.60233 | -41.14032 | 2026-08-04 04:17:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f22a021a-1897-319a-8330-f01405d85835 | -3.67199 | -49.47659 | 2026-08-04 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 11ebc8a2-3465-3d26-9e6e-e10d0c3e8983 | -5.63953 | -47.10337 | 2026-08-04 04:17:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7a493f6-9612-34c1-9546-58e2f782206e | -5.04484 | -43.26356 | 2026-08-04 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 30e18a76-2cd6-362c-96f6-cb1f2c10e858 | -3.67277 | -49.47194 | 2026-08-04 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 517212b3-e5f7-38da-8a7d-e8247a431956 | -5.17547 | -37.00132 | 2026-08-04 04:17:00 | NOAA-20 | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| aae260c5-77c7-3ac8-b840-b03b3aa3d845 | -3.02707 | -48.41253 | 2026-08-04 04:17:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 381526cd-022d-3818-847f-aece187460d5 | -5.14137 | -46.20514 | 2026-08-04 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 829a7df6-feeb-3af1-93e6-0d1b0398e7fc | -1.54352 | -53.69496 | 2026-08-04 04:17:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c2451ec9-4c17-3999-a2e2-01d089078f5e | -5.34177 | -41.01474 | 2026-08-04 04:17:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b2ba5d6a-d80e-3afc-afe7-a176867e9b11 | -4.45861 | -47.91946 | 2026-08-04 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 74cfdaf1-d953-32b4-ae4f-31aa76a8b712 | -3.66255 | -49.47208 | 2026-08-04 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 489a5ae2-5e32-3430-8e31-1e505f2c4553 | -5.73232 | -43.2775 | 2026-08-04 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9788d522-e358-3e2d-8bd1-e395029aa9cc | -2.89142 | -48.01918 | 2026-08-04 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a179ce6b-515c-344e-bc24-85a4e3ad82b2 | -4.27363 | -48.60571 | 2026-08-04 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d47a17d3-ae23-3d13-bec4-e164ab897e14 | -6.2945 | -43.82471 | 2026-08-04 04:17:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 463b1570-1646-3c18-acb7-75b7bab9e0ed | -4.37986 | -43.38509 | 2026-08-04 04:17:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fbc729bc-ae5a-3d0d-85ce-0b67e688b2e1 | -6.18355 | -44.85386 | 2026-08-04 04:17:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4a4e484-7893-35ce-b8bb-b610e37d27e7 | -3.9649 | -40.0537 | 2026-08-04 04:17:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 3c47c1a9-1a6c-3790-8917-a4fcbc40e38d | -4.64418 | -43.13289 | 2026-08-04 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e755dd8-7a57-325b-a8b3-1cfc18f94b24 | -3.42246 | -43.1657 | 2026-08-04 04:17:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d2eebca-0c0e-31b8-92cf-8c11ec40d71c | -1.54127 | -53.69606 | 2026-08-04 04:17:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d0678e16-18a5-33f9-80f8-1f3b50a25ecf | -1.63727 | -54.46648 | 2026-08-04 04:17:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 69f199dd-4139-3341-a20d-b4191fc1a756 | -2.96193 | -50.34809 | 2026-08-04 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| de78c931-f198-341e-b780-cd92aed89479 | -1.63819 | -54.46104 | 2026-08-04 04:17:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7ce322cd-d905-3a0a-b8ee-3411e65ac5bb | -5.14206 | -46.2009 | 2026-08-04 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c856827c-8d0a-3c9a-b9e5-daed5b0aab8b | -3.66745 | -49.4758 | 2026-08-04 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 0e592441-1005-3ea2-8741-13e72b80dd07 | -6.20586 | -43.29293 | 2026-08-04 04:17:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a02efdd7-c5c9-36dd-bf72-ec4b4764ec17 | -4.64142 | -43.12892 | 2026-08-04 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 775b95e9-647c-3564-accc-83347a934d11 | -2.31353 | -48.58598 | 2026-08-04 04:17:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f914ea2-60e8-36d0-8f95-d2f121910847 | -4.90694 | -43.46896 | 2026-08-04 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3802de54-dedb-39ff-a8f2-56bd4fa1bee8 | -3.11328 | -47.90815 | 2026-08-04 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a4a85dbd-935b-3ef7-bc34-647729056b4c | -4.13322 | -50.26499 | 2026-08-04 04:17:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eaa89847-1086-3bb3-87e0-1180635298fd | -1.63813 | -54.46584 | 2026-08-04 04:17:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e882caeb-4b47-3b50-b8c5-743d223a752f | -6.47879 | -42.22448 | 2026-08-04 04:17:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 428659ec-878e-3b7f-88ea-2fef169b123d | -5.60633 | -41.13712 | 2026-08-04 04:17:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6b880ddf-eae9-382e-b5e1-09aa373a798e | -2.95921 | -50.349 | 2026-08-04 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c62676f-2c8a-31f0-8d4f-5f637646e593 | -4.63481 | -43.12788 | 2026-08-04 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1f55c38e-f0cd-33e0-aeb5-ed116aabe81c | -5.48459 | -45.1181 | 2026-08-04 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe108078-84cf-3103-84c1-d3e7c2c857ee | -6.5399 | -55.16528 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3b2ab8be-7ab2-396e-afed-0d866d007d02 | -11.21172 | -54.85889 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8138ed2c-3371-3a17-bf83-c12654954218 | -10.58532 | -46.77649 | 2026-08-04 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 224959be-ef83-3d5b-977e-4465e3f41374 | -6.55016 | -55.16395 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2d99ac54-deba-3321-86a5-c36f30216759 | -8.35808 | -45.98348 | 2026-08-04 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| a4b1d118-d65b-3446-a9a3-63f27c9615bf | -6.96038 | -52.82006 | 2026-08-04 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14fabe85-8731-3e55-9fe7-631711a5049c | -12.15022 | -48.44742 | 2026-08-04 04:19:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a16892b-ad97-3ea8-9420-55d43fd211a6 | -11.21742 | -54.86009 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 682e6758-c5ee-3ca1-8b34-8022780174cd | -6.57238 | -55.16592 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f681802a-d9f9-31fe-873b-a31d3ec1cd7e | -11.20982 | -54.83794 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67c682ff-247c-30f0-bb5e-4e9decda272a | -11.21477 | -54.84303 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| acfb3567-d168-3c79-8285-5e87b5073875 | -7.68681 | -45.06012 | 2026-08-04 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3120a7da-9a53-3c60-8dea-a0359acb3210 | -6.95501 | -52.81895 | 2026-08-04 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 697bef4a-d77b-3b81-a980-b90d04471a44 | -8.27891 | -47.54491 | 2026-08-04 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c0d749c-84f7-3924-8a81-6a52740efee7 | -6.56417 | -55.175 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1dff9874-41fd-31d6-bfbf-df2d67a1aa5d | -11.20676 | -54.85379 | 2026-08-04 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c5f3b47a-fc2e-3ad7-90d4-4f31ad3dd6c5 | -8.34015 | -45.98452 | 2026-08-04 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a49725fb-6572-3aa4-bba4-d8f580a0e8bd | -7.38187 | -45.05613 | 2026-08-04 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2b439d3-5b85-36c1-a314-07b40623dbb5 | -8.0001 | -47.30669 | 2026-08-04 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f281c416-d3c7-3be3-a090-f8e9d1b30228 | -8.34423 | -45.98124 | 2026-08-04 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 770a53d9-fae4-3842-83e5-f615ad15cc67 | -7.62219 | -45.30799 | 2026-08-04 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd68cd5b-3fcd-3fd8-b5ac-3e112cb8f695 | -6.56168 | -55.15333 | 2026-08-04 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c03cbd3b-dbf1-312f-b88e-84c88bfa460c | -7.71039 | -48.44197 | 2026-08-04 04:19:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 479e472c-4832-3b5d-9386-bd3c5f56ddf6 | -7.3926 | -45.05406 | 2026-08-04 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b33b322-123c-3eb2-9946-3b8e69f41fd7 | -12.45157 | -50.38525 | 2026-08-04 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6cb51f59-5e14-377f-a359-6e2ebb3620e0 | -8.35528 | -48.24312 | 2026-08-04 04:19:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c7a670c2-e68d-3986-b7e2-6943519ae91f | -10.86542 | -44.80265 | 2026-08-04 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1130468f-e752-3891-98c3-a05b6157157e | -9.1216 | -48.37593 | 2026-08-04 04:19:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3087c0f5-81a1-3c98-b071-7c4b7f38b83f | -7.0822 | -43.3371 | 2026-08-04 04:19:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a8e41187-89f4-3488-8d38-4fa35acbb206 | -11.75644 | -50.28521 | 2026-08-04 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af4cced6-a6e0-3f18-9e53-9bb03060759c | -7.5369 | -45.03571 | 2026-08-04 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29069c3b-6c4f-316c-8652-67d4bee222c3 | -8.9229 | -45.2106 | 2026-08-04 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c7ee466-f9b4-3216-8be1-8c6ef52620cb | -8.00084 | -47.30225 | 2026-08-04 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README8.md)
