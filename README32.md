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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ad675e1-22f1-33a1-a43a-459c57ee906d | -2.85747 | -45.31465 | 2024-11-23 04:16:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 958595dc-0c7a-3c72-aae0-e8b36383c895 | -0.04538 | -50.81436 | 2024-11-23 04:16:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2908560-3516-3b83-9568-412d7b38c5a5 | -2.70947 | -46.09673 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 17c39188-8482-30b5-ab9b-4c5205e1628d | -1.20705 | -51.7495 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 695282ab-c770-3135-8f87-46a895c3956e | -2.70425 | -46.26512 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5ea2f118-2340-3314-a4f9-1a5885ed4208 | -2.68673 | -45.66389 | 2024-11-23 04:16:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 84c8ea98-d67c-34f5-b3e3-7fa13171b2ac | -2.69553 | -46.84559 | 2024-11-23 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0aac4af2-5213-3a70-afd8-ab1efd58856f | -2.7053 | -46.28114 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3f73282b-e7d0-3dd2-9914-a934fd533c78 | -2.84693 | -45.18475 | 2024-11-23 04:16:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 13642002-8ef8-37cc-960a-7fd1e934b505 | -1.77834 | -53.60866 | 2024-11-23 04:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4bf4e79b-507e-39e1-8c0a-13557ec7c8fd | -2.70381 | -46.24524 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 04d2a111-5753-3ce2-8b25-85901a9eee38 | -2.45037 | -49.0881 | 2024-11-23 04:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a73871fc-2359-3218-9b26-dad318088462 | -2.43858 | -46.52639 | 2024-11-23 04:16:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7466198d-29a3-3392-831e-9ea18f9005d7 | -1.6747 | -53.20998 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d06372e-f0b7-375a-b422-76b30cb69aee | -2.66512 | -46.60564 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bf39bc6f-924c-3b35-acbd-e64443693e53 | -1.748 | -52.38868 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cf274aa-930c-37c1-afc7-b9de0023299a | -2.07703 | -47.15547 | 2024-11-23 04:16:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a042279-3573-3de4-8477-265e0f581217 | -2.52555 | -46.38906 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3a14593-fef8-3d7d-86ba-d713a88eace4 | -1.71611 | -52.48834 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc1b3169-d1b6-306e-8a1c-d704f679dcbd | -2.66449 | -46.60963 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bfc59e0b-19f3-3dec-87ca-c6ac059c1db9 | -1.63179 | -52.60818 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 308a52bf-2da5-3ec3-bdcb-9a997a050611 | -3.26888 | -45.44119 | 2024-11-23 04:16:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 382b0036-7c63-33c2-aee4-5be1152dc114 | -1.19719 | -51.97019 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af438053-c59f-37d2-8f51-78fdb95c8261 | -1.18676 | -51.93756 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 243fcdbe-d0e5-3b84-bed7-4f35fae70bbb | -1.52436 | -51.6273 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 0a3afa71-dba0-3f9c-a759-d08efe81c123 | -1.10933 | -52.34893 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ab40f40-2e36-3bdb-8be0-783c27cc64b6 | -1.19316 | -51.77114 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f94e0cb-a011-3002-acff-22d74a5fccba | -1.81107 | -52.16939 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 09530b8f-998e-3817-815d-e206dc1d3d28 | -3.17136 | -45.72739 | 2024-11-23 04:16:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 111270e0-320e-3f87-8067-2c7ac94acfb4 | -2.68867 | -46.09349 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 553dd8b9-bd55-3b3f-b09c-e53434867049 | -1.77141 | -53.61538 | 2024-11-23 04:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 951da62a-8928-33f8-8434-6da5a1499bd6 | -2.67981 | -46.26126 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e5c9beb-34a0-30c7-87ab-adb3912cf5e7 | -2.69847 | -46.09889 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fab524f9-2a55-3daf-9adc-3d0f22fbd137 | -1.60665 | -52.60292 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 46d67c45-ed39-3fe2-ab80-4995c72dd25a | -0.93535 | -47.55595 | 2024-11-23 04:16:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f73544ff-f3cd-3ce4-8030-6a5fb644c779 | -2.60508 | -48.24433 | 2024-11-23 04:16:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4940919a-850b-307c-b932-d2deae39c389 | -2.69072 | -45.66074 | 2024-11-23 04:16:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4da9e619-d633-3961-9b6b-59d4a7e5b344 | -1.30957 | -51.75426 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0654bc1-7731-37f2-98a9-33626aa36c22 | -2.01321 | -51.17144 | 2024-11-23 04:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6d033c3-07b8-33e6-97f9-8143673cac42 | -1.19772 | -51.77487 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9fcbfa8-df1c-379a-8f13-d192569f22a2 | -1.19136 | -51.94144 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c756fe6e-4aad-3bdd-8d4e-d35a9e6dabf7 | -1.7833 | -53.64908 | 2024-11-23 04:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a166ed23-36b6-35b3-81a8-0a580482f11d | -1.92208 | -46.81251 | 2024-11-23 04:16:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a9b7e01-4bbc-333f-8656-04dac0741f2b | -1.07195 | -53.37074 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60d1efdf-6218-3526-a90d-4256f15af27f | -2.68406 | -46.16712 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9908869-b7b7-3f26-9d01-f7f01b28fa35 | -1.66037 | -52.70148 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29548188-7c51-30ef-98c9-32dd4f1b61cb | -2.28896 | -46.32909 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44ca9c22-a918-3949-8056-6dd1e74542bb | -2.55879 | -47.32504 | 2024-11-23 04:16:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00444b67-6551-336e-babf-f67115e16dc1 | -2.77206 | -48.40701 | 2024-11-23 04:16:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 39b4817f-0dfb-34cb-a718-d88709be5692 | -1.65983 | -52.70481 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a9c5e428-d9ea-367e-8d3d-00b8fbcf6d4e | -1.45229 | -53.40059 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ac243108-1ec1-3822-b29b-e05fc70de0e6 | -2.58709 | -46.54819 | 2024-11-23 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a0ad175-b9f7-3943-a646-080766333a43 | -2.56192 | -47.35229 | 2024-11-23 04:16:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 498f5a7c-b588-3cc1-a186-083235e1d3cc | -2.70242 | -46.27672 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 863b4955-bde1-3a1e-b6ef-ac49cc241381 | -2.70607 | -46.25354 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2776492-d9f5-3c7b-8567-6df6f5452f36 | 0.38568 | -51.08962 | 2024-11-23 04:16:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4af6ced1-ed6e-3d66-b09b-95076aa836a4 | -2.70495 | -46.08047 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3faf3bf0-2262-3eba-b4f9-64492f26808b | -2.52844 | -46.39354 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9322c1f-14d1-33ec-960a-d422620b7864 | -3.6105 | -41.67721 | 2024-11-23 04:16:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f0cc1afe-2ec8-3522-aad5-fb831bcafec5 | -2.18321 | -45.67727 | 2024-11-23 04:16:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7f651136-25ac-3714-9204-01e6d3308ba6 | -1.95472 | -52.07845 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9b8e98f-1068-336f-83c3-c33487947260 | -2.69487 | -46.84977 | 2024-11-23 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc9d595f-09ce-32cf-8c7b-db204f4ea54f | -3.07714 | -45.96711 | 2024-11-23 04:16:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2190d4a-6c65-396c-8c39-a05aec195fa4 | -1.50412 | -52.03835 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a998114e-8911-34c1-a044-550f2c7e25f7 | -3.14508 | -44.4808 | 2024-11-23 04:16:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d20f0e2-f05d-3c61-b158-eec5e198d4c5 | -2.64708 | -45.1607 | 2024-11-23 04:16:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c81ab126-1cdd-3587-8997-4114b4842564 | -0.91822 | -53.10072 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ffecede-a873-3008-a7ef-fd6b130f44c1 | -2.71007 | -46.09293 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad2cc231-69ed-3d6a-8933-1fdc96b222fe | -1.11453 | -53.39339 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a15a23ad-1759-3906-9f3c-15d062f298b0 | -1.29173 | -51.73649 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 919af729-6c02-338c-b1a1-161008d26444 | -1.2615 | -51.76437 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ed3fa72e-7661-3a7c-bc6b-25ea173deaa4 | -1.63795 | -52.70461 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91fe729c-000b-3f0b-8e4d-e6540d772f06 | -1.18284 | -51.96162 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 378f08f2-98cf-35f4-a3fd-d4b53016b6d6 | -1.18235 | -51.96464 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59abe183-6dd0-3a4d-a285-766ad932e116 | -2.70364 | -46.26898 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8eba162e-5747-357f-9ede-8c5348322a31 | -1.83467 | -54.52332 | 2024-11-23 04:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e13cb9a5-f7ee-35d4-bd64-08c82b2dce68 | -1.28199 | -54.54545 | 2024-11-23 04:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 24285829-5366-3478-80dc-4c7cfb582ee6 | -1.22561 | -51.79449 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 063673b8-9779-3042-9dda-1b550c2f0201 | -2.43512 | -46.45663 | 2024-11-23 04:16:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 08936282-c90f-378b-9ab2-62bcdb56e8d2 | -2.52655 | -46.40535 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 274b521f-bbc7-316a-8e7e-cddfb35b3032 | -1.28671 | -51.73567 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0dd7c99a-7ba4-3d74-a317-cdf99c61e184 | -0.97705 | -51.71747 | 2024-11-23 04:16:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| efd2195c-8d00-3591-9514-717ca8b62058 | -2.3278 | -47.0862 | 2024-11-23 04:16:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77f199da-8c49-389a-bcce-e47a698a598b | -2.64372 | -45.16018 | 2024-11-23 04:16:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fbc6d5a1-44f0-396b-92e3-d8da03bd0038 | -1.677 | -47.0583 | 2024-11-23 04:16:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b66db6c5-563f-3625-bd47-abca3550375a | -2.56691 | -46.562 | 2024-11-23 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b25cb29-cb28-3281-a3b4-d1f226aa05b2 | -0.96099 | -51.72091 | 2024-11-23 04:16:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e57bda2a-ffdd-3cb2-8e50-b59299d74c56 | 0.767 | -50.80505 | 2024-11-23 04:16:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c2c65895-3eed-36ba-a344-0d5f42e9f175 | -2.68332 | -45.66334 | 2024-11-23 04:16:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38da38b7-971f-3dba-881d-1c4c7cbece4f | -1.20562 | -51.75824 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a3c22e4-f0fb-3413-b950-4a41c4c4caa0 | -1.29765 | -52.27969 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbb9bf36-5f9d-387e-90e2-a9e82eb3d5a4 | -1.6337 | -52.69705 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 25c0af9a-602d-310c-82c1-60f285dfab57 | -2.69205 | -46.18412 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a4df2ac-48a8-3861-8ed7-bcda0e5e187d | -1.75304 | -52.39321 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09f3095e-3e40-3637-95e7-967264e1c606 | -2.00949 | -48.10286 | 2024-11-23 04:16:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ba052be2-84da-328a-a1f6-17e5e591ee21 | -1.64329 | -52.70549 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 614f5606-0553-35eb-9d0e-8b1e78e8c530 | -2.56399 | -46.55742 | 2024-11-23 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b0111abe-5ed1-38a0-a7b8-78e5bcc11eb3 | -2.27883 | -47.70973 | 2024-11-23 04:16:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 08b69d5e-1fdf-30e1-8bd1-f7a0db4b0d0d | -2.15496 | -50.49522 | 2024-11-23 04:16:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb7f2720-4aa1-3903-9142-176fc1dcb8cf | -2.70286 | -46.04896 | 2024-11-23 04:16:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README33.md)
