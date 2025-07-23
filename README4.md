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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be582f88-e4c0-3ae4-bbb8-1e5003cb4351 | -3.9476 | -41.48589 | 2025-07-23 03:40:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e7f8745c-7df3-345c-a441-565f5b11c1ea | -4.08759 | -46.92461 | 2025-07-23 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0048c34f-5a2a-3cea-9628-0ad12e0239c6 | -4.08819 | -46.92487 | 2025-07-23 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0d0a0c5-67f3-3eae-a797-7901c97230ee | -3.03979 | -47.38496 | 2025-07-23 03:40:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6c628eb6-e47f-3b6e-9735-9dbee3d36a96 | -2.91539 | -48.24081 | 2025-07-23 03:40:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5c228bac-ac0b-3a9d-b6aa-ce46c58f42c3 | -3.03506 | -47.86084 | 2025-07-23 03:40:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 75395c00-af16-35e5-951f-4a6ab8c6b6cd | -4.10216 | -48.20467 | 2025-07-23 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07f61bc2-653e-36a0-86bf-0268c6c06f9a | -4.58534 | -43.31892 | 2025-07-23 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b2c6f54-c487-3d74-b0e7-c5ee4ec07629 | -4.08724 | -46.93021 | 2025-07-23 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80a3ee04-d405-3f45-8241-aa835a9974e5 | -4.25705 | -39.2315 | 2025-07-23 03:40:00 | NOAA-20 | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b684757c-c235-3195-9e38-328fbc8a0ad7 | -4.87322 | -38.2671 | 2025-07-23 03:40:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a15ec589-1616-39be-9b43-74ddf8a61818 | -4.04553 | -42.5149 | 2025-07-23 03:40:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 7d855e62-6064-3e08-a443-d65f8f5df978 | -3.4735 | -39.57007 | 2025-07-23 03:40:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 36163b3e-6478-312c-ac6d-9914911f179a | -3.47593 | -39.57052 | 2025-07-23 03:40:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| b118c498-0ba7-32dc-b282-ed3e65bc8926 | -3.03388 | -47.86775 | 2025-07-23 03:40:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 53af65b2-232b-3011-b467-ff4f9ac2eaf3 | -3.0343 | -47.86274 | 2025-07-23 03:40:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5a050378-70e4-3a1e-b9c1-759f02fd4d79 | -4.52216 | -42.07238 | 2025-07-23 03:40:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 08d62258-6fd3-3612-92da-f303d1d68a40 | -4.25396 | -39.22602 | 2025-07-23 03:40:00 | NOAA-20 | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e5165b01-4b8d-3b6a-aacf-04f2f9f06883 | -3.59022 | -41.65244 | 2025-07-23 03:40:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 84f941eb-4258-3c8f-ab4f-cce3d4f623a4 | -4.5835 | -43.31935 | 2025-07-23 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 823887f9-b9fe-3fed-88d0-732924e86068 | -4.09456 | -46.92642 | 2025-07-23 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02a41246-027b-35a5-84c9-38958d528d9a | -4.08668 | -46.92998 | 2025-07-23 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 33d6cd45-6979-3306-8c37-2d7698c9bcb0 | -3.58562 | -41.65166 | 2025-07-23 03:40:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ec34f267-5667-38dc-afd5-82f79e1dcee0 | -5.56162 | -38.93723 | 2025-07-23 03:40:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 04d9e37a-32af-3916-b923-dd86ae4012cc | -4.87389 | -38.26288 | 2025-07-23 03:40:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8ca7c6a1-a1e7-34a8-bbaf-92504c538bc5 | -3.94308 | -41.48514 | 2025-07-23 03:40:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4bd43279-fbe8-3b6f-b522-1cf93b30050e | -3.12007 | -47.01272 | 2025-07-23 03:40:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6cb4dd8c-e697-3db7-a246-ef3065005fec | -4.04464 | -42.52028 | 2025-07-23 03:40:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| f9dfedec-ac98-3973-87f6-89be601be1f4 | -4.10087 | -48.21196 | 2025-07-23 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49638e47-a23f-3e37-815e-aec1ac430e65 | -5.36215 | -36.89489 | 2025-07-23 03:40:00 | NOAA-20 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 45eaca73-7b6e-3d36-b5ce-702a482be632 | -4.05037 | -42.51571 | 2025-07-23 03:40:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| dc046775-226d-388c-9b54-1950287209dc | -7.7473 | -44.03085 | 2025-07-23 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5edf80e3-1e2d-32ff-9c5f-130edfdc5894 | -10.88211 | -44.36615 | 2025-07-23 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22bce3f8-ce26-34c8-9461-30a7c026bccc | -7.23343 | -44.78342 | 2025-07-23 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d9e6e33-07d4-3542-a875-930dadb61d2f | -10.63845 | -45.2316 | 2025-07-23 03:42:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb587928-0a14-33d1-b3f7-4414bb837a02 | -8.01129 | -37.07149 | 2025-07-23 03:42:00 | NOAA-20 | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 20894662-18a9-38c4-b225-56242507b82f | -7.23218 | -44.79023 | 2025-07-23 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59c462ff-e252-389d-b63e-48359cce0b39 | -6.84796 | -42.7345 | 2025-07-23 03:42:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1f3d9c12-a81e-39c1-a389-a5e52185467a | -10.63785 | -45.23475 | 2025-07-23 03:42:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e77022a5-cd6f-3a59-bceb-c4c35ba0cf9c | -7.76358 | -44.02704 | 2025-07-23 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e551c94-65fe-3c70-a9bc-ace9de77aa49 | -5.5939 | -45.05874 | 2025-07-23 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1ffe2282-da75-3c16-953d-7812c103a3c1 | -8.28746 | -44.96748 | 2025-07-23 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b91146d-28cf-3558-8244-ecca89870666 | -7.14003 | -46.09914 | 2025-07-23 03:42:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| afef64d9-5cc5-344a-927e-3f9e28f6b9e4 | -6.88702 | -45.24937 | 2025-07-23 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9457486-057e-39c1-8bfa-da20b7ab2df3 | -7.75907 | -44.02317 | 2025-07-23 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5981554-0823-323d-8803-4f82f9ed9df8 | -7.75001 | -44.01565 | 2025-07-23 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fffd7234-c934-33ae-989f-ae9b56151d56 | -5.87651 | -42.4085 | 2025-07-23 03:42:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3f0fbf62-77e9-306f-8991-73f0df876b1e | -7.74788 | -44.0276 | 2025-07-23 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 859237b2-94b2-3d0d-a534-5640b4251594 | -5.88117 | -42.40929 | 2025-07-23 03:42:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2696b953-d2d0-3185-9667-c4dc96ce63b8 | -8.28555 | -44.96807 | 2025-07-23 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98d00846-5ddb-350b-95f5-d21d403827ed | -8.01407 | -37.07563 | 2025-07-23 03:42:00 | NOAA-20 | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3d0dcb83-b804-316e-a73b-76cd216ba648 | -7.89132 | -45.56094 | 2025-07-23 03:42:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 790a5a28-519f-3585-8602-571b1b81550c | -9.7428 | -48.5821 | 2025-07-23 03:42:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d9516ab-dd9a-39e4-b019-ed7cb6f12332 | -7.04282 | -45.84838 | 2025-07-23 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 163d609f-bd1b-3ac0-9973-b982b1fee4c0 | -5.11195 | -43.78353 | 2025-07-23 03:42:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2c624d95-54c4-3002-85cf-5173f38a9bef | -7.892 | -45.55722 | 2025-07-23 03:42:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 18c6ab4e-6754-344e-9ca9-934b975c915e | -5.28044 | -44.95026 | 2025-07-23 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60cd52ab-4e34-35d9-a46c-c4bfce215e81 | -6.61191 | -42.34694 | 2025-07-23 03:42:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 88242242-f08c-3fae-bf15-850f470a936f | -10.63266 | -45.23371 | 2025-07-23 03:42:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27fef4c8-8b4c-3035-96d3-c13384256283 | -6.18694 | -44.39572 | 2025-07-23 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c497dd0d-121e-313d-b4b2-134cef65d36f | -10.63725 | -45.2379 | 2025-07-23 03:42:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71977708-24e0-33be-9b8c-920e8e963376 | -9.06846 | -45.06303 | 2025-07-23 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f8233637-0ccd-3291-a7ae-bd9d723cbbf8 | -5.68121 | -42.20039 | 2025-07-23 03:42:00 | NOAA-20 | PRATA DO PIAUÍ | PIAUÍ | Brasil | 2208601 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 6503acbf-92f2-3e47-afa6-100892b95683 | -7.1959 | -45.33038 | 2025-07-23 03:42:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 0236a6ee-6455-3727-a19d-e3f4c68e8b62 | -10.88311 | -44.3606 | 2025-07-23 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dca81769-3a65-3cc5-a8c5-9806e263dd66 | -7.74438 | -44.01806 | 2025-07-23 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3ea72530-4364-3e8c-bc81-1673e95d08e9 | -7.75508 | -44.01638 | 2025-07-23 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 36be872b-e739-3d01-b274-41fca35dd54c | -7.7596 | -44.0202 | 2025-07-23 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e552aad-9d15-3cf6-b0e0-8341b0848e18 | -7.75236 | -44.03164 | 2025-07-23 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58feeb16-f76a-307a-9025-8478134d0f6d | -7.74329 | -44.02414 | 2025-07-23 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d7b547e7-3192-3f2a-bbba-d029f13fbfce | -5.27874 | -44.95008 | 2025-07-23 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08a0c84d-12a4-3a5e-b35c-e7f85f51207e | -6.35832 | -42.61462 | 2025-07-23 03:42:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 227416e9-83e9-3359-925d-61a114c1a4bb | -6.97729 | -42.79129 | 2025-07-23 03:42:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 937c160e-a72b-3903-affd-2c5d67b414b7 | -7.74384 | -44.02107 | 2025-07-23 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 74fd85ff-603f-3103-b7d8-05b8263aaab1 | -7.88714 | -45.55239 | 2025-07-23 03:42:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61cd032e-bb20-39ef-8820-87e8094c0d39 | -8.28616 | -44.96473 | 2025-07-23 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d08ac001-104d-3621-b884-1d036ee2616e | -7.74222 | -42.29417 | 2025-07-23 03:42:00 | NOAA-20 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3f362a40-54e9-3fb3-a322-e9ef494baf72 | -10.64433 | -44.4833 | 2025-07-23 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5fc4eb7-c1c7-39ae-9dfd-86bf6663a152 | -7.04707 | -45.85336 | 2025-07-23 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7960d8e6-5717-3f50-a9e9-2d771d5b60f9 | -7.74842 | -44.02457 | 2025-07-23 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f4eeb92d-b7ac-3589-acb2-37b2a92e39aa | -6.60813 | -42.3415 | 2025-07-23 03:42:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 914238a7-5df1-3817-9924-8ac2061bd052 | -7.23593 | -44.78296 | 2025-07-23 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3fdab30-c20e-3f03-9975-b21c81043f53 | -4.77271 | -45.34008 | 2025-07-23 03:42:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04e249c3-a082-32a7-bc1a-2c38a8622619 | -5.68106 | -43.67097 | 2025-07-23 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6eb37858-4242-3ca3-ab7a-d0b54546cf21 | -10.50805 | -44.88636 | 2025-07-23 03:42:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02ba2889-ec2b-340b-b9b2-602b5a416048 | -10.63326 | -45.23057 | 2025-07-23 03:42:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d9d7b51-d82a-3aae-80fd-8df49c8990c6 | -5.72508 | -44.50776 | 2025-07-23 03:42:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cbc683cb-c72b-373d-ba85-0835011e8311 | -7.04198 | -45.84857 | 2025-07-23 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6637b6a6-21d9-39f1-bbac-2c653161c187 | -7.27145 | -44.36527 | 2025-07-23 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 865cc01d-44cb-3ce5-9a0a-ee1d093bf16f | -5.73173 | -44.5015 | 2025-07-23 03:42:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9557d960-25bc-3fab-af6c-c71a4fe7a8be | -6.18863 | -44.38606 | 2025-07-23 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b024cda0-1eec-3be3-bba7-33128b1118a9 | -6.35919 | -42.60958 | 2025-07-23 03:42:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 98891ada-1eb5-397a-aa05-cb0056e6cb76 | -7.22938 | -44.78884 | 2025-07-23 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c9da81ec-3ed5-3bd1-88a0-cf0fcd105c3e | -7.04777 | -45.84941 | 2025-07-23 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d084976-0f17-3bcd-83f5-e9bd0930c7fb | -7.0239 | -45.85003 | 2025-07-23 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16ed1719-4cf3-3abe-b1d8-cacb8214c18b | -9.05198 | -45.06355 | 2025-07-23 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f0019102-a644-3816-97a0-f68d49e82137 | -7.20072 | -45.33541 | 2025-07-23 03:42:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| be6ab625-981a-3a11-9b27-4f28476623ad | -7.758 | -44.02918 | 2025-07-23 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f39a476b-3159-37d3-88db-63f6e7362fe4 | -9.7439 | -48.57662 | 2025-07-23 03:42:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5778d52-f67e-3d44-b242-d82d7704516b | -6.88774 | -45.24532 | 2025-07-23 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README5.md)
