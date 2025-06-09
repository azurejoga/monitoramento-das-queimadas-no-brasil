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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2c69371-b966-36cc-85ce-9301103ddcd4 | -12.54913 | -45.42278 | 2025-06-09 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 56c920b7-eda8-3ee3-b306-fc26d6a949ca | -15.07749 | -48.94657 | 2025-06-09 03:47:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6cb5b98-dc7a-3c33-a89e-a999ecf6866b | -13.01837 | -47.86338 | 2025-06-09 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 790805cf-49aa-333d-a836-677776c3240a | -16.68095 | -43.88378 | 2025-06-09 03:47:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17bb7d7f-0025-39da-81eb-7ee88c0fffe6 | -13.01584 | -47.86664 | 2025-06-09 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e318241a-b717-3415-899d-f5b44e6e4fad | -13.15767 | -43.26283 | 2025-06-09 03:47:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f66c77d1-16ee-336d-9ccf-128ae0e946c7 | -12.54605 | -45.41929 | 2025-06-09 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6e52abf-bdfc-3490-bab3-31ad9fa52d79 | -14.24794 | -45.48671 | 2025-06-09 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03464110-69bb-3838-8669-3b5d0a1b52d6 | -13.00989 | -47.86539 | 2025-06-09 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7537e9a6-3637-3b89-afc8-2ddd26a6a003 | -14.93544 | -42.29099 | 2025-06-09 03:47:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e7694a0e-5788-3e89-acb6-ec63637c9c11 | -13.9355 | -47.21133 | 2025-06-09 03:47:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 56a59e13-f6a0-3071-9c1b-437761f43259 | -14.24271 | -45.49062 | 2025-06-09 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e07b1619-161f-3621-b177-ba1660e2c5ec | -19.45484 | -45.30808 | 2025-06-09 03:49:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| afb6b919-7034-3ec7-a03a-23cc4087954b | -19.971 | -44.21691 | 2025-06-09 03:49:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| df0b50b8-8001-3aac-a6f5-1ae7c4ef67ca | -20.7676 | -40.74045 | 2025-06-09 03:49:00 | NPP-375D | ANCHIETA | ESPÍRITO SANTO | Brasil | 3200409 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7e615f16-b3b7-3687-b2bd-80a91e319c83 | -19.66118 | -40.18188 | 2025-06-09 03:49:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 16d52c7a-3a2d-3836-a0a0-49c3743e4562 | -19.83825 | -40.08079 | 2025-06-09 03:49:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 690bac78-b9d6-3426-ae59-7309b6ce54b4 | -3.35018 | -39.12838 | 2025-06-09 04:04:00 | NOAA-20 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| de34cb58-7347-3801-be9e-d5368541da2a | -3.04833 | -49.43494 | 2025-06-09 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 202c67af-12bf-33f9-8978-a2c789f00645 | -3.04781 | -49.43807 | 2025-06-09 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 158d9650-5d30-377f-91b3-d2877170db70 | -7.01485 | -44.60108 | 2025-06-09 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ef066b8-c079-3ebf-935c-ee27594e1f53 | -8.07422 | -34.97706 | 2025-06-09 04:06:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 594208a3-81f0-3730-89bd-c5fd32129bc5 | -9.40458 | -48.44319 | 2025-06-09 04:06:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb8f5fa4-b6e7-37ee-b8d8-13fcb39b2d5c | -7.00702 | -44.60411 | 2025-06-09 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a41eb215-feb7-31c8-b150-67c9b3674ed4 | -8.38237 | -41.85091 | 2025-06-09 04:06:00 | NOAA-20 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8842fa0e-2695-3f9f-a1ce-8b6aff24b024 | -7.00861 | -44.61695 | 2025-06-09 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 76272b43-ab14-36a1-8b8a-4c69b4fe8979 | -6.22831 | -48.53326 | 2025-06-09 04:06:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cf94cad3-8c1c-373d-b059-d9dae7acb387 | -7.0122 | -44.61742 | 2025-06-09 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f5c89c2b-a267-39a5-b5d0-693faaa56b9b | -9.0753 | -47.14927 | 2025-06-09 04:06:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5e4e22c-208d-3489-9413-567e98cd679b | -6.23373 | -48.52934 | 2025-06-09 04:06:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 526f51ad-25ef-3b7c-abb9-dce0b6ff9e4c | -9.41255 | -48.44897 | 2025-06-09 04:06:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 454bf2e1-02a1-3760-af0c-ae9aaa2e310a | -9.07932 | -47.14999 | 2025-06-09 04:06:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97ddedf7-cc61-3aa1-934c-d1b70537636f | -8.70077 | -47.1431 | 2025-06-09 04:06:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d47ca69-2262-3aa9-ab6f-419ecf01f905 | -7.28031 | -44.21544 | 2025-06-09 04:06:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f2e5e5b-9858-378e-857c-da45921d781a | -7.18118 | -42.80501 | 2025-06-09 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5eddb0b9-ffa0-31d5-a004-a6957bb6cc13 | -10.69456 | -37.05005 | 2025-06-09 04:06:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e8455f1f-fd5c-354d-8c03-5545444bf767 | -8.08777 | -47.11194 | 2025-06-09 04:06:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24c425fe-7977-310a-8990-a7a1b78a76df | -8.96531 | -47.97121 | 2025-06-09 04:06:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe8e497e-d7f4-3ca7-8a78-19a3cdc1cc64 | -7.65444 | -46.09937 | 2025-06-09 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e6628f2-abc7-3411-ae44-9868ed914df7 | -7.01419 | -44.60515 | 2025-06-09 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3687df56-8f8a-3310-b0ef-6aaa1abf1127 | -8.07434 | -34.97488 | 2025-06-09 04:06:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 111d3a9c-357c-3708-abff-48fd9db52fe1 | -7.65199 | -46.10112 | 2025-06-09 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 17186508-872a-30a2-9971-e17a30692c7b | -7.01577 | -44.61801 | 2025-06-09 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b32042c6-cf80-3821-9d51-7f941fe27f51 | -9.41328 | -48.44471 | 2025-06-09 04:06:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bffc4d8a-a392-3a9b-8b39-279dd67429a3 | -7.2714 | -44.226 | 2025-06-09 04:06:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2eae8311-a947-3c88-a861-7817b320ed12 | -7.02107 | -44.58531 | 2025-06-09 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9b21a99-b096-311c-a5fa-9f2975f3e127 | -7.13516 | -43.59497 | 2025-06-09 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 16bf1db6-06fe-35a7-9de1-8d790dc7773c | -7.27204 | -44.22208 | 2025-06-09 04:06:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d12e23ff-ec34-30fa-a194-06f62d7a386b | -7.49392 | -37.80399 | 2025-06-09 04:06:00 | NOAA-20 | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6f4276a1-9d1c-3969-92df-5ea8af4a1b8d | -7.86692 | -47.89783 | 2025-06-09 04:06:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a805622-5f9a-370c-a23c-c919aec4d1e1 | -8.01018 | -46.78368 | 2025-06-09 04:06:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| abcb6817-5fed-3238-b937-2b00fc492aed | -7.01709 | -44.60986 | 2025-06-09 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3388e38a-c6f4-3145-be13-a4be7baad0ae | -6.85788 | -45.03536 | 2025-06-09 04:06:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b76948a2-57ee-3a3a-ae81-7bdad743fb9f | -9.40317 | -48.42546 | 2025-06-09 04:06:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3aaf5af4-fbb9-326a-8ffd-51b4e79cfba3 | -7.02041 | -44.5894 | 2025-06-09 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| af699374-5d79-388e-8386-bccf65e95c7f | -5.85007 | -47.10063 | 2025-06-09 04:06:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f45318f-0c93-33e7-aea7-3f05f84c9c62 | -7.00635 | -44.60823 | 2025-06-09 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 73f5871a-7ff4-30ac-8444-c7ee48611be7 | -7.00927 | -44.61283 | 2025-06-09 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 5a2f41ad-06c0-306a-a3fc-632550461d1b | -7.01643 | -44.61393 | 2025-06-09 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3dc84d20-f94a-31f6-9766-79f3bfcd4bbb | -7.01842 | -44.60169 | 2025-06-09 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a80f9197-3edb-3fc2-a502-ab3648b563b9 | -7.65584 | -46.10175 | 2025-06-09 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9b523220-576c-3e94-ad29-ec95c0eaabd9 | -8.72226 | -50.03935 | 2025-06-09 04:06:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fc027f8-dc12-306c-8dea-dba35a73d0ac | -7.02305 | -44.57309 | 2025-06-09 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9c0e552a-fe36-3944-8e5a-0d062181e046 | -9.40966 | -48.43971 | 2025-06-09 04:06:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52f59d01-75c0-32d6-8bff-49a3a78ee125 | -7.01617 | -44.59294 | 2025-06-09 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cef0e7b2-69d4-346b-9cef-389b95424969 | -7.01683 | -44.58889 | 2025-06-09 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 46d98af2-42cf-353b-93f7-dba8e206ad63 | -5.84942 | -47.10456 | 2025-06-09 04:06:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82c11d7b-39f0-3754-8a9f-1493c20fdb19 | -7.87193 | -47.89444 | 2025-06-09 04:06:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 675a5a3d-a68b-3ec0-a840-68a22c1bbe61 | -7.13798 | -43.59925 | 2025-06-09 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd90eaa5-278c-30b1-8a0a-06336c8db0a7 | -7.65365 | -46.10419 | 2025-06-09 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| be305b1d-1e76-31e5-bcae-0cf54080df2f | -8.08308 | -47.11486 | 2025-06-09 04:06:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd09259f-4cfe-32f1-abed-9c7f331714ee | -7.65829 | -46.10001 | 2025-06-09 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b9489cb4-c326-30b1-8fee-01750fac75a7 | -7.86763 | -47.89368 | 2025-06-09 04:06:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7078c409-09d5-364e-93a1-e4f46685859d | -7.01948 | -44.57257 | 2025-06-09 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fab957b1-952d-39af-b827-e084b226f75c | -9.17475 | -40.94756 | 2025-06-09 04:06:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 56d0275b-a563-3e32-bae6-4b1a60bc3a21 | -9.40531 | -48.43894 | 2025-06-09 04:06:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 99ef9bfc-4cb8-30ec-a54f-b2dc3fa84bc3 | -7.27554 | -44.22266 | 2025-06-09 04:06:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0344960e-b623-3143-beda-a3032eb0dfc1 | -7.01776 | -44.60578 | 2025-06-09 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 96b5344a-84aa-3bd6-a719-b0a198f9d851 | -6.53066 | -45.69238 | 2025-06-09 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef5ede21-40dc-3439-9e6a-c89571cecdfb | -7.02066 | -44.61049 | 2025-06-09 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e27c6513-dc18-3149-994c-3832224d5029 | -7.27968 | -44.21933 | 2025-06-09 04:06:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc21f5da-cf57-3c67-be48-020a7afede24 | -5.63464 | -43.72496 | 2025-06-09 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3fd2e95d-e057-3e53-93bc-4a212f414b50 | -5.12077 | -37.78994 | 2025-06-09 04:06:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0f1620eb-4448-313b-9278-330029d32051 | -6.01272 | -45.76943 | 2025-06-09 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f1fde134-9edc-3784-afb3-7a7279319d69 | -9.40893 | -48.44394 | 2025-06-09 04:06:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a69b0923-9aaa-3de6-ad58-d978f4fc5808 | -7.04496 | -45.77191 | 2025-06-09 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb05d5b4-bedb-3e30-84fd-53e757090d27 | -7.02173 | -44.58125 | 2025-06-09 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c5e459a-38f8-3104-ab9a-9aae297bfddf | -7.01353 | -44.60923 | 2025-06-09 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6c78efc2-f515-31f6-ac1a-be2cc5d4b4d4 | -7.01881 | -44.57666 | 2025-06-09 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e108051-b73e-3380-b109-34aa76d22946 | -7.02239 | -44.57717 | 2025-06-09 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 56323cf2-f3e4-3e04-b513-b18d53920788 | -7.66135 | -46.10548 | 2025-06-09 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 02bfb9f8-2bae-3444-8916-d35e993a430b | -8.96469 | -47.9705 | 2025-06-09 04:06:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eb960608-fe19-3d2c-b37f-f21068e42823 | -9.41401 | -48.44049 | 2025-06-09 04:06:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2bb4fc13-ff0e-3b23-9d07-71187a31d07b | -4.48593 | -43.77387 | 2025-06-09 04:06:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 630556ec-156d-3daf-bd05-95fffd7a108e | -7.01286 | -44.61333 | 2025-06-09 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8017c35d-1c89-315b-b990-debd912ed440 | -7.01749 | -44.58482 | 2025-06-09 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9e15bea-8102-396f-92ab-9f1823850202 | -6.74136 | -44.99317 | 2025-06-09 04:06:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6ad4967d-b095-38fd-ab73-482a96d50870 | -4.48946 | -43.77443 | 2025-06-09 04:06:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| d273d189-c00d-3341-ab65-36b68f48eb3e | -13.48855 | -44.13427 | 2025-06-09 04:08:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3020a7ff-e38f-323f-a6ae-e0210c068bd8 | -10.64979 | -44.48066 | 2025-06-09 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README4.md)
