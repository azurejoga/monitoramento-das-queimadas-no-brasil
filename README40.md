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
| c2a96c4f-702e-3327-b1d7-b8a22b580ede | -2.46124 | -49.36663 | 2025-11-08 12:16:00 | TERRA_M-T | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 3bdd2178-2684-3a2c-9515-1b0606a7d0ec | -2.71369 | -49.53554 | 2025-11-08 12:16:00 | TERRA_M-T | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ee912f5c-5d42-3d73-8110-d48b681c8150 | -2.83314 | -49.41311 | 2025-11-08 12:16:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0741e926-1f67-3a3d-90bb-e93e45167d35 | -7.97225 | -38.66792 | 2025-11-08 12:16:00 | TERRA_M-T | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 81.1 |
| ed07947f-5d9c-3524-9a21-02d4af0f96eb | -7.03979 | -46.98396 | 2025-11-08 12:16:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 0aaefc04-8f27-3301-b237-9ba183d7cb3c | -1.09498 | -47.51173 | 2025-11-08 12:16:00 | TERRA_M-T | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 68253f7e-783d-3dda-80bb-d8df8e6d3dc8 | -0.91304 | -47.55547 | 2025-11-08 12:16:00 | TERRA_M-T | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 20392680-dcb1-3078-898f-597288f6eea3 | -2.83698 | -48.86494 | 2025-11-08 12:16:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| a1ba3582-efe8-3eab-9b43-5949aa4ea4ab | -4.27935 | -48.33801 | 2025-11-08 12:16:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a2ac51c8-0e9e-3e73-a4d5-1489612e8eab | -3.31703 | -50.12384 | 2025-11-08 12:16:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 1e8bc654-e3f4-3495-a628-74202c45604f | -3.57834 | -42.44617 | 2025-11-08 12:16:00 | TERRA_M-T | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 52c673ef-e268-3bfb-b3f5-cd670519111a | -5.11043 | -38.00401 | 2025-11-08 12:16:00 | TERRA_M-T | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 63.0 |
| 1d801520-ee80-3b16-8d87-5c4ed17eb1be | -3.55647 | -42.43747 | 2025-11-08 12:16:00 | TERRA_M-T | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 25.2 |
| e1dab90a-34be-3ef6-9323-367d5cb62cec | -4.2742 | -46.44624 | 2025-11-08 12:16:00 | TERRA_M-T | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e946b0fb-4d5a-31a9-81fe-64a79c72d326 | -3.55436 | -42.45232 | 2025-11-08 12:16:00 | TERRA_M-T | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 103.3 |
| cbcbbdd3-9c9a-3126-92df-dbda7588f240 | -3.41222 | -45.43522 | 2025-11-08 12:16:00 | TERRA_M-T | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7a0b0aa5-dcc9-39e9-b75f-1f0da1235d5d | -8.0489 | -39.4249 | 2025-11-08 12:16:00 | TERRA_M-T | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 39.8 |
| 6154a117-9eac-345b-89cc-ae3aec9587da | -0.91433 | -47.54657 | 2025-11-08 12:16:00 | TERRA_M-T | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 140caf5c-a51e-3bdd-a789-7bf7fad4f800 | -3.43088 | -50.11277 | 2025-11-08 12:16:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 867bb4c6-cbf5-3347-9566-34af06767abf | -1.26281 | -49.29458 | 2025-11-08 12:16:00 | TERRA_M-T | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 63fc6362-b741-3a26-954c-ec567a4d0020 | -3.11632 | -44.08792 | 2025-11-08 12:16:00 | TERRA_M-T | PRESIDENTE JUSCELINO | MARANHÃO | Brasil | 2109205 | 21 | 33 | nan | nan | nan | Amazônia | 132.1 |
| df59c42b-4ec8-362e-98b5-a7c0e939dab8 | -2.95381 | -48.06496 | 2025-11-08 12:16:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 941a2298-e3b4-3741-b702-60954655a70c | -3.34968 | -50.17324 | 2025-11-08 12:16:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b6029b3e-3562-3e61-9355-86db2de1ac4c | -1.10384 | -47.51295 | 2025-11-08 12:16:00 | TERRA_M-T | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 74fe3ee1-232d-3156-967a-1202209c184b | -6.96305 | -46.22235 | 2025-11-08 12:16:00 | TERRA_M-T | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4efd949b-a231-3eb0-8f19-9e0b5c5346ab | -3.11791 | -44.07671 | 2025-11-08 12:16:00 | TERRA_M-T | PRESIDENTE JUSCELINO | MARANHÃO | Brasil | 2109205 | 21 | 33 | nan | nan | nan | Amazônia | 26.7 |
| ee6f5bab-906c-317a-8cc4-270d01b324f6 | -4.84464 | -47.69716 | 2025-11-08 12:16:00 | TERRA_M-T | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3bb4d6d4-009e-3f8f-9569-78ffbf37aba5 | -3.51082 | -44.86442 | 2025-11-08 12:16:00 | TERRA_M-T | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| eb7072c9-75dc-370b-a886-dd5fbe50ef02 | -1.43002 | -47.04766 | 2025-11-08 12:16:00 | TERRA_M-T | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 20ec6afc-e8a8-3704-9672-074fa2344e39 | -4.02789 | -45.45855 | 2025-11-08 12:16:00 | TERRA_M-T | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 8312de6c-7c1f-3c5c-8597-eb44f7471192 | -3.55579 | -42.4432 | 2025-11-08 12:16:00 | TERRA_M-T | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 65.5 |
| b0d36d3e-e654-3af1-aff2-916293f443a1 | -7.9659 | -38.66014 | 2025-11-08 12:16:00 | TERRA_M-T | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 63.0 |
| 6641e302-0191-3807-aed2-c5f1706fe60a | -3.31864 | -50.11298 | 2025-11-08 12:16:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a5c9f085-8c77-3c60-bcea-87d0561984b1 | -3.05009 | -45.26616 | 2025-11-08 12:16:00 | TERRA_M-T | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| a219b3f9-052e-302e-87fc-d33ecde00406 | -3.5538 | -42.45802 | 2025-11-08 12:16:00 | TERRA_M-T | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 73.2 |
| e7340dea-7844-32f6-8ba4-2690fa426a60 | -3.09217 | -50.32844 | 2025-11-08 12:16:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 2ea8f8a0-cc10-306f-9459-edcc59714914 | -4.08297 | -48.04346 | 2025-11-08 12:16:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| cbc1529d-fe2a-3189-b8ca-b8566e7008b5 | -3.65378 | -50.27515 | 2025-11-08 12:16:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 40fbe2e6-b733-3249-86ed-6bd9fae73426 | -3.69564 | -42.76961 | 2025-11-08 12:16:00 | TERRA_M-T | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 85edcfab-f597-31d6-9893-a95deb8793c3 | -3.25222 | -50.14154 | 2025-11-08 12:16:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| d4ce21e1-3231-319c-99b7-c77eb11950a4 | -3.24877 | -48.76499 | 2025-11-08 12:16:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 29e7c1ec-5cdd-3dd4-b096-ea02cf79e8db | -7.36768 | -46.82155 | 2025-11-08 12:16:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0cad5833-53fb-3572-bebd-ff93461d0efc | -3.56505 | -42.4596 | 2025-11-08 12:16:00 | TERRA_M-T | MADEIRO | PIAUÍ | Brasil | 2205854 | 22 | 33 | nan | nan | nan | Caatinga | 348.0 |
| cc327744-48d1-3efa-92e1-46178ec74907 | -3.45111 | -48.83458 | 2025-11-08 12:16:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 97ebb289-357b-30b0-9fe5-0b76fe990d43 | -8.03781 | -39.41659 | 2025-11-08 12:16:00 | TERRA_M-T | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 46.2 |
| fce5e051-5d4b-3b89-a2ee-794adf8788f1 | -3.4602 | -48.8359 | 2025-11-08 12:16:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| c61eefa8-d208-32bd-a3af-59ca8efda540 | -5.9403 | -38.16629 | 2025-11-08 12:16:00 | TERRA_M-T | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 30.8 |
| 2d42a50a-86a9-392c-b978-30d7812ca41b | -1.27309 | -47.49467 | 2025-11-08 12:16:00 | TERRA_M-T | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3c4fceb0-8145-31c1-96ab-c7889fb036dc | -3.52787 | -47.53628 | 2025-11-08 12:16:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 85ceea6d-240a-3d0b-ad79-a4aede1e9ccc | -3.40395 | -45.43744 | 2025-11-08 12:16:00 | TERRA_M-T | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 20.3 |
| e03e917c-59e5-3b0e-84a6-0f40c4882194 | -7.53877 | -47.69873 | 2025-11-08 12:16:00 | TERRA_M-T | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fb8acc8b-39ab-33d1-9e25-ce0de84ab6fd | -4.46146 | -46.3002 | 2025-11-08 12:16:00 | TERRA_M-T | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 0e77f815-309f-3ad3-900a-df609b7ed96e | -3.69755 | -42.75543 | 2025-11-08 12:16:00 | TERRA_M-T | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 64f7d7f5-cb7b-3420-b255-685b3bf58403 | -3.47826 | -49.92282 | 2025-11-08 12:16:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e33adc5b-69e3-3b13-ba7e-84f9230c1671 | -4.04656 | -48.9913 | 2025-11-08 12:16:00 | TERRA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| ebfcdf3d-5b08-3496-b820-57e2e2b55332 | -5.10588 | -38.03924 | 2025-11-08 12:16:00 | TERRA_M-T | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 46.4 |
| d85eb91c-8ac9-3bf1-944b-4b3d283cd1da | -3.9311 | -42.63794 | 2025-11-08 12:16:00 | TERRA_M-T | PORTO | PIAUÍ | Brasil | 2208502 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 279b00b1-a96c-390e-a2f0-38f3aa21ba23 | -3.40533 | -45.42784 | 2025-11-08 12:16:00 | TERRA_M-T | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 1f8525fc-6511-3478-a072-3b0cca663e7d | -3.1262 | -44.08926 | 2025-11-08 12:16:00 | TERRA_M-T | PRESIDENTE JUSCELINO | MARANHÃO | Brasil | 2109205 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| b53d1463-bba9-3999-b023-97de03e99449 | -3.29456 | -44.27117 | 2025-11-08 12:16:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a9d9f045-c01f-3525-bed9-c5cd4d344ea2 | -1.2533 | -49.29325 | 2025-11-08 12:16:00 | TERRA_M-T | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 823a86a4-cd31-3676-93fd-0d9529ca1384 | -2.30035 | -47.97865 | 2025-11-08 12:16:00 | TERRA_M-T | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 8b91163b-24ee-3815-ad71-8e9b6f83308d | -3.15487 | -45.49755 | 2025-11-08 12:16:00 | TERRA_M-T | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0eb2b25d-264a-38f1-abb3-f54699477b71 | -4.46276 | -46.29111 | 2025-11-08 12:16:00 | TERRA_M-T | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 269d70c3-e755-30bd-ac1c-8fcaab5aaa63 | -3.15433 | -50.60175 | 2025-11-08 12:16:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| d06cbf86-4953-329a-8e4b-749c5d43a840 | -4.82654 | -48.0713 | 2025-11-08 12:16:00 | TERRA_M-T | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f19529c6-ae9e-3e19-9074-2bbcec5b981d | -6.19334 | -38.51221 | 2025-11-08 12:16:00 | TERRA_M-T | SÃO MIGUEL | RIO GRANDE DO NORTE | Brasil | 2412500 | 24 | 33 | nan | nan | nan | Caatinga | 38.6 |
| 0b95bfcc-797f-3740-ad1f-af435629c066 | -6.79542 | -46.75547 | 2025-11-08 12:16:00 | TERRA_M-T | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| a5da6e98-b765-3f74-933d-4c8cc526245b | -3.65543 | -50.2641 | 2025-11-08 12:16:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| c4f007d6-ff77-3198-8040-177d57ee374f | -3.83193 | -49.82749 | 2025-11-08 12:16:00 | TERRA_M-T | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 8812b8dd-6180-3997-b74c-88533e5e0ad0 | -4.55508 | -46.68347 | 2025-11-08 12:16:00 | TERRA_M-T | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 6e2a79c7-180e-38d7-a7ad-d1a8739ce3ad | -4.04794 | -48.98186 | 2025-11-08 12:16:00 | TERRA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 0489220c-3463-31c8-bb16-f30a42f1e34b | -7.06527 | -48.36264 | 2025-11-08 12:16:00 | TERRA_M-T | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 34.2 |
| a101ec88-be2e-38aa-b594-74b243efdf29 | -7.9615 | -38.69569 | 2025-11-08 12:16:00 | TERRA_M-T | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 37.8 |
| 192ced61-de85-305c-be81-0394e75ca62e | -5.31511 | -47.88386 | 2025-11-08 12:16:00 | TERRA_M-T | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4b92a27b-04e8-3d40-8b62-ca0783919a98 | -3.7208 | -42.16005 | 2025-11-08 12:16:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 20.9 |
| bac52220-19c0-329a-aff5-7daa20f0005d | -13.05856 | -43.55401 | 2025-11-08 12:18:00 | TERRA_M-T | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 9873d4d3-c5e0-340c-aa03-785bbb497b01 | -9.04876 | -46.99533 | 2025-11-08 12:18:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d28c0fa6-340f-32f6-b5c1-8ca01668dfa6 | -9.04745 | -47.00468 | 2025-11-08 12:18:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6030fc99-b11e-33c8-b59d-498988b86ff1 | -13.16562 | -43.31758 | 2025-11-08 12:18:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 15.1 |
| f83cc12e-9e92-37b9-ab37-c1133c38b5c4 | -13.05647 | -43.57157 | 2025-11-08 12:18:00 | TERRA_M-T | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 91ded292-fba0-3f7a-a7b4-ea960824e245 | -10.53097 | -47.86068 | 2025-11-08 12:18:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5a6162f0-7cd7-3939-9673-738d1dc4beb8 | -13.46258 | -46.43201 | 2025-11-08 12:18:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 39.6 |
| c774a585-87d8-3262-946c-f27121713695 | -10.75779 | -44.80587 | 2025-11-08 12:18:00 | TERRA_M-T | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 840cdeac-e58d-3c0a-b692-ed4553392076 | -12.41823 | -48.60631 | 2025-11-08 12:18:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 0d72a05f-080c-3ecd-b731-1e9dddb0148b | -9.16296 | -49.35938 | 2025-11-08 12:18:00 | TERRA_M-T | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 87d4adb7-61ec-3a9b-bba1-b3810b12cf68 | -7.45952 | -48.68766 | 2025-11-08 12:18:00 | TERRA_M-T | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b2c44c02-31fa-3903-9b82-3a0dab438a05 | -10.10916 | -47.51883 | 2025-11-08 12:18:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a5973640-0e86-3ecc-bb45-fd6af9da92c1 | -8.91553 | -47.81252 | 2025-11-08 12:18:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 436a4b40-8fae-32ae-a079-92bc4de7620e | -7.87596 | -47.27256 | 2025-11-08 12:18:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 06d09814-ae6d-32d9-8837-586a2cfb6599 | -8.60283 | -47.14815 | 2025-11-08 12:18:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a6767519-1ca9-3050-9c4b-26269e8e055b | -15.43464 | -49.63586 | 2025-11-08 12:21:00 | TERRA_M-T | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 51c764dd-3b54-354c-8741-5aa608ae19fd | -16.51113 | -49.72179 | 2025-11-08 12:21:00 | TERRA_M-T | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b9ab7aaf-1f64-308a-9dd2-ea6add2d0e1b | -15.21892 | -49.66549 | 2025-11-08 12:21:00 | TERRA_M-T | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| acccfc01-55fa-3284-af1c-3d93d7de8eab | -25.45411 | -49.52895 | 2025-11-08 12:23:00 | TERRA_M-T | CAMPO LARGO | PARANÁ | Brasil | 4104204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 1c01c143-3189-30b9-9b2c-7653d3efe07b | -3.5671 | -50.4213 | 2025-11-08 12:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 6de58519-b1ae-334a-b38e-df35d9ed5187 | -5.9234 | -41.3056 | 2025-11-08 12:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 80.0 |
| 50a4d260-ca16-3534-8a15-3cb912cfbaca | -4.0366 | -48.9852 | 2025-11-08 12:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| a746a025-e06a-38ab-91a6-79cf96034f26 | -5.9368 | -38.1694 | 2025-11-08 12:50:00 | GOES-19 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 95.9 |
| 6e4dc151-348b-3d0f-a6f2-c6fcf0813427 | -5.9234 | -41.3056 | 2025-11-08 12:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 81.9 |


[Clique aqui para ver as próximas entradas](README41.md)
