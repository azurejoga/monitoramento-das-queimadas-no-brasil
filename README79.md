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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dbb7453e-c55f-3424-9a4d-4834d7c59c3f | -7.5136 | -55.3251 | 2026-08-30 13:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 368.1 |
| ef6d31d0-bd8e-3a90-94d5-33a795815ffa | -7.5323 | -55.3041 | 2026-08-30 13:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 833e979a-2b33-3bc5-8e1d-e3b2ad3b5f2a | -7.2933 | -60.5905 | 2026-08-30 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 7a40bc9e-7655-326e-8a4c-7a75ce9a99f4 | -4.9604 | -55.8424 | 2026-08-30 13:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 274.5 |
| 5c2296b2-322f-3647-800f-79e8ed465d09 | -8.739 | -45.3844 | 2026-08-30 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| c28b62ff-ce49-3a5d-9760-bdd0f8d30598 | -7.3117 | -60.6089 | 2026-08-30 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 279.6 |
| 688963da-6883-3fce-9b9d-67b51fd50083 | -7.6343 | -44.8358 | 2026-08-30 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 384379d7-8ed2-36a2-9948-e5bc4e92e5cf | -8.6156 | -54.7743 | 2026-08-30 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 163.5 |
| 8302bc83-1746-30de-8169-a07240ee3bef | -7.2932 | -60.6096 | 2026-08-30 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 76bd3f5c-2db8-3b47-931b-f33d7942ef4c | -5.4876 | -57.1416 | 2026-08-30 13:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| c845c3fd-0b28-3938-9f7d-3f9d6372f49d | -6.8568 | -59.4757 | 2026-08-30 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 194.8 |
| aa7ee3bf-fd65-3238-b070-a94e9a7f46f8 | -6.8753 | -59.4557 | 2026-08-30 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 9c54233d-3e9c-3c6d-a17c-3d4d57a1fb83 | -7.5137 | -55.3051 | 2026-08-30 13:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 201a083a-e423-316c-b567-5feea8831b11 | -14.1456 | -52.8082 | 2026-08-30 13:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 127.9 |
| b8debb0a-04d8-378f-aa62-1037f276f573 | -13.8749 | -54.1361 | 2026-08-30 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 1e3256de-512c-3c30-a0a9-ec93507f2b9f | -11.2314 | -54.0164 | 2026-08-30 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 133.0 |
| 44ecca26-a80e-3e69-8897-2e1ac802c8d7 | -7.3118 | -60.5897 | 2026-08-30 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 287.8 |
| 816de74a-13a5-3118-8336-e7a17412bccd | -10.1538 | -45.6982 | 2026-08-30 13:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 89ed0a37-95d7-3929-8648-fcc0672af19a | -11.2503 | -54.0146 | 2026-08-30 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 731096d2-622e-32be-8bd3-e47bac2b693d | -8.5969 | -54.7755 | 2026-08-30 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 8225d343-170a-31d6-bd53-71812cbcecd9 | -6.8569 | -59.4564 | 2026-08-30 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 069fccba-d61b-364b-afc6-e8a7041dfb98 | -7.29477 | -60.58469 | 2026-08-30 13:10:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 53f37889-96bb-356c-9c52-dd3b91d35e3c | -8.31115 | -65.27721 | 2026-08-30 13:10:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4ddbfafb-d20f-3aa6-91c1-817938e8efc8 | -6.86836 | -59.48692 | 2026-08-30 13:10:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 204.9 |
| e6a48fd9-bec0-3848-9f45-85f57d224dc8 | -9.00407 | -65.4419 | 2026-08-30 13:10:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 6b1de92c-f393-3ffc-bb45-150343e370d2 | -6.87227 | -59.48098 | 2026-08-30 13:10:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 283.0 |
| 048ffa20-203b-3b29-8df3-e9a289bd5ba2 | -8.47436 | -62.70636 | 2026-08-30 13:10:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 82dd3e0b-00d5-308a-8b8e-7a702d5819f5 | -8.91595 | -66.9473 | 2026-08-30 13:10:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| bdfde031-2500-3db9-b8ca-cb068c760af7 | -7.40123 | -60.57759 | 2026-08-30 13:10:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.4 |
| bf80d4bf-a030-360c-9976-adce3dceaee1 | -9.05814 | -65.42036 | 2026-08-30 13:10:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 9a4e72e4-f11e-34b3-a64a-f3e5e762056c | -7.24258 | -60.62197 | 2026-08-30 13:10:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 03bbdfce-16f5-3ab9-a874-8647181929cb | -8.94868 | -62.38277 | 2026-08-30 13:10:00 | TERRA_M-T | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 2aaf1c14-39b9-3842-8ab3-538d254c725d | -6.87618 | -59.45057 | 2026-08-30 13:10:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.5 |
| e3b62c8a-f86e-34b7-b201-6121716820fd | -9.07309 | -64.24089 | 2026-08-30 13:10:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 28df4b48-e285-357e-a1f7-11f3c1ddd16e | -8.96132 | -62.38436 | 2026-08-30 13:10:00 | TERRA_M-T | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 3108e4bd-f268-3bec-ac0b-b9961a523a81 | -7.32329 | -60.58812 | 2026-08-30 13:10:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 511.1 |
| 087384a5-1fac-3e11-8745-e4c5160e5d9e | -9.04342 | -67.6246 | 2026-08-30 13:10:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| feedf697-0f83-3205-9bf6-fd7eb1378145 | -7.55541 | -61.31409 | 2026-08-30 13:10:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 3bef384d-3c10-3e01-a61d-e7db1b893990 | -8.58387 | -66.95494 | 2026-08-30 13:10:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 81c05b72-8671-3855-a958-4a18d00f759a | -8.58519 | -66.94541 | 2026-08-30 13:10:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 635ff93c-dd79-3f41-a5c8-c1e2d01a3e8e | -8.46579 | -62.7118 | 2026-08-30 13:10:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 141b94a5-e173-3a3c-b449-7c5f4f2ca550 | -8.95884 | -62.40356 | 2026-08-30 13:10:00 | TERRA_M-T | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 27.9 |
| ffa60dcf-4b8b-3d5d-90ad-7697a4711e69 | -8.91464 | -66.95686 | 2026-08-30 13:10:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 46c83434-d9c8-3b61-b580-ba5cb8da581c | -9.02032 | -65.39715 | 2026-08-30 13:10:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| bce5057c-cfbd-31e2-a81b-bc9d800d919e | -7.30903 | -60.58638 | 2026-08-30 13:10:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 43135a85-cab0-3577-83b8-2a39f144698e | -7.56098 | -61.30793 | 2026-08-30 13:10:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 5967cf25-af72-385c-83e6-b31b2ea61f6b | -8.9312 | -67.37168 | 2026-08-30 13:10:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e71fc470-9122-3300-8a4c-99a651952d2f | -6.96999 | -59.04784 | 2026-08-30 13:10:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.8 |
| bd097917-a076-3a21-b320-8bc0ffdb50bb | -8.9325 | -67.3624 | 2026-08-30 13:10:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 76882f9c-90bb-3d30-bb2f-a8ff8fc65cab | -8.31066 | -65.28355 | 2026-08-30 13:10:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5d5a604e-3307-3212-b465-4700f147cf4d | -9.09034 | -65.48315 | 2026-08-30 13:10:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 22c6b5d7-533d-3902-a7c0-969668b01160 | -7.70796 | -61.15473 | 2026-08-30 13:10:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 4ff16ede-6293-3ae4-b824-f038d91e23d6 | -8.15344 | -64.00417 | 2026-08-30 13:10:00 | TERRA_M-T | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| d78312e3-3f23-3dfc-b647-3510b7274398 | -9.16173 | -58.29523 | 2026-08-30 13:10:00 | TERRA_M-T | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 34.9 |
| b02e0d35-7db2-329b-befa-e85714d9b749 | -6.87203 | -59.4566 | 2026-08-30 13:10:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 199.5 |
| 21f2051d-0b08-3d38-a7e4-3564d940d015 | -9.89438 | -60.26492 | 2026-08-30 13:10:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 51eaa656-5c43-3fc5-a18c-9dad5ea25b43 | -9.05967 | -65.4088 | 2026-08-30 13:10:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 22.0 |
| d047693f-1d67-3c24-b732-49bd2379b45b | -10.48997 | -59.59437 | 2026-08-30 13:12:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 2f697699-7933-313d-aed2-3c807913a3f5 | -9.69456 | -65.09078 | 2026-08-30 13:12:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 3eca7a92-991c-318b-94a2-a8ec491aa1ff | -7.95 | -44.31 | 2026-08-30 13:15:00 | MSG-03 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b5e15e37-c9b3-3924-aa62-d1f55e21459c | -7.3118 | -60.5897 | 2026-08-30 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 152.4 |
| 9b4221b0-aff1-350b-80c2-e53ba1984653 | -11.2317 | -53.9958 | 2026-08-30 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 88aefeff-b0d6-35c8-9bc5-392ac06354cf | -11.2503 | -54.0146 | 2026-08-30 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 121.9 |
| e77181f6-c831-3d6b-82a1-0436c139c9f4 | -10.1348 | -45.7006 | 2026-08-30 13:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 7c429e76-a533-3fa3-b3a9-34a83b6e4aa4 | -7.5323 | -55.3041 | 2026-08-30 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 41188e9c-fc0c-34ae-99c7-31f031a33566 | -7.9907 | -46.5177 | 2026-08-30 13:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 19b1f16f-0c20-3d23-a227-fd45c0e02546 | -13.8749 | -54.1361 | 2026-08-30 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 255.9 |
| 7832bfe3-7038-3498-bf5b-316a20363a06 | -14.1649 | -52.8058 | 2026-08-30 13:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 113.5 |
| d8f14d8d-1407-3b50-821c-af27eb831663 | -13.8752 | -54.1153 | 2026-08-30 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 179.5 |
| df0f0447-56dd-39ae-9ed8-76e19a86dc81 | -7.5134 | -55.3452 | 2026-08-30 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| b1132de5-1050-351f-a9e5-69729715a5d5 | -14.1456 | -52.8082 | 2026-08-30 13:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 2df11a9b-5b1f-329c-8234-bf1b9042f9ef | -4.9603 | -55.8622 | 2026-08-30 13:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 128.6 |
| 9ad5ac90-1d5c-38ba-9874-37fd8174016f | -7.0434 | -42.21 | 2026-08-30 13:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 87.4 |
| 3bfdbe42-2e12-3d86-a008-74e9a92d0a7f | -13.856 | -54.1175 | 2026-08-30 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 2f0656c9-37fc-3edc-a648-4bf8e0bbdea9 | -11.2314 | -54.0164 | 2026-08-30 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 135.5 |
| aa52b641-2790-3b05-a964-b0ef728b34be | -6.8613 | -41.6532 | 2026-08-30 13:20:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 159.1 |
| 6d1baaac-c3dc-3849-90d4-6b3f5a6b8945 | -9.8034 | -46.3279 | 2026-08-30 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 3f97a1b2-33d8-39cb-8b41-6ee344271b3f | -6.8799 | -41.6754 | 2026-08-30 13:20:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 107.9 |
| 370eb97f-6a33-392a-a0d5-d2d86d1a7e72 | -10.5596 | -50.4449 | 2026-08-30 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 048c3408-9dfd-3aa7-939b-307d249ce9b9 | -6.861 | -41.6772 | 2026-08-30 13:20:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 259.9 |
| 77a48769-adbc-329b-b4b4-6c1af6874254 | -8.2229 | -54.9412 | 2026-08-30 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 0752f011-58df-3b80-a0f8-81294f9246ad | -11.2485 | -45.0963 | 2026-08-30 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 6fb164e7-90e5-3c62-8736-453b50e9ffdb | -11.2443 | -45.3497 | 2026-08-30 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 370.8 |
| 69dbb4e3-e3e7-3802-917d-d60ac5d33c57 | -8.2227 | -54.9613 | 2026-08-30 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| f61e889f-f6c0-3f82-8d6a-01461f1e75cc | -11.2294 | -45.099 | 2026-08-30 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 243.9 |
| 8b4517c5-d847-3462-bd18-6d5648a4e7dd | -6.8569 | -59.4564 | 2026-08-30 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 127.2 |
| ec14d5a1-ef98-3c5d-8382-3f6cf6e022db | -8.6156 | -54.7743 | 2026-08-30 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 194f3dba-d601-3465-ad8f-455c415443e3 | -7.2933 | -60.5905 | 2026-08-30 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 9a004325-ef1a-335c-a857-3297684d2f37 | -8.1534 | -45.4904 | 2026-08-30 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 01fcd87e-ee1a-36bb-807c-39cf44e6dfb0 | -14.4193 | -52.5625 | 2026-08-30 13:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| a43bbd53-bfe9-3b43-bc33-75830a27f9bd | -7.5137 | -55.3051 | 2026-08-30 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| beb4c5d2-aadd-3d6f-b5fc-efc8f8070950 | -6.0 | -45.0889 | 2026-08-30 13:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 3211fc7b-4bfa-381e-9cd3-85c377f125c2 | -14.4197 | -52.5413 | 2026-08-30 13:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 247.8 |
| e8edc466-91b0-3b48-a902-1625f299d744 | -5.4876 | -57.1416 | 2026-08-30 13:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| c4c1c8f0-e911-3903-b3e2-4fd163e498a1 | -15.4048 | -52.6437 | 2026-08-30 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 97.6 |
| b11a872b-63cf-30ae-9c69-0f4b6aebce27 | -11.2506 | -53.9941 | 2026-08-30 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.7 |
| c52813fd-a871-3a30-bb88-25d8a66c8472 | -10.1538 | -45.6982 | 2026-08-30 13:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 501.2 |
| 1342c37a-c43a-346d-a92e-b6cb57b80d6e | -12.9216 | -45.8812 | 2026-08-30 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 23f1a3a1-4266-3f55-aa52-9287a2ecfa6b | -7.991 | -46.4954 | 2026-08-30 13:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| becc3ac7-2ec0-3173-bafd-37ce76aa005b | -12.3619 | -48.1903 | 2026-08-30 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |


[Clique aqui para ver as próximas entradas](README80.md)
