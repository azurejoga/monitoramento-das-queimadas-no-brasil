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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69266cd1-7afb-33c9-820f-bf99ccb26a15 | -13.19491 | -46.34238 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b6902dd6-4980-3e3a-ad42-e26877419354 | -13.19431 | -46.34653 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 903639f8-5c62-349b-ae2b-0f4e7ec0c6ad | -13.19371 | -46.35067 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 82127415-d8a2-32b1-b2ae-b9d2572808c5 | -13.19313 | -46.32951 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 0603d5ef-bd36-3b48-b018-07d4ff45d596 | -13.19311 | -46.3548 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1e4366b5-2404-3774-9bcd-66e484898448 | -13.19253 | -46.33364 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 96d6e611-5457-3af2-9976-c903d68d1566 | -13.19252 | -46.35891 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bee188a1-3cd0-37e2-a333-6b407e733d97 | -13.19194 | -46.33776 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ea1a8a7c-889f-3dc4-9856-e92c1b2729ef | -13.19015 | -46.35014 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d320e3ef-9589-3f39-80ce-93f592a32d80 | -13.18955 | -46.35425 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1eaf7c57-606b-39cf-8bdd-b6b6b0678c06 | -13.18896 | -46.35836 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 240fdd37-1d03-3564-8d55-e2dc73a75037 | -13.18896 | -46.33318 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 777041d1-5085-34be-94b5-bdc8161f0c3e | -13.18888 | -46.30846 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4621bace-61a7-3b42-ab26-f310da890443 | -13.18777 | -46.34141 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| bf940fa6-d4f4-3c6a-b237-d6570babebe0 | -13.18717 | -46.34552 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1d6476ac-e433-3033-b20f-43c07ed487d2 | -13.18658 | -46.34961 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2732bf31-bdb1-3a32-8e0b-ba06028aeb48 | -13.18599 | -46.35371 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 36.1 |
| f15383df-2803-393f-937d-6c1f49fc5c3e | -13.18539 | -46.35783 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 95b179ea-5f64-3679-8303-73090f99318a | -13.18529 | -46.30806 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 54eac2a6-27ac-3a46-9a96-6e39350b5bc7 | -13.1848 | -46.36195 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| cefddee1-ed71-3ccb-8215-ab0daa39d984 | -13.18471 | -46.31208 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 53437992-664f-36f7-85ae-2eb6448a76a9 | -13.1842 | -46.34089 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 72605205-e085-34ac-9351-9c370a6399af | -13.18412 | -46.31618 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5c77dc91-e592-38aa-b637-689e17fbe0c3 | -13.18361 | -46.34498 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 79b508a5-0044-3e99-b319-c92cdaaa19d2 | -13.18302 | -46.34907 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4ce9e06f-9fb0-346f-8eaf-4d013b4fd9c4 | -13.18242 | -46.35318 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 2be23ae0-01e7-395c-bbad-72ceb1dd868e | -13.18183 | -46.3573 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 44c2d9eb-134b-3976-b5cf-a5a02ed95a12 | -13.18123 | -46.36143 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 4b073b8b-fc36-3e04-b337-5a3cc7dcf712 | -13.18064 | -46.36554 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 3dadc94a-f80e-37a9-a4fa-ca7391d9e64b | -13.18004 | -46.34444 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22f4c7c8-0bfc-37bd-9364-6ad4a36ca9bf | -13.17886 | -46.35265 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fb6c2d6c-2eac-353d-8171-1077e65d921b | -14.59627 | -45.7481 | 2024-09-30 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 61d5146e-8682-3bd6-84bb-28be1ddcd1b1 | -14.54513 | -45.39816 | 2024-09-30 04:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d6b38bb-e685-36fe-bc6e-c6783193baf6 | -14.18295 | -46.44941 | 2024-09-30 04:32:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 68a8290f-96d9-3b7e-abc4-88f2e9c94d90 | -14.18235 | -46.45352 | 2024-09-30 04:32:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96a76f51-262e-3b78-9efe-29d6d38aeeef | -14.18176 | -46.45761 | 2024-09-30 04:32:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ea7b881a-c072-303b-89a2-a767ffab366e | -14.17937 | -46.44885 | 2024-09-30 04:32:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5ceabf5d-f8aa-3c1e-b8b7-77f1211ede49 | -14.17877 | -46.45298 | 2024-09-30 04:32:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5de482e3-305b-3aae-adcb-75f67e4750c1 | -14.17817 | -46.4571 | 2024-09-30 04:32:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ea6301f0-1436-3da0-8166-e4d9cf7f79de | -14.17458 | -46.45664 | 2024-09-30 04:32:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c40dea2c-8bd8-3c0b-b23b-0cb9ebea5964 | -14.17398 | -46.46075 | 2024-09-30 04:32:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0e337b65-450d-3f4e-a7f8-e6446d474e38 | -14.17098 | -46.45617 | 2024-09-30 04:32:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 09614f80-1d83-38e5-92e0-672e6dc99cc0 | -14.17039 | -46.46028 | 2024-09-30 04:32:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ff439045-fe5e-3929-b949-23003a1b8ddf | -14.16978 | -46.46448 | 2024-09-30 04:32:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ee83ca00-45fa-36b2-a121-814a8fa6b595 | -14.1674 | -46.45564 | 2024-09-30 04:32:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c4f6ca1-6088-388e-926a-0e45943c0cde | -14.1668 | -46.45979 | 2024-09-30 04:32:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91ecfd52-4a4b-3e52-b94f-c2203b53fdfb | -14.07033 | -46.32655 | 2024-09-30 04:32:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 562e8102-4bd6-394f-84e7-12880c5651a9 | -15.20649 | -46.23155 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf6725a9-0fe8-3402-a841-66e5b250942c | -15.19915 | -46.23051 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 202bb4c8-a949-3a08-b251-5b746e1856c8 | -7.80948 | -45.49193 | 2024-09-30 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0eabc815-1644-3845-8f16-fc780746a5c1 | -7.84652 | -46.14608 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ccc39251-8786-391a-be3d-8369b69d2c6f | -7.73875 | -46.16437 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5dba4eda-09cb-3878-9584-128f52fc3d37 | -7.66268 | -46.61264 | 2024-09-30 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83d6ec64-2262-37f0-82b6-3e20a2e40852 | -9.26147 | -45.73931 | 2024-09-30 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8b87eb8-1849-371a-928d-9a7f67964d5a | -9.23212 | -45.7395 | 2024-09-30 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c75af128-1b22-34f2-8d49-a53c29dad953 | -9.2292 | -45.73843 | 2024-09-30 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7d16a4c-4bda-33ad-90b6-d4675480f70d | -9.22859 | -45.73899 | 2024-09-30 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fcf914a2-e451-3df1-9efb-be89736af8f3 | -9.21278 | -45.72454 | 2024-09-30 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 044e503d-6c50-3d8e-b6fd-af23ebd09386 | -8.93235 | -45.66854 | 2024-09-30 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a9fc21e-5bcb-316e-9fb8-220a18df3ceb | -8.92942 | -45.66403 | 2024-09-30 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01f07aac-9710-35f5-8949-c8fc086d3a13 | -8.92883 | -45.668 | 2024-09-30 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52bc5301-8c4c-399f-a0b1-ab68d0b424d5 | -8.91381 | -45.64627 | 2024-09-30 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c7440ef-de2e-3f2a-87c8-6c32d57c19ee | -8.91029 | -45.64572 | 2024-09-30 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9aadb9e8-b2e2-3805-a17b-0809f2a16cd8 | -8.89681 | -45.63953 | 2024-09-30 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c722f17-71e5-314a-bb30-557717a05667 | -8.07169 | -45.47778 | 2024-09-30 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81292f10-ef71-3f6c-b928-f60bc3606ab1 | -8.06817 | -45.47722 | 2024-09-30 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0fa78474-4810-3cae-9f3d-0c54acfdac73 | -9.22919 | -46.79113 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 10453c3f-2819-3114-8a68-5f12f24a9d56 | -9.11046 | -46.65327 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e06448b7-4902-3650-bb94-7014d09189c9 | -8.81671 | -46.78477 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6ee47a67-2838-3811-8669-da914ce972a1 | -8.81331 | -46.76187 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8068cba-759e-3786-842b-ad75ab89dd02 | -8.783 | -46.80188 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ed039772-5389-3e3e-88f9-e852f9fcdc1b | -8.77796 | -46.81226 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c02e622f-22c9-3765-846b-4d661b1d378e | -8.6246 | -46.55361 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9d894c9f-3f42-3931-8da8-5b64a0b4f677 | -8.6212 | -46.5531 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2567ac42-e79c-3e15-981f-a5824f887832 | -8.46902 | -46.86099 | 2024-09-30 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0569a1a7-3736-3c62-9947-e791f9ce82fc | -8.46566 | -46.86045 | 2024-09-30 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18a34ee7-b3e9-326e-b16d-5f90f3a1ce63 | -8.42971 | -46.36245 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c263d0ee-9a81-38d8-8ca9-2f3c7dcc2b39 | -8.42915 | -46.36616 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4cec662-9c4e-3cf7-ab2d-69806f7a5c24 | -8.42913 | -46.3433 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8efc457c-fe04-3d4e-bab2-de32ee6749cc | -8.42858 | -46.36986 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2a20abb-e6d4-393f-8616-c24ea6d0beca | -8.42229 | -46.34235 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c6b628d7-bb6d-3744-bfa3-860f5d145edc | -8.42173 | -46.3461 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1af82bc3-66cc-3c68-9c4c-1d1c72e403a7 | -8.41831 | -46.34558 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf0ec2c7-cd05-3937-87da-b710c6c43779 | -8.41324 | -46.37902 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e593e313-0890-30a7-8ead-d1b508b149e0 | -8.4121 | -46.38649 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab2985fb-a20b-3764-bbc4-557968390dcc | -8.41036 | -46.35197 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07f42f4f-18f9-3d9b-b7ed-c2d0a815930d | -8.40468 | -46.34335 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff625581-1716-30df-b9ae-ef1aff60b7d9 | -8.40412 | -46.34706 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b336f0f-5003-37fe-bf8b-0a30d78b5cc5 | -8.81669 | -46.76237 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9842e771-852d-3c65-9749-b743eafd2124 | -8.77907 | -46.80498 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 36772a80-d561-315b-96a3-e681f1bc1d2d | -8.77851 | -46.80862 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30414ae6-fe43-3858-b1cb-6423167b7d77 | -8.61724 | -46.55629 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5124979-9af9-3af9-950d-d8a7a931912d | -8.61328 | -46.55947 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8682161-b4d4-3b1e-828a-b99a8c666318 | -8.47239 | -46.8615 | 2024-09-30 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 58b70a20-e5de-35bc-b60f-04696cc52d1c | -8.46153 | -46.45063 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5d1deee-cd50-3354-a992-59f17b0f4bed | -8.42571 | -46.34283 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b943d406-89f3-3ce2-8c18-2d041dee9284 | -8.42515 | -46.34656 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3f21e24-d452-32d0-b66f-bbe322ac1f22 | -8.41888 | -46.34184 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b171936-d314-3926-a061-a236970654cc | -8.4149 | -46.34504 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 941dbe15-10dc-3749-85df-c658ea3b603c | -8.4138 | -46.37531 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README37.md)
