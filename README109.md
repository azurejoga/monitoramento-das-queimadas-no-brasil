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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87996030-a628-3024-a90f-0a0568b610fe | -12.46507 | -53.13615 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 351a67d7-70a1-3039-ae82-70921334ef6f | -12.46429 | -53.14306 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31fc19be-229d-38dd-9fd4-b0efca537264 | -12.46384 | -53.14187 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d7a8e57d-588c-398a-8596-34caaa15dccf | -12.46354 | -53.14979 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8669613c-d8bd-31f9-9bf2-7b5fbf742e08 | -12.46313 | -53.14868 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 69767eb7-8234-3930-8b38-0460a24a5afd | -12.45737 | -53.14204 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0bcd2eb6-3a55-3543-a8ef-b9a8b432550d | -12.45691 | -53.14082 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 933db0e2-7ce6-3efb-899e-3a02e69d9fdf | -12.45661 | -53.14886 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e54cf2c8-1e7c-38bc-afac-ed1d6e377e58 | -12.4562 | -53.14769 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5f3c1a91-9880-3408-9bfb-95d26798c56f | -12.42195 | -53.14417 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5ae41f8f-8baf-3387-972e-d9fda4d1fa77 | -12.42123 | -53.15071 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 88f58ff8-15d1-33a5-9de3-11a79a80efaf | -12.4205 | -53.15739 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 6e7af3e2-ad08-3c24-b383-060956514e9c | -12.41429 | -53.14987 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 41436dee-bc5c-3a25-b645-7f67d16b4172 | -12.41357 | -53.15644 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 92eebc78-c4dc-34e5-9575-bfc074c6068e | -12.41285 | -53.16311 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 53e833ce-511b-3c14-863f-a34dacc1a26f | -12.40664 | -53.15559 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 64f6d364-4799-3969-ad2f-a4979ea167c0 | -12.40593 | -53.16214 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1da1e892-8b74-327d-86ec-4ae48f5ec13b | -12.40521 | -53.16871 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 97cc693b-cb9e-3c84-98df-c94dd73fab52 | -12.44102 | -54.56309 | 2024-10-11 05:42:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e95e22d4-b294-3235-b959-087eecfee8bf | -12.44025 | -54.55988 | 2024-10-11 05:42:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 566191d7-6235-3be6-9c54-e25d18e58f32 | -12.43961 | -54.56527 | 2024-10-11 05:42:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8dc17069-0559-3478-83f1-92426ef0ad65 | -12.43463 | -54.56236 | 2024-10-11 05:42:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f03eff0d-9ac7-3ffd-95e0-c5b6ec411e34 | -12.43386 | -54.5592 | 2024-10-11 05:42:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4f98cbb-2426-39dc-8448-286c991094fd | -7.96487 | -54.76967 | 2024-10-11 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9620d252-3044-3828-a279-6aa54ca8c50b | -7.96427 | -54.77406 | 2024-10-11 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b849c20b-2337-326c-9bde-8533990c008c | -7.96224 | -54.76178 | 2024-10-11 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ef6879c-09c5-3b14-939c-cd06a82c27a5 | -7.96168 | -54.76616 | 2024-10-11 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb821ec3-8ecd-3933-9049-dd3ad0e41c02 | -7.96111 | -54.77053 | 2024-10-11 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38669bb3-e93f-3df6-924c-6f17115face6 | -7.9601 | -54.76012 | 2024-10-11 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e80c89e6-3798-36b0-844d-5dc1ff9a2693 | -7.9595 | -54.76451 | 2024-10-11 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b02eff6-530c-3470-852a-f17107ce428c | -7.95891 | -54.7689 | 2024-10-11 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea21e1f2-cecd-3441-857f-9a59bf2d5b59 | -7.91364 | -54.88073 | 2024-10-11 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52985085-661a-310f-b0d6-d39ed61a6fbf | -7.90775 | -54.87981 | 2024-10-11 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c81db81-55eb-32a3-ad96-35eb6557ca04 | -7.82814 | -54.72457 | 2024-10-11 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9e1ae3c9-47de-388a-b4aa-163a27cae867 | -7.8276 | -54.7286 | 2024-10-11 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3342d85a-7977-3418-b423-7e87c9e89e25 | -8.49436 | -55.16133 | 2024-10-11 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3bed6761-1388-3039-bfb6-2cd8c4f7791c | -8.49381 | -55.16554 | 2024-10-11 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67619215-f940-3bc9-b85f-f2aa6630cccb | -8.48795 | -55.16482 | 2024-10-11 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9a556be-7f76-3160-85cb-a1037ecdbbe2 | -8.44398 | -55.45549 | 2024-10-11 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 637228c5-7f84-39bb-b252-0e6d20ba974a | -8.44348 | -55.45936 | 2024-10-11 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e77ea0f5-067f-3bcb-9d17-88e5fe03d4ef | -8.43823 | -55.45483 | 2024-10-11 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd1d033c-bdb7-3b41-8d36-6b160809501d | -8.43773 | -55.45866 | 2024-10-11 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1faa6943-6b73-321b-98f3-34e78b3c56b1 | -8.43723 | -55.46249 | 2024-10-11 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d2469aec-3933-3a2c-b571-223d914071cc | -8.43672 | -55.4664 | 2024-10-11 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| fe6b5321-43c4-3658-a737-da96e5c48976 | -8.43621 | -55.47032 | 2024-10-11 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1babf13f-9193-3676-903a-41f32a31bb2e | -8.43569 | -55.47426 | 2024-10-11 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4a9a42c9-21c2-3254-adf6-3662b62643ab | -8.43199 | -55.45796 | 2024-10-11 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1bd2abdc-463d-3eaf-bb59-1f207b89cc46 | -8.43149 | -55.46182 | 2024-10-11 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b2f9785f-7e05-3270-9827-600de20b6fb4 | -8.43098 | -55.46574 | 2024-10-11 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 960fcb73-ab74-341d-a1f0-b264be2e020d | -8.43046 | -55.46967 | 2024-10-11 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1533ab87-725a-3b8b-a34e-7d46c75e260a | -8.42524 | -55.46505 | 2024-10-11 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e13ad0e-3d6d-3929-bee6-65373da02373 | -8.36358 | -54.9555 | 2024-10-11 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ccd20b4-37bd-32de-8a39-29079c168033 | -8.35768 | -54.95463 | 2024-10-11 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b6c92fa-af1b-3723-8f25-e1c5d5de4aa1 | -8.29468 | -55.37991 | 2024-10-11 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e80cf03c-4678-3763-b3d2-24794f7a16c0 | -8.29461 | -55.37816 | 2024-10-11 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 238f8ab2-8bd0-38e7-a352-17ee63912cd3 | -8.29418 | -55.38386 | 2024-10-11 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a09e88b-2c5f-39eb-9ecd-45a80d7c5e1f | -8.29407 | -55.38211 | 2024-10-11 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5e19ec7-11ae-36bd-ae5f-c53e90444202 | -8.29045 | -55.36723 | 2024-10-11 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7dc12dd7-f5f0-3b58-9c2f-78e72a817698 | -8.28994 | -55.37119 | 2024-10-11 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f37f94a3-b6b3-3ac3-b0da-1dee7fe89cf5 | -8.28992 | -55.36948 | 2024-10-11 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 912c1d2d-6e63-340f-b11b-3887662d611b | -8.28939 | -55.37344 | 2024-10-11 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 93de6bf4-45bd-3973-b12d-7850536e058f | -8.28893 | -55.37913 | 2024-10-11 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0c7c1b2-c7e1-323e-9c7c-9ab4baeeb14e | -8.28843 | -55.38305 | 2024-10-11 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e364cba8-4051-3a04-9632-8be8e51388fd | -8.28832 | -55.38133 | 2024-10-11 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd7120f8-dbf0-3ff2-aa5b-1c45c9adc685 | -8.28793 | -55.38697 | 2024-10-11 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e958b822-cff9-3ffd-adc6-9e1b0c5e0b83 | -8.2878 | -55.38524 | 2024-10-11 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b997558-4edc-36c0-a201-61fbed251ab4 | -8.28417 | -55.36869 | 2024-10-11 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 781b5f3d-64a7-33ba-8b30-87451a85db42 | -8.28365 | -55.3726 | 2024-10-11 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16957dce-c5af-35ba-abe3-e3cad3aa579f | -8.28206 | -55.38443 | 2024-10-11 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d30c287-8274-37f9-866d-ed28c33309af | -8.28153 | -55.38836 | 2024-10-11 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8b88e4d-c24f-30a6-8339-0a416ebe5f06 | -8.2779 | -55.37175 | 2024-10-11 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fcb97abc-337e-35a1-ace1-d4d3c756c851 | -8.27738 | -55.3757 | 2024-10-11 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb082ddf-7e44-3657-b3e4-b311ba226d83 | -8.27579 | -55.38754 | 2024-10-11 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fbda384-c95d-38a4-a8c3-1814cd3e977b | -9.40185 | -56.29385 | 2024-10-11 05:42:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a1b18077-e1a0-3c1c-a73d-fa5c515b2691 | -9.40137 | -56.29752 | 2024-10-11 05:42:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 23064d65-9210-3b63-b49c-8c0e43e34469 | -9.40089 | -56.3012 | 2024-10-11 05:42:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4ddb27fb-6e04-3d4e-ada2-156fb8eb4b58 | -9.3958 | -56.29741 | 2024-10-11 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4f4a3d8f-554c-32c3-b819-6b2a3fb2f69f | -9.39532 | -56.30105 | 2024-10-11 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bfe8e960-b6da-304e-86cf-afeb624d7ea0 | -9.39485 | -56.30472 | 2024-10-11 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5d0889d-3932-31b7-bb4e-0db71e18a0b7 | -9.26913 | -56.89936 | 2024-10-11 05:42:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68e87d2d-5ee5-369d-8fc4-84a386955aa7 | -10.38804 | -57.29734 | 2024-10-11 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50d9480b-0783-3b6e-894f-030de8c4bef4 | -10.38793 | -57.29758 | 2024-10-11 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a084f272-d3c5-34f0-b94c-52951465d56c | -10.33465 | -57.50022 | 2024-10-11 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7583592e-df62-3a4e-9343-1d5406833430 | -10.33424 | -57.50328 | 2024-10-11 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea5c5f43-5536-3e2e-ae7c-ad97a16403e2 | -10.33384 | -57.50633 | 2024-10-11 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 05391af3-c46a-32ba-bfe3-58258c810d09 | -9.95825 | -58.10353 | 2024-10-11 05:42:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| acfa8bce-4711-3204-9f85-fe25618d1e1d | -9.95556 | -58.10407 | 2024-10-11 05:42:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eb0f5607-49a4-3682-b4d2-dac3c8d1bcb7 | -9.95485 | -58.10955 | 2024-10-11 05:42:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1eff846-8430-3ed1-81e2-7f7cf94ef339 | -9.95336 | -58.10281 | 2024-10-11 05:42:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4da3242c-ae9c-3e6f-aec6-ef99b9fb1f09 | -9.95261 | -58.1083 | 2024-10-11 05:42:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c8abf0f-da94-3065-8175-7d4da0cd9fd1 | -9.95186 | -58.11379 | 2024-10-11 05:42:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea85d04c-20a3-3589-8bf8-9bbca059851a | -9.95067 | -58.10335 | 2024-10-11 05:42:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 81c0d3ac-f876-35a8-a24f-7d4ebb05a19c | -9.94996 | -58.10886 | 2024-10-11 05:42:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75ed246e-701b-3303-bcf1-07f3ab84926e | -9.94925 | -58.11436 | 2024-10-11 05:42:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 088db3e3-807d-3727-9a3a-c140799bbc56 | -9.94855 | -58.11978 | 2024-10-11 05:42:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ddd523b-1245-3a45-a2ab-af78ee5f3699 | -9.94846 | -58.10212 | 2024-10-11 05:42:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fa84d4e2-1934-39d2-b953-7a66a70c8e61 | -9.94771 | -58.1076 | 2024-10-11 05:42:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eb1aa4da-17ce-3a08-ae21-3f269b7deba2 | -9.94623 | -58.1185 | 2024-10-11 05:42:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4caaee6e-78be-3ed5-b37a-5e8b1182214f | -9.94357 | -58.10142 | 2024-10-11 05:42:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a6b493d6-5869-3831-bb01-fdb4633befd7 | -9.94282 | -58.10691 | 2024-10-11 05:42:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README110.md)
