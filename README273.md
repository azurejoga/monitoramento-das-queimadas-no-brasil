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

## Dados Diários - Página 273

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2aadf592-fa65-34b4-9d8c-13a1bf9d7e9a | -11.08479 | -44.00858 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 1680e500-cb49-3f36-ab71-763d3d36d955 | -11.86531 | -47.39678 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 79d2e06e-820e-34b6-a230-85537a5592c9 | -13.44329 | -39.14941 | 2026-10-08 16:18:00 | NPP-375 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 8099120e-97fe-3d68-bf75-ac6586789dea | -13.69714 | -49.12261 | 2026-10-08 16:18:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d18a79a9-83f6-3677-a9f8-33056ad2a909 | -11.7514 | -44.93217 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 38c1c200-97a2-3926-8c24-b374dd84158c | -9.9394 | -43.56922 | 2026-10-08 16:18:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 5c9ab393-2b74-373f-a7e9-2d5d3ca64d5e | -10.15952 | -40.53024 | 2026-10-08 16:18:00 | NPP-375 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 20.3 |
| ea1fe611-88cd-34b5-b96c-6141448a6bcc | -12.3164 | -47.05482 | 2026-10-08 16:18:00 | NPP-375 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fced0bd3-2f9e-3feb-b9b1-c67c290634b9 | -11.24141 | -44.02005 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4e0c7474-a227-309f-ad6e-d2b0b15b0abe | -11.85883 | -43.5387 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 71579167-61e3-3bf9-b90d-ee5c0354c091 | -12.7741 | -44.863 | 2026-10-08 16:18:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 9ff19633-885c-31de-a669-11a59e93c933 | -11.33869 | -46.71079 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e84d0242-dc10-3e2b-b0f3-95320156674e | -8.95467 | -45.1713 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 27.4 |
| be1da476-605a-34cb-8cce-01559605c354 | -11.77603 | -45.57838 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 7ff94b24-b5a9-3118-82bf-36b74a706951 | -8.88478 | -45.39347 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d4b205d7-9914-3a1e-9b39-08f850f66c35 | -8.9556 | -45.17001 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 48c8622a-30c8-30d9-8e1a-27e31325d43c | -11.22453 | -45.24636 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| cf7695f0-e37b-3666-b31f-35d0024f8316 | -11.0791 | -45.78048 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d315f639-ea1a-3918-ad42-e0bae97ff527 | -11.36891 | -47.72297 | 2026-10-08 16:18:00 | NPP-375 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 602eb5eb-4cab-312c-a9c8-f5c2bfea5cce | -9.83289 | -45.75921 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| fe14d0e3-3dee-30c7-8cda-875c733dff2b | -10.41536 | -47.27755 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 79bcedf3-1b89-3242-9fb9-39232a6bcd97 | -8.40178 | -38.85096 | 2026-10-08 16:18:00 | NPP-375 | CARNAUBEIRA DA PENHA | PERNAMBUCO | Brasil | 2603926 | 26 | 33 | nan | nan | nan | Caatinga | 10.6 |
| b10d67ad-37eb-3c2f-94ef-26068d244691 | -9.80947 | -47.81612 | 2026-10-08 16:18:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 45e8f678-cee5-3d43-b4e2-bde4d063d860 | -9.02847 | -44.38154 | 2026-10-08 16:18:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 150.3 |
| 959a33c9-3a3a-3ff5-a25f-f6e011048df6 | -11.77261 | -45.58921 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 24.0 |
| bad537a0-dd5c-34c2-931f-6f4f2336c1e4 | -10.43253 | -47.29172 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ac621595-875e-3de5-8ed8-4f76d9e98a4f | -9.84748 | -47.85461 | 2026-10-08 16:18:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 8a48b7a0-abb3-315d-8f0d-304bfc43c635 | -8.89 | -45.38897 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 23ffb7a8-8130-3399-8763-20225fb4aba4 | -9.84028 | -47.48577 | 2026-10-08 16:18:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 08012e36-72af-39c2-9e73-f19d53bd3b43 | -12.18832 | -44.64964 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| c12949d5-e7d4-3949-8cb2-986443523e2a | -8.93981 | -45.15424 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.7 |
| bfc254c9-e16f-317d-8a62-c42c73ff3f44 | -11.0832 | -44.02897 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 166.9 |
| f4bcbf28-e8bf-3cb1-bac7-c7ad5c4934bb | -13.13119 | -46.36961 | 2026-10-08 16:18:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| b4e9bb5b-ef14-3902-86cc-639927981f68 | -9.84287 | -47.85036 | 2026-10-08 16:18:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| dd87951b-5749-3b87-8e50-7770aa7c1709 | -8.28619 | -45.71026 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bc0279fe-5585-39f9-ae35-95e3b940f8c3 | -11.20248 | -49.42806 | 2026-10-08 16:18:00 | NPP-375 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| dcc2f897-2644-3258-b987-c8daa4dca862 | -10.46348 | -47.24142 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| e5e23a4a-6f6c-3d49-a5de-8b5d820bd162 | -11.00188 | -45.41608 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| ae41b4e7-9a22-3e9c-b7d5-e9eec5b71181 | -9.08125 | -45.11633 | 2026-10-08 16:18:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 22.0 |
| e932bfda-a838-3446-b0c4-005953401864 | -9.24756 | -45.65532 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 493fdfc6-bb74-31dd-88cf-d1b8f09bf805 | -8.9719 | -47.56183 | 2026-10-08 16:18:00 | NPP-375 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 58c3ed01-f5fe-34d3-8607-3e66781dfe5f | -7.68567 | -40.90099 | 2026-10-08 16:18:00 | NPP-375 | CARIDADE DO PIAUÍ | PIAUÍ | Brasil | 2202554 | 22 | 33 | nan | nan | nan | Caatinga | 24.5 |
| 130cea43-4afe-383a-9c2f-7a2fc8fefd77 | -11.08745 | -44.02839 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 166.9 |
| 4f883485-4203-31b5-8f89-343f6e577e49 | -9.81304 | -45.68149 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 9911c452-ddf7-337f-9f2c-8782f876eb2b | -10.47517 | -47.24953 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d1dc6492-c412-31dc-ba94-30ca2e4b87ff | -11.72508 | -43.63602 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.2 |
| fa6cba65-d6ff-3923-acbb-ec5526d3674e | -10.56858 | -46.28947 | 2026-10-08 16:18:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| ac66fc9d-96f4-3630-b2e6-9ab6ea8f0457 | -8.57231 | -37.12076 | 2026-10-08 16:18:00 | NPP-375 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3de62774-c58f-36f4-aac5-9c56543d28d9 | -11.58609 | -43.68233 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 216.0 |
| 000a635f-8b9e-34be-a878-5ccc4592dc7b | -11.58926 | -43.67429 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 3818cf3c-bf19-38f9-a165-8f63590aa057 | -10.22124 | -39.34911 | 2026-10-08 16:18:00 | NPP-375 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 936e50b2-ff37-3c33-8eba-12280b2d82fa | -13.29704 | -41.50894 | 2026-10-08 16:18:00 | NPP-375 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 15.5 |
| bbb0148e-1d73-37f4-91f9-bf26ff3d42d7 | -10.44349 | -47.29395 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 41232c52-2649-3e55-a9db-b966545749d6 | -11.85422 | -43.53581 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 6cc194a2-657a-3963-9819-964a3d90df4d | -8.76884 | -44.15398 | 2026-10-08 16:18:00 | NPP-375 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 4f3248db-39d2-3c7c-b272-2b8b2a2f6314 | -8.96834 | -45.13833 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 71ec3b60-42c2-3305-91ba-1f0fd28cf66d | -11.40739 | -47.574 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 41021ec1-d57c-32fa-8b6e-922d4bbe6489 | -9.79042 | -44.7777 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bbbc72e9-0544-3dcb-a503-8afbf644db38 | -10.51553 | -47.31595 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 41bfaa36-b1bc-37a5-b65b-7ae64d2e258d | -8.29247 | -45.72065 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 1ec2d93c-22f4-3777-8c38-488a48f0053c | -11.35986 | -46.71376 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 992c99f5-781a-357f-9367-c394b5082056 | -10.90561 | -45.53393 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 0c0b3508-0187-30b8-8872-e4b5a9959dfb | -10.07948 | -46.00702 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 514e1ce1-1099-3dcf-b9d4-72fbef67968b | -9.36741 | -45.95072 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 9d26f825-06a1-33d4-9de5-8ff1f67ab288 | -8.52203 | -46.91512 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 06e99369-f53b-3a3b-8545-b12f7cae511f | -9.89365 | -44.85125 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 70f44567-9d1c-3750-96c2-b2fab42f792d | -11.84449 | -47.36089 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 22f9a334-8869-385e-b1e4-9dfddc6922d4 | -11.82748 | -47.31083 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9dfa9348-0303-3424-b046-ff93ef170f35 | -10.52173 | -47.31994 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 2b62d91b-9df7-3331-9694-7a8dd391e4d7 | -12.82165 | -45.55844 | 2026-10-08 16:18:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 350ba6ad-66d5-3ce1-9c34-9608ae274f50 | -11.23652 | -46.27068 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 60d1d8ca-e48e-3095-86c4-16f089ca7c2b | -10.48288 | -47.22683 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2cba0080-5384-3372-9da9-41c752f67c32 | -9.13673 | -45.83012 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.6 |
| b3fe1b94-6b16-35f1-9212-555d124f1c68 | -10.47356 | -47.23708 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 8e83c43b-9ca6-3b96-85e9-8e85ab1dfaf4 | -12.34129 | -47.08228 | 2026-10-08 16:18:00 | NPP-375 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 43673334-44a4-3c50-bf9e-bded6e25cd89 | -8.88993 | -45.3974 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 29e532d9-564f-367f-ae82-5928304c452b | -11.24728 | -46.2671 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 453221ef-daea-3eb8-ba09-56fb67e513c9 | -10.51634 | -47.32255 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| bf7b1a64-0e5a-3175-a854-ef44539972ea | -9.84159 | -47.85163 | 2026-10-08 16:18:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| c1e81dab-593b-3b57-83c9-e0719566bcfd | -10.33922 | -46.24504 | 2026-10-08 16:18:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| c465d998-589a-37da-91a9-2801cc0a1b64 | -11.58977 | -43.67805 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 74bf7516-a2cc-3137-b8e3-cc91b96df3e6 | -11.11592 | -45.68979 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 08d55e0d-2775-34aa-b27b-a074fce1fbdb | -10.16008 | -44.6746 | 2026-10-08 16:18:00 | NPP-375 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 31.0 |
| d19f9fd8-6068-3c87-987f-bd1a1872dd75 | -11.59408 | -47.1832 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 033ac2ad-ed0a-39bb-b6f6-7f4330ef8e1f | -11.59972 | -43.6574 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 1ed75ca8-9364-3778-86ee-72ede662d67c | -11.15668 | -47.29188 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 09c4ff92-ea51-30ef-8b00-46fbb214aca2 | -9.81705 | -45.67598 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| bb8f3783-396c-304d-b481-1f45f0fe798c | -8.58176 | -45.69247 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 229aec98-c9c4-3ee8-af6f-0bfa9018ca16 | -12.22765 | -44.73774 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 98b9d6ff-f9f6-3828-b90b-ca06f6ec317a | -11.01387 | -45.43471 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d89f997b-66ba-3848-a9a8-9c8b36ba067d | -11.86488 | -47.39333 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 85254f4c-7daa-3549-a526-55d2af79a45a | -8.78225 | -47.37722 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| fe8c5281-f52f-3a28-bee8-ac3fe5f4d241 | -11.64042 | -43.70615 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 96c61719-516e-37a1-a25e-7849bc2714c8 | -8.5529 | -46.91402 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 003e7a79-f875-3ebf-af58-3a7743ab8a62 | -11.85314 | -43.56847 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 4004d9c0-a454-34db-9c10-eabf2919f528 | -8.7898 | -47.59399 | 2026-10-08 16:18:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 858b1246-6db2-3fa7-a8cd-59ca224a82cb | -9.10449 | -45.12107 | 2026-10-08 16:18:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 7e8c036b-c89a-30ad-9dc6-fc98e3b35ae4 | -8.75901 | -44.144 | 2026-10-08 16:18:00 | NPP-375 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 19.2 |
| cb7dd23b-f266-36d2-b36d-1d4074bf14be | -8.96075 | -45.14249 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 83f0bc9c-3f5a-3aaa-8241-5e23f2fd5ba0 | -10.52486 | -47.26182 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README274.md)
