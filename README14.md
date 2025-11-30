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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56a1f54b-0ed4-3eb2-92d2-0046c8fa1ed5 | -12.00678 | -49.26939 | 2025-11-30 04:25:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b80e5fad-b1c2-393e-81c2-13d8daaee8ec | -2.6309 | -48.54889 | 2025-11-30 04:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d78f4c5-168e-3c57-9836-b2f2be033b75 | -4.6075 | -45.20648 | 2025-11-30 04:25:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 635e049d-bf9e-3fa4-ba9e-6506d1060b03 | -4.90342 | -42.68272 | 2025-11-30 04:25:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 59831ce1-8a8c-37ba-94dd-afa8b2407b39 | -5.41533 | -41.19122 | 2025-11-30 04:25:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1952d007-9b14-315f-8cc0-59957db42777 | -15.71411 | -50.00784 | 2025-11-30 04:25:00 | NPP-375D | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3f60048c-4518-3d8d-a31d-f35eb3c84892 | -2.63961 | -48.54517 | 2025-11-30 04:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e117ac11-a668-3de1-902f-05a22043168d | -12.65775 | -46.7543 | 2025-11-30 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fc6e6f5e-348d-319c-a939-927e011a3a83 | -13.94016 | -44.38654 | 2025-11-30 04:25:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80673f82-e201-3490-bb95-f37f91153bf8 | -3.25105 | -50.69606 | 2025-11-30 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e62e8363-2c56-3b5b-b7e2-e7d5e7aebc91 | -3.65186 | -42.24537 | 2025-11-30 04:25:00 | NPP-375D | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d85e5972-ee81-3143-bd6f-434567cd8057 | -2.63756 | -48.035 | 2025-11-30 04:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 270c54f8-003c-3bcf-afa4-916be5d3a585 | -4.26949 | -40.66936 | 2025-11-30 04:25:00 | NPP-375D | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d3acd24f-7096-3c7c-aa6e-0d671fa8f0cf | -2.64908 | -48.55379 | 2025-11-30 04:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 677afae5-f381-3d9f-8233-91abc8e72a5d | -2.70122 | -47.39835 | 2025-11-30 04:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc36167f-8f27-3552-b6c4-2ec6a998e4aa | -15.71324 | -50.00892 | 2025-11-30 04:25:00 | NPP-375D | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3074f8e4-ee2e-349e-937f-7e846a02953a | -3.44195 | -45.41136 | 2025-11-30 04:25:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4a620ea5-c7aa-3b1d-992e-c7e416b0a11e | -16.45926 | -45.01626 | 2025-11-30 04:25:00 | NPP-375D | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 994cd7bf-f0e0-3e35-99ad-fd36c1a31122 | -3.64615 | -42.23691 | 2025-11-30 04:25:00 | NPP-375D | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a7c0a23b-0398-3c47-aaea-e7bd803c3101 | -5.36683 | -43.02447 | 2025-11-30 04:25:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3bf3a70f-1d46-3f0c-aac9-d641db77bc95 | -4.60638 | -45.2135 | 2025-11-30 04:25:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66c70a5d-62cb-3308-a4d5-0c1a27253387 | -15.71052 | -50.00712 | 2025-11-30 04:25:00 | NPP-375D | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 58356db6-b171-3fa2-9007-bb3b98abe5d4 | -4.42424 | -43.30986 | 2025-11-30 04:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e983aa25-8542-38b3-85df-393861080789 | -2.51368 | -49.10321 | 2025-11-30 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e9faa21e-1846-3c70-bfa0-ae04fbeb35c6 | -4.414 | -44.44558 | 2025-11-30 04:25:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0afaf937-53ad-3d89-a8dd-20de67546bd3 | -17.22678 | -42.21164 | 2025-11-30 04:25:00 | NPP-375D | CHAPADA DO NORTE | MINAS GERAIS | Brasil | 3116100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2805bb0d-1f89-338e-96d3-a593a5c71ab8 | -12.00154 | -45.40436 | 2025-11-30 04:25:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 723c44fc-bafd-353a-bc0f-da2cde10b066 | -2.84049 | -48.82948 | 2025-11-30 04:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2212e7f9-ff05-3722-8ab8-c2bae88db246 | -2.63014 | -48.54553 | 2025-11-30 04:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acf76dc1-248c-333a-af13-2781c4823a1e | -12.8287 | -47.39103 | 2025-11-30 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 210258d3-dd3e-3d54-b848-da41f3512bb8 | -12.70558 | -46.79128 | 2025-11-30 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d5b04cf3-f6e3-3c38-81bb-0229ccd74cc5 | -5.15556 | -37.68802 | 2025-11-30 04:25:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 80282086-62be-3b86-aca6-f9b748c59519 | -12.70501 | -46.79484 | 2025-11-30 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 086cceae-1c21-3da7-a777-7c688b10b1ca | -2.99439 | -45.41481 | 2025-11-30 04:25:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 95c0506b-26b6-3403-ba3c-1233ee72d7f2 | -2.39488 | -49.38741 | 2025-11-30 04:25:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51865959-11b7-3b51-b5fb-be336ee09f9d | -17.38523 | -42.46592 | 2025-11-30 04:25:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e212e984-da1c-31cb-95cb-bf2e2443b1a3 | -2.54599 | -48.35352 | 2025-11-30 04:25:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 375fddfe-8a9d-3800-9b2a-064d8249311b | -3.3502 | -45.55164 | 2025-11-30 04:25:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8f06e8b3-57ea-3d8f-b38c-8a7f9b9b1818 | -4.95507 | -41.20351 | 2025-11-30 04:25:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d4ed9095-758d-3b74-b36a-fa6f72b024b5 | -2.70676 | -48.3488 | 2025-11-30 04:25:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| caded530-bd87-3b1d-b83f-5013a311d82c | -2.64981 | -48.03215 | 2025-11-30 04:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 318ccfe7-d429-3827-8cde-ed2ffaffaa0e | -5.73007 | -39.83677 | 2025-11-30 04:25:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 37af6928-cc0d-36b2-87a3-0f8a5dd76dbc | -11.25952 | -44.5425 | 2025-11-30 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f433cf19-b33d-3ec1-a784-360b2d04153b | -3.49788 | -44.22309 | 2025-11-30 04:25:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc2cc675-182d-32bc-a1b0-23fb395a6b83 | -2.64277 | -48.55084 | 2025-11-30 04:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 60f27c27-0e82-310f-821c-789c9c0ae2c9 | -12.22789 | -54.38063 | 2025-11-30 04:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9190672f-acc2-352e-95d6-38d9eb8d7739 | -4.44725 | -44.49327 | 2025-11-30 04:25:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44c92f77-c264-326a-82bf-c92aa69c936d | -2.64139 | -48.03561 | 2025-11-30 04:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 66ccd926-3ab3-39a5-b342-ee0e687b901a | -4.42479 | -43.30635 | 2025-11-30 04:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ef82f7f-a4e0-324e-9b34-3ec045856625 | -2.45073 | -49.00692 | 2025-11-30 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 136964f7-f559-324e-b16f-7ab81108ff24 | -5.74474 | -40.80756 | 2025-11-30 04:25:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| aec5ef6e-44d3-365f-9034-3886e2e17401 | -2.69754 | -47.39771 | 2025-11-30 04:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d2b655f-b1db-3b10-a1ad-a1f46f80dc35 | -2.64356 | -48.54581 | 2025-11-30 04:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9303e0d0-37d5-3f4a-aa12-e2976573030b | -2.60909 | -49.26224 | 2025-11-30 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c371ede-e365-3185-a282-bd9c3095cb3d | -4.99674 | -40.73463 | 2025-11-30 04:25:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b89c3cea-dae3-3e80-998c-79150b46fd1b | -2.64598 | -48.03154 | 2025-11-30 04:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a6c928b2-5db6-3685-bba5-bded153f39d9 | -13.57847 | -43.06596 | 2025-11-30 04:25:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 16561508-bc42-3461-86ed-1964a8416413 | -4.36816 | -43.16386 | 2025-11-30 04:25:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8bf6e18c-226d-3dfb-bdd5-90c2fe608008 | -3.64844 | -42.24484 | 2025-11-30 04:25:00 | NPP-375D | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| aa61016b-90dc-36ed-8831-96611fc7badd | -2.64117 | -48.55248 | 2025-11-30 04:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 484a23a8-3ad9-31cd-9831-111df94feb95 | -13.48607 | -46.71642 | 2025-11-30 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ca103995-d88d-317f-aa05-ea82834bc339 | -3.59016 | -45.62297 | 2025-11-30 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b235126-b598-3365-ab70-95f2e9ee1bd7 | -2.50957 | -49.10254 | 2025-11-30 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a5134023-d64e-3bbe-b856-70db5a19a630 | -3.59301 | -41.66528 | 2025-11-30 04:25:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 9f0fa4a2-7174-3127-bab0-912e32b7503e | -2.51426 | -49.09956 | 2025-11-30 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f26cba1f-3d22-3320-b9fe-aff8a83ce254 | -3.59361 | -41.66142 | 2025-11-30 04:25:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a9231167-51c7-313d-bcc4-8a31b567ff2f | -15.70966 | -50.00819 | 2025-11-30 04:25:00 | NPP-375D | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fed8ddd4-e8b3-3237-929a-d7a79a812056 | -12.00387 | -49.2645 | 2025-11-30 04:25:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b20efebf-6897-3466-8561-c01e8941b1d2 | -12.01041 | -49.27004 | 2025-11-30 04:25:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b11ec2eb-3d33-3ce6-bf3d-b7c5ae39604e | -14.60767 | -49.42622 | 2025-11-30 04:25:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 336bb7aa-f50e-3c19-970c-1545f3ef9e5c | -3.58601 | -41.66422 | 2025-11-30 04:25:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 5c98ac02-b754-3ede-9b78-aa8421aefda0 | -5.31255 | -40.88635 | 2025-11-30 04:25:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 21ac0056-24f1-3eee-b3cf-a3f331bc4b97 | -4.61084 | -45.207 | 2025-11-30 04:25:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32312036-bd99-356c-a7b7-f21a0d43d154 | -12.01766 | -49.27133 | 2025-11-30 04:25:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22dc2deb-7feb-3ccc-b146-d6c208ad6eba | -2.70341 | -49.31887 | 2025-11-30 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a168ece0-d0db-3046-a40b-9818a19bc9fe | -10.71743 | -47.2599 | 2025-11-30 04:25:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5ce8b11-18af-3d4e-acf5-83aa6dcfdc2b | -2.6008 | -49.2609 | 2025-11-30 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 46268d3b-2c7c-3c4f-9572-6691ac8f5501 | -10.71803 | -47.25622 | 2025-11-30 04:25:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dbe75a73-1d2f-3bde-9e86-6ad3bfa71675 | -12.01837 | -49.26709 | 2025-11-30 04:25:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2195ed39-fa10-30a8-8bd7-ff8558585989 | -12.82534 | -47.39045 | 2025-11-30 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 60e6e482-a437-3448-9191-bfbdca2efb46 | -5.73209 | -40.81531 | 2025-11-30 04:25:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 26ebd599-dec2-374b-8753-f41e80d8ca9d | -5.5083 | -42.5849 | 2025-11-30 04:25:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b067915b-09d5-36f7-bd4a-c48e7cf11250 | -12.01546 | -49.26221 | 2025-11-30 04:25:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 78508e7d-24c8-320f-80c7-a9c00352e1d7 | -5.23643 | -41.23863 | 2025-11-30 04:25:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3d67caf8-b112-329e-b37e-523f9b539d44 | -5.73189 | -39.83547 | 2025-11-30 04:25:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 76b350f5-6786-3ec7-b0f6-1b4e307ccdaf | -5.36344 | -43.02396 | 2025-11-30 04:25:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 89a2c67d-07a1-3ad3-a594-6804eabd007a | -4.19447 | -42.36873 | 2025-11-30 04:25:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ec3c4b27-098e-3709-943e-8dc792ee1a5e | -5.50603 | -42.57689 | 2025-11-30 04:25:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c6195756-f698-3e65-92d4-0db6d1f0e1ef | -15.32117 | -42.05276 | 2025-11-30 04:25:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 857007a2-e363-3fdd-8e69-807af8f7850a | -2.92345 | -48.2239 | 2025-11-30 04:25:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13669094-83e8-3175-8c73-f90da979fba8 | -2.44944 | -49.00708 | 2025-11-30 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1925e74-7127-343d-a42b-a0c86e868fca | -5.74708 | -40.81742 | 2025-11-30 04:25:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 47d14617-395f-319c-8da1-1fad61a0058e | -2.63804 | -48.54683 | 2025-11-30 04:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5161db87-4429-3b13-a49f-1bc3d43947d6 | -2.63486 | -48.54955 | 2025-11-30 04:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 62a81cc9-16cf-3bb2-8aaa-cc79ef424079 | -12.83601 | -47.38854 | 2025-11-30 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3dc31ea2-4f50-319a-a538-d808aed97686 | -2.49505 | -49.3801 | 2025-11-30 04:25:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1473579e-1c37-3b95-adbb-5ec585b81dc5 | -13.85979 | -49.31859 | 2025-11-30 04:25:00 | NPP-375D | MUTUNÓPOLIS | GOIÁS | Brasil | 5214101 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 65914cd7-3376-3fea-81da-4f7a09dcb57b | -15.71396 | -50.00467 | 2025-11-30 04:25:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f074cd7d-713e-37ec-af40-5002e0f3d048 | -18.13234 | -47.15631 | 2025-11-30 04:27:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b7aaf93-6884-3a85-b6e6-9a8839aeaef0 | -21.14914 | -48.61475 | 2025-11-30 04:27:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README15.md)
