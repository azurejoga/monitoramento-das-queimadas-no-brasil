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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 265f05eb-18b2-335a-818f-3e47121200c6 | -8.4848 | -44.57942 | 2026-09-15 03:38:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8774c124-70d1-382c-aaab-501a7ed7e30b | -14.20876 | -47.42087 | 2026-09-15 03:38:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 30.3 |
| b2cb7881-2017-3d1e-9976-d22103456680 | -14.20682 | -47.43034 | 2026-09-15 03:38:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| b8bcb1c2-0409-336c-920c-e6da0ec8145e | -7.22124 | -46.13937 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 958ff55e-2468-31cf-bedf-f0476e8da1b3 | -7.22712 | -46.17846 | 2026-09-15 03:38:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f07cae0e-60d8-33ab-87e4-9c02ef2ecd11 | -11.24894 | -43.45248 | 2026-09-15 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe7ee660-2338-3613-b847-30d242dbbb1f | -11.23546 | -43.4686 | 2026-09-15 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8268dc90-332c-3058-9a33-1bfef20733ac | -11.8919 | -43.81944 | 2026-09-15 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e637bd0-52c3-3a97-b862-948df1cc5bad | -8.09407 | -43.7834 | 2026-09-15 03:38:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| dce5f860-e9e1-3ea7-b815-ae931304c603 | -10.57611 | -47.74108 | 2026-09-15 03:38:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 343c9163-504c-3bc1-82f4-6b68a1a19978 | -15.25288 | -40.99091 | 2026-09-15 03:38:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| d4d8934d-b0d8-3112-84fd-205ed301d914 | -11.23096 | -43.46466 | 2026-09-15 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d66a71be-7a45-3749-b988-a55409a5e140 | -13.30839 | -43.71601 | 2026-09-15 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a3ff8a90-d7a8-3d35-90d0-b8b074c0e137 | -12.03192 | -47.8154 | 2026-09-15 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5e07cc17-1728-38fa-99be-c802127da5be | -14.2078 | -47.42552 | 2026-09-15 03:38:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 7be6e6e4-6ac5-39dd-893d-5f6aac02fc87 | -14.20627 | -47.42718 | 2026-09-15 03:38:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 4fad92bb-5679-3482-b40b-892820fcf807 | -10.98111 | -48.33009 | 2026-09-15 03:38:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e8f45fbc-af9a-33c6-912a-251f8b58a8c8 | -7.1082 | -47.47964 | 2026-09-15 03:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1974c3d1-18b5-3446-bc6c-bbbd4ea988b4 | -7.55181 | -46.87082 | 2026-09-15 03:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2b5a5b2b-722a-3cb5-b41b-91b7467da5fe | -13.57522 | -47.90894 | 2026-09-15 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 79c35be0-6ea4-3e5c-b2e8-ec39f099ae99 | -7.23588 | -46.16198 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 05233385-f0ec-33d2-9584-778e64e16294 | -12.85659 | -44.38909 | 2026-09-15 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 17140721-8c45-3b1d-95e6-2e4298fa46af | -11.24109 | -43.46654 | 2026-09-15 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4458c4a2-ea2c-3706-ab56-d536ab953520 | -11.4902 | -45.75048 | 2026-09-15 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 4dd6bbef-f7cc-357d-8131-240abd98919c | -7.23141 | -46.15005 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5f7aac4e-b5c3-3d04-ab24-2030d77131b6 | -10.98281 | -48.32196 | 2026-09-15 03:38:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ab87d02a-1398-33d9-9e2f-9cc7f770586f | -14.16718 | -47.40463 | 2026-09-15 03:38:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fcfbbbf5-5fce-3676-93b6-0ecfed4896ea | -9.4606 | -40.39159 | 2026-09-15 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 32.5 |
| 2e57f06d-5e45-35ab-85a1-d76e6ba72028 | -7.46538 | -46.15195 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 91fce601-267f-3793-a0b9-c2a40e83a43f | -11.81639 | -46.5882 | 2026-09-15 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ab934efa-e07f-37af-b38a-db78da106efb | -11.89071 | -43.82568 | 2026-09-15 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c35787ea-e167-36c3-b71e-53a588bc8e3e | -8.09538 | -43.77597 | 2026-09-15 03:38:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ff34e152-9c43-325a-84be-1d5bfd60ce96 | -9.87646 | -47.77649 | 2026-09-15 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0450f16c-13c2-324f-8b0e-5351cd12f877 | -7.96709 | -43.98262 | 2026-09-15 03:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 76503fb0-8475-3852-ac42-d27831cbb9b6 | -12.49314 | -41.42642 | 2026-09-15 03:38:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| fcd9c914-36a1-394b-b500-2086a293e21f | -14.77016 | -42.94535 | 2026-09-15 03:38:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 25932949-8493-37a7-b49d-7717f8e97e62 | -7.24396 | -46.15977 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| d268f6f8-c348-36a3-bf7e-4df110db0a92 | -11.88498 | -43.82786 | 2026-09-15 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 0b203969-b787-33d0-95e5-957c08fdc21f | -7.21403 | -46.13624 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a6ce9fa1-2f3c-336a-ab42-42a9bc7d562b | -11.49859 | -45.74416 | 2026-09-15 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| a0848037-b900-3b76-8916-563a6319c6db | -12.78428 | -47.56702 | 2026-09-15 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5ef6852-680a-3234-83f1-fce06b17dce9 | -14.20727 | -47.42249 | 2026-09-15 03:38:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 33308fa3-396a-3b69-9701-737afee441bf | -12.49383 | -41.42259 | 2026-09-15 03:38:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| a4b87fb9-3f60-31f3-9daf-1622ca46cd26 | -11.50092 | -45.78792 | 2026-09-15 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38e20151-a9d4-33f2-ae41-76529ba7a30f | -8.09605 | -43.77766 | 2026-09-15 03:38:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a8de62aa-e8a5-3893-a6a8-6704491274f2 | -7.23757 | -46.15838 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bdea8664-6a01-3d02-a6c3-ccea66bcc24c | -7.45995 | -46.14541 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6e4f6aa8-cb69-38f3-9822-6d974e23d6ab | -11.8925 | -43.81633 | 2026-09-15 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 237ebe9a-f3ae-322b-998a-b8874a62cc78 | -10.57728 | -47.73518 | 2026-09-15 03:38:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ffc84b06-7f0e-3db9-9720-93861e7e5377 | -13.56519 | -47.8983 | 2026-09-15 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1bebae5-d86a-3a6e-b92f-b9222a1b9046 | -14.76926 | -42.95019 | 2026-09-15 03:38:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| da814656-be76-3977-a118-13803f417db7 | -7.24095 | -46.17568 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| cec16609-a30b-399a-b092-f3fa258fdb62 | -7.96778 | -43.97888 | 2026-09-15 03:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a86de8b-d61f-385d-9c25-3bfa63511298 | -12.48006 | -41.39992 | 2026-09-15 03:38:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 76785909-4cda-36ae-a740-8f94b55b2a23 | -14.22654 | -47.42249 | 2026-09-15 03:38:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e7fe9afd-999b-3a0c-ab70-80ed5aeaf159 | -8.49049 | -44.58876 | 2026-09-15 03:38:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a7955d0e-2260-38f6-b711-1be2b32a3729 | -7.25034 | -46.16119 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| f3176ef6-1aa1-368f-a718-3809ffda5e23 | -15.25561 | -40.99871 | 2026-09-15 03:38:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 9a131862-7354-3837-81f5-7a49506b52f4 | -8.30222 | -39.52552 | 2026-09-15 03:38:00 | NOAA-21 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 61543772-479e-3294-9334-a7a7bda74db1 | -13.59735 | -47.90419 | 2026-09-15 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b7b9566c-6e83-3835-a8e9-abb60a328e8a | -13.43793 | -43.82521 | 2026-09-15 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb6772a8-4798-3722-b9bc-8a776c6eb9b5 | -10.70102 | -47.50549 | 2026-09-15 03:38:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4671fe6-97bc-37eb-9249-dc7f27739f8b | -7.23396 | -46.17257 | 2026-09-15 03:38:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4131c7ba-ee57-3501-bbb8-8563bffc8e3d | -11.23152 | -43.46164 | 2026-09-15 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd70a9c3-cc5e-3bab-96cd-6fc6182b09a0 | -11.88737 | -43.81539 | 2026-09-15 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 48a908df-edf7-3fd0-ab47-51f0b462c0b0 | -7.45901 | -46.15059 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2e4e2a12-4e7b-329a-a114-a61d2d9866d7 | -11.02295 | -37.07776 | 2026-09-15 03:38:00 | NOAA-21 | ARACAJU | SERGIPE | Brasil | 2800308 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 839b45fd-4377-379b-a708-33bee3d133bb | -9.25795 | -48.54281 | 2026-09-15 03:38:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3f529733-0d98-3d44-935b-33fbea183d97 | -10.80033 | -46.20613 | 2026-09-15 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 220298ca-66a3-3dce-8b11-8cd53ad5b2b3 | -12.12052 | -44.21052 | 2026-09-15 03:38:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d22c9c4-8e54-392a-82d9-1002be55532c | -10.57866 | -47.74528 | 2026-09-15 03:38:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 195e8b8d-fee9-3aa8-84d9-b96b532da6aa | -10.58273 | -47.74268 | 2026-09-15 03:38:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d53119a3-875d-3892-bf27-42bd1b3eb09f | -11.50193 | -45.75248 | 2026-09-15 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8fb126e-3fa4-339c-b222-077eaab6caa0 | -12.1252 | -44.21432 | 2026-09-15 03:38:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1fa0a28a-f713-3f4e-b45c-5e130e86129c | -11.88309 | -43.8264 | 2026-09-15 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c8b0e332-af64-3f31-86ea-6ac46248dac1 | -7.46121 | -46.14705 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 39d326b7-8817-314e-a2a0-ca5bed84e837 | -11.88558 | -43.82474 | 2026-09-15 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 791a200c-d727-3561-b18b-29da9356eac9 | -11.24726 | -43.46149 | 2026-09-15 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bd519843-2b6f-3fe6-8d05-7d2a3d1a5116 | -12.85137 | -44.38808 | 2026-09-15 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| dcab9136-d5b3-3b3a-9485-e96d73f15a63 | -11.81121 | -46.58241 | 2026-09-15 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d4195ff-de12-3586-92d1-2b81bda409cb | -10.70873 | -47.50127 | 2026-09-15 03:38:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb814b26-4582-3d3b-b96e-db5a2888fe3d | -11.88618 | -43.82162 | 2026-09-15 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| bb03c901-f98b-3a32-a023-1e04270f75ac | -7.23296 | -46.17806 | 2026-09-15 03:38:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8cf3f985-c839-32be-ba1d-3a2ab95b0ca5 | -11.49694 | -45.74713 | 2026-09-15 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 30c3598e-8fef-3a26-8360-cded23d94b90 | -11.19159 | -42.82184 | 2026-09-15 03:38:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 7633bb04-97f7-38c3-8576-be5b75315879 | -13.64134 | -47.8854 | 2026-09-15 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc37802d-b977-3343-9c4c-dc3c98f09bf6 | -8.09473 | -43.77967 | 2026-09-15 03:38:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f8f2c34f-44bc-3558-bba5-375b613644df | -7.46632 | -46.14674 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ae5d00bb-0d2c-35f1-b417-bdea201e7eee | -11.97919 | -44.9287 | 2026-09-15 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2da8faab-9353-3422-9b41-55cc15fdd502 | -11.23208 | -43.45864 | 2026-09-15 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1105b3a3-e838-392d-a58f-9d83a4a3d6b5 | -12.85128 | -44.38888 | 2026-09-15 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 1bfa4271-55c7-3fae-a1fa-0c1b1216df7e | -13.57124 | -47.89581 | 2026-09-15 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 602b2e3d-ad73-327a-9558-e1aa344c8a11 | -7.24227 | -46.16337 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 0884f064-bf61-3f9f-a87a-4495a55ec8e6 | -14.039 | -43.29263 | 2026-09-15 03:38:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e9ef2675-a344-3bc0-bc10-8977c109d1c7 | -11.1767 | -42.80431 | 2026-09-15 03:38:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 69a35647-f74b-3bc0-a2bb-ee4ad71b0c93 | -7.23493 | -46.16724 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bfe55e67-840c-38b9-8766-d9162679090e | -14.20027 | -47.42517 | 2026-09-15 03:38:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 1c0f4a53-2eff-3e66-a3ba-ceeda9f531ff | -9.45925 | -40.39471 | 2026-09-15 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 62.7 |
| 0ecccda3-e87c-3776-85d9-3ce349bdc4b6 | -13.55464 | -43.53286 | 2026-09-15 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4eb548f5-f09d-316f-bec8-455b260e4a13 | -8.48639 | -44.57917 | 2026-09-15 03:38:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README20.md)
