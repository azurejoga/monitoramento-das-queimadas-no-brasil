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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8323c17-1365-3309-9d5a-66fec85b8b6e | -9.14995 | -59.64786 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3db9314e-ee0b-3593-8744-d0cc5617e51a | -9.79825 | -63.55422 | 2025-08-14 06:01:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46fa91b0-df88-39fc-b888-d2774d9973cd | -7.6323 | -63.52064 | 2025-08-14 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1d78995c-4dfd-3b00-853d-f763ae3eb600 | -5.74141 | -59.89738 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 285cdec0-e968-3a34-9bd7-e8d392be604a | -9.15453 | -59.66965 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 6a67e470-32d9-3b1d-8a5b-2ee0b97dfba8 | -5.75725 | -59.88069 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94955719-5b7d-352e-a64d-d84c17045030 | -6.11352 | -59.91587 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4bbfaeb4-059e-3f48-8581-2c648902327d | -5.7499 | -59.89176 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1923f24e-d9a7-322d-add2-aaef4c33374e | -6.08627 | -59.94382 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 420de501-bc2f-3f35-8b51-82cdc4dd8043 | -9.16229 | -59.65669 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9c094d83-48b7-34fe-adcb-6832e43c6e4a | -7.62311 | -63.5193 | 2025-08-14 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 25bc3f8f-1a87-355b-9fa4-664881a1f78d | -7.62376 | -63.51455 | 2025-08-14 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6aa99995-1f75-3a03-bb12-b2ccf9a12d40 | -10.04624 | -64.89591 | 2025-08-14 06:01:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 276ec774-9ecf-3238-939a-56216f4c73ee | -7.881 | -61.81706 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a90b3e8b-9e89-33ef-978b-322fc3168a41 | -6.89655 | -59.14181 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5b0ed8a8-e4a4-378c-9d28-f72bcc9e830b | -6.90445 | -59.12888 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4a7bc300-e508-3b94-b85c-172043bf718e | -6.65741 | -58.81931 | 2025-08-14 06:01:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 637b6a9b-1b32-3867-abaa-0334d5c8ce24 | -6.89594 | -59.14656 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 7eccc9ce-8398-393b-b001-a84ce0a7cd7c | -6.91605 | -59.13532 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e8ab7904-55ea-3027-8ab3-aeca7e67c3cc | -7.24055 | -57.64595 | 2025-08-14 06:01:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f505a380-0bef-3a73-9a97-269fd9d750af | -7.12925 | -60.12372 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76aae2f0-1e66-316d-986e-e56f3aa67990 | -6.91023 | -59.12726 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 30d8f1ec-b225-3437-b023-4f2c7f71aebf | -7.60866 | -63.52202 | 2025-08-14 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 910d562d-7b35-3d96-9b8d-c6787dc58e1b | -6.10393 | -59.94293 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c999f4df-2199-34ea-b126-61f1600587f0 | -7.09012 | -60.0191 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f9f4270-84dd-3b49-8a14-f1700180313a | -6.8717 | -59.136 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d25418e7-0dd8-39e8-9ebe-6ebde907f0c5 | -7.87667 | -61.80993 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c3cf6ab4-5304-315c-9d41-2c57b83db236 | -6.87762 | -59.14404 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d5bdb61d-de4b-3203-aaf5-751aa2b07b41 | -7.12872 | -60.12773 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d695228-b779-334a-a020-ee6936bb867e | -8.11021 | -61.19556 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 21188bb5-12f0-38f3-8b26-9f147d93d5d1 | -9.15508 | -59.66508 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 377d5200-63a8-33c2-8830-7aba9f03a705 | -10.0625 | -67.74848 | 2025-08-14 06:01:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0dd94535-8fca-3f7e-823b-ad6b071fe97b | -9.49923 | -60.52509 | 2025-08-14 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59fb0eab-eb9e-3250-a655-0b0f2d401738 | -7.81775 | -61.32976 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18e38a3c-3f93-37ec-af6f-a1b15748c97f | -7.33174 | -60.62383 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f841c244-ceb9-3d7b-9623-3ebe10401f84 | -6.89421 | -59.15341 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| d11f8cd5-63f7-3a5f-b763-0653d30a4e9b | -9.53716 | -63.57569 | 2025-08-14 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2655d9f7-e9fb-3208-9cea-78a26af6e1f8 | -6.10614 | -59.92687 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 942e872d-203a-3647-9f81-5cefc18aaac4 | -6.08517 | -59.95183 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f2db752f-7361-343b-9591-360ef182aa8b | -5.75153 | -59.87979 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb51492b-fc7b-3705-ad68-70beab833814 | -6.93901 | -59.63371 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5976e252-d91c-32c0-80d0-9f34f14de2be | -5.74065 | -59.87378 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 376ae074-ea68-3dc3-8969-535a939d4ec7 | -10.00685 | -59.22349 | 2025-08-14 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a81ca0bf-fb18-37d4-a87d-eaf3384bda77 | -9.21272 | -59.64948 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2f91a468-06d2-3059-9e07-fb534c81caf9 | -6.90875 | -59.14363 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 761b3edb-0006-39b6-a800-58d1a5c6e673 | -6.92032 | -59.15022 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f929c453-1f61-3aab-a07f-cd2fc2727bcb | -10.43149 | -67.72888 | 2025-08-14 06:01:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c8d54c8-0f43-3a1f-b81c-78eecc9775f4 | -7.09423 | -60.02887 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3dc55940-be27-36cd-870f-c7ddac5d0085 | -7.60931 | -63.51727 | 2025-08-14 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 90af4ff1-9568-3de1-a579-73d6506d0b89 | -6.90412 | -59.12641 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 55a37723-2c67-3135-b2b4-769e104161e4 | -7.33831 | -60.62517 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1aa7f219-3a72-3f86-a249-bde8cc905787 | -9.15544 | -59.65335 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67f8037c-ae7d-3fdf-afd7-ad80364ffe75 | -7.61391 | -63.51794 | 2025-08-14 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 04560c27-94c1-3ba0-80a9-e07ba885d236 | -9.15564 | -59.66051 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5eafe041-4609-38d3-8569-37514a15c220 | -8.11008 | -61.21181 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e11af710-3cd8-32e9-93e4-cb1db726cae5 | -8.10973 | -61.19907 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d1143e1b-b85c-323c-aaba-c86875803ea0 | -9.1372 | -59.65074 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bfef112c-6267-3e5b-8583-2aed7ff47c51 | -6.89677 | -59.13461 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dce49314-f677-3c2d-85e1-75abf7944792 | -9.49973 | -60.521 | 2025-08-14 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e09ee12e-2e8e-33f7-8a47-c20e8473c22b | -6.90225 | -59.14009 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8c80c796-8bf8-3e5f-8261-c675069887a4 | -6.90834 | -59.14103 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| ce8c9174-d258-3378-84a8-be24addda563 | -7.26943 | -60.63031 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 940501bd-40ce-3a1d-882c-60d582f239f0 | -9.15369 | -59.66701 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 606b58bc-93e2-355c-9053-4989d886c250 | -6.89775 | -59.13255 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ee18db7e-2f8e-3951-bca5-222697f36511 | -6.09308 | -59.93679 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 40bfdaba-2c1f-35c0-8fa3-76305c147181 | -10.1066 | -68.96695 | 2025-08-14 06:01:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d9de9b8-5831-3ea2-ad2c-098bfa867287 | -9.18657 | -59.66057 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 33b7a510-321a-30e5-aa0c-2643d125cb52 | -5.75615 | -59.88872 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a5d31b1-d3e2-3538-8fe7-41395aa31665 | -9.19324 | -59.65672 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e364b628-21a9-3e27-ab7e-91d0698d7d66 | -6.07528 | -59.93864 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05b6660a-bc6f-3556-8023-41995df6e506 | -7.62836 | -63.51521 | 2025-08-14 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d256d5bd-6cdb-3258-ab69-cdd49543825b | -6.88811 | -59.15257 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| ec8eb226-f02e-3a7e-b867-1624710aa0aa | -8.65387 | -70.75119 | 2025-08-14 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89dc47ef-596c-349b-bac0-cbbdbd0697fd | -8.11371 | -61.21043 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 625ca668-8245-384f-a3ff-31511eaa9fcd | -9.21215 | -59.65408 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b528a971-4e57-305a-8bb2-1e19f61d98d2 | -6.87528 | -59.15555 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 76fff738-b451-3f70-ab23-308a43247254 | -7.24059 | -60.00044 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 841594e6-d5d8-3d6d-9cb3-8985bb57378a | -7.87581 | -61.8163 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 109feb78-f8fc-395f-9a51-04a7827b0a7b | -6.87702 | -59.14875 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2de807aa-b094-3f56-b5c7-cea68ef6db7c | -7.96094 | -71.43668 | 2025-08-14 06:01:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f3c7073-9d11-380d-b11b-73f31493cccd | -9.06316 | -60.65282 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7fc71643-ac90-345e-8ac6-48165bd3b246 | -9.15066 | -59.65049 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6f0b8771-2601-3244-abeb-c1f54cbb89e4 | -6.88554 | -59.13073 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4f303d66-2f82-30c6-97ca-3f9da65d749b | -6.90083 | -59.15679 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 75daf80e-d3c2-33d2-b2a6-4041989e7c40 | -8.10692 | -61.19343 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7d13d070-7af5-3dd1-8dbd-8d964939df5e | -6.91424 | -59.14923 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 87399c04-fdf0-3d95-8161-d8b5304f839b | -7.61851 | -63.51862 | 2025-08-14 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9ccdfa7b-d0c8-3d2c-9ccc-a9b932e64957 | -7.81819 | -61.32642 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 520d2a5d-05a2-3c1d-a526-33dcd7f28782 | -7.26384 | -60.62961 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e774712c-d6bd-333a-b90b-4791864e8cc6 | -7.25905 | -59.99504 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 12d8ec97-2991-352b-9834-d38867b427f5 | -7.24004 | -60.00465 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b45e25a8-a69f-3c6f-92e1-a54bc3427c55 | -6.09933 | -59.93383 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff59ff59-454e-304a-a29f-4ec0ee8e5394 | -6.87718 | -59.14149 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 618dbebd-649b-38e8-9f59-d73f0acc973a | -6.87884 | -59.13451 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b31d08f7-19e0-32fe-82ea-274d98403ea5 | -9.16668 | -59.67146 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7db70eb0-d230-351a-b74c-2ae56163e334 | -6.89357 | -59.1581 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 30aab0a7-b789-313f-83f3-e2fb99114578 | -6.10448 | -59.93893 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8af365bd-f9c4-34eb-babf-f7c6f83474e4 | -6.88495 | -59.13538 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0a42ca0e-8691-3ab4-9465-222c447e4d03 | -7.2346 | -57.63894 | 2025-08-14 06:01:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c3e5db0c-4dfc-38fe-9ea5-45a9cbbe9354 | -9.93008 | -65.23631 | 2025-08-14 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README36.md)
