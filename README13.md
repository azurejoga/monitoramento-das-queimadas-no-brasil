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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb762351-d26e-3cee-b19b-7f8802bc1d33 | -2.4719 | -45.85543 | 2025-11-29 04:12:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fb7d118d-f94b-3842-95e3-4e1886bfc7e4 | -2.53596 | -45.38836 | 2025-11-29 04:12:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e9b0dd5-3eac-3d0f-acef-043749f66215 | -2.74819 | -49.86297 | 2025-11-29 04:12:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec2bdab3-928e-3e07-b0d3-44b170862f23 | -2.12641 | -45.36732 | 2025-11-29 04:12:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab9bf6f2-a0a3-3ef7-a46f-c1f287b72458 | -3.34317 | -39.99024 | 2025-11-29 04:12:00 | NOAA-21 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 85fb9143-79ec-36ec-9877-356183e2fb23 | -2.6447 | -48.02707 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a7c0e133-29b9-3643-acce-6d2e4d5f0e26 | -2.95627 | -49.18574 | 2025-11-29 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3c721342-6361-3c5a-bdbd-af7a8c2f39cc | -2.97042 | -45.50827 | 2025-11-29 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2cc2470-8612-39ee-9014-2f584b074bf4 | -3.62954 | -42.7547 | 2025-11-29 04:12:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be757ab2-016f-3817-b447-9073f8554a78 | -2.74734 | -49.86819 | 2025-11-29 04:12:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2461188-c378-3641-9272-acc1080eacc2 | -2.63981 | -48.03033 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ee7fe968-2cbc-3337-ab0e-dc75129b4203 | -3.53224 | -39.94287 | 2025-11-29 04:12:00 | NOAA-21 | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 679c5bb7-9177-316f-9a76-28d2ec94d1ca | -3.79902 | -42.08355 | 2025-11-29 04:12:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 78e40e55-7e39-375c-a35f-0235bc422437 | -3.94523 | -42.08565 | 2025-11-29 04:12:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2fb6f017-cbb3-3487-bea4-0b95457d087b | -2.63979 | -48.54725 | 2025-11-29 04:12:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5e394d4a-11e8-336c-8dc2-c706784f2aba | -2.99587 | -45.41875 | 2025-11-29 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81e49314-2a44-3da5-8af8-4cf443274cbb | -2.64366 | -48.03563 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 4cf3580d-1142-3a6d-b16f-16eab6140304 | -2.6318 | -48.485 | 2025-11-29 04:12:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d9a0a7f7-0a1a-30a1-9d82-f57569fac737 | -2.74461 | -47.13372 | 2025-11-29 04:12:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1d84917-9f28-3327-a697-0753cca68b3c | -2.70823 | -47.41324 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c91eeab-bd44-3619-9e45-2aac7db8737c | -2.18207 | -46.1595 | 2025-11-29 04:12:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 843d8665-0343-3b82-a316-147c3f9fc4f0 | -2.78208 | -47.42119 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c171c62a-79f7-3fed-86a6-12389a6d6e55 | -3.34948 | -43.54102 | 2025-11-29 04:12:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2dee0938-c58d-3799-8965-f7425b381e41 | -2.63472 | -48.55077 | 2025-11-29 04:12:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 05bb21bd-0b49-371b-87d2-dbe6825008ab | -2.33113 | -45.47066 | 2025-11-29 04:12:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 917a2aed-1128-3456-a896-4a5158a13de8 | -3.76564 | -42.51591 | 2025-11-29 04:12:00 | NOAA-21 | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5b99679-e486-3ebb-9ab6-c76f5f8e61c5 | -2.466 | -48.11371 | 2025-11-29 04:12:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a04c531f-aea2-37dc-a826-4a2bf9197ecf | -2.39676 | -48.51492 | 2025-11-29 04:12:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 956b051f-b038-3964-8bf5-2e3cfaf32d57 | -2.17709 | -48.42176 | 2025-11-29 04:12:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 68d23f68-90d8-3e38-aa01-52d88722f1bc | -2.6449 | -48.02775 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| ff8522f3-b770-3654-b66e-ac9be0f6483e | -3.79137 | -41.93742 | 2025-11-29 04:12:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4c0f3250-8341-392d-84f8-f2c2817f358b | -2.78556 | -47.42542 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b64f15ef-395e-34ec-8f8f-7d20bfa9f805 | -3.09319 | -40.06243 | 2025-11-29 04:12:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dc593e08-c92a-310e-a061-1774854f858f | -3.78143 | -41.93588 | 2025-11-29 04:12:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 361393e2-3a7e-3911-a231-5f58ad60d8da | -3.08489 | -41.25332 | 2025-11-29 04:12:00 | NOAA-21 | CHAVAL | CEARÁ | Brasil | 2303907 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b3bbbbdb-7a81-3582-92a5-3c151f9fa0f9 | -3.16963 | -45.24031 | 2025-11-29 04:12:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b2e0beb-3592-3e0f-876d-4e4148616568 | -2.34716 | -45.7007 | 2025-11-29 04:12:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41d312d8-3d09-3f43-b514-4eaeb31c2b0f | -2.92449 | -45.25292 | 2025-11-29 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 576839c2-4b49-3583-a515-73e02b2e78d5 | -3.66581 | -43.56187 | 2025-11-29 04:12:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18fe8213-3a98-3572-945b-720be825e360 | -3.3404 | -41.86353 | 2025-11-29 04:12:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e7890729-4a5e-3a3a-9364-acc8048622f0 | -3.5588 | -39.10777 | 2025-11-29 04:12:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 34c8c3ee-d834-3cfb-a4c9-9d6500c0b6a9 | -2.78788 | -47.43686 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19c6a9b4-dea8-35dd-8922-e1c794fc4792 | -3.18115 | -45.6201 | 2025-11-29 04:12:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8c1d03be-ce08-3702-be66-b6ce711bd081 | -2.47261 | -45.85104 | 2025-11-29 04:12:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| df66a610-e8ed-387d-9b11-0e2b72098a8b | -2.74429 | -49.32875 | 2025-11-29 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9a98d8cc-1373-37b4-82f9-69e892006966 | -2.70011 | -47.41184 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10401155-97ab-3bd7-ace1-e6dd1f255ac0 | -1.88694 | -48.40125 | 2025-11-29 04:12:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fb8df75-0b49-3064-8f6b-78fc5a612794 | -3.86495 | -41.57513 | 2025-11-29 04:12:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7d4ebbe4-da73-33ee-bb42-6da6fa3202ab | -2.54974 | -44.60304 | 2025-11-29 04:12:00 | NOAA-21 | ALCÂNTARA | MARANHÃO | Brasil | 2100204 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c03426c-5bab-349e-bfb7-dd5ce264f2b1 | -3.10549 | -45.78798 | 2025-11-29 04:12:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d9e5e102-df03-30ea-852a-d57ae98d099d | -2.63404 | -48.55503 | 2025-11-29 04:12:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bfc61e9a-3b31-36fd-b42f-55a0dd37c588 | -2.24778 | -48.31639 | 2025-11-29 04:12:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c97417e-0398-3885-98a3-eb46ef78b402 | -2.64764 | -48.03559 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| bab39641-5727-3ca2-a252-270f8bcbe2d2 | -3.17753 | -45.61954 | 2025-11-29 04:12:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cbb3ad1c-5ac9-3bb4-b136-2db402bed2ab | -1.29994 | -47.21544 | 2025-11-29 04:12:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a75a598a-9297-33a3-bad2-1d0aba4806a4 | -0.97064 | -47.56636 | 2025-11-29 04:12:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba577ad9-cc41-319c-8b2a-ddc0a5ce4a13 | -2.79312 | -47.43026 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e280b369-1cac-3d0c-ba10-f2fc15d4112a | -2.63033 | -48.55007 | 2025-11-29 04:12:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 815aa7e9-268b-3948-94a5-f3e6ee8e3057 | -2.60293 | -47.34042 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4aa7601c-0bda-3dd5-ab94-68fb0a54ae42 | -2.96083 | -49.1865 | 2025-11-29 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aba54a95-f1a5-3223-8e6a-01742e35c09b | -2.42727 | -50.29134 | 2025-11-29 04:12:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9e4f4eee-e029-3178-a9a0-960edd874282 | -2.64428 | -48.03169 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 905e2b57-b19f-39f4-b6bc-bf14bfede289 | -2.63101 | -48.54581 | 2025-11-29 04:12:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 12561b06-0b50-31fa-8baf-60153a474301 | -0.75308 | -47.76095 | 2025-11-29 04:12:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 83b8e3db-1fd4-3aaf-a30a-6a6d83efb36c | -2.57486 | -49.09922 | 2025-11-29 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a09fe8c-6f55-35fb-b92e-66fedd2d0dc0 | -2.64405 | -48.031 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| ae6445f8-e166-3a0f-9a5f-51254caec792 | -3.10616 | -45.78368 | 2025-11-29 04:12:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f1ecb7d7-a33e-300f-a60f-68832e96f789 | -3.43818 | -41.49839 | 2025-11-29 04:12:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2fcedbca-f21f-3f71-8282-e62e790f385f | -3.89217 | -40.76912 | 2025-11-29 04:12:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8e2977b1-5dae-3e8d-b666-30d27a3999a1 | -2.64829 | -48.03167 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| dfbd9ffd-d5f1-3f24-9c80-24a2220085b9 | -2.18182 | -46.16076 | 2025-11-29 04:12:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cef7ff4d-10ed-39a7-afb6-6243fdf53a4a | -2.79254 | -47.43386 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9f898ee6-7fb4-34d7-bccb-03029a29ca73 | -3.10565 | -45.78643 | 2025-11-29 04:12:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0bf8e83d-fc6e-3376-a248-7558f60d8b37 | -0.77323 | -52.33127 | 2025-11-29 04:12:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba590f5e-f0e5-3069-b6d7-2c0f52336e7f | -3.4422 | -45.41777 | 2025-11-29 04:12:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| faf311b3-98ec-3d55-b10c-3eb86cae7b21 | -2.84343 | -45.17073 | 2025-11-29 04:12:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8669668-f5cb-30d5-a41a-70d2e0f9b8fc | -1.48483 | -45.78838 | 2025-11-29 04:12:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 08e0e252-0c14-3dbe-bec4-bba4c0969b97 | -2.63618 | -48.48568 | 2025-11-29 04:12:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 70ac21d2-3d8f-3226-a882-338c476c6ed7 | -2.60236 | -47.34401 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 660dfe89-6f82-32ab-bb72-01d97ec9d825 | -3.79848 | -42.087 | 2025-11-29 04:12:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f0a8af7e-3dc0-356f-af2d-8c983088ee91 | -2.63608 | -48.54228 | 2025-11-29 04:12:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 9f4585bd-588e-3653-a433-6c05849dff42 | -2.65428 | -47.38608 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b77dd789-fd01-3fbb-8e02-f84abb042d49 | -2.68328 | -47.36127 | 2025-11-29 04:12:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84d98a81-2544-34ba-a3b5-bb8f9d6ed144 | -2.3055 | -47.73658 | 2025-11-29 04:12:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2a9f8e51-a644-359e-9661-7df97a34f6f0 | -2.30489 | -47.74036 | 2025-11-29 04:12:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 713ade36-18e8-3e33-a2d0-c1f97098bf32 | -1.37643 | -52.51071 | 2025-11-29 04:12:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39186299-4fd8-3506-8f8c-cfa7f5de0b7a | -3.80233 | -42.08406 | 2025-11-29 04:12:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7477af3f-95d6-39ec-b183-103aa9407dd2 | -2.44124 | -47.0703 | 2025-11-29 04:12:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8e1223b0-92c3-3923-a5ad-de3803a927f3 | -3.33214 | -42.50353 | 2025-11-29 04:12:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 86347544-c9b1-3672-b86d-7c6bedc0352d | -2.22486 | -47.51131 | 2025-11-29 04:12:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c0a723b9-bd0b-334e-beb3-f6f255dce35c | -2.97708 | -47.92784 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad04a7e7-98d3-3e5f-a54e-97855116a8ac | -2.64894 | -48.02774 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ae50c00f-b706-391f-8756-9bc67119bef6 | -3.59497 | -40.85746 | 2025-11-29 04:12:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| db56dac9-f704-3947-ab94-a915413e5ee4 | -3.62899 | -42.75814 | 2025-11-29 04:12:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9449cb77-72cd-3c8a-b405-1ef135b27444 | -3.66915 | -43.56239 | 2025-11-29 04:12:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4602f3d6-5283-3f52-bf1a-036300f14e3a | -3.88991 | -40.7613 | 2025-11-29 04:12:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5ef67139-e8ac-3835-8b28-7d2e3c6cd70a | -3.65473 | -42.24459 | 2025-11-29 04:12:00 | NOAA-21 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8025bf31-fe9e-3437-ac51-8d7988fdf0dd | -1.48109 | -45.78778 | 2025-11-29 04:12:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 5042b66b-a60c-340d-8772-b422884622d8 | -2.55294 | -46.00311 | 2025-11-29 04:12:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| df5360e8-a7d4-38a9-866b-75744c31b7ab | -2.74804 | -47.13784 | 2025-11-29 04:12:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |


[Clique aqui para ver as próximas entradas](README14.md)
