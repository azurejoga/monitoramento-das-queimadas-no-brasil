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
| 34cee193-405e-35dd-b3d6-345d9616cca2 | -6.1877 | -39.22894 | 2024-11-05 03:17:00 | NOAA-20 | QUIXELÔ | CEARÁ | Brasil | 2311355 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 16d8498d-227c-306b-8b4f-7b9af348314d | -11.85683 | -43.87516 | 2024-11-05 03:17:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 02a17000-0581-3390-9eaf-a7e1adf71e10 | -6.50696 | -41.41666 | 2024-11-05 03:17:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d73179ff-18ec-32ef-a4f1-35ac6ac3cade | -10.26957 | -36.32085 | 2024-11-05 03:17:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| bc948875-2a22-3f3c-aab5-b80a7581a63f | -9.52929 | -40.34526 | 2024-11-05 03:17:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b716b133-2996-3183-b68f-7501dc8280c2 | -9.86371 | -36.41013 | 2024-11-05 03:17:00 | NOAA-20 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 75a05617-1290-3008-9f6f-b2a844d146d7 | -5.85761 | -42.66267 | 2024-11-05 03:17:00 | NOAA-20 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f1938093-b763-3ec9-a89f-5c63968952fa | -9.57696 | -37.81765 | 2024-11-05 03:17:00 | NOAA-20 | PIRANHAS | ALAGOAS | Brasil | 2707107 | 27 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 98ee2528-f971-37e7-8063-e6c5b19ef46a | -6.4879 | -39.97072 | 2024-11-05 03:17:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 16499211-0232-38b5-81a8-1a7f5d855d23 | -6.98497 | -37.32825 | 2024-11-05 03:17:00 | NOAA-20 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6a2d4550-50a1-3010-ad0a-0cd83cdee964 | -7.54103 | -35.13321 | 2024-11-05 03:17:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8dab5fae-dba8-367b-ae0f-106fe63c7fb6 | -6.67311 | -37.46534 | 2024-11-05 03:17:00 | NOAA-20 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a2085c98-bebb-3824-b56a-e01b4aee9a83 | -6.18815 | -39.22752 | 2024-11-05 03:17:00 | NOAA-20 | QUIXELÔ | CEARÁ | Brasil | 2311355 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 27a2247c-2d0f-3116-8903-547e75e4ff67 | -6.44209 | -35.06269 | 2024-11-05 03:17:00 | NOAA-20 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f92cd198-f95d-3758-9a8c-f9d0d40e5926 | -7.04073 | -38.724 | 2024-11-05 03:17:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0027ce3b-bd32-3f44-a2aa-70aab0990943 | -6.19275 | -39.23414 | 2024-11-05 03:17:00 | NOAA-20 | QUIXELÔ | CEARÁ | Brasil | 2311355 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a3622b46-7d66-399d-9827-dcbe1c990ec9 | -6.67365 | -37.46229 | 2024-11-05 03:17:00 | NOAA-20 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5313354a-f59e-356c-ba0f-a64a20bf276a | -6.50588 | -41.42252 | 2024-11-05 03:17:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 99c6305e-e513-3a89-8ddb-a7f06259aa73 | -11.85463 | -43.87998 | 2024-11-05 03:17:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7494e657-e497-3d69-9d0d-0749fdb54255 | -6.48594 | -39.97296 | 2024-11-05 03:17:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d4710fd1-08fb-3738-b668-fedab2f359f0 | -10.27401 | -36.32167 | 2024-11-05 03:17:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 29.8 |
| b6037f48-3772-38b6-83a5-f473433acbe8 | -8.13604 | -35.3308 | 2024-11-05 03:17:00 | NOAA-20 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e50a4df6-29bc-3bc4-abb1-766602b6f4e9 | -7.2932 | -35.18507 | 2024-11-05 03:17:00 | NOAA-20 | SÃO MIGUEL DE TAIPU | PARAÍBA | Brasil | 2515005 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b711b4f0-f16a-34cf-8d3c-0f30f652f421 | -11.85544 | -43.88187 | 2024-11-05 03:17:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 010d0293-fc33-37cc-af13-0ce16626c4ea | -7.04126 | -38.72178 | 2024-11-05 03:17:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3da8cf31-d33c-3079-a4a1-154872ee8c70 | -5.93302 | -42.67166 | 2024-11-05 03:17:00 | NOAA-20 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6a4110a6-af6a-321d-aee3-e416dd9cf634 | -7.19321 | -38.82311 | 2024-11-05 03:17:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9053f388-7fad-3a7f-8ed8-c1274b6e45c8 | -6.69783 | -37.47431 | 2024-11-05 03:17:00 | NOAA-20 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c8bc3107-7289-369f-844c-9b211395189f | -15.02483 | -42.28674 | 2024-11-05 03:17:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7f63e1a7-9737-3852-89a2-ae79acc64dee | -8.45526 | -35.11395 | 2024-11-05 03:17:00 | NOAA-20 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e72d518d-c596-3e98-90e8-65ea80ca6335 | -9.8719 | -36.41622 | 2024-11-05 03:17:00 | NOAA-20 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| c178b2a2-e3fa-3026-9954-892640f5b7df | -6.1884 | -39.22494 | 2024-11-05 03:17:00 | NOAA-20 | QUIXELÔ | CEARÁ | Brasil | 2311355 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 25a3da86-05c5-3bc0-89d8-05cfa0bffd87 | -6.44713 | -35.05927 | 2024-11-05 03:17:00 | NOAA-20 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a3b37af6-33d6-3d78-9cdc-f64ef5ce8644 | -6.51364 | -41.41729 | 2024-11-05 03:17:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 723aa535-7d9e-3acc-92e9-61a2f8ec15a6 | -6.53485 | -35.15448 | 2024-11-05 03:17:00 | NOAA-20 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e48bd8d6-5478-36e2-a3d5-dfbcbb6eac8f | -6.44279 | -35.05853 | 2024-11-05 03:17:00 | NOAA-20 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ca842370-6554-34c9-bb2d-b1b72692b9e4 | -6.19244 | -39.23668 | 2024-11-05 03:17:00 | NOAA-20 | QUIXELÔ | CEARÁ | Brasil | 2311355 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 834a7fdb-fb67-3253-9232-d65af7e09b39 | -5.85397 | -39.4233 | 2024-11-05 03:17:00 | NOAA-20 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| f7187596-e700-35a7-b82e-8113f3f7652d | -8.05041 | -38.01802 | 2024-11-05 03:17:00 | NOAA-20 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 6ee3103c-2547-351c-a851-eb139d66e04f | -9.86822 | -36.41086 | 2024-11-05 03:17:00 | NOAA-20 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 17.0 |
| 8d88363d-81a1-3030-aa41-216a6da54eb6 | -9.8674 | -36.41541 | 2024-11-05 03:17:00 | NOAA-20 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 3e7162f3-88dd-3525-a7f6-727d4e5a7f25 | -7.25528 | -38.94999 | 2024-11-05 03:17:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3d1892ab-b1c9-3b71-9793-a8666fd90971 | -7.38082 | -34.90037 | 2024-11-05 03:17:00 | NOAA-20 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 32697cc3-1927-39b6-bb77-0f633fc2919b | -6.44643 | -35.06343 | 2024-11-05 03:17:00 | NOAA-20 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 27a7acfb-8289-3b85-9a4b-39c90d3d4264 | -6.47988 | -39.97206 | 2024-11-05 03:17:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| df780217-fb45-307f-9a8d-c9084f2640a9 | -6.67415 | -37.45943 | 2024-11-05 03:17:00 | NOAA-20 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c708c75c-888d-3b3a-829d-750e06ec86ce | -5.85503 | -39.42645 | 2024-11-05 03:17:00 | NOAA-20 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| f8c6462c-c316-3a14-b526-a191d5d8c23c | -7.38148 | -34.89637 | 2024-11-05 03:17:00 | NOAA-20 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| c9ef2182-519e-3109-af43-6e9ab5567e3f | -8.13675 | -35.32666 | 2024-11-05 03:17:00 | NOAA-20 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 8b13070f-4a2c-35a6-b57c-dcf953c635e9 | -11.98037 | -42.90506 | 2024-11-05 03:17:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 04212ddb-a8ec-3489-a547-a0792248277c | -7.55475 | -38.76888 | 2024-11-05 03:17:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3b39430b-8a00-3c8a-bbac-78fa9031100c | -8.04984 | -38.02114 | 2024-11-05 03:17:00 | NOAA-20 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4f339668-654a-3e63-83f4-f8075b1daa88 | -6.48706 | -39.97527 | 2024-11-05 03:17:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 50ef245d-27bb-392b-afd8-d544e85099ef | -12.29682 | -40.91058 | 2024-11-05 03:17:00 | NOAA-20 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 94580542-d99b-3462-b355-8e15907d1d79 | -12.74194 | -41.82619 | 2024-11-05 03:19:00 | NOAA-20 | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2dbf659f-f973-3dd0-954f-713e2d9d475b | -4.8582 | -42.9332 | 2024-11-05 03:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 56a6492b-8de4-3c02-9e60-a3d8c1665418 | -2.6506 | -48.5844 | 2024-11-05 03:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 1ad76b42-facb-3cb2-ab7d-2a139b11ed33 | -3.4934 | -50.3819 | 2024-11-05 03:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 120e0291-feec-3cd5-bf5a-b8d1f8763d09 | -2.6691 | -48.5624 | 2024-11-05 03:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| b6c3dfec-a6c1-30a7-8111-8594307936c2 | -3.967 | -48.15 | 2024-11-05 03:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 9f7cc1fe-53a7-3b9b-b728-6312bc661fea | -4.606 | -46.8758 | 2024-11-05 03:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 68.0 |
| f6264c42-8f45-3c4b-b64e-460d6b18cdc1 | -4.858 | -42.9566 | 2024-11-05 03:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 03987ce0-c974-3140-911e-436beca7934f | -6.1229 | -43.9578 | 2024-11-05 03:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 435485b3-0f43-3156-9680-be897f21f94c | -2.6507 | -48.5629 | 2024-11-05 03:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 20086802-804c-3c98-b84d-b79234aebc4f | -4.0667 | -46.9246 | 2024-11-05 03:20:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 59.0 |
| c134d252-de78-3cd0-9b96-5177e7988561 | -6.1041 | -43.9593 | 2024-11-05 03:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 82447259-b5b8-3528-9278-80e943f7dac3 | -4.2243 | -48.5482 | 2024-11-05 03:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 963d6825-00a7-3d78-945f-3591544ea5b0 | -2.6507 | -48.5414 | 2024-11-05 03:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 2d23658d-9abb-33db-8081-4ea228781fe4 | -2.1173 | -54.6472 | 2024-11-05 03:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 19b037a6-84f5-3e02-beed-37a7cba9d573 | -2.6506 | -48.5844 | 2024-11-05 03:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| e83a5d8c-392b-300d-a5f3-941f07828915 | -4.858 | -42.9566 | 2024-11-05 03:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 41.4 |
| cfb60243-7a0e-355f-8912-c12282bbc672 | -6.1041 | -43.9593 | 2024-11-05 03:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 4766c202-f2f4-3619-bbbe-0c1035308913 | -4.0667 | -46.9246 | 2024-11-05 03:30:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 57.7 |
| fef8a5bd-4149-3b67-96eb-e42a8a48ddd0 | -4.606 | -46.8758 | 2024-11-05 03:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 46.7 |
| c1fa8990-269f-38d4-b9e6-8af9613c0f2d | -2.1174 | -54.6272 | 2024-11-05 03:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| cdacb81a-f6f8-3ed3-b25d-dfdcb5e81a46 | -2.1357 | -54.6269 | 2024-11-05 03:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| f32ede1a-f805-3c04-b44a-4b3b088d9fd6 | -2.6507 | -48.5629 | 2024-11-05 03:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 144.1 |
| cf4476f8-c910-3b36-97e4-6d41e60fac3f | -2.1357 | -54.6469 | 2024-11-05 03:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| bc8812ba-b560-339a-bf67-a73e222ef8dc | -6.1043 | -43.9362 | 2024-11-05 03:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 13ea30f4-6593-371a-9898-0deef8b0189a | -2.6691 | -48.5624 | 2024-11-05 03:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 037fea71-1ac4-3711-961d-eccf3b3cd5a4 | -6.1229 | -43.9578 | 2024-11-05 03:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 374b94e6-17ad-3ff9-a0c5-fe9ab4d96945 | -2.6691 | -48.5624 | 2024-11-05 03:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 016d31bc-e81a-36d1-8f32-ab26cc275245 | -4.0666 | -46.9466 | 2024-11-05 03:40:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 6b6c61b0-12ac-390e-b9eb-df2a9e93a46a | -6.1039 | -43.9824 | 2024-11-05 03:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 354a8619-9140-339c-a0e9-c029dc0c56a9 | -3.563 | -47.4066 | 2024-11-05 03:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 432d0763-6510-3b29-86da-a26da3ae0248 | -3.5444 | -47.4073 | 2024-11-05 03:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 8e5a9f5a-2fa5-3efb-b071-82bfad873cd7 | -6.1041 | -43.9593 | 2024-11-05 03:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 1ba5c087-9607-3afa-bbe7-b821e3ac54a2 | -6.1229 | -43.9578 | 2024-11-05 03:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 1e17a590-b519-336c-a105-44a77b8c869b | -2.6507 | -48.5629 | 2024-11-05 03:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 2e59f835-a6e2-38f6-8b9b-22f32721ceae | -3.5631 | -47.3847 | 2024-11-05 03:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 284.1 |
| 5feb4703-3f5b-38a4-85aa-8eafbbb7b9a4 | -3.5446 | -47.3855 | 2024-11-05 03:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 344.8 |
| 3e6f0a92-85aa-3a35-9041-3e6471acab7f | -3.5447 | -47.3636 | 2024-11-05 03:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 0c5b811d-0a4c-3a18-b6cf-656eb9eb6c19 | -2.6506 | -48.5844 | 2024-11-05 03:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 571f377f-7918-3c92-8a0f-17e257a7a7fd | -3.5632 | -47.3629 | 2024-11-05 03:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| cdde788e-9a4b-35f8-8127-de2b363c7f4e | -2.1174 | -54.6272 | 2024-11-05 03:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 1cb53d51-fd4a-3ce6-a2a0-c91c6fa2b72a | -3.563 | -47.4066 | 2024-11-05 03:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 45faeb6c-d90c-3909-a2f7-5c9d6122d71f | -2.82 | -52.9409 | 2024-11-05 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 642012dc-2933-3066-9632-0ed4db00cb41 | -2.6691 | -48.5624 | 2024-11-05 03:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 8d6f7fbf-9597-3113-9acb-f73d3006772f | -2.6506 | -48.5844 | 2024-11-05 03:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 6d2c751f-b891-3c65-af5e-7f863f9a8906 | -3.5447 | -47.3636 | 2024-11-05 03:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 110.0 |


[Clique aqui para ver as próximas entradas](README12.md)
