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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a040f375-3c88-303d-be2a-44fb6666d406 | -14.74428 | -48.1343 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 26f434bd-1910-3acd-b5f8-b82708b80788 | -15.66379 | -44.49741 | 2025-10-03 04:14:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e20306e5-69a2-3d18-a186-c1a37c4ec03b | -16.76775 | -43.95597 | 2025-10-03 04:14:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a492c2b-f3f2-3b51-8ffb-5a7b8aad9b56 | -14.97935 | -49.96758 | 2025-10-03 04:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5280b91a-36bf-394d-a83f-3fc6e658a365 | -14.94244 | -46.91188 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ac95734e-6953-32f7-b009-3c9a3b41acae | -14.8571 | -48.35971 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a3d7909e-5e78-3b76-90c4-246da7108bdf | -15.32573 | -45.05421 | 2025-10-03 04:14:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 631661d5-3198-35ec-83ce-0d1115f5ac07 | -19.60314 | -44.63163 | 2025-10-03 04:14:00 | NPP-375D | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 87fe7b70-0781-3568-8952-6aaaffbb550d | -14.87646 | -50.24474 | 2025-10-03 04:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 807aac0f-7bc1-3d1e-9beb-a4f1c130a3b8 | -16.02584 | -50.93553 | 2025-10-03 04:14:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e28c42d0-ec63-3227-abaa-e764b20d06b3 | -14.6523 | -48.24789 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 695a2700-805c-3f28-8a4f-cc5857db7b8b | -19.71378 | -45.91501 | 2025-10-03 04:14:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 36ae86c8-6050-345b-b4b0-922b5d123a31 | -15.23852 | -50.12354 | 2025-10-03 04:14:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dc10ac11-f192-39e8-8788-a09324e1dd54 | -19.71838 | -45.90818 | 2025-10-03 04:14:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4de8a9e-b9a3-3c97-a5f5-2d6f21b99474 | -15.61214 | -47.03888 | 2025-10-03 04:14:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0acd187-a9ac-3913-a96d-fcab2f87ab68 | -15.23312 | -46.96244 | 2025-10-03 04:14:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 217d07d0-c962-37c7-a255-b1992b0e6480 | -15.24257 | -49.31844 | 2025-10-03 04:14:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3647b2e7-4984-38d2-a193-0325bee1f586 | -14.90967 | -48.32822 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bb71e20f-baaa-3a73-9155-e156c83affd7 | -14.67175 | -48.07089 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 925cec7f-a2d8-3639-b597-a48d7cae480d | -14.90024 | -46.96631 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c0770284-1788-3b57-9465-8bdac55805c9 | -20.37175 | -42.20246 | 2025-10-03 04:14:00 | NPP-375D | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 515f0463-6c1e-3bdd-aefc-75223dfd75b2 | -14.72893 | -48.13567 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 899e0d29-aa3d-3b1c-8c04-d15488b34520 | -16.68514 | -53.01903 | 2025-10-03 04:14:00 | NPP-375D | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 771a9de5-8e92-34fa-be46-6113f7e45dc1 | -19.58726 | -43.83857 | 2025-10-03 04:14:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00db6b6f-74da-3f87-8a61-672aec3f5704 | -19.60065 | -43.8409 | 2025-10-03 04:14:00 | NPP-375D | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f3f7d4d1-b982-37ad-bf14-b5b27a0f86c0 | -15.21456 | -47.6531 | 2025-10-03 04:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bda5d680-4975-3ce9-a0e3-631e9bbab1d7 | -17.86942 | -57.62412 | 2025-10-03 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 2e4ad882-1c54-3bd0-8f75-822ffc142c57 | -15.24331 | -49.31435 | 2025-10-03 04:14:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16128280-8746-387a-8b9d-30a2741bb605 | -15.20982 | -47.18661 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52b606d6-ebf0-324d-abea-8600dee18c4d | -14.62167 | -48.23692 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1f0e9dac-9e1f-3170-939c-ff816fc61d2a | -21.34848 | -45.00964 | 2025-10-03 04:14:00 | NPP-375D | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 3e4bf24e-fad4-324d-9354-c41233a24ccc | -15.3167 | -46.38554 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e23090a2-8031-3a45-8673-b7a6447c77a4 | -21.34515 | -45.00904 | 2025-10-03 04:14:00 | NPP-375D | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 655aa111-6fff-3c28-83ed-742a105ffbeb | -17.70259 | -44.44104 | 2025-10-03 04:14:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3927211f-4daf-3f5d-8b20-be3c6a6e8007 | -14.93193 | -46.9132 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cbedc23e-ca6c-38dc-bb29-9d1dff845ba4 | -21.55712 | -45.27505 | 2025-10-03 04:14:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| af326a5d-4dec-3331-aad7-3b1305140fb5 | -15.35129 | -47.06042 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 994337be-2a18-3b2a-b5f4-f13c1ce0ecbc | -14.65137 | -48.2531 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9f290cd4-55f5-38ba-bdfc-ccbe66ba4743 | -14.90849 | -48.34624 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e2dcd9b-40e1-3797-9a46-499120f6723c | -20.04051 | -41.32857 | 2025-10-03 04:14:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e5e68892-b111-3a83-8173-97072bfc84c6 | -16.58369 | -44.00996 | 2025-10-03 04:14:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 538bd031-143d-3793-913c-0f835ce48fa5 | -20.36823 | -42.20189 | 2025-10-03 04:14:00 | NPP-375D | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cb55c6d8-07c7-34f8-a10f-aad0002d95a2 | -18.45091 | -43.80896 | 2025-10-03 04:14:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2784eb5d-1007-3469-af23-c5baa6fca19b | -15.52119 | -46.81071 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 999a25bf-1b45-3f97-9f44-59dbefb848c8 | -14.92899 | -46.90841 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 660818be-155f-3a56-b792-45c5fed95f4a | -14.91242 | -48.34713 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd3cc505-4a41-3418-af40-8b3f44e2f859 | -18.22318 | -47.96364 | 2025-10-03 04:14:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f4c13cb7-5c6d-33d2-a3f2-f9f79dbaac42 | -15.32072 | -46.29747 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c0e5bccb-cc06-3bd7-b9e1-9d4ab84ab431 | -14.91525 | -48.29762 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9866a450-bb3b-35f0-9e38-7b616018c00d | -14.87047 | -48.30762 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bc9dc6a3-8f8d-361a-9dd4-732e3fd90bba | -18.44897 | -43.7109 | 2025-10-03 04:14:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cdae0142-d0a3-3584-b3d7-ab659b3da008 | -15.60552 | -46.9264 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a02aade4-9f5b-3839-85e0-9d934844d6a1 | -16.36376 | -47.06392 | 2025-10-03 04:14:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6ba61a86-9712-33a8-bf3a-83966f28df38 | -21.24368 | -45.01056 | 2025-10-03 04:14:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2d1b8402-12ba-392e-a1e9-5d205d92fa80 | -21.06989 | -45.61324 | 2025-10-03 04:14:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 10a36eba-1bc2-3f7e-8c21-ffbf76d3eb9c | -14.92974 | -46.90399 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b649c476-b21a-3366-b741-c14a60fb29f2 | -15.31712 | -46.27586 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 027d8736-ecaa-3ae0-a265-3feaa28c9d87 | -15.19756 | -46.40733 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30248160-36c7-33bd-885e-b530ac03be5f | -15.51248 | -45.91077 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6655cec-4ccf-3b57-a44f-97b1a2a41154 | -17.9657 | -44.39628 | 2025-10-03 04:14:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a1eface5-e853-35dd-844b-67788363660e | -18.52058 | -45.0505 | 2025-10-03 04:14:00 | NPP-375D | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8f712d92-fa98-3a3d-bdba-70e695f5053e | -15.58978 | -46.90971 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca7acaa1-6ead-326e-821a-29968c974391 | -15.35633 | -47.06782 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9226d35-8d42-3f8e-9ea8-eabf525fb304 | -15.25238 | -50.12254 | 2025-10-03 04:14:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f305678b-230c-3398-810e-93c6971ffa7a | -19.46523 | -43.65083 | 2025-10-03 04:14:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e4342cb-3247-32b9-9875-475a11b175c4 | -14.93657 | -46.90244 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0311f495-7655-3f62-bc4e-dc85ed3afd54 | -19.51122 | -41.96666 | 2025-10-03 04:14:00 | NPP-375D | SÃO SEBASTIÃO DO ANTA | MINAS GERAIS | Brasil | 3164472 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 20421c85-de73-362b-8154-31737651faa7 | -14.92307 | -47.21696 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f473ac3-c835-3c18-a553-331a27532c27 | -15.92349 | -43.3061 | 2025-10-03 04:14:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79c9ea29-1003-3727-b11e-66cbae6e41ce | -15.94843 | -43.34354 | 2025-10-03 04:14:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c2ac964-4d63-3f39-82b3-e0cfa5c0ff98 | -18.15708 | -53.34236 | 2025-10-03 04:14:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb0317e9-f7fe-361d-9567-b4c58cc112c3 | -20.67284 | -44.05382 | 2025-10-03 04:14:00 | NPP-375D | ENTRE RIOS DE MINAS | MINAS GERAIS | Brasil | 3123908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| be3e4e10-728c-3056-a8a4-8f49b2b3483a | -16.33425 | -49.94038 | 2025-10-03 04:14:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 27e74b13-3fc1-363c-a824-170783cb5a29 | -19.81681 | -46.9212 | 2025-10-03 04:14:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c6dbac4-9a9a-390d-9c27-ca56d2a45e3f | -14.91045 | -48.30162 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4ab31f26-c435-331b-b326-126afc7e417d | -18.16796 | -53.34886 | 2025-10-03 04:14:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b3b3b3c-23a0-33eb-96da-e57349c5f944 | -14.62254 | -48.23211 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3dcf04c-9909-327c-8174-777b1c33a21c | -21.40717 | -45.8359 | 2025-10-03 04:14:00 | NPP-375D | FAMA | MINAS GERAIS | Brasil | 3125200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 20d35df2-12be-3892-ba7f-2325be0f6b73 | -19.90621 | -44.50626 | 2025-10-03 04:14:00 | NPP-375D | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e41edec9-c4d9-3297-a759-b94c05a37c76 | -15.59759 | -46.92907 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7570c97e-ff90-3968-a4d6-5673f97fd71d | -15.75816 | -47.77594 | 2025-10-03 04:14:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f27f7813-6a2b-319c-8082-6df74dba2b0d | -20.04108 | -41.32443 | 2025-10-03 04:14:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a1d51994-285e-3933-a5a1-2472c651859e | -14.7463 | -48.12312 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1c05f8f2-c9f3-31b2-b9a9-2d8a483e3009 | -19.58605 | -45.90727 | 2025-10-03 04:14:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86ab4d5a-3f3e-34d6-bbf5-6f9d14552df0 | -15.58839 | -49.06636 | 2025-10-03 04:14:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ff89d52-beeb-35cc-b62e-366af08e2b1f | -15.25932 | -49.32133 | 2025-10-03 04:14:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5fff1612-f54d-3eab-8684-3f7a375a71ce | -15.5853 | -46.91428 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9912714-b408-3823-a36d-51208313d02e | -16.58036 | -44.00939 | 2025-10-03 04:14:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3fc60fdb-44f0-3f5b-ba36-1a378feb53de | -11.0151 | -46.5393 | 2025-10-03 04:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 5afe6cbc-ac6e-3094-83db-496f445f21ff | -10.0148 | -50.2443 | 2025-10-03 04:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 38.2 |
| eab58b7d-c45c-3678-a633-4ff78d450aa7 | -11.9167 | -46.259 | 2025-10-03 04:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| f295fd83-22f2-3d7b-b99e-b743d9270224 | -10.0151 | -50.2229 | 2025-10-03 04:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 42.5 |
| b30ebb3b-f93a-381a-a8b3-d1f1b1a0c362 | -14.1936 | -46.063 | 2025-10-03 04:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 47.0 |
| f85eae7d-45f9-302c-bfd5-cb758e4d3190 | -12.6131 | -46.9725 | 2025-10-03 04:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 122.4 |
| dadaa4fe-64e9-3d6d-8510-811a21731bd4 | -13.7764 | -47.5617 | 2025-10-03 04:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 189858a6-c57f-3ff4-8ca6-fa94bbddb82d | -14.9342 | -46.8965 | 2025-10-03 04:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 3d0c22b5-f682-32ab-a647-dc4923d33625 | -12.6323 | -46.9697 | 2025-10-03 04:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 123.5 |
| d8c886ab-57af-3c3f-bda6-b4c2285dbce1 | -10.9939 | -46.677 | 2025-10-03 04:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 73cd7275-7a54-3424-913a-5531857c1064 | -7.7494 | -46.272 | 2025-10-03 04:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 226.7 |
| aaf20c88-7163-3454-8075-d9ca741176b1 | -10.9942 | -46.6545 | 2025-10-03 04:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 48.1 |


[Clique aqui para ver as próximas entradas](README85.md)
