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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1190132-b336-3ba3-a247-067efbc0e97e | -4.95272 | -45.55004 | 2024-11-02 05:04:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f4a7dcf-7377-318f-bcf9-1f3fdc11eb44 | -4.89662 | -45.70664 | 2024-11-02 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea1f8b9e-869e-3084-9001-8c80bc54fd0f | -4.89609 | -45.71043 | 2024-11-02 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f3f4557-e7b2-357c-b736-aff604c8b70d | -4.89471 | -45.96059 | 2024-11-02 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37ba1228-10b2-3dae-a3a4-9a28b36c1580 | -4.85806 | -45.78239 | 2024-11-02 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3aa235db-05e8-3462-8041-f75ae7ceb0c9 | -4.85763 | -45.78453 | 2024-11-02 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ea80f9c-4db2-36be-a25e-ce342fd2be57 | -4.85752 | -45.78616 | 2024-11-02 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8450303-3073-3f1c-baf0-3bcc92a0bcf6 | -4.85214 | -45.78345 | 2024-11-02 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fdf144b7-d874-3f30-9ae4-7588adc856bf | -4.85204 | -45.78508 | 2024-11-02 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2639dedf-9d72-3dce-a82b-4a318a963468 | -4.80838 | -45.77508 | 2024-11-02 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5033b5c0-c90c-333d-89d6-0219eddd4e30 | -4.75145 | -45.66083 | 2024-11-02 05:04:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e068f4f3-4d13-3b81-98bb-24d0ed12c934 | -4.72831 | -45.74326 | 2024-11-02 05:04:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa59621a-6120-3c43-85e2-587c7bf34cb5 | -4.72779 | -45.74692 | 2024-11-02 05:04:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02f5edc6-3a85-3f29-8324-9883e16fa5f8 | -4.72284 | -45.74208 | 2024-11-02 05:04:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5eca1ea9-c596-39fe-bd03-7805e1566e7a | -4.72235 | -45.74549 | 2024-11-02 05:04:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec6e643a-5515-3756-87f0-d429e3ad1d23 | -4.68917 | -45.66014 | 2024-11-02 05:04:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4ea798b-a9c5-3409-9f5c-658a81b495a5 | -4.57365 | -45.68127 | 2024-11-02 05:04:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c03f3bfe-d70a-37b8-9172-75895714ed94 | -4.57316 | -45.68474 | 2024-11-02 05:04:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd94b847-f6ec-37d5-87c5-8f1d70786186 | -4.38802 | -45.79689 | 2024-11-02 05:04:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ffb79f0-6966-3bf7-88f8-b5b8b1c8789c | -4.38753 | -45.80025 | 2024-11-02 05:04:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f1cdec6-f2a7-372b-99f7-cc1606802a82 | -4.38208 | -45.79922 | 2024-11-02 05:04:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ad5a4cc-1275-3206-a818-54595ffea04b | -4.20745 | -45.88199 | 2024-11-02 05:04:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 700bcc03-7914-38f7-94cd-ff08e8182431 | -4.20695 | -45.88555 | 2024-11-02 05:04:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dea18d3f-7e36-320a-8653-8c6c92fbd990 | -4.20572 | -45.8827 | 2024-11-02 05:04:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 3073c60c-3440-3276-bf0d-624fcab834f0 | -4.20519 | -45.88628 | 2024-11-02 05:04:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| f73bccec-1d2a-348a-8b41-006548706bb3 | -4.20202 | -45.88115 | 2024-11-02 05:04:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 130d61df-1047-3656-b552-a444b47963b9 | -4.20151 | -45.88475 | 2024-11-02 05:04:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| e408ddc3-b6c9-351a-921d-d187bf75f0ba | -3.71494 | -46.00178 | 2024-11-02 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26f3250b-f460-37e4-825c-7ef5845c8291 | -3.64293 | -45.94693 | 2024-11-02 05:04:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45f03571-4750-3ce6-99db-ca6a88d7225c | -3.64243 | -45.95032 | 2024-11-02 05:04:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d45b7701-f28f-3174-9637-9e63c24b6d04 | -4.89522 | -45.95697 | 2024-11-02 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98e3789e-4b6b-38ff-84b8-cdab937d73c6 | -5.00336 | -46.02953 | 2024-11-02 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4e746b1a-ac79-38d5-b10a-31461ff4f6b8 | -5.00289 | -46.03287 | 2024-11-02 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ec657292-c755-3b67-98db-97b7cc2c6759 | -5.00241 | -46.0362 | 2024-11-02 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 92f15c47-876a-3c51-b5f7-2a2585f67a2e | -6.35442 | -45.9104 | 2024-11-02 05:04:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0d16963e-4ba6-3254-9641-cdc2f1238c41 | -5.44192 | -46.27011 | 2024-11-02 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f783f814-be6a-3b7c-8f22-00aeed9d345e | -5.43918 | -46.26849 | 2024-11-02 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 410ad2fc-d3d2-33a6-a4ce-984d4dd1094c | -5.43703 | -46.26582 | 2024-11-02 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ac43bfd-9b41-3938-974f-70115bd84b14 | -5.43652 | -46.26937 | 2024-11-02 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35122f73-f885-31e6-9249-83b888c61407 | -5.34278 | -45.36086 | 2024-11-02 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0c436fe-1475-3877-81b3-b1d95dc51c99 | -5.34133 | -45.359 | 2024-11-02 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2a858539-0dd2-3865-be86-a9a87751abc0 | -5.3408 | -45.36274 | 2024-11-02 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 104e0504-b5e3-30ca-8ef1-09e6e5380a4e | -5.33704 | -45.36018 | 2024-11-02 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f7f2cf2-5a7c-3a63-91e5-d36151b30d2b | -5.33508 | -45.36196 | 2024-11-02 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc3a5b82-4e69-3fbc-bbcb-c9cd499e472c | -5.19503 | -46.1504 | 2024-11-02 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9d3f9bf7-fd1a-33ce-965b-9c3bf6d84690 | -5.19453 | -46.15395 | 2024-11-02 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5a7e8eec-f708-3876-bd69-36f4dd1489a5 | -5.19063 | -46.18148 | 2024-11-02 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f3f4375e-7e99-3c9b-864e-1b1c6b785117 | -5.19016 | -46.18486 | 2024-11-02 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 92f63ff3-055d-3433-b6e7-3737633938b1 | -5.1686 | -45.3287 | 2024-11-02 05:04:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32875fd1-785a-39ce-9b62-ba6b33561916 | -5.16807 | -45.33253 | 2024-11-02 05:04:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c40597b-0270-32e9-b345-106cb26178aa | -5.1669 | -46.11432 | 2024-11-02 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50173676-7a1c-3b1c-a12b-1afa5254222f | -5.16627 | -46.03881 | 2024-11-02 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5cb792f9-a343-3b4c-81cd-d9ec608af23c | -5.16582 | -46.04203 | 2024-11-02 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55527109-6058-3008-9387-8bd3598b0ff3 | -5.16199 | -46.10985 | 2024-11-02 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 498d868a-f6c1-359e-8a1c-2661c52c0b65 | -5.1615 | -46.1134 | 2024-11-02 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62318dc8-b010-35c1-85b4-28e8bae5909b | -5.16032 | -46.04161 | 2024-11-02 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8be2448-3c3b-3172-97c2-84f678fbc522 | -5.12735 | -46.16068 | 2024-11-02 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 912fd768-4644-3486-a192-9f5efa3b16bb | -5.12522 | -46.15861 | 2024-11-02 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b760cf42-94b1-3cdd-a649-202eb287d0b9 | -5.12474 | -46.1619 | 2024-11-02 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7daebea6-0596-3531-a5fe-ce93984cca19 | -5.12192 | -46.1601 | 2024-11-02 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 447a20bd-73eb-3271-99b0-a88ffec6a8b3 | -5.11657 | -46.02562 | 2024-11-02 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12e11ccf-5083-3ccf-9c38-74c53d21345e | -5.11606 | -46.02918 | 2024-11-02 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8960a2e2-851b-385b-8281-25b03bcd10c4 | -5.11546 | -46.11115 | 2024-11-02 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| daf97352-cd3a-3ff4-a7f8-d6df9c5b8038 | -5.11498 | -46.11449 | 2024-11-02 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a338b77-e018-35f0-864c-dcd053de0686 | -5.1106 | -46.02846 | 2024-11-02 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a2b7842e-f180-36b0-bc2b-656f66f3c9e1 | -7.43582 | -46.62394 | 2024-11-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5ba67f57-abb4-33f9-bc70-d3eb28d2020e | -7.43388 | -46.62171 | 2024-11-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66ddf102-56f8-3501-ba2a-6d916bc0ee36 | -7.43339 | -46.6252 | 2024-11-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cc768a9-a6ef-3477-984c-c251a503f03e | -7.43169 | -46.65537 | 2024-11-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 572e46b0-8983-3764-8191-70b8786c627b | -7.4304 | -46.62325 | 2024-11-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a4569b8-6c06-305e-9ef0-210c518a6c6d | -7.42952 | -46.6531 | 2024-11-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e98c03f-85cf-3fb5-a1e8-945078466533 | -7.42903 | -46.6566 | 2024-11-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f57f2611-86f8-3a44-a7a5-374ba695d85c | -7.42627 | -46.65472 | 2024-11-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a32ebdf-c3b5-3b63-aed9-b4627864895e | -7.12586 | -46.37106 | 2024-11-02 05:04:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fba4bd1e-d544-3c5b-93ef-71c45b4b53fe | -7.12551 | -46.36904 | 2024-11-02 05:04:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab4fcf63-bad3-3f09-ae3e-4bbac440e38a | -7.12503 | -46.37255 | 2024-11-02 05:04:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d61fec14-6fac-36bf-8720-ab6e233b893a | -7.12491 | -46.37841 | 2024-11-02 05:04:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 773bcb11-fd56-38c7-9c23-bdafd9db4aee | -7.12452 | -46.37623 | 2024-11-02 05:04:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00dfd026-9ed6-3984-a385-949a6830104e | -2.07951 | -47.13002 | 2024-11-02 05:04:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a49becee-0895-33e1-94cf-b0884e86802c | -2.07873 | -47.1353 | 2024-11-02 05:04:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4daba1cc-844a-3c08-b98f-0a83a6c13e8b | -2.01554 | -46.831 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 43cefa91-eb4f-3b48-901d-3acf2f9e8a93 | -2.01361 | -46.83028 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 81cb455d-b9ba-3862-8afa-79785163b8f4 | -1.94708 | -47.03684 | 2024-11-02 05:04:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| baa6f556-70a8-3736-83cc-c363e278a56b | -1.59799 | -47.14054 | 2024-11-02 05:04:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 4463bc30-18b3-372f-988a-34475609e731 | -1.46599 | -46.72202 | 2024-11-02 05:04:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 792a741e-1d16-3dd3-9fe6-bdb37cd63786 | -1.46514 | -46.72757 | 2024-11-02 05:04:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 73865f47-0478-372b-a8b9-e521fb75d86f | -1.46106 | -46.72129 | 2024-11-02 05:04:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 8a62f92a-3d83-3e83-a566-4f3c822be6d0 | -2.16301 | -46.38998 | 2024-11-02 05:04:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76973ae7-5ec7-3ee4-b158-22e29230b7d7 | -2.16255 | -46.39303 | 2024-11-02 05:04:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62c4c23b-88fd-3b86-9701-5940dcdf09e2 | -2.15838 | -46.38617 | 2024-11-02 05:04:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42f2e4e5-65d7-312f-bc77-ebc0aaafbcce | -2.15793 | -46.3892 | 2024-11-02 05:04:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f01bd1e-b19c-3b05-8ed2-f941c159b090 | -2.08403 | -46.33783 | 2024-11-02 05:04:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7a8e81e-756e-305c-b1f5-1e6329c1d0b2 | -2.00438 | -46.59024 | 2024-11-02 05:04:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53b247dc-2076-3c88-9326-e7d65f724df6 | -1.80054 | -45.90642 | 2024-11-02 05:04:00 | NOAA-21 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa05d588-e39d-3b7d-a8d7-c62be1a6b5db | -1.22037 | -46.51937 | 2024-11-02 05:04:00 | NOAA-21 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eecec4f2-dee1-3426-898b-12c05ba7fda8 | -1.21994 | -46.52222 | 2024-11-02 05:04:00 | NOAA-21 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d82e5fa-5b4a-3e8e-9b43-8324000acfc3 | -2.82498 | -46.61984 | 2024-11-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c3720fc9-175e-3623-8df1-8425cb93caff | -2.82454 | -46.6228 | 2024-11-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1b952e2e-207f-32c7-93ec-85dc7e1a6d42 | -2.82411 | -46.62576 | 2024-11-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f713c273-19ad-3794-80c4-e16700c6e032 | -2.81991 | -46.61909 | 2024-11-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README57.md)
