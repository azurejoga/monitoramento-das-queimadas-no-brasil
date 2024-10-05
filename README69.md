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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4730612-af82-3abc-9a2b-78c0ae6bd63f | -10.29988 | -50.51761 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fe72676e-807d-3072-85d1-93f27e53d397 | -10.29949 | -50.53364 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ace9bc6e-e580-3d3b-b3bd-c59432e06112 | -10.29907 | -50.52209 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0762156f-4361-3af7-bca8-881b6b88808c | -10.29825 | -50.52656 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| efc1c3e9-8554-3721-9982-0108aa1208bc | -10.29744 | -50.53104 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8e6dde7d-6a1a-3df1-8bd9-75a36ebab4e1 | -10.25373 | -47.71004 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04c99ef7-48a5-3832-b227-2bd7ec7c3390 | -10.24998 | -47.70941 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc8788a3-3b24-345d-8c96-2decb24c63c7 | -10.24457 | -52.73567 | 2024-10-05 04:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e2990e5-8109-309c-94d6-7b39877174d2 | -10.24397 | -52.73883 | 2024-10-05 04:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bad8be00-cbe8-3505-b10c-bb296acc4c89 | -10.23936 | -47.72626 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 57c7c78e-7fdf-3b92-8428-c9614b005428 | -10.239 | -47.72864 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d00030e-bf81-30f4-bb89-f051a624f928 | -10.23859 | -47.73078 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d28103a-e31e-3170-a683-95ee4c6d2d0b | -10.23826 | -47.73314 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8670173-6274-3c59-9319-16c43d2f08c5 | -10.23781 | -47.73526 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9828df90-4be9-3dc6-9ef8-6d1a9736b9d2 | -10.23751 | -47.73764 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 55b3321e-04e4-317d-a5b3-973c443b1055 | -10.15585 | -46.34557 | 2024-10-05 04:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fae6e14c-0bf0-34d4-baa2-f001a69a5059 | -10.15234 | -46.34499 | 2024-10-05 04:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a9ab4da-2944-37fe-8184-6bd57442fc61 | -10.15101 | -46.35292 | 2024-10-05 04:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7f6c0ce-b2e4-3c75-a6da-4152a185288b | -10.14047 | -46.35123 | 2024-10-05 04:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0fa42ba5-9400-37b1-b732-2d1fc51e2291 | -10.14016 | -46.35154 | 2024-10-05 04:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3184e6b-9333-386a-8a98-b9c853b92d5e | -10.13665 | -46.35097 | 2024-10-05 04:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79736477-7b0e-38d5-bc72-d4e376bb2213 | -10.12613 | -48.82737 | 2024-10-05 04:14:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9a7657e-1cdb-3fc2-9b8f-a72ab62aa7c1 | -10.12554 | -48.83086 | 2024-10-05 04:14:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26baaf7a-d578-32b6-ab1f-36d5841a3094 | -10.1221 | -48.82676 | 2024-10-05 04:14:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b926447-c166-3809-a321-28edcbc224c8 | -10.12151 | -48.83023 | 2024-10-05 04:14:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6061a1f5-3900-33c7-a714-f50235e2d823 | -10.11061 | -48.82145 | 2024-10-05 04:14:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 134b2669-f168-33b3-8c26-e8e222516d62 | -10.03488 | -48.20822 | 2024-10-05 04:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aa94bd57-dd8d-321c-a80b-eb5986d18071 | -7.37317 | -47.25403 | 2024-10-05 04:14:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bb92d7b7-9707-332b-bb05-5e58f179f0a9 | -7.36937 | -47.2534 | 2024-10-05 04:14:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1e098093-205b-3599-9731-8846e9ee682d | -7.36759 | -49.61032 | 2024-10-05 04:14:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4ec5f62-8d7d-3f07-bd9f-e07de67264db | -7.35996 | -44.72725 | 2024-10-05 04:14:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 975fc8df-845e-34b4-be13-eb5c172e5ee6 | -7.35599 | -44.73035 | 2024-10-05 04:14:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 227db6a2-8886-390d-9af1-8d3176971c24 | -7.3507 | -45.50766 | 2024-10-05 04:14:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea2418c9-fac0-33fe-abc3-941611daf1a0 | -7.34946 | -45.51535 | 2024-10-05 04:14:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 60737ba3-8e3d-3050-a989-e1c152f9a2df | -7.34748 | -46.2076 | 2024-10-05 04:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 03db4c15-712d-3deb-9d3f-cb74442e9766 | -7.34606 | -46.20789 | 2024-10-05 04:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7fd47cb4-b132-31ea-9056-d06e7ffe5adb | -7.34497 | -46.12351 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c068d4a7-d883-36e2-859f-49d68456d268 | -7.34491 | -45.85474 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ff6a302-41e4-3dc0-89ec-3a4067ddb9e2 | -7.30676 | -49.25857 | 2024-10-05 04:14:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 82b6787d-d5dd-3c70-b7c1-8090a451278c | -7.24905 | -48.00702 | 2024-10-05 04:14:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 028be5d2-eb2c-316c-9a74-5f3e1f98e388 | -7.22506 | -44.93897 | 2024-10-05 04:14:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 228f548a-360b-3e79-be4c-1fc2f103928a | -7.19327 | -47.82965 | 2024-10-05 04:14:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ee0bb8a6-e6d3-33a0-9918-667272d79026 | -7.19237 | -47.83489 | 2024-10-05 04:14:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| abfb0da8-0ca1-311d-9de1-e7314cac2f35 | -7.19021 | -47.83291 | 2024-10-05 04:14:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 431de3f9-db00-3fe6-a91f-fa43fa9e283a | -7.1893 | -47.82912 | 2024-10-05 04:14:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2e07c79a-1916-354d-aacf-37191662ecf1 | -7.18843 | -47.83422 | 2024-10-05 04:14:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9683998b-20c4-3278-a391-7638e5058799 | -7.18707 | -47.82729 | 2024-10-05 04:14:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c4f6954b-f59a-3fd5-9fc8-326994578ee3 | -7.18625 | -47.8323 | 2024-10-05 04:14:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8d852154-0155-3285-b469-fe87b7404221 | -7.18542 | -47.83738 | 2024-10-05 04:14:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 27676a44-d549-32f0-8ed2-eb4d6c1058a8 | -7.18534 | -47.82859 | 2024-10-05 04:14:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2fb39f28-bc16-3377-8da3-c9021e851dc6 | -7.18361 | -47.83865 | 2024-10-05 04:14:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 32470c0b-39e0-38e1-86d0-772624960d30 | -7.18263 | -45.05045 | 2024-10-05 04:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79697286-6ac6-31fe-bf1c-0e664b8ae5e9 | -7.18147 | -47.83673 | 2024-10-05 04:14:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d8c98466-22da-3b4d-8d9f-6861e5492e90 | -7.1792 | -45.0499 | 2024-10-05 04:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8edaae81-abc8-3e3a-a1b7-c997cd68891b | -7.16608 | -45.04394 | 2024-10-05 04:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 676d68bf-3a6d-3502-b548-0ea8585a4369 | -7.16325 | -45.03967 | 2024-10-05 04:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df8e3d73-d1bb-3eb0-aa6b-66e17a1d1db7 | -7.16265 | -45.04339 | 2024-10-05 04:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 084d31c2-cc82-3d13-b43b-ea0860350d1f | -6.9997 | -45.73611 | 2024-10-05 04:14:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3654e7f3-6e05-3a99-b43c-99134cf35aab | -6.99904 | -45.74006 | 2024-10-05 04:14:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6740c5d2-9aa1-32bf-aaec-7e1812f42989 | -6.99619 | -45.7366 | 2024-10-05 04:14:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a8b67829-f879-3726-9333-79f54232f155 | -6.99616 | -45.73556 | 2024-10-05 04:14:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6ed0a698-7dc2-3e1e-aa12-68b0d35ae85a | -6.99556 | -45.74056 | 2024-10-05 04:14:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7704a2a5-2127-3b69-89ff-33124db5c23a | -6.99551 | -45.73951 | 2024-10-05 04:14:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9e374f11-fc7b-31c7-8435-13e9e2dc1b4c | -6.99039 | -45.72763 | 2024-10-05 04:14:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 4dde8ecc-3c2a-374a-8cb6-fe4321a8c210 | -6.98976 | -45.73157 | 2024-10-05 04:14:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 7c9c8915-ea48-3da7-827b-0745d9e62777 | -6.98913 | -45.73552 | 2024-10-05 04:14:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dd98836f-650e-3adc-93f0-5fee4fe76f49 | -6.79392 | -47.01614 | 2024-10-05 04:14:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e53f00be-9ca7-3b99-a68e-9842cc096df7 | -6.56534 | -48.36325 | 2024-10-05 04:14:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4877511d-bf46-371a-9f13-7c64570cd892 | -6.45075 | -49.92132 | 2024-10-05 04:14:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ed86ce8-b7e4-3281-b4cb-043ec5cc5b43 | -13.6331 | -51.21135 | 2024-10-05 04:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d8a8ca5c-44b9-31d4-99d7-5e56dc2a55a3 | -13.63207 | -51.21025 | 2024-10-05 04:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ee86fb51-da6e-3598-ba2e-9621ebb49cf7 | -13.63176 | -51.26079 | 2024-10-05 04:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b33a748-d812-3d7a-8adf-8bfe3828b8d5 | -13.63092 | -51.26524 | 2024-10-05 04:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07be93ef-854c-31b7-932f-54292014d3b0 | -13.62872 | -51.26117 | 2024-10-05 04:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 5e5ac6c2-a425-3040-a98c-7771c30ebafd | -13.62792 | -51.26563 | 2024-10-05 04:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c48a6fb5-91f8-3c6e-a71e-d6efce331435 | -13.62733 | -51.25993 | 2024-10-05 04:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a6f4a7cf-c414-3c08-89e3-c1aeef1f293e | -13.62711 | -51.2701 | 2024-10-05 04:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c3a0a5c2-db51-3724-bcf8-30c6d3bda516 | -13.62649 | -51.26439 | 2024-10-05 04:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| fe1c1897-f943-31a8-8119-90127774502a | -13.62565 | -51.26885 | 2024-10-05 04:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a30abbe5-9949-3965-91a1-0af6db95caed | -13.62348 | -51.26476 | 2024-10-05 04:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 7f9e5323-172c-308b-b58f-f6abe843795e | -13.62268 | -51.26923 | 2024-10-05 04:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 41921b80-3ecf-3cc5-8468-3878e08e5199 | -13.62225 | -51.19553 | 2024-10-05 04:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fe25544a-8fcc-3563-8e1e-757a1cec6a1a | -13.62206 | -51.26353 | 2024-10-05 04:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| de3c582b-a889-34e7-a695-d660208b258a | -13.62187 | -51.2737 | 2024-10-05 04:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f392586e-dee2-345d-adeb-d8d201b073e9 | -13.62145 | -51.19994 | 2024-10-05 04:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc297707-a16e-31c3-86ef-3ff63fd6c465 | -13.62122 | -51.26798 | 2024-10-05 04:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 92943f63-0041-3720-8333-270aa733bd0a | -13.62038 | -51.27245 | 2024-10-05 04:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c3204cd3-26a8-358a-b037-321e6323c843 | -13.61985 | -51.25943 | 2024-10-05 04:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc5bc5f1-9836-364a-8fab-277f2f7b6f0b | -13.61905 | -51.26389 | 2024-10-05 04:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9235a9bf-c2b8-3dd3-bbee-7b7e1b250718 | -13.61824 | -51.26836 | 2024-10-05 04:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a35884b5-bb97-3011-beeb-7e19ccb3b325 | -13.61813 | -51.06794 | 2024-10-05 04:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af8eb068-a693-396a-acd0-226e0535cbdb | -13.61763 | -51.26267 | 2024-10-05 04:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 05c8e0f9-5ee8-3f27-9db6-726208dfc5c6 | -13.61679 | -51.26712 | 2024-10-05 04:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71786f89-daf7-3af4-9bd4-82daaff3769f | -13.19864 | -51.18452 | 2024-10-05 04:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d93a8557-3407-3501-807b-1ec84e2f6efe | -13.1916 | -50.63066 | 2024-10-05 04:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c408723-78b0-34c8-9410-2c00cfa18f28 | -13.16415 | -51.20777 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f72cc16b-ddd6-3126-8a72-24218e73ba68 | -13.16333 | -51.21226 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7a0eda09-71e1-325d-bc12-ab110bac59c2 | -13.1597 | -51.2069 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 037e00ec-332b-35b8-b5f4-5a715da501bc | -13.15525 | -51.20603 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38b62ec6-a32d-3e98-a3ee-468f4f91ff86 | -13.15326 | -51.19171 | 2024-10-05 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README70.md)
