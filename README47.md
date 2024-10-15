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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03a32ebe-b788-303b-a848-6d9a5ef42ec4 | -7.08037 | -42.66666 | 2024-10-15 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| bfc553e9-27ad-317b-be97-445d20f3202a | -7.07998 | -43.0205 | 2024-10-15 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 00f17e2f-d8ce-3994-8146-b9b706c6edd9 | -7.0775 | -42.63464 | 2024-10-15 04:25:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 18051546-30e5-32f0-85aa-00ac751a7896 | -7.07698 | -43.01566 | 2024-10-15 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| af430060-acae-39f3-8c38-fb96d4c8f01c | -7.07665 | -42.66611 | 2024-10-15 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 9dbdc8e1-6e54-33da-924b-571888373d13 | -7.076 | -42.67049 | 2024-10-15 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| a4595a01-f326-330b-88fc-6fe282b708fc | -7.07378 | -42.63403 | 2024-10-15 04:25:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 58172344-438a-34f1-8fdb-e7d6bb3659a6 | -7.07376 | -43.03688 | 2024-10-15 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c006ccb9-eb07-3088-a08c-9e079bd1732a | -7.07312 | -43.04109 | 2024-10-15 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b68db43a-d5af-333f-802b-51352d0d4f39 | -7.07228 | -42.66996 | 2024-10-15 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 2d6c4174-291d-320d-b6b3-3acde251495a | -7.06613 | -42.66011 | 2024-10-15 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 0e1b6519-a553-303a-bdc7-6b71c75fc496 | -7.06242 | -42.65955 | 2024-10-15 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c5ca1316-a264-383a-9945-2413ffda36f2 | -6.59251 | -42.2415 | 2024-10-15 04:25:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e60ccb0c-2b58-3ae1-abb9-519e49dc2623 | -6.69242 | -43.04808 | 2024-10-15 04:25:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e7e67ed-2782-357f-94f3-ddb8727012a6 | -6.6918 | -43.05226 | 2024-10-15 04:25:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c2a57fa-3e33-32a6-ace9-82a39d1d8fa3 | -6.46919 | -43.31644 | 2024-10-15 04:25:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| af3f6c8c-3700-3fd1-9c24-56b886c304a8 | -6.46795 | -43.32463 | 2024-10-15 04:25:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f17bf401-0a5b-32a5-a750-4162548d5190 | -6.46501 | -43.31991 | 2024-10-15 04:25:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f87ce3f-5407-32ae-b7a0-63012451951d | -6.4519 | -43.33418 | 2024-10-15 04:25:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f92f97e0-e7b2-3813-a49e-7517147ce923 | -6.44894 | -43.32964 | 2024-10-15 04:25:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d63dabf6-bc91-3e0e-b020-500915fc72b2 | -6.44834 | -43.33363 | 2024-10-15 04:25:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9681c730-2912-3a7e-876f-c15cf2bd4d30 | -8.3391 | -42.74842 | 2024-10-15 04:25:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 43d76af1-fe90-3364-b01e-de9dc261b312 | -8.33844 | -42.75294 | 2024-10-15 04:25:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 204488b3-4700-3195-9334-03b7c0695c4d | -8.33779 | -42.75747 | 2024-10-15 04:25:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 90573eb5-e815-3602-b6ed-51ff29dda030 | -8.32702 | -42.77884 | 2024-10-15 04:25:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 42bc50fc-8aba-3dc5-b3e3-4bcf02a620a2 | -8.32617 | -42.78021 | 2024-10-15 04:25:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 8146c0a9-4f38-33f8-ae68-ab0e7746c2de | -8.32327 | -42.77826 | 2024-10-15 04:25:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d0226f26-d742-36d0-982e-6b75f7e922cb | -8.32262 | -42.78275 | 2024-10-15 04:25:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ac0098e2-ec6f-3b62-b0da-babf81027114 | -8.32242 | -42.77963 | 2024-10-15 04:25:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ca2d56b9-764c-34d5-9d6b-0c59d78ac389 | -8.32174 | -42.78411 | 2024-10-15 04:25:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6f40a9c4-2560-371c-a974-f9abf143ae2d | -8.11126 | -43.90829 | 2024-10-15 04:25:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| fb6b6179-6110-3ed0-9d1e-7abe287973b3 | -8.07373 | -43.82056 | 2024-10-15 04:25:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9b8200b1-2a35-3e70-a6a8-73a217a66693 | -8.07314 | -43.82458 | 2024-10-15 04:25:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9d3eb3df-c754-3e57-9302-2b58340af2b2 | -8.06959 | -43.82406 | 2024-10-15 04:25:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 777351d3-c0dc-39fe-8dbd-1056ef9092b1 | -9.8313 | -43.78177 | 2024-10-15 04:25:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a1d2a926-1343-3235-9e36-48c8f40ea0ce | -9.72363 | -43.85716 | 2024-10-15 04:25:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 94362762-4ea0-3e6c-b8c0-d0eaf4587919 | -9.72002 | -43.85664 | 2024-10-15 04:25:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d6b44adb-554b-3bb0-a52a-a15b69f82106 | -9.37353 | -43.71025 | 2024-10-15 04:25:00 | NPP-375D | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7bc88ac5-d87c-37ff-b2e5-f2f481bcd9d2 | -9.3728 | -43.71183 | 2024-10-15 04:25:00 | NPP-375D | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6fe74d33-0e2d-310c-81d3-d474f3966930 | -9.45545 | -44.18508 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3c03b547-35e3-3c7c-a832-4495d28d4c06 | -9.45485 | -44.18904 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 99fd3af2-7085-340d-a85d-d643b6aa4ba6 | -9.45434 | -44.1439 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e8264ead-9753-3050-a4ff-fb3b1ddf6b16 | -9.45315 | -44.15191 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 223ad613-0e1d-3217-8c44-f87c8c52a3b1 | -9.4525 | -44.18057 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3053b435-325d-3427-8ab4-f04fdf90c8b7 | -9.45191 | -44.18453 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 262c03c6-608c-399b-8857-c420dd88cdf6 | -9.44961 | -44.15135 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8f4e8ed-a27f-3923-b747-7eafb7f09ae6 | -9.44897 | -44.17998 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| b4e12cdd-c4d2-3fa9-a9e0-40ce3f3fe2ca | -9.44838 | -44.18395 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f40bbaaf-21dc-3008-8151-94818a0a6c8f | -9.4449 | -44.13426 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 713e449f-9819-34c7-adb9-a744e8b4efe6 | -9.4425 | -44.17484 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87bbd383-e7ba-3326-b298-f79bfb8504fe | -9.44191 | -44.17883 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8b45e54-9c28-350f-a974-68b3072e4ef1 | -9.439 | -44.12519 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a6074d9-7218-3b28-9c6e-6c8575d519e5 | -9.4384 | -44.12922 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ffba7a90-c142-317a-b844-224b2857743d | -9.43602 | -44.16975 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a9df8d2-7064-363f-ba16-49a9da324169 | -9.43543 | -44.17375 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1071686-5aad-3cbd-84ef-9b32e3d1cf4d | -9.43308 | -44.16519 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6eb63f23-da6f-33a8-a625-82081f148878 | -9.43248 | -44.16923 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c37f3290-5078-36f5-a9c2-232173f06125 | -9.43189 | -44.17321 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d6edea4-ff47-3a57-a796-f921b07109f8 | -9.43013 | -44.16063 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff893c85-3488-39f2-82ca-bfb9e4dcd394 | -9.42777 | -44.17663 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 698f6a5d-3b00-347b-aae5-5b63252b9533 | -9.42186 | -44.1431 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9bf4d40-69ef-3e21-9412-0bee64b545c3 | -9.42127 | -44.14712 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad5ca5f8-c95f-322f-8fe4-a31d8badbd21 | -9.41892 | -44.16307 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 941b4c5a-7d82-3041-9058-ab4ff76ee076 | -9.41804 | -44.14772 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5a842f7-7ef6-3154-8d27-4ec93b1426cf | -9.41773 | -44.14659 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a9580d0-b1aa-31a9-8965-f0e83a52da97 | -9.41745 | -44.15163 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 700a6b30-8052-32a3-bc3a-d85201da06f1 | -9.41086 | -44.17113 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8895897-3f32-34e0-9316-cd7de5fadf12 | -9.41066 | -44.17001 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df2fa55f-e04f-37cc-a715-51a34add37cb | -10.2604 | -43.97308 | 2024-10-15 04:25:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7f21b1e3-abe4-39c5-834a-0329faa3a83b | -10.0922 | -44.2335 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 788175c8-d8b7-3a4e-a019-c9cdc3f5ee6e | -10.08984 | -44.22491 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed3574d6-6ccd-3b24-8a1e-2dd302172aec | -10.08924 | -44.22894 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 987c998a-ce85-33da-a6ac-beecb9175b47 | -10.08866 | -44.20829 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 23dc94b8-d807-3d44-9671-f0d9faa54c54 | -10.08865 | -44.23295 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89116962-a3ce-3b9b-a2e3-c486621da43d | -10.08807 | -44.21231 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ac4c789f-8ea7-350a-adff-a20784d9db03 | -10.08688 | -44.22035 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f9c5307-134c-3a13-991b-e4ab36c5c162 | -10.08628 | -44.22437 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f47dc84a-7b4b-3309-9a7e-921f35e17e57 | -10.0857 | -44.20372 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae2a4a26-28f2-38a8-a63a-63d06a568344 | -10.08569 | -44.2284 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f8d331a-0e2c-3536-9e36-0b3f693df09d | -10.08511 | -44.20775 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14c4e28a-75d8-31ee-93b2-2e3367c55201 | -10.08509 | -44.23241 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2eabc5f3-fe47-37ca-abd4-202cc79486bc | -10.08392 | -44.21579 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50987210-458b-3140-8a72-15a42a949969 | -10.08332 | -44.21981 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7bb6b77-8f00-332d-952a-1f7a8d799fdd | -10.08275 | -44.19911 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 404b9462-7a55-397d-af36-1bdfc4404a65 | -10.08273 | -44.22383 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e4aa181-aed0-30cc-8521-169f79b5ff90 | -10.08215 | -44.20317 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8cd87199-20c7-3591-927c-2d164afe9d69 | -10.08214 | -44.22786 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fbe379cd-2682-3f31-a725-e2662880cc18 | -10.08154 | -44.23188 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e6e0ff7-7c2b-3a91-a443-db294692c22f | -10.07979 | -44.19451 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d9ecf457-2ab4-3d2a-ac07-d2199b2de97b | -10.0614 | -44.24541 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b19d59c-ec22-35d7-a465-66166d136289 | -10.05903 | -44.21205 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 33ff61d4-be70-3cb1-8a1e-cda6029b5763 | -10.0588 | -44.17123 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0acda50-c094-3f4b-b31d-fe580cd6b276 | -10.05819 | -44.17527 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c60bd893-6c63-392c-9806-2a4bf01a9885 | -10.05725 | -44.17447 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 693bd9cc-e30a-3204-bda6-5aed6a421e8f | -10.05608 | -44.25694 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 51c4d362-585b-3a14-96dc-542a6832ed1e | -10.05549 | -44.26094 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1da07384-33b1-3709-b154-da3b2744f1fb | -10.05463 | -44.1747 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42d60dd3-d9eb-3837-8c12-bcc3a6b208cd | -10.04568 | -44.18578 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| abd9f1f9-715e-32df-a436-8c362bdf9ba0 | -10.04506 | -44.18985 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6d8a8eb3-2055-36ff-bb31-aca6a7f9dfec | -10.04445 | -44.19389 | 2024-10-15 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README48.md)
