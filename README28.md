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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8150e11-ff89-399a-b197-ee958c237b9c | -3.29733 | -51.60126 | 2025-10-14 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9900777-6064-3d2f-86cc-08eea1b8451d | -6.21732 | -41.56425 | 2025-10-14 04:23:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 076e3a23-ed97-3fec-994d-1b79a41ee80f | -5.86645 | -42.88101 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8aa6301c-b180-393c-b258-d1dcb6bbe47e | -5.15459 | -46.26071 | 2025-10-14 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0ae7dc5-e623-3b7a-9459-23d9896bf9d1 | -3.99657 | -48.34335 | 2025-10-14 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f38104c-d9dc-3ea5-b795-707144035e96 | -5.73812 | -47.47795 | 2025-10-14 04:23:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 76f317ca-3ddb-36bd-bbc6-36968b932b1d | -4.12878 | -42.21745 | 2025-10-14 04:23:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6173e470-7416-3eda-b125-65b417cf0bc9 | -4.92175 | -45.84207 | 2025-10-14 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 289707cc-8117-3e17-aeb3-61118df253a7 | -4.86861 | -48.65971 | 2025-10-14 04:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fbfa70f5-063d-37b3-ac45-2be802727c0e | -7.25268 | -40.59464 | 2025-10-14 04:23:00 | NOAA-20 | CALDEIRÃO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2202091 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0cceeaa0-e56a-34e3-9083-ea88e1645f5c | -5.28281 | -48.27665 | 2025-10-14 04:23:00 | NOAA-20 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5343f38c-4244-38c4-be46-39672b0ca0f4 | -4.66823 | -43.1229 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| cf0c0b84-2099-3861-989a-7fcc7b449abd | -6.33141 | -46.03676 | 2025-10-14 04:23:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84765317-a38c-3ce3-9861-a46ad7a7dc91 | -4.28134 | -48.57622 | 2025-10-14 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d674ec8-660f-3d87-a5ca-3d0440909ca2 | -6.28842 | -43.90626 | 2025-10-14 04:23:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 49df6a5e-8770-3790-a2b7-f678a74ffe16 | -5.832 | -47.65715 | 2025-10-14 04:23:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25db7c58-9356-367c-963a-45bb249e0cba | -5.56787 | -41.3243 | 2025-10-14 04:23:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 886c5901-4d7d-3c24-80e1-c535f35f85ac | -3.47019 | -51.64859 | 2025-10-14 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c58f9e9d-8c6a-36e1-85c9-0cbe0ab6cd9a | -4.8402 | -42.7778 | 2025-10-14 04:23:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 6b12d875-b593-33a0-a00d-d8a1710e50a8 | -4.88046 | -45.45788 | 2025-10-14 04:23:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a37a39cd-087b-3aa8-938d-93c1f844ef8e | -5.62352 | -42.68961 | 2025-10-14 04:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 180913f3-9b93-35da-ba32-4bba51111010 | -3.27592 | -50.04568 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d4549f8-f0f2-3f4e-9801-06627b80d257 | -5.59156 | -46.41887 | 2025-10-14 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83d4e7f7-99b1-31cc-9779-e6fb42f31b53 | -4.05169 | -47.25396 | 2025-10-14 04:23:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a4c476a-4f26-3631-b3c5-367ea3ff52cf | -5.99264 | -42.87245 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| dbba3b4f-adbd-39c1-9575-229a0d065abb | -4.40357 | -50.62419 | 2025-10-14 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a8894da-9a38-3a4b-8b2b-1bda3817614b | -5.5921 | -42.575 | 2025-10-14 04:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2d3d79c7-f552-3864-ad37-c32c79cd9b38 | -5.39359 | -51.38272 | 2025-10-14 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18279430-7624-3133-9817-6a5bf542b6d4 | -2.07278 | -52.00444 | 2025-10-14 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ac3280c-08f9-3470-bb06-a11908f6d4ab | -4.9179 | -49.319 | 2025-10-14 04:23:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aae729e7-dd08-3762-8e6c-38f586bfb457 | -4.66585 | -43.1385 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2854ce6d-31ea-336b-9383-e2dcbac10787 | -5.54664 | -46.38 | 2025-10-14 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75e59a6b-b53a-3a14-8a7d-7be396c2de2a | -3.88927 | -44.91298 | 2025-10-14 04:23:00 | NOAA-20 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31c70326-b948-341f-a01c-62f3c3e8679e | -3.15884 | -42.88774 | 2025-10-14 04:23:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e913d07d-b2b4-37cf-8d1e-bfe7bc33a765 | -6.22197 | -41.55964 | 2025-10-14 04:23:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1a9f3d6a-015c-33c9-a315-0bcefb6998b9 | -1.47538 | -52.9868 | 2025-10-14 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 062d71ef-2f49-3651-8fdd-d24871fb76cf | -5.8321 | -49.02034 | 2025-10-14 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3da2c13-1b3c-311c-89c0-c28522cc8680 | -5.48547 | -45.41116 | 2025-10-14 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 41ae3835-9aab-365e-affe-dc9be3b56f3d | -3.13255 | -50.20971 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7482db93-70da-31df-a9b6-822bda5e4dd9 | -5.96743 | -42.24952 | 2025-10-14 04:23:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e8616e17-3870-30f1-a26f-470922bc772c | -6.21765 | -42.49331 | 2025-10-14 04:23:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| adaa1ca2-975c-3bce-95f8-29101af5f492 | -4.23403 | -48.68647 | 2025-10-14 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 030a0f32-4d7c-388e-8249-1fff3d31b6ba | -5.62416 | -42.6854 | 2025-10-14 04:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 077bc422-d0b3-343c-868b-0d16ac1c30b2 | -7.4017 | -39.78342 | 2025-10-14 04:23:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b58ebcf5-cee3-383f-bec0-6cf5579fe131 | -7.08442 | -41.95173 | 2025-10-14 04:23:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 2723947d-c138-3f33-b687-96ae9e303f22 | -5.54189 | -46.1312 | 2025-10-14 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9b5f71f-ddb9-3c30-9fd0-408487481b92 | -6.17685 | -42.61449 | 2025-10-14 04:23:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 24f11bd6-1da1-3761-a547-e933b287d32f | -5.40601 | -40.88552 | 2025-10-14 04:23:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9d6e7831-5152-3b8f-9bc6-096c50469642 | -5.73553 | -40.76985 | 2025-10-14 04:23:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 5fc9e3a7-8043-3ef3-95fd-a8b7eea9e59f | -2.88086 | -50.73734 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| faef3b9f-5826-3958-b9cf-f7de082839db | -5.9737 | -43.56768 | 2025-10-14 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf59e65e-70ed-3ce5-bd74-4575afabd2cb | -3.45673 | -50.09395 | 2025-10-14 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10beedaa-fddb-3b32-a37b-ec8863f2291c | -4.8444 | -42.77423 | 2025-10-14 04:23:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 7f1266e7-48a6-3eae-bc52-15a917ed3790 | -5.11848 | -45.49908 | 2025-10-14 04:23:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a40dd445-3ecc-3c57-9937-bf897910db8d | -6.4417 | -41.82834 | 2025-10-14 04:23:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a0b78b6a-e1a7-32f1-ac3e-5acfc3581c63 | -6.45075 | -43.99268 | 2025-10-14 04:23:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0cb534a-9510-301a-9782-2990b5f21ec5 | -5.30754 | -45.52846 | 2025-10-14 04:23:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3abd467e-50a3-3200-b83e-4562ce9ba596 | -3.29189 | -50.17337 | 2025-10-14 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ddeb3567-23af-34ec-84ee-696e07cf26fc | -6.29712 | -42.98659 | 2025-10-14 04:23:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 565bafd3-49fe-356f-b3d3-12ae1589dcd9 | -6.02566 | -43.3998 | 2025-10-14 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7cb3b6bb-fad2-3a29-9cc0-c7099495490d | -6.67934 | -43.56976 | 2025-10-14 04:23:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 846b924c-34bd-35ae-94a9-3c141027569c | -5.22162 | -50.95265 | 2025-10-14 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b62d40e-11af-32dd-9fce-9c3564987dbc | -5.83064 | -42.31174 | 2025-10-14 04:23:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 928ae3d8-c18f-3907-8444-7d947681cf1f | -4.02926 | -45.01667 | 2025-10-14 04:23:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0760b83e-57be-3f28-a6d6-7b1503ead740 | -6.47151 | -43.94975 | 2025-10-14 04:23:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7ad27ec5-79be-3841-881e-0889fd88d625 | -6.45467 | -44.57658 | 2025-10-14 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0397510f-94c9-33d8-afb5-ebc5a73f43e3 | -4.62672 | -45.77409 | 2025-10-14 04:23:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7dcdaad5-e5ca-3764-9953-b7787cabbd84 | -4.84435 | -45.2113 | 2025-10-14 04:23:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9389954-7a07-3441-838c-94c07a1f2085 | -1.80243 | -47.7046 | 2025-10-14 04:23:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b45cf411-1f1e-3898-9520-985cb0b70f45 | -5.95998 | -42.29798 | 2025-10-14 04:23:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e8763fe0-816b-30bc-85cb-2117a417ee17 | -5.85165 | -46.44965 | 2025-10-14 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af3169d1-9241-3c56-89ba-9e8b8ffc94f2 | -4.22975 | -43.0112 | 2025-10-14 04:23:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfc62ae5-776b-3d11-ab7c-965af77b4498 | -2.94753 | -49.02659 | 2025-10-14 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| add2f126-4ea3-3e15-9e33-55789294b6d4 | -5.97477 | -44.93354 | 2025-10-14 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2f5d95af-07c4-3ac4-a3f0-28f20a20e883 | -3.04401 | -40.11273 | 2025-10-14 04:23:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| f262aeae-acf2-35fd-ae87-d9a0256d6b9d | -4.61752 | -43.61535 | 2025-10-14 04:23:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7848aec-6c31-321b-9966-d246c00de691 | -0.90053 | -47.54702 | 2025-10-14 04:23:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| aa263945-2fad-31cd-97c2-4346e314d755 | -4.30227 | -50.40482 | 2025-10-14 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aebca4bb-0915-346e-8765-d5e85bfddbe5 | -5.94067 | -43.73508 | 2025-10-14 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2ca037a4-e170-39c3-be10-b3d611a44db2 | -5.86749 | -42.8265 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 01269bca-016a-36b4-bdd4-8f584c319183 | -6.4603 | -44.58484 | 2025-10-14 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e17d1d8c-1929-35dc-823d-90479f2ea7a7 | -5.6455 | -51.08923 | 2025-10-14 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2b9231d-389f-377c-b471-f226675681b0 | -5.62492 | -42.58199 | 2025-10-14 04:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 24585ea1-7555-367e-8be2-1b86ff8c38fe | -5.97777 | -43.56439 | 2025-10-14 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b377289-1948-3e66-895f-db7c553e5f6d | -5.88696 | -42.90429 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b64455f8-7a61-356b-9fe8-39877fb23386 | -3.09546 | -50.38645 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c567b24d-9eee-30e8-b065-f1eb605b7431 | -4.66936 | -43.13903 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09057fb6-76ce-3cf7-9535-8c45291ee521 | -6.18358 | -41.76585 | 2025-10-14 04:23:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 1b292508-ef36-39e7-a1d7-49c74333e5cf | -5.56789 | -43.00819 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85099ff6-3383-3164-8bb0-b575a0b0cbc3 | -3.35141 | -51.63013 | 2025-10-14 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b86044a9-ed9f-3d6a-a66d-7e81255c5a6a | -4.28558 | -48.57273 | 2025-10-14 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 293d7928-8a85-3c35-aa99-5275b65710b9 | -5.59637 | -42.57141 | 2025-10-14 04:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 981dee60-0422-3e8a-a3a5-a14b25a8b0be | -3.12512 | -50.20506 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 15c44e44-6163-385d-8232-f6ce5b6b8c10 | -5.59508 | -42.57978 | 2025-10-14 04:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 10a2942f-ce66-3906-add5-f994db340930 | -4.5306 | -45.58635 | 2025-10-14 04:23:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e971c184-a8e7-3d2b-8381-5b9efbdfa9dd | -5.1551 | -39.50975 | 2025-10-14 04:23:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bff6e644-a173-3ecf-84ad-b08929b66224 | 0.39401 | -51.04242 | 2025-10-14 04:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a827ac58-e08c-3e0b-b87e-c2ba0a6ab5a8 | -3.13655 | -50.21033 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf79b0b4-6556-3bfc-a405-de695d9c5852 | -5.10449 | -43.20219 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 901600ab-2741-35aa-a901-aa53b0939c05 | -5.74363 | -40.77122 | 2025-10-14 04:23:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |


[Clique aqui para ver as próximas entradas](README29.md)
