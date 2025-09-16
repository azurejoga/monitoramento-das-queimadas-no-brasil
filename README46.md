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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd57d777-6dac-318b-87b2-dc635be561b2 | -7.39122 | -50.00669 | 2025-09-16 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aab51302-8921-3967-b615-d53b265d0177 | -8.7029 | -49.41416 | 2025-09-16 04:29:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6602b069-ab2e-3c6a-aa9c-576e47b70fa7 | -12.73596 | -47.20054 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70d084df-05d3-3a27-82d3-7bebaf47df6a | -7.19653 | -48.60297 | 2025-09-16 04:29:00 | NPP-375D | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0d1cf83e-268c-3eb8-8c8b-17405312c0e8 | -10.36662 | -61.2587 | 2025-09-16 04:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 32cd1024-3c2a-38d0-84e4-80a89d4bd213 | -11.11909 | -45.32441 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 06f0fcde-67d1-38c4-9c37-364cb6e48677 | -8.39313 | -47.2678 | 2025-09-16 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8c301ca-9661-3963-93d6-a01e4a07a44b | -11.70375 | -46.8831 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8d1010a1-033a-3fa3-97ed-e338c50d8a27 | -11.44485 | -46.94352 | 2025-09-16 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c05a598f-c9da-3c59-adbe-6b9cdf10cfa6 | -8.84235 | -47.94667 | 2025-09-16 04:29:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 547a80ee-b23c-3d0a-b404-165bfa0ca2b4 | -12.11539 | -44.83942 | 2025-09-16 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 190c3549-8cc5-3c59-a37b-fd7d06183eae | -12.66589 | -47.71279 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 54a2be04-b746-33ea-86e1-7a8333241526 | -10.36386 | -61.25826 | 2025-09-16 04:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e0c2b88c-7ebf-398a-b139-f2161d4cadf0 | -10.07279 | -48.17517 | 2025-09-16 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fcda679c-1834-32ea-9c94-10135582effe | -10.65118 | -46.46183 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 42862992-1510-3b06-89b4-3efcfe9a0317 | -9.45928 | -48.57906 | 2025-09-16 04:29:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 852a5e31-59fe-3114-95df-e6fdbf12394b | -8.1206 | -48.26283 | 2025-09-16 04:29:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4bbe581d-012c-3ab6-84ed-5303326d870a | -12.60746 | -47.95774 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8c8e6b5b-b37c-396e-9e94-b9e476ca0a74 | -8.00254 | -45.66639 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30f80781-f4e2-3195-a0e3-77db6bdd0534 | -12.67875 | -47.97651 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85414874-943c-3a5d-9ea5-71d3d1cac174 | -13.18972 | -47.3064 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05f502fd-6289-3318-b8b3-96077acea28d | -7.67898 | -46.28818 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c49f382-0cca-3bde-a4e4-8a7b41a5ce97 | -7.80792 | -46.11898 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2bdc2346-cdcd-3839-9a82-7ae8b1fb627d | -12.81157 | -47.24204 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 61e46432-7275-38a7-99d9-d9508f051628 | -9.13386 | -48.70889 | 2025-09-16 04:29:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 465fa4b7-6e85-34c7-ac38-a201e3ba9999 | -13.20749 | -47.30207 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29cd7347-c8fe-3409-9c6f-ff9f4daa4bc5 | -9.10084 | -44.86579 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 58e27baa-3eb5-39a1-b954-b45cf66b3a6d | -10.643 | -46.22679 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d92327b2-6575-32e2-ad6a-cf64e56f1ba2 | -10.78651 | -45.97578 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 685567cd-643b-3c74-8d09-84dd805f37e2 | -8.41487 | -47.21734 | 2025-09-16 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe7e382c-adf1-3c1d-ba66-6c5da5478964 | -8.93702 | -45.79648 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c27686b-cafa-33e4-b7f9-e4b7ecf3a966 | -11.70709 | -46.88363 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 87e71d96-61d9-3541-b9bb-134d13008edf | -11.69932 | -46.88963 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1bd97899-a33e-368c-8908-26a8fbd69f7a | -7.99303 | -45.66125 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0eca131-d04b-324b-a7ea-af4ec8d25f22 | -7.69238 | -44.66766 | 2025-09-16 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef2059ed-41de-3dc1-abc3-29281629f323 | -11.11566 | -45.34713 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e1bdecc-5a78-3569-a28c-6281998ff5f5 | -12.69372 | -47.98988 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4579f535-56f7-3069-bf7c-2f208b6f6819 | -9.136 | -46.93801 | 2025-09-16 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a4164e4-7c41-3efc-b6f6-e566fda15eb1 | -10.40686 | -50.63359 | 2025-09-16 04:29:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2cf9c75-5933-3e16-9166-7bb0d4682bb1 | -10.47378 | -45.16636 | 2025-09-16 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1f7bd76-d1af-3319-8502-e14e9322ff21 | -12.41803 | -47.80343 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7811f10-6a9e-3d23-9f2f-88cf2d095143 | -7.40141 | -50.00166 | 2025-09-16 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 42fd9fa7-3671-3c4d-bd06-7e19ab73aaa8 | -11.13174 | -45.33418 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 587babef-a172-3b66-bb47-97d46f0565de | -8.60843 | -46.33846 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 290a0417-8be5-3801-b16f-8da17cc181ba | -13.19972 | -47.30803 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 14bcd778-a621-3cf7-b6cb-f67e6c0045ff | -11.7054 | -46.87259 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9952a496-6ca3-3c0b-81b1-424a141b91c3 | -7.69352 | -44.66026 | 2025-09-16 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 928d0f4e-6a57-3fdc-9caa-62614339be30 | -13.51488 | -44.30267 | 2025-09-16 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e1a562ee-cd3c-3cb7-819a-6d1e26354ab0 | -13.21416 | -47.30318 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6d332c06-00cc-3433-9860-9e5a9301156b | -10.64952 | -46.47248 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 93e89c80-452d-3183-818f-e22550f9b24b | -7.70841 | -45.30693 | 2025-09-16 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eef9b908-5dda-360a-9f13-b14803c790b8 | -7.7306 | -45.30263 | 2025-09-16 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 414c1bea-07f8-36d7-8045-82343cf8317d | -8.00925 | -45.66748 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f8193356-e900-39ee-a1de-1c5adf2cb266 | -12.70136 | -47.74767 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c149b3df-b02d-3b1d-8906-f62376e37de6 | -7.56358 | -50.46033 | 2025-09-16 04:29:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d88f43ab-eb7e-3080-9987-d65a479223f1 | -8.61185 | -46.40359 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5ae8df83-304f-33ef-937f-37008cfe8142 | -7.99656 | -43.83308 | 2025-09-16 04:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 90f7c303-8709-33cc-8a4c-ac6519ca2de3 | -9.48597 | -55.96568 | 2025-09-16 04:29:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd343d62-223e-3dfb-a953-1ca4483b0526 | -12.96408 | -47.96495 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 21a992ed-d98c-321a-a36c-68166a3fcdf4 | -9.23091 | -45.65821 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e8b3030e-895b-3ddb-9583-71af445c950d | -8.65609 | -46.35298 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a5252827-4f8c-3f90-8cdb-70e5df3159be | -8.60021 | -46.41249 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb53d6a3-2253-309c-be96-decbf58f7dcc | -10.63854 | -46.23341 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca2910f6-deeb-3e5e-83c5-a39c71a973c9 | -12.80823 | -47.24152 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 445e9eb5-c895-3e7c-97ca-955db9ace1bf | -11.11565 | -45.32385 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7758f08c-7880-3351-b907-a3e14c6a7734 | -7.72723 | -45.30209 | 2025-09-16 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb76a26e-22fe-355f-afdc-a376f1acb359 | -11.70594 | -46.86906 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ab4da6d3-2573-3892-af03-d65a47ca1c71 | -10.11219 | -45.66367 | 2025-09-16 04:29:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99cdcd5a-95fa-39cb-8590-ea76e3b1b590 | -12.80879 | -47.23797 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a82da7e-af9b-35bd-9913-81f6f208fd83 | -7.40954 | -49.9873 | 2025-09-16 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 453c909e-9c3e-3198-901d-c6d1393a4139 | -11.45818 | -46.92387 | 2025-09-16 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb1818ff-de78-361e-92a9-1964fc6263a8 | -12.62462 | -45.75453 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6aef7810-49f4-3c1c-9e63-9835099fe4e5 | -10.71803 | -46.48668 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1605b304-fab4-35e1-a2ca-314bb69140ec | -12.73875 | -47.20464 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd8d30b2-e7c7-3d51-b4c5-fb1bf5483bd2 | -10.65007 | -46.46893 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8c0a4313-51a1-38d8-96a1-fd571ae22852 | -11.12139 | -45.30915 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d72c317f-e857-3b43-ac44-f01039f22d97 | -10.04863 | -44.34861 | 2025-09-16 04:29:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dde3fe9c-986c-35f6-a5fb-f68ea0430d95 | -8.90676 | -46.15506 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ccc2a2b-804f-3f1c-9756-265805fbb95d | -10.62995 | -44.21457 | 2025-09-16 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7f6f502-4daf-3cdd-bc0e-2390738edfd0 | -13.00405 | -47.94971 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ed30c9d-adfe-3725-9518-94c704153bc2 | -8.99241 | -45.75781 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16b22ce3-ed97-340e-b44f-c47c7ab9381b | -11.48494 | -43.60059 | 2025-09-16 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 21153a55-0834-3f75-81ed-584dd78c1193 | -11.97091 | -46.77561 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f94d182-29aa-328e-bc25-560b397063a1 | -12.80934 | -47.23441 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8398da9b-c9b7-39b6-a9b0-a47981cbcf08 | -8.96441 | -44.19625 | 2025-09-16 04:29:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ff5f680-d802-3ac1-8e8d-0507a4db8a2a | -9.08749 | -44.84879 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a24916c-fc1c-3efa-871b-d76c41f7489b | -7.44564 | -46.16171 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0f666ab7-9624-37d8-8790-1436007a6723 | -12.05614 | -46.53584 | 2025-09-16 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d8b08e4-6c73-3184-ba33-4cd26c5e0042 | -9.06408 | -47.03043 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ee9ddceb-d42a-3212-8da5-742599704a6d | -11.47253 | -43.58017 | 2025-09-16 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3febe195-de7f-3bc9-b158-b3bf6c659053 | -9.05756 | -44.83656 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e872c4fe-5d40-3595-a390-483caa330099 | -8.5868 | -46.34579 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| fb0b3b01-8945-3721-8eec-c12ce1e6ac0c | -10.13215 | -46.14696 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7e0c676-3294-3bff-a83b-246acd54a2e8 | -11.91193 | -48.55754 | 2025-09-16 04:29:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a49808b0-33f3-3837-98ee-a5834f07fe14 | -9.21164 | -44.50945 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f1f90778-be69-3f61-b9f4-752bab1d4a9b | -13.21805 | -47.30015 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4da1f5be-a743-3e45-afbb-489d38724146 | -12.04328 | -46.55224 | 2025-09-16 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 21c16e39-9159-345c-8106-a3550bf53a33 | -13.00129 | -47.94563 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 139e9dd6-4dc3-33e7-b17d-58c8e183a9dc | -12.10049 | -44.82646 | 2025-09-16 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ed53362-9039-3493-8afd-53a03fb20f8c | -8.12002 | -48.26648 | 2025-09-16 04:29:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README47.md)
