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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70f763a5-3121-3c2f-bee0-eee8b580bf1c | -8.8363 | -62.451 | 2025-08-26 02:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 01ff730c-e163-3f8f-8bff-e496c750789c | -8.3209 | -50.5667 | 2025-08-26 02:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| abc09310-a599-3c56-8a52-619dcfe5f70c | -6.246 | -59.9982 | 2025-08-26 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| ad1e69f6-95ed-3914-80c6-c540b57f7d65 | -11.5397 | -52.14 | 2025-08-26 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 185.8 |
| 60084ee2-1260-3d9e-b43f-00a7e980bf4c | -7.4224 | -60.6236 | 2025-08-26 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| aa3a6d2e-7caf-3e51-a425-475431aee06e | -11.2937 | -55.1129 | 2025-08-26 02:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 3a02b1bb-33bf-39a7-bade-08b029237b4a | -6.8413 | -58.9552 | 2025-08-26 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 65423a5c-3d90-3b1f-9bf8-464e7cbe61f9 | -7.367 | -64.348 | 2025-08-26 02:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 5e01b59d-c9eb-3b85-a0e1-1c5358327c25 | -14.2876 | -49.1291 | 2025-08-26 02:00:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 8ce4d506-52e9-31d9-9003-f1a0da5416bb | -4.9606 | -55.8028 | 2025-08-26 02:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 431c58a8-b09a-3c06-b4d7-b3f709035580 | -11.559 | -52.117 | 2025-08-26 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 146.9 |
| f6455bc1-e1b6-3080-8587-a4b965c6586a | -8.855 | -62.4313 | 2025-08-26 02:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 42cae41e-efb4-30bc-91cb-9d9073fa7504 | -9.1722 | -59.4629 | 2025-08-26 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| b42dacbc-1c7e-300b-991b-47fe5611509e | -9.1909 | -59.4619 | 2025-08-26 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 45c53a56-8510-3891-acfc-88efeef63573 | -9.006 | -65.4 | 2025-08-26 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 0d5fab64-49a3-3cdf-9f13-c49c7064ac7b | -8.3396 | -50.5652 | 2025-08-26 02:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| b97ccf0c-bcf9-39cb-aa0b-d0d37b43cf95 | -8.9873 | -65.4379 | 2025-08-26 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| a680eb11-c145-36dd-9d37-9843d2210193 | -8.8364 | -62.4321 | 2025-08-26 02:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 78b0b561-5b45-337e-bf0b-f176ba8d5546 | -7.3854 | -64.3475 | 2025-08-26 02:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 134.5 |
| 0ad286d3-e655-3190-999c-00d043b77d01 | -6.8229 | -58.956 | 2025-08-26 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 224.0 |
| f14bd197-5659-3184-946e-6a06a8f486e2 | -8.8548 | -62.4503 | 2025-08-26 02:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 164.7 |
| f4e41e9c-92cf-3e9b-844a-eb46a59f48ca | -6.8228 | -58.9753 | 2025-08-26 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 336.1 |
| e3bd8b9b-047c-3b5a-b6a8-4a8d61bb607c | -6.7635 | -59.6718 | 2025-08-26 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 713727f0-342e-3bd4-a1fb-0a7e7c0fa989 | -6.2275 | -60.018 | 2025-08-26 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 92c59080-5b1a-3157-9b32-a9d7c5dc484c | -6.2459 | -60.0174 | 2025-08-26 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 94.9 |
| de94f353-5ccd-3579-859a-9396c7fa514e | -11.54 | -52.119 | 2025-08-26 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 220.6 |
| 21a68293-3fab-3d99-81d0-cda16c932f73 | -9.1724 | -59.4436 | 2025-08-26 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 1609e2c0-968e-3850-83b5-5858b38a5e51 | -10.4241 | -64.3903 | 2025-08-26 02:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 5a7126b6-7a3b-3037-afd7-6efb15e4c507 | -8.8734 | -62.4495 | 2025-08-26 02:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 8cd1b0f3-1c62-31f4-b752-76e0f561c83a | -11.3126 | -55.1112 | 2025-08-26 02:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| e6ec1996-b993-36e7-a9c8-ab696655bf4f | -7.3669 | -64.3667 | 2025-08-26 02:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 0b134a5c-db22-3740-9a46-388d5e20a273 | -6.8044 | -58.9568 | 2025-08-26 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| cd44735f-efbd-3f54-8f17-bc1fcd5c2e0d | -11.1396 | -44.7654 | 2025-08-26 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| e577d4e2-535f-3c09-bb70-24179e60a232 | -11.1587 | -44.7627 | 2025-08-26 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 352.1 |
| 753d4200-5962-33a2-9002-ff7fd20e5e77 | -9.25108 | -65.62348 | 2025-08-26 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 42240de6-c598-3052-ad9b-0953b52d4cf7 | -8.8377 | -62.45281 | 2025-08-26 02:09:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 21e45fc3-0940-3ff7-bac1-bbe47834f03a | -10.41862 | -64.39919 | 2025-08-26 02:09:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 32.8 |
| e2d143c3-de9a-3c53-b4d1-7ce714d45abc | -8.86096 | -62.44318 | 2025-08-26 02:09:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 124.6 |
| b4b190dc-022c-38a5-b066-606c9592e32d | -8.97016 | -65.42805 | 2025-08-26 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 811834b2-5d08-383b-96c3-f67d61e7c80f | -7.37852 | -64.37515 | 2025-08-26 02:09:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| e7d78b72-b190-39d5-9161-ea71e30fd41a | -7.38889 | -64.34691 | 2025-08-26 02:09:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| b00475b8-85c6-3c19-8ae8-a6b69c679f54 | -8.98607 | -65.44585 | 2025-08-26 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 26.3 |
| cc5c0cdd-a3a1-3adc-bce2-5fa4b415c38f | -8.35471 | -62.94779 | 2025-08-26 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 27.3 |
| ce602998-c83b-3eac-a919-d4608196662d | -7.37662 | -64.34338 | 2025-08-26 02:09:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 106.1 |
| cc85f498-a06b-34e7-bf8c-011e4c58148f | -8.8991 | -62.47173 | 2025-08-26 02:09:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 9a7a9083-d9c7-3bc4-8cac-fb1462d79bf5 | -7.38081 | -64.36919 | 2025-08-26 02:09:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 7c6d7792-eddc-30bf-b9e0-40cac9e46239 | -8.85382 | -62.44984 | 2025-08-26 02:09:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 304.0 |
| 511e8ec5-5b9b-3627-95bb-5b6cc03b46ba | -8.62988 | -67.24721 | 2025-08-26 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 6bac3b10-e240-37a8-b551-f78a35fa8f3f | -8.34504 | -62.95637 | 2025-08-26 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 5727b7ac-5d26-32dd-b165-18e9a9d9b36e | -9.81207 | -64.28384 | 2025-08-26 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 3c27b052-c10d-3b61-ae96-84bb93b4c7d3 | -9.04378 | -65.7337 | 2025-08-26 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 23.6 |
| cd00d657-b988-38db-8fa6-7ed6d8867453 | -10.41484 | -64.3765 | 2025-08-26 02:09:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 23.2 |
| c70317ae-b536-334c-b81b-5b861b7ea1a2 | -7.39099 | -64.34104 | 2025-08-26 02:09:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 42fb5f47-3d19-3a5d-ae73-0dd4e1a624ee | -8.98296 | -65.42596 | 2025-08-26 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 662f4cb0-795c-3d6a-90d7-b8e615e3cb9f | -9.08265 | -65.72165 | 2025-08-26 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 06b23db4-de0c-3b9f-8733-f9ea9ecc1cf2 | -10.42106 | -64.38201 | 2025-08-26 02:09:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 41.5 |
| a96e9dfd-e51a-3e73-a36c-3f624b782844 | -7.39514 | -64.36685 | 2025-08-26 02:09:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 7603a877-5361-301f-b8f1-0eeaa643d895 | -7.37453 | -64.34932 | 2025-08-26 02:09:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 139.5 |
| 02a658ca-d869-37c7-a6b3-a3cb76347ca7 | -9.02837 | -65.71683 | 2025-08-26 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 19.2 |
| d61196ef-622c-3341-84e6-d89b51286825 | -8.55096 | -62.63189 | 2025-08-26 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 48d80bf5-e9ca-3d7d-9ed2-d45195fc65c6 | -9.30797 | -63.43928 | 2025-08-26 02:09:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 202846cc-d7ad-3d3f-a669-7e9547ee7c07 | -9.04526 | -65.72775 | 2025-08-26 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 83ba51f8-8d1c-35a2-82a6-a888632d778c | -9.03129 | -65.73559 | 2025-08-26 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 8fde2bb0-bfad-3493-bae7-845aefde63cf | -8.1094 | -62.86894 | 2025-08-26 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 23.5 |
| ba335013-b17e-39c2-9703-c1960e549f4c | -11.5587 | -52.138 | 2025-08-26 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 95.9 |
| f78f6c27-cedc-3180-985f-f73e215c8c5e | -6.246 | -59.9982 | 2025-08-26 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 91b35fa7-9cc5-35b6-a211-dde71d17ed47 | -7.3854 | -64.3475 | 2025-08-26 02:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 81086020-6de6-3f91-82b2-a42cdd51a8d3 | -9.006 | -65.4 | 2025-08-26 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 8b0700b1-7083-3825-ae37-56d22534ab77 | -8.3209 | -50.5667 | 2025-08-26 02:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| b2d7107e-edda-3017-adf4-0aec68a4de35 | -7.367 | -64.348 | 2025-08-26 02:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 8cfc523a-3d48-37bc-9d5c-ac8953cbf3c4 | -9.1724 | -59.4436 | 2025-08-26 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| a2376eb6-1514-321e-8443-8f310ca7d74f | -9.191 | -59.4425 | 2025-08-26 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| a3b84321-8748-3135-b826-eb85a5c2a476 | -11.1591 | -44.7395 | 2025-08-26 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 184.7 |
| e83803ae-911c-35f1-a84a-c493d6e553c7 | -8.3394 | -50.5863 | 2025-08-26 02:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 256155c1-5fb2-3ffa-831f-6839e8d1d071 | -6.2459 | -60.0174 | 2025-08-26 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 4d4829a9-4686-313c-97a6-50a029609761 | -8.9873 | -65.4379 | 2025-08-26 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| e8111a5d-d6cd-3572-9422-02a86ba3eec0 | -11.2937 | -55.1129 | 2025-08-26 02:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 42.8 |
| d61dad2e-8bb6-35bd-a167-9ec3b70c14db | -11.1779 | -44.76 | 2025-08-26 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| a8daffa1-15ab-3648-8881-545e1152a93c | -8.8363 | -62.451 | 2025-08-26 02:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 01729a69-591d-35c4-aa7b-fce80b43f2ef | -6.8043 | -58.9761 | 2025-08-26 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| eb33d3ad-37fa-3376-9a7c-75066fcfc22c | -6.8412 | -58.9746 | 2025-08-26 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 388cf723-f2b5-3c45-84f9-dc36f0db222a | -6.8228 | -58.9753 | 2025-08-26 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 308.4 |
| d612d16a-5cde-3af4-b63a-c21763b016ae | -8.9874 | -65.4192 | 2025-08-26 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 52bac137-0a2d-320c-a331-fc2587fb0fe1 | -8.8734 | -62.4495 | 2025-08-26 02:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 67.5 |
| bed04254-fd17-3e76-a0a0-721d9bfceb1c | -8.855 | -62.4313 | 2025-08-26 02:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 84.5 |
| d316e888-6f3b-35d7-93ee-bedf1d27d42e | -6.7476 | -62.8664 | 2025-08-26 02:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 8ecd5c64-a0a9-3eac-ac85-d2eef655a538 | -4.9606 | -55.8028 | 2025-08-26 02:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 14c92be5-3c6b-30fa-a447-6dbb51221f20 | -8.8548 | -62.4503 | 2025-08-26 02:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 171.0 |
| 2cd4f566-3b65-3ff6-9b42-d31410ea36f9 | -9.0415 | -65.7349 | 2025-08-26 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.5 |
| a6a4f2e9-e249-30ae-a302-98b57058ca74 | -6.8413 | -58.9552 | 2025-08-26 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 45ea23a7-404c-3bf6-bd48-724cb8791a11 | -8.3396 | -50.5652 | 2025-08-26 02:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 3aa39ece-b673-35d3-9262-fafcf337cc5b | -11.1396 | -44.7654 | 2025-08-26 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 116521b2-719f-30f6-aba9-f54ed2883557 | -11.1583 | -44.7859 | 2025-08-26 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| d624ab22-03fd-34b0-a585-e262e3375618 | -7.4224 | -60.6236 | 2025-08-26 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| d3c62a4c-d35d-3b29-8d73-ab1849de7e78 | -6.8044 | -58.9568 | 2025-08-26 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| ab8d285f-29d6-375c-9f41-e750c7a51b00 | -11.559 | -52.117 | 2025-08-26 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 125.6 |
| f5784bd0-cf13-3748-95fb-fc6eeff22e99 | -11.6351 | -44.8561 | 2025-08-26 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 729ff468-1146-3d7c-94f5-26367e1ec3e4 | -9.1722 | -59.4629 | 2025-08-26 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 1d089d3c-88b8-352e-bc96-0ec182988c69 | -6.8229 | -58.956 | 2025-08-26 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 241.5 |
| 2aab591b-6226-3f00-abcf-94d26e0b764d | -4.9605 | -55.8226 | 2025-08-26 02:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |


[Clique aqui para ver as próximas entradas](README21.md)
