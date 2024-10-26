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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c51cce4b-edda-3085-b119-3b34767f7c48 | -15.26584 | -43.05794 | 2024-10-26 04:21:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d21219f3-16a1-3f02-adb0-d8d1f9b8826c | -14.24949 | -44.14278 | 2024-10-26 04:21:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41fb7e29-0276-350c-83c0-4ab4839436d3 | -14.11917 | -44.38901 | 2024-10-26 04:21:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dec399cb-3c43-3d82-96a3-cf3c6be5fefd | -14.11573 | -44.38847 | 2024-10-26 04:21:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c68f3eb7-af42-3035-b563-655ee8280499 | -14.06205 | -43.70582 | 2024-10-26 04:21:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54482c18-8168-30b2-92ee-9cd984372094 | -14.06147 | -43.70987 | 2024-10-26 04:21:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1804def4-40c3-32c8-8fa1-0bc388f3c1a3 | -14.00284 | -44.11067 | 2024-10-26 04:21:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a49e8ae6-d7af-3176-ba52-535a5ea3364b | -13.99937 | -44.11013 | 2024-10-26 04:21:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 914af1bb-bfdd-3ae3-96db-2358c1080a1a | -13.97714 | -43.72304 | 2024-10-26 04:21:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04a43b2b-d418-3e32-92e3-c891dc83a56f | -13.86094 | -44.4595 | 2024-10-26 04:21:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9e66774-f122-3f2a-9137-0dd55eda30b0 | -17.87964 | -57.56748 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 68275a2d-1fa0-3033-8255-52f3e252feb3 | -17.87897 | -57.57061 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| ba40f23e-e356-3d1f-9373-4887dab5fdd1 | -17.05606 | -53.45598 | 2024-10-26 04:21:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ee3fc763-43b5-39ac-bf5f-7e16c9b5966c | -17.05521 | -53.46036 | 2024-10-26 04:21:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d546c92-3f63-3334-a558-e1c993371e05 | -17.0552 | -53.45644 | 2024-10-26 04:21:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3ed84f59-74da-3a27-9d20-042eebfb7fcb | -17.05438 | -53.46084 | 2024-10-26 04:21:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e4dea55e-5145-3aee-b575-4f6f022e6e6e | -17.05168 | -53.45117 | 2024-10-26 04:21:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ce8aecbe-0894-35f9-ba6a-5443147a50e5 | -17.05087 | -53.45551 | 2024-10-26 04:21:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d537548-5588-3061-908a-9f8756325d00 | -17.05005 | -53.45991 | 2024-10-26 04:21:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 762ac282-75de-314b-940d-497a93262fa1 | -17.04894 | -53.44177 | 2024-10-26 04:21:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 689adae8-24aa-3893-b849-4937abc1cb20 | -17.04815 | -53.44603 | 2024-10-26 04:21:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 41b2d75b-5fe9-3498-aaa1-9aa07b3838e4 | -17.04734 | -53.45032 | 2024-10-26 04:21:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8fb13846-92ed-3661-8640-10b43df2d980 | -17.04654 | -53.45464 | 2024-10-26 04:21:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 93ded0c8-1b85-3454-88d9-5057a0a1c747 | -17.04572 | -53.459 | 2024-10-26 04:21:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e400e2f9-ecd1-3ccf-bece-7d86fbf5c4d3 | -17.0449 | -53.46338 | 2024-10-26 04:21:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8f29bb57-94b2-3d99-a005-204f924ba797 | -17.0446 | -53.44095 | 2024-10-26 04:21:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7417dd7c-0bd4-30a4-ae46-aa76c911810a | -17.04408 | -53.4678 | 2024-10-26 04:21:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dabf8f88-4efe-33ae-b7b0-3f4372fdce53 | -17.0438 | -53.44523 | 2024-10-26 04:21:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 434588db-4ef2-3a8b-8701-083da4e8a6a4 | -17.04326 | -53.4722 | 2024-10-26 04:21:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8cf7060e-a4c3-382d-99a6-7a2e8d695ce0 | -17.04137 | -53.4582 | 2024-10-26 04:21:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b20b75e9-1766-3d31-89ba-f723e1d3a396 | -17.04055 | -53.46257 | 2024-10-26 04:21:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 45a80cd4-a649-360f-bc7e-0055591e1786 | -17.03702 | -53.45742 | 2024-10-26 04:21:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8d552d16-856a-37e9-9667-94ca87c5746b | -17.03621 | -53.46176 | 2024-10-26 04:21:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9a7ad8a4-848a-362b-8a7a-f84bc0997879 | -16.38107 | -54.5767 | 2024-10-26 04:21:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8211dfeb-9df7-341d-896f-e63a75383741 | -16.55516 | -56.24399 | 2024-10-26 04:21:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c5734fc1-fc4c-3b53-a091-97d4aa3f2333 | -16.55652 | -56.23735 | 2024-10-26 04:21:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 093b8f5c-37e2-39b2-8cd2-85cc5d111530 | -16.55585 | -56.24067 | 2024-10-26 04:21:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c1dde4fd-f650-3322-b493-397952142278 | -17.01446 | -56.50983 | 2024-10-26 04:21:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3b8a7eed-374d-309c-bd2c-3f2a073ea012 | -17.00848 | -56.51203 | 2024-10-26 04:21:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| dac723a9-5889-38ad-957b-7f789a46167d | -17.03651 | -55.98384 | 2024-10-26 04:21:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 90c30ce2-27b4-3f27-aaed-77bd821cd296 | -17.03587 | -55.98698 | 2024-10-26 04:21:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 872139eb-1361-38af-a863-df8d9588d293 | -17.03141 | -55.9827 | 2024-10-26 04:21:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f6e0770d-54f5-3f6d-b131-cd83054ac8bc | -17.02567 | -55.98471 | 2024-10-26 04:21:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 48daa3f8-acdf-3e87-9ab1-1d39117cc180 | -17.01736 | -55.99925 | 2024-10-26 04:21:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d3a30eb0-b7c1-36db-9ded-7c2b96d097a1 | -17.01671 | -56.00239 | 2024-10-26 04:21:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4229712e-7f87-3dc5-a4ad-1b6483d5aeb1 | -17.01606 | -56.00555 | 2024-10-26 04:21:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a10370c7-a6cd-3a0a-b8f7-570d90d4854c | -17.01225 | -55.99811 | 2024-10-26 04:21:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| bce4e3fb-7d49-354b-bf04-d5139ee1d693 | -17.01161 | -56.00126 | 2024-10-26 04:21:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 68bdcd26-5c1a-3b29-8bc7-07cc72ce32ec | -17.01096 | -56.00441 | 2024-10-26 04:21:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| c9d9b387-48b1-3651-825b-b6def89d8e3c | -17.01089 | -56.51144 | 2024-10-26 04:21:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 78a8adb5-9298-3c87-b914-4d94c58dfc8d | -16.56493 | -56.2497 | 2024-10-26 04:21:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7f15fd26-7353-386d-8db2-14465c9b4786 | -16.56174 | -56.23854 | 2024-10-26 04:21:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 72782aab-3be9-322b-b625-bc9a8f25f4a4 | -16.56039 | -56.24519 | 2024-10-26 04:21:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6692f30d-9bd5-3878-8102-5d34ccc0033d | -16.55971 | -56.24851 | 2024-10-26 04:21:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 3563409a-f206-38ea-8ea9-f5da92b8d647 | -18.20569 | -56.64838 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| cdc1181a-ab2a-3b2f-99ff-cf3d79d6ae1c | -18.205 | -56.65169 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 55af06d1-2213-3ebf-b749-d4d5c855c204 | -18.26931 | -55.99099 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| b7f4aa6a-7b0c-3f7b-b239-8a095bd597a9 | -18.26434 | -55.98985 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| d62461be-eea1-37b5-b9ee-eb53c8047107 | -18.26312 | -55.99585 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| c80bb9d8-f9e7-334b-bb25-1d9500cbced5 | -18.26068 | -56.00787 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 6b7cf905-1a14-333d-96da-036d39542f3d | -18.25946 | -56.01389 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 404422d8-1044-3fef-a748-8bc1b6e400e3 | -18.25692 | -56.00073 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| c9627a8c-de6a-3ec1-b9a7-e23fa1a6aa0b | -18.2557 | -56.00674 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 9e5b6f5b-1115-31ad-9dbf-b149cad222f1 | -18.25447 | -56.01276 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 85da1967-bbbf-3d6c-aade-f122059dd24b | -18.25071 | -56.0056 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 5781a631-2847-36bc-80a9-c9783bb4455a | -18.24949 | -56.01161 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 4900d839-a008-339a-b2f6-d75008ae4b7b | -16.74769 | -56.66895 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| f47375be-2820-3708-a122-3446ee0e8f1f | -17.27111 | -57.51077 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 192552a3-4f37-3715-89a7-7d00f688c363 | -17.26553 | -57.50946 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a06011dd-5961-30d4-a158-407b7195341f | -17.2647 | -57.51337 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9c5e8696-1d43-34a7-bf0b-1c5362c41b6b | -17.26386 | -57.5173 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| e2b98b75-2c69-3c63-af78-6ad3f154392d | -17.26161 | -57.50036 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| a9e969a4-19c9-3c7c-9966-bc16ec8f398a | -17.26078 | -57.50426 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 0ac4039c-4dfa-357a-a1cd-973878a4b97c | -17.25687 | -57.49515 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 0f1151ba-41bd-36e2-8773-97f83519c3a9 | -17.25604 | -57.49904 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 5351c56f-4d16-371c-9058-57bba6db031c | -17.25521 | -57.50294 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| f43d478b-36ae-3baa-bbcc-17de81596378 | -17.2513 | -57.49384 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 37acfbfb-bc12-3728-8c65-eb30e315720c | -17.25046 | -57.49774 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 57c05e74-d6d6-3644-a7e1-42c8a2c94c89 | -17.24963 | -57.50164 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 2eca9b43-b809-3cbb-b152-bb9d513f575b | -17.24489 | -57.49644 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| bb0d817c-31cf-3a63-826c-974a398dfcb9 | -17.24405 | -57.50033 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d6193e40-b435-3eb8-b6b1-d6a9fb8d2699 | -17.2329 | -57.49774 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e76a2afb-bac4-3e5c-a309-70b34012c978 | -17.23048 | -57.49702 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 672533b8-4b61-300a-a331-2c0557f4a90b | -17.22732 | -57.49644 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 89418cef-7e2d-3b8d-9d08-57d63c01739d | -17.22491 | -57.4957 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 86db703a-3e0e-3448-9dda-637023d0f5ff | -17.1406 | -57.4646 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| fe28e2ed-bab0-3f8b-8be1-a20261bf9331 | -17.07825 | -57.48284 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b8838d23-edad-3c56-bbc9-419d698014f0 | -17.07743 | -57.48676 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| df3616c8-bd40-3b5e-9ed6-024e17f72996 | -17.07634 | -57.40867 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| dabfb133-d414-3faa-934a-3fe58b44bfba | -17.07306 | -57.42421 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 0994f97e-709d-3b67-b605-93424da8494e | -17.07224 | -57.42811 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d6494201-6255-379d-8e97-b46961b339ca | -17.07078 | -57.40738 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| ad21a78e-284d-3995-9f85-4d1b93790939 | -17.06996 | -57.41126 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 8ee9a394-6c1c-3918-8495-b21a3f77d403 | -17.06667 | -57.42679 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| d9e1a894-01a5-351f-87b3-4a45b8406558 | -17.06066 | -57.48284 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| efce4ce1-fb6e-35f0-8390-52e509a1cb70 | -17.05983 | -57.48677 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 272c851f-84a9-3a39-a371-02d919f789a8 | -17.0553 | -57.45283 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9ff6154f-b860-3a55-b6ed-7de02e7c4a27 | -17.05507 | -57.48154 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ae916c22-4ff3-30b6-9188-4ae400bc0a6b | -17.05447 | -57.45674 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 551d90a4-bbf9-3951-89c1-b90b23ebfce7 | -17.05424 | -57.48547 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |


[Clique aqui para ver as próximas entradas](README57.md)
