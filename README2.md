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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9756f546-4f55-3a80-8c48-7e11f9577ebd | -6.74092 | -44.99168 | 2025-06-09 03:45:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cad4cf0b-0d00-3a7e-9c7d-3a44db55511c | -5.12354 | -37.78801 | 2025-06-09 03:45:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d2d61325-5ba2-31c0-84d2-9a3cecd2f41a | -7.01362 | -44.6082 | 2025-06-09 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1e296a62-25e4-3282-a453-f4cc14c8f606 | -5.12112 | -37.79017 | 2025-06-09 03:45:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f8062afa-12d1-37bb-8bdd-0d2268c69a34 | -7.86695 | -47.89999 | 2025-06-09 03:45:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31efe9b4-0470-3abd-b2a8-474528909fe5 | -7.01835 | -44.61269 | 2025-06-09 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e4a86143-e46b-37ea-a8ec-6bb3b0736873 | -7.00692 | -44.6146 | 2025-06-09 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bcd8c513-a344-3450-90d0-5ea7ac39f10e | -10.64334 | -44.4826 | 2025-06-09 03:45:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a26f9fa9-7496-3782-8d87-8954b4e1b49d | -4.48629 | -43.7758 | 2025-06-09 03:45:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ee990b7c-47c0-3fd1-91aa-8dbb4bf34191 | -8.96257 | -47.96877 | 2025-06-09 03:45:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9515939b-73e2-3622-9ade-c2e4b7cf0548 | -7.27674 | -44.22282 | 2025-06-09 03:45:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e152605-eadb-3e64-9d4c-98292125dce7 | -7.01239 | -44.61497 | 2025-06-09 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3a4a0e3c-edf5-3102-8fa2-946550122acc | -8.96214 | -47.97174 | 2025-06-09 03:45:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d67b8fa3-bee8-34dc-829a-a1d67da255e3 | -10.28044 | -46.99248 | 2025-06-09 03:45:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2d05245-345e-3e4b-a6b5-940f185c2749 | -5.63332 | -43.7255 | 2025-06-09 03:45:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 46c4fd4d-b3a7-36ea-815a-63d0eac5140c | -7.59002 | -45.994 | 2025-06-09 03:45:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c8de310e-58b3-3e4c-a885-c14433da5112 | -7.01715 | -44.61932 | 2025-06-09 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 784d5dad-2b97-3133-908e-ab9624c2313a | -7.01783 | -44.58487 | 2025-06-09 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0db9cb69-bc3d-3145-bedc-a1a103477b54 | -10.2532 | -46.9115 | 2025-06-09 03:45:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18060789-b980-3171-9896-641013ece799 | -7.86838 | -47.89949 | 2025-06-09 03:45:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6e52d1e-5990-3d97-b022-639e0cd44f77 | -8.07485 | -34.97704 | 2025-06-09 03:45:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8cb1567b-177c-3f0a-b2a7-34afa0b3fe4c | -8.96155 | -47.97419 | 2025-06-09 03:45:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d224c180-68d9-333e-995d-258723d5d290 | -7.02381 | -44.58235 | 2025-06-09 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3496fb1b-e747-3b50-9577-e01ec3690efb | -10.27366 | -46.9958 | 2025-06-09 03:45:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6ab01ed2-a65f-3f87-a591-2896f6d883a5 | -5.11996 | -37.78742 | 2025-06-09 03:45:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f76c620e-1be5-34bc-acca-4856da90011a | -7.0226 | -44.58909 | 2025-06-09 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 086a5e0f-1c1c-31d8-a553-5f68dc845dce | -7.27617 | -44.22596 | 2025-06-09 03:45:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19077959-d92a-3f33-bb61-4fb6dc15afe9 | -7.01663 | -44.59152 | 2025-06-09 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 51c1ddf3-ed09-3af7-804a-002490bb27ac | -7.01423 | -44.60484 | 2025-06-09 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 754d6596-34a0-32ed-8839-9226ed6f2081 | -7.65313 | -46.10223 | 2025-06-09 03:45:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5fed1edc-321f-3feb-a00e-f22670a20301 | -7.27788 | -44.21658 | 2025-06-09 03:45:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06821d58-84bf-3bdd-b0e2-2608a88c481b | -10.26686 | -46.99927 | 2025-06-09 03:45:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 28c194c4-3807-3f84-a094-9466b7aecee6 | -7.00818 | -44.60764 | 2025-06-09 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| be17e3b2-2b41-3af7-8c86-c10a501b9b2b | -7.01301 | -44.61158 | 2025-06-09 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9c50ac08-0805-35a9-833e-b7f88600ba9a | -7.27711 | -44.22152 | 2025-06-09 03:45:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5382a24-b11a-378b-91e3-d16807138b25 | -7.01115 | -44.62185 | 2025-06-09 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8c91e65c-2ab2-341c-a115-caf2b981263a | -7.27656 | -44.22466 | 2025-06-09 03:45:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dbb303b0-2143-3481-ab7b-75e6470ea4bc | -11.37198 | -39.07455 | 2025-06-09 03:45:00 | NPP-375D | ARACI | BAHIA | Brasil | 2902104 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2e8a5530-9a6a-3563-bee1-77b3da049a41 | -7.65898 | -46.10328 | 2025-06-09 03:45:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c0b30e6-be84-3bc2-b8e3-33fc69a8540b | -7.0063 | -44.61804 | 2025-06-09 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7701f851-ed2b-3bce-be17-e5a824000cf7 | -10.64834 | -44.48352 | 2025-06-09 03:45:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d5e95d42-bae3-36e7-abea-527f0eaaf6ca | -7.27097 | -44.22503 | 2025-06-09 03:45:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 222292f6-36d4-3c53-aec7-fd269da0d5a8 | -11.37552 | -39.07515 | 2025-06-09 03:45:00 | NPP-375D | ARACI | BAHIA | Brasil | 2902104 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7ae4d15b-dcc2-377a-bd8b-a9c4915986cd | -7.01895 | -44.60935 | 2025-06-09 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 84eaab19-2f86-32f4-b1cb-c8221aa71a42 | -7.27081 | -44.22686 | 2025-06-09 03:45:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a345d66-6855-310d-813e-2db7bbc93d62 | -7.01775 | -44.616 | 2025-06-09 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b5204b0d-c164-3f67-81a4-a531629c297a | -7.02504 | -44.57554 | 2025-06-09 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c73d5c6d-4d0d-3f14-8925-a246cc049beb | -10.25238 | -46.9157 | 2025-06-09 03:45:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55cffce8-fbe2-38d5-9e31-370cdfb9acf9 | -7.86943 | -47.89386 | 2025-06-09 03:45:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be6b006f-70b4-3db1-a894-9ca3e4958212 | -10.27284 | -47.00011 | 2025-06-09 03:45:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 98b68111-7708-3ff7-a53d-6a50c8f06f40 | -9.07692 | -47.15248 | 2025-06-09 03:45:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ae4644d-ffef-3366-a53c-e7e09a374568 | -7.01967 | -44.57466 | 2025-06-09 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e3c1869c-b3fe-3cc0-a196-c34b3bc43c89 | -6.74026 | -44.99534 | 2025-06-09 03:45:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c2e2be23-31c7-3e00-a73f-c79632038cc1 | -7.27765 | -44.21839 | 2025-06-09 03:45:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28884ace-fd1a-3f00-b364-608a2217ff1d | -9.07718 | -47.15371 | 2025-06-09 03:45:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3cf827ac-9419-31fe-aaf9-4771154dc94f | -7.01604 | -44.5948 | 2025-06-09 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 89c49fdc-5204-3e65-bb58-73b3c60acc75 | -10.24652 | -46.91441 | 2025-06-09 03:45:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe30a3cf-a751-31f0-8ea1-e7bfe3baed4f | -7.47723 | -34.8441 | 2025-06-09 03:45:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 14c6a094-426d-3259-8bfe-25f7352f9b62 | -4.49159 | -43.77671 | 2025-06-09 03:45:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| adfd36ce-1c55-31ff-922b-3e365e87773f | -5.63369 | -43.72546 | 2025-06-09 03:45:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb3823f6-c147-32eb-aa26-d98414571156 | -7.27135 | -44.22371 | 2025-06-09 03:45:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6744de44-93a2-39a3-9d2a-cf66293b73df | -7.86804 | -47.8944 | 2025-06-09 03:45:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 87a2b1db-0c31-3c1e-af60-538d50a5a14a | -7.58421 | -45.9929 | 2025-06-09 03:45:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e698fe09-658e-36ad-b5d1-e93f981ccf64 | -7.01905 | -44.57809 | 2025-06-09 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e7c4bdcb-3549-3c88-a3e4-2bb713d2f6d4 | -5.16984 | -37.60485 | 2025-06-09 03:45:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d079daff-16d7-3198-8439-b0639e270c27 | -7.01177 | -44.61841 | 2025-06-09 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e2ed7b01-5725-3e54-bdee-131fcbfdb3b9 | -9.07784 | -47.14777 | 2025-06-09 03:45:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bd2e1fc-d825-37ed-a2c5-d89309602f27 | -7.01723 | -44.58821 | 2025-06-09 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a0b9b1e-c2e6-3d6f-b2b5-96ba41272a3d | -9.07807 | -47.14898 | 2025-06-09 03:45:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e220cf2-5ad2-3f39-be7c-3f60c8845302 | -13.55862 | -44.19948 | 2025-06-09 03:47:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a41fbf4f-d3c9-3047-9dd6-47aa894e5a63 | -13.50626 | -47.85731 | 2025-06-09 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17e4229a-1366-37af-b152-a699f17e01d5 | -18.05876 | -39.91586 | 2025-06-09 03:47:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a7259725-3311-3fd6-b279-3abe71ff3031 | -13.50528 | -47.86207 | 2025-06-09 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 780b269a-dc61-3f44-8f9b-507d58ce9dc7 | -18.03962 | -39.92438 | 2025-06-09 03:47:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a78840f8-e935-346e-b96e-c320b8a2994e | -17.09419 | -43.8065 | 2025-06-09 03:47:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67cedca9-b55a-3285-a4ed-9126a80f2a6e | -14.23499 | -45.47678 | 2025-06-09 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db405475-abca-3dff-98c2-b411439f737c | -14.23385 | -45.48265 | 2025-06-09 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd17e557-d3c2-3950-b3cf-ca885a1c2774 | -13.93625 | -47.20752 | 2025-06-09 03:47:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f0056f91-3d16-3e5d-96cf-7c356960f8a0 | -18.77341 | -40.90109 | 2025-06-09 03:47:00 | NPP-375D | BARRA DE SÃO FRANCISCO | ESPÍRITO SANTO | Brasil | 3200904 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b61846d0-a4ab-3872-8363-aad7676dd193 | -13.02177 | -47.86792 | 2025-06-09 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b41f31a-9c44-35b0-9721-795943ad9dba | -13.93918 | -47.20704 | 2025-06-09 03:47:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6e1ec39-8180-35ea-8482-3b774020ea89 | -14.24384 | -45.48476 | 2025-06-09 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b5984848-4f23-34ca-a664-3106e46d3b8f | -12.54855 | -45.42589 | 2025-06-09 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9f27bd51-e255-385a-ba36-0ea615f1b270 | -15.0946 | -44.81452 | 2025-06-09 03:47:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55346127-a1aa-3797-a258-d52d2d513aa0 | -13.55398 | -44.19848 | 2025-06-09 03:47:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23a987b6-640c-3eb5-9b47-57423785b1f6 | -14.9361 | -42.2873 | 2025-06-09 03:47:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b3cb520a-bfc6-3b04-8cfd-be3a8cd41e40 | -13.01741 | -47.868 | 2025-06-09 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97e4ac7c-747e-39d4-a72c-7e3319bb2c77 | -12.54665 | -45.41621 | 2025-06-09 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7fcb7b05-e02a-3c21-a22c-b466583dbcf6 | -14.2477 | -45.4917 | 2025-06-09 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cdd3196b-0211-31e6-ae3f-bab56f6f6486 | -18.05533 | -39.91521 | 2025-06-09 03:47:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 98fd2205-0d54-3e56-ae85-2d56974ca810 | -13.93841 | -47.21085 | 2025-06-09 03:47:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62946595-e4dd-3a6b-8022-da6aa7053a48 | -12.54459 | -45.4186 | 2025-06-09 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a745f9a7-1859-39c8-a168-7abd25150d6e | -14.24677 | -45.49253 | 2025-06-09 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e559719b-4d77-3a77-9ddd-e23d204e48b2 | -14.23885 | -45.4837 | 2025-06-09 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 372cb8f6-3331-317c-b28b-8c2fbce4408a | -14.23997 | -45.47784 | 2025-06-09 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f160c019-07c7-37bf-a80d-aa5ce19e7553 | -16.69266 | -41.01844 | 2025-06-09 03:47:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 01cc0db5-3108-36aa-b3d4-89fe15fe68a7 | -17.77759 | -42.81166 | 2025-06-09 03:47:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b27b72d7-6413-3eba-b6c1-f474df5b3eec | -17.77856 | -42.80628 | 2025-06-09 03:47:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e4a65373-0c1f-37ee-b98b-b3e741036f33 | -12.54971 | -45.41969 | 2025-06-09 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9be1dd08-f214-3ad5-b73a-6d12c2a91a92 | -15.83536 | -42.59405 | 2025-06-09 03:47:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |


[Clique aqui para ver as próximas entradas](README3.md)
