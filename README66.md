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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81277683-f036-36b0-9390-89e85999918c | -7.52543 | -55.32633 | 2026-08-31 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ba29f4f-bd22-3f2d-98c8-0ee60ecd451c | -7.39998 | -60.59135 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10e07225-1cbd-3135-8c12-4dd4414fe180 | -6.7199 | -60.0126 | 2026-08-31 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42c4e4d2-ac4a-3b9f-8215-e98124c4f289 | -7.29973 | -60.57903 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 800413a6-eeb6-34ac-8c09-7ff100af3ca2 | -7.44301 | -61.4263 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff0e1a0a-8947-3475-a18d-2772ef601d0f | -8.03216 | -61.25626 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0e4fa5d7-9e80-3b8d-941a-2596a39c989e | -9.15607 | -59.5429 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f7046b43-7b85-31b3-a6f8-856c9e9703d5 | -7.30305 | -60.57956 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e2a8be1-1acb-31a1-9044-300afba31ccd | -7.40053 | -60.58788 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| afece7ee-d01e-341e-991d-792d47b352d5 | -7.56551 | -61.31694 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9bb4c59-b053-321f-937d-f4c0233f7498 | -8.61133 | -54.78182 | 2026-08-31 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6dfe3c86-1e6a-3514-9d42-bfebd37c13dc | -9.20922 | -51.57053 | 2026-08-31 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 199af53e-34fc-3329-89ce-4be41a9c4be6 | -6.88229 | -59.40215 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f232eb73-57d9-3414-8e4e-e2e3eb889d94 | -7.3086 | -60.58756 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27e76dd9-85fc-3ecd-a600-bf32709305c8 | -8.26262 | -62.7574 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe7dafdf-2d95-3db7-97cd-eded45c20c36 | -9.20315 | -51.57366 | 2026-08-31 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e7462de-e643-359d-b414-70b939db9613 | -6.80384 | -59.43465 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9407ac9-fa0e-3370-a204-b0d947c80bc9 | -7.3075 | -60.59452 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53c88dd7-6549-307e-ad82-f16ca8acce5f | -7.50998 | -61.38678 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75496aff-d225-363e-9a27-06e9005a452f | -7.22154 | -60.67015 | 2026-08-31 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c326361-7c6d-3125-b6a3-c936fa00ae35 | -9.15153 | -59.50426 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 226e6476-446b-38d3-b663-4533b47d3c0e | -8.63858 | -62.85141 | 2026-08-31 05:36:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3dbc7d7-7e06-325c-8f4d-6912adfbbdfe | -7.52963 | -55.32692 | 2026-08-31 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc16551e-e089-3c01-b82a-2311ff021b80 | -8.85029 | -47.06652 | 2026-08-31 05:36:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8522f697-1000-3bac-b5a9-ae4530ceb600 | -9.16874 | -59.3695 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 842a408f-44ed-379e-a520-78cdb1f0c6c5 | -6.86091 | -59.40621 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88de817c-b679-383e-92ed-505988554f5a | -9.18888 | -51.55314 | 2026-08-31 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d9b9dce-ad96-33ea-9dc0-9dd9f61077ee | -7.69184 | -63.3262 | 2026-08-31 05:36:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 091e9662-d32b-3b80-a39c-8740f1223856 | -7.79029 | -61.57857 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d352f7d-aeae-3e05-b0b1-e7edc2abca73 | -7.39776 | -60.58387 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf22a11e-70b7-3b34-b3e8-fd88e3a833af | -6.89098 | -59.05341 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c354b44a-86e9-3ca2-9a03-86b7848086d9 | -9.58335 | -47.61273 | 2026-08-31 05:36:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0cffa888-dc11-306a-90e2-3a3d33194823 | -9.30519 | -56.80499 | 2026-08-31 05:36:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72080b8f-d8b8-333b-b8f3-4501c76c1451 | -7.22264 | -60.66319 | 2026-08-31 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e634b9ea-4e42-3982-b6fd-1b0c01adb525 | -7.43912 | -61.42927 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6694453e-8ae0-3a47-9ac0-64d5c5110220 | -8.61254 | -54.77314 | 2026-08-31 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 84a9088c-0006-32af-8f3f-d4557707b634 | -7.27854 | -60.65425 | 2026-08-31 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e59c547-e389-34d1-8653-8f05f49ec3b2 | -7.69471 | -63.33066 | 2026-08-31 05:36:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12bf7968-1d51-3016-9d8a-569404a3792e | -7.31028 | -60.59853 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c970f193-bdc9-3318-8d96-f13fb8433d92 | -7.30195 | -60.58651 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 93651b80-a01a-3349-a8e2-10bc4658dafb | -9.15209 | -59.54606 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9ce11204-5a8c-3ee0-a114-1ab75f0c4d74 | -7.46058 | -60.76491 | 2026-08-31 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61aae46e-26ae-3654-8621-1cf615ba5a4f | -7.57824 | -61.34402 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77f42cf8-95ad-3f77-8e7c-0310b57794ca | -7.92095 | -61.33784 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ad2641d7-2cce-3c50-8859-fb1dec4e5776 | -9.01206 | -60.59901 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5efbdafa-ecfe-36da-a0b6-cbd431cbd897 | -7.52851 | -55.33453 | 2026-08-31 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e11f05eb-2316-30f0-8e19-60850d3a2175 | -7.60982 | -61.37407 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 845967d2-0811-31b7-91ea-0ed2cbe59211 | -7.43968 | -61.42576 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05f5519c-683e-3b49-8b97-b5ad36089bab | -7.84514 | -62.31658 | 2026-08-31 05:36:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d1adb280-f90c-357e-a5b4-eb350f92731c | -7.58272 | -61.23037 | 2026-08-31 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ef301d4-76b2-37cf-ab90-fae5ec21edef | -7.30528 | -60.58704 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7fea80c9-0ef3-3092-9c52-84ed301a3295 | -9.30982 | -56.80058 | 2026-08-31 05:36:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c602b214-497c-3fe7-9789-884105864572 | -9.17364 | -59.60988 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 982932ba-5efd-34d9-a91e-9703cecdbbd0 | -7.55885 | -61.31588 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cb57a33-d5d4-3528-9775-df4b6f0ad48c | -8.20746 | -54.95199 | 2026-08-31 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 57943ce7-5ebf-3442-bc9a-a0be20aed26f | -7.21877 | -60.66614 | 2026-08-31 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2c7b061-7254-313b-841c-56503290a040 | -7.31415 | -60.59557 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ea92cce-2df1-305e-95f0-257bcaedbf7a | -7.61315 | -61.3746 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7bce7705-da6c-3f72-ad4f-4240af22d88e | -6.88566 | -59.40269 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30c2a266-da72-392a-8c6a-136b277e1e40 | -7.60705 | -61.37004 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 3fd3eb69-7d69-3c6b-b4a0-2f4dc6f35e82 | -7.52316 | -55.34174 | 2026-08-31 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b6f4101a-d53f-331a-a541-306903d57a01 | -7.51216 | -60.73429 | 2026-08-31 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df7ef71e-5d4c-3dbf-80e5-4f3f916f440d | -9.15495 | -59.50479 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3db6ef1-fc4e-3508-9f4c-97647c59627d | -8.14853 | -63.9998 | 2026-08-31 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5de27e67-3059-3382-869b-fe2a59eef0f9 | -9.16072 | -59.37593 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 051eada9-e089-3c03-ad58-a66cd9b709f0 | -7.40108 | -60.58439 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5c715fb-e9d1-336d-a154-e5062b3a31e3 | -8.09059 | -63.83931 | 2026-08-31 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2306fee8-67ca-3b28-b01d-9fe3946da85d | -7.31635 | -60.58166 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 74b697f8-0c3c-3f48-8391-d5f5bf6ff8fa | -7.57268 | -61.37894 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6578f4f3-8bbd-3743-9180-d074558591fb | -9.14001 | -57.56546 | 2026-08-31 05:36:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf26934f-236c-38ff-bd3f-c195d5686190 | -9.00928 | -60.59497 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 720be089-b0d4-3d08-bf03-ea60fa7f2ab8 | -7.58823 | -61.34563 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 328df497-2f56-35ca-bc81-d958e3ef54b0 | -7.30583 | -60.58356 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 86de4024-813a-3b1e-bbc9-10b479263df9 | -9.40617 | -51.68695 | 2026-08-31 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7238adbb-a9b0-36c9-abbc-94fcb90a5d3e | -7.96015 | -52.44753 | 2026-08-31 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eaf85ec4-d5d9-3886-8957-8840e3449e1f | -7.34183 | -60.59283 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2625ee35-f46f-3225-bac1-8e246853bf37 | -7.5081 | -63.65303 | 2026-08-31 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45687a96-bf12-3a66-8d54-c50ed00d6676 | -10.73428 | -47.971 | 2026-08-31 05:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e3f5c36e-2e6c-33d2-b01b-95a977a008fd | -7.62592 | -55.28888 | 2026-08-31 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| de546551-8d87-3eac-ac06-aeea84a06040 | -6.85868 | -59.42059 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b22f09d8-964f-338c-acda-63b6fc923caa | -7.52738 | -55.34219 | 2026-08-31 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 470a25cd-b3f4-3158-be9f-8e0bdf383dca | -6.9065 | -59.49053 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 420ac33d-9ab4-3c69-90f4-4cd3fe27b1e2 | -7.57438 | -61.30406 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4576048-9f6e-318e-990b-fb36b21c4aba | -7.32799 | -60.5942 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 528dc879-23ff-39d5-a884-3faac50a3f5d | -7.55878 | -61.42329 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1df9c1f6-a739-31d6-b9b4-e4a8aaa46631 | -9.00539 | -60.59797 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19cb96ec-a35d-3bb7-904a-782d0b0acea4 | -9.14981 | -59.53814 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 293b9ccf-d6be-33de-b030-bd4a1784933b | -7.55608 | -61.31186 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a6b3319-52c8-3a26-9802-25e362be3b90 | -7.25804 | -60.63319 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| efcea8d3-5060-3be1-9cf1-f865ef863259 | -7.29918 | -60.58251 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22e270a2-c0b6-3b68-b392-d619f805be95 | -7.58434 | -61.34859 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef2e8bf5-6c2a-332a-94a0-e5a2e6e50acf | -7.61371 | -61.37111 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 829f06d6-ea6b-305d-91f2-d58036de7051 | -7.52794 | -55.33837 | 2026-08-31 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba1825f2-fa8a-3dce-9ba6-ac763704ed45 | -7.44784 | -60.75932 | 2026-08-31 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ad11784-52c6-3cd3-ae58-c9871c50d398 | -8.14278 | -54.97097 | 2026-08-31 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42b0a3fd-fbf8-391f-97f8-492c6893ff6e | -7.6133 | -55.28695 | 2026-08-31 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2269de8c-1401-3dac-901c-88f5a946b8ae | -6.90074 | -63.06247 | 2026-08-31 05:36:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94934b4a-f646-3043-b22d-b91e5ef87b6e | -7.58779 | -57.69256 | 2026-08-31 05:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5fa6846-7295-35b9-8850-131ff4814cdd | -7.56274 | -61.31292 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a24515f5-4ac8-3113-859a-7185a5472468 | -6.86662 | -59.48062 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README67.md)
