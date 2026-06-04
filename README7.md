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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06796022-822f-34ca-b262-487d41dabc90 | -12.2136 | -57.2888 | 2026-06-04 04:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 214.1 |
| ede30309-f248-3756-a8f4-5bc534c77484 | -11.5499 | -52.7867 | 2026-06-04 04:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 0b4b7dd3-3116-3c86-abb3-b48e3a901172 | -12.2325 | -57.2872 | 2026-06-04 04:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 2432bc39-025f-3610-843c-87712caad11c | -12.2327 | -57.2672 | 2026-06-04 04:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 98.7 |
| a4dd9530-90ad-3743-8e9d-7ef2e3eeb997 | -12.2325 | -57.2872 | 2026-06-04 04:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 90baa84f-9c93-380c-9018-b8407639f928 | -10.3842 | -49.4338 | 2026-06-04 04:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 682c44b3-5e70-3d5f-a27a-6dcf8d584059 | -10.3839 | -49.4554 | 2026-06-04 04:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 6bbf0f30-2d9f-35e7-8ebf-5bf709ea1055 | -12.2136 | -57.2888 | 2026-06-04 04:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 143.7 |
| b0c329e2-cc0a-3e1d-b812-92199a53ecd8 | -12.2327 | -57.2672 | 2026-06-04 04:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 113.2 |
| e235eed6-1748-3ef5-8870-b5f32a67f349 | -12.2138 | -57.2688 | 2026-06-04 04:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| fa05c978-ac88-31fc-9838-f5a5e212c6bf | -12.2325 | -57.2872 | 2026-06-04 04:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 1ce958fa-3768-3ad2-b1dc-6fe65180ac1a | -12.2327 | -57.2672 | 2026-06-04 04:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| fae0f459-5d68-3abd-855b-7862eea8cf51 | -12.2138 | -57.2688 | 2026-06-04 04:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 1ccd82c5-02cf-33ce-8b22-f029f8c12b7d | -12.2136 | -57.2888 | 2026-06-04 04:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 135.6 |
| 69aab96b-2423-3bd6-8f49-8ce266feb754 | -8.05 | -46.79522 | 2026-06-04 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42c0d795-d375-3cd7-a8ae-490a5eeb3428 | -7.27422 | -46.80878 | 2026-06-04 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7538fbe1-3145-3597-ab9d-1c11e423a0c3 | -8.57833 | -45.99829 | 2026-06-04 04:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dd4bdfc2-9289-3b69-9890-bc0efc83af4c | -6.39893 | -44.84009 | 2026-06-04 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e54db81a-f7b4-3955-98ff-0d0a0559c8dd | -6.76034 | -45.01073 | 2026-06-04 04:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58345bf2-e2f8-30b8-9ce5-1a2952543784 | -7.48683 | -47.50681 | 2026-06-04 04:42:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b18b4162-d582-3f87-88f1-126f031953e1 | -8.0688 | -46.19881 | 2026-06-04 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94aedde2-9176-3a94-924a-d8de5963c5f5 | -6.99132 | -42.87748 | 2026-06-04 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3f3f9d4d-d57b-3377-8070-5c0f723e8ba6 | -7.41096 | -49.66771 | 2026-06-04 04:42:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70f8bac7-ebc4-3c65-8e28-aec52a462d18 | -8.5748 | -45.99778 | 2026-06-04 04:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cfbb8229-5a04-3175-8c8a-378af47f114a | -8.26915 | -48.23412 | 2026-06-04 04:42:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2b65ab4b-7316-3993-b52b-f8e74056d411 | -8.27193 | -48.23815 | 2026-06-04 04:42:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34ea4bfd-a59c-393f-872b-285c10c4b09c | -8.29579 | -48.23835 | 2026-06-04 04:42:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3aaa612-b161-36ff-8034-a47b194b36d6 | -6.91039 | -43.62383 | 2026-06-04 04:42:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 11102ec2-13a2-38fa-8681-3a2ecccc11df | -7.54334 | -49.88602 | 2026-06-04 04:42:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 57f51355-4278-37f0-994e-1aca90f396ab | -4.36295 | -37.90092 | 2026-06-04 04:42:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9cc01a38-f443-3554-a4dd-3d0edfe2bf3a | -6.98965 | -42.88865 | 2026-06-04 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 00a95503-95a8-3f06-8f10-981a05215ba6 | -8.57065 | -46.00126 | 2026-06-04 04:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 399b889a-c050-3165-95b6-81f63ee61aae | -8.57126 | -45.99725 | 2026-06-04 04:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 45c478e2-5ece-365b-9516-12a340869a6c | -6.74316 | -47.12341 | 2026-06-04 04:42:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68818d77-a88e-3ee0-954b-5992aa09d10b | -6.98552 | -42.88805 | 2026-06-04 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e00e16b5-5a9d-3c93-9a6c-96dcedea95be | -8.28968 | -48.23381 | 2026-06-04 04:42:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f5eca15-31df-3874-a3db-b53fcd271269 | -8.07403 | -46.18796 | 2026-06-04 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a455dc4-8d71-3ca6-b751-c51848521e0f | -8.07344 | -46.19177 | 2026-06-04 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66950fb2-4b58-393d-9342-7559c8afd15e | -9.04051 | -46.31725 | 2026-06-04 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 222dcbc4-5633-382b-a8de-90b607c11f6e | -8.28024 | -48.22872 | 2026-06-04 04:42:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 833bf30b-3cda-3781-99e8-10f934ba6c52 | -6.98607 | -42.88434 | 2026-06-04 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 3baeea50-59c0-3e52-acd9-91ed80aaf289 | -8.57541 | -45.99378 | 2026-06-04 04:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5199b313-d65d-3c65-9010-8a0cefd9cc13 | -8.57418 | -46.00177 | 2026-06-04 04:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aa3cb999-9d7a-3a18-89e6-19f8df71f965 | -8.2869 | -48.22978 | 2026-06-04 04:42:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e3ad183-6f3b-3cdc-95c9-4cbdbb2f6ab0 | -8.28635 | -48.23327 | 2026-06-04 04:42:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ba717fe7-15da-33b2-ba4a-159454882afb | -8.99189 | -47.85171 | 2026-06-04 04:42:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 86efc00b-898d-3f01-a454-99e4b909d6a7 | -8.28079 | -48.22523 | 2026-06-04 04:42:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dada177b-46ec-34d8-9b79-7dbb8b202bf9 | -8.29246 | -48.23782 | 2026-06-04 04:42:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44951b52-496a-3644-862c-876a5dfa44fc | -5.52277 | -37.48342 | 2026-06-04 04:42:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a83ef984-9e82-3a7c-b6e7-e92c25fd15cd | -8.27746 | -48.2247 | 2026-06-04 04:42:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e742a86e-8cf4-37a4-a352-18c8c9754dfb | -8.29301 | -48.23433 | 2026-06-04 04:42:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2d990bf1-d678-317f-8ed0-baed5791537a | -8.28913 | -48.23729 | 2026-06-04 04:42:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8fbd0d99-395e-37bd-bf1f-914381390692 | -7.48579 | -47.5033 | 2026-06-04 04:42:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3602811-c1bd-3217-9ba4-1e6b202ad210 | -9.03643 | -46.32055 | 2026-06-04 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4410653b-1e4c-35e0-b087-8b10ce1a77bb | -8.2686 | -48.23762 | 2026-06-04 04:42:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c6254a4a-ddca-3feb-9eff-3b7697fa2eb6 | -6.99021 | -42.88493 | 2026-06-04 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9e3c69fd-5387-3cb7-a68f-48270d1cd796 | -5.52108 | -37.48547 | 2026-06-04 04:42:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5e474512-39da-3e81-8a14-586673e3709a | -8.07111 | -46.18367 | 2026-06-04 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 607b68ff-796a-34fa-86de-8eed1ac8d605 | -5.52217 | -37.48756 | 2026-06-04 04:42:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b0fd43c3-ee2b-3c13-abef-62778d817d14 | -8.35176 | -48.14333 | 2026-06-04 04:42:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f74ef2b-b96d-336c-b390-804ef83ed263 | -8.05341 | -46.79575 | 2026-06-04 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33e0a2bf-b421-31a1-9bf7-0beb5b1ef9da | -14.08974 | -59.38152 | 2026-06-04 04:44:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81eff516-bb12-309d-833c-96967300e833 | -14.08838 | -59.38825 | 2026-06-04 04:44:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef55dbd6-b133-349d-ac7f-ed51be063d18 | -11.88902 | -57.83278 | 2026-06-04 04:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 789a7403-967c-3ffa-bcd6-cdbadf22b7dd | -11.04524 | -54.19598 | 2026-06-04 04:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6523485e-b498-3cf0-bcff-d139990d1e15 | -12.21717 | -57.28885 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 5f2c9486-bc83-3f9f-9d18-7b729652432e | -12.00501 | -45.34538 | 2026-06-04 04:44:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86bc63cd-b367-3071-b8f0-40565140fd50 | -14.09209 | -58.88626 | 2026-06-04 04:44:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22ab4986-6f25-3ac6-83b5-8f93e19f5fc6 | -10.85154 | -53.75159 | 2026-06-04 04:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b9fd668-2684-3a2f-843f-a711d09a5cf0 | -11.57309 | -48.14225 | 2026-06-04 04:44:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 293f8815-c9c9-3d65-9a68-1327e70fbd27 | -12.43707 | -58.40314 | 2026-06-04 04:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 53ab8225-f4b2-3980-b4de-54eff59ac14a | -11.61376 | -52.55337 | 2026-06-04 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8aea35b4-9ca5-339a-85fc-94c39f5c1331 | -9.53095 | -47.7538 | 2026-06-04 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7efbcc52-e93a-328f-a9d0-83a700647503 | -9.39175 | -48.6214 | 2026-06-04 04:44:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae1f28a4-fcbb-3b6a-8601-13f785d23aa1 | -10.862 | -53.73799 | 2026-06-04 04:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd223c32-fbd1-32f1-9d1e-9e7e199b53ec | -9.89408 | -47.8577 | 2026-06-04 04:44:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 815776a4-6c90-316f-8a3f-0405e50c37be | -15.4949 | -55.72903 | 2026-06-04 04:44:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f55c8b2-cfc3-368c-a464-1bdd755eaf45 | -12.21693 | -57.27909 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| b71dfb35-c33c-3eda-846b-0c2215e4bf98 | -9.36863 | -50.54344 | 2026-06-04 04:44:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b452fe1e-abde-315b-b752-87a9d674029a | -12.43521 | -58.41046 | 2026-06-04 04:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6248db05-104b-3edc-983f-1872766692a8 | -10.39045 | -49.4483 | 2026-06-04 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 8cb555d7-8be8-323f-8515-c5fe58275a4a | -11.60673 | -55.33261 | 2026-06-04 04:44:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3543682b-0177-39d3-ada6-5f622810af23 | -12.46739 | -58.46936 | 2026-06-04 04:44:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3ed4f87f-f59d-3da8-a181-5733368cb51f | -9.56642 | -44.57751 | 2026-06-04 04:44:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67509f14-7074-3fc3-802f-fd287f3aa6a1 | -11.62919 | -55.18537 | 2026-06-04 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 17baa670-f06e-31d6-b547-992afcc92a7f | -10.82256 | -56.59435 | 2026-06-04 04:44:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93da49c2-f15f-3da5-84ac-6a1e3e3ec60a | -12.46618 | -58.4756 | 2026-06-04 04:44:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9a8c3e73-51b3-36b5-9f2e-822604c42abb | -9.80618 | -48.24437 | 2026-06-04 04:44:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55f7f7b9-8bc2-3531-8487-c27ab971d44b | -10.38378 | -49.44722 | 2026-06-04 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 106e8b42-33de-334a-88ad-83efa2c107f1 | -14.04701 | -46.33802 | 2026-06-04 04:44:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2d74e99-3a42-3b0d-b878-06a0d147bb76 | -11.26387 | -53.96564 | 2026-06-04 04:44:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d18083c-8ae6-36e5-855e-cd1651ac37f0 | -15.43836 | -46.33345 | 2026-06-04 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bfea410-daae-3b5c-89c1-e06e93a4b0f9 | -12.73801 | -54.2046 | 2026-06-04 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ea60081-86d0-38bc-8daf-bdd9888876e7 | -12.43641 | -58.40407 | 2026-06-04 04:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eeace840-693b-3024-9c77-3a952a7a7a6b | -12.21484 | -57.28999 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 90c72d8d-1312-3423-9f6e-29512d62796d | -12.45637 | -58.47037 | 2026-06-04 04:44:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9fefd238-1f2c-3895-94de-0c15981a4577 | -12.22278 | -57.2747 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d35a120d-38fe-378f-ab87-c31d1c89cf1b | -11.63344 | -55.18616 | 2026-06-04 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f532e54c-cfc5-3b7c-ab68-0a643836fb4c | -10.98841 | -47.07225 | 2026-06-04 04:44:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fc292382-c1d3-34c0-9931-b491133561fb | -12.43401 | -58.41685 | 2026-06-04 04:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README8.md)
