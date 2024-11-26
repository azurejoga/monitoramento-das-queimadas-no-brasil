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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f98d7df-db89-3b28-bd29-a8acf95e05c1 | -4.31905 | -47.51186 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 99d64203-4ad5-3953-9218-39936757298a | -3.949 | -48.07318 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a2bbf78-e803-3706-a07f-2927250bf30a | -2.91864 | -48.72391 | 2024-11-26 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 32596604-ef43-3586-bab3-5787937b10ef | -3.44415 | -50.01263 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b48304bc-2d04-3ea9-8d79-d972a36f46c5 | -4.24941 | -48.59353 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 91797bdd-22f7-3f35-9e62-cae6a7f40fa8 | -3.18101 | -48.43962 | 2024-11-26 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 5364a13e-74fe-316d-82aa-accab99d80d9 | -3.96013 | -48.08221 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 12b6f348-5acb-34c2-83b3-3e8789e24f64 | -1.93603 | -45.76202 | 2024-11-26 04:14:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 200ed60f-cb6e-3b05-95af-646f373f4d38 | -3.98183 | -48.05211 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f9f176d3-a0ad-3c9f-9e69-8d0dcf7d7b07 | -2.71839 | -46.26089 | 2024-11-26 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6c8e04d-6e50-3935-a3cc-a5e1e89fe7cd | -3.9888 | -48.06086 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c2de98d-5e90-36e4-8f65-b4f23ec03d8d | -3.17252 | -48.43829 | 2024-11-26 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 49058041-9ab6-3610-8d25-b8b02f395313 | -1.56259 | -53.7936 | 2024-11-26 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d7eb868e-18cf-373d-b422-0883cabe71be | -3.95429 | -48.06656 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3ec9d9d-9ed1-3f19-a6f7-10633d802db1 | -3.97888 | -48.09612 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 86420456-04cb-39d2-a3a7-c354e06529aa | -2.95809 | -48.61579 | 2024-11-26 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96631732-e313-3d53-a51a-409210c83f46 | -2.93502 | -48.82123 | 2024-11-26 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a861caf-2c31-3eeb-a6a2-835b244a487d | -3.39084 | -50.09398 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3bcc403-c3ae-31ca-88aa-cbcc1108a1d0 | -2.38727 | -48.60257 | 2024-11-26 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4871188d-ff75-3cd6-846f-5935c628fd3c | -3.97601 | -48.06214 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 224a258b-030a-3076-81e9-3c2235c64dfa | -3.28163 | -50.01913 | 2024-11-26 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dd9d9539-0b9c-3c86-a3fd-cc54edb07615 | -2.71768 | -46.26532 | 2024-11-26 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d7111ab-cb98-38a2-809e-653f08f4dd26 | -2.18973 | -45.6047 | 2024-11-26 04:14:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 59794dd9-7f30-350c-ba95-8bed50f9a383 | -4.25811 | -48.67168 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b251b9e1-7479-3d44-afeb-5f65596c5e1e | -3.98066 | -48.05931 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7ce1dfd4-a111-3010-8dc7-8b35087bec71 | -4.00399 | -48.07071 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| daf8f034-2e7a-37ca-b73b-84140ac17dec | -2.71854 | -46.28368 | 2024-11-26 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 30b8fbd4-8dcb-3da5-a58a-1fcf85948d46 | -3.17188 | -48.44226 | 2024-11-26 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| dcf5d0fa-d385-3a72-9750-eeb4ac5b36d8 | -3.39198 | -44.75291 | 2024-11-26 04:14:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c06955b7-5afa-321b-bd3c-c3f68d1874ba | -2.18949 | -46.36209 | 2024-11-26 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b84195c7-2c0f-35c9-a81a-e060b1984edc | -5.949 | -39.66933 | 2024-11-26 04:14:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 20.9 |
| e50ad755-f690-3be9-b57a-1db279a095ce | -3.2918 | -50.54072 | 2024-11-26 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 70aa6e18-aea6-34dc-8aa8-e1e65b221985 | -4.09532 | -44.85749 | 2024-11-26 04:14:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03330101-6abc-3588-a6fb-9b2d73902bd3 | -4.00458 | -48.06702 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e6e2541-797c-3e68-a05e-3f4ce30a95d7 | -1.00684 | -47.10293 | 2024-11-26 04:14:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95ddcccd-e246-35a8-b1ea-a877f1356f92 | -3.96245 | -48.09373 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a779e3ea-3741-30b4-a5ca-ec307138866e | -3.97369 | -48.05062 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e98f00e-59b9-302e-9747-f94ba70b0c4b | -3.9584 | -48.06712 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9c5b69d0-31bf-35ef-82ff-371ed48ed8da | -4.06569 | -50.00749 | 2024-11-26 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b77e57a7-4dea-3fe9-882c-2258f37cf81c | -3.37973 | -50.10256 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50476dfd-2e19-3c72-84c4-59bcfc02146a | -1.825 | -46.28784 | 2024-11-26 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72d90f00-6aa4-3baf-8ea3-0215c6e1e630 | -4.53463 | -43.29364 | 2024-11-26 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ac3bf765-5c50-360b-9dc4-a800224d3e20 | -4.81088 | -43.31249 | 2024-11-26 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c00f8ab-086d-35a7-8932-66151e26203f | -1.56178 | -53.79859 | 2024-11-26 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| de89f835-e35c-37b6-8636-67143fcb7140 | -1.19343 | -51.769 | 2024-11-26 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b25e3024-19a5-3125-a818-156ed52346e9 | -3.93014 | -46.49685 | 2024-11-26 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56ea0e85-4e96-3463-a672-40fe989ee17e | -3.9537 | -48.0702 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac0cd245-735b-350d-8ceb-343d3d209167 | -1.56366 | -45.67464 | 2024-11-26 04:14:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2fcced98-2924-3fa1-aa5f-41309afa04cf | -3.43944 | -50.01186 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d9ddac83-257d-3a4e-a50e-ed73a1892d19 | -2.17887 | -45.60306 | 2024-11-26 04:14:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1358d34-945d-3f1b-930e-b15186e68be4 | -4.53794 | -43.29415 | 2024-11-26 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| eef1e66a-daad-32d6-94a9-264c93ccc3a5 | -3.96126 | -48.101 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48d50fcf-bf85-3932-853f-d4cf5a64fbd0 | -3.38571 | -44.17351 | 2024-11-26 04:14:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07e1a18d-567e-3d21-a27b-6f24beb243c4 | -2.49402 | -45.03564 | 2024-11-26 04:14:00 | NOAA-21 | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae132824-2531-3d32-93a0-911cc5a68711 | -2.58101 | -45.47284 | 2024-11-26 04:14:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 20ab14fc-3b5a-37ed-9ef5-d92acf064494 | -4.55239 | -42.87678 | 2024-11-26 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03ab29e0-1c8d-3b34-ad59-defd0b48bdb7 | -3.29969 | -47.01844 | 2024-11-26 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2dd619b-8515-35d3-94ae-8dfac081d8e3 | -3.98 | -48.11511 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72b3d4cc-a29f-3b60-986e-dff0ef44f80f | -2.9402 | -51.29817 | 2024-11-26 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79544ce4-5335-3d9c-9be3-291151ed353c | -3.66176 | -43.39332 | 2024-11-26 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8508f05e-9a67-39bc-b3e2-45d0e797ff54 | -1.43602 | -47.31832 | 2024-11-26 04:14:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| d9b0e893-7bde-300b-9921-965a0018a773 | -1.67469 | -45.80453 | 2024-11-26 04:14:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74cce719-82f9-30ad-971b-51e7b80ce801 | -2.97019 | -48.00453 | 2024-11-26 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64a634cc-aafb-3795-85e9-cf6a6585a7dd | -3.98239 | -48.10038 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a42dc743-73b0-3a6c-b9cd-89c3a1c987a6 | -1.70208 | -47.72629 | 2024-11-26 04:14:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| beb27dda-a526-376d-86b8-8c5fd659ac00 | -3.44136 | -50.26883 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ee9747a-149f-3cfe-ba19-6b3e5bf2c506 | -3.9092 | -42.4193 | 2024-11-26 04:14:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 356f4515-2c22-3993-bc50-51e647e5c6ec | -2.88548 | -48.73581 | 2024-11-26 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca818ae0-72fb-3b83-95ac-54d806168650 | -3.38173 | -50.09616 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d7d47c00-e4e6-3f12-9615-eb2e0a59d540 | -1.60453 | -45.7717 | 2024-11-26 04:14:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 984dae5f-96a6-31cb-96df-65e8afbf02e6 | -2.60611 | -46.8096 | 2024-11-26 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 764108ae-3512-3fef-87bf-ab578d59978c | -3.97649 | -48.11084 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc238b6b-6509-3eae-aded-9c6e4c13784c | -2.93445 | -48.82121 | 2024-11-26 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7dcbcbf6-e5f4-3e08-864e-b06a9929079b | -3.86234 | -49.14294 | 2024-11-26 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f1b03b79-c433-376f-b769-d67a94c62124 | -0.87223 | -47.29662 | 2024-11-26 04:14:00 | NOAA-21 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4ab9fb47-0b85-30db-92d9-0fcc1f6a0742 | -1.13534 | -48.35805 | 2024-11-26 04:14:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 706a6039-3066-3ab5-937a-85d7c3179429 | -3.96961 | -48.04992 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d93ed52d-2a7c-3fe2-a78a-e59ee087ee80 | -3.15829 | -45.44223 | 2024-11-26 04:14:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2025c846-32c7-3732-848c-af5bb370e913 | -3.07545 | -49.50533 | 2024-11-26 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05da7f41-b2a2-36f6-96dd-e48fe3e38922 | -2.50152 | -48.34774 | 2024-11-26 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b59e02ab-2d18-33b7-93c4-b45e6954583f | -3.95655 | -48.10402 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 414249b2-8deb-380a-b733-977a8a86d8f3 | -3.5889 | -50.38742 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 57984914-6102-3b11-a09e-52e3134eedee | -3.2771 | -50.64795 | 2024-11-26 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9aef0805-e0cf-3440-9e38-7e51bda9d68e | -3.17613 | -48.44293 | 2024-11-26 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 5dd52c8f-d3cf-39cb-adef-797349b8464a | -3.95483 | -48.08887 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f60f69f-fdd1-3705-9450-b8ef16adfc18 | -3.97427 | -48.04708 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8eb4c73-bf7d-3ec1-bedb-e420afa5ebc9 | -1.60908 | -47.3865 | 2024-11-26 04:14:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d743f668-1b40-36e8-b038-52574ccffa32 | -5.31298 | -43.08072 | 2024-11-26 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 712cb975-3dc8-30d7-90f4-14d708678d04 | -3.9806 | -48.11143 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e738bd7-c06e-33ae-bcf5-ab35431c2caf | -5.30968 | -43.08021 | 2024-11-26 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 215954ac-57fe-36c0-8f4e-1121b00bc0bc | -2.0935 | -46.55328 | 2024-11-26 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8e77edb-cc9b-3e45-ae64-e7442d5e016e | -3.98357 | -48.06724 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63a79d9d-07fb-3590-bb6f-e023ab3e2486 | -4.25304 | -48.72786 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29991a87-1192-3d8e-bb15-47589df5c890 | -2.92449 | -45.15615 | 2024-11-26 04:14:00 | NOAA-21 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 274d2589-0ed0-370e-bb3e-144ff96c5e9d | -3.03961 | -48.50812 | 2024-11-26 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b1e21fb9-0c87-3279-a541-632e20878ea1 | -3.50282 | -50.46488 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14d4bc7d-46dc-36af-bd3e-ae56a0737481 | -3.38176 | -44.17659 | 2024-11-26 04:14:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 256c4bd2-da73-33c9-81c7-714f499c9281 | -3.91635 | -42.41687 | 2024-11-26 04:14:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 30635049-8ee6-37c6-8409-55652f8ca42d | -3.58598 | -50.64783 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7115b691-c7af-3299-a701-92392a89aace | -4.16385 | -44.07174 | 2024-11-26 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README16.md)
