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
| 35373988-e02c-3bc8-b073-0019a078c088 | -20.39599 | -48.85603 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 499d3654-5a04-3277-8e7d-0a887614daf3 | -20.39565 | -48.83501 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 55.9 |
| cdc33523-129d-3d7b-bcf3-e7d3c79defed | -20.39544 | -48.8846 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2586092-6430-3148-a990-15a25360b549 | -20.39489 | -48.83494 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 86.6 |
| fe8f58ca-a359-3b59-82e9-78965aa4c86e | -20.39479 | -48.83899 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 3cdd31c2-f9c1-3713-b72e-0e1154201c8b | -20.39459 | -48.88841 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e85a5bc8-a34a-3c0e-ad54-c0fc20ed7375 | -20.39401 | -48.83892 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 145.8 |
| e70875da-17e6-3a16-8020-63d3aac9a00c | -20.39308 | -48.84698 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 115.3 |
| abac746c-d2f3-30dc-b60c-8c8a0f6018b3 | -20.39223 | -48.84688 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 76.3 |
| f82dde20-ef5d-32f8-ae30-6ec52475328a | -20.39141 | -48.85474 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 91e331ee-8003-3c5c-ba87-f0df2dd67a00 | -20.86548 | -48.46653 | 2024-10-08 03:45:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f62f7c1d-9ed8-345c-9378-f87a382695c4 | -20.86471 | -48.47011 | 2024-10-08 03:45:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35870d4e-0e6c-3296-b1f3-4c944a12c319 | -20.5735 | -48.49532 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a34cd09-f348-3963-b352-679cff81e50e | -20.57271 | -48.49888 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8487f27-5ffd-32fb-b031-2154569089c2 | -20.57171 | -48.49557 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24fc5b12-e95b-39d0-beef-37c50eafc3e9 | -20.37296 | -48.82948 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c4708445-0293-317f-a992-3e44f01b3455 | -20.37144 | -48.86216 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 233.5 |
| c2b0ae4f-9479-315f-94ec-a91ff6b9c497 | -20.37125 | -48.84091 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 0616753f-51fe-3a98-b8a3-8c8165a782ca | -20.3687 | -48.79944 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cf391615-24ab-35fb-8efd-84fee58ac3eb | -20.36776 | -48.85272 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 380.9 |
| eae67887-8bd9-30a6-ba4a-7b0fcd9d444c | -20.36744 | -48.83181 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 45.3 |
| a8c75e79-b4c4-3491-bddb-1c7890852798 | -20.36702 | -48.80717 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d4351088-f8a6-3c46-bd48-5bd3a37a78f9 | -20.3662 | -48.81093 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2494a5cf-94ec-3346-9070-5ad69c16e346 | -20.36536 | -48.81478 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| acd98b29-2cc2-36ca-9ac6-8421daa70d65 | -20.36493 | -48.84339 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 107.4 |
| bd1436a6-0429-31bb-8d50-57173f42360d | -20.36407 | -48.84735 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 6d179951-2589-3b6a-bdf6-5d134d24061b | -20.3624 | -48.80184 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ba184333-a5e4-3a19-99e5-7974e79fafb2 | -20.36156 | -48.80569 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 09780dc5-5928-375f-a8d4-b3faae0ff676 | -20.35906 | -48.81718 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3cf7bece-5d4a-3aa7-9617-fd0f42dfe339 | -20.35654 | -48.82874 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 770021ff-3a5e-3507-b5a1-60b24e487a88 | -20.35341 | -48.86975 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| da8ac76e-142d-3bcd-898b-5279bbb50723 | -20.35278 | -48.8195 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fa049cf1-f043-3ef9-9aa8-512b357bb0bc | -20.34853 | -48.83895 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df6fabf1-42c3-38b0-8733-4870ae9339b8 | -20.34768 | -48.84283 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ab39141-ca09-3e17-9d31-bf50bc739194 | -20.34706 | -48.87226 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0c249435-d537-37d9-aaa6-a3427db7a3b8 | -20.34509 | -48.85474 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9137c651-9eed-31da-ad1d-d9d6ed87572a | -20.34216 | -48.84163 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b001afb-e810-3a65-8806-3abb8fe66da9 | -20.37329 | -48.80487 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83de2ca6-6721-354d-955c-86b52eb0b49e | -20.37165 | -48.8124 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a01f771-3c58-3b80-82ea-c0bf2e224549 | -20.36784 | -48.80336 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fb434573-75a9-324a-9d39-48f740dfc137 | -20.36661 | -48.83562 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 5d305bdf-58e5-344e-a50e-9a22ff1070f3 | -20.36578 | -48.83948 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 6be06649-67b4-3c0d-9ffd-b94bc131070f | -20.36366 | -48.82261 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5298254f-f064-3422-9b06-03589b690bce | -20.36116 | -48.83412 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 328fa946-5f73-3702-b369-50ea515382db | -20.35822 | -48.82107 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 945f4a89-9160-30ad-be39-bbc89bfd0f0d | -20.35571 | -48.83258 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 871e01bd-c7ba-38c6-a2af-2f609fb664b0 | -20.35023 | -48.83118 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1cb8c185-f839-3f27-8493-44605f5357b4 | -20.34302 | -48.83771 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d4980df-0f4b-3bc8-9673-1fa92677adeb | -20.37042 | -48.84474 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 411604d1-727c-34d7-a577-cf80d0fbd9c6 | -20.36955 | -48.8447 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 306e970b-1cfc-36b8-9ade-a573a07f2fff | -21.06581 | -47.22877 | 2024-10-08 03:45:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 287ec214-4647-3938-8911-361b30b4e8ff | -21.06538 | -47.2349 | 2024-10-08 03:45:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 719f6929-91b9-3b4d-819d-748e69d6c1b2 | -21.06471 | -47.23412 | 2024-10-08 03:45:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4db2076d-f0c6-30c7-afdd-c6f38d653334 | -20.9085 | -47.41204 | 2024-10-08 03:45:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59b701ac-b4e8-38f0-a65e-89e94395c7cc | -20.90414 | -47.40788 | 2024-10-08 03:45:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7a7231b5-2823-3523-b392-313b89b139ea | -20.69127 | -47.60122 | 2024-10-08 03:45:00 | NOAA-20 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06a6c9d0-9f97-38c2-968c-e1d228872b99 | -20.68693 | -47.59663 | 2024-10-08 03:45:00 | NOAA-20 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 864b0038-3862-3394-941f-55e6852a91b7 | -20.68063 | -47.18409 | 2024-10-08 03:45:00 | NOAA-20 | ITIRAPUÃ | SÃO PAULO | Brasil | 3523701 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aac65801-6312-3a8d-917b-00bc96a26c28 | -20.45165 | -47.62619 | 2024-10-08 03:45:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e25a5cfa-9a6f-3f96-bf8f-314d8044b8e6 | -20.45094 | -47.62948 | 2024-10-08 03:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7cc97c31-f084-3e98-937e-23bec6ac7e54 | -20.43287 | -47.66375 | 2024-10-08 03:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10f3a2b7-2362-372f-abb0-95ab05e97063 | -20.43216 | -47.66709 | 2024-10-08 03:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f352399-68a3-3d82-be5a-0986f710495e | -20.43144 | -47.67044 | 2024-10-08 03:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fedfea76-5f75-333c-aa65-83781f8f9937 | -19.81668 | -47.39661 | 2024-10-08 03:45:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33e57b89-f59b-341a-9c04-04d4cc9d8332 | -19.81166 | -47.39511 | 2024-10-08 03:45:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ad05f7d-2b01-3f2d-b94c-776d7af556ee | -19.81096 | -47.39848 | 2024-10-08 03:45:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9cfba59-62a9-3821-80ad-07107c3b3a1b | -20.38623 | -47.05144 | 2024-10-08 03:45:00 | NOAA-20 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e8b5a3a3-21c4-31e3-b0fe-0bd9628eb1fa | -21.31808 | -47.61066 | 2024-10-08 03:45:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 498c5677-9dbf-3bc7-b9c6-47be12d8b1dd | -21.31734 | -47.61408 | 2024-10-08 03:45:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b56b75a-ce43-3bef-8517-4831eae1a162 | -21.3132 | -47.60886 | 2024-10-08 03:45:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06d5196e-bc55-3c6e-914e-f97076a9f6b4 | -21.31241 | -47.61256 | 2024-10-08 03:45:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7215974-831a-399a-a6e5-72cf6de9fc39 | -21.09088 | -47.23623 | 2024-10-08 03:45:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 86adf45a-4cef-3b22-bb30-74cd57d71b3c | -21.08881 | -47.22161 | 2024-10-08 03:45:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d61af9a3-0cc0-3c72-90a8-b2f9d61ad73a | -21.08754 | -47.22762 | 2024-10-08 03:45:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ed93c2bf-8bde-3bcf-9f5d-b12467e2a511 | -21.08393 | -47.22031 | 2024-10-08 03:45:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6416b138-2ff5-3e8d-a8b8-4568c2a85867 | -21.08264 | -47.22641 | 2024-10-08 03:45:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d4cc1b3b-7ff0-3e8d-aaad-35c995be552f | -21.07266 | -47.22488 | 2024-10-08 03:45:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5ebaea24-f272-38fc-a56f-6d3e2b53ff9d | -21.0719 | -47.22417 | 2024-10-08 03:45:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b3f84047-fe3c-35b9-8dbc-7dc5910526cb | -21.0708 | -47.22953 | 2024-10-08 03:45:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f73c5765-01be-3b04-aebf-b9157f622ea5 | -21.06765 | -47.22423 | 2024-10-08 03:45:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a062e214-8818-388c-8b3c-702bd6f85000 | -21.06689 | -47.2235 | 2024-10-08 03:45:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5c3a0aec-d2f4-3133-a8c2-dfbbf63a9702 | -21.06684 | -47.24888 | 2024-10-08 03:45:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 795434ab-689c-3064-bddd-94c954fbb1ac | -21.06653 | -47.2295 | 2024-10-08 03:45:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 97f6063c-786b-322b-8769-1ffae1c92fbd | -21.06348 | -47.24007 | 2024-10-08 03:45:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e2cec74f-4a0f-35fd-a382-7a214aec09e6 | -21.06266 | -47.22346 | 2024-10-08 03:45:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b0a5bc83-9180-32c4-acfc-fb61d3ddcfa1 | -21.06257 | -47.24808 | 2024-10-08 03:45:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7d797d19-3200-32cd-88c1-17c676be55dc | -21.06205 | -47.24706 | 2024-10-08 03:45:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 40664aa4-556b-36a6-abba-5c732e7c7717 | -21.06152 | -47.22881 | 2024-10-08 03:45:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 405b1709-0ae7-3d13-bfec-9c6bf563f735 | -21.06081 | -47.22807 | 2024-10-08 03:45:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fdc358de-12a2-3d1d-a041-0bde26aa293b | -21.06042 | -47.23397 | 2024-10-08 03:45:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bd04c112-0fa0-3535-8000-03dfe989a538 | -21.05973 | -47.23327 | 2024-10-08 03:45:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3476314a-cbea-32e2-ab51-67566c0bb49f | -21.97795 | -47.39212 | 2024-10-08 03:45:00 | NOAA-20 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 3d9efa0f-decb-3178-80a9-2b25e466c757 | -21.97672 | -47.39805 | 2024-10-08 03:45:00 | NOAA-20 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| eff37fb2-1fd2-34ac-b51b-2d2384e0077c | -21.8534 | -48.41453 | 2024-10-08 03:45:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 96db1f48-3cb3-3a05-9fec-cfae9405abc7 | -21.84898 | -48.40968 | 2024-10-08 03:45:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55b04f52-ef62-35eb-803b-4696149439a5 | -21.84823 | -48.41311 | 2024-10-08 03:45:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5cce0b6b-bb7f-3eef-bfab-34f374c159f7 | -21.84748 | -48.41657 | 2024-10-08 03:45:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93e732b4-b04a-3d3c-b85b-8bf26207b0e9 | -21.84672 | -48.42006 | 2024-10-08 03:45:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f4e864a-9f86-36a2-a8a0-20cef8ff7157 | -21.63862 | -47.71726 | 2024-10-08 03:45:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 93f85c52-2f5d-37c0-a0b3-dc6f358ad9df | -21.63796 | -47.72036 | 2024-10-08 03:45:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README43.md)
