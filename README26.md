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
| 35585b47-b7dd-3dc9-8d79-3bedbc608ddd | 0.99538 | -50.26569 | 2024-11-29 04:04:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5c7a0b2-5490-3e78-87f4-37d2d87ad242 | -6.01848 | -43.74179 | 2024-11-29 04:04:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e234f5b-af5e-3edc-b81f-a6217cb90d4f | -6.86342 | -38.57193 | 2024-11-29 04:04:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 24e46a47-1dfe-3c83-b4c0-c9f8c91f181b | -3.4662 | -50.53945 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d4ce958-6f87-3ca6-862c-bd04779bd181 | -1.58021 | -53.84396 | 2024-11-29 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 8b3f50b9-0dea-381c-9f95-a33614c0cb4f | -2.66681 | -48.78468 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24f7720a-759f-3c70-ac16-27d26dcda3fd | -2.3014 | -51.99531 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e812dbbe-b0eb-3cae-9587-acfeaaa4d9a9 | -3.1255 | -49.40799 | 2024-11-29 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0aa2efe1-715d-39a1-b230-185caa79c1fd | -4.72344 | -43.25239 | 2024-11-29 04:04:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3ef07756-0788-3a2e-a850-6641fe2933d0 | -1.91642 | -52.89767 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5f544fb-b2ce-3589-92bc-7e5e557903a6 | -3.24499 | -50.77798 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c494b972-5c49-339b-93e0-55c0ae18bcb5 | -2.94004 | -48.33645 | 2024-11-29 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a68da5f5-972d-34f6-92bb-5df0f07ea1a2 | -0.95119 | -51.65499 | 2024-11-29 04:04:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94e18fd9-b6c4-3353-a759-ac85d384aeb0 | -2.95863 | -53.72845 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d8ff2843-84f8-3324-8532-63c142b56387 | -3.95056 | -46.72752 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3b9b2b9-46de-3f6f-855e-8b2927721bb1 | -4.01925 | -46.99583 | 2024-11-29 04:04:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 768adc67-ba08-39c9-b9b0-17827eda64b4 | -1.13842 | -48.33641 | 2024-11-29 04:04:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 169d5793-4e84-31d0-980e-9e4d5c2708ce | 0.94099 | -50.73952 | 2024-11-29 04:04:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e71380d5-f55a-32c6-8a4e-03be5488b1ce | -2.86244 | -45.54509 | 2024-11-29 04:04:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c3d520fd-9257-34b8-9845-56243590e9a2 | -4.81952 | -44.35491 | 2024-11-29 04:04:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76ffe79c-627a-3d03-9a38-0a846ce407f0 | -2.65634 | -48.78587 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 0ae9fee9-b376-33fb-949f-c54c58d9dcc9 | -3.13068 | -49.40891 | 2024-11-29 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 368e4977-fa66-3917-8618-ba1538d01f44 | -6.16437 | -44.42455 | 2024-11-29 04:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02d3500e-53d8-37f4-9902-ac7243a896a3 | -2.98208 | -53.29842 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 30807b81-828b-3e0a-9ff1-3c4c9b21be27 | -2.25476 | -53.74638 | 2024-11-29 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 656b1fd7-e72c-3654-823b-93a0d82ba138 | -3.93558 | -46.71243 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 434269f4-0b79-38a3-b85a-6ba266695d77 | -3.84356 | -46.53392 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48e25e8d-5692-35f3-ab00-9aa2e63c3b07 | -1.70491 | -52.76788 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8cdb8c4e-5a2c-3fc4-bd86-5d77b616fa6b | -3.81187 | -44.05208 | 2024-11-29 04:04:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0bc5bbc9-1367-333c-8c2d-9bc9ccc3cc7c | -4.73066 | -46.67393 | 2024-11-29 04:04:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27916c1b-774b-3354-9585-afd816e91515 | 0.93958 | -50.74176 | 2024-11-29 04:04:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea24ffd8-d12c-3944-bf62-ac257ec107d7 | -3.1724 | -48.43991 | 2024-11-29 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ee5d66c0-c342-3972-ba93-63e61d26e84d | -5.54866 | -45.20001 | 2024-11-29 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 05ec227a-2424-3d9f-90b3-b7bc2c83791b | -2.22783 | -53.6958 | 2024-11-29 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ea70e28b-d729-35b7-88e0-0deeab6ebe81 | -3.83999 | -46.52945 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35802053-6511-324b-a7dd-b2141a620ce7 | -2.57913 | -48.08324 | 2024-11-29 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a47327b-4eb7-337f-b8d2-34094d6a789e | 0.0369 | -51.11326 | 2024-11-29 04:04:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c955a4de-9f9c-32ec-be43-54da440013cf | -3.23999 | -50.77313 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c784573-0002-355d-862e-75da7ab3d993 | -3.14613 | -49.21549 | 2024-11-29 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae145936-ba80-31fb-9dc8-32f274b03da3 | -5.39531 | -44.31729 | 2024-11-29 04:04:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a06b070d-7f22-3932-a255-fbaf6784a2d0 | -4.97947 | -43.91316 | 2024-11-29 04:04:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef60aac7-14c3-3fb9-9915-047d8cbc06af | -3.81996 | -46.59795 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c11663e-637f-3043-9319-87207e669477 | -2.64137 | -47.12941 | 2024-11-29 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1924e48d-92d6-3fe1-83fc-1e6271164c68 | -3.64373 | -49.40078 | 2024-11-29 04:04:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3676b460-d180-3ffa-a3c6-5c62d00dcb63 | -4.17052 | -48.61102 | 2024-11-29 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ff132dc6-992a-3ff7-b7d7-596a579243df | -3.9473 | -46.69422 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| acd8e0a4-6a00-3716-aed3-8ca532c56ad9 | -4.30302 | -48.23484 | 2024-11-29 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7bbfb58-0435-36a2-855e-ae256f73dc13 | -3.70356 | -50.51223 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6aac5700-7d67-38d0-bf09-044711873a62 | -0.47434 | -48.63556 | 2024-11-29 04:04:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56518838-9b37-3529-afdd-03cc9758cba6 | -2.70651 | -46.12082 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb655a35-97fd-3783-9113-8230dd25f4a6 | -1.71228 | -52.77407 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 19d8f309-5b0d-3f04-85c8-312c9f329439 | -2.73089 | -48.89537 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 53a04b29-c0c6-354b-afe7-31078dd20557 | -3.87223 | -48.36874 | 2024-11-29 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 22a3fa1a-3ed8-342f-994f-928b5568eec3 | -6.03056 | -38.12321 | 2024-11-29 04:04:00 | NOAA-20 | FRANCISCO DANTAS | RIO GRANDE DO NORTE | Brasil | 2403905 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8a39bd23-422d-3929-a488-c58319322433 | -3.2642 | -49.89861 | 2024-11-29 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 8aadbb52-43c6-34aa-8521-3e99f265afe8 | -3.09945 | -53.82476 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ffdf34e-f212-3a4c-ba01-cab50d7cbf57 | -5.21697 | -41.28186 | 2024-11-29 04:04:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| efcf8ee3-def1-3f89-88ce-aaee9f80f86c | -2.84407 | -46.81876 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad2a999d-b1cc-3403-b3db-c41fb811c6a9 | -2.38382 | -48.60295 | 2024-11-29 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8e9e9d0-bcac-32ec-8d23-7019f54cdf56 | -3.86009 | -50.1284 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b61547d6-c886-328d-8407-c7de929fc33f | -4.28268 | -46.29733 | 2024-11-29 04:04:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 238d4ca8-7c8d-3937-a3b8-95e446ae0836 | -3.17314 | -48.58423 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 24811b5b-2cc0-37a4-ac28-4a1aea4bcda2 | -3.55129 | -42.16353 | 2024-11-29 04:04:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b2b0c17b-80d5-30d9-9f16-e2bdfdab5675 | 0.03822 | -51.11671 | 2024-11-29 04:04:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d08ac219-0259-3c1e-a98f-8b50885e46c2 | -3.07869 | -50.25463 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93f740a7-8c0e-3bd3-b6fd-7e27b8f03bce | -1.53577 | -52.66644 | 2024-11-29 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0827f325-0970-33ac-ba83-8c366e255cf7 | -4.92971 | -44.52847 | 2024-11-29 04:04:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3af66955-2f89-36c6-9cb8-6edd12d7dca6 | -3.32846 | -50.21959 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 13e23b27-448e-3cc1-8f4d-cc1f5f887c9b | -1.03582 | -51.74166 | 2024-11-29 04:04:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5865f38e-e8bd-3015-b605-bf0d760a2918 | -3.16662 | -51.09776 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59bd775b-c5a1-344a-9bca-74181ab7271b | -3.14493 | -46.59675 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17e17df2-7182-3f8a-93e5-6ee9c6777f73 | -1.68817 | -52.43224 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4db9fe5-1365-3ffa-8ec3-428563e3dac4 | -2.84392 | -46.87487 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 750bb34e-4723-30ed-8dc1-340ae248bf29 | -3.88524 | -46.67717 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 931ecda4-096a-33ac-9313-145387300b00 | -3.10177 | -53.81167 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3538cc0c-3f7c-3005-98c9-0b1b31f094b6 | -5.1963 | -44.24992 | 2024-11-29 04:04:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 326beeb3-3885-33bc-81dd-0527138bf26b | -1.08222 | -53.38857 | 2024-11-29 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2143d7a5-9ed0-32b4-bad3-751ff2deaba6 | -3.27218 | -50.61783 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c49036c-b13b-36e3-b2a4-a0f494512462 | -3.14932 | -49.43148 | 2024-11-29 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a994865-516e-336a-a9df-94b43f6c0ddd | -3.24676 | -50.59802 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79c2654b-5a0d-3193-a9c6-d34cdc8745a3 | -0.05114 | -50.8324 | 2024-11-29 04:04:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b2dd699-15db-3848-82f1-4fda0b586fb0 | -3.79532 | -50.13683 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5826caa6-ae05-3526-843c-078b9b92255a | -4.8534 | -41.25926 | 2024-11-29 04:04:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 38c4eb16-dca5-3677-80f1-6a5fdca696f1 | -3.46184 | -43.52847 | 2024-11-29 04:04:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 080869f9-6497-3285-a5c3-75301365e88e | -5.5618 | -42.87774 | 2024-11-29 04:04:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6cdc75d0-f916-3140-88b9-3552e3818ae4 | -3.93624 | -46.70844 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aff66ca1-b2e8-36f7-9af5-a1f837ca6dc1 | -3.26171 | -49.89461 | 2024-11-29 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 441322e3-48e0-3d27-a230-a2201c299e33 | -4.65564 | -46.54896 | 2024-11-29 04:04:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce41770d-11d4-3490-8478-74ead4e21266 | -5.60203 | -41.44463 | 2024-11-29 04:04:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f9e94e37-8790-3121-8f3c-f06856dc6b1f | -3.27537 | -50.59904 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81c69474-f118-3720-a254-fd1b72c9adad | -3.31349 | -52.15359 | 2024-11-29 04:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 59571777-252e-3867-b961-b682d54d8956 | -5.16827 | -46.16478 | 2024-11-29 04:04:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 79cbc32b-06fb-3d7f-b58a-579a570f5dac | -3.10063 | -53.81813 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 072bf59a-e6ac-3349-9f03-d6d14bd95b92 | -3.97026 | -47.23957 | 2024-11-29 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 67b0b6fb-ad51-37ea-acb4-0320baa52f10 | -3.70342 | -47.13486 | 2024-11-29 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3bdb71db-fa42-3f73-aa7e-9e307fde94d7 | -2.83705 | -46.69825 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07f92625-a65f-3e4d-b751-893abbad4133 | -3.17442 | -46.30386 | 2024-11-29 04:04:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88171c06-d335-3189-bdc6-7d630be01441 | -3.60965 | -50.19246 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1e13464a-a735-35c7-a88e-f6b1b1417a7c | -4.75166 | -38.52411 | 2024-11-29 04:04:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f83cbddc-dec0-34e0-816b-e4414733739a | -3.22268 | -46.30307 | 2024-11-29 04:04:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README27.md)
