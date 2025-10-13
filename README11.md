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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fd19f59-0c8b-3955-b1c1-f007e4017a23 | -5.38919 | -47.20691 | 2025-10-13 03:53:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 117c76eb-cf5e-3c44-8dfe-802faf4ada7b | -5.94164 | -43.93528 | 2025-10-13 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1689638-49e5-32e2-95f6-878f84c866b1 | -4.88852 | -37.49734 | 2025-10-13 03:53:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 27.7 |
| 4cf0f012-d09d-3d79-a142-3ed4d314bf8f | -6.23385 | -43.0044 | 2025-10-13 03:53:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5f1844bc-d4cf-3410-bb44-8005fbe238ca | -7.69148 | -42.37434 | 2025-10-13 03:53:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 248dbffd-3fdf-3e71-9f42-8e2a6d3a0775 | -2.4611 | -49.03629 | 2025-10-13 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba438fb7-7a26-3869-b3f1-aebb32916706 | -2.46191 | -49.03138 | 2025-10-13 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ea89c74-33e9-3ebe-8cac-316c841d5dbc | -6.73631 | -42.08566 | 2025-10-13 03:53:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 8f4e7ef0-21b3-3a9a-9a00-0a6f3c16b9d6 | -7.49866 | -42.76649 | 2025-10-13 03:53:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d0f4099b-4e09-393c-87d7-3496d84e3a3c | -5.86597 | -43.84742 | 2025-10-13 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1955bad-8271-38ce-9bf5-3d2f5304e406 | -5.30485 | -44.26769 | 2025-10-13 03:53:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e5c21509-9f9b-3c02-a8c1-62961766de44 | -7.33604 | -43.86414 | 2025-10-13 03:53:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 60ab2bf9-28e5-33e0-a2f0-0d7836947ec7 | -2.53982 | -47.8056 | 2025-10-13 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| abc7b30e-bb01-3c89-8f17-4f64fe0b91a5 | -5.62184 | -42.58207 | 2025-10-13 03:53:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| c8dd3ff5-57f0-3caf-9727-1b7f50994751 | -7.06064 | -39.27373 | 2025-10-13 03:53:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 291cfc7c-4d47-376d-9a46-71df29116c7b | -4.48177 | -44.93727 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9282f461-b013-3cbd-b83e-cf0882be39eb | -7.14691 | -41.70875 | 2025-10-13 03:53:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| bf8814ae-126f-3653-95a2-d2282fb38b70 | -6.73594 | -42.20406 | 2025-10-13 03:53:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| d2c5028a-8064-31c8-8ab2-6bda9ad16213 | -6.4647 | -44.11207 | 2025-10-13 03:53:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50d38ccf-1cd2-37c1-9c51-ddcb1a8ee0a6 | -5.88487 | -41.38854 | 2025-10-13 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a26f830f-33fd-3716-8e6b-2e044de4c092 | -5.32099 | -43.43523 | 2025-10-13 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbf743ab-58c9-31f2-bba0-45d79cfea1ff | -5.10874 | -43.20288 | 2025-10-13 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ed8b31da-cf27-33f3-9c0a-109f045be573 | -5.93622 | -43.94208 | 2025-10-13 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dcbb9b6f-cf08-350c-a436-6c82693330ec | -7.05494 | -44.27095 | 2025-10-13 03:53:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a28e4582-fce3-317b-9cab-c6f658c741f8 | -5.5852 | -41.13134 | 2025-10-13 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cc3f3b77-8804-3ec2-ada9-42d108afdf61 | -6.88898 | -44.69288 | 2025-10-13 03:53:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3401deff-03be-3fcc-8e59-2f5ba14e8c28 | -7.48501 | -42.7546 | 2025-10-13 03:53:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ff4bcdb6-c112-3d2d-8e37-a910021f5196 | -4.47935 | -44.95155 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d0c095e0-8cf3-3502-990d-46032fd6034b | -5.30992 | -43.42582 | 2025-10-13 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e8f4f2ac-d1e5-3e65-9ba3-89dd11bfc215 | -4.88558 | -41.55714 | 2025-10-13 03:53:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d34c0b00-7cc4-3a4d-825a-8e644230ce80 | -2.92381 | -48.29754 | 2025-10-13 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9bdbbb9e-4ec4-3782-99ba-de84e714daf4 | -2.52833 | -47.8035 | 2025-10-13 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 20f841a5-efdf-3107-a3cc-60d91ea41737 | -5.61989 | -42.58007 | 2025-10-13 03:53:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 728e0557-dc06-35b5-a983-bcb35d8c356c | -7.65585 | -42.56765 | 2025-10-13 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b6bed63c-7458-3c13-a638-402a2ccb9d72 | -6.73046 | -42.07514 | 2025-10-13 03:53:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 5315ca98-6fb8-326b-93c3-f6db139410a3 | -5.88553 | -41.3844 | 2025-10-13 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e8146293-17ad-3344-87bb-c1510f62fb3b | -6.20033 | -42.67215 | 2025-10-13 03:53:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2541d1fe-aa0c-3235-840c-fe7c8e10d916 | -4.68181 | -43.12933 | 2025-10-13 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7cc33a50-5898-3615-b7bd-e5f656044539 | -7.14648 | -42.52065 | 2025-10-13 03:53:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b280b0d0-2ada-332b-89e6-265545408f00 | -7.14346 | -42.51539 | 2025-10-13 03:53:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b9b26ddd-6b9a-3a40-bd44-bf61f6456f3d | -6.20641 | -42.68325 | 2025-10-13 03:53:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1fa55632-250c-318b-8abb-b8ba60762dab | -6.33708 | -44.32518 | 2025-10-13 03:53:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2edbfea9-db86-36c3-8bb7-2f905a777a96 | -7.28225 | -41.96232 | 2025-10-13 03:53:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| cfc058f0-6de7-38df-b466-3f650df6e93c | -7.51302 | -42.15762 | 2025-10-13 03:53:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ba3a7a1b-2a3f-3fcf-864d-18adc01b057e | -6.77471 | -42.82396 | 2025-10-13 03:53:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 5e40e343-cac7-3169-85f4-4f1dfdad0d3a | -5.93308 | -40.88863 | 2025-10-13 03:53:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 17327e01-9a1e-33fa-b3aa-5d96c5ce112e | -8.46279 | -46.11834 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 02dc0341-f9b8-3d47-b458-0ff9a27b02f4 | -8.40172 | -45.06256 | 2025-10-13 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c18312a-f2e4-3744-b7fc-c9d0b3b7c1c9 | -7.88062 | -44.45334 | 2025-10-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 005b9ee9-9b10-3aaa-893c-689bd8e8b4e9 | -7.75051 | -44.20127 | 2025-10-13 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| deeee801-9923-3a3a-a9e0-568a40a0fda3 | -13.75414 | -45.6488 | 2025-10-13 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2dde594b-7250-35ba-8513-9370fdb06f2b | -7.5018 | -44.63395 | 2025-10-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 61f5feb8-ed95-3ded-8184-f8ebbdac5e42 | -13.86214 | -45.48985 | 2025-10-13 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ced0f98f-6ef4-3b43-a640-1852174b6ddf | -7.49751 | -44.63325 | 2025-10-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 3990d992-f11e-32ef-83e9-dcf75d837d23 | -10.81341 | -43.98601 | 2025-10-13 03:55:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 62b7a99b-bb6f-3997-aff3-ed21b8c8382d | -8.46571 | -46.12915 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9382da2f-2cce-327b-a3aa-abc98a3aedf4 | -7.91837 | -47.21564 | 2025-10-13 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d5c39d0-7645-348d-b30f-973f4593f21f | -7.32355 | -44.75431 | 2025-10-13 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| def30d3c-595f-3221-a4a1-494d59be39c3 | -8.44255 | -40.43024 | 2025-10-13 03:55:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 89fc07f2-6735-39c7-ae9f-3991fc6acb7b | -7.67495 | -43.98874 | 2025-10-13 03:55:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a198160a-09d5-3f73-b9b5-be10c7896e70 | -15.05084 | -41.23864 | 2025-10-13 03:55:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 06658f0e-0c21-37c6-83be-05d1e41a3e04 | -7.754 | -44.20573 | 2025-10-13 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0eafeed7-4372-336c-beb6-551f1478dc3b | -10.80044 | -43.96788 | 2025-10-13 03:55:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a7c7c466-166b-30b0-98f9-40fc69b1c383 | -13.56613 | -43.41615 | 2025-10-13 03:55:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 978398c0-68d6-3176-abeb-9d47d6367c32 | -13.3312 | -47.10733 | 2025-10-13 03:55:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42cbf0b9-62f7-3f50-9c0c-ef1e2a784ddb | -13.33184 | -47.10484 | 2025-10-13 03:55:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0ce367b1-ac1b-39f0-ae81-dbc2c9f65b30 | -7.78118 | -44.04852 | 2025-10-13 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b553716-f0c9-3a39-9857-75e71744ed94 | -10.03638 | -43.81279 | 2025-10-13 03:55:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e0122226-5811-3bba-946d-06879cfe7f8d | -7.62196 | -43.04764 | 2025-10-13 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 165ffeae-1641-3087-8ff7-7b0dff8a6366 | -7.49892 | -44.62503 | 2025-10-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 26.3 |
| cebb2291-c59c-3480-acf8-ad72c0c3facc | -10.79914 | -43.95201 | 2025-10-13 03:55:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90364c45-80be-380d-98f8-74e6db8ef09e | -8.32187 | -46.24783 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07616445-ca3f-3c3a-a783-98b5ba1f7871 | -7.35871 | -45.19934 | 2025-10-13 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8e9eb839-36e5-3e24-9387-a529644405b6 | -8.46952 | -46.1349 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 90562a96-a1a7-321d-9484-66b709444db0 | -11.66381 | -47.5561 | 2025-10-13 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9f3d9264-37c9-3688-9ff8-8f3c4f43c3e6 | -7.74893 | -42.40926 | 2025-10-13 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 96b8fcf0-93cf-339a-a2cb-f1fced547a9a | -10.80735 | -43.97442 | 2025-10-13 03:55:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0370f8e6-8881-3e0f-9e43-090c50df4be0 | -7.49314 | -44.60739 | 2025-10-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6105a9fa-c92a-3b0d-be30-b1bbe88cbcfc | -8.21839 | -43.33078 | 2025-10-13 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 023553e0-d644-3f84-9f9d-e679b72f0ff6 | -13.3231 | -47.10008 | 2025-10-13 03:55:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60998bb2-6643-30f7-90eb-ab83474f1af5 | -15.18292 | -43.57473 | 2025-10-13 03:55:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 10e72a8a-6bbf-3986-9e9b-8b7b1e6ae42f | -7.76215 | -45.69732 | 2025-10-13 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8e8f6c02-6c0d-3481-9ec1-ee6d4e675b31 | -8.2356 | -43.35218 | 2025-10-13 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| ddeac2d5-f312-3c5f-9954-44f3927a5734 | -13.87983 | -45.48516 | 2025-10-13 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 01098edf-e571-35fa-9173-e32c67c3ef1c | -14.43788 | -48.05214 | 2025-10-13 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd98b1df-1f6d-3ee6-bc97-3265c1d02000 | -7.50014 | -44.59224 | 2025-10-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5351b779-c8bd-3fc9-9504-3dc93394bddf | -8.38806 | -45.06393 | 2025-10-13 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 21278956-7741-350f-9bb6-2bd0fc53b979 | -10.80259 | -43.97883 | 2025-10-13 03:55:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d96aa120-3ade-3891-832a-55b5beed3c25 | -15.53661 | -41.79626 | 2025-10-13 03:55:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 17eed0a9-f0c4-3fc3-a64b-934ce2182a33 | -7.51725 | -44.59505 | 2025-10-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5fb131a8-1178-39ef-ad50-ddc14faeb55a | -8.24004 | -43.37326 | 2025-10-13 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1229a648-e497-3efe-ad81-29d857d7d3c2 | -8.84702 | -45.26131 | 2025-10-13 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0b0d723a-6046-3068-b85c-cfefe9dafca6 | -7.75115 | -44.19753 | 2025-10-13 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d8c4dc1d-e056-3766-9148-7afdd54c7720 | -13.75484 | -45.64495 | 2025-10-13 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a1f6bf83-253b-3b6f-9eb2-70d7647785a0 | -8.47507 | -46.13064 | 2025-10-13 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a925752-03e4-3392-b069-84b93019d3d8 | -8.21175 | -43.3277 | 2025-10-13 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 2ee7cb5d-88b9-3026-840d-d302b4d936ad | -7.76136 | -45.70189 | 2025-10-13 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 74c14cf1-1ec4-309d-b85b-0f4592280a08 | -15.18365 | -43.57048 | 2025-10-13 03:55:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f0f65d40-2a92-3588-af2a-f77e608f682b | -7.48964 | -44.62772 | 2025-10-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 30188047-9c1e-3ae3-8fd5-10dc4b2c537d | -11.85026 | -38.20282 | 2025-10-13 03:55:00 | NOAA-21 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |


[Clique aqui para ver as próximas entradas](README12.md)
