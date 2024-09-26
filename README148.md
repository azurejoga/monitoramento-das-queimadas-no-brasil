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

## Dados Diários - Página 148

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36f2de06-040f-35e2-a33e-68f2872751fa | -17.0871 | -56.16444 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 74.8 |
| 696ddb16-7639-34dc-a77b-8b40863850e1 | -17.08707 | -56.18663 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 3d8924bb-737c-3fb8-93f0-75359b2aaa1b | -17.08595 | -56.19384 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| b42a7d23-ec45-3c6c-bb24-c677ea649d39 | -17.08543 | -56.17526 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 24.3 |
| 9607924d-198f-3495-8d09-c6517cabebd7 | -17.0854 | -56.19744 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| c855cbb3-9042-30f2-b7b7-5ad896261b5e | -17.08487 | -56.17887 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| abad0219-d1a8-3025-b42d-24484d8249df | -17.08484 | -56.20104 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b2168981-d68a-3815-b66f-d4ad361dfb49 | -17.08434 | -56.16029 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 55d35278-3502-33da-82c9-0897c899b50c | -17.08431 | -56.18247 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| ccfce84f-44da-3816-8628-10fdba7a2a52 | -17.08379 | -56.16389 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 61.5 |
| a9c24503-645f-35c9-bb97-fa5194195554 | -17.08376 | -56.18607 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 904a1526-66b2-3a82-a76c-bf2941dd786c | -17.08323 | -56.1675 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 61.5 |
| d1fd37f5-27ac-335b-9418-ca2fd8ee1d71 | -17.0832 | -56.18968 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| e75247b6-3eb3-30fe-bf0c-6952fdee094f | -17.0827 | -56.149 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 7882ac6a-80a6-382e-a7fb-fbf609ed30a9 | -17.08267 | -56.1711 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 18.3 |
| ffffec6c-021e-3bfd-b113-1e6113efd53a | -17.08265 | -56.19328 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 8c72ed11-2480-3286-93af-3b03acdbe599 | -17.08214 | -56.15252 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| d1e62d07-a13f-3d95-bd10-03010c4c910c | -17.08212 | -56.17471 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 18.3 |
| 8b483f43-aed7-3a15-a34a-a5abb2f9cf24 | -17.08209 | -56.19688 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| e666950c-50c9-3a69-99ae-08d7aa8daed4 | -17.08156 | -56.17831 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 23.3 |
| bac5f997-4965-3611-8c5d-dfb7cebfc4f6 | -17.08153 | -56.20049 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| fb795886-1bf0-35e3-91d0-cbed2b6e408b | -17.081 | -56.18192 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 23.3 |
| d17f0ecd-83f8-3cf9-b71b-562495cded30 | -17.08097 | -56.20409 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a4ef427e-24b0-3213-be9d-373a4e9e370f | -17.08045 | -56.18552 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| aa5ce4d9-918d-3a62-a943-5182ee1a8757 | -17.07989 | -56.18913 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| f58a2f7b-c7d4-3b33-a5bc-5f642ba87802 | -17.07939 | -56.14845 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 3ed0fc3d-8006-38f6-99d9-17f75fbf102f | -17.07936 | -56.17055 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 18.3 |
| 1c2e5baf-f17f-3cd0-9709-a15b7ef86759 | -17.07933 | -56.19273 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 9afa4bad-ac79-3db1-a7b4-892404d95a3c | -17.07881 | -56.17415 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 18.3 |
| 314a74bc-d215-3af3-a58a-ef3a4fca4b87 | -17.07828 | -56.15557 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 00f97058-dcc3-3e7d-813f-7ba41ffef3c0 | -17.07825 | -56.17776 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 23.3 |
| 2cac9ee0-cb26-365a-ac0e-6c10ecd17bfd | -17.07769 | -56.18136 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 23.3 |
| 8f2ec62a-99e6-3f0f-bd76-7dbea34a982d | -17.07714 | -56.18497 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 455c6d37-91fa-33c4-b0cc-c76f3b22a2e9 | -17.07658 | -56.18857 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 70ca13dd-a6dd-361c-8e3a-19deab1cd5ea | -17.07608 | -56.1479 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 46a186e4-4eb4-30c6-9236-03b4452eedc1 | -17.07605 | -56.17 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 27f60222-2ba9-3653-824b-b49426d2f180 | -17.07603 | -56.19217 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 0d363707-b0b3-3327-a6bb-a9a1cca4881a | -17.07552 | -56.1515 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 96515f8b-4b9d-34b1-a201-db8e3284761f | -17.07547 | -56.19578 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| af2257e2-fb5a-3994-9a14-b25385c8ec53 | -17.123 | -56.15195 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 561ab8d1-ad45-3338-a9fa-fbce84390f0d | -17.11913 | -56.155 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| fb9460a1-3119-3bf1-a000-0e4749891fa8 | -17.11748 | -56.1437 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 9e3a4554-048d-3dfb-9f44-29d86c2f98fd | -17.11693 | -56.14724 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| d31540df-d4f5-371d-bbcb-15ec712d9374 | -17.11306 | -56.15029 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6880d180-76df-38ac-aff7-7ea5132f0d1c | -17.11031 | -56.14613 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 73cdde46-9d18-354b-80d1-7b6102117981 | -17.10975 | -56.14973 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 820ed8c8-4fc1-337e-b7b8-8cda37a44676 | -17.10919 | -56.15334 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 4873f24c-47e3-365a-bea5-606ed65e9cd6 | -17.10644 | -56.14918 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8061ad3b-f9ed-3a99-89a1-a097b4bf3fcd | -17.10588 | -56.15279 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ffde0579-07c1-36c6-b296-a1efd069dd85 | -17.10423 | -56.1415 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| b26b844a-9e98-3ae5-add9-eff6814556b9 | -17.10201 | -56.15584 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 44323b28-1976-39ca-bf72-e798164ebae1 | -17.10148 | -56.13734 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| d4efdc38-297d-3a3f-a29b-2f13eb5def3a | -17.09706 | -56.14392 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9ec27a3f-15b6-35f6-a00c-b193e9cf5a38 | -17.0965 | -56.14752 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 98d1af71-c57f-35ad-a742-e5132dd68066 | -17.09595 | -56.15113 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 021ecefc-9155-3327-afb5-06de07e3c1a5 | -17.09539 | -56.15474 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b6c0b67e-8a5f-3a7d-90b4-460c890ef229 | -17.08712 | -56.14234 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 53580ca4-50e1-3511-bb85-a0c868b63d63 | -17.08657 | -56.14594 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 6d35bea8-9315-377a-b16b-89c750cde58d | -17.08159 | -56.15613 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 02f415cc-e7c0-31b9-bec1-83fd6cd93f14 | -17.08105 | -56.13763 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e766ca7e-8e14-3ca6-a3b4-1caa5596a0c0 | -17.07883 | -56.15197 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7f875a56-b1ca-31a1-ba6a-dfc1a9820b04 | -17.0783 | -56.13346 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| d286743e-df8b-3f88-9748-3e56836f64ee | -17.07497 | -56.15502 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 0b491030-9350-3632-83c3-ba2f8b729cf0 | -17.07332 | -56.14373 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9051ffc5-43d2-32b5-a3db-1fec27659049 | -17.07001 | -56.14318 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6d28ccc2-40d5-36c4-858a-1cd03f0d64e3 | -17.0667 | -56.14263 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| b096187f-81af-3970-97ef-2060ec235737 | -17.06503 | -56.15344 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b0e4f13a-0840-357b-b2fc-60809266f6b1 | -17.06339 | -56.14207 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| ed258668-3601-3c78-90a6-a3c35438dc9f | -17.06172 | -56.15289 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| deacc15b-442d-32a9-85f4-6df25a12f390 | -17.10221 | -56.35165 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| ce4111d6-a1a9-338e-b322-e7e3a3776b2f | -17.09891 | -56.35109 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 59f97fde-d987-3cb9-9e10-1cfe7fb1ead5 | -17.09555 | -56.37267 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 289c7a86-8cac-333a-8e30-9adcd60bbc81 | -17.09224 | -56.37212 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| a824b92f-b5a2-3e92-8205-9fa94e09b782 | -17.09173 | -56.35358 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 013f7af2-3479-3201-9c82-79069c957004 | -17.03431 | -56.39557 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 5a3fc163-7305-3e4f-acd2-0862de07a92b | -17.03156 | -56.39143 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 1c23bb34-e660-3aaa-a831-f5e62b227cb9 | -17.01715 | -56.33015 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 348d7a0b-0328-3cdd-bb9f-514ba0f4f6fc | -16.9953 | -56.23056 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 357ef4c4-8f07-300b-b6ec-36890ea3f10a | -16.94288 | -56.24024 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2fdbf4fb-c714-33f0-b951-cd5b71df503b | -19.11503 | -57.48531 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 950ebd16-9eb6-3e5a-8e62-a9ea65be9b9e | -19.11331 | -57.49614 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 9b3510b6-8ac0-3d52-880b-4fa1e1e33f46 | -19.11173 | -57.48473 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a350623f-a389-3d40-89b2-efa4fcfdce53 | -20.05231 | -57.94683 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2812865a-f857-3cac-ba50-0a5a53c1975e | -16.35838 | -57.67076 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 23ca899b-36cb-33bb-94ae-bbf3cb4144a4 | -16.35443 | -57.6739 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5fdb515e-a6a6-311d-8a7d-89f7fc43be02 | -16.35108 | -57.67335 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ae0a0a67-049d-38ed-8753-b21960cca2ae | -16.13516 | -57.53394 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8b20509b-6cc6-3f91-967d-305bf66dd73c | -16.13242 | -57.52965 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 96f76e17-b038-3c81-aa6e-5865e778bc13 | -16.13182 | -57.53337 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 0dfd535f-0c23-3af2-8e33-b8a6784ab9a2 | -16.12969 | -57.52537 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 16677d3a-9648-3759-8f48-aff0d21f086c | -16.12908 | -57.52908 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| dc15cbbc-10a1-38ad-91cb-4df89ca47744 | -15.96494 | -57.21717 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e4917542-a118-3dd8-b6c1-438e83fb8734 | -15.96219 | -57.21301 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e31d484f-589e-32f5-b96d-fe5234af1124 | -15.96162 | -57.21658 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3cfce26d-cc92-3738-af20-7c8901008330 | -15.92296 | -57.20235 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7797d2f-0683-337e-8387-4ff7e2f48929 | -15.91964 | -57.20176 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5bd8fee7-a97f-3ace-a84b-9785b31b992a | -15.85724 | -57.40017 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd9be774-d81b-3fb6-9206-41ebaf3af6f7 | -15.85666 | -57.40376 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e74052dd-8065-3656-b8af-552811dd9f82 | -15.85507 | -57.3924 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 195e9d19-e177-3d72-bec9-a12d34e8bf77 | -15.85449 | -57.396 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README149.md)
