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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e05f0a4-27b9-3c1b-9c64-cffcbe0f70b9 | -18.60523 | -43.41577 | 2024-09-27 03:49:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 559cdbf7-a516-3479-a2e2-9ed6e5c09106 | -18.49844 | -43.88617 | 2024-09-27 03:49:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f5406d03-eaad-37bf-a42f-0ca43f9b59c5 | -18.35253 | -43.98167 | 2024-09-27 03:49:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f97c1d1-b3d8-3e7f-8bd6-f65acead3417 | -18.35159 | -43.98691 | 2024-09-27 03:49:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 421df152-b21e-3aa2-970d-ec816d25a67c | -18.2542 | -43.59893 | 2024-09-27 03:49:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 51c97111-1805-36b9-b478-ccc189b49548 | -18.25418 | -43.59604 | 2024-09-27 03:49:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eaec11c8-a23c-3a6c-bd18-300844296c06 | -18.05532 | -44.35014 | 2024-09-27 03:49:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa450af8-153c-39a0-a8ca-0c87582c6752 | -18.05441 | -44.35514 | 2024-09-27 03:49:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e48909b7-67a6-379a-8f4d-0883ddd8d12f | -18.0523 | -44.3443 | 2024-09-27 03:49:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2f9bf090-42e9-31ac-af7b-3a59c5a4feb5 | -18.04929 | -44.33837 | 2024-09-27 03:49:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b600f522-2bb6-31aa-90c2-27758fa4d039 | -18.04837 | -44.34337 | 2024-09-27 03:49:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9bb6ff79-b632-3b75-be1d-5fb5035bed4d | -18.0447 | -44.38562 | 2024-09-27 03:49:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cf1ea6e-65e2-3246-a71e-ce8a6dcdfcd8 | -18.04375 | -44.39079 | 2024-09-27 03:49:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63c3ed1e-4e68-39a3-955a-022c470cf16f | -18.04073 | -44.38485 | 2024-09-27 03:49:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b5215a6-0d86-34a0-b830-4c08c0e4fccc | -18.00807 | -44.33955 | 2024-09-27 03:49:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fe4d2da8-1026-37c9-8a3d-4e99f8a61fbe | -18.00608 | -44.33688 | 2024-09-27 03:49:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 44d2319b-5468-3197-8b0c-b37612f62054 | -18.00508 | -44.3424 | 2024-09-27 03:49:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 73294225-2d2e-3114-9cb7-34df2d10476c | -18.00413 | -44.3387 | 2024-09-27 03:49:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1f6e4660-a22e-30a5-9fb4-6b197fbbb0f4 | -18.00411 | -44.34784 | 2024-09-27 03:49:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d3265521-8c8e-39bb-8aa9-de769a34cf4a | -18.0031 | -44.3442 | 2024-09-27 03:49:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 22c04fe8-927b-3979-a8d7-4c83d095be57 | -18.00099 | -44.46588 | 2024-09-27 03:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0727a0ce-b20d-3565-b079-0249ef57f5a6 | -18.00032 | -44.46949 | 2024-09-27 03:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dfb0a088-f208-35c3-954c-44545b03fde3 | -17.98223 | -44.4693 | 2024-09-27 03:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4e06256f-c6cf-303d-85cd-e5e56f3246a7 | -20.22655 | -43.69553 | 2024-09-27 03:49:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d0306c53-6ff0-31ed-ab13-212873208bf9 | -20.2229 | -43.69457 | 2024-09-27 03:49:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 873917b2-bb4d-3c4d-863d-94474cad8a55 | -20.18673 | -43.5429 | 2024-09-27 03:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d48f8b02-94af-35ad-a720-20daf295a49e | -20.18594 | -43.54737 | 2024-09-27 03:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a597f77b-cdef-36bd-ac94-2de5d57e819f | -20.18519 | -43.53033 | 2024-09-27 03:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 5fb635e7-82bf-3196-90e3-8988cf45ba2f | -20.18451 | -43.53412 | 2024-09-27 03:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1f696c80-c8d4-35f8-ae4c-61bfae1414fc | -20.18382 | -43.53798 | 2024-09-27 03:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 09c674bb-4611-3fe5-b65c-24dcafa29a72 | -20.18308 | -43.5421 | 2024-09-27 03:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 949224cf-3126-32d0-af74-dbf63f99e0bb | -20.18151 | -43.52968 | 2024-09-27 03:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1d252d48-ec9d-3c37-b6d1-e7c25b6da0d4 | -20.17208 | -43.51884 | 2024-09-27 03:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.8 |
| 148fdd1e-1e1b-340a-b4df-a34b3ffe343e | -20.17135 | -43.52294 | 2024-09-27 03:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 1a00852b-1762-39ec-9724-f68e6ec574fc | -20.17063 | -43.52694 | 2024-09-27 03:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| fd3ba13d-73d0-398d-9484-29b3c491ed31 | -20.16992 | -43.53092 | 2024-09-27 03:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 53.5 |
| 783ad04b-e343-379a-a4da-43c79c0b8e5d | -20.16844 | -43.51797 | 2024-09-27 03:49:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| 0b294d39-785d-3e8c-bca8-d08ec3351393 | -20.1677 | -43.52215 | 2024-09-27 03:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| af0b576a-15b5-3428-bb46-946d5e8d024f | -20.16696 | -43.52626 | 2024-09-27 03:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| e9f7e139-4980-3a70-93cc-c57ef5aadda2 | -20.16622 | -43.53039 | 2024-09-27 03:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| e5dcf38f-272b-31a9-982b-4f3f188bf3a8 | -20.16482 | -43.51707 | 2024-09-27 03:49:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| afd90ecc-b96a-386f-8520-366400261876 | -20.1618 | -44.33343 | 2024-09-27 03:49:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| bc1d136e-7113-3cde-b78d-524f029e4617 | -20.15801 | -44.33247 | 2024-09-27 03:49:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| fbb48752-0934-3e33-814e-6811a46cb25c | -20.15711 | -44.33744 | 2024-09-27 03:49:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 6ef7e988-e7dc-35e0-9ab3-0bfaa632f3cd | -20.15682 | -43.56179 | 2024-09-27 03:49:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e394ad22-3fd1-3e67-9fcb-5a8dab1d65c3 | -20.15422 | -44.33153 | 2024-09-27 03:49:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 69717714-51d8-3422-a6e9-e97c1b7bdfb3 | -20.15405 | -43.55609 | 2024-09-27 03:49:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ab110ddf-2705-37d6-b85b-28dfd2a88024 | -20.15384 | -43.51489 | 2024-09-27 03:49:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| bb0c9a5b-1a10-3ca2-a90a-0eaf2db850b1 | -20.15332 | -44.33647 | 2024-09-27 03:49:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a10a6c8a-d85a-3368-aa95-befd553cc3cc | -20.15305 | -43.51928 | 2024-09-27 03:49:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7ea89260-fdea-3c78-80e8-3f8582317e59 | -20.15239 | -44.34158 | 2024-09-27 03:49:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 6a93c193-f2b9-39e5-bcc5-2464653bda72 | -20.15041 | -44.33068 | 2024-09-27 03:49:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| f8ec3a16-afc1-3573-88e6-27266cec2ea0 | -20.1502 | -43.51408 | 2024-09-27 03:49:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 37b7d949-a7d8-364a-b6cb-fbbec053e1c1 | -20.14952 | -44.33559 | 2024-09-27 03:49:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| dec392c6-a709-353f-a9b5-e874263b2bdc | -20.14943 | -43.51837 | 2024-09-27 03:49:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5a3053f2-d7fd-3b1f-a787-7932eee55a70 | -20.1486 | -44.34063 | 2024-09-27 03:49:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 625e6f29-2c94-3547-9f3a-a208be27b5c8 | -20.1466 | -44.32984 | 2024-09-27 03:49:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ed2de31d-7c4d-3918-9153-679a7438c8ab | -20.12254 | -44.26669 | 2024-09-27 03:49:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4c177110-19bf-384c-9f9b-9fbb0a0b8b25 | -20.11516 | -44.50201 | 2024-09-27 03:49:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d8b7e856-fd20-3bbb-bfe3-eabda43d21e8 | -20.11039 | -44.50621 | 2024-09-27 03:49:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 30a44db9-5123-33d9-b9a0-43441a07af29 | -20.10788 | -44.23909 | 2024-09-27 03:49:00 | NOAA-20 | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0e3dd974-df06-3c8b-9256-5cd3ba9ba3dc | -20.10312 | -44.2435 | 2024-09-27 03:49:00 | NOAA-20 | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1598ded1-74ac-39ee-bddd-1b1debc4b28c | -20.1022 | -44.24844 | 2024-09-27 03:49:00 | NOAA-20 | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3abf7afd-7350-3ddb-b502-85e6cf09d1d2 | -20.10024 | -44.24614 | 2024-09-27 03:49:00 | NOAA-20 | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3be9e626-6f20-37ca-ab33-2d6b52956665 | -20.09584 | -43.83698 | 2024-09-27 03:49:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a02be600-324c-38e6-b6d6-2e8e7da48f73 | -20.0921 | -43.8363 | 2024-09-27 03:49:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e2153f25-3c1d-3a28-96f6-97a88bbf7d02 | -19.94735 | -43.79316 | 2024-09-27 03:49:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 2ce89ef0-0161-369f-b2a9-f7460a634396 | -19.9465 | -43.79795 | 2024-09-27 03:49:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| bb0ccf3a-0ac4-30d6-94ca-675b5cba7808 | -19.94563 | -43.80289 | 2024-09-27 03:49:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 89233b94-be15-3941-b7b2-cbed5872d872 | -19.94192 | -43.80206 | 2024-09-27 03:49:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| fafca877-4388-35e6-bbde-6afff82a2609 | -19.93959 | -43.77171 | 2024-09-27 03:49:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2edd989a-a59f-3986-a98e-7258c25e0df8 | -19.93623 | -43.79063 | 2024-09-27 03:49:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d1cbcaec-cded-3135-8d6b-f8f40271e6c7 | -19.93509 | -43.77537 | 2024-09-27 03:49:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3d1573af-4b8f-3617-a41c-2245d4a7c58f | -19.92616 | -43.80384 | 2024-09-27 03:49:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 34327efd-de42-3c8a-9cda-bd3001707b43 | -19.8754 | -43.82821 | 2024-09-27 03:49:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ad7598b3-6c70-3535-b2c4-34732f1a902c | -19.87168 | -43.82737 | 2024-09-27 03:49:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 12b62af1-a93c-3fea-9c32-bc50c13206e7 | -19.81726 | -44.06134 | 2024-09-27 03:49:00 | NOAA-20 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 914bb8be-7553-39d5-874f-03767cdfe627 | -19.81437 | -44.05575 | 2024-09-27 03:49:00 | NOAA-20 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 401a3937-bf1e-3f52-b64a-87c4c9a28f5a | -19.81058 | -44.05502 | 2024-09-27 03:49:00 | NOAA-20 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aac5f5ec-f7f2-377b-9cd9-46a35d62a1da | -19.79468 | -44.20549 | 2024-09-27 03:49:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6efd36da-18ac-3171-90de-61351a29be6c | -19.79375 | -44.21056 | 2024-09-27 03:49:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b4fdbe8-167a-3769-9076-67a7801cd98b | -19.75866 | -43.67882 | 2024-09-27 03:49:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 627d2443-544c-3697-8822-f27a739c34ed | -19.75694 | -43.68111 | 2024-09-27 03:49:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9de01c81-fe67-3920-886e-18bef846a226 | -19.75625 | -44.43489 | 2024-09-27 03:49:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe35e038-dcd7-3f8c-a876-f925ebc00474 | -19.75406 | -43.68293 | 2024-09-27 03:49:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 540c3dda-c4b0-3b17-8e29-f046edbea971 | -19.75321 | -43.68044 | 2024-09-27 03:49:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5acb40fe-08bf-32fe-9806-99bce06b03b3 | -19.73156 | -43.56498 | 2024-09-27 03:49:00 | NOAA-20 | NOVA UNIÃO | MINAS GERAIS | Brasil | 3136603 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1058703-2622-35e4-9696-def27d37aa3e | -19.64519 | -44.15449 | 2024-09-27 03:49:00 | NOAA-20 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db437df4-9d00-3059-abcf-c3eb135b3984 | -19.64363 | -44.18504 | 2024-09-27 03:49:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d96fc09d-f736-3c41-ab68-8614eaa548a4 | -19.64274 | -44.18996 | 2024-09-27 03:49:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5e452f7d-2887-36e4-8388-44f9461e7377 | -19.64138 | -44.15371 | 2024-09-27 03:49:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e407bdf-40b0-3e0b-86cf-2d7d085dc732 | -19.63511 | -44.18837 | 2024-09-27 03:49:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5aa40906-f26e-360e-b5c7-603559a18e26 | -19.62742 | -44.18706 | 2024-09-27 03:49:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3d5f6f2c-b891-3470-ae4e-170650f5d20c | -19.62358 | -44.18641 | 2024-09-27 03:49:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| de20a490-0b5b-3033-857c-6e5ed776afd0 | -19.62066 | -44.18067 | 2024-09-27 03:49:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42019cb9-f15a-3435-ae82-1404838119fb | -19.56962 | -43.77359 | 2024-09-27 03:49:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70e60dad-5883-34ed-a139-763dd3996948 | -19.51925 | -44.11649 | 2024-09-27 03:49:00 | NOAA-20 | PRUDENTE DE MORAIS | MINAS GERAIS | Brasil | 3153608 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fdfa8b7a-2e29-363d-9e8b-d702d2ea7535 | -19.51833 | -44.12149 | 2024-09-27 03:49:00 | NOAA-20 | PRUDENTE DE MORAIS | MINAS GERAIS | Brasil | 3153608 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14c8ca99-2c94-392f-98d2-1238611863b9 | -20.11421 | -44.5072 | 2024-09-27 03:49:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4a7abd6d-d191-312e-8535-8da01c383f03 | -20.10747 | -44.50031 | 2024-09-27 03:49:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README64.md)
