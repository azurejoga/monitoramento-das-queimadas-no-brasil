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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d8ce392-2783-36d6-a575-d7133dbc8e33 | -11.3549 | -47.66841 | 2025-10-05 05:14:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca9f6e19-564d-3aa6-b98b-402783f84a8c | -9.31448 | -45.66206 | 2025-10-05 05:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3c615c5f-9e10-3191-b31e-db8f19e20879 | -8.58306 | -46.30166 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 2022709c-2fe1-3690-aaa6-cc9f73d8b1dd | -10.44834 | -48.37678 | 2025-10-05 05:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 19e906c8-353a-3fb5-8903-118cdd3315d8 | -11.5286 | -47.67665 | 2025-10-05 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 683f138a-c104-39bb-9c05-2d577a05e53e | -8.62538 | -54.96804 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 10060e2b-9f12-3aee-b87a-f8f05433b179 | -11.53411 | -47.68142 | 2025-10-05 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0b9ea144-143c-3e6c-b24a-b2c7fe5d56c5 | -8.85881 | -46.10342 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4e89858-cfe7-3714-bacf-9498acddf2bb | -7.61114 | -45.46847 | 2025-10-05 05:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d79a520b-a474-35d0-a87a-e5d937b85035 | -6.16767 | -44.60016 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| af451288-1b41-376c-a54e-247070045070 | -8.611 | -54.96594 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb079d47-3fa5-3dde-9856-1bcd60b24ab9 | -8.57855 | -46.3363 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 24792419-38de-3796-87e9-9691a005ebd6 | -6.18539 | -44.62158 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 271c8809-4819-32b8-9d43-dee96ef7868f | -5.13676 | -60.38903 | 2025-10-05 05:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 551c0d23-7542-39b3-99b3-73e66ed76298 | -11.70304 | -47.50751 | 2025-10-05 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ddc9173-375b-3ffa-8d27-1b53fa37fe6c | -11.00059 | -46.52043 | 2025-10-05 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 28281866-d869-3838-8a43-88c3b874435b | -6.18867 | -44.61456 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb5da8a4-66eb-3f20-a6c5-7bbae93d1050 | -10.39867 | -45.41245 | 2025-10-05 05:14:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2454672-b761-3b59-99c1-aa4fa2ec521e | -9.32231 | -54.52946 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2eb6244a-b6c5-36e7-88bc-a3591ac2d937 | -9.0201 | -58.98474 | 2025-10-05 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3c261c2-2cc1-3b91-82ce-b742cfaa1273 | -8.55481 | -46.27252 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d13abb36-fead-3c42-9952-fdf2ce2dee2a | -6.17283 | -44.63046 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 00893b18-0945-36dd-9f61-9e44d024a181 | -6.18948 | -44.60839 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ca67b4e-d930-3338-aa0c-788bcbf5a563 | -6.18669 | -44.57705 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aa71a6a9-1ac5-342e-af4b-ec8e09660565 | -10.57551 | -48.68591 | 2025-10-05 05:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d63fac07-cbeb-3536-90bb-320ad6f94571 | -9.32602 | -54.52999 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5297c80a-22f0-3026-812c-cc876d905c14 | -11.09315 | -47.88301 | 2025-10-05 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4b5814bc-54c9-3d10-b503-189f3f4d2ece | -8.5993 | -46.27536 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50babfa6-f0c0-3237-96a0-fa60f258f641 | -9.29778 | -46.01821 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 55da633b-9708-319d-83d1-17d4d5089c0b | -6.17101 | -44.57572 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f61730b4-fbe3-390f-b931-85b0d3d5674f | -11.71156 | -45.35049 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85c88b01-439a-3dce-b43a-e6a0c2909deb | -7.7933 | -44.55175 | 2025-10-05 05:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff35c31b-4ded-3aa6-8c0d-5d843527dd7d | -8.43397 | -70.12846 | 2025-10-05 05:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ab086405-acb8-3fca-9ecc-48bcc4f7ffb8 | -10.57504 | -48.68956 | 2025-10-05 05:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48357dc0-27a1-3c7f-86bc-46319a7ad08e | -11.82528 | -45.07898 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a0f04565-184b-3fba-be94-adb6344056d9 | -8.57547 | -46.31086 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 39837e8f-53e9-39dc-a574-66752da4e051 | -5.13743 | -60.3848 | 2025-10-05 05:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67a151c0-3926-320f-a48c-14e1fd58cc98 | -5.9904 | -51.88692 | 2025-10-05 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45df7143-bb30-3be9-b9ff-0c1c0a0d7b53 | -10.4895 | -48.10644 | 2025-10-05 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ebcfc0c-75da-34ec-8d35-ac73be76edae | -6.17388 | -44.65518 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e24d7b18-4109-33b9-a7c8-8b7202ce1355 | -9.2983 | -45.9602 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b89a09f-420d-310e-ae4a-d7238f385262 | -8.54087 | -46.33149 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8019176-7d31-383a-8ab4-8d3a2ea668d2 | -10.757 | -46.61767 | 2025-10-05 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e455d74b-f0d7-358d-8148-b85c51e7e46a | -6.1601 | -44.60519 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4bf6d697-788d-3770-9edd-93ceee0a573b | -11.46218 | -51.52045 | 2025-10-05 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8c185793-60f3-3151-a30c-21609c968da9 | -5.99676 | -44.36395 | 2025-10-05 05:14:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ab82fa57-5c11-39e2-90fa-a722c90903f4 | -6.98872 | -44.21606 | 2025-10-05 05:14:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e2da12ff-c5a9-35e9-a4bf-2c5ffa915c26 | -10.05103 | -49.20665 | 2025-10-05 05:14:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e651760-b12e-384f-9c20-170ca5bdc9c1 | -6.17994 | -44.57597 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a6aaab8-d1da-3e09-a205-10740b2cf956 | -6.01563 | -44.01896 | 2025-10-05 05:14:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8d2e7b6-7688-3b81-abbf-dd5278d8a5f3 | -9.25993 | -46.77838 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0e0c7d75-dfeb-3d5a-806d-1a2b20e463dd | -12.4479 | -44.74454 | 2025-10-05 05:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c043cebb-4d98-33b5-944a-1d286efc4d2f | -8.53713 | -46.31075 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5aa4876-a8a2-342c-9422-a50e46b6ae36 | -9.9853 | -57.81948 | 2025-10-05 05:14:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a36153e-e18f-353a-b067-c32074336a4d | -8.86026 | -46.84609 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f52008f1-4370-313a-a786-36e313078d6b | -8.5867 | -46.32274 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f931cbc0-af79-3d73-83da-c1b172a369ac | -6.425 | -44.46659 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7f48d158-66b5-34bb-885a-daf40b3e163a | -11.09847 | -49.86941 | 2025-10-05 05:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac5fa43d-93fc-31c8-ae5d-09b9db80fe12 | -11.80694 | -46.85512 | 2025-10-05 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2d15e732-b83e-3e31-9b70-6fb55d9c9c54 | -6.17839 | -44.58786 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78c83346-3681-32c0-b211-4c07fcd959f2 | -9.84463 | -60.27686 | 2025-10-05 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ba6d1b5-544e-3414-9390-3fcaa0918651 | -9.33521 | -45.76683 | 2025-10-05 05:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2d90fcaa-44db-3feb-a0e0-f63de80e9d8e | -9.29204 | -46.01148 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 709dc97b-7432-33c2-8723-36e04381efba | -9.20367 | -46.92621 | 2025-10-05 05:14:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6010e087-0b39-3b48-bccf-489a785c154a | -6.43055 | -46.02401 | 2025-10-05 05:14:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33140c9b-f097-3ffa-8409-e84d22688bfe | -10.49999 | -48.11267 | 2025-10-05 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 045529b4-0479-321d-980d-a73b9a36868f | -11.81267 | -45.06383 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d179b653-0d75-34cc-82f2-03f35eaee4ef | -11.59372 | -46.7169 | 2025-10-05 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c5acd1bf-c9da-32b7-8d45-f2581e56f447 | -6.18104 | -44.62025 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 10459529-b9a4-353d-9ad4-f5ca0e5b79e9 | -9.31383 | -45.6675 | 2025-10-05 05:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e7d04421-3f08-3d95-a07f-f05c081b9e7e | -8.59494 | -46.30861 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1118d649-577a-36ca-b285-4f19c512f9ff | -7.71077 | -46.26772 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b10ab57-17fd-3e23-ab6d-dc2831cc6c0b | -9.25933 | -46.78307 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c748c543-f469-3df0-90cc-3e934a4bf85f | -11.14779 | -47.92365 | 2025-10-05 05:14:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f0b9724f-5e74-3ac1-8c1d-14b97186ad01 | -7.16164 | -46.08783 | 2025-10-05 05:14:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bf9cea4c-ecbf-36d8-b930-af08d606444b | -9.63438 | -54.31503 | 2025-10-05 05:14:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe2ed024-67b8-397b-9fca-9306c9721c53 | -11.01813 | -46.70183 | 2025-10-05 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| daef27ef-6aca-3f0c-909f-2d96e61e89af | -8.54067 | -50.15615 | 2025-10-05 05:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a713378a-335d-3b4c-95c5-e5e425411862 | -6.14909 | -44.58477 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 17f26804-17c8-3a51-a408-05e9ec568f6e | -8.55544 | -46.26764 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d734b11a-52c9-3558-8057-62991fdc22c5 | -5.97015 | -44.35458 | 2025-10-05 05:14:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 45b9ea62-d455-3fc0-b18b-5413ea90da40 | -9.45418 | -56.65119 | 2025-10-05 05:14:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1702e576-7461-37ab-9626-7165e88411df | -9.19471 | -59.55246 | 2025-10-05 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f3020a7-5801-3545-88b9-79f9bec6d1f6 | -9.04883 | -61.64085 | 2025-10-05 05:14:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72f704ea-07c0-3b53-b2b6-a9429c44346b | -11.04012 | -47.79272 | 2025-10-05 05:14:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f7b7e774-9a3e-3955-b089-344f61d02d8e | -9.84385 | -59.47128 | 2025-10-05 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9d415eb-22d9-36ea-99b4-2f30f34669bc | -6.14743 | -44.59703 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6d1a1067-d45b-3daf-8562-12c199b2dd41 | -10.47089 | -57.50127 | 2025-10-05 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b31df57f-3b56-3b5d-b850-79834255ef25 | -9.6419 | -54.31617 | 2025-10-05 05:14:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3bbb4883-822f-3e75-9f61-a362366cf5b3 | -11.83252 | -45.09598 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 76a2c595-fea6-3154-80b8-3e83435dc1cd | -11.11991 | -49.866 | 2025-10-05 05:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d8e83cd-fe8c-34d7-9dfb-0ff5f071cf9b | -8.58933 | -46.3026 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ae71c2af-f315-3dbb-a23e-67409a4744a2 | -10.36561 | -48.28242 | 2025-10-05 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c7dd4066-28fd-3f89-b59d-8dc56e16df3b | -6.59067 | -44.32055 | 2025-10-05 05:14:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0dc53613-925c-3cf9-a47f-e848185df6f3 | -11.22843 | -49.9276 | 2025-10-05 05:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3fbf92c4-3fe7-370d-ae22-a09fde79ff4c | -7.58794 | -63.35749 | 2025-10-05 05:14:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 575c1a58-c830-30e8-b8d3-07faee46bdde | -3.89868 | -52.1907 | 2025-10-05 05:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f84418cb-8987-3c5a-8e43-5f180f75826d | -6.84366 | -45.48909 | 2025-10-05 05:14:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e95075d1-a57b-312e-8989-29c31e763418 | -9.99413 | -48.29682 | 2025-10-05 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b0e435e-5cbf-3c29-803e-eaaa15a2ee3f | -6.14855 | -44.63949 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README125.md)
