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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94f2e2af-1c01-34e2-9791-c0db26fe2ee9 | -4.35959 | -45.86931 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2541b7f0-52da-3f31-b38f-74a44270f847 | -2.65793 | -46.1682 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0166e53-b487-39ea-91cc-b86071cabdc1 | -4.65265 | -45.12817 | 2024-11-16 04:23:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a577edc-5a9a-3615-a1eb-45ab65d4410b | -3.28069 | -46.2082 | 2024-11-16 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44c49eab-85b6-3b29-95a6-86576ba0824b | -5.32933 | -40.89844 | 2024-11-16 04:23:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7d90dc24-487f-362d-99a6-4b4f6cfee3b2 | -3.32761 | -51.65901 | 2024-11-16 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b6b8bdd-0411-3860-b4b3-75eb36ea8701 | -2.14933 | -46.4065 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5105358d-fd27-3c6e-93f4-a1371ea74bfb | -1.89772 | -47.00543 | 2024-11-16 04:23:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea801da5-73a1-3d35-9b05-de653b4c737d | -2.09718 | -46.33624 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ccfe204-b052-3889-9f16-d91da3aff5e5 | -5.21396 | -43.78952 | 2024-11-16 04:23:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e1e4c93-4ee2-341f-9956-68326b5edae6 | -5.21568 | -43.7931 | 2024-11-16 04:23:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 435a85d6-a764-3b86-a7ee-51f03142d09e | -5.14115 | -37.70353 | 2024-11-16 04:23:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7c856879-d0e8-3d33-83f2-ddf9544ad5b5 | -1.99366 | -46.57584 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9949df14-5547-3a88-bbb0-1b9a9a638926 | -2.77081 | -48.57553 | 2024-11-16 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 89314a95-95f2-33c0-9ccb-83ef3432e5b9 | -2.67435 | -46.84077 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09756f9a-6112-3446-9504-13c77365549c | -3.25254 | -46.53851 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1583755c-c5e0-37e8-bd2e-bd3cb22c84fd | -3.64353 | -43.01964 | 2024-11-16 04:23:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1dcd7741-3512-3d78-8b58-1281b40b3611 | -2.16465 | -48.90926 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6db57c73-408a-395d-82b5-3b5d554874e4 | -3.92001 | -46.40485 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| af9b6e13-a69a-3d01-b80c-a6c216ceeb94 | -3.69899 | -44.90465 | 2024-11-16 04:23:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7afd1ea2-0b52-3dfb-b132-aaeb0d26fd78 | -3.73704 | -45.65133 | 2024-11-16 04:23:00 | NPP-375D | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| cc8f6fcf-2e2b-30b9-aa89-c097cdc52db2 | -3.8941 | -50.07648 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d995f1bb-eb7d-3bbc-ae23-a1560ad2d6f4 | -5.14199 | -37.69777 | 2024-11-16 04:23:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bba557be-5946-3505-b1cd-8008968c9442 | -0.78737 | -49.48358 | 2024-11-16 04:23:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b44b64f3-f67f-3100-83e0-a5f6e30ff4eb | -3.89503 | -46.47623 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 515ec1fc-b014-3438-b342-347206859b04 | -2.15038 | -46.55281 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a728c05-eed1-31f5-acd6-eb07c768b92f | -2.4366 | -47.039 | 2024-11-16 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c9ffb3e-6201-3ad4-8459-b6d68a996311 | -2.21606 | -46.40963 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f9945dec-565b-3dd9-a5ae-49c46dec290b | -2.22522 | -48.37127 | 2024-11-16 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5153626c-a584-35c4-baa4-f0a8021e9408 | -3.75059 | -44.37735 | 2024-11-16 04:23:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| decbdf65-b298-3a8a-8d04-79c1103a6ccb | -2.90562 | -48.29392 | 2024-11-16 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22cdd996-f728-3164-9342-d5ff83e79a8e | -2.3892 | -47.94244 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6c29d18-1df2-3c85-afd6-7ddddf9e6b6e | -2.30634 | -48.47012 | 2024-11-16 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f7ad3c0-a37d-328b-b68f-ebf3c1957106 | -4.91645 | -44.78184 | 2024-11-16 04:23:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2bd02c8-0446-38e1-8f5c-7f2884be8e5a | -2.77013 | -48.57976 | 2024-11-16 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| df3e3f39-1db1-379e-ac36-ad90a0fcc4b9 | -3.94562 | -46.71223 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d1591d67-e4ba-3941-a9e6-28fcd9121059 | -2.63401 | -46.18954 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f657a070-4d83-3247-a11b-4ef1c274f6dc | -2.58619 | -47.47841 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2ad09e8-2088-3dd0-baee-ee27366235d6 | -2.2377 | -48.38612 | 2024-11-16 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4732832-fbab-3829-b93c-ddec4cc095e4 | -2.19376 | -46.6146 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f50cda4-31ea-3c18-be65-be31fac4d168 | -3.60389 | -44.80111 | 2024-11-16 04:23:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee2a2a46-c3db-3f56-9d48-c885050efb70 | -2.66354 | -46.19779 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cdba300-e417-349d-ab69-69d11e04c3a2 | -3.93141 | -42.40536 | 2024-11-16 04:23:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1a716c49-6337-3b71-801a-618644dccb9b | -4.36013 | -45.86585 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4ad23ce-d32a-3841-a60f-1e93d1ae68af | -2.64956 | -46.15612 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e07f769e-632c-3ba7-a602-b43761a83abe | -4.02955 | -44.10921 | 2024-11-16 04:23:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21f7d177-83de-313b-9140-dc9a514b4aeb | -3.04321 | -47.97936 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cdfa8982-37e0-3a5e-bbfb-4c0489284cd2 | -4.00449 | -44.33664 | 2024-11-16 04:23:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c053b63-9b04-3cf7-b53b-19a669911857 | -5.23774 | -44.91113 | 2024-11-16 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 21e7a4c5-ba34-31f7-9d84-205d5e076f73 | -3.26738 | -45.5002 | 2024-11-16 04:23:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 8ff18d95-7a98-3941-94b8-916d215b56b5 | -1.87039 | -54.27822 | 2024-11-16 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82497a79-5312-377b-bbb1-c8a26ffb39ea | -2.2247 | -53.61003 | 2024-11-16 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8489402c-e0b8-3334-8d8c-c40fcae767ea | -2.39105 | -46.31329 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2628a11f-ce74-3efd-9d16-1b6184366e38 | -4.22184 | -50.67619 | 2024-11-16 04:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ab16382-77a1-35f3-b9bf-4538d48f9e8d | -5.09862 | -42.73788 | 2024-11-16 04:23:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3dce5523-1a96-3eb2-9121-e57f7ce4f018 | -1.20876 | -53.56466 | 2024-11-16 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5d6dfd9-19d5-39b0-b375-5b6ce3d0395d | -1.73283 | -45.61708 | 2024-11-16 04:23:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2593e163-e225-3df6-b643-ed1d78ac91bf | -5.33795 | -40.89595 | 2024-11-16 04:23:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 298bb61a-d653-3aa8-a567-2567168ee563 | -3.99978 | -46.50058 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3c80202-8011-38e0-b68e-c11768a672a4 | -2.66747 | -49.12174 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6d59b7fb-f3a3-32f9-a75a-8e6432ed664a | -4.21009 | -45.61609 | 2024-11-16 04:23:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00ad8725-60da-3914-b928-acac203aaa15 | -2.4958 | -46.22861 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 298efb93-3d30-3c5c-99df-ad3b387a758f | -2.55419 | -46.89276 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| abe2a44b-4e0b-359e-9832-247fb0eaa9be | -2.85283 | -46.62163 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94b5ca15-0328-3831-a79e-bb2425914671 | -2.10949 | -46.41845 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5c10a25-c039-3a32-af5e-f381d79e7383 | -4.23973 | -48.34948 | 2024-11-16 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 653e73c1-bb0e-38c5-993c-2fd42325bfca | -3.96235 | -44.04752 | 2024-11-16 04:23:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1342c60e-4ba7-3658-9f7a-3f079bf4b615 | -3.49615 | -47.20604 | 2024-11-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7e297fb5-7085-3cfd-92c1-5598f7b72f03 | -4.73761 | -44.09329 | 2024-11-16 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd9f60c7-e5d5-39db-b84c-284f02f12f66 | -4.01251 | -44.58435 | 2024-11-16 04:23:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e02e8e09-1169-37b5-a908-1988f5e502d4 | -1.85908 | -54.27994 | 2024-11-16 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0eae0d0c-de01-3292-94fb-e5564dd95288 | -2.1583 | -46.41519 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd842100-cb48-383e-be25-8fe179caf7de | -3.10135 | -45.97297 | 2024-11-16 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b4c2dfd-ac75-307e-a0db-10d818c2e371 | -5.00458 | -44.32782 | 2024-11-16 04:23:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 249cef7a-4671-3cf8-8f1e-25f5d9363821 | -3.27401 | -45.50124 | 2024-11-16 04:23:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d20f8a0-47b1-3524-aecc-4d4a3f6844c6 | -3.20936 | -46.68094 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4789532-eb5a-3cba-8e22-13bb6b98c7da | -2.82972 | -46.6582 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34fed4ea-0d0a-3c94-9ced-6a63e6734db7 | -2.6682 | -49.11723 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a76c09c9-c65c-3d00-ab95-27feb781cb66 | -2.1723 | -48.32958 | 2024-11-16 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 052659b3-38ab-35a4-87c2-016586117cdb | -3.73873 | -45.6622 | 2024-11-16 04:23:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 8e32f93d-a7f0-39ec-a0b5-768191b71c79 | -2.61171 | -46.17888 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63d89ca5-d941-37ca-87cb-6f1a27c049a5 | -3.07407 | -48.01152 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5d825edf-6fdf-33cd-95af-fae153d23bd1 | -2.34492 | -47.46928 | 2024-11-16 04:23:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0991c130-380b-3af6-8091-90961659c63e | -2.44828 | -48.02447 | 2024-11-16 04:23:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5cd47354-32e1-3e23-a47d-5e925e138f5c | -2.17177 | -46.46103 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da60ebfd-1eb5-37e8-9867-65fd8d7b4b5b | -4.53181 | -48.64454 | 2024-11-16 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f37ed4c6-0ac3-3db5-a9ee-5818c7f4a8c9 | -2.67492 | -46.83715 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8c9351f-388b-3b3c-bb9c-eb9ef5488c78 | -3.84537 | -46.61636 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ac72bb8-14c0-3247-80f1-852d5e03b4dc | -3.18152 | -42.07452 | 2024-11-16 04:23:00 | NPP-375D | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29be40a5-2801-3a21-ab5f-df0bf6af0ce2 | -2.30754 | -48.55567 | 2024-11-16 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff3ece7a-9b99-3cf4-8412-87e9ed983947 | -3.97327 | -45.80843 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e03e028b-8b7d-3a9a-a282-eef7b57512b5 | -1.75005 | -50.47993 | 2024-11-16 04:23:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b096b7f3-a033-39bb-b736-984ee7cb2981 | -3.03394 | -45.1348 | 2024-11-16 04:23:00 | NPP-375D | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c96befd-1edf-344a-996e-da0f19ec3ffb | -5.67016 | -35.65182 | 2024-11-16 04:23:00 | NPP-375D | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 33da0b99-c1cc-364d-baab-2339765b8a8f | -3.88952 | -46.61963 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20473c56-852d-3b81-b77f-e63f555f412d | -3.65073 | -44.34782 | 2024-11-16 04:23:00 | NPP-375D | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d205682-939d-3b0f-9760-b351f8ba7527 | -3.62268 | -43.15507 | 2024-11-16 04:23:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9808c0f0-4516-3423-84f9-bc5202b1639f | -2.89976 | -45.34369 | 2024-11-16 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3b9e0b0d-096f-366b-9577-2f6778cbad12 | -3.1169 | -45.98251 | 2024-11-16 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0326ff71-9111-3dff-a0ba-0efd7bd9068b | -2.94674 | -48.01659 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README27.md)
