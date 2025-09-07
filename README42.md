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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06a42e97-03c1-30a3-b82a-4c324d483913 | -7.58575 | -49.2877 | 2025-09-07 04:19:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0156c18c-5b17-3c73-b319-460a947339e4 | -5.48535 | -45.91061 | 2025-09-07 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2eb10ec8-d402-3a38-8cd1-5e50acbb371a | -8.03441 | -44.08846 | 2025-09-07 04:19:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b2eb96a-5d0f-345b-8530-a800e830af89 | -6.2199 | -42.46217 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| bfdd9781-baaf-3e90-a715-5917acb36c63 | -11.83948 | -47.57231 | 2025-09-07 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57b500a2-ba0a-390b-b2b9-f5ead8b6c59e | -8.34789 | -48.27127 | 2025-09-07 04:19:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21b148c0-2b74-3368-8998-428150bbd31e | -12.54965 | -48.07787 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bf0ac37a-1a35-3039-b645-104cf75fbd23 | -6.48558 | -43.98407 | 2025-09-07 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| dcff5176-da15-3f26-9cdd-105a6b5a8711 | -6.20883 | -44.19086 | 2025-09-07 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 783e9df7-6028-32d8-a004-7bebc834d8f7 | -8.15197 | -44.85636 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b7c92e1-3d29-37b6-b49b-3c3ca6b52ccd | -7.58922 | -44.6998 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc3992bc-d6f3-3af9-97af-a62467957550 | -7.67284 | -50.30046 | 2025-09-07 04:19:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c80665c8-bc8d-358b-a670-83ee4b6bdf25 | -6.43092 | -43.61543 | 2025-09-07 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 27e8a117-01c3-3034-ada2-8b79318474ed | -8.45356 | -47.31883 | 2025-09-07 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07544f62-fc6a-3098-a5a1-62c040672ac7 | -11.31446 | -46.54793 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 03eb7ede-d5ac-32d9-8da9-6723362330dc | -6.60795 | -48.05153 | 2025-09-07 04:19:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b1e3c335-cc9f-33ae-a09b-f1d05e5096f2 | -10.06552 | -49.29729 | 2025-09-07 04:19:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9b05a940-8a1c-35e3-90f8-e06ba6206c1a | -6.21089 | -42.63446 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ad4763c5-77f0-395b-a0e1-e05612714325 | -8.34652 | -52.54929 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7e6b6b2e-517f-317d-9b1e-caa0dfc0b55d | -7.73602 | -50.32025 | 2025-09-07 04:19:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5544fb5-8969-348b-9ce4-ef7f25f0a42d | -11.21125 | -55.02509 | 2025-09-07 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b42afd49-4b1b-3c86-b41a-356670c81f51 | -8.08514 | -44.80661 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 518e60ff-e9ab-39e1-bcfe-2ee106fdbf43 | -6.59827 | -43.98045 | 2025-09-07 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7bcc8138-e332-3791-8673-0b6476826d78 | -10.7438 | -46.33578 | 2025-09-07 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd5322d4-56fc-3617-86eb-1cde88100732 | -10.60932 | -44.33412 | 2025-09-07 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1c28d12d-1e29-39bd-8cfc-78d1af073fcd | -6.15111 | -44.25626 | 2025-09-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bbfc29df-1751-3d87-baa6-66dabe7298e7 | -7.73714 | -48.82141 | 2025-09-07 04:19:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 123b7732-486d-3995-9c5f-251ccba3895b | -11.2243 | -55.01411 | 2025-09-07 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1abde8c7-92f3-3e57-9fd5-3d59c10277c2 | -11.31941 | -46.55964 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2913154b-c00a-3b63-a7e7-a80bd6471b95 | -6.12738 | -44.2561 | 2025-09-07 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8fd9e8c-da6c-3216-b436-7e30389dcfd9 | -11.31227 | -46.54034 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 923545b7-8d12-31de-90a7-af9bd1b743b9 | -10.72754 | -48.58125 | 2025-09-07 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 760d196b-055f-3a5d-8034-203eccc6b837 | -11.37392 | -43.54268 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d3333a9-b63b-3b83-8b67-95bfaaece98b | -6.55532 | -42.94378 | 2025-09-07 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6d521a40-2ef5-38c5-9f94-f297e858dafa | -11.04311 | -54.17445 | 2025-09-07 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d1ae44aa-1be1-3b03-9305-a7c542befba3 | -11.34675 | -43.51068 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be912e3c-8676-3f9c-af2d-bfb71a9a8e3a | -11.15066 | -48.39377 | 2025-09-07 04:19:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1aa86c9b-c07b-3308-9f05-75d3192393bb | -9.97268 | -51.66085 | 2025-09-07 04:19:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bc80381f-48fd-3a01-8355-114bcc4d210e | -6.13015 | -44.26007 | 2025-09-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c3e3128-b2f9-3ae4-871d-aa0a58978f8e | -6.19658 | -42.63607 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 39f8a6f4-0316-38fd-9664-f644fc9a5279 | -10.58246 | -48.47523 | 2025-09-07 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 12dea6cd-2854-3146-afc9-ec57b6fffbcb | -5.97329 | -44.73791 | 2025-09-07 04:19:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4cf8dab9-bd34-3bab-8ed1-ca6b90255130 | -10.57958 | -48.47062 | 2025-09-07 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e91a54a2-67e0-3239-9f69-2201f2547c6a | -5.76176 | -45.53864 | 2025-09-07 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46d25360-43d7-39ba-8bf8-9318e8bca6eb | -10.80723 | -47.72894 | 2025-09-07 04:19:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e16f1b50-bb53-3aa4-8a18-be1564ddfe8b | -11.20789 | -55.01412 | 2025-09-07 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 89056406-f2b2-3d6c-8c20-47c29b88851f | -8.11687 | -45.31713 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2f0caf6c-3341-3392-a715-09eb26530899 | -11.60052 | -47.16139 | 2025-09-07 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ffdeb446-56be-37ba-9d1b-2284ce19b0a3 | -5.9416 | -46.17484 | 2025-09-07 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7c4938d0-352f-3e5b-a505-6b803398c17c | -7.97452 | -44.94918 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5de61c04-c1b3-3f7f-8b03-f47b28cc5a2c | -12.85576 | -47.98791 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f43043bc-b953-3bae-8d98-0a18a8508c6b | -6.19409 | -53.25724 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26e7d6c1-969f-332f-ab83-6648563ce95d | -11.26295 | -46.46788 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb06ab24-0b46-3407-b515-7745ee0628ae | -6.196 | -42.63979 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 1bf3bd0a-faaa-32e4-b079-0dbc316f90b0 | -11.56863 | -47.74952 | 2025-09-07 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d01eb9cf-75ae-3eed-b74e-ac53eaf3fd8c | -6.65968 | -47.71434 | 2025-09-07 04:19:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d6a21b5-d1b6-378f-a413-a15a2b34f392 | -7.63107 | -46.55073 | 2025-09-07 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58c5cd1d-c83d-3aec-a5c1-e22528f052bb | -6.13123 | -44.25317 | 2025-09-07 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16c06ba1-ea47-3491-9d93-0489192e4d4e | -12.46874 | -48.03752 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86eed524-da0c-3834-9649-372a8a85ad7a | -8.34224 | -48.28317 | 2025-09-07 04:19:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2aff5b06-3a65-3e0c-9dfe-dc97a7c58e24 | -7.84418 | -44.93532 | 2025-09-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4edb5cf4-082c-30e6-94e2-1d3cdaadb79d | -8.45639 | -47.3232 | 2025-09-07 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39ffed7b-b512-3b1d-81c9-c1d124ef1119 | -6.23645 | -43.29005 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8460997b-9cab-3a04-ba3f-dea17c567de9 | -12.89504 | -48.0067 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4bfc7b84-90ef-3d8b-9756-49cf987a9d07 | -6.54607 | -44.83251 | 2025-09-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c833319-e18a-3c00-8a95-d8b7761dcbd1 | -8.80462 | -47.49206 | 2025-09-07 04:19:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4160cb30-0119-3f33-87f1-e2bf28834735 | -7.67981 | -50.30908 | 2025-09-07 04:19:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ac5af40-3ad1-3c0d-aacd-ef46a1fefa23 | -7.73508 | -48.81861 | 2025-09-07 04:19:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cac8e7ef-931b-3c3b-8797-b6694903d9af | -11.1512 | -48.36862 | 2025-09-07 04:19:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1867d7c3-fe91-32cd-b54e-56b62fb1bdac | -5.54286 | -45.6701 | 2025-09-07 04:19:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c75d1078-123f-39f3-88ff-6d1e097ca259 | -10.15219 | -48.74477 | 2025-09-07 04:19:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6f7737b1-110e-327f-9139-898e9882f63c | -10.74879 | -48.58529 | 2025-09-07 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fddf107a-49b6-368d-80f6-aadd570154ba | -11.77513 | -47.56131 | 2025-09-07 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0dd82886-0f8f-3b72-be87-a3beb3cc35bc | -10.78633 | -47.74881 | 2025-09-07 04:19:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd1719b2-65be-3427-b137-25e6042089f0 | -5.68016 | -45.43177 | 2025-09-07 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e526018-ff9c-3887-9a81-caaa79cbbeae | -6.17395 | -43.19196 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 60b96fc2-1b87-32d6-83ca-0c798ca3b08e | -6.66354 | -44.56042 | 2025-09-07 04:19:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06d09027-f391-3508-b416-d1b2049863dc | -9.45827 | -56.05352 | 2025-09-07 04:19:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7a0af063-62c0-3bd2-9d7d-daf01e31fe7c | -8.68125 | -54.66594 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d6cc331-d34a-3bf4-9861-059798b9dd81 | -7.01774 | -44.96395 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76532d6b-b535-3d45-90bc-117f51e39d4b | -11.83669 | -47.56803 | 2025-09-07 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 492e9de1-c291-3c6a-8648-b9c64c697c3e | -9.8771 | -53.81552 | 2025-09-07 04:19:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40f0d5e7-12e0-35ab-9f3f-8da3a8d261b4 | -6.53663 | -44.8274 | 2025-09-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| b08dcc17-3b2d-31fa-9be6-c40f80139b46 | -6.1472 | -44.23792 | 2025-09-07 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f35934bc-843a-3d44-a8fc-25ed5d2a1827 | -10.09011 | -48.09963 | 2025-09-07 04:19:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32cbd33e-f799-34c0-b209-106152952f8b | -6.85245 | -45.91837 | 2025-09-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 829059fd-2d7f-3f32-adf1-67a56c0fe7b6 | -8.50939 | -51.31486 | 2025-09-07 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4c3d8a81-cc40-38de-8ff2-be4e8696e420 | -11.0149 | -45.91144 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| adba6d82-46b1-3f79-b8a2-5c4ab3a63296 | -10.08107 | -42.6729 | 2025-09-07 04:19:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 906d1e16-5ea6-382e-a869-b9a2a78c76b7 | -6.19871 | -43.60174 | 2025-09-07 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb9933cd-3da7-33f2-bfdd-39899e005713 | -6.2235 | -43.29531 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a710dc41-18be-3484-b7a7-0781db5f538f | -6.22911 | -43.28144 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a3c6ef5-83ef-361f-93d3-15c642bc9c81 | -6.19885 | -43.36494 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae2a7712-47d9-340c-8710-09668a0ee2b1 | -11.2032 | -55.01553 | 2025-09-07 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d24fbfc5-74e0-3a2c-a994-1141849d3860 | -7.9242 | -49.30797 | 2025-09-07 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0d74d14-788f-3f5e-8c91-7b4440cb8dc7 | -6.80418 | -47.06969 | 2025-09-07 04:19:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 623fb48c-f7bd-39d5-8589-6cb9c5ae7bc1 | -6.219 | -43.32409 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 138f3d09-d060-35d1-a63e-0ac4ce30435c | -6.54938 | -44.83303 | 2025-09-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32a4d1bf-b9a8-387e-8b84-15a96422d2ff | -6.07718 | -43.36091 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b228fe1e-2eb1-3c3e-bead-3d17a94b9cb5 | -9.60943 | -47.89059 | 2025-09-07 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README43.md)
