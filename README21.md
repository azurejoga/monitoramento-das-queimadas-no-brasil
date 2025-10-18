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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de355ef6-de43-3586-922e-2b0627fab0d4 | -11.59464 | -44.06355 | 2025-10-18 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d949864e-8d4f-3bc9-80b7-373340059927 | -10.62208 | -42.30066 | 2025-10-18 04:02:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7741a3a7-405a-3e95-bb98-866e36f30240 | -6.92422 | -44.13698 | 2025-10-18 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5611b674-8946-3a52-a561-fc796b4d1aee | -12.15333 | -45.07637 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 72aec611-b403-35f3-ac0c-47597354de4a | -6.94044 | -43.67616 | 2025-10-18 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7d8a1b7f-b12f-3b4a-b531-d578d87eee39 | -13.73659 | -44.23167 | 2025-10-18 04:02:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d22ea897-cf18-361d-951c-445504872044 | -6.96086 | -45.59345 | 2025-10-18 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a4abf326-64dd-3d5c-a78a-73ebbc15cbaa | -9.0365 | -47.72021 | 2025-10-18 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6860100c-851d-3b5f-9c44-eddac565a0d0 | -6.94117 | -43.68813 | 2025-10-18 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7545f609-525a-3c53-b5b9-e5372b1b2575 | -10.80982 | -44.01764 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5a3e21c1-5403-3744-bd4a-99a0cc3423f7 | -8.19975 | -43.96372 | 2025-10-18 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e38d80f-7e33-3ef7-b85b-f5dcce13e35c | -10.52045 | -43.40106 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad8b9105-8580-3e39-b659-2938b393839f | -7.35309 | -43.85397 | 2025-10-18 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| b781424f-20d2-34cc-8d9b-db0973862d06 | -8.21853 | -46.83258 | 2025-10-18 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 639833da-025f-3536-942a-61611d3cbb37 | -8.09242 | -44.1062 | 2025-10-18 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 12940017-f378-3573-9f15-ccab750024d5 | -7.77003 | -42.48915 | 2025-10-18 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a9cd7b28-41f7-3eed-9561-b21cce006a64 | -10.49128 | -43.42531 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f5dc129d-b4a9-382c-b9b2-00a31008e438 | -9.72108 | -44.57295 | 2025-10-18 04:02:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2eee6844-5b7c-3403-b238-e7582ad7a8e5 | -9.28496 | -43.73435 | 2025-10-18 04:02:00 | NOAA-21 | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8e17d33b-8a65-36a2-845f-dd4e62675a80 | -10.81466 | -43.92965 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 70464352-e2d2-3108-bb1a-5a4f17acf402 | -7.45715 | -46.83962 | 2025-10-18 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cf4da480-34a5-3851-be6d-d69c5ff7d571 | -10.62938 | -42.29813 | 2025-10-18 04:02:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 26105400-abde-3a23-8d60-ef531e26575e | -13.7405 | -43.19 | 2025-10-18 04:02:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c773ca9a-b43c-3786-b506-a680335634e5 | -9.03868 | -46.61455 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0552e429-7ba8-3528-8e5a-c54c5d8e7f7b | -10.14909 | -44.52631 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ec6293cf-710f-3ce9-b79a-0a6701b46013 | -6.93599 | -43.69639 | 2025-10-18 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 560879dd-3f74-305f-978b-622239331806 | -8.16889 | -43.30167 | 2025-10-18 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ae0dcc22-e238-39d4-a8ee-d31d2eb48028 | -7.59276 | -44.9862 | 2025-10-18 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81847482-e745-3b98-8ff0-a1ad7c942f7b | -13.43821 | -47.98782 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb98680d-aa87-3bee-8204-d521281e9980 | -7.58526 | -44.98797 | 2025-10-18 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cd85cb6e-21e8-39d6-8808-34d81daa5141 | -10.70068 | -44.55223 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ffb9d489-3b17-303e-953f-c6e214b122ab | -12.36627 | -44.07934 | 2025-10-18 04:02:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ceb878f2-d5a7-3940-9270-d87d88bd6643 | -7.43718 | -43.75906 | 2025-10-18 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9651949b-6ceb-3d52-a934-7f33382a72f1 | -10.71705 | -44.5397 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2adc0479-d995-31aa-bb38-a184e72c2b34 | -7.95473 | -44.11781 | 2025-10-18 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 73bcb387-c9b9-3f4c-b078-d7e586b11ee1 | -10.58174 | -47.4046 | 2025-10-18 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2c7dbe70-7966-32af-977e-87d62fb4044d | -13.76623 | -48.22654 | 2025-10-18 04:02:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d18e6779-ebab-3f27-ba35-4e8470012d26 | -13.77707 | -48.24181 | 2025-10-18 04:02:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5174735a-79c1-329d-a2a3-610453735b44 | -7.71213 | -47.84763 | 2025-10-18 04:02:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7c1487a7-c50c-3110-a1c4-3e7fe227dd02 | -12.91161 | -48.58642 | 2025-10-18 04:02:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e9d8b663-c050-373d-a3a0-7fc1932c2206 | -7.06721 | -44.73369 | 2025-10-18 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4da5d8f3-2e6b-3fed-bc00-2645467eb68b | -7.45557 | -42.68893 | 2025-10-18 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7b35ddf9-84c5-3936-8ce8-fbc068cc0e53 | -10.51292 | -43.42483 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 953643bf-220b-3759-9264-940c80a1e31a | -11.4856 | -44.02061 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3883cf06-90b2-356f-97c6-f6cbf4ebc71c | -13.45819 | -47.97732 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2b71c2b-2caf-3570-9a27-856525605af7 | -11.35358 | -44.1785 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 694bbc18-68bf-3968-ac02-8c819a9c208f | -12.98338 | -48.45488 | 2025-10-18 04:02:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b54395cb-ccd0-3709-8770-e41a9f04a35d | -10.9344 | -47.56445 | 2025-10-18 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1364593c-07dd-3cf9-9f77-743cfbd0997b | -10.68487 | -45.33152 | 2025-10-18 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71bc32a2-7bc3-3cea-9012-1022fe9cfd4b | -10.42135 | -47.74352 | 2025-10-18 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81cae5a7-d33a-3971-8b1a-2ce2af6ce26e | -10.48012 | -43.42757 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 9407a349-73d0-3e58-841a-0872e7b623b4 | -12.16581 | -45.05903 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63d4305d-053d-3eaf-b429-5adf34be2811 | -8.41626 | -44.72218 | 2025-10-18 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6682ae5a-ef88-3e93-8a55-1615c6b18828 | -10.33625 | -47.76805 | 2025-10-18 04:02:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 539130fa-3603-3ea0-9e65-63c16951d0f0 | -10.17623 | -43.89557 | 2025-10-18 04:02:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1868a534-99af-34cd-a68c-51e6fc1e756a | -10.51078 | -43.41608 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 385657bc-d1fb-3d35-8c14-20672789858f | -10.67989 | -45.32756 | 2025-10-18 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76996026-10ef-3fdc-889a-bbf5e8108661 | -10.42738 | -45.02233 | 2025-10-18 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aaf45236-1dad-3c40-b302-fc91205241de | -13.45723 | -47.93302 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 649fb550-de91-3146-a681-f03266761082 | -13.20095 | -48.32178 | 2025-10-18 04:02:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5834017d-56e7-3262-bdfc-cb34b80bafc8 | -11.68049 | -43.89776 | 2025-10-18 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 841d09fc-9432-3b1c-a11c-c79c295b702a | -7.16576 | -42.66003 | 2025-10-18 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 1a68e661-b5b5-3dd0-b596-4bfcad30ddfd | -10.96336 | -45.46513 | 2025-10-18 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 38e5d13e-c40f-3da9-bad6-ceaf3aa9acf2 | -10.71247 | -44.54978 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3a2b67b-7426-308e-bc8a-e443914fdf15 | -10.96033 | -45.45956 | 2025-10-18 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2b81e433-2801-30fe-a7e0-2d0ba5b392d3 | -8.38694 | -46.22969 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 02924447-536f-38b4-af78-06c3a4108605 | -13.70893 | -40.98548 | 2025-10-18 04:02:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3bbcc661-d3b9-3ffc-b869-19eb8709c29e | -8.71715 | -49.59881 | 2025-10-18 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f8f5f9a-b301-3df5-87ea-def2d473cf08 | -9.25031 | -44.34716 | 2025-10-18 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fa63599a-111d-31a5-b8b1-9c37791bec4f | -10.24546 | -44.05753 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 774ff378-d6d8-3c47-9447-d49f9d2ca5f3 | -7.76942 | -42.49301 | 2025-10-18 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| fcb34001-9abf-362c-851a-98d121cef30f | -10.51629 | -43.40451 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76b2bab3-0930-3380-bcc5-25336300b9aa | -6.83509 | -44.84708 | 2025-10-18 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3aec8749-86ff-318d-bc94-b0f3b9186d85 | -7.58773 | -44.97298 | 2025-10-18 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cac7e94c-b77c-361d-a381-18d3568a4cc4 | -13.48388 | -47.95989 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 94db6a90-a8c9-3bbe-a116-f0a538d8318c | -13.5253 | -48.00826 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1edd41ec-a909-3c6b-917e-cb7acf2ecbd9 | -6.94338 | -43.67496 | 2025-10-18 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dbaeae22-176d-30fa-9aa5-2a5f053f242e | -11.48446 | -44.26863 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3733ca19-2da0-3648-b0be-f226797d4155 | -13.61656 | -43.96672 | 2025-10-18 04:02:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5bfbf1c3-094f-3552-b854-776e65bb97f2 | -11.37015 | -45.2665 | 2025-10-18 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d02b9fe-3c94-3f19-806b-af93834ec1be | -10.9573 | -45.45395 | 2025-10-18 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e461acb8-9e2d-32a0-8cb0-ef1c66b8b53b | -10.10286 | -44.57411 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dffa7b77-b5ed-3c78-b2d7-d27e9da1aac7 | -10.53052 | -49.54848 | 2025-10-18 04:02:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd6b2bb6-81a0-328e-b6c6-a982a4257143 | -7.76434 | -42.48044 | 2025-10-18 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| ee26c548-33b3-3481-ae89-0b3fce32455c | -11.61678 | -44.0843 | 2025-10-18 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 3194b727-f764-3d24-84f9-3540826d0e6d | -6.89644 | -45.4585 | 2025-10-18 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 78ecb1f3-27c3-3e8d-b633-69c8f487f9db | -11.38128 | -44.30024 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9aababf1-28d6-3956-9588-57f9be746abb | -9.64831 | -47.1236 | 2025-10-18 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e46cd492-c892-32df-b22c-70abf9848bdf | -7.30151 | -41.94828 | 2025-10-18 04:02:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 54444eb1-4dd0-3b7c-a631-1dfec560dd38 | -6.94272 | -43.68557 | 2025-10-18 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cef7cf3f-e807-3766-be1e-92acfc20e03e | -8.35864 | -46.21693 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 656936bf-bd78-33a8-a995-04f03624405e | -8.45878 | -44.1666 | 2025-10-18 04:02:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 444184f8-10d0-3b90-b96e-792dd9efb9cd | -11.49629 | -44.1757 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7e6301b-6164-3f26-bc6a-9acc8ed272fa | -6.72937 | -46.27549 | 2025-10-18 04:02:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 822d2cb5-c23e-3757-a335-0312d56493fa | -11.47207 | -44.0141 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7caffda5-c452-3f7c-8c65-0c43918cee27 | -10.50661 | -43.41954 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be091d12-d67a-3a45-8a2d-0c6f2aa112d9 | -10.71921 | -44.54921 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c17c6b15-68bc-30cd-bdc4-b56aa54df4f9 | -12.87126 | -44.8293 | 2025-10-18 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1298473-92df-304e-aff9-ef7df0bfb842 | -12.15979 | -45.07165 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7842a0ac-d71e-3cd6-9556-7971b626b0fb | -10.24032 | -44.04365 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README22.md)
