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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb9b0478-1abd-3034-a35d-d7b65426ef70 | -6.38441 | -54.98356 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6938d2d-214c-3b01-bee3-daa4a36db289 | -6.339 | -54.75903 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c20336f1-d658-3320-a3ec-01482653c58c | -7.31604 | -46.1481 | 2026-08-24 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f664d26-12af-30c6-bc45-4feeef8e0505 | -6.12094 | -57.83628 | 2026-08-24 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c6de303-5c7e-37a1-b8af-0b3399d893b3 | -3.01438 | -51.05356 | 2026-08-24 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9577cf8-640e-3475-a19b-aae6485adbaf | -3.26858 | -49.53083 | 2026-08-24 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c651a30-a21f-3a6e-8a17-b073b2a9f5f4 | -7.48482 | -45.13524 | 2026-08-24 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bd3195ab-2b3d-3803-bc69-476bd985faf9 | -6.83804 | -52.49969 | 2026-08-24 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 2f56651d-dd98-3019-a9ad-98714228cdc2 | -6.17928 | -53.5345 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a70bff97-a60b-3c8c-ab01-dbff2c8c19de | -6.3396 | -54.75547 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1051f826-1fa1-3418-929d-0996c710cc86 | -5.94994 | -51.96644 | 2026-08-24 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ee187dc-6040-37e8-843f-6fe85b5f4fa8 | -5.00847 | -47.06802 | 2026-08-24 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be73be29-2394-34e6-a413-fab6db55e31d | -7.16979 | -42.74128 | 2026-08-24 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 98376db0-6ab9-3b13-b5f0-9103bdc077a7 | -6.1368 | -57.77522 | 2026-08-24 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c10c10c6-4691-34bf-8a38-4b1eb965797f | -6.83033 | -52.5024 | 2026-08-24 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 81d8c0e6-1284-3eab-999c-f3e58f498efb | -6.18005 | -53.52993 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 493c5907-ab27-3255-ae33-83fd74aee78e | -6.69863 | -52.08675 | 2026-08-24 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e856c2a1-3bd2-3cf1-af17-9a0706dfcb58 | -6.21816 | -55.92573 | 2026-08-24 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a89729c7-b530-3bf0-85ab-5ddc8959fbc8 | -5.06662 | -47.55003 | 2026-08-24 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9b80e78-c905-305b-b610-e27cdebd05b4 | -7.55645 | -45.59911 | 2026-08-24 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 36dd32ea-1fa9-3aef-886c-7e565f04b71e | -7.25668 | -49.92064 | 2026-08-24 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 57d7930c-7f21-3548-88ec-12bf8e2291f2 | -4.25911 | -56.03099 | 2026-08-24 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f67f6895-4e5d-3fb6-b934-03e097066d88 | -6.94713 | -42.69455 | 2026-08-24 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6cab4e4a-937c-3042-8bd4-229220ede50f | -6.14947 | -57.93987 | 2026-08-24 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b207cdd5-f24a-335b-ad77-9bee7f26aa40 | -3.53617 | -48.18343 | 2026-08-24 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 608241de-fa33-365e-a7df-18cb4c7f7b33 | -7.33502 | -43.4221 | 2026-08-24 04:44:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2b8a4fb-180f-3f36-9599-a385aaae3364 | -7.45595 | -46.90861 | 2026-08-24 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0dfeaf4-d71c-373a-91e9-9256010be429 | -7.36828 | -45.80305 | 2026-08-24 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b1adf8aa-e700-3fc3-9483-5f412f709639 | -7.36378 | -45.80713 | 2026-08-24 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8829cb04-25bc-367d-9ccd-95d0f61d6ac7 | -7.55715 | -45.59434 | 2026-08-24 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 85c667e7-b3ce-3434-965a-ee8558805457 | -6.17555 | -53.53099 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8afae4ae-f1fa-3ab1-a233-c1f4b09eff6e | -7.3572 | -45.82513 | 2026-08-24 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6cfc419e-c202-3b50-8bd2-44725f87accc | -6.19739 | -53.51874 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 063e8b05-0476-3927-ac2e-204be283334c | -5.92604 | -50.10577 | 2026-08-24 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c40110a5-f8e3-3dcb-9ee3-f1d4553407e6 | -7.83543 | -47.64734 | 2026-08-24 04:44:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dac53ed8-e23d-3cea-997f-0ff704d2fedc | -6.12647 | -57.83416 | 2026-08-24 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6806844c-275b-3ca2-9e42-a50e09e78c80 | -6.86924 | -45.01451 | 2026-08-24 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a86c84a6-48d6-38a1-be96-3179ae651f2a | -5.47216 | -44.4193 | 2026-08-24 04:44:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f3b0cee-acb0-39f5-a887-daa968117a4a | -4.51586 | -54.83991 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e625ce2-48cc-32a6-aa4e-532f866eb2ff | -6.33495 | -54.75836 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1558bc2-65fb-3bf9-8eb6-6d6812458baa | -7.39493 | -45.98825 | 2026-08-24 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2debcc27-ed0b-3c22-8bbb-3a8fdc685dae | -6.12595 | -57.83714 | 2026-08-24 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb0590f1-d420-3eca-b2aa-67d9cca1f693 | -6.02205 | -50.20647 | 2026-08-24 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba6c7257-f123-364a-9d95-e2105a7c2ee5 | -7.28649 | -45.36408 | 2026-08-24 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d0b91bfc-e78a-310f-8bd3-328b3dda38d3 | -5.87001 | -57.56202 | 2026-08-24 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b5c522a-6bc3-3d86-9dd6-056fede4a580 | -6.38853 | -54.9842 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2386cb0d-44ee-397e-8c0e-be85a40eb3d1 | -6.4291 | -52.75711 | 2026-08-24 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2a69a4e-ac80-3a7e-9951-1b63275a776d | -3.21802 | -49.22919 | 2026-08-24 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 76cdb67c-25bb-3c9b-a690-e1b5d1aa847d | -6.3402 | -54.75191 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 654630e0-8033-3a2c-a5c9-ab34121f4c99 | -6.44022 | -54.97803 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f73675a-bac6-3979-87b7-a12d0bd80784 | -6.3465 | -54.76395 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 196d2139-9ccc-349e-877f-024843fe6f14 | -5.07311 | -49.37828 | 2026-08-24 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 701a9fe1-ea44-3e96-8286-5e2c3f2f794e | -7.1909 | -42.75209 | 2026-08-24 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c93e0a8f-6fbe-3ca0-8a0d-c30fbcd2ab4a | -5.06704 | -49.37379 | 2026-08-24 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 163909a2-da57-3c44-9478-8741ec3dd68f | -7.35171 | -45.81008 | 2026-08-24 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0148f5ae-6dec-3822-b8c4-8b01ca1deb8c | -5.00836 | -56.13603 | 2026-08-24 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32961d33-4eed-300d-b706-633939a6d109 | -3.26582 | -49.52684 | 2026-08-24 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cfa7d5eb-e479-3dd4-bcb8-0d0b17fec0b9 | -7.48504 | -45.12665 | 2026-08-24 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 90369c15-ecec-393b-8955-bac904d60c0a | -14.578 | -53.03525 | 2026-08-24 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1108e029-e16b-3fb8-860a-a40fcb4cf3e7 | -13.0986 | -43.35428 | 2026-08-24 04:46:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9990ce88-892c-3e5f-b7a9-219b2870b73a | -8.37192 | -46.47137 | 2026-08-24 04:46:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a8e1bc9-92ac-3dab-851f-df35254053aa | -19.27675 | -46.67569 | 2026-08-24 04:46:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37326048-9681-3f54-9577-8bbca9fe9be3 | -6.54949 | -58.58799 | 2026-08-24 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 835cb72a-fd4c-3b8f-bd39-81d7350985f1 | -14.78104 | -48.77127 | 2026-08-24 04:46:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b1d9b5b0-53f9-3cfd-94c9-a0a34e90fee3 | -9.0323 | -50.71893 | 2026-08-24 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8ede341-2aae-38c4-a287-3424c1b3f80c | -14.41652 | -51.7866 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1623b8b-c8c0-39c5-a899-b4446a71506d | -9.96662 | -48.33266 | 2026-08-24 04:46:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f60ed570-bfa6-3d94-9df6-dd71f92806f4 | -8.34851 | -49.17558 | 2026-08-24 04:46:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dbca0f34-43c7-344c-a45b-9197db6125c8 | -11.16295 | -54.00497 | 2026-08-24 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cc3469d-6c2b-36b8-a2c4-3b5bcbe8809d | -10.42753 | -50.46853 | 2026-08-24 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63a6c3da-ba11-3508-9217-a2ebec711248 | -12.73772 | -46.46893 | 2026-08-24 04:46:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf4bc629-789b-333d-a87c-99b4a5f74eb7 | -9.03543 | -50.82692 | 2026-08-24 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 396cecce-867e-3b80-83a2-7ccf8bcb44d7 | -12.71682 | -48.39879 | 2026-08-24 04:46:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 27c84ecd-1656-3722-adb8-3cefa7a6e96c | -12.06517 | -50.57069 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e303cbd2-6708-32db-8636-462dba1d7371 | -12.72448 | -48.39579 | 2026-08-24 04:46:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fedb192f-9cb5-3c0f-9e53-b225227c0190 | -12.75298 | -48.3735 | 2026-08-24 04:46:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b709c352-6a60-311a-ac81-a542ac51d296 | -12.11162 | -50.62112 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53d0f432-4b91-35cd-9b3b-d36070d868e3 | -8.81142 | -46.60666 | 2026-08-24 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f97e23c-51e0-31b2-8ad0-4d5f536afcaf | -10.42808 | -50.46503 | 2026-08-24 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67a83127-3ac3-3281-b5c0-6a3091363e54 | -13.42785 | -51.80817 | 2026-08-24 04:46:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3cdbc67-339a-38b8-a367-eeff3cec5e7e | -12.89293 | -48.47803 | 2026-08-24 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68e4f100-f9a8-313f-8142-b9c9a9258cc7 | -6.797 | -59.58705 | 2026-08-24 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2751cb3-8fec-3d0d-a8bb-b5c6b44be944 | -12.07732 | -50.57989 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f97d3bc8-e392-3863-b7a5-edbdbda69444 | -12.10057 | -50.60487 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| f8fa706c-a18b-3cb3-94bc-742920716fcc | -10.79648 | -50.94794 | 2026-08-24 04:46:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 102ec12c-710f-3de1-ae85-7ec87b7ca82b | -15.321 | -49.22134 | 2026-08-24 04:46:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd89303f-529b-351c-ba42-f9dd71ecaf20 | -12.10223 | -50.61599 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc9216d1-0b87-3957-9f47-6cb00db77db8 | -8.57575 | -49.97808 | 2026-08-24 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e4b294b-5319-3a5c-8d2e-78160ad0e6f3 | -12.06185 | -50.57015 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c82ce84-0a3e-33eb-941b-36b70c5de5c3 | -12.73842 | -46.46389 | 2026-08-24 04:46:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d5a4c86a-d2c9-37f2-8f67-e79af8940041 | -9.05156 | -50.76866 | 2026-08-24 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a8c6c3a6-09cc-3feb-b29d-cfcc6cf6e371 | -9.1994 | -49.11526 | 2026-08-24 04:46:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e73a0ef2-3c83-3cc2-9bf2-fba41d808ce4 | -12.10664 | -50.63116 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0b219339-cbc5-3038-a9ee-17cd3d6ef304 | -12.08063 | -50.58042 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97480768-1f4b-374a-9734-e447b9377fd7 | -14.31261 | -51.84235 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6245e215-4e4c-3bcf-a4cf-fd4c25d11392 | -8.09221 | -50.05043 | 2026-08-24 04:46:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5da18876-baa8-362a-9269-6f2022f2a387 | -12.89476 | -48.48995 | 2026-08-24 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da2353e0-b133-3451-a599-f03dd8db3b54 | -6.80595 | -58.6643 | 2026-08-24 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dc8011c7-499f-30da-88d1-586810cf557b | -10.04111 | -46.43911 | 2026-08-24 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 703ebdf9-4506-30b7-b3ac-8f94be900e52 | -9.00938 | -60.42085 | 2026-08-24 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README29.md)
