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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 894fd46a-d8df-3cce-b3a6-63edd0d573f9 | -7.20477 | -60.61543 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a009aa14-3ec9-3a94-bb3f-cc80ffec6ad0 | -7.22047 | -60.62553 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80ba6216-8db1-3edf-8917-72cfc38c1ffc | -9.16588 | -59.40247 | 2026-08-25 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1540a0ba-7781-383b-acac-c679acc68541 | -8.56849 | -63.02315 | 2026-08-25 06:08:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3f528f67-1e30-3a84-9bfe-d9a8d4d337e7 | -7.53892 | -61.298 | 2026-08-25 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cece90b1-4a9c-32db-94b2-5c022548afb5 | -7.21035 | -60.61623 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| e5de8258-dafc-3b41-bffa-31917303dea9 | -7.63778 | -63.38532 | 2026-08-25 06:08:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 934c85da-552b-318a-8aa9-b95f1c8d28e8 | -6.99628 | -59.23822 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 26a6998f-4fd0-3015-aa90-9c8d90c99bff | -7.53638 | -61.3565 | 2026-08-25 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03bb38ec-2384-35cb-a972-14e7033f45b1 | -6.95531 | -59.07913 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35698c34-b2b9-388d-80b9-d259621bfaa1 | -7.31957 | -64.69669 | 2026-08-25 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| eba408c3-f33a-3d35-be21-5b623e039276 | -7.01439 | -59.249 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a83d741d-97de-33ce-ab9d-3f6ef0b8e3ca | -8.81488 | -62.33676 | 2026-08-25 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b085f5a2-a7ee-3f59-8f6e-93bcae182989 | -8.80675 | -62.32023 | 2026-08-25 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1fa97f3-c080-3b85-9ee4-8a7d85f0bf4a | -7.00779 | -59.24483 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fd42cec0-0645-3b14-b561-ce5cc7cfdb29 | -8.81446 | -62.33981 | 2026-08-25 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23433f91-391d-3bd2-8510-63bc46f4df68 | -7.54573 | -61.36773 | 2026-08-25 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9314fcc8-fb39-340b-bdfc-c89e22432044 | -6.91229 | -60.06977 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34611d1f-1bec-31de-bc1b-1cb71a8f0077 | -7.6357 | -63.387 | 2026-08-25 06:08:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e649c918-04b3-3245-94a2-286d23a9d6b4 | -8.80716 | -62.31719 | 2026-08-25 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4a2e107-d1d4-34a7-a791-5e66a97c9ea6 | -7.0205 | -59.24976 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e45fa283-e266-3fc0-abfd-6091390e82c9 | -7.00587 | -59.25878 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f42a20f2-1eaa-3d45-9070-22d2352775b3 | -7.01499 | -59.24441 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| eae75b39-2db8-3796-a18a-33e652d7e1c9 | -7.53683 | -61.35321 | 2026-08-25 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3a0bb539-1e12-3cfa-a316-5b8953e87e6b | -6.99436 | -59.25232 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 530c34f5-8b38-3f6e-8c29-cea3668c4fdb | -7.0187 | -59.25571 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3497c6c0-53bc-3f8b-bac8-84e0bd5b6e98 | -7.21087 | -60.61242 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d170b759-962b-37b6-9e87-764c2b97d4c1 | -7.54527 | -61.37105 | 2026-08-25 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c9266a82-3ec1-3398-9d31-cb8ca0b86fbb | -6.96761 | -59.08085 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ba700b1-5cd0-38f7-b0f2-ef085dc477d0 | -7.00042 | -59.25332 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| a3fe4d72-7195-3f73-9346-35eb95ef4fde | -6.99566 | -59.24277 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 269a2afd-0f74-3c2c-b20c-c534c73254b7 | -6.91807 | -60.07048 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a210120d-c4e9-3ac6-941a-96234a0e9ebb | -7.01989 | -59.25438 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91e4f2e3-6338-372c-92c0-226115f045c3 | -6.96149 | -59.08289 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffd66758-b83b-370e-bb78-baa8494831a2 | -9.19991 | -59.57794 | 2026-08-25 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e1bb58e-bf66-3739-af50-eec574cfad75 | -7.20983 | -60.62008 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc70779b-97e4-3801-9553-2c2330209c25 | -8.66294 | -62.84277 | 2026-08-25 06:08:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 86d3e13c-8c7f-3d0f-aeb5-55261e925e6f | -6.98959 | -59.24183 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1aa547a0-1831-318f-88e4-ac7173fd68ed | -7.54038 | -61.36705 | 2026-08-25 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8f775180-d245-38ba-8a6e-821c57a10ec5 | -7.0126 | -59.25492 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d02f468-11cf-3dd9-b3f9-60dab1971038 | -7.0065 | -59.25421 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d2edb55-01cc-3d53-af88-913f15e5303f | -9.20053 | -59.57317 | 2026-08-25 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 501e7501-633c-3450-bbb1-0605bdd0424f | -7.01386 | -59.2458 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ae786622-16b8-3bb3-894d-4605ef7bf0c7 | -6.98828 | -59.25139 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 75d5105b-604a-33e9-b822-d8fde655b24e | -6.99371 | -59.25708 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| c36633cc-6378-374d-a191-2c6159eefd97 | -6.96083 | -59.08468 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a449571e-ae04-3fb8-96b1-60ef7a5b5073 | -7.32381 | -64.6973 | 2026-08-25 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a5c5992-024a-3619-abf5-fb55d81f3954 | -6.96764 | -59.08374 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc34f59f-c78c-3fd1-8610-3c4bd905bcd3 | -6.99915 | -59.26258 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 3ef43f58-8d91-3dc0-8f4b-30141dcefeb3 | -8.56776 | -63.02849 | 2026-08-25 06:08:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db77d674-0142-3242-8a92-5bcc1c949b61 | -7.0138 | -59.25356 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eef9bb1e-5e27-3400-85e5-dac1ec010be2 | -7.00108 | -59.24848 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 8d2194ba-541e-36d9-959c-5df760a6b98c | -6.99978 | -59.25796 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| c4ae3dc1-8421-3310-a31a-6610b843fe17 | -6.95534 | -59.08205 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 949c6c7e-f51f-3ffd-8cc8-83308f94609c | -7.00525 | -59.26332 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 794c8047-8781-373e-b81c-3a30bc48bb31 | -8.56292 | -63.02781 | 2026-08-25 06:08:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b386c80-8a7f-3769-9a59-91315228a965 | -6.96215 | -59.0782 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66b6fb68-1dad-3b41-88e2-cba3007925fc | -6.96698 | -59.08556 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 995df932-0b9a-397d-b93b-3898bad147ce | -8.81529 | -62.33375 | 2026-08-25 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a87bdf7-c977-309f-9be9-eb777ae27b2c | -7.54429 | -61.29876 | 2026-08-25 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e98d1b54-ae96-3541-9e0c-b0e73e7e505a | -7.00234 | -59.23934 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 90a3d160-f47a-3fe6-9dba-c8d570f55058 | -7.21489 | -60.62469 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 25c6d00b-3336-3754-b86b-1a19c650dac4 | -7.00172 | -59.24381 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 1aa7997a-fa01-3c1e-beed-dd553f955fbe | -9.1997 | -59.57745 | 2026-08-25 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cdf10051-66cc-3bda-81f7-2a10d9c578a9 | -7.00841 | -59.2403 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3f637672-3402-3c33-a11d-d03dd874f5ed | -6.95469 | -59.08381 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16a43958-f05c-36e0-84d5-c6fc74c70951 | -8.81956 | -62.34047 | 2026-08-25 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3948fcd9-89a4-3da2-86cd-23aba362ce4d | -7.0132 | -59.25815 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5aaab92c-d6ce-39d5-a0d2-58c5a5f9a23d | -7.20423 | -60.61934 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5e024770-4fb7-3a26-88d2-75778feda51d | -7.221 | -60.62165 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 681ccca2-842e-339c-967a-90d21c3ce644 | -7.0145 | -59.24117 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7e7848a8-79bf-3599-a35f-06652a9734ee | -7.54083 | -61.36376 | 2026-08-25 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2c079eea-3f92-3bc1-8a4d-0badc8b7fb10 | -7.00715 | -59.2495 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 793aaf94-192a-336c-a956-ee4bd7927f27 | -7.54618 | -61.36448 | 2026-08-25 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61c52b69-bd8e-3b9f-a6df-1727b095799a | -7.00462 | -59.26788 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 55921711-eff4-31f7-849c-536ac8bd9f36 | -7.01933 | -59.25111 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e845c372-3398-3075-af88-9ad004b88a8c | -9.20028 | -59.57268 | 2026-08-25 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 37ed9edb-2410-3fd9-8339-91aef5617c13 | -8.80758 | -62.31417 | 2026-08-25 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1f58ec2-6ab3-3960-8ada-d5d958d5e178 | -9.15347 | -59.40084 | 2026-08-25 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fb24726-e5ab-3cb5-8f6a-3e9d4934b990 | -9.16027 | -59.39693 | 2026-08-25 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3bb45b1c-a75c-319b-91b3-4d81ff0d0ca9 | -8.66496 | -62.8451 | 2026-08-25 06:08:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4e4c5cfc-ae30-34d6-bc62-3d3eb0457c88 | -6.96146 | -59.07998 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 618d4565-9f1d-3c82-8b50-cd209eb9bb45 | -9.15967 | -59.40168 | 2026-08-25 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06d7de43-6a46-32ae-aa8c-7eb2dfce8e27 | -6.99502 | -59.24743 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 95c34a75-a1cc-356a-833b-7423d70ef6f9 | -6.98764 | -59.25615 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 97cbafd6-e559-36c9-9464-6256eee8a8b4 | -8.80552 | -62.32927 | 2026-08-25 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26876a44-54ef-3453-b986-aa7226b7759e | -7.2093 | -60.62392 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a0c5fbc8-4464-3d5d-8e51-f70bb4c421f5 | -10.7988 | -50.9305 | 2026-08-25 06:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 55.3 |
| ddc4688a-d243-3cfa-a424-a05464ee1bf5 | -3.5406 | -48.1889 | 2026-08-25 06:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 8371b151-b458-3343-a03e-9f07d3130e7d | -11.1443 | -44.4865 | 2026-08-25 06:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| e8583e9d-acad-372c-bcaa-03b0b67f97e6 | -7.0057 | -59.2575 | 2026-08-25 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 35572d8e-248d-3fc9-b84c-c90313020acc | -3.5221 | -48.1896 | 2026-08-25 06:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| df8bb878-14f1-355a-87a9-1377df2672c9 | -10.581 | -46.3242 | 2026-08-25 06:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| cefe1abd-e517-36df-93de-8c8444b553ff | -6.9872 | -59.2582 | 2026-08-25 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| fac4b2cd-79d7-3d76-8a9b-53e43d490f70 | -7.2901 | -45.3683 | 2026-08-25 06:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 1eee9f30-21db-3b06-a4dc-e883ed12a6e3 | -3.5407 | -48.1673 | 2026-08-25 06:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 426d0f5e-f458-367f-8096-d6e007425cbc | -7.0058 | -59.2382 | 2026-08-25 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 67427d6a-656b-361d-887c-c629003bc8df | -7.0058 | -59.2382 | 2026-08-25 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 845b8a42-b2e6-3ce9-971c-63590b7ce326 | -6.641 | -58.4987 | 2026-08-25 06:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 164026c7-31e8-32be-ba5b-dcdf2a8acd49 | -7.2901 | -45.3683 | 2026-08-25 06:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |


[Clique aqui para ver as próximas entradas](README68.md)
