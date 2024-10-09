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

## Dados Diários - Página 172

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0caf5d58-5654-38cf-804f-fc99e4b3911b | -8.98494 | -52.8007 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd78bc29-9cea-3322-8878-d012c012228f | -8.98256 | -52.79147 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7000f2bb-8486-3343-bf5b-48f8adeed7bb | -8.98189 | -52.796 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fd60ef7-91fd-3217-b8dd-8d48df6ea0a0 | -8.98126 | -52.80021 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9f7192f-8430-3321-a088-a965bdcf33e6 | -8.97888 | -52.79094 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44dd1fdd-aab1-33f9-a585-45672ab98c1b | -8.94947 | -52.78653 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e246841a-6a0c-38a6-ba52-540dfd46f2ea | -8.94452 | -52.79464 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 784261de-a1d8-36a9-a2aa-7467972728a7 | -8.93589 | -52.80235 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a7698f32-acca-335f-9cff-3c488efbdffd | -8.86802 | -53.01227 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fb3a95e0-9194-3ccf-8dfa-5de8e08dafa5 | -8.86742 | -53.01644 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cacb920a-0f8e-3c34-b8b1-74b83bcf9786 | -8.86691 | -53.01396 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 570be090-8d09-3da7-a6e8-77e9eca55c14 | -8.86613 | -53.0508 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c78798e-88de-3bb2-801f-955c61ab17ae | -8.86581 | -52.99663 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb48f8a3-91c9-39cc-af48-8902dbbfef59 | -8.86482 | -53.05242 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 49aa5f4b-2856-34dc-8477-64397158ef84 | -8.86328 | -53.01343 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 255e90ea-7b6e-39c6-8b58-ef86684261a8 | -8.86252 | -53.05021 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 58af4aab-36f5-39ad-89b6-4987110cf84a | -8.86215 | -52.99625 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ed7658e-67bc-3f77-97ad-459470fc33c6 | -8.86152 | -53.00043 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b3b04b4-0b25-3e6b-81ac-da08c1124706 | -8.8609 | -53.00457 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76bb7b54-5647-39c6-bcb7-8352d62771cd | -8.85729 | -53.00393 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a6d321a-1a2b-3525-9275-e0f95a2458b1 | -10.61976 | -53.67406 | 2024-10-09 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e941c68-516c-3e3c-bfa0-15715191b258 | -10.61916 | -53.6782 | 2024-10-09 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 145a9e1b-0d0d-39f5-9485-f8201615f36a | -10.6175 | -53.67508 | 2024-10-09 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c824765d-5a07-3574-861e-6d9c2d2bac5f | -9.75429 | -53.154 | 2024-10-09 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ecd4a8d-da58-3801-ac5b-d4864dd6f8c2 | -9.75003 | -53.1577 | 2024-10-09 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9b48c26-b82e-3c7f-a7c0-e576da6ee93a | -9.74577 | -53.16142 | 2024-10-09 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bca38b05-8e6d-3990-bcc8-cbbc487677a2 | -9.72811 | -53.18068 | 2024-10-09 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9167d7d-6fbf-393d-89af-ba4437e45a10 | -9.71522 | -52.83413 | 2024-10-09 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b60a59f-88b3-3715-b9a1-63db5501bd66 | -9.67055 | -52.23758 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 410da6db-4928-3da4-a0d0-a64e3cab2a15 | -9.66673 | -52.23693 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2b66883-e295-3bc9-844d-b6315b6d1303 | -9.66606 | -52.24164 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1915fd2d-917b-30d6-abf8-37aa6a5164dd | -9.66292 | -52.23628 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9b5ef34-b05c-3661-a972-aca1afcc4b04 | -9.39976 | -53.2045 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7cb5d77-c242-340f-82a1-a5f2c8cb7c63 | -13.31743 | -53.72772 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c40042b-f445-3700-b9e6-183ba1afe60f | -13.31687 | -53.72604 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b889f5ae-7259-3ddf-82cb-c4c34c1f8664 | -13.31624 | -53.73051 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 640045f0-669f-3584-a6cc-574a039c2964 | -13.31439 | -53.72276 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7adfdd16-214d-363f-8d0f-cdfd529a012e | -13.3138 | -53.72106 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a4be1f7-7e81-3376-8d55-1a312513d9c9 | -13.31374 | -53.72721 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d95b8f61-e024-39d0-b085-04b48b804493 | -13.31318 | -53.72553 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77ed8353-8e1c-31c8-a460-d578ff47a488 | -13.3131 | -53.73165 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40640bf8-2231-3342-a12d-1cdadb636441 | -13.31256 | -53.72999 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 514d1794-5e0f-3c3e-af92-d108a9bf2b86 | -13.3107 | -53.72224 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a395858-c0af-34fb-aa3d-d842636e280a | -13.31012 | -53.72055 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f264b3d7-a68c-3934-91c4-a23a2a1eb547 | -13.31006 | -53.7267 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0487143-4b89-3ec2-838e-09380e62e45a | -13.30949 | -53.72502 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecaf5364-15fd-30b3-9518-c53a9a711cee | -13.30941 | -53.73114 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f41b930-401b-3cf7-b1f1-7fb0a8891ec6 | -13.30887 | -53.72947 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1575ce29-178b-33da-891c-ef7389a7fe29 | -13.30877 | -53.73555 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71ede390-6def-30bf-bb7d-0a9004518756 | -13.30826 | -53.7339 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c34c99b-c0cf-38ba-b0b5-17db10e07102 | -13.30767 | -53.71726 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 310cd779-a437-3f9b-9818-53d2479db15e | -13.30764 | -53.73832 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 481a2ee0-3d52-308a-8e46-543ef3109689 | -13.30702 | -53.72174 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7aacb981-5d0d-3b13-88f6-e1b2122e0416 | -13.30637 | -53.7262 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 365d3e0f-dcfd-348b-8875-db38e7abf336 | -13.30572 | -53.73064 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a203c74-6e20-398d-b26f-c42b7eaab460 | -13.30508 | -53.73504 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0e6d7ee-7fab-3ea8-ba8a-8ddda902bef7 | -13.30444 | -53.73945 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57e353a5-8ae1-30db-851d-e41374e940a3 | -13.30333 | -53.72123 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 776cdc7b-7af8-3403-97b8-4fe5dd269997 | -13.30268 | -53.72568 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b6c3fde-d7d0-3620-b3c7-a18940da1cea | -13.30204 | -53.73012 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03ebabf4-a40b-3f36-831b-b83836c39c53 | -13.3014 | -53.73453 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67fa2bcc-28cf-3597-a496-0b640cba0902 | -13.30076 | -53.73894 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e207f98-f38c-39ee-8ab6-1eef022940e1 | -13.29771 | -53.73402 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a692e62-973f-310d-b77c-1ee46c491a1b | -13.29707 | -53.73844 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 524970db-8c50-32cf-bd49-9c5a868ac8de | -13.29339 | -53.73793 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1d2af11-85b7-3497-bc0c-423d6cd6ebf5 | -13.29275 | -53.74233 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0330e261-84d7-39da-a615-17a47f2d0926 | -13.29246 | -53.69224 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f753a3f4-2536-3a4d-a234-2d320f869a51 | -13.2897 | -53.73741 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f860c7e2-51dd-32fc-bff2-1042b028bc94 | -13.28907 | -53.74183 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec9d9b0e-bc0f-3e07-8e43-b741ded33e65 | -13.28813 | -53.69619 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c651860-5228-338e-9ee1-52d7971871f0 | -13.28602 | -53.73689 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3cd1c5cf-62a7-38d2-af19-858090a4892a | -13.28444 | -53.69563 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b29f1c1a-1da5-302d-a608-3d1cdc2a742f | -13.2838 | -53.70012 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 02c80649-f6ef-3296-9fc2-6c3f273e3e90 | -13.28076 | -53.69506 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b7478b95-2007-3b7c-8ee6-a1a7ce6b90ba | -13.28011 | -53.69955 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8c71001b-1d3d-3d6f-949e-78947ad76149 | -13.27707 | -53.69452 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d1ec0dd2-aa57-3f46-9327-e7fd56db85a6 | -13.27643 | -53.699 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bdc8419-5137-3020-9226-4c68a4adfaaf | -13.00271 | -53.66014 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f81f704-eaf6-39aa-8a3b-341a964a4697 | -13.00207 | -53.66454 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e89ed685-7167-3aba-8065-dbe6e7ac6e77 | -13.00151 | -53.66174 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a88033db-fe67-3f4d-bd70-ac4553194741 | -12.99903 | -53.65957 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 925502d2-c153-3967-bdab-6b96d6e126c5 | -12.99783 | -53.66116 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f56cbd4f-907c-36a0-b36a-b44b95c2bad8 | -12.99471 | -53.6634 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 151d850d-30ae-380c-b35b-555666e568b1 | -12.99415 | -53.6606 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 370f0f96-7d72-3588-a5ab-4e72c301c4c3 | -12.88409 | -53.47065 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09fe7222-7716-3c33-87a3-d8ccd35eea42 | -12.88344 | -53.47519 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90ffd2ae-ede2-3498-b690-c4ece94c1032 | -12.87973 | -53.47466 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23b188a5-1903-3de2-82bb-4ce3c31035e1 | -12.84833 | -52.82583 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb98e3a0-aab8-3759-bac0-dd4c9f3ab8f8 | -12.84516 | -52.82038 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d278726d-43bc-3554-a007-4e5fbd1bf259 | -12.84448 | -52.82526 | 2024-10-09 05:04:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 61793879-208f-3054-bd3a-de42e479a725 | -12.84379 | -52.83015 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4041e00-9d08-3607-ab37-ce84a78ac1d7 | -12.8413 | -52.81985 | 2024-10-09 05:04:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c2806af-58fc-3332-a384-d418f3010913 | -12.84062 | -52.82471 | 2024-10-09 05:04:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06822a89-0e82-3ce8-9c54-5f8ce83899b2 | -12.83994 | -52.82958 | 2024-10-09 05:04:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 78a0b51b-a7c2-3089-a945-6dd718e39a79 | -12.83744 | -52.81932 | 2024-10-09 05:04:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da90057e-b180-35c8-88c9-b79774bb25f4 | -12.83677 | -52.82417 | 2024-10-09 05:04:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 222b7806-75cc-35f5-8335-014049548bbd | -12.83609 | -52.82903 | 2024-10-09 05:04:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 26ec104e-8adc-35d4-a168-31685ffbe31b | -12.83541 | -52.83392 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e413bc66-587a-3849-918e-d58111197866 | -12.8329 | -52.82366 | 2024-10-09 05:04:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7123e6a-4fc4-3d51-8927-ae5878c64156 | -12.63432 | -53.11184 | 2024-10-09 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README173.md)
