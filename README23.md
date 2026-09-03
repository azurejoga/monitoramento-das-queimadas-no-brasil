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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e0e1926-4222-32d0-981e-e5534c42ae26 | -6.6542 | -59.426 | 2026-09-03 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 1e05bdb4-2fd8-3fd6-830b-a51de95db5a8 | -6.6541 | -59.4452 | 2026-09-03 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| d3b05022-81cf-3b3d-ab48-d9343d62d6ea | -3.2485 | -47.2657 | 2026-09-03 04:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| cc171a63-bbd5-3d92-8dc2-1afba5c8219c | -6.6357 | -59.4459 | 2026-09-03 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 26ae96d8-b1e4-3555-9bfe-018f7d1172f8 | -8.0924 | -50.9642 | 2026-09-03 04:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| e72310f3-a9b2-3628-af67-0eeef5239615 | -6.6883 | -59.9436 | 2026-09-03 04:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 102.8 |
| a49e86b7-f7a6-30f1-828a-0a5e5eb33c7f | -8.4677 | -54.6429 | 2026-09-03 04:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| d6e07492-57e8-33a8-ae5b-43fe03e3f8a1 | -7.566 | -61.343 | 2026-09-03 04:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 56461f1a-de8d-39ac-92b1-e523aaf69607 | -6.3237 | -56.0434 | 2026-09-03 04:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 77bddc46-f5b3-3df1-b38a-6b263c51f40b | -6.6698 | -59.9443 | 2026-09-03 04:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 909cb348-be17-3a90-9e96-9ed177046b3e | -8.5916 | -67.1788 | 2026-09-03 04:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 2d9f86ea-d45f-325f-b17c-03df4c31e216 | -1.80189 | -47.95124 | 2026-09-03 04:36:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3e852bda-0dc2-3f70-b26d-c81733cb3e83 | -1.7151 | -47.08808 | 2026-09-03 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73cc0330-76e5-38ff-9670-776bc734cb94 | -1.79835 | -47.95067 | 2026-09-03 04:36:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 127bd5e1-60df-3025-91f9-debd7fa0846a | -1.59424 | -47.35882 | 2026-09-03 04:36:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| df711ad0-589e-3b47-b336-44181ed55f70 | -1.09576 | -48.05874 | 2026-09-03 04:36:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2cb3287-cb0a-3ebb-b78e-9c080b0a1d85 | -1.83025 | -44.889 | 2026-09-03 04:36:00 | NPP-375D | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab6508c3-4c57-305f-8353-a0d9e16c6a63 | -5.41311 | -44.80243 | 2026-09-03 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f1f5355-9619-365b-aa17-bbc010a4f105 | -3.33872 | -42.79768 | 2026-09-03 04:38:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4af77112-d477-3d1d-9e45-e47d9297bfba | -6.50137 | -53.61142 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e622878c-5f4f-3a37-93b7-502d8f11a469 | -4.08872 | -51.0423 | 2026-09-03 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 525f9e05-24c8-391e-82e3-6cd3b179a4c4 | -6.14557 | -55.66431 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 702ee950-846f-3bf7-b25c-fa6bd75d03dd | -6.76634 | -56.33471 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e88117c6-5693-3fa2-b6d9-776ecc3d1fb2 | -8.43916 | -54.69275 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 501e63fe-e5ac-3112-a597-7154b1447e21 | -7.26066 | -43.78436 | 2026-09-03 04:38:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5329cd3a-f222-3c9b-b96a-6d06887757bc | -5.94712 | -52.15396 | 2026-09-03 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 35800b73-a716-3f77-b416-84e2915ef54b | -7.05752 | -59.22057 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a6d6a79-c2d3-3054-a316-9ddc13094743 | -6.76152 | -59.43991 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1aa52682-4a71-34d1-a94e-db239796a51d | -7.08667 | -56.51743 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 85fa175d-7be2-3eec-bc1a-5aa618e1039d | -4.17689 | -42.44038 | 2026-09-03 04:38:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ab0528d0-4a7a-3cce-9418-a653b9a99754 | -6.07924 | -49.79877 | 2026-09-03 04:38:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eac62b3e-7b31-3dc0-a29c-d7ed4c832976 | -7.4098 | -49.73996 | 2026-09-03 04:38:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ee3bce9-815a-375a-bd76-2fbfb9848676 | -9.60962 | -40.34686 | 2026-09-03 04:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 927d0778-fc03-32bd-8789-66b122a50a1b | -8.43232 | -54.7029 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 671d41f2-2a7b-3c29-8532-3b1a9b902577 | -2.47775 | -49.40878 | 2026-09-03 04:38:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6658da6-eb39-353e-bfb9-755988d8014c | -4.9782 | -55.85423 | 2026-09-03 04:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e40b483-8090-3d20-9f60-1e4a4e20a6c9 | -8.45649 | -54.65165 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 65e31c0d-b015-3321-af3e-00e92e7ef29b | -6.43649 | -48.53416 | 2026-09-03 04:38:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a6085d92-bf3e-3e58-97b1-a7ec2bc89897 | -6.94394 | -45.19906 | 2026-09-03 04:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c837b17-3b87-33cf-bc1b-d306648dcf11 | -6.63896 | -59.44178 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 247b499e-75f3-3857-87c7-47196ef9e7ff | -6.61966 | -55.24397 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 192de85d-18d0-3dda-ad88-8bb98bc33088 | -5.44675 | -46.58281 | 2026-09-03 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1478d271-e9f6-3010-bc29-b3ac2aa8da4b | -8.42745 | -54.70196 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 317175e3-8451-38f0-aaa0-21ee265c4574 | -3.18333 | -48.01965 | 2026-09-03 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e37e0f53-18ac-3055-9c30-0cbc0be51e02 | -7.08101 | -56.51655 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa89c17b-b071-3296-ae8a-799a33089807 | -3.24286 | -47.25385 | 2026-09-03 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 2cfc9d0a-bc5c-3724-9efd-c56088e5e60c | -9.42304 | -45.60344 | 2026-09-03 04:38:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7903a072-3b5b-35b7-9b2b-131060181c67 | -4.63292 | -55.7324 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01a1a2d8-74e8-3936-af72-ab32a798175e | -7.34619 | -55.2088 | 2026-09-03 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0671f8e-7ba5-3711-a0a3-b93ef1bb2316 | -3.44648 | -56.32303 | 2026-09-03 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 323c57aa-caf0-3406-9822-46d18a499f4d | -4.08813 | -51.04589 | 2026-09-03 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1964cce-7536-39a0-a0c7-ab0f0d9fd8e4 | -3.33684 | -42.80978 | 2026-09-03 04:38:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02802f6b-caf5-3244-9a70-dae9bf6bc14a | -5.94284 | -52.15322 | 2026-09-03 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc5fd22c-617f-34e6-869d-3e6433a28f1b | -4.63229 | -55.73612 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ba5bba6-d54a-389d-9172-7d5bdb895ca9 | -6.76461 | -56.33296 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b32befed-a2b8-3a7d-8b92-f700e1a56517 | -3.50625 | -46.12231 | 2026-09-03 04:38:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35417952-c8c8-31f1-8e55-6a56e8bdc1d9 | -9.1619 | -47.57981 | 2026-09-03 04:38:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c914439a-6399-3ed7-a4a6-e8e48dcf9b19 | -7.83164 | -50.24009 | 2026-09-03 04:38:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6a8e9ed-1182-3fa6-880a-9d18f527bbef | -6.88081 | -56.50407 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1333114-d3c7-34de-9bdf-555feb955af1 | -6.31856 | -56.05239 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5541d4ce-7169-377f-8b9d-908407e94b11 | -9.15065 | -49.98176 | 2026-09-03 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b38d1d9-7ad9-3a37-ac62-15a053d1a0b7 | -7.08029 | -56.52049 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e448190-e87c-3bfd-87d7-8d17c0f20159 | -3.7311 | -44.65987 | 2026-09-03 04:38:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c236a19-5dfc-36ab-b519-19517dc9bc5b | -6.75852 | -44.57 | 2026-09-03 04:38:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9c6eef31-7497-39e1-aa9f-b9a00528ad21 | -1.65818 | -55.02979 | 2026-09-03 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0a9b113-a2c6-317c-9b9c-b8682b23ec37 | -9.08665 | -47.82106 | 2026-09-03 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db4310ef-5e88-336d-8aee-ffeffdb1b77f | -3.24005 | -47.24968 | 2026-09-03 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 20957621-43e2-307b-9f86-76f3b9c0ded8 | -6.32342 | -56.05714 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f652c2ba-4f92-320e-90b5-40905201a586 | -6.32408 | -56.05346 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 055f4f18-167e-3481-87b8-48ef48e8fb9e | -6.31922 | -56.0487 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d3f2e939-7091-3bed-919a-2ee0955ee49e | -3.18621 | -48.02407 | 2026-09-03 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9803036e-0718-3a78-8597-6af0d2f657f8 | -8.08454 | -50.97015 | 2026-09-03 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 06f6df10-4470-3561-a243-58ce1d0c0053 | -9.15134 | -49.97763 | 2026-09-03 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3587e95a-73ab-3928-8f69-488065b21e19 | -8.08534 | -50.96539 | 2026-09-03 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| a800fbb5-cbff-3cdd-a171-5415b93ed3eb | -6.76253 | -44.56681 | 2026-09-03 04:38:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 84858ff8-641e-3b10-8329-1671797fea3e | -7.2424 | -42.77349 | 2026-09-03 04:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| be6d3da6-bfc7-3630-a718-fbd70730ec22 | -6.31369 | -56.04767 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 300dc337-bf5f-32ca-bfa0-8625b55a17e8 | -6.63771 | -59.44857 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 422c49f0-46a5-331e-baf6-7e7db5f8924b | -6.14893 | -55.67268 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a663185b-5c77-3174-9460-a9a553429a96 | -7.32147 | -55.13305 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ef9fd2f-ff01-38a3-89c5-ad88791d11a8 | -6.49226 | -45.92276 | 2026-09-03 04:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8375558f-70ca-3e49-a3f3-ccc30cae4b53 | -4.10751 | -51.03021 | 2026-09-03 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2f032649-84ae-3ca7-b372-be7a7e355b39 | -8.09221 | -50.97148 | 2026-09-03 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54b72f64-6338-3839-af7b-31f598f24c16 | -6.30883 | -56.04295 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d2a333de-5055-3069-9e9c-e771d4601f82 | -4.14517 | -51.07311 | 2026-09-03 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a603f924-35f6-39cf-8622-5bce5d429f99 | -6.31436 | -56.04399 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c70e7ef4-50f8-39cc-9455-aee5c82199ee | -5.54557 | -46.59832 | 2026-09-03 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc3450e3-790f-3caa-a3bf-401e0b7223dc | -6.65553 | -46.13724 | 2026-09-03 04:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1b4d564-c1f9-3306-93b6-d6a162f6f1dc | -7.052 | -59.21323 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50458310-fab7-33ff-bd5c-4927db20c375 | -8.4323 | -54.73139 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56dc89ee-8c18-3db2-832c-ae0242fd69b2 | -6.63233 | -55.23312 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e87e60bd-cbea-368f-bb2a-17fe6881d7c3 | -9.61415 | -40.34751 | 2026-09-03 04:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 6be733ca-07a2-3b4c-b9c7-7d837f7868cd | -6.7591 | -44.5663 | 2026-09-03 04:38:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f86d9f97-0393-3799-8081-d4a39bb5a5aa | -6.75795 | -44.57371 | 2026-09-03 04:38:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 424570e3-e0bc-3efb-973f-287410b275e0 | -3.22052 | -48.81335 | 2026-09-03 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 463b62dc-4ecb-3024-ad0c-b9f2b6eae6cc | -7.34107 | -55.20769 | 2026-09-03 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3362dbf3-2556-3b1c-8fd4-e7c45f1fa148 | -6.62769 | -55.22887 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aea0ee97-c001-3c56-8c3d-b0c0769042ed | -7.3225 | -55.13435 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| edbe2052-3d6d-34b0-a245-5602c915a222 | -8.07686 | -50.96883 | 2026-09-03 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| db9f0331-4270-31c5-847b-c33c2b87d396 | -7.41273 | -49.74473 | 2026-09-03 04:38:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README24.md)
