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
| d182e7dc-4d5a-3e64-885e-b17476764fc4 | -20.22846 | -57.99802 | 2026-10-04 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 64ed5ae2-e095-3b76-b3d2-8ce21933611b | 2.87 | -60.54342 | 2026-10-04 05:57:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 24.1 |
| b2592998-dde5-3f76-90d6-ebf1fd7f631c | 2.8652 | -60.54424 | 2026-10-04 05:57:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d0608323-17f1-3787-a1b8-99ddd51ef584 | 2.86603 | -60.54945 | 2026-10-04 05:57:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 18.5 |
| cca51903-35e3-3dcd-b96b-4927d16c2665 | 2.87037 | -60.54771 | 2026-10-04 05:57:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 3c1310fc-a626-3c56-8711-1f3ab75eb46e | 2.8695 | -60.5425 | 2026-10-04 05:57:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 026e9af3-2712-3747-b5e7-5cc981e1cf5a | 2.8743 | -60.54169 | 2026-10-04 05:57:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 32.8 |
| cae90891-24c8-3840-9e17-d3f1715b2ef6 | 2.86558 | -60.54852 | 2026-10-04 05:57:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 5894d6ec-32d7-38de-900e-e185b27695c9 | 2.87083 | -60.54864 | 2026-10-04 05:57:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 512179e3-1bda-3c86-888b-94a16075ded4 | 4.05311 | -60.29133 | 2026-10-04 05:57:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 04d6a221-8bd3-3a11-a01b-fc38d368b57f | 2.87479 | -60.54261 | 2026-10-04 05:57:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 2c147d20-52cf-3aa9-89ee-ca2959ce0d30 | 2.87397 | -60.53737 | 2026-10-04 05:57:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 24.1 |
| a09793ac-909e-3ec3-8c29-dfb5af4dc0d2 | -2.15223 | -59.22445 | 2026-10-04 05:59:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 425ff265-95de-357c-b314-d6de50565c5c | 2.00985 | -61.08983 | 2026-10-04 05:59:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4025f544-09b1-3066-a147-bb937558f53a | 2.01066 | -61.0948 | 2026-10-04 05:59:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cab165cd-bd82-32c5-b049-c9e9f40d4669 | -2.77803 | -57.68552 | 2026-10-04 05:59:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ab0a43cb-d928-3e82-9bbf-9b9a5719faf0 | -1.20787 | -55.86214 | 2026-10-04 05:59:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7f63e9ba-e113-3ce3-ba4b-a61139f5ebf9 | 2.51692 | -60.99861 | 2026-10-04 05:59:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dfc2ac11-98ee-39e8-ac5d-8d20b6ecbc0e | -1.20887 | -55.8555 | 2026-10-04 05:59:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8c0343b5-9f77-3cf0-a787-e36704fdb262 | 2.51394 | -60.99549 | 2026-10-04 05:59:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 02558e72-81b9-3783-b6f4-1e92d6441633 | 1.03954 | -59.46392 | 2026-10-04 05:59:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f64e1a4d-bfe1-3af2-b8d0-d1840dbef40d | -1.2084 | -55.8577 | 2026-10-04 05:59:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 331ed80d-d7ee-31f8-b45e-41e65b060108 | -1.20734 | -55.86445 | 2026-10-04 05:59:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e7e40f7f-3112-3ce4-be41-29954840b675 | -2.15165 | -59.22833 | 2026-10-04 05:59:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf4185c6-664d-313c-a11d-8fa8909cadb5 | -2.05978 | -56.87523 | 2026-10-04 05:59:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 22f6f200-8d4c-3c6b-bc88-9799a2315857 | 2.5161 | -60.99366 | 2026-10-04 05:59:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| abb060d6-b71a-354a-863d-83dda9781f64 | -2.05892 | -56.88099 | 2026-10-04 05:59:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e5b9d52e-fdd6-3b12-ae1b-ce070fde8494 | -9.15274 | -68.23491 | 2026-10-04 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 781b6ec8-2418-3f84-aec1-6a476ff7b46c | -8.4386 | -70.11099 | 2026-10-04 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2638745b-ab2f-3940-877b-6c0200acb8b9 | -8.62184 | -63.95273 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09637e65-2b82-350b-9500-db52e4818050 | -10.98907 | -59.14441 | 2026-10-04 06:01:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3399056b-4d31-3295-a3f2-a557796f00a2 | -8.60495 | -70.2017 | 2026-10-04 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a1395cc-e197-305b-b068-93f544b17ec8 | -8.05065 | -67.26864 | 2026-10-04 06:01:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee2d6016-bbb4-302b-8d40-1a72b1fe4b92 | -8.55923 | -67.06626 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d8aa2964-3796-3d4e-9df3-90f88e94c056 | -9.92788 | -65.04005 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79247d2d-7f6b-38f3-862a-f5e19bf9c9ef | -9.11496 | -67.71069 | 2026-10-04 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c48b1661-98db-31e1-909c-a5092f3d3eeb | -9.23096 | -67.89953 | 2026-10-04 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77520724-7d78-31d6-ad79-4b63bfc4b9da | -9.16458 | -61.40689 | 2026-10-04 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eaa8ae64-9942-32a4-aae2-0a59927a6d4b | -9.54382 | -68.52443 | 2026-10-04 06:01:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1828db8f-dcb5-3f7e-bbb8-8287c88d1f3d | -10.99489 | -59.15046 | 2026-10-04 06:01:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f9c4485f-772c-3a89-9e8f-6922a0c43054 | -9.88394 | -65.13728 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 11317fad-82d0-365a-bc73-c843fc1d2cfa | -8.57213 | -67.00452 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ac8c107-8138-309a-8459-ce2c22fa6b35 | -8.34689 | -62.8334 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 05e9e335-31d7-3af7-a66d-f3cbfef2e5b7 | -8.89546 | -66.7281 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f77b597-850d-32ea-8920-fe849101145f | -7.81975 | -69.99951 | 2026-10-04 06:01:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b9f0144-22a9-351a-a927-6a569e8e8637 | -10.99033 | -59.13368 | 2026-10-04 06:01:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 78648e36-d613-3fab-911f-0f05a717b74c | -9.91986 | -65.03479 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b979403-4005-34fc-a4e8-c84d42cfbe79 | -8.60078 | -66.80996 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0914cef7-0763-3f48-995e-ed169e94c83c | -9.03763 | -65.4263 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85eace4b-8c8e-39f4-9d60-7af3d7224509 | -9.05052 | -65.42435 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 795bdfc9-cdb8-3ec0-82b2-b48ced44e911 | -9.48277 | -64.6892 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1cad7951-c31e-3961-9c68-095a9b8d30d4 | -9.91354 | -65.01715 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 446640f3-4789-3250-b8c3-40d92346dba5 | -9.54585 | -64.81072 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a85164d5-7bf1-3514-9451-cf6a944b7236 | -9.15139 | -65.39695 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f31fdb3d-1af0-3d15-84c9-4931e1d342c3 | -9.5541 | -65.98566 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1189837d-cf27-3988-90c4-ec917aa4a699 | -9.47423 | -67.06396 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66db0d51-bfc3-3b66-b415-61ae59e8b862 | -8.58816 | -66.81745 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 00498ec3-495e-3a78-ae17-559247b91176 | -9.41582 | -68.885 | 2026-10-04 06:01:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb097a0a-100e-3c66-8bd6-f28af8b6d637 | -8.59192 | -66.81799 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ef30e674-42b7-3125-a818-ee44d479df7e | -9.01601 | -65.70456 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 836236c1-0e84-3ca4-a9b7-0f2dddae0ed7 | -10.09285 | -68.26529 | 2026-10-04 06:01:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd2219d3-8289-3951-80f4-a9af335a68b7 | -9.50201 | -68.49409 | 2026-10-04 06:01:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1ada7bb-dbb1-3eac-8812-338ba1cf92ba | -8.67154 | -67.1176 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6357616a-4541-39c8-8e13-23b100c398d5 | -8.88252 | -66.76439 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6026a15-bb8a-3bca-8c57-cdbf6af12fef | -8.54493 | -67.16313 | 2026-10-04 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93b323e4-b8ab-3cd5-a74d-2610dc8adce7 | -8.85587 | -66.78886 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0624c523-e5f7-3172-ba5b-0c47c78762b7 | -10.03087 | -65.26186 | 2026-10-04 06:01:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e7ed20d-2d29-3097-908d-6e706bbacbea | -9.5693 | -66.30323 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7fd6b4a0-2c72-3cc1-ae2e-573adf3e0c61 | -9.40742 | -65.89951 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b696a2d7-1643-3498-9cb5-a57e8d90a6cf | -9.1705 | -61.40388 | 2026-10-04 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74ce1645-8d92-37e5-81c0-48e09f64ae57 | -9.56915 | -66.30453 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| afc65efb-6942-3c23-8f53-162737439d40 | -8.89167 | -66.72758 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f74734f0-5ef1-3212-931b-6bf64678d73f | -9.91873 | -65.04295 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e97e656-e257-3c89-8815-17842538ebe5 | -9.14923 | -68.23436 | 2026-10-04 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1b75d236-9e94-3928-b745-5c51b478e9d8 | -9.13289 | -65.467 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f8dcd910-6943-36c9-9044-b26df063e1b7 | -8.77497 | -69.53466 | 2026-10-04 06:01:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa091aaa-e5dc-3aeb-b4d6-589ebeb87236 | -9.62067 | -64.1758 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14842c79-12e0-3e44-8016-eb165ba9dec4 | -9.7127 | -65.06644 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4211b49a-8748-38b5-8be8-ba45b4768499 | -8.54592 | -67.02793 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8db4e5c4-ae11-39ad-bfab-1b141c4ec23f | -8.60787 | -66.9686 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7573fe4f-55f2-3675-9e11-a8b6f19f078d | -9.13513 | -65.94704 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a119faa-2801-30fb-9794-928aa1db0288 | -8.56338 | -67.01233 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ad8e152-1a32-345b-9ff5-bd77608da33c | -9.48713 | -64.68984 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a2f18e1-66d0-3f6d-a34d-2158ef8ee71c | -8.96326 | -62.34546 | 2026-10-04 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7fb5bfc-8926-3d95-af0d-08d090c44764 | -9.13965 | -67.93246 | 2026-10-04 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9201ef18-7b32-3b4a-82d4-8d597a0f1c7c | -9.50144 | -68.498 | 2026-10-04 06:01:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac9d9169-f404-3206-be83-92116a69ee1b | -9.50492 | -68.49853 | 2026-10-04 06:01:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d3a6b47-47ec-3b63-a65e-7cd7d9bf50d1 | -8.54747 | -67.06902 | 2026-10-04 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6310cb7d-4b93-30c8-8f39-34dadd0dbd89 | -8.86209 | -71.8165 | 2026-10-04 06:01:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59dd799d-e8e3-342a-8eb9-4d3c60c39e9c | -8.56907 | -66.99949 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 604edff8-3118-35ab-a4fd-0dafc3345063 | -9.92043 | -65.03069 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99af5f54-538f-384b-9ee7-e2d85f8d113e | -8.89601 | -66.88428 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 126e3486-c245-3c99-922b-53c7a03a79bd | -8.66849 | -67.11266 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9bbc0bd3-b79a-3d0a-9cf2-d144ea7321d7 | -8.58883 | -66.81288 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5c2c9685-f6f6-35a5-a30a-143ee08f81ea | -9.47783 | -64.69279 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5dc6cc4-cb15-3898-89ed-c24c21865596 | -9.89637 | -65.01466 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9420647a-8f0b-3606-b1c5-38dcb5852577 | -9.38072 | -65.47032 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66ce037e-0439-3a37-b712-f2790cd77939 | -8.62052 | -64.22945 | 2026-10-04 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28522d6c-8a5c-3f62-9d45-b4d21bb071f2 | -9.15553 | -65.39755 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41cc2b3c-d7ae-32c4-a265-b35fbab44d2f | -9.10715 | -67.71377 | 2026-10-04 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README68.md)
