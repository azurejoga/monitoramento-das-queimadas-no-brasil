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
| 68d613b8-d84d-31a2-b9a2-3e9be51b2231 | -10.58335 | -44.96916 | 2025-12-20 03:32:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc3520bf-5688-327a-9b6d-ddfa280297e9 | -9.98065 | -37.0387 | 2025-12-20 03:32:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 91dfb701-8bf0-3426-aa90-e3e16150c4e6 | -9.95756 | -36.52792 | 2025-12-20 03:32:00 | NOAA-20 | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 97269667-a0af-3ba2-81b4-5c6e4037b984 | -13.9587 | -43.27304 | 2025-12-20 03:32:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 451d7bd7-5f6a-30f8-b144-7ba19299bb83 | -17.397 | -42.12312 | 2025-12-20 03:34:00 | NOAA-20 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3b3adcdc-df2d-324c-954e-cb2707c0b9d7 | -19.72009 | -39.99815 | 2025-12-20 03:34:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 44f77656-ee73-323b-85b4-782c57551bf6 | -16.75034 | -42.36653 | 2025-12-20 03:34:00 | NOAA-20 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 515290fc-7f59-37e4-9fe1-5919cf509960 | -19.06212 | -40.55029 | 2025-12-20 03:34:00 | NOAA-20 | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 87b76149-fa27-3725-91ba-57d625243165 | -19.72009 | -40.00047 | 2025-12-20 03:34:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1ff2165b-548a-3510-9070-6fcd7b49a458 | -19.06182 | -40.54954 | 2025-12-20 03:34:00 | NOAA-20 | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 536653e0-5e4f-3e51-8562-02bf9607ab72 | -19.06615 | -40.55123 | 2025-12-20 03:34:00 | NOAA-20 | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 71e1bc39-601b-31a0-acdc-6ca5a3a7da19 | -16.75017 | -42.36639 | 2025-12-20 03:34:00 | NOAA-20 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 99084989-9f86-38ed-8495-b1e6a288fded | -19.06585 | -40.55047 | 2025-12-20 03:34:00 | NOAA-20 | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8cf31e36-e827-30b7-9dea-bd6dbb42f532 | -16.74561 | -42.36549 | 2025-12-20 03:34:00 | NOAA-20 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0fcc47a7-7da8-351d-a3e5-643fb8fe5810 | -28.26053 | -48.86777 | 2025-12-20 03:36:00 | NOAA-20 | IMARUÍ | SANTA CATARINA | Brasil | 4207205 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7fd8927e-6eaa-31f0-bf2e-3fabefb11768 | -28.25945 | -48.87214 | 2025-12-20 03:36:00 | NOAA-20 | IMARUÍ | SANTA CATARINA | Brasil | 4207205 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e3728d4a-34ef-3698-968e-92efd4f891e9 | -3.8631 | -40.653 | 2025-12-20 03:40:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 60.6 |
| 78e85498-0768-3e63-a0be-6043f92fdb9b | -3.8631 | -40.653 | 2025-12-20 03:50:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 56.4 |
| f26f275d-53ba-3cf8-a59b-99f468c1d0f2 | -2.97293 | -40.03828 | 2025-12-20 04:21:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e8d117e1-3702-3166-8bf0-9d02baad8d53 | -8.04553 | -40.00776 | 2025-12-20 04:21:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 35dffb0f-5b23-3f37-aa12-3c7132a7c2dd | -4.1753 | -40.71654 | 2025-12-20 04:21:00 | NOAA-21 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| a0cef2a6-3874-3818-9fa7-3d89352fe77b | -5.84744 | -40.34275 | 2025-12-20 04:21:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3efb0078-4e5d-3aa2-9170-4b664649f0c3 | -4.91744 | -37.44399 | 2025-12-20 04:21:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 641b1df8-c171-3d18-9237-fefbf9d422fd | -6.9944 | -38.69826 | 2025-12-20 04:21:00 | NOAA-21 | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 32447cff-0e93-352e-bef3-9a2c56074115 | -1.06595 | -47.08072 | 2025-12-20 04:21:00 | NOAA-21 | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55c8c09c-a972-3aa8-85a0-1b0f72b66459 | -8.62751 | -37.00111 | 2025-12-20 04:21:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b763b550-cd33-331b-bf07-d7db97f0561d | -5.31585 | -37.60777 | 2025-12-20 04:21:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a8faac9e-a4e3-3015-9a17-035aa444f962 | -2.19439 | -45.72383 | 2025-12-20 04:21:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e748523a-ff0e-346f-9c70-141c0bcf46c4 | -6.10969 | -40.79029 | 2025-12-20 04:21:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 44bd6610-b906-33f3-8c4d-34ae53df10eb | -3.60428 | -38.93815 | 2025-12-20 04:21:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b359648e-6beb-307e-93e4-571e1be0d35b | -2.82487 | -46.71616 | 2025-12-20 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efbdb171-e7c0-3e5a-91a0-7554da133b1c | -5.99103 | -39.11473 | 2025-12-20 04:21:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b594e9f4-14fc-30dc-b029-f4e656be3312 | -8.25841 | -35.8283 | 2025-12-20 04:21:00 | NOAA-21 | BEZERROS | PERNAMBUCO | Brasil | 2601904 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c3a0d569-63af-36bf-bd23-716bea3e7f13 | -5.74289 | -36.30671 | 2025-12-20 04:21:00 | NOAA-21 | FERNANDO PEDROZA | RIO GRANDE DO NORTE | Brasil | 2403756 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2391b320-a1c5-38ff-b714-03bda70c9813 | -4.91831 | -37.44133 | 2025-12-20 04:21:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f6cb9ba6-5a2a-371d-a174-2f0e57b851c6 | -4.08413 | -38.23101 | 2025-12-20 04:21:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 6b001d8d-3ebe-3b3d-a4ed-9fdaf39a1af2 | -5.11049 | -40.7394 | 2025-12-20 04:21:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6e171e8c-8410-389b-8f7f-46d490cc4dd3 | -4.12158 | -40.82286 | 2025-12-20 04:21:00 | NOAA-21 | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b81b1db1-9c82-3f87-a7b3-fec5a069d46d | -5.38402 | -39.68269 | 2025-12-20 04:21:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3f83b410-6db2-315a-af0a-824c05902a1d | -5.65694 | -39.72909 | 2025-12-20 04:21:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cff41021-ebb2-3d0d-a274-680076074d07 | -5.31845 | -40.61929 | 2025-12-20 04:21:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 72fe97af-7cf1-3210-ad62-8802096248f8 | -8.62688 | -37.00429 | 2025-12-20 04:21:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1d088d02-da0e-331f-954b-225335fc31ff | -5.46021 | -40.4981 | 2025-12-20 04:21:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 823b07d1-b408-3366-acd8-0c51b83ae51d | -5.22803 | -38.16495 | 2025-12-20 04:21:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 460d9e58-657a-3f47-98f4-fae6ff276cfb | -3.86068 | -40.64354 | 2025-12-20 04:21:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 16.0 |
| e075701e-cb4a-3324-8df3-f09f25a850a5 | -4.74086 | -40.75718 | 2025-12-20 04:21:00 | NOAA-21 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 38ea418c-c8fb-348f-936e-68fd8750c243 | -3.22016 | -41.97554 | 2025-12-20 04:21:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5874837c-31b7-3107-8b01-53ed236eb550 | -4.08474 | -38.22693 | 2025-12-20 04:21:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 73ad6cc1-e305-3963-9f65-ab766bd79fb7 | -6.30301 | -41.88306 | 2025-12-20 04:21:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 06e52301-8e59-33a5-aee1-396d47ce2bfe | -3.86369 | -40.64843 | 2025-12-20 04:21:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 777ca958-dfd5-3768-bfd1-420c83854d54 | -2.97223 | -40.04282 | 2025-12-20 04:21:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4fe71404-7eb8-3ca1-8ffd-b4bd6e7a949d | -4.73808 | -40.75839 | 2025-12-20 04:21:00 | NOAA-21 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a9e9c1c8-7097-302d-9ede-d6950bc37d15 | -3.86001 | -40.64789 | 2025-12-20 04:21:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5c7aab81-52c8-3a55-8ab4-271296a5c41b | -5.22828 | -38.16279 | 2025-12-20 04:21:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b69883ad-7058-37fa-964c-1a68093e18f9 | -4.9283 | -38.09123 | 2025-12-20 04:21:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 768ade3b-2baa-3fab-bc1e-362b594d9301 | -5.98734 | -41.88602 | 2025-12-20 04:21:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| aaa89a9b-80cc-3d77-bf4d-5b23a6daf9cf | -3.25175 | -41.42363 | 2025-12-20 04:21:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2cf5f3ce-d804-3beb-8b5c-417c1bb238d7 | -2.99228 | -40.34591 | 2025-12-20 04:21:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0e04c11c-0c44-30cd-b8b6-01159c297a4a | -1.17236 | -46.13462 | 2025-12-20 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1bc47a5d-2c8f-3d7b-a111-9a8bc6b9fd16 | -7.22229 | -40.13727 | 2025-12-20 04:21:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ed67aeee-a677-33a7-b491-bd20088afb0c | -7.39949 | -35.23423 | 2025-12-20 04:21:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ca5849bc-bd8b-3649-a943-5a8b3473befb | -4.96289 | -40.58372 | 2025-12-20 04:21:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8376b6e6-b107-3d9e-9c6c-8eabb493d038 | -1.16886 | -46.13407 | 2025-12-20 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c856d3f-1430-3916-96f9-78d12470f032 | -3.90233 | -40.68779 | 2025-12-20 04:21:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2eb336b0-0325-3452-99b1-d83f1634d210 | -9.41024 | -35.94054 | 2025-12-20 04:21:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 47269e95-a91d-333d-9120-c79925b81bdb | -9.40479 | -35.93976 | 2025-12-20 04:21:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| afc6e34c-3fb5-3b61-9d51-fcd778704844 | -5.07995 | -37.64769 | 2025-12-20 04:21:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 7fd11569-2b5d-3889-8528-f6bde5d8f4a4 | -4.91371 | -37.44062 | 2025-12-20 04:21:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0f24200c-1ba6-3bb5-981b-a82916b41f92 | -3.25115 | -41.42755 | 2025-12-20 04:21:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 24e3dd16-2ea4-313f-b3e1-02f971b8effc | -1.95117 | -46.32717 | 2025-12-20 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f9c89f5-86cc-3859-a6c2-b0a2a44d2cc0 | -4.65429 | -40.73676 | 2025-12-20 04:21:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 16d1ec10-d382-35a4-a223-1153b17a0452 | -5.464 | -40.49868 | 2025-12-20 04:21:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ddaef30e-2abe-36e9-aca5-9bab783f9c4a | -4.08904 | -38.22757 | 2025-12-20 04:21:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| dc7b471b-fd97-39ba-9f28-273d6b536ede | -2.98858 | -40.34532 | 2025-12-20 04:21:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c5504355-e819-3a02-9203-411348d36bb8 | -3.56258 | -47.1818 | 2025-12-20 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7eea8149-349a-3567-9147-cc81928b8147 | -2.96185 | -40.30733 | 2025-12-20 04:21:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 188c0125-9db9-3663-9ea9-561dfc8ac72f | -1.6121 | -45.18655 | 2025-12-20 04:21:00 | NOAA-21 | BACURI | MARANHÃO | Brasil | 2101301 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b58a84a8-076e-3885-979d-182332fd1745 | -8.62711 | -37.00399 | 2025-12-20 04:21:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 23f399fc-7a6d-3d3f-b69b-dabfc43c70c7 | -5.65474 | -39.72911 | 2025-12-20 04:21:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b5053169-44db-3f8d-b380-40840d036911 | -8.62763 | -36.99851 | 2025-12-20 04:21:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7474d9e5-cf2f-34ba-a192-38b8ddbf9edb | -4.55157 | -37.93 | 2025-12-20 04:21:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ef887cfd-0458-3b34-aafd-8e990ed766f7 | -9.07169 | -35.59734 | 2025-12-20 04:21:00 | NOAA-21 | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 70380df4-24fb-3b65-adc2-c2ec049f1644 | -1.48563 | -45.92199 | 2025-12-20 04:21:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c31d850f-b538-3aee-a80e-3d8743640bd2 | -1.03825 | -46.82919 | 2025-12-20 04:21:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c5116cc-873f-3f02-aa6a-f7752149dabe | -2.16719 | -45.96392 | 2025-12-20 04:21:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65031a46-2e15-3748-903c-0e97e5a1d916 | -4.31977 | -38.12914 | 2025-12-20 04:21:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 11e24dce-a965-30d6-a2f7-db7a82fbab16 | -4.40703 | -40.69505 | 2025-12-20 04:21:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 932ad95c-7f6b-3ded-9e49-cc7b6dd69fbe | -8.62726 | -37.00141 | 2025-12-20 04:21:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d4f415a9-8ddf-33dd-9f71-9bc4b327e994 | -6.2396 | -40.30064 | 2025-12-20 04:21:00 | NOAA-21 | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 36edc5a6-a834-3225-a379-c6add6021056 | -5.93378 | -39.05926 | 2025-12-20 04:21:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f78debc2-e44d-3ddc-919a-f4568b16f6a2 | -5.56926 | -39.10034 | 2025-12-20 04:21:00 | NOAA-21 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a2015323-666e-3742-b1e6-9e9e55da975d | -5.23268 | -38.16347 | 2025-12-20 04:21:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4d3be30b-e81e-3aca-a494-5547e8a5e2d5 | -4.33621 | -39.36394 | 2025-12-20 04:21:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0123b42d-0d2d-3fa9-9b42-7278f872af23 | -6.72001 | -40.00059 | 2025-12-20 04:21:00 | NOAA-21 | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b2fd6e0e-735a-34e7-930e-6adacfe32634 | -6.59192 | -39.6473 | 2025-12-20 04:21:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d0ec682f-16f3-3664-9892-9b8badbb414a | -5.92511 | -42.27842 | 2025-12-20 04:21:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f46caf16-08bd-37df-ac72-0827f9547a88 | -5.5698 | -39.09662 | 2025-12-20 04:21:00 | NOAA-21 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 39acedec-9a7b-34d9-a048-2d0de898cb15 | -1.88733 | -46.26961 | 2025-12-20 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 454c0cd9-24ed-3aa9-b651-6443ab087b65 | -5.92388 | -42.27526 | 2025-12-20 04:21:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 663e4e32-0de1-329c-b7ec-722892df15a2 | -7.22092 | -40.13833 | 2025-12-20 04:21:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README4.md)
