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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9ba7983-6032-3174-ad3a-69e36b1910f1 | -7.25111 | -43.0589 | 2026-01-14 04:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c79b766e-a8fb-326c-8348-a7d6363b57d8 | -4.69004 | -38.16381 | 2026-01-14 04:01:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c7aba80a-ec82-3de0-acd4-7c05eeb85cbe | -7.25952 | -43.05201 | 2026-01-14 04:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1edcab3f-e030-3904-ac58-e40d7d49786b | -5.8889 | -39.28748 | 2026-01-14 04:01:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a2ef89a2-de55-3325-9801-7f50d0391575 | -4.50163 | -38.43139 | 2026-01-14 04:01:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 93d064cb-ac60-3ba5-9d50-54b640831725 | -6.1391 | -35.1609 | 2026-01-14 04:01:00 | NOAA-20 | SENADOR GEORGINO AVELINO | RIO GRANDE DO NORTE | Brasil | 2413201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 487d5a3d-8fbe-38d6-aad3-1061e0b7e8b6 | -7.25597 | -43.05143 | 2026-01-14 04:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 49250359-4ca4-3f0e-ad93-7cd4174338df | -4.50218 | -38.42784 | 2026-01-14 04:01:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bbd5eece-3a66-3af1-aa87-787e9bc25b3e | -7.24402 | -43.05772 | 2026-01-14 04:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d1e4705e-51ec-3a16-a0ae-232cfdee3f34 | -5.10761 | -43.23931 | 2026-01-14 04:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb1cdf91-a546-31b1-953f-9d802ebd9274 | -6.5479 | -43.08781 | 2026-01-14 04:01:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89cb7d51-40c3-351d-9060-62ac1c09ff5b | -6.66421 | -39.66985 | 2026-01-14 04:01:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 02a85a51-4d15-3b7a-a2d7-2b2956086daf | -4.21051 | -38.12006 | 2026-01-14 04:01:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d8f41f7d-6f2a-3a17-804a-74a6db80a49c | -7.25243 | -43.05084 | 2026-01-14 04:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| afad5e2b-ad95-3c3b-9116-ec24680ee491 | -7.26306 | -43.05259 | 2026-01-14 04:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8f5fb9e5-4117-3bfd-8dd6-62f35d2e2534 | -6.27835 | -41.29035 | 2026-01-14 04:01:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 344ae2a1-fa8a-32ab-a09f-f4fae47c8991 | -6.12464 | -39.79787 | 2026-01-14 04:01:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 87a5191c-8b57-3751-974c-0fd0df5647dd | -6.95493 | -39.00701 | 2026-01-14 04:01:00 | NOAA-20 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6c90860e-d44f-3d9a-927b-65494e3985d7 | -5.1085 | -43.23637 | 2026-01-14 04:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f0182969-61e1-3f1a-9bab-a115c4cb034a | -4.21428 | -38.94443 | 2026-01-14 04:01:00 | NOAA-20 | GUARAMIRANGA | CEARÁ | Brasil | 2305100 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 01794a88-38e4-37b2-89af-e4d4741575ef | -5.10484 | -43.23573 | 2026-01-14 04:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9b79d718-55eb-3131-afd5-a7dabd24ff40 | -5.09979 | -43.24377 | 2026-01-14 04:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 514b0293-5150-3ac5-81e6-a4f977663501 | -5.17374 | -43.27229 | 2026-01-14 04:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 711891df-f2cb-34c8-8012-2481eb9b28eb | -6.58032 | -39.64238 | 2026-01-14 04:01:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4fd33eb7-0e59-33e1-8180-6cf436252f0a | -8.93124 | -42.95626 | 2026-01-14 04:01:00 | NOAA-20 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 69e8cb96-e7af-30a1-a071-2eebbd42bed4 | -6.54432 | -43.08722 | 2026-01-14 04:01:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d94d62ce-844a-3e7a-b9bb-b0ee8c960ec0 | -6.69227 | -39.12225 | 2026-01-14 04:01:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d7899ad9-2b57-30e1-ba29-4e36a2a11846 | -5.09682 | -43.23882 | 2026-01-14 04:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 42e73428-f0a8-34b3-a360-08e44c49519e | -6.73443 | -38.96175 | 2026-01-14 04:01:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a93ee018-812d-383b-abbf-27f84b44e899 | -6.54591 | -43.0904 | 2026-01-14 04:01:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8b618731-2a60-35e1-a1cc-afb41f689708 | -5.49721 | -39.16552 | 2026-01-14 04:01:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 50112cda-dd24-37a1-91fe-23224e570534 | -7.25886 | -43.05603 | 2026-01-14 04:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9829aa84-ccdb-3094-96d7-64fdb024a773 | -5.28679 | -45.82931 | 2026-01-14 04:01:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1358816-5d80-36ad-b24d-c22187a6b61d | -7.24468 | -43.0537 | 2026-01-14 04:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 28a3663d-4b41-34be-8a7c-7295bacbb198 | -7.34103 | -35.10428 | 2026-01-14 04:01:00 | NOAA-20 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 00c926f9-76d0-3159-b60f-15ce419bfd97 | -5.10048 | -43.23943 | 2026-01-14 04:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ce0ab85c-e9f5-3a73-b063-3f7a48954a5b | -5.08371 | -41.08991 | 2026-01-14 04:01:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fa80c793-a202-39f6-a09c-c23fc5363e1f | -8.5711 | -40.2849 | 2026-01-14 04:01:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 22a9e926-dc1d-3858-ad42-1d99d5250931 | -5.52445 | -37.77724 | 2026-01-14 04:01:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0d63826f-34c2-342b-ace1-dc10787ff888 | -5.10833 | -43.235 | 2026-01-14 04:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ea34fcc-39ea-3e15-b186-04d0672f0763 | -3.21727 | -39.68762 | 2026-01-14 04:01:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8a8c9003-ed01-3f40-a10c-1297a0794585 | -6.14308 | -35.16155 | 2026-01-14 04:01:00 | NOAA-20 | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 990d9bc4-8529-314b-bf09-2f7da44272b4 | -5.0865 | -41.09401 | 2026-01-14 04:01:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| aa6c352c-9c3e-3685-98ee-1c909d76ac53 | -7.17887 | -39.05223 | 2026-01-14 04:01:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1c338652-dfb7-31e0-9592-94beaa6a2242 | -7.15556 | -39.95715 | 2026-01-14 04:01:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4b9c307d-6768-36e7-b821-73765f42ef6e | -5.55322 | -42.73925 | 2026-01-14 04:01:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c4b23e2c-be98-3b18-ab01-10fa87b1e8cc | -3.89355 | -38.67243 | 2026-01-14 04:01:00 | NOAA-20 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4b774b9e-a1ed-3f2a-bb2b-7543cfebfe11 | -7.22379 | -35.05318 | 2026-01-14 04:01:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ab2fb8ab-b38c-3f8c-b605-bc9722358530 | -6.9769 | -40.95694 | 2026-01-14 04:01:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4dff65d6-8880-38bb-a2d2-2d6f2b6a951e | -5.3901 | -39.13452 | 2026-01-14 04:01:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 20e010af-148a-37e3-8be1-a1b7102e2127 | -7.2624 | -43.05661 | 2026-01-14 04:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 34220745-6952-3c8a-8876-56814a56554a | -4.92391 | -37.83251 | 2026-01-14 04:01:00 | NOAA-20 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f068d5b3-83a6-351a-ad89-617895a0b689 | -7.00936 | -39.65643 | 2026-01-14 04:01:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e7002c8f-aa71-3193-92ec-94bdcc91084b | -5.52503 | -38.92253 | 2026-01-14 04:01:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6bb2024f-a20d-3f7a-b11d-8ce016d17405 | -6.54367 | -43.0913 | 2026-01-14 04:01:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aeebca2b-bd9f-3ba0-acca-c0695cdc8b8d | -7.00882 | -39.65992 | 2026-01-14 04:01:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b87cd801-a71b-3876-a825-cf3c22b6baf1 | -6.66698 | -39.67387 | 2026-01-14 04:01:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 49e5fb6c-f7de-3786-9366-69b08ea952f9 | -3.89909 | -39.92967 | 2026-01-14 04:01:00 | NOAA-20 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| caa4a9c6-75e3-3c36-97fd-862b29abeed9 | -4.74689 | -43.24888 | 2026-01-14 04:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 93a51ff3-847d-38f2-99d2-f02e7669691c | -7.01654 | -39.65398 | 2026-01-14 04:01:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 40bb2441-bb51-3bb2-9d2f-0ecf2da77cb0 | -5.3486 | -42.90926 | 2026-01-14 04:01:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f7e80a7c-2965-3eed-992e-ac139909d11e | -7.25177 | -43.05487 | 2026-01-14 04:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| ea578ba7-4363-3743-bf7c-915a6234e608 | -6.48353 | -42.9439 | 2026-01-14 04:01:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7466955b-2017-38b6-8dc4-368fa68c2302 | -7.61005 | -38.26023 | 2026-01-14 04:01:00 | NOAA-20 | SANTANA DE MANGUEIRA | PARAÍBA | Brasil | 2513505 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cd8064f0-249c-3185-bb29-4a95670db6a4 | -3.96966 | -38.36029 | 2026-01-14 04:01:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 01c84ce4-6c9a-3715-b02c-f3d0a35cdfe7 | -7.24823 | -43.05429 | 2026-01-14 04:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| c50a2e50-d6bb-38d3-a0ab-2e74793ccc31 | -6.90318 | -37.8718 | 2026-01-14 04:01:00 | NOAA-20 | CAJAZEIRINHAS | PARAÍBA | Brasil | 2503753 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 304b4883-2df6-3ba9-9dc2-0673b1b5583b | -3.89688 | -38.67295 | 2026-01-14 04:01:00 | NOAA-20 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c3ebece8-6b14-3ebc-8c69-070b43e5f67e | -6.66644 | -39.67735 | 2026-01-14 04:01:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6e28f6ba-80d3-3780-abff-c01fc7cc8e14 | -6.12011 | -39.22013 | 2026-01-14 04:01:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5970bdb2-3140-3804-a91c-883b4827782d | -5.2104 | -37.28791 | 2026-01-14 04:01:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7253ffd7-af38-39df-b56b-8f2471c73869 | -7.27059 | -41.03265 | 2026-01-14 04:01:00 | NOAA-20 | BELÉM DO PIAUÍ | PIAUÍ | Brasil | 2201572 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1fafeba2-14ec-3b38-a46b-4769d003e1bb | -5.44252 | -40.86338 | 2026-01-14 04:01:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 008a7b22-dd34-3f74-9873-370967e1acc9 | -4.26002 | -38.06871 | 2026-01-14 04:01:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f7468a8e-b726-355c-bf9c-77f32e5ad37c | -7.46047 | -37.13549 | 2026-01-14 04:01:00 | NOAA-20 | ITAPETIM | PERNAMBUCO | Brasil | 2607703 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 797d007b-1f4b-3cd7-9626-e3e3cf008b0d | -4.73633 | -41.33079 | 2026-01-14 04:01:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 324d955a-adf5-3dc2-950e-7fbfeee94272 | -6.56618 | -39.42944 | 2026-01-14 04:01:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 392daacd-81b4-3011-956f-2d0ead3292a0 | -4.18033 | -38.10424 | 2026-01-14 04:01:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0af6974b-dae8-361d-a01a-3da2850ca261 | -6.59434 | -44.32758 | 2026-01-14 04:01:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e4790a46-6ec2-35c0-b293-c19901f28eae | -6.56286 | -39.42891 | 2026-01-14 04:01:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| df011e52-7f27-3cb7-a1d0-f68b70724e65 | -4.75058 | -43.24947 | 2026-01-14 04:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c0f7c966-184e-3206-83df-28e73ef1910b | -7.25465 | -43.05948 | 2026-01-14 04:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 49b8dec2-4f1f-3820-b8e2-893044714493 | -5.88504 | -39.29044 | 2026-01-14 04:01:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c39b4b42-9429-36f9-8620-3274ab4a545f | -7.2197 | -35.05267 | 2026-01-14 04:01:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8d03fa45-9570-338e-8b89-f31bd54a2e57 | -5.10118 | -43.2351 | 2026-01-14 04:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b6f9eef9-e7fc-3aa5-b561-88df5e730b59 | -5.88836 | -39.29096 | 2026-01-14 04:01:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b7ab2f9c-04d7-34b7-a540-1c1d0547c2df | -6.02291 | -44.54491 | 2026-01-14 04:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5366c375-40d8-36ac-8540-82ae1732dc14 | -9.00368 | -39.88719 | 2026-01-14 04:01:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4ca7d418-4e4d-30f3-95ac-70a14928541e | -4.78591 | -39.6493 | 2026-01-14 04:01:00 | NOAA-20 | MADALENA | CEARÁ | Brasil | 2307635 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c667f6f6-0bc2-3393-a2c0-30ef585704fd | -6.86143 | -42.26922 | 2026-01-14 04:01:00 | NOAA-20 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cb8c5f29-b846-39f4-ac8b-a1dbd7a38855 | -6.12066 | -39.21663 | 2026-01-14 04:01:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 64c8d436-7a6e-39be-a73a-ec2d650d1e22 | -12.113 | -45.57648 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb3eba9f-9db0-3ef9-8149-af2dbea1f866 | -15.25379 | -42.52182 | 2026-01-14 04:04:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5155e7f9-adb5-3f72-bf37-708b82dc4bea | -12.08641 | -45.57167 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35505c9c-d659-3dec-8665-26391159891a | -11.15772 | -43.57457 | 2026-01-14 04:04:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 440e302b-30d4-3deb-8088-20e955819995 | -12.1168 | -45.57717 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 698be7df-15da-334a-a6de-55ed74c637b3 | -11.85274 | -43.72897 | 2026-01-14 04:04:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7066ff00-97ec-3635-b76d-707621f2863d | -11.84991 | -43.72445 | 2026-01-14 04:04:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8bc7b15b-668e-35f2-995b-0669b6b66c35 | -11.16559 | -44.85152 | 2026-01-14 04:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 316fd236-42e5-3e6b-abdb-53833e68d821 | -11.99199 | -45.15143 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README5.md)
