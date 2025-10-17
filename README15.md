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
| 78a80f18-b888-3b0f-a4a0-5586f0c682d4 | -11.5729 | -44.0501 | 2025-10-17 00:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| ca014d65-9519-3d7b-9812-08a2db94f5f0 | -10.5831 | -47.4423 | 2025-10-17 00:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 349cb103-2e37-3c8f-9439-ba75a5781cc8 | -9.0821 | -48.0252 | 2025-10-17 00:50:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 8905d2ad-d037-368b-9c9c-a600fa414468 | -4.3872 | -43.406 | 2025-10-17 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 170.8 |
| 3b724d11-e0e8-3a4b-9d2b-d5facbc1e542 | -2.8644 | -50.7361 | 2025-10-17 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 156448fb-0fae-3e7a-85d5-e1cc3e80c93d | -4.4061 | -43.3816 | 2025-10-17 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 57e7390d-d801-3cef-ac72-499eb66b913a | -9.879 | -47.6779 | 2025-10-17 00:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| bff948a9-ad4d-3f54-a3f2-9e1d898f96b1 | -4.9548 | -44.956 | 2025-10-17 00:50:00 | GOES-19 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| c09af8f8-2989-3a15-8ab2-f04ab6cc060a | -3.5213 | -52.4728 | 2025-10-17 00:50:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 0eaefac5-b367-3d0b-a885-f98b8bbc3fce | -10.5128 | -43.4525 | 2025-10-17 00:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 40.9 |
| bb3e75e1-bf03-3122-9ab8-bf55099231aa | -9.1378 | -46.6261 | 2025-10-17 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 6fae6d52-8318-3bf7-b23a-b5d27d7a4dca | -9.898 | -47.6758 | 2025-10-17 00:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| ef419913-752c-33ec-8a92-501d935507ff | -10.2935 | -44.0455 | 2025-10-17 00:50:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 723b9a7b-4655-3b16-bddf-3fe84e71c968 | -3.236 | -45.9639 | 2025-10-17 00:50:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 267.1 |
| adab0ae8-923e-336d-a49f-7b55e6ce518e | -4.4059 | -43.4049 | 2025-10-17 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 447.7 |
| 83fe13b4-be71-3a3b-bc5f-107ad1a00e6f | -11.398 | -44.1933 | 2025-10-17 00:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| a2430e27-6684-344e-a13c-29114c9a19a4 | -11.5921 | -44.0472 | 2025-10-17 00:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 272.8 |
| 7a2cd647-f1c7-3fcb-9ff9-a24e96d55d44 | -16.0131 | -43.4753 | 2025-10-17 00:50:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 29905b5c-a92d-3b9f-a83e-4d44d5e9cff8 | -8.1996 | -43.3189 | 2025-10-17 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.7 |
| 16bbca23-c359-3d35-b5e5-a7683acf1bfe | -2.7401 | -49.3715 | 2025-10-17 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| e392f1b9-e1b8-3f44-ad42-a5b633ae1cfa | -3.2359 | -45.9862 | 2025-10-17 00:50:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 236.1 |
| 425df591-e370-3fa8-9ec6-bb9d6f07a629 | -10.1528 | -44.5289 | 2025-10-17 00:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 4619679f-c197-3e7d-80da-3d009fcf962e | -3.5028 | -52.4734 | 2025-10-17 00:50:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| ad47067f-466e-384d-8e4c-681f6142ddc2 | -16.033 | -43.471 | 2025-10-17 00:50:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 948a55b2-8dc7-319e-b1f7-54ce49bacf4c | -10.2745 | -44.0481 | 2025-10-17 00:50:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 22e35ad0-6571-3ec2-9159-f4138e49f98d | -9.1375 | -46.6485 | 2025-10-17 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| d79027af-e80c-38c8-9c20-4ed06f60caee | -3.2545 | -45.9855 | 2025-10-17 00:50:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 173.8 |
| 7f115733-78fa-32d5-a999-034bb019f594 | -10.9475 | -49.7605 | 2025-10-17 00:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 50.8 |
| c78af4ac-ef98-37e6-b442-ac4153efee04 | -10.534 | -49.5471 | 2025-10-17 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| befa2a7d-39db-3714-8b0d-30c76e8e91de | -10.2939 | -44.0221 | 2025-10-17 00:50:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 137.2 |
| bfce99d6-3a11-3503-abe3-aae0aa95adae | -9.7302 | -48.9183 | 2025-10-17 00:50:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| cc9166b6-4996-37b7-8144-96e5caafe167 | -6.759 | -42.3802 | 2025-10-17 00:50:00 | GOES-19 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 63.7 |
| c046a425-3155-3a31-b307-db75c402d6e5 | -11.4939 | -44.179 | 2025-10-17 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| f1956945-f7ed-3d9d-a67a-0c922a5a818a | -7.9442 | -44.115 | 2025-10-17 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 5ef78c19-f237-37a0-a867-7518e0dced7f | -16.0125 | -43.4996 | 2025-10-17 00:50:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 808d13a3-530a-3a4a-b901-aa216436b405 | -10.5132 | -43.4289 | 2025-10-17 00:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 9a7eca0b-cc71-375f-9f08-f6079fdb85a4 | -2.7401 | -49.3927 | 2025-10-17 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 36d530fe-b920-3c5c-9136-c20dc2dfc798 | -10.5136 | -43.4052 | 2025-10-17 00:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 67ad53cd-bba9-343d-8d64-085725e01cdc | -10.5834 | -47.42 | 2025-10-17 00:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 140.0 |
| f8015be5-a62a-31b3-8263-1ba84a40e436 | -6.7404 | -42.3582 | 2025-10-17 00:50:00 | GOES-19 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 64.5 |
| fd044f6f-1089-3a86-8dfc-f3203e976307 | -6.7401 | -42.382 | 2025-10-17 00:50:00 | GOES-19 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 69.5 |
| d0b4d235-2430-35e1-9986-67108b3b8335 | -3.5212 | -52.4932 | 2025-10-17 00:50:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 60ba25f5-90c5-3e10-ae8d-199ad93af237 | -18.0898 | -42.4475 | 2025-10-17 00:50:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.5 |
| 8d304b6b-43b5-3d6c-85bc-8e849e11b70c | -4.4248 | -43.3805 | 2025-10-17 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 8e82f89f-ce87-30f4-8426-5a0dfb193c89 | -9.1375 | -46.6485 | 2025-10-17 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 02509f69-e548-3624-9c50-c9a374a0e054 | -10.1528 | -44.5289 | 2025-10-17 01:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 0f9fcab8-b5cf-3a80-9f92-db29e6c809fa | -2.7441 | -48.3022 | 2025-10-17 01:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 6d12626f-d45a-37d1-8ab9-fdd08c4cf43a | -10.5136 | -43.4052 | 2025-10-17 01:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 61.8 |
| cfcaa6e0-8cf5-3768-96b8-813763171500 | -4.484 | -42.9335 | 2025-10-17 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| e730a11c-9358-3f5d-ae84-56b31fdb1a30 | -11.398 | -44.1933 | 2025-10-17 01:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| a2008ccf-d78f-3fe8-80d6-caca24a24c59 | -3.2546 | -45.9632 | 2025-10-17 01:00:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 193.8 |
| 75d8d4e8-8f17-3fa6-9114-71e58ec8e12c | -10.5128 | -43.4525 | 2025-10-17 01:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 82f9d52b-86da-392b-8fa9-4d8c134fcec3 | -3.236 | -45.9639 | 2025-10-17 01:00:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 369.7 |
| 41dda71f-02d6-35bd-acaa-0ad53b07f410 | -3.2545 | -45.9855 | 2025-10-17 01:00:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 176.2 |
| a217695a-bd43-3e0c-ab59-e7c5fa3178fc | -11.5724 | -44.0736 | 2025-10-17 01:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 0cd44e30-7c94-3ec0-8f05-acf64fcdd960 | -11.4939 | -44.179 | 2025-10-17 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 4d9c4dfc-c8da-3544-ac5c-091dce2892d0 | -3.5212 | -52.4932 | 2025-10-17 01:00:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| a67de9dd-4a8f-3ee4-a347-2902c1434ec4 | -16.0324 | -43.4953 | 2025-10-17 01:00:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 134.6 |
| c563a78a-12f7-35cf-a32e-7ee11eaae8c1 | -10.5834 | -47.42 | 2025-10-17 01:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 116.2 |
| d670e193-14f5-3520-a59a-f06ead6922a8 | -4.4061 | -43.3816 | 2025-10-17 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 160.5 |
| 53ebdf70-4ba1-3b1a-9af0-5a16d87f0c55 | -16.0125 | -43.4996 | 2025-10-17 01:00:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 106.5 |
| ca879973-d409-3bf4-a273-f840007d0172 | -10.5644 | -47.4223 | 2025-10-17 01:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 47c5b8ef-b239-3f0c-9a71-3a0a86b04ea3 | -7.9631 | -44.113 | 2025-10-17 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 171a770b-88a2-3948-a2f1-4d984bf84795 | -10.2745 | -44.0481 | 2025-10-17 01:00:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 63bace78-9a1c-3e05-9163-0f23a63a44f7 | -11.5921 | -44.0472 | 2025-10-17 01:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 277.7 |
| e255d00a-f493-353c-9188-f95d4b4ca9a6 | -9.879 | -47.6779 | 2025-10-17 01:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 08fac14f-876b-3ba4-853a-9ab80a6af69a | -11.6113 | -44.0443 | 2025-10-17 01:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 956e6401-eb11-39b6-b4ba-65016f4aa3a2 | -9.1378 | -46.6261 | 2025-10-17 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 5d111bba-41b2-3b95-968d-5404c608a52a | -3.5028 | -52.4938 | 2025-10-17 01:00:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 121.2 |
| a9e133dc-e7d8-39b3-b8e9-9b3442829781 | -2.7401 | -49.3927 | 2025-10-17 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 79ad8020-cd3b-3f0b-b4e0-a8a49778097c | -9.0821 | -48.0252 | 2025-10-17 01:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 4acaddbe-6c9e-330e-91a8-fa4e686abe2a | -2.7585 | -49.3922 | 2025-10-17 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| eb92501e-8dc0-3c13-9efd-7c7e667b6201 | -10.4937 | -43.4552 | 2025-10-17 01:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 29.3 |
| bf79501c-ac54-3e87-9fff-0a2db1686042 | -4.4246 | -43.4038 | 2025-10-17 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 228.0 |
| bf663714-a374-3fe5-86a8-93928f700aab | -16.0131 | -43.4753 | 2025-10-17 01:00:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 2b09ed67-d96f-3028-9175-11786ec7dff7 | -4.3872 | -43.406 | 2025-10-17 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 142.3 |
| cd0d12a8-a199-334d-a396-83f049571d5e | -4.3871 | -43.4292 | 2025-10-17 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 18636c9d-6123-367f-9518-3d1cbd390129 | -10.5132 | -43.4289 | 2025-10-17 01:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 185.0 |
| 25b6c7a7-e267-3be6-bbd7-927bac9d1e87 | -4.4058 | -43.4282 | 2025-10-17 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 7b88f58e-7bfd-3a16-b766-a939cd9af815 | -11.5917 | -44.0707 | 2025-10-17 01:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 403.5 |
| 34a32de4-748d-3bac-b631-3de344a57e4d | -10.4941 | -43.4315 | 2025-10-17 01:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 81ed32c7-58b4-3547-9eeb-cb7a8e788458 | -4.4059 | -43.4049 | 2025-10-17 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 406.8 |
| 6e98c45f-f2ad-35d5-af92-17b947bb33ac | -4.3874 | -43.3827 | 2025-10-17 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| f5afb624-af8b-3486-a9d2-613e218347bc | -3.5213 | -52.4728 | 2025-10-17 01:00:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| e98a9f49-53e9-3815-83fc-3dd876b91ccc | -10.2939 | -44.0221 | 2025-10-17 01:00:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 161.4 |
| f095a39c-14ca-33b1-a1e1-c3e422501e64 | -10.2748 | -44.0247 | 2025-10-17 01:00:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 158.4 |
| d953fcaa-0128-36f1-a2cf-2a107626075d | -10.4945 | -43.4079 | 2025-10-17 01:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 4adb6b5d-bf2f-33fd-a905-59e28147751d | -11.4748 | -44.1819 | 2025-10-17 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 117.5 |
| eb112097-7a7f-33c4-9537-4a96c83c2e1c | -11.5729 | -44.0501 | 2025-10-17 01:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 226a8671-419a-3f4a-b8dc-0fb5a7e57f70 | -3.2359 | -45.9862 | 2025-10-17 01:00:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 327.1 |
| 19cc2206-a1f2-3fc0-91cb-59c75dd93846 | -12.4451 | -51.3217 | 2025-10-17 01:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 5a17f4ef-b207-37ea-8415-50d98c6693fe | -16.033 | -43.471 | 2025-10-17 01:00:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 93.4 |
| fbbe669d-9c48-3134-b4aa-52a135ae0d1f | -11.6109 | -44.0678 | 2025-10-17 01:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 1e8c1f07-d733-331a-a66f-33af5e8ea80b | -3.5028 | -52.4734 | 2025-10-17 01:00:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 49ea138b-0d76-3030-833e-a5563cbd4706 | -10.4302 | -45.0232 | 2025-10-17 01:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 59.5 |
| d78ccdbb-01ae-35d9-bb43-52d11a656d3a | -10.2935 | -44.0455 | 2025-10-17 01:00:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 3b004922-4588-36b2-a0af-f77442ed47b1 | -11.5733 | -48.5568 | 2025-10-17 01:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| c49f4dcf-7549-3474-8f44-81ab5e9d5e5e | -8.7215 | -43.868 | 2025-10-17 01:00:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| f6c49f0f-0916-3cc3-abc9-e94d6581d3c1 | -4.9548 | -44.956 | 2025-10-17 01:00:00 | GOES-19 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 5c62dbfd-a3bd-362b-892f-5aae632f362f | -16.0324 | -43.4953 | 2025-10-17 01:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 119.1 |


[Clique aqui para ver as próximas entradas](README16.md)
