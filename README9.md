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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5aa0d8d-90c4-3562-8918-42e483c5ef42 | -5.3182 | -38.00311 | 2025-05-29 04:12:00 | NOAA-20 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| bf740be2-43a8-34ae-98f7-89d7c361599e | -3.04682 | -49.44083 | 2025-05-29 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff291541-7533-3a51-ad04-d88f1072ea7b | -7.54565 | -43.3523 | 2025-05-29 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ac7891ad-5f8f-3c41-92db-60441cf50817 | -7.58202 | -45.95035 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3348356-7618-3322-a376-69df47f3d52a | -7.95014 | -44.85849 | 2025-05-29 04:12:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82d72649-94bd-32bd-be0c-b2fe6bf572a5 | -7.5884 | -45.95543 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| af139a74-23b0-31a4-81e9-04cd7d9f4aca | -7.23642 | -43.09377 | 2025-05-29 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 04bc0cb4-910b-3a1b-a966-be89df5d630e | -6.8076 | -45.36748 | 2025-05-29 04:12:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a59d0a77-34cc-374d-8f6a-020570733bd2 | -6.23767 | -43.37536 | 2025-05-29 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fb76f4cd-58fc-3276-acaf-0e9f4050eeed | -7.23587 | -43.09724 | 2025-05-29 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| cbac53dd-34d0-3f58-a9fa-a4a4957aff20 | -4.48456 | -47.79296 | 2025-05-29 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cedcc82e-d1ba-3480-bc89-c4490b951ce1 | -3.04602 | -49.44578 | 2025-05-29 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| becf1c6b-977c-3322-8658-2dbbc44d7c73 | -7.67705 | -46.099 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0bb15ed7-26c0-38c1-8eab-bac54fa3dc52 | -6.20826 | -43.34554 | 2025-05-29 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27c90f73-f58f-3e03-a16e-f7ecb8b483c3 | -8.74224 | -49.76689 | 2025-05-29 04:12:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9a343841-4919-3bee-bf45-c401e5f09daf | -8.06227 | -47.12227 | 2025-05-29 04:12:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 631a13de-d96f-3030-92b0-81a147c2bb9d | -7.54125 | -43.35871 | 2025-05-29 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 024e7bc4-f6ff-3655-9c9b-c4bf56947533 | -6.53759 | -44.45621 | 2025-05-29 04:12:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 31d06018-0d01-3a78-a4b8-d523a50ec2bd | -4.81563 | -47.31843 | 2025-05-29 04:12:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b7012a6-6451-3dbf-b2d7-732a2b28e2b1 | -7.58577 | -45.86207 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c0b70759-a32a-396a-841c-de9706e3e420 | -7.62308 | -45.74422 | 2025-05-29 04:12:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cff78304-e03e-3dec-8c8d-7a26a9e345d1 | -5.97864 | -43.76528 | 2025-05-29 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ca0047cd-18f2-3c3e-b62f-505449273164 | -7.3528 | -43.30425 | 2025-05-29 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3960e277-9d2a-30fa-a7de-3f60942f6153 | -7.66521 | -45.24926 | 2025-05-29 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3b265f1-8e7e-337b-b86e-4d2cd4555132 | -6.34306 | -43.37435 | 2025-05-29 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94546345-85c3-3d2e-840b-6968f964d97a | -7.07281 | -44.924 | 2025-05-29 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1c75bd5f-7d8a-32f6-b380-f6cc23912b01 | -6.80698 | -45.37128 | 2025-05-29 04:12:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28f9a7d2-0bb0-3a4d-9b71-e04748aab752 | -7.33057 | -43.68093 | 2025-05-29 04:12:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 279c83c9-1d9d-308e-b4a7-d57483c2c555 | -7.07101 | -44.93504 | 2025-05-29 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4ef9d7e5-2913-31ed-9ab7-1a26f8c2b56f | -6.34029 | -43.37036 | 2025-05-29 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 08d426a4-db2a-3405-8232-e6b9544bb948 | -7.17506 | -43.33252 | 2025-05-29 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 008e36dd-08b1-34fa-9112-75b66d28dd94 | -7.57877 | -45.86094 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1ba7aa3-fe49-3ac4-9218-aef708825854 | -7.18626 | -43.11071 | 2025-05-29 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e3561d88-35de-38e0-9c0a-279984d4cba4 | -6.34691 | -43.37141 | 2025-05-29 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7a594c45-a455-3120-bb23-98cdf5dd2bc1 | -6.91023 | -47.85296 | 2025-05-29 04:12:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fae9d4f8-6234-36ac-bb65-3d120847b8a0 | -6.2371 | -43.35753 | 2025-05-29 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0d9679b-5512-3000-a13c-801b0a28554e | -5.96589 | -43.75967 | 2025-05-29 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dab523a0-98ed-3b42-8db5-5cfc4e9e1fc8 | -7.43384 | -45.42001 | 2025-05-29 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f37275f9-9f41-32d4-bbc1-7198adda9bf4 | -6.53702 | -44.45976 | 2025-05-29 04:12:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 58838277-5010-35b1-b85b-b7d2c5225eef | -7.9486 | -44.85818 | 2025-05-29 04:12:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e69f0f3-6870-3ed6-9e20-8713ec0bb442 | -6.23822 | -43.3719 | 2025-05-29 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b341caa3-f80e-3ca8-8ef8-aadb4c53f692 | -8.52168 | -50.02269 | 2025-05-29 04:12:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff3ad1a3-5925-3440-a575-c2b6f5f5f15a | -5.21548 | -43.3091 | 2025-05-29 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 76c713da-cd4f-3549-999c-4390ce06c009 | -5.21493 | -43.31256 | 2025-05-29 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0a1f0024-f4bf-3c65-8ae6-a85044f2db7e | -7.67064 | -46.09385 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 30b955f3-f7d4-393a-9853-cdd1e81c6e7b | -7.66581 | -45.24554 | 2025-05-29 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9bce0ab-c143-34b2-876d-4ae5a5166b83 | -7.58775 | -45.95939 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c2b28cb8-1c18-3fbd-a816-38738a3ef28f | -4.46984 | -41.61282 | 2025-05-29 04:12:00 | NOAA-20 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5e19759c-1afe-3080-ad13-01b002643089 | -8.0128 | -46.15162 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd3aa0cf-1dd8-3676-975d-333cef6f5fca | -7.07161 | -44.93135 | 2025-05-29 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 27483aa1-740b-3bc3-9ec1-f7054780a4b9 | -7.94465 | -44.86125 | 2025-05-29 04:12:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b383570-a272-3700-9604-0c26beff1528 | -7.24194 | -43.10175 | 2025-05-29 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 64f2f0ea-e755-3481-b933-cbe5fa025b5b | -7.61469 | -43.43074 | 2025-05-29 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13255715-b455-35bb-834e-c1588e19b0ba | -7.92085 | -43.70768 | 2025-05-29 04:12:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2fb84fc1-1403-3fe5-8cf8-556b39197bf9 | -6.55992 | -44.48917 | 2025-05-29 04:12:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6677c6b-4e78-35a8-a07a-72b737ece36b | -5.21051 | -43.31898 | 2025-05-29 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 162065c2-d7ce-3c81-981c-31de8beb48bf | -5.23367 | -44.60408 | 2025-05-29 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87bc7191-3e50-3ea4-9329-588531f9e3e2 | -5.10446 | -44.44877 | 2025-05-29 04:12:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5cc8a51d-a492-30e4-b50b-162cc31eb938 | -5.96312 | -43.75564 | 2025-05-29 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ef8034b-f434-34a6-97af-c25319cf9046 | -7.94802 | -44.86178 | 2025-05-29 04:12:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c5cc2ab-21d3-3ef0-a497-bec3e583cce9 | -6.33642 | -43.37326 | 2025-05-29 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8c411a76-105b-3f22-acfa-422a29c63708 | -7.0774 | -44.91722 | 2025-05-29 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cd456328-5169-3bf1-8309-229b3f9d0893 | -7.6713 | -46.08988 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0755aefe-4218-39b0-bb71-438700ae5392 | -7.06821 | -44.93083 | 2025-05-29 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bfeb04fb-f7f4-31a0-bf89-3987ca36a318 | -6.65469 | -43.18591 | 2025-05-29 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5742fd41-2ab4-3bf3-92d0-9948f5af5735 | -8.09953 | -46.28504 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4cfe756f-afac-3afc-a1b4-0d0f8c65278c | -7.62182 | -43.407 | 2025-05-29 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11286b5c-caad-3686-ba6b-603ae2e922c8 | -6.12 | -43.94587 | 2025-05-29 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f6d7f51-9b2e-360b-b3a1-5675d5663ea9 | -8.74657 | -49.76763 | 2025-05-29 04:12:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 26347f29-b1cf-3326-abf6-c01ffe563994 | -7.68058 | -46.09959 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 121d78b1-a033-34a6-947f-256c23fe4831 | -8.7903 | -47.94057 | 2025-05-29 04:12:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 5fb83134-d9c4-3dae-8ef8-daf20ba947bb | -7.9458 | -44.85403 | 2025-05-29 04:12:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6dfb5a1-0a98-3d5b-b147-516c806e6f99 | -7.63219 | -45.93026 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 773bcfb6-b986-3485-bd13-9d8885591e34 | -5.78153 | -43.61629 | 2025-05-29 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d53a63d-0d3a-39a6-ae52-8b4c2f6a614c | -8.00222 | -46.14982 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 11457ee7-d9db-3992-89e2-3c1fc1cffc0a | -6.29899 | -43.65167 | 2025-05-29 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 771c2774-2eb5-3e84-8c0b-d4160dcc8475 | -4.23164 | -48.97184 | 2025-05-29 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f2115df2-1323-3ead-9803-37e7caecaae7 | -4.28893 | -48.27013 | 2025-05-29 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df1a1a21-e5b0-3fb5-93e2-d3b4f9624963 | -7.07841 | -44.93242 | 2025-05-29 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cf60ec78-86b1-3962-8c8e-8d4fd517ae57 | -8.19705 | -49.81137 | 2025-05-29 04:12:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 84350e55-acaf-347e-ba5a-634c61580c9d | -2.65836 | -48.80062 | 2025-05-29 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a80e3b2a-a837-3cd9-949e-49cc2ca36192 | -8.5092 | -50.01601 | 2025-05-29 04:12:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 291d02d5-72ae-3d6f-b491-d7c9c447082f | -7.56766 | -43.32027 | 2025-05-29 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9b54fa0-a5db-35cb-a571-9e8191bfc3cd | -6.22022 | -48.46872 | 2025-05-29 04:12:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00492f67-fd48-3e4c-a8b2-99f64bf1c9b1 | -2.65763 | -48.80505 | 2025-05-29 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 49af15d9-95a0-3cb4-9852-49c5aa62c4ef | -8.78458 | -49.16731 | 2025-05-29 04:12:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3898b5fc-2831-30b9-bb45-bccb7b3d8bc4 | -6.22205 | -43.34416 | 2025-05-29 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 589adbf5-5320-3460-8fd6-f78a9d46524a | -7.25911 | -49.51257 | 2025-05-29 04:12:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 899ca315-801f-315f-898b-49c1b42827b2 | -7.67418 | -46.09442 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| dfc610f0-6414-3842-95bd-0088502ae609 | -6.30231 | -43.65219 | 2025-05-29 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a58de19d-a391-3e58-8b38-af2a2e5e348e | -6.34637 | -43.37487 | 2025-05-29 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f0f8d48-26aa-3a4b-8d23-66e3004256f0 | -7.94917 | -44.85457 | 2025-05-29 04:12:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 933fdd58-c4a4-3771-ace0-026d3f56f48a | -7.68459 | -45.65124 | 2025-05-29 04:12:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dfd07169-58c0-30db-9c4e-4bd6e77c7da5 | -6.8319 | -44.65379 | 2025-05-29 04:12:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cafdba97-ef45-3e87-892a-4b6dbf8076b4 | -6.24208 | -43.36897 | 2025-05-29 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 417931b0-25fa-3c7d-84ac-e0843dfc62cf | -7.18681 | -43.10725 | 2025-05-29 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 84a6d558-bed0-325a-bce7-541e6d0fdf81 | -7.15176 | -43.24367 | 2025-05-29 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 8ee9a606-7040-33eb-adf0-552707850c38 | -8.01709 | -46.2141 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 75399420-6c78-37d1-855c-290d1e10986a | -7.94363 | -49.76181 | 2025-05-29 04:12:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c26d3782-4a22-3381-924e-2cf66dce8d54 | -7.19066 | -43.10431 | 2025-05-29 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |


[Clique aqui para ver as próximas entradas](README10.md)
