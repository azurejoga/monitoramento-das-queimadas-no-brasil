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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf8bb437-b6d2-3ab6-ba31-25bb05785bc5 | -4.57553 | -45.60974 | 2024-10-24 04:32:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4d7c068-39ea-39f8-bc71-1052c6a15be8 | -4.57466 | -45.61002 | 2024-10-24 04:32:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d57f020-b004-3182-abd2-292f5d7b7557 | -4.76568 | -45.75851 | 2024-10-24 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 313808f1-24cc-3610-997d-29cfb15958db | -4.55675 | -45.80073 | 2024-10-24 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f5189f9-d08a-3e56-8d48-fb0018e05fb5 | -4.5562 | -45.80436 | 2024-10-24 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09c069a9-6ee5-376b-b18b-571eddb03fdf | -4.55337 | -45.80023 | 2024-10-24 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b167b313-3b9d-3f43-a4a2-e7fd679d849e | -4.55281 | -45.80387 | 2024-10-24 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 05e1bdb6-25a0-3f1f-9350-8211eac5f1ea | -4.54999 | -45.79972 | 2024-10-24 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 59544bc0-626f-3ad9-b800-87782c5eb06e | -4.54943 | -45.80336 | 2024-10-24 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7613f045-9248-35c1-b514-e396b973346b | -4.54661 | -45.79919 | 2024-10-24 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 165e109a-b630-32b7-8740-d2699a753c31 | -4.54605 | -45.80286 | 2024-10-24 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aedca8c0-5034-33a2-8fe9-1cf3e29bb978 | -4.5451 | -45.79927 | 2024-10-24 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d2cd5577-170a-3c8c-b9bc-ae143a45ea0e | -4.54453 | -45.80293 | 2024-10-24 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82a5e544-6ba2-3613-bcce-ec5f3c34f5cb | -4.54172 | -45.79877 | 2024-10-24 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6cb48e98-b3ea-3736-8c5f-53cc583017ae | -4.49705 | -45.5942 | 2024-10-24 04:32:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35200fcb-0072-3e34-92d8-080a17842c52 | -4.46476 | -45.89396 | 2024-10-24 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4313253-f106-329c-adcb-3cdf1d6cd25a | -4.4642 | -45.89756 | 2024-10-24 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7c19dba-b8c0-351b-8628-505230dfe478 | -4.46146 | -45.645 | 2024-10-24 04:32:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| e7eebace-a1c9-3dd6-9223-929252624f8e | -4.46139 | -45.8934 | 2024-10-24 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b08cbada-feee-3562-a72f-954e428a36f1 | -4.4609 | -45.64867 | 2024-10-24 04:32:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3ad82157-8ceb-30d8-bd44-adac08d2a3cd | -4.46035 | -45.64475 | 2024-10-24 04:32:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 39141593-e070-3feb-b3bf-5290b10e2e53 | -4.45978 | -45.64842 | 2024-10-24 04:32:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c44e7d1c-a045-3744-8c84-6a18f688332d | -4.45696 | -45.6442 | 2024-10-24 04:32:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6f2b8c4f-c3a1-3563-aaaa-5ea0d25c126b | -4.44428 | -46.02642 | 2024-10-24 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed9ed20e-929b-3d8c-b4ab-d97f0c7adacb | -4.41957 | -45.986 | 2024-10-24 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d32589ad-19c7-3634-8475-6952d689ef16 | -4.37013 | -45.77938 | 2024-10-24 04:32:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a9cb2cd-d0e4-3dfb-87c0-19535eda63a3 | -4.29606 | -45.99978 | 2024-10-24 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4ed6f6c-6ef7-3965-90db-07dabccfc6ca | -4.29327 | -45.99571 | 2024-10-24 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4778a9d5-47bf-3d37-818b-0861d0498b68 | -4.29271 | -45.99926 | 2024-10-24 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 25381923-08b4-326e-9b4f-65cf9ab48e89 | -4.08838 | -45.51294 | 2024-10-24 04:32:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7fe77cee-4c87-343d-8926-f12244cee21b | -3.99109 | -45.79534 | 2024-10-24 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d23746d-6a96-3d3f-806b-a5d2a2e1ec83 | -3.87141 | -45.8431 | 2024-10-24 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba924392-5479-30cb-a9bd-c4c07cbc40f5 | -5.06487 | -45.5053 | 2024-10-24 04:32:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 595859bc-b67c-32db-ba0f-0df84f9e4b39 | -4.99393 | -45.94488 | 2024-10-24 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d307af9-0846-31fc-ac48-4447f8f0a12f | -4.96548 | -45.51342 | 2024-10-24 04:32:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b277bd70-ee8d-3d92-8ae0-66efd9fefaca | -4.96205 | -45.51291 | 2024-10-24 04:32:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0897b59-7a0d-3a42-b71f-4f22b1f34151 | -4.96148 | -45.51665 | 2024-10-24 04:32:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40f79f1b-fe40-30c5-8776-8572fb5e90ed | -4.85893 | -45.74663 | 2024-10-24 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41d2492c-d9b9-357c-b8ac-b73e770bf5ab | -4.84929 | -45.8532 | 2024-10-24 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e11a0a6-0f7d-3219-b26e-8ae16c4cb36f | -4.84873 | -45.85682 | 2024-10-24 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 046bab60-70d9-39fe-9160-97fcafae3b56 | -4.8465 | -45.66975 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 910a45b0-c88e-3da6-8127-8ee9f279108b | -4.84534 | -45.85632 | 2024-10-24 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8bc961b9-22bc-3c27-a767-ba54d55ff8b0 | -4.82439 | -45.63236 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9754e0f2-77a7-3388-be7b-5ab7e6bef7c0 | -4.80174 | -45.68932 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 652b78de-04db-399c-9079-ace9073abb4b | -4.80118 | -45.69298 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1d11188-82b5-3cad-8b68-9bd7a18f7572 | -4.80062 | -45.69664 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| caed8c65-7fc3-3219-a1fe-ebbd60bec701 | -4.79779 | -45.69247 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 26a3e706-674a-3151-a329-01d871f26cdd | -4.79723 | -45.69611 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8e967f0-9d26-342b-af95-8e290ea8e772 | -4.79494 | -45.68832 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50fae8b4-6fa9-3451-b456-1cccb39eb24d | -4.79448 | -45.4839 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ceb2a8f-d856-393d-9174-0b66d1dbbeb1 | -4.79439 | -45.69196 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71012276-c5dc-36f9-b831-73beceb28c5c | -4.79155 | -45.68779 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b6a890c5-b5c1-3ccd-87f2-ff5bfa483129 | -4.79099 | -45.69143 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ba66f81-e5d8-3f58-9da3-11b74b7c1329 | -4.79043 | -45.69507 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d57840f-fade-336a-9e67-574b05b792be | -4.78815 | -45.68726 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6e8d78a1-cd13-3a1a-8d83-e4dc199f4788 | -4.7876 | -45.69091 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d21dab0a-23df-35fc-a54e-92231b02687d | -4.76907 | -45.75903 | 2024-10-24 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd2baf69-5cd1-3eac-960a-71361bce0be9 | -4.76511 | -45.76215 | 2024-10-24 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2809037f-3274-3126-a02c-82e8e276d041 | -4.76173 | -45.76163 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a729cf7-1399-3721-b033-7a16340a9242 | -4.75721 | -45.76837 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2458dfd1-8488-3837-b8d2-74866be7fc21 | -4.75561 | -45.66694 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4e4c249-32c9-3fa5-9921-8953396f9ca1 | -4.75221 | -45.66642 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a67e926-1900-3060-af22-ee923fd9a7d2 | -4.72506 | -45.72961 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1be32908-1906-3c87-9c5e-73de1e54b851 | -4.7245 | -45.73323 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 48e45998-fb4f-3773-82bb-1f77b6bddb09 | -4.72111 | -45.73271 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a1e2a15e-f329-3fc3-99b8-1df54f863b0f | -4.72054 | -45.73634 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 157fcefb-174a-3dec-8757-4e2be70337fb | -4.71716 | -45.7358 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 600235c0-1d18-36fd-b4f4-78c5d0703c6b | -4.7166 | -45.73941 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8b449170-9504-3e4b-993a-22314318e50d | -4.71377 | -45.73524 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1c167b94-81d8-3490-b393-a8cb5d28c3e6 | -4.71321 | -45.73888 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a63d4a18-dd04-3576-b944-766444f85d42 | -4.71038 | -45.7347 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 7cfecbfc-30ad-3554-b64b-1913d48b8372 | -4.70982 | -45.73834 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f9e0433c-fc45-3790-89f9-79ac5eb2fe98 | -4.70927 | -45.74195 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 4d1c9ea3-3a68-39d6-b49d-c02e28541d85 | -4.68632 | -45.86838 | 2024-10-24 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82a40993-477f-3c7a-a6a6-8927f40fdf55 | -4.68168 | -45.80865 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cdbc7bd8-d9e2-3bdf-9198-2f8da6b90943 | -4.6783 | -45.80815 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2a297917-d56b-3a99-b216-42abef878419 | -4.66049 | -45.69031 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 43af9fb0-3fb3-3281-aee4-ff78552088c1 | -4.65767 | -45.68612 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ded72a7-0a1e-3ebc-b5a3-40a93c80a934 | -4.6571 | -45.68977 | 2024-10-24 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 068f123a-3c81-33ca-977b-82959621dd9e | -5.08756 | -44.92665 | 2024-10-24 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f7de6ae-8ddd-353b-beee-8df8a7d12ac0 | -5.08405 | -44.92614 | 2024-10-24 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92fc0b98-26d8-39b4-beb5-9b29b5ea848e | -4.94056 | -44.96526 | 2024-10-24 04:32:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a08c5c2a-b5d3-3471-8f2f-36e22f3c21ab | -4.89174 | -45.33049 | 2024-10-24 04:32:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8637d838-0411-3a94-8082-edb990b978d0 | -4.84974 | -45.03536 | 2024-10-24 04:32:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 63e67395-e4c8-31d9-a675-e0e0bf2ca050 | -4.84915 | -45.03923 | 2024-10-24 04:32:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9618f158-2665-37df-9060-8899ca56c6a8 | -4.84626 | -45.03481 | 2024-10-24 04:32:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a729ea1d-94b8-34ad-b500-9888fa45f89d | -4.84566 | -45.03869 | 2024-10-24 04:32:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46c15593-626b-33da-afcd-683288111a0e | -4.8129 | -45.41046 | 2024-10-24 04:32:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6b04498-87b9-3d53-8dd0-c4066da2c3d1 | -4.74036 | -45.1996 | 2024-10-24 04:32:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ea728b4-1704-37fa-82fa-da2d6f9e978f | -3.92697 | -44.76545 | 2024-10-24 04:32:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1adf40c9-4ef3-3b8e-9982-ed00fef7f66d | -3.81166 | -44.96006 | 2024-10-24 04:32:00 | NOAA-21 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b19185f-bf96-3b3e-99dc-1cf09271bf5e | -3.75149 | -45.19435 | 2024-10-24 04:32:00 | NOAA-21 | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acc38221-6750-39ab-bdeb-90f45a57af95 | -5.55299 | -46.3971 | 2024-10-24 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 233671ad-c74d-33d4-929a-f19f5f20ec65 | -5.54964 | -46.39656 | 2024-10-24 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db57e702-1119-3bfa-a403-bfad4540ec51 | -5.45783 | -46.35337 | 2024-10-24 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14d652b5-c00d-37f8-9401-55c079c73474 | -5.4229 | -46.34091 | 2024-10-24 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 521cda74-36be-37d6-b760-641ad37a6a96 | -5.70686 | -44.99995 | 2024-10-24 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c967bc23-bb44-30ea-8752-9390cdf0693c | -5.70625 | -45.00393 | 2024-10-24 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7e1ca44d-ae2c-3b1d-9c7e-2fd8792749a8 | -5.55765 | -46.19678 | 2024-10-24 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62848332-28c3-3372-a370-e66cc8217dd0 | -5.53586 | -46.27053 | 2024-10-24 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README28.md)
