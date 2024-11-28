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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2885b051-f5f0-301b-967e-bcc6ca6eb0a5 | -6.48529 | -47.49865 | 2024-11-28 03:59:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2dd609b9-816b-331b-8d18-1298b71cca27 | -4.72328 | -43.25278 | 2024-11-28 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 803a1f3c-5a44-39b8-ab57-a8ad83e62d2c | -3.0543 | -48.51722 | 2024-11-28 03:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 326f93a6-f6a6-3d5d-871a-3a3fd3e4849c | -3.59061 | -50.69087 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec796f44-61db-3b00-a4f4-64ec84383351 | -5.81632 | -43.79927 | 2024-11-28 03:59:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 32337df7-9c5b-3304-93ae-b52299c16ffd | -3.69419 | -43.43015 | 2024-11-28 03:59:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3c555468-b07b-3dce-89be-d0954ebf1892 | -6.16742 | -42.62424 | 2024-11-28 03:59:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| c5df313b-a5f3-31ed-9276-f9c3a3887c9e | -3.27053 | -50.62062 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 379b06a4-abf3-3484-826b-3acd2c6f4743 | -3.60423 | -52.54004 | 2024-11-28 03:59:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 42a56957-5608-3ae1-b9fe-f3812ec16c3c | -5.98377 | -45.36835 | 2024-11-28 03:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c92759d7-2223-3aba-8a80-8996c4b2f33d | -2.53634 | -47.3288 | 2024-11-28 03:59:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d883a8f-9d94-3e72-b1ae-4d0f8d47617d | -4.85768 | -42.66635 | 2024-11-28 03:59:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f33556d-5182-3038-aa8e-22a164a798e4 | -3.81176 | -47.46613 | 2024-11-28 03:59:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b916bc4b-89fd-33eb-8c14-1a9f0ebd787f | -6.36 | -47.06095 | 2024-11-28 03:59:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3ce3c707-fe12-3ce0-b10e-4b2c2cf97554 | -4.03248 | -46.5428 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a167d769-a100-33cf-8d34-8501cec7bdc6 | -4.38089 | -45.97182 | 2024-11-28 03:59:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2aac6da5-6d8a-3419-b51a-97d899d66868 | -2.87216 | -46.8411 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49724be6-c227-39a7-bc04-2ec5ae3811f9 | -3.17374 | -48.44195 | 2024-11-28 03:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0785f680-e474-30f8-ad9c-ef45a6a2be1d | -2.73103 | -48.89457 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 77465175-bbde-39a4-8b73-d91fc24fdf61 | -3.08682 | -49.21646 | 2024-11-28 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cd9ea310-5acf-3d40-baab-934b30a296b4 | -6.17653 | -42.61325 | 2024-11-28 03:59:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 21.4 |
| aea02480-5503-3fc4-abe6-dddf6acd255e | -6.12324 | -46.59025 | 2024-11-28 03:59:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 564d7ef8-f2a2-3766-a20a-34dcdd4ef15a | -4.20963 | -50.90083 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf19e73f-8b35-386d-ad98-2014cb057e90 | -4.05546 | -48.83406 | 2024-11-28 03:59:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ac299fd-9732-3f38-9a1c-208c71d5bd90 | -5.62135 | -38.12416 | 2024-11-28 03:59:00 | NPP-375D | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5acebb34-200e-3062-9330-b8bca8894582 | -6.17456 | -42.62537 | 2024-11-28 03:59:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 26619822-32e7-3025-9c69-1f372e175964 | -3.3817 | -50.11744 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5e5dc599-ea74-3ac8-a394-ecfda005badd | -3.38614 | -50.31888 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25b36587-4e06-314c-baa2-59ba17fd7070 | -4.12058 | -48.81566 | 2024-11-28 03:59:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce5de4e8-945d-3845-9b36-9c5a81245bf8 | -4.21314 | -50.89976 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8fa9d90-50ef-3110-abba-bce8a02bfeb1 | -4.17795 | -48.454 | 2024-11-28 03:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbfe80ac-30d2-3d16-8cb1-495cc4e6ea80 | -3.96088 | -50.18436 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 29cd7ead-c560-3a41-93ec-812638e22d33 | -3.13276 | -50.25781 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb84254e-1c03-3753-a436-06bf6cd8d915 | -5.979 | -45.3395 | 2024-11-28 04:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 78c4bbde-84a8-3057-935c-fccf7c1ee490 | 1.2538 | -55.927 | 2024-11-28 04:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| c7cd8469-0cbe-3015-b98c-11ec284993db | 1.2355 | -55.9272 | 2024-11-28 04:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| b20dce42-51b4-3690-93c4-0a45bab37e63 | -1.5897 | -52.271 | 2024-11-28 04:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 8b0f2d43-b596-3ac9-aff2-a1e0e19a8220 | -2.8609 | -46.8626 | 2024-11-28 04:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 37204852-7a84-37fd-ac73-edf69f16386d | -3.3837 | -50.1125 | 2024-11-28 04:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| b4a2c69c-bcab-3fbb-a928-45919ab4c6ab | -3.1113 | -53.8242 | 2024-11-28 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| bfe29044-bec0-3f94-8a96-ff5dcc10748b | -5.9788 | -45.3621 | 2024-11-28 04:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 1b90a38c-619a-382c-b0a5-156a61f6879c | 1.2537 | -55.9467 | 2024-11-28 04:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| fcc4a19e-ecff-3182-9efe-e4693ec3741b | -5.9975 | -45.3607 | 2024-11-28 04:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 39.3 |
| d0f949f2-a12d-3bdf-b7f2-fa552ded5f0f | -10.03163 | -36.27564 | 2024-11-28 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| f4db9e2b-d3b4-3a36-abf9-d6e4d631d441 | -7.82782 | -48.19143 | 2024-11-28 04:01:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8707d787-7c3e-331a-9aae-3126672bea42 | -8.1297 | -47.98527 | 2024-11-28 04:01:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| adef448b-09d4-3277-bea8-f91c278608cb | -10.03159 | -36.27389 | 2024-11-28 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 873f7946-b177-3ee4-ace0-3b26d264e622 | -8.12393 | -47.98976 | 2024-11-28 04:01:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 138c5f97-1bd0-3336-92b4-4c2ad779b22e | -8.56156 | -49.20301 | 2024-11-28 04:01:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ade42ea6-753b-30ed-9fa8-5d053671c45f | -15.93073 | -42.43311 | 2024-11-28 04:01:00 | NPP-375D | NOVORIZONTE | MINAS GERAIS | Brasil | 3145372 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f779ae6e-3c81-3eb3-9d31-ef0bcf31716d | -9.02742 | -44.03189 | 2024-11-28 04:01:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5cf67030-bed9-3832-9660-8c1828b220e5 | -10.03231 | -36.26903 | 2024-11-28 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 85caa257-eb14-380e-834f-930d4116822f | -7.8377 | -48.19309 | 2024-11-28 04:01:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af472574-5fc0-304d-914d-a52fb0855061 | -8.69166 | -47.96169 | 2024-11-28 04:01:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66233da0-3136-3c85-8a74-1aa705bac433 | -9.17341 | -44.72902 | 2024-11-28 04:01:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7094423-7099-36bf-a019-ef02ff993930 | -7.79556 | -50.00214 | 2024-11-28 04:01:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec67d02c-5806-3029-8bb1-cb4af25f4797 | -10.41403 | -49.24417 | 2024-11-28 04:01:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 119c1c13-3c7d-306e-9f68-40f6e410b3c3 | -9.17423 | -44.72421 | 2024-11-28 04:01:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4bd10d95-7da5-3593-a5b0-b2949d8d6f57 | -8.12486 | -47.98442 | 2024-11-28 04:01:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f2985251-6c16-309d-a4e3-b081734d10f5 | -9.17038 | -44.72358 | 2024-11-28 04:01:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f8b22b0-9cd8-3c33-996f-7751f1034f10 | -8.56709 | -49.20066 | 2024-11-28 04:01:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a760edf4-4b75-3d93-b9a7-5adda92a9c7a | -9.0791 | -49.58124 | 2024-11-28 04:01:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4f27451-9924-33bb-ba53-bbf36b576800 | -10.41459 | -49.2412 | 2024-11-28 04:01:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa58f426-636b-38ca-9175-32066bec4c44 | -9.17807 | -44.72484 | 2024-11-28 04:01:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 754a44a9-feef-3f1b-8d67-ed027c892f8c | -16.19935 | -43.38715 | 2024-11-28 04:01:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d06d881d-d790-3a41-879a-8880ab2754ab | -8.47751 | -47.81443 | 2024-11-28 04:01:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 086a90dc-724e-3c36-ae3b-b7002ab4a39b | -7.83276 | -48.19225 | 2024-11-28 04:01:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44c6d5b4-4f11-3a68-b58e-9c352a838b33 | -9.1712 | -44.7188 | 2024-11-28 04:01:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 444e7d73-c5b3-3e04-8000-71cf9765daf6 | -8.56677 | -49.20398 | 2024-11-28 04:01:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f76c3ace-6418-3c31-962b-eb7d3a1bc028 | -8.5665 | -49.20385 | 2024-11-28 04:01:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93477eca-b272-3ef3-8731-b8f923bbe458 | -9.10281 | -43.19381 | 2024-11-28 04:01:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 80e333a6-8410-3be9-ac2b-253a9ff0d057 | -9.0114 | -41.98159 | 2024-11-28 04:01:00 | NPP-375D | DOM INOCÊNCIO | PIAUÍ | Brasil | 2203453 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 26b140f3-5aa5-36f8-8314-ee05adac2508 | -8.56188 | -49.19972 | 2024-11-28 04:01:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62f222f9-f9f4-3a24-a070-00d8667cd472 | -7.8288 | -48.18587 | 2024-11-28 04:01:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01aa5827-654d-30b7-8824-901b6ba9073d | -8.12739 | -47.98605 | 2024-11-28 04:01:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b5091a34-b476-320e-a43f-e2d09e3deaca | -7.79622 | -49.99852 | 2024-11-28 04:01:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b8a7463-d160-3a82-a659-f06653a3cc75 | -9.09927 | -43.19319 | 2024-11-28 04:01:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6d9b570c-9b92-3a0e-9c94-6982bbafc1de | -10.41963 | -49.24227 | 2024-11-28 04:01:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| efd92e7d-dcf8-327c-bffb-8f04b1da74e9 | -8.08724 | -47.0645 | 2024-11-28 04:01:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c54c97a-746f-3bec-9cea-db4341079422 | -9.17504 | -44.71944 | 2024-11-28 04:01:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c18125be-b54d-30d5-a772-bf59724ab7f9 | -10.0362 | -36.27134 | 2024-11-28 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 0bf2f4aa-ad17-35db-a0cc-810d87ee5750 | -8.47275 | -47.81363 | 2024-11-28 04:01:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 138443c0-3657-398c-8bb7-4f1ca6381682 | -15.8902 | -46.0001 | 2024-11-28 04:01:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 833da611-56bd-33a8-b3ba-50f665036546 | -10.03548 | -36.2744 | 2024-11-28 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 431a5eac-a45d-3387-97e8-aa194d2ba420 | -8.12836 | -47.98077 | 2024-11-28 04:01:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21e96f0a-669a-3602-ae71-345602ecd245 | -9.07971 | -49.57793 | 2024-11-28 04:01:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f14b7dda-1c28-36bf-a6b6-aa455779250f | -10.65338 | -37.01541 | 2024-11-28 04:01:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d80702c3-1376-38dd-a0ab-4f5574a406a8 | -12.10076 | -49.48766 | 2024-11-28 04:01:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| abeaa405-4d86-3acd-8bf8-09a5df59cd4d | -8.54906 | -47.77257 | 2024-11-28 04:01:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30576325-d424-3d50-afda-73657b7a82c4 | -8.56129 | -49.2029 | 2024-11-28 04:01:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9161599-f70a-37d7-9afb-bc5cabb65734 | -8.56212 | -49.19983 | 2024-11-28 04:01:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07430d9a-9bf3-3609-93ea-58825499d1f4 | -7.94288 | -49.75616 | 2024-11-28 04:01:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88e4e903-40a6-3c56-bc37-9e9bab9ecff7 | -16.05073 | -43.79714 | 2024-11-28 04:01:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 79a25f14-38c7-3cda-8a7d-19914315bfb3 | -9.81358 | -48.16397 | 2024-11-28 04:01:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 727619b0-dbe7-3549-a9ca-ec4b45f83971 | -8.56734 | -49.20079 | 2024-11-28 04:01:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de631f55-907b-33b0-b143-732175b96386 | -15.2295 | -43.32916 | 2024-11-28 04:01:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4cb549e5-86e2-3cb7-94db-7832472adfcd | -10.03231 | -36.27078 | 2024-11-28 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 8cd115b5-cce4-38d7-91f8-c5c047391917 | -7.94835 | -49.7571 | 2024-11-28 04:01:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6dd6748-c720-3a6a-93bf-17677c395064 | -8.12642 | -47.99139 | 2024-11-28 04:01:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d8b68347-5687-39ae-8106-fd524472528b | -8.09103 | -47.06976 | 2024-11-28 04:01:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README41.md)
