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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65484e18-354d-3f1a-8d87-7a5998f86cfc | -17.5713 | -46.3505 | 2026-09-26 11:06:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 08b9fab0-b302-35a2-a50a-27901fd86f6e | -14.99536 | -41.53602 | 2026-09-26 11:06:00 | TERRA_M-M | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 46e77b2d-69c5-3a0d-880f-2e48cdbea10f | -13.56013 | -40.6468 | 2026-09-26 11:06:00 | TERRA_M-M | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 84581310-5f3f-3cc6-bc8b-456e86ddd5db | -12.54166 | -42.47181 | 2026-09-26 11:06:00 | TERRA_M-M | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 00c700b8-57c8-335c-ad8e-30faf270fd39 | -13.15592 | -42.35297 | 2026-09-26 11:06:00 | TERRA_M-M | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 43d0f1bd-7c53-3e37-b6b8-b9f5d2f7d23c | -12.68982 | -42.77295 | 2026-09-26 11:06:00 | TERRA_M-M | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| e917c141-9b5c-3a6e-8ec0-3bb105fcc5dc | -12.32183 | -40.22195 | 2026-09-26 11:06:00 | TERRA_M-M | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 9cd95839-0352-31f1-b647-7d3f2ed79143 | -13.67408 | -44.26925 | 2026-09-26 11:06:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 70893238-b923-369a-b79e-c75d71b6c34a | -13.6728 | -44.25795 | 2026-09-26 11:06:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 2d5c8f15-f7f3-3aec-ad7e-3e9635751788 | -14.8635 | -41.06441 | 2026-09-26 11:06:00 | TERRA_M-M | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| faf07c11-413e-3031-87da-77bc391d8383 | -21.54412 | -41.27975 | 2026-09-26 11:08:00 | TERRA_M-M | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 718d7fba-d53c-303d-9639-6b0e769b5eaf | -17.5639 | -46.3458 | 2026-09-26 11:10:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 176.0 |
| 97380aa2-bfd0-33fd-a3c5-dab32c2b74ea | -17.5639 | -46.3458 | 2026-09-26 11:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 119.6 |
| bf79e41c-34ba-3e5d-b863-fd4bcbebbe19 | -14.2223 | -48.4975 | 2026-09-26 11:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 109.6 |
| b988fe4e-1b88-3df5-a382-f93f78b25343 | -17.5439 | -46.35 | 2026-09-26 11:30:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 041fcb9f-7599-3adf-9775-4f685826c069 | -17.5639 | -46.3458 | 2026-09-26 11:30:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 8cfe7cdc-b1b1-35b3-9714-ccbf0800e077 | -12.2633 | -50.7463 | 2026-09-26 11:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 5f5dc9f5-0d43-3c3a-81cc-71eb5012ceab | -14.2223 | -48.4975 | 2026-09-26 11:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 105.6 |
| ac819e4c-4f82-3824-9b64-84d6ee265d2e | -8.3397 | -44.1658 | 2026-09-26 11:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 116.5 |
| fec77a3e-64cb-3b92-9cc4-dac48a060af5 | -14.2223 | -48.4975 | 2026-09-26 11:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 96.8 |
| f18364b8-e2f5-36d1-8faf-528a807970d5 | -8.34 | -44.1427 | 2026-09-26 11:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 8ad03717-706b-3cee-be8d-246194ad5e48 | -17.5639 | -46.3458 | 2026-09-26 11:50:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 281.4 |
| fae2c8cd-bc90-3ef2-903b-d367550c6430 | -17.5439 | -46.35 | 2026-09-26 11:50:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 110.4 |
| cb12c6fb-af04-34f7-8c47-0b9426a08aed | -8.34 | -44.1427 | 2026-09-26 11:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 254.9 |
| f85d96be-6723-326e-b52f-c2cec238fe1c | -14.2223 | -48.4975 | 2026-09-26 11:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 105.2 |
| b0fbec8b-ae8d-3dec-a55c-eb6f04805526 | -8.3397 | -44.1658 | 2026-09-26 11:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 212.1 |
| f2fcfe13-7332-3903-9460-b6f83eb755e5 | -8.34 | -44.1427 | 2026-09-26 12:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 318.5 |
| 104fc719-0e20-329b-93de-3747234f1f1c | -17.5639 | -46.3458 | 2026-09-26 12:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 331.2 |
| 4249bd0b-237f-3781-9ec0-4b7f2d91a16a | -16.5732 | -43.9798 | 2026-09-26 12:00:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 110.5 |
| e2de28dd-cda9-3e76-bc24-cd0b15464b04 | -17.5439 | -46.35 | 2026-09-26 12:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 118.1 |
| e14df120-ab5f-3245-a712-d78f2995ad1c | -14.2223 | -48.4975 | 2026-09-26 12:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 4d8b6b3c-7b97-3b41-a39a-f571ecc8280f | -8.3397 | -44.1658 | 2026-09-26 12:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 375.7 |
| 4f74ae2d-9517-37bd-bb52-3341405a8352 | -16.5732 | -43.9798 | 2026-09-26 12:10:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 117.0 |
| e0a609b0-e9df-355c-bebc-54a976b80fff | -17.5639 | -46.3458 | 2026-09-26 12:10:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 2e36b73b-0e8c-39d9-b133-816637412f5c | -8.34 | -44.1427 | 2026-09-26 12:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 448.5 |
| e22f4da1-330c-30ae-bbdf-d81d5b774606 | -12.9457 | -51.0695 | 2026-09-26 12:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| f03b33ca-9bec-3e47-a5c3-97d38e972045 | -7.2758 | -43.2975 | 2026-09-26 12:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 10e0db18-c9c1-3a78-b5da-e5bac73ccb32 | -14.2223 | -48.4975 | 2026-09-26 12:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 223ef084-8508-3443-84de-05feb23e1d8e | -8.3397 | -44.1658 | 2026-09-26 12:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 545.9 |
| 14d211cb-350d-318d-9116-5e98992352d6 | -8.36 | -44.16 | 2026-09-26 12:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 54801f88-7ae0-3305-bb20-d61fad4c4e83 | -8.33 | -44.15 | 2026-09-26 12:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3de6be00-741d-3495-9d9c-3132800be6d1 | -8.34 | -44.1427 | 2026-09-26 12:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 447.7 |
| 16e62298-139d-330c-9ef4-ffec1f3191cc | -7.3656 | -42.0819 | 2026-09-26 12:20:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 83.2 |
| 832d1356-f2c5-3c14-98f5-89ff931e4f79 | -7.2758 | -43.2975 | 2026-09-26 12:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| aafb4b64-aca4-30f9-8bd4-f1e48954babd | -14.2223 | -48.4975 | 2026-09-26 12:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 14b7205a-c04b-37a7-969c-d17a81369b77 | -12.2508 | -50.3189 | 2026-09-26 12:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.2 |
| b2ced196-aeb0-3453-956e-39ecaf017d89 | -6.8408 | -43.5021 | 2026-09-26 12:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 452bb790-2cd3-387b-8340-a06e935ed8bb | -16.5732 | -43.9798 | 2026-09-26 12:20:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 98.6 |
| fc9b3db3-abf6-37d2-9f17-3b5cbc8be1be | -12.0803 | -50.2535 | 2026-09-26 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 291a8b5f-181f-3d25-aab3-ada0d402c672 | -7.2758 | -43.2975 | 2026-09-26 12:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 0f73cd23-12d3-38ff-bb9f-19b865a90022 | -12.2699 | -50.3166 | 2026-09-26 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 45ec92a6-a98d-3f18-af77-fac52c2be416 | -8.34 | -44.1427 | 2026-09-26 12:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 352.6 |
| ffaf8e5e-4cc7-3e7c-beea-214c45a4c939 | -14.2223 | -48.4975 | 2026-09-26 12:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 6e28c76d-f6ff-3df3-8a0d-56d499664206 | -12.0994 | -50.2512 | 2026-09-26 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| b0e8f304-ff01-3ef9-8fa0-b7e7a1e18005 | -12.0806 | -50.232 | 2026-09-26 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| e60eceae-0cc1-3662-8b00-1a45be90280a | -16.5732 | -43.9798 | 2026-09-26 12:30:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 2add16d5-aed7-3770-8b41-d65410bfa33d | -12.9457 | -51.0695 | 2026-09-26 12:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| c56b495a-9764-3653-94d7-d5a0e3425479 | -12.2508 | -50.3189 | 2026-09-26 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 1788a6b8-5ef8-3620-9fa7-8f51ddf3f80f | -7.3656 | -42.0819 | 2026-09-26 12:30:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 100.3 |
| df34281c-6754-3ad1-bcc4-15f4fcdcaacf | -12.7514 | -47.8257 | 2026-09-26 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 104a8282-abc7-3ebc-abf2-da210a4c3cde | -12.0997 | -50.2297 | 2026-09-26 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 342c4897-e6a8-3206-87d6-5ad6f13fd0e7 | -14.2219 | -48.5198 | 2026-09-26 12:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 79.3 |
| cb00bffe-e6a9-3de1-8eda-a7766acbdae6 | -7.2758 | -43.2975 | 2026-09-26 12:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 97.3 |
| b58d6933-49f0-3da6-a16e-c90f29ea715b | -12.9457 | -51.0695 | 2026-09-26 12:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 2ed707a0-d16c-389c-9790-e1c3169dd01d | -12.0806 | -50.232 | 2026-09-26 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| d01af3d6-d2a7-32ae-8418-591262f6ca10 | -6.2587 | -41.6377 | 2026-09-26 12:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |
| b7a9d273-6aa1-3413-b0d5-bf243f41ac72 | -11.9596 | -50.6751 | 2026-09-26 12:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 98.3 |
| bc5591a6-bda0-3e15-bcd2-032565e0175e | -12.0803 | -50.2535 | 2026-09-26 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| d93e3ac0-cd45-3f40-9475-f68d606c9640 | -11.7837 | -50.9939 | 2026-09-26 12:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| d3ceb629-c1d4-3840-91bf-b630d8085032 | -14.2223 | -48.4975 | 2026-09-26 12:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 41aa698b-0c48-3a7d-b9ff-06aa24d025a1 | -12.2508 | -50.3189 | 2026-09-26 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| e317b805-3756-3131-abeb-de6cae974bc2 | 4.41259 | -60.15886 | 2026-09-26 12:40:00 | TERRA_M-T | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0ff81d94-21c1-3bf2-aa22-ffe7ece79146 | 1.59343 | -56.06286 | 2026-09-26 12:40:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| a41bc6ef-ad7e-34a3-9801-081efa287cce | 1.60036 | -56.03445 | 2026-09-26 12:40:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 9970e113-7771-332f-833c-edf5bd21a0f5 | 1.64064 | -55.98095 | 2026-09-26 12:40:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 054a6137-23e5-341f-b511-94f9c0af2913 | 1.63866 | -55.96737 | 2026-09-26 12:40:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 9ac00c06-bc82-3dd7-824a-dfa7d65c8c4a | 1.64751 | -55.95223 | 2026-09-26 12:40:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 7e9f599b-f6f0-3d91-9fee-753ecac224ba | 1.12544 | -51.176 | 2026-09-26 12:40:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 8d32c686-766f-3b8b-b622-d7961c8865f7 | 1.13337 | -51.16843 | 2026-09-26 12:40:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 5ad96cf2-5284-34d2-bd99-79bf38b3a4da | 1.64949 | -55.96588 | 2026-09-26 12:40:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| d77204d6-57f5-3ef9-8108-609e8c18a862 | -2.90213 | -54.0957 | 2026-09-26 12:42:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 26bfaf45-9a8b-3a3c-aec1-e18e10db975f | -2.91946 | -52.03545 | 2026-09-26 12:42:00 | TERRA_M-T | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| d689bf8e-5391-3f84-a427-32b808746994 | -1.13855 | -54.08101 | 2026-09-26 12:42:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 25b86b17-241b-3fb0-9487-0051a1abca13 | -6.86902 | -59.88357 | 2026-09-26 12:42:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 013534f7-88d9-379c-a86c-4b1ff74425dd | -1.13914 | -54.09701 | 2026-09-26 12:42:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 365b5450-4f6d-3519-9ed8-fe2c0c6fcfe7 | -1.14219 | -54.07581 | 2026-09-26 12:42:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 977dda5d-4add-3e74-a13a-e2d51e5912c9 | -3.83727 | -55.91045 | 2026-09-26 12:42:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 25ed34c5-451f-3057-aefc-1af5e51450e6 | -1.82455 | -53.38333 | 2026-09-26 12:42:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 53dd90ff-6df6-34ec-a81d-331736279f9c | -2.0652 | -56.87243 | 2026-09-26 12:42:00 | TERRA_M-T | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| b920c4b3-4d52-35ed-9747-7f9709a68ade | -6.31869 | -62.68121 | 2026-09-26 12:42:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0be983ed-1105-3958-afe7-c3dc6fe182e5 | -1.21731 | -54.55681 | 2026-09-26 12:42:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 382dcbf3-6837-3a79-a916-d059f1f23aa4 | -5.06966 | -56.06496 | 2026-09-26 12:42:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| e0d420fc-853c-3047-a34f-fdce4c7a5060 | -11.65137 | -54.05084 | 2026-09-26 12:44:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 67118f6e-1270-38a2-8005-4617f5df4f73 | -11.76902 | -54.32989 | 2026-09-26 12:44:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 31.6 |
| f7963032-5acb-355c-b45f-9163985d3336 | -12.94874 | -57.2445 | 2026-09-26 12:44:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 23.7 |
| f067f237-fbcb-38b2-b70e-e9e3d98066d5 | -9.93288 | -60.7215 | 2026-09-26 12:44:00 | TERRA_M-T | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4c33ea89-5283-3974-a826-d3dcdf838d7d | -12.17204 | -56.53426 | 2026-09-26 12:44:00 | TERRA_M-T | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 317a3467-27c5-37cb-805b-384b1f7f83a0 | -9.96376 | -52.39217 | 2026-09-26 12:44:00 | TERRA_M-T | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 24.7 |
| ebf61563-7276-36cc-93d6-faf4d3099949 | -11.12478 | -53.99535 | 2026-09-26 12:44:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| f9ceef81-c91c-36ac-9b7c-de84e628df6c | -12.13749 | -54.67456 | 2026-09-26 12:44:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 30.8 |


[Clique aqui para ver as próximas entradas](README32.md)
