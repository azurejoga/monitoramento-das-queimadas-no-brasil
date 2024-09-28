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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8823f4d-ce00-32dd-ab5b-a92908305c24 | -8.0762 | -42.910198 | 2024-09-28 00:14:02 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ee8e9886-59de-3130-ad6e-278fa1df1302 | -9.5562 | -50.162899 | 2024-09-28 00:14:03 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| daffb126-8e13-3648-8778-3a08471f1e34 | -7.8966 | -42.6614 | 2024-09-28 00:14:04 | METOP-B | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 05a62c2e-9549-356a-b00b-c75b52eb3da4 | -7.8703 | -42.681702 | 2024-09-28 00:14:04 | METOP-B | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 79293fce-0c1d-3531-b927-f1b8e0b4ea88 | -9.3787 | -49.989101 | 2024-09-28 00:14:05 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fad2fa3a-5f12-3728-bc9e-c1313ad02786 | -9.3818 | -50.004299 | 2024-09-28 00:14:05 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 99cb4fe6-6f06-3a0e-b98f-bbab30f48a5e | -9.369 | -49.9911 | 2024-09-28 00:14:05 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 71a62a04-bbf3-35ae-8e70-4392e0affa36 | -8.363 | -45.465 | 2024-09-28 00:14:06 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2f7a3461-e0a4-3a44-bbb9-fd48dd1ca255 | -8.2371 | -44.8419 | 2024-09-28 00:14:06 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 677efc6b-80c5-3924-b30b-33c9b1e44e81 | -8.2388 | -44.8494 | 2024-09-28 00:14:06 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a71aa357-38ed-3026-b73b-b5c91ff5fa95 | -8.3647 | -45.4729 | 2024-09-28 00:14:06 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4995fcf9-46cc-335a-af6a-2e646cea005f | -6.9328 | -39.403198 | 2024-09-28 00:14:07 | METOP-B | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 3ef7cecc-6b9d-32e0-a88d-44279c13dc25 | -6.9349 | -39.411999 | 2024-09-28 00:14:07 | METOP-B | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 70f4701b-b7ba-3144-9eae-7dd18ef87c7e | -9.3409 | -50.701099 | 2024-09-28 00:14:08 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6464dbec-9a78-3a53-91f9-5b08fc394e9e | -9.3444 | -50.718201 | 2024-09-28 00:14:08 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cafb7ea-90b0-3665-8024-3cc627d71f1b | -9.3478 | -50.735298 | 2024-09-28 00:14:08 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e578462-28ee-3bd2-b157-cde880751a9a | -9.3347 | -50.7201 | 2024-09-28 00:14:08 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 109a1929-95a7-3819-ac94-2b7c4b170fb8 | -9.3381 | -50.737202 | 2024-09-28 00:14:08 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 002d8bea-5f0f-3532-bb9e-d2718237f74a | -8.4005 | -46.348999 | 2024-09-28 00:14:09 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b29c5289-dafc-3067-a89b-dade55f8a7d7 | -7.8946 | -44.592701 | 2024-09-28 00:14:11 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a9b92ecb-2fdf-326b-95b1-86fa6a7ce9a0 | -7.8962 | -44.599998 | 2024-09-28 00:14:11 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bea57266-04d5-3d87-84b5-6c311179c029 | -7.8978 | -44.6073 | 2024-09-28 00:14:11 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2626fd82-ce6e-375d-ad76-995bd0b725fc | -7.8994 | -44.614601 | 2024-09-28 00:14:11 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fc3e1711-ca1e-36b9-becd-da7b7da2966b | -7.8815 | -44.580399 | 2024-09-28 00:14:11 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6c04f015-7ec6-3ec8-8f97-453aaa5dd3b3 | -7.8831 | -44.5877 | 2024-09-28 00:14:11 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4fa9e404-6c6a-3f91-97d1-a79b0601fe70 | -7.8848 | -44.594898 | 2024-09-28 00:14:11 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d6d257c0-fe58-31f7-af2c-e181bc4bda05 | -7.8864 | -44.6022 | 2024-09-28 00:14:11 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a49e58c8-bb50-3e64-8bfb-42e962ef5546 | -7.888 | -44.609501 | 2024-09-28 00:14:11 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b48ac975-800a-3eb4-a92c-483cf0e17489 | -7.8896 | -44.616798 | 2024-09-28 00:14:11 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 87daacaa-b42b-3987-81c1-25b2631771b2 | -7.8717 | -44.5825 | 2024-09-28 00:14:11 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7377981b-532f-38a9-8d04-98d8fbc63265 | -7.8733 | -44.589802 | 2024-09-28 00:14:11 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e437cdc0-d3d0-3d55-9fc6-bbb062e0006b | -7.8749 | -44.597 | 2024-09-28 00:14:11 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| eee13844-2334-3a71-acef-f5d225cf18c3 | -7.8765 | -44.604301 | 2024-09-28 00:14:11 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9a38f8f1-8de9-3b46-9063-172a3c17ccd3 | -7.8781 | -44.611599 | 2024-09-28 00:14:11 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c2929f54-708d-3c92-a8a3-3be660d3a94d | -7.8797 | -44.6189 | 2024-09-28 00:14:11 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dac34ffd-14bb-3d66-9fbe-83ba2dd86ecb | -7.8813 | -44.626202 | 2024-09-28 00:14:11 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cc64fb78-34f9-3746-8585-7b526ca1d470 | -7.8619 | -44.584702 | 2024-09-28 00:14:11 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 98467b1c-088e-3d4b-8b9d-4d9cf82467cd | -7.8635 | -44.591999 | 2024-09-28 00:14:11 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 075fc43c-cc37-3031-aa88-c0468be8d604 | -7.8651 | -44.599201 | 2024-09-28 00:14:11 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 74372566-65e1-380c-abc8-9763471f834f | -7.8667 | -44.606499 | 2024-09-28 00:14:11 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0e7aa3d1-295f-3f89-836c-04c749b8a42e | -7.8683 | -44.6138 | 2024-09-28 00:14:11 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 09a48310-a0e5-3830-9a26-435e71bed786 | -7.8699 | -44.621101 | 2024-09-28 00:14:11 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 97e2f020-7b5a-347b-8f83-d06396b944d9 | -7.8521 | -44.5868 | 2024-09-28 00:14:11 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 89d8ecdd-93b3-34e4-8cf6-fb6430dcdfcc | -7.8537 | -44.594101 | 2024-09-28 00:14:11 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 02c8c152-27d4-32b5-bf36-fd0a3b50b0bf | -7.8553 | -44.601398 | 2024-09-28 00:14:11 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f0023633-d85c-3dcc-9f21-f06ccc8df0dd | -7.8569 | -44.608601 | 2024-09-28 00:14:11 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9bfe2109-feb7-3f71-b505-a0b7be1aa27a | -7.8585 | -44.615898 | 2024-09-28 00:14:11 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dedc17a6-7800-3313-846a-1d5248fe7d2c | -7.189 | -41.766399 | 2024-09-28 00:14:12 | METOP-B | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bfcebe83-2952-3087-aa8c-c448d5bdddc0 | -7.8455 | -44.6035 | 2024-09-28 00:14:12 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 54050ef1-e9ce-381c-acb6-c72c74c43230 | -7.8471 | -44.610802 | 2024-09-28 00:14:12 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e1200223-488a-3936-b29b-62339e4cb53e | -7.7963 | -44.660198 | 2024-09-28 00:14:13 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bbb16d21-7469-3a50-bc88-1748d5fd37a7 | -7.7979 | -44.6675 | 2024-09-28 00:14:13 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bd950b91-a787-3b96-8303-9879ec3de7c6 | -7.7849 | -44.655102 | 2024-09-28 00:14:13 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0e91799e-72c2-3658-9066-e48514662445 | -7.7865 | -44.662399 | 2024-09-28 00:14:13 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6aa4d86e-570f-3cb3-aae8-3c15d15fe708 | -7.7881 | -44.669701 | 2024-09-28 00:14:13 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a0e42c70-fa36-3eb0-8f67-9542845263fe | -7.7735 | -44.649899 | 2024-09-28 00:14:13 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bc8ed679-ec14-3007-965b-ae0a85b91b14 | -7.7751 | -44.6572 | 2024-09-28 00:14:13 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c1f4d196-9653-318e-a9a1-03e7ec9d13e7 | -7.7767 | -44.664501 | 2024-09-28 00:14:13 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1a39264f-5059-3e70-81f1-1965f5eb70d9 | -7.7637 | -44.6521 | 2024-09-28 00:14:13 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 16ab69c8-14ef-3f59-b419-7acd4f9bf508 | -7.5705 | -43.872898 | 2024-09-28 00:14:13 | METOP-B | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7f31cb82-c873-35fc-8d90-36c4b38d188c | -7.2058 | -42.476299 | 2024-09-28 00:14:14 | METOP-B | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 462fd4fa-3578-32ee-a3f9-3042611dfb64 | -7.2073 | -42.4832 | 2024-09-28 00:14:14 | METOP-B | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8cbded0f-d83a-36d3-a9c0-6360ed779654 | -7.0637 | -42.076801 | 2024-09-28 00:14:15 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b158d164-5163-3fe0-87c7-59d197be0556 | -7.477 | -43.7766 | 2024-09-28 00:14:15 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 595279d9-b778-377c-98e2-565bf772fe32 | -7.4626 | -43.7579 | 2024-09-28 00:14:15 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c2d0c7fb-61b7-374f-98b4-93503c0c1a31 | -7.3005 | -43.033699 | 2024-09-28 00:14:15 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6ff69cdc-eab8-3efa-a99f-158ae33c8b9b | -7.831 | -45.4739 | 2024-09-28 00:14:15 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f0abbdfb-8746-3ad2-ad33-0f72d65ed166 | -7.8327 | -45.481701 | 2024-09-28 00:14:15 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5a29832e-228f-3f1e-9565-1eb0314a0460 | -8.753 | -49.762402 | 2024-09-28 00:14:15 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4347fe3-428d-3137-965a-7417f3418854 | -8.7433 | -49.7644 | 2024-09-28 00:14:15 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f58f24e7-c794-38b8-8a3c-c432d6fda34b | -7.8216 | -45.525101 | 2024-09-28 00:14:15 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e4fae33-b89e-3902-abdb-9b78bb324d21 | -7.8233 | -45.533001 | 2024-09-28 00:14:15 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7c1914fd-4876-3cd1-8a1a-2f85f4adb3c1 | -7.8101 | -45.519402 | 2024-09-28 00:14:15 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 42049d1e-3981-3555-9084-69db0da4c747 | -7.8118 | -45.527199 | 2024-09-28 00:14:15 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 93da3260-77c3-3da5-8eba-0111466ad8ed | -7.8135 | -45.535099 | 2024-09-28 00:14:15 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7395175f-861f-3a7a-b375-4422febdfdc2 | -7.8153 | -45.5429 | 2024-09-28 00:14:15 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a3e19a3b-b98a-3a19-981a-5f51ed765e3e | -7.817 | -45.5508 | 2024-09-28 00:14:15 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f96a6fde-1359-3926-972f-6bde4c379912 | -7.8187 | -45.558701 | 2024-09-28 00:14:15 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f1b3089-c03b-3ce2-8150-fd6225542b7b | -6.7855 | -41.2188 | 2024-09-28 00:14:16 | METOP-B | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| aedcd387-5cf6-32f4-8460-ea61d952b892 | -7.1289 | -42.5009 | 2024-09-28 00:14:16 | METOP-B | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4a46bc0b-8fa1-3c22-be4b-d2f22ab1caef | -7.1305 | -42.507801 | 2024-09-28 00:14:16 | METOP-B | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 221aeb51-497b-3c18-a8a8-dadc51a533a3 | -7.1336 | -42.521599 | 2024-09-28 00:14:16 | METOP-B | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9ac42998-bfff-3c61-9b2f-f893f655c565 | -7.1352 | -42.5285 | 2024-09-28 00:14:16 | METOP-B | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b6b53036-8aba-3676-b906-2ba9699e303a | -7.8089 | -45.560799 | 2024-09-28 00:14:16 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4461f52f-e5b9-347e-8842-1815b92122f7 | -9.0358 | -51.495201 | 2024-09-28 00:14:16 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49809cc9-e6f7-3740-a488-3eb5383f95eb | -7.3823 | -44.091099 | 2024-09-28 00:14:17 | METOP-B | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5646e03d-1c4f-3b63-b6d1-ef1115399ca4 | -7.3838 | -44.098099 | 2024-09-28 00:14:17 | METOP-B | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c43c46c6-ad74-33ce-ae16-a1743b94aabb | -7.3678 | -44.072201 | 2024-09-28 00:14:17 | METOP-B | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ae2c2ccc-c95c-3288-ad01-50cbec6eceb0 | -7.3693 | -44.079201 | 2024-09-28 00:14:17 | METOP-B | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 936a211c-2f83-3d9e-a5ac-a90f6716596c | -7.3709 | -44.086201 | 2024-09-28 00:14:17 | METOP-B | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 02235c1a-50d1-306e-ad2c-7bfca77d01a5 | -8.553 | -49.582699 | 2024-09-28 00:14:17 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffdf593b-269c-3d07-ac8f-04ccb9afad55 | -8.5433 | -49.584801 | 2024-09-28 00:14:18 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8356bfeb-5626-3aa3-885b-b541846d5faa | -7.7523 | -46.149799 | 2024-09-28 00:14:19 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 592dc8e3-fd25-3420-ae57-e67e71312a93 | -7.7542 | -46.1581 | 2024-09-28 00:14:19 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff7c2b1a-fc88-359e-9619-1c8f79d9722c | -7.4235 | -45.161499 | 2024-09-28 00:14:20 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5abc8f37-55bf-3762-ba43-cab2f93927db | -7.5592 | -45.781101 | 2024-09-28 00:14:20 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3040525e-45fb-32db-8aa3-10e00479686f | -7.561 | -45.789101 | 2024-09-28 00:14:20 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f2af10b7-7523-3d58-b5e3-1cfdb488cf78 | -7.5627 | -45.7971 | 2024-09-28 00:14:20 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b65beb2c-ea49-327a-81a5-2b200210b069 | -7.5165 | -45.773701 | 2024-09-28 00:14:21 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7dd5e6c9-2478-3c71-82cd-610446cc6f35 | -6.6217 | -42.0364 | 2024-09-28 00:14:22 | METOP-B | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README7.md)
