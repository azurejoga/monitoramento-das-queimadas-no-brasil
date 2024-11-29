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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3fab110b-9d49-3b7a-9cf5-878fb7f67339 | -4.17217 | -48.60899 | 2024-11-29 00:52:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 95550609-e343-3582-ab61-375f90c90612 | -2.14851 | -50.61816 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 2a694e20-75d5-384e-aaa2-cadea2a13ca7 | -2.94625 | -48.33929 | 2024-11-29 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2dd8a73c-010c-3887-9a36-1428aae58e42 | -2.87896 | -46.873 | 2024-11-29 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 23ca40be-325f-3ea3-b90b-acabbb61250f | -1.30808 | -51.92823 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d377b911-734c-3e66-a8e0-d07c0541ab45 | -4.33905 | -45.86226 | 2024-11-29 00:52:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 44740ac7-5e3a-34b6-8f35-fc763830221a | 0.9853 | -50.13372 | 2024-11-29 00:52:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| dfe135d4-c910-3514-ac47-863fcd695fb7 | -3.05516 | -48.52424 | 2024-11-29 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 08a29439-712b-390b-bac9-39c8857b3e9b | -1.31437 | -51.75583 | 2024-11-29 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ffd093f4-67b2-3938-8ee5-5fcc4ad5bc11 | -1.25238 | -54.53802 | 2024-11-29 00:52:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 59fde9d5-eaf1-3a36-be3f-0d27f22279fa | -2.57072 | -49.07995 | 2024-11-29 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| e64c114c-b0ee-3259-98f1-79352da1919e | -1.16439 | -51.92585 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f4140301-f49f-316d-85ab-af1b6b73265b | -4.23363 | -45.76902 | 2024-11-29 00:52:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 673b7fdf-8753-3cad-89c9-ed2566ca1de2 | -0.87126 | -51.7191 | 2024-11-29 00:52:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c11b2201-3976-3aa5-93c0-5a0f701c76ae | -3.32719 | -50.21514 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 3565bdff-bb7e-3f6a-8929-3579c2b72ec5 | -0.88104 | -51.71771 | 2024-11-29 00:52:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 36985b7f-f3af-3863-9a39-5b391ce3c76c | -4.31652 | -46.03973 | 2024-11-29 00:52:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 30f42f44-d78d-357a-8258-fd5930fdf24b | -3.70787 | -50.5108 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 800eac19-6a54-39b3-a03e-f346313e7c21 | -3.87071 | -48.36341 | 2024-11-29 00:52:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 0568fd2a-db98-37a8-88ad-6ebcc457e590 | -4.5237 | -45.72964 | 2024-11-29 00:52:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 41f370b3-5ca9-36de-b2ee-a4c38f465e16 | -2.83884 | -48.09945 | 2024-11-29 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| d704c724-8b3d-363a-b541-7c27415f996e | -3.94147 | -46.89227 | 2024-11-29 00:52:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 85b9c955-3513-35a5-b4f4-b8d675faea34 | -3.22021 | -54.19025 | 2024-11-29 00:52:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 7bdcf60f-80d4-3cec-a865-ebdf367949de | 0.99448 | -50.27012 | 2024-11-29 00:52:00 | TERRA_M-M | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4699ec71-f0d9-3b9b-979a-383ca21f3d91 | -1.89027 | -54.54302 | 2024-11-29 00:52:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 1539d680-aefc-34b4-831d-9bfac587051f | -1.59181 | -52.28868 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| cc91fa38-ad46-34a0-872e-69b7560f5916 | -4.36076 | -47.25478 | 2024-11-29 00:52:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 17.3 |
| c1a417f3-efe3-3228-8530-2aabefd3de12 | -3.85459 | -47.06111 | 2024-11-29 00:52:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1d5230a7-342a-3e10-b575-91ad97b9a63e | -5.5886 | -45.21727 | 2024-11-29 00:52:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f0ddfebc-773c-381f-8ae2-4efcb714fd5c | -3.94987 | -46.69474 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 2acc0044-e1f3-3f37-831e-33f2eabfa060 | -1.31123 | -51.95097 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 4a28ab7f-7bec-3ff6-a5cd-285f3d1f5985 | -5.63744 | -46.9678 | 2024-11-29 00:52:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| bdaa67ce-cf3b-39e5-8355-89b1da69220e | -2.57336 | -51.84315 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 5a588ec8-0543-31aa-af13-0b6fdf8d519d | -0.95321 | -51.64649 | 2024-11-29 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 87c88305-728f-3047-8c2a-9e35ba24ce34 | -1.69653 | -52.43644 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| a9b8aa5b-12d5-3399-b63d-c9ab4973e2e9 | -1.20214 | -51.75537 | 2024-11-29 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 50912e36-cd11-3bdb-ada8-f10fe62cc6a2 | -1.67399 | -52.42693 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| dfeb6f69-b0a9-3d25-b7c6-cc74fe289ff0 | -4.34448 | -46.74708 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a7f5b8ca-df39-3787-9346-5201fa4ff399 | -2.67592 | -46.26972 | 2024-11-29 00:52:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6add81a3-9ee6-3145-b45b-8ba129f7c190 | -1.05884 | -52.42392 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e3635c53-a984-32d9-8451-b5bfe5e4c6d2 | -1.36379 | -51.96122 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0f780d7b-702d-3dc7-8154-0e3734b28753 | -3.25226 | -53.64456 | 2024-11-29 00:52:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| e23e1211-6475-3abd-8c49-b072af17f10c | -4.26432 | -47.61281 | 2024-11-29 00:52:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 051e04bd-8178-3703-9fb3-20a7cadfc6fd | -3.09669 | -50.3587 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7c16d15b-8fd8-39df-9969-ceacd1c8552e | -1.53103 | -51.61796 | 2024-11-29 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 64818861-ce37-3c23-8087-5343864cd740 | -3.93611 | -46.72186 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 325318a7-a3b3-3ce7-a4ac-44d6c473b187 | -3.5346 | -52.1565 | 2024-11-29 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 99b75b37-95b1-358b-9c94-270a7a098044 | -1.29003 | -51.72548 | 2024-11-29 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6d0793d8-2938-33ea-a3f9-92b12836540f | -3.96015 | -47.94258 | 2024-11-29 00:52:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6f27f986-c4d7-3418-81f3-79bd923fc6d0 | -3.03378 | -48.5003 | 2024-11-29 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 44e7e117-d791-31f8-938a-78025944b6a4 | -3.94653 | -46.72987 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 0dd307a0-b874-381f-9f8d-48a6207d3f0e | -2.58186 | -45.51321 | 2024-11-29 00:52:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 7ed4dfa5-24ec-3c96-b794-77719da9aeba | -2.73559 | -45.66405 | 2024-11-29 00:52:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 44d4ff86-dbc3-315a-ab39-f5ac5f1859fa | -2.9551 | -48.33804 | 2024-11-29 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 334ce6de-25dc-3308-8f39-d988925afdf2 | -1.64825 | -55.05492 | 2024-11-29 00:52:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 40eaf831-9458-3141-946f-541dba10200c | -3.06439 | -45.10065 | 2024-11-29 00:52:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bdf8011e-d570-3d89-b947-00ed0cf8c337 | -1.62307 | -47.5031 | 2024-11-29 00:52:00 | TERRA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f1813649-7df2-3b42-aacb-457832ced2be | -3.5427 | -50.18685 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 489677e6-1f0e-36db-93e6-bff70106647e | -2.10163 | -50.34771 | 2024-11-29 00:52:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| a92402dc-94ec-3146-ac21-7d38112576e6 | -3.59627 | -50.36932 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 802f01ef-a2a1-3f34-a389-2c893cf19987 | -3.05394 | -48.51543 | 2024-11-29 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| bc4070cc-f238-3f79-b8f1-5dc267814aea | -2.58911 | -48.08381 | 2024-11-29 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 75a90bf4-87b5-32e1-b87c-c8a13d496552 | -3.25394 | -48.88976 | 2024-11-29 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| c3e1d206-da9c-3127-8cd9-7b91317e0f35 | -3.8098 | -46.61149 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 40d75561-8be3-346e-abb6-37fae03a4625 | -4.69316 | -46.6727 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 14.1 |
| b2e9dfa3-be5a-3ffb-b0e9-869ea1538f16 | -2.62308 | -51.75956 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 099cb19a-11df-333f-9387-89d73455d0ce | -1.61929 | -52.46549 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 98435f32-2a1a-3d11-a70b-0547ac8fdf3d | -3.24292 | -53.63514 | 2024-11-29 00:52:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 49f30966-70b0-309b-be3b-ceff4c63fb5f | -4.78767 | -46.11225 | 2024-11-29 00:52:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2de35e86-1409-3b13-8778-a78fb2b59447 | -2.29016 | -50.58623 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f286ad17-149b-3099-91fe-ed7fdbb6a9e6 | -1.59717 | -52.25105 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f4bd6cbc-c67b-33fa-9d0f-e84dd1bfe7c6 | -2.58655 | -53.96819 | 2024-11-29 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 382df835-58a9-3735-bf0f-a67db758d657 | -3.46494 | -50.5423 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0a7c1c54-9810-36f1-9086-b97938540a41 | -2.28313 | -45.64829 | 2024-11-29 00:52:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| b895be88-3554-37c3-8144-f4039e6d99ff | -2.58472 | -46.20633 | 2024-11-29 00:52:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 76c6ea96-60db-3911-804d-06a3a29c6b7e | -3.25689 | -53.64954 | 2024-11-29 00:52:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 4ee206e7-c5be-3410-89d4-f1e14e8b180d | -1.8887 | -54.41083 | 2024-11-29 00:52:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 82ed4b97-bd13-3b87-ab8e-1e6b6e80bdd0 | -2.97686 | -51.58116 | 2024-11-29 00:52:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9bdc22a2-c990-30e5-a130-36221bd0a66c | -1.3672 | -52.13155 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e4abc71b-6975-335e-b5ae-a46decc01162 | -4.66163 | -42.3859 | 2024-11-29 00:52:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 20.9 |
| d447aae8-d4ed-39a1-ac7a-07ce13c5d959 | -3.19488 | -46.57011 | 2024-11-29 00:52:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e3133ba4-c8da-3dd9-b54a-cbf2c56d06b4 | -3.35532 | -45.42011 | 2024-11-29 00:52:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 6315331a-01dc-3451-837b-6bc94b5e5aa8 | -3.37694 | -50.18262 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| a6bba681-5dc7-34a6-af51-45ffc35ff10a | -4.05894 | -46.6823 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 379853a5-162b-30d3-9d8d-06554efd8e26 | -4.48122 | -48.11714 | 2024-11-29 00:52:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| e0f5a94b-d0e4-34e1-a200-8150dec39330 | -2.29764 | -51.99567 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2b7b0883-239c-357c-8a5d-26357aca3d3e | -1.19999 | -53.88576 | 2024-11-29 00:52:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 493f30a2-8a3c-31a3-bccb-5596ed5d3a27 | -3.36357 | -45.40766 | 2024-11-29 00:52:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 527e7bc5-80e1-34d0-abb2-4dd2ef742d45 | -3.893 | -46.68007 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 69913151-e709-374c-a159-6510c1e43181 | -2.70744 | -51.99992 | 2024-11-29 00:52:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| c200e8c0-c53b-3752-aa84-cac2527c55f5 | -2.64863 | -48.78318 | 2024-11-29 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 42e40cd0-3b84-3abc-91d4-885bbebb9269 | -0.27381 | -51.62696 | 2024-11-29 00:52:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 54.9 |
| d67049e8-da2c-35f6-8231-eaf51a146823 | -4.772 | -44.95678 | 2024-11-29 00:52:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 67a3ac5c-d48f-3814-86a5-7f4aed7b8634 | -2.72465 | -48.66721 | 2024-11-29 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b1ad6543-5418-3e89-9759-edebd3c65b87 | -2.61921 | -48.16973 | 2024-11-29 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ab21485f-7699-31a7-97e6-b1a45e516610 | -4.34993 | -45.87093 | 2024-11-29 00:52:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 93e6f839-bf82-34c3-94d0-516dbfcd2a13 | -3.2268 | -54.17771 | 2024-11-29 00:52:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| fbefa8d7-efbe-366c-bb05-a5f88067ff97 | -4.78184 | -46.11896 | 2024-11-29 00:52:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 229b41e9-fff1-3636-b466-327ede5bc4c6 | -2.29604 | -51.98384 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 36c896f3-95c5-3840-a3a8-1d818be718e6 | -3.17434 | -46.29391 | 2024-11-29 00:52:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README11.md)
