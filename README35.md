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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bcfa6171-992a-362c-bedf-7cac970477e2 | -3.10623 | -50.31306 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5e9bd292-a9b1-3a3d-8b22-443716a30bdd | -5.74882 | -45.13064 | 2026-10-10 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 67fe6479-0c53-358e-9e71-813a880042fa | -4.09541 | -53.99972 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d0f0c517-40ef-36de-806e-aaac9180a6e6 | -9.21755 | -45.66026 | 2026-10-10 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c449ae80-3691-3f33-a4c5-b896d9d1685e | -8.35599 | -48.14741 | 2026-10-10 04:08:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c72effac-ac60-33b0-b7f1-7c785ed03da1 | -5.98685 | -43.93321 | 2026-10-10 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1eb8627d-4119-3d9d-966c-5c5c7d2a17b3 | -9.83789 | -44.78056 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7872977c-4ec8-36f5-86ce-4c5448efc48f | -3.59497 | -54.60687 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| b9505b3a-580e-3e69-974a-7142e369dbfe | -3.45667 | -50.59536 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0326f304-7ca6-33ed-ac2e-926b916e7774 | -9.30978 | -47.38408 | 2026-10-10 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 872365a9-30d2-3925-8ca6-d32f3eb7ce4a | -9.26842 | -47.42397 | 2026-10-10 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96b3c233-cda7-3f92-9dd4-c0054f09bb18 | -3.87493 | -52.2571 | 2026-10-10 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5524c7be-f85f-3fda-a2da-d7199e9fa6bd | -3.00893 | -51.00781 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b303abd3-0229-3cc6-b37e-b111e1fb0a58 | -7.23558 | -44.16331 | 2026-10-10 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a4b1f8cf-79d0-3512-b855-adf751c9aaab | -2.99032 | -53.90594 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0c1a8c27-280f-3b5c-9ab5-c4d6b0949af6 | -7.18423 | -52.6206 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aedccb94-ad30-3215-87d5-a5d9dc632774 | -6.45121 | -44.45519 | 2026-10-10 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7fb2cfc7-2d97-37d2-87c5-c3daec69abe7 | -6.77267 | -48.66774 | 2026-10-10 04:08:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 74b2e060-b80a-34aa-8c07-cbc82b11003c | -3.20987 | -50.54756 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0ae74a70-f659-380c-995f-2098bed2d55b | -8.3432 | -45.01121 | 2026-10-10 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b279f9cd-6b85-3a81-a635-012f0edb5267 | -7.93887 | -49.74669 | 2026-10-10 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8302dfab-0e2d-3777-9398-ac5ff99675fa | -3.26264 | -54.18817 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 47d3b45c-5ca5-373f-9ecc-478ca4ec5e76 | -8.87152 | -50.18956 | 2026-10-10 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 98b67f2e-6ca4-3326-9830-0ad8ec2a3924 | -6.1617 | -46.14013 | 2026-10-10 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0da12320-fac7-30bd-aa3c-51931d06672e | -3.35145 | -50.48021 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8373fa20-37af-3840-8dba-a027524475a3 | -3.56722 | -54.69218 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c4cb5fff-fafd-33a1-a4a1-1a182d71d844 | -6.41834 | -46.19997 | 2026-10-10 04:08:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ac00a7f-46e4-3e04-a0dd-ea800a139a34 | -7.19279 | -52.64001 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b89e11dd-2dc0-32f8-997a-a92c2d4d9fc9 | -8.77354 | -49.60767 | 2026-10-10 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5332e309-e4d7-3d3e-b09a-ccdc78dbd43b | -4.39524 | -46.53369 | 2026-10-10 04:08:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 07ca5605-c7a8-3029-89c5-ebfe8201d7de | -5.7035 | -41.67889 | 2026-10-10 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b018c894-e617-396a-870e-716640f9ecc7 | -3.58479 | -54.71629 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c8f69b70-1a51-308f-8c3f-8e84c4b1d13b | -3.545 | -54.69522 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f2c5bb4-5b2e-3b2b-9a03-fb12f9730218 | -8.22752 | -46.38717 | 2026-10-10 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b351df37-6084-3f2b-89a8-f880c11c4a84 | -3.26924 | -50.39509 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eaa66c63-67ee-3b23-ba07-400def976bbf | -6.07717 | -44.00525 | 2026-10-10 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e3b5957-0f72-3837-9b04-d59f8f4e5607 | -2.89189 | -54.07496 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| dbf9c838-ac90-30b8-ba86-e3af02d512eb | -7.23247 | -44.1825 | 2026-10-10 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3c8c1a87-4887-304c-a5fe-f647b90b68da | -6.93782 | -44.56681 | 2026-10-10 04:08:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| be3dca68-fc02-3403-8269-018c8a83900b | -6.46542 | -44.29993 | 2026-10-10 04:08:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3ee181c-955f-3bb1-b1d2-e7d34ccc8b19 | -3.2168 | -49.45048 | 2026-10-10 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87aaed11-a18c-3953-b235-c1b33363806b | -8.45668 | -48.69802 | 2026-10-10 04:08:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73c3cb1c-4d0b-37e5-a4bf-a488bf08b099 | -9.76435 | -44.78046 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b37db094-e328-3ed7-a05a-ea0d14c519a4 | -6.44173 | -55.03281 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 939a1da3-7f72-355f-983b-ef93229abf7a | -3.12294 | -54.17625 | 2026-10-10 04:08:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 078bef06-558a-3612-9605-506bdf4c4a8a | -3.58515 | -54.70282 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cfd29302-5bdb-3b31-adaa-83f827f2cd31 | -6.64332 | -55.32917 | 2026-10-10 04:08:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b30422b-3b62-3166-a13f-56d526ab657e | -3.21953 | -50.55075 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 619b948c-6f0b-3633-8b57-0bb19b11262f | -4.22816 | -40.77433 | 2026-10-10 04:08:00 | NOAA-21 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ca4bb553-07fc-3af1-af1d-dbe4f520b42c | -7.77291 | -43.79263 | 2026-10-10 04:08:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4b2ab5b1-46db-3fb3-bd31-8daa5a41eb64 | -2.18794 | -46.82671 | 2026-10-10 04:08:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a7b66e7-8994-31b4-90ef-9bf0c144da65 | -8.25271 | -46.41842 | 2026-10-10 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 49b69f84-752d-3c79-9cbc-b44340039cb1 | -4.32505 | -41.24635 | 2026-10-10 04:08:00 | NOAA-21 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3f477bcc-f1b3-3aff-b799-210569c840d5 | -6.91922 | -43.08223 | 2026-10-10 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 948b8c67-72d3-36e6-b6e9-3c31eca644a7 | -6.45399 | -55.50035 | 2026-10-10 04:08:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc2d5034-4c54-305b-8064-9bcddb7c594e | -6.47709 | -55.0718 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| f4782a67-0416-3444-b698-6d624e40bef5 | -7.51699 | -48.02148 | 2026-10-10 04:08:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 48955304-2302-3c90-b196-6c7521dbba17 | -3.18628 | -50.58214 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 692f3c18-71c8-36ad-9a37-4864757179c7 | -3.47576 | -46.06992 | 2026-10-10 04:08:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 25d946a5-6669-3f4c-bf2f-5179ac56b1e6 | -3.48456 | -50.33153 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fca93aaf-6fbe-3492-9799-d766feef6e69 | -3.53788 | -54.73631 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| edd55d30-b951-33e3-a31f-7da25ac23443 | -3.36175 | -50.48536 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5e4463a2-5dee-3484-b54b-2b4de64a6dc7 | -4.66843 | -50.44687 | 2026-10-10 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd5cc1ed-aca0-3869-bd2c-9fcbbbcb3e52 | -1.11108 | -54.17278 | 2026-10-10 04:08:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3b763f00-1d63-3fdf-80ef-0a7af30f109a | -3.59184 | -54.71738 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f70c090a-f63a-3219-92f1-940c589a2380 | -7.71736 | -43.96527 | 2026-10-10 04:08:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c3c488d-396d-3750-b8f6-d03c01b3565d | -7.11782 | -42.53359 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| cc4a7a48-3fb5-3df1-a5c0-4cb066175300 | -1.96463 | -54.39718 | 2026-10-10 04:08:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83e365fe-8f1f-3726-8a49-a2219e01c734 | -3.20665 | -53.86128 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e507947a-abe2-3246-a5df-bb06f82c0270 | -3.21895 | -50.5543 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d6cc9ac0-7303-3e24-90de-00f4d22bcfe0 | -3.20361 | -50.81878 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9f4fd4ac-7f8f-3333-afa0-eeab812baff2 | -3.21094 | -53.86046 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fd461e33-7447-385a-a8f9-ca714de83e9a | -3.57578 | -54.71482 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8ea85f66-c967-3c29-8c88-de44a5fe0520 | -3.36234 | -50.48188 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 44e3e4c7-29d9-3351-8575-c1987538ed16 | -8.92635 | -45.42093 | 2026-10-10 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2e6b68c6-7872-3053-add6-04320da9d1c4 | -5.59613 | -47.27182 | 2026-10-10 04:08:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6c0ceec4-c179-3e96-8b73-138172b13b53 | -1.53544 | -51.60394 | 2026-10-10 04:08:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8620f126-3bf3-348e-a858-07fa9d412425 | -2.94845 | -51.41197 | 2026-10-10 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08baf196-3d29-3bdc-8826-b595faadbc9b | -5.59848 | -47.28091 | 2026-10-10 04:08:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0a11f467-558c-32e3-97e9-41cf06804ba1 | -3.00979 | -51.01949 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f38b9f7-840e-3a48-be5b-e0cc4b8f93e6 | -7.37302 | -44.05265 | 2026-10-10 04:08:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa8875c1-9752-3ea0-bf7b-560824d0d49e | -7.22838 | -40.35633 | 2026-10-10 04:08:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f1ad8025-268a-3b17-a494-e8fd2c837c71 | -3.21781 | -49.44442 | 2026-10-10 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5ac6451-f4b7-3fe7-bc42-9f9e1e6a70e2 | -5.10733 | -46.22887 | 2026-10-10 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf4e552b-f872-365f-8988-1eba4288fdf2 | -9.07701 | -45.09721 | 2026-10-10 04:08:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bd85f229-0ee5-34c7-8112-eed0185e517f | -6.13314 | -53.10464 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cb5db543-e7f0-3cdb-bd5c-2480ad8ce72c | -6.07652 | -44.66199 | 2026-10-10 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 877d040f-c664-37fd-bf7f-4f85aa63b2ac | -3.27245 | -54.05641 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 557b9f04-6311-3bd2-8fec-0f2edbaa823d | -6.90406 | -43.15652 | 2026-10-10 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 32313e41-34de-38a0-9118-2e2e0b82cdfa | -8.21139 | -46.53323 | 2026-10-10 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7edf932e-c06c-3119-85ed-1800eb518146 | -8.27638 | -46.41783 | 2026-10-10 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4faf7065-8dfc-349b-8f2f-819630cdc0d1 | -3.45788 | -50.58818 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91c76cff-3a5f-3037-b40b-ada6ebabcc1f | -9.26783 | -47.42755 | 2026-10-10 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5905269d-3288-3436-bc0b-0d0ea8cd808b | -5.70849 | -53.47368 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 408d2e84-8aa6-34a6-905e-cb29f1307ab7 | -3.26244 | -54.06395 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5983a7fd-8dae-393c-b058-8b39f57dc61f | -7.22893 | -40.35273 | 2026-10-10 04:08:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e7c104d5-abeb-34d6-888f-5589a518df56 | -3.39544 | -50.22022 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2bf6f251-3489-31d9-8f0a-116a723c516b | -7.1869 | -55.16545 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bfc11f34-0389-319f-9a88-b75ee9abf679 | -9.89378 | -44.78571 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b91096c-50c8-3091-87cc-ac0b1adf0501 | -8.4482 | -47.98926 | 2026-10-10 04:08:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README36.md)
