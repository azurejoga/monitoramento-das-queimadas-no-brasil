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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f69f0d1-fb4c-30c2-9342-b8824518ed09 | -6.39831 | -54.94446 | 2026-08-17 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| f961f10f-4fac-3ff4-aa26-19085355354e | -7.3794 | -59.99097 | 2026-08-17 00:30:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 572ad175-20fa-3086-b604-7cf224ed39ad | -6.99191 | -59.04575 | 2026-08-17 00:30:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.7 |
| e1a7a67b-97cc-3624-a371-f9c407e7f0b0 | -6.87829 | -56.41759 | 2026-08-17 00:30:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 01950277-2b98-38f6-a0a1-6a39a0f976d7 | -8.8981 | -60.58583 | 2026-08-17 00:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 35.8 |
| b27738b8-df16-329d-bbda-33e224d5d468 | -8.98006 | -60.50687 | 2026-08-17 00:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 162.8 |
| df51ca40-8283-3746-98d4-05af9070c109 | -7.36835 | -55.4871 | 2026-08-17 00:30:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 4e9ac981-1828-33d4-9327-b50f4d529d3c | -8.63543 | -54.71947 | 2026-08-17 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| b0fe210c-83da-36b4-a72d-772be2a954a8 | -7.55257 | -61.17494 | 2026-08-17 00:30:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 38.6 |
| ccdd833e-4022-3253-91a8-bde5c3ba2d72 | -7.42511 | -60.01131 | 2026-08-17 00:30:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| feb71d21-bee5-3aa9-9de4-7ca6c0e53b4c | -7.06747 | -56.64994 | 2026-08-17 00:30:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 270d590c-b86a-3388-9655-75d2e9a86f53 | -7.61787 | -60.96663 | 2026-08-17 00:30:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| d0f9c4f5-3b82-39d7-b83c-04febfaf30ca | -7.56815 | -60.84801 | 2026-08-17 00:30:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| ea0504a6-150d-3927-a19c-2da31511e976 | -7.06869 | -56.65887 | 2026-08-17 00:30:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 08ef5b71-8e2a-3be9-81d2-9f0ceffa1be4 | -10.08002 | -60.50441 | 2026-08-17 00:30:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 87a55f94-8cd9-39b1-8f21-343e95d3af5a | -10.92354 | -62.77605 | 2026-08-17 00:30:00 | TERRA_M-M | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 0e95d750-2ed1-3d92-a44f-6fb21135d6b7 | -6.82906 | -56.45151 | 2026-08-17 00:30:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| b75dcb1f-fba5-380f-894a-0cfc4604563f | -8.90164 | -60.60644 | 2026-08-17 00:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 4e8a3122-5482-318a-9d54-b9672051c3e2 | -8.51583 | -54.92413 | 2026-08-17 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 23d1b6de-998e-3b34-a73d-fcd187096dff | -8.50821 | -54.93435 | 2026-08-17 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 7d1161a8-ce7d-37b6-aae1-e97750e640ed | -7.37962 | -55.50357 | 2026-08-17 00:30:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 565d2eb1-8592-3ccf-adef-318e05891913 | -7.39603 | -55.4922 | 2026-08-17 00:30:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 501e4162-4bf6-3e1f-ae18-5a3d35c79ae8 | -8.51208 | -54.89713 | 2026-08-17 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| aba65b9d-388c-3cc0-acd9-1f73c3337786 | -7.56951 | -60.85426 | 2026-08-17 00:30:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| b3edc298-b8ec-3fe3-8ead-76ec7e1971e8 | -6.78063 | -51.06216 | 2026-08-17 00:30:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| bc540a79-1bdb-30a8-b44f-084fbac97c54 | -8.6367 | -54.72857 | 2026-08-17 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 54b1fc05-eae9-3e68-bb73-ee2fa633d96e | -8.90707 | -60.55935 | 2026-08-17 00:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 5797e4ee-1094-39c1-adfc-60cc53329c44 | -8.73833 | -62.91834 | 2026-08-17 00:30:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 21.6 |
| a25ca92a-c73c-3be3-bae9-159f44aadc06 | -8.52173 | -54.88979 | 2026-08-17 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 870f9572-7ec8-382e-9d7f-dd0622da75fb | -7.55867 | -60.86475 | 2026-08-17 00:30:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 487f48de-2000-3b0a-a7e8-d9df62a9c0b7 | -8.89574 | -60.56085 | 2026-08-17 00:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 71dcb103-01af-31e8-882d-fd827a4eb7c2 | -9.19856 | -60.79976 | 2026-08-17 00:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| f0bcc70c-ec4f-36e9-b8cd-0b2ca6fa3e76 | -8.06989 | -48.53238 | 2026-08-17 00:30:00 | TERRA_M-M | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| f1518bdf-9899-30e3-802e-21a8b12fbf1c | -7.36958 | -55.49596 | 2026-08-17 00:30:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| c48eaa62-6226-35ad-adab-e1f1ee6113d9 | -8.95296 | -60.56306 | 2026-08-17 00:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 2190e230-e2f0-3c00-97cd-a049c22cc054 | -6.83027 | -56.46034 | 2026-08-17 00:30:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 56a510e3-9d75-3b9f-86ef-96ae2804d194 | -8.59725 | -54.70642 | 2026-08-17 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 21441a59-0365-34e1-bcc3-ec6e5037beb6 | -10.91446 | -62.77122 | 2026-08-17 00:30:00 | TERRA_M-M | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 34.8 |
| b3301333-f90c-3134-a89f-be52fa33ccbe | -7.55815 | -60.85568 | 2026-08-17 00:30:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 640d7000-8d96-3412-b42e-e2417efd190e | -10.05852 | -62.45282 | 2026-08-17 00:30:00 | TERRA_M-M | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 20.9 |
| f107be31-942d-39f5-b7d2-4ca7b88a1b14 | -8.90573 | -60.55388 | 2026-08-17 00:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 1ca93001-95d8-3d74-bedb-8f6d3df505a1 | -6.96359 | -56.49894 | 2026-08-17 00:30:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8936cd7b-9909-3c7e-b734-045f43cd7006 | -7.37203 | -55.51369 | 2026-08-17 00:30:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| c38a672d-7fe3-392e-8db3-d309d0ea99f7 | -8.58706 | -54.69864 | 2026-08-17 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 8c404bca-d6e6-30e6-8e91-f488b007a04f | -8.8977 | -60.57601 | 2026-08-17 00:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |
| e90a7300-ee3e-3939-b1fa-0fc4f6f140f0 | -8.89967 | -60.59122 | 2026-08-17 00:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 64067a25-dd75-3b5d-a072-6c680897d731 | -7.3948 | -55.48333 | 2026-08-17 00:30:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 183cc9f0-ada6-31cb-b74f-e544b46c03ae | -7.46167 | -60.00011 | 2026-08-17 00:30:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| aef7427c-35b8-38e5-9921-d42f0ea9ab86 | -8.02356 | -55.15382 | 2026-08-17 00:30:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| a8f7d2e8-5a14-3825-acea-cb6b5cd362ea | -9.19579 | -59.67213 | 2026-08-17 00:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 81d29ba1-1b14-3deb-8e8d-57d102ce5e58 | -8.95105 | -60.54794 | 2026-08-17 00:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.3 |
| c31e4a74-ba68-3a51-bc81-865e08ea89aa | -6.95982 | -59.04504 | 2026-08-17 00:30:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 63a162c1-5215-3933-ad67-f9a09b667b1e | -7.53947 | -55.58593 | 2026-08-17 00:30:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| a9d5709c-af36-3ba9-8d94-f00539d0ec3e | -6.40595 | -54.92776 | 2026-08-17 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0240860b-b038-3d79-9ba5-4dae0cc7cadb | -7.43745 | -60.02309 | 2026-08-17 00:30:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| fa448427-3413-32f3-a9d0-6b2afa93414b | -7.40051 | -49.62563 | 2026-08-17 00:30:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 37df3b86-b4ba-3e75-86bf-ea17544a8020 | -7.38598 | -55.48459 | 2026-08-17 00:30:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 616067fc-0459-3fdc-85b5-e66f4995bce0 | -7.42684 | -60.02452 | 2026-08-17 00:30:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 0b15fe30-2a8c-3f59-87a5-2384a66181f7 | -8.64433 | -54.7182 | 2026-08-17 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| f124bb07-11a3-3c81-a01e-ad86382e6332 | -8.89625 | -60.57061 | 2026-08-17 00:30:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 043e4385-4e39-3f06-adcf-39e83072d280 | -4.12185 | -56.33697 | 2026-08-17 00:33:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8d365857-3ae3-364f-97ef-24ee3e87239b | -2.80702 | -48.59188 | 2026-08-17 00:33:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| b3a2c770-9e36-3dbd-83eb-f0d25f3ea0d1 | -6.11759 | -57.72736 | 2026-08-17 00:33:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| c1f846e6-3ab1-34ee-bfe6-5704a823161d | -6.86689 | -58.94515 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d1f04e04-e867-37b3-94fe-01f71e9ed6e8 | -6.66345 | -58.96831 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 65a66f67-cde4-346b-926f-521ac8dce19b | -6.77932 | -59.77153 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 237887c0-cb18-39b6-a2eb-a79aa45db3bd | -6.65372 | -58.96963 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 14f6afe0-3b4a-3eb1-9b10-d7ea65c1e8fc | -4.09923 | -49.06307 | 2026-08-17 00:33:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| c02e949d-5bb3-36c2-a2ed-75ab5a5c4d3b | -6.62449 | -58.97344 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.9 |
| d3a03fa3-7713-3696-a06a-d834fe62ac64 | -6.77227 | -59.77823 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 1be22158-035a-3a25-a3bd-97046f995a8e | -6.12793 | -57.73547 | 2026-08-17 00:33:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| b3ad98a0-cd1f-3831-8e0b-2062c5aa0080 | -6.02779 | -57.81285 | 2026-08-17 00:33:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 47e308c7-de87-3bed-b34f-9c77311d836d | -6.83733 | -58.96609 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 673f6ca6-6c18-3294-b5fc-1d2d18229d94 | -6.54251 | -58.50058 | 2026-08-17 00:33:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 0fd91072-460e-39bc-a01d-aa36d194c4e4 | -6.62488 | -59.05176 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b7f7e6da-913d-3e84-9e58-01cc77a8d4df | -3.4671 | -56.8078 | 2026-08-17 00:33:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e7919b58-226e-33ab-aa10-e15dad010acb | -6.59531 | -58.97754 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 9e7c7d6d-ffbf-372e-a1e6-a0d58e05947d | -6.71949 | -58.92171 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e7197624-2634-3c56-afca-11fc72b6c47e | -6.68941 | -59.07118 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.4 |
| f8b8564e-e128-365f-ac26-287e6cb4a866 | -6.64398 | -58.97094 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 60072b70-cb83-300f-ad4b-8d5531e8a7d5 | -6.78113 | -59.46481 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 30.1 |
| eb50646a-d78d-32a3-ad6e-5881821768ba | -6.71266 | -58.94481 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 9f7f2207-7935-3ab9-94db-4ae3cc05abe7 | -6.54386 | -58.51082 | 2026-08-17 00:33:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 74ca79db-4d9c-31a5-9010-73a88a299664 | -6.60504 | -58.97618 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 96082601-710b-390c-b965-a612ac009f36 | -6.72093 | -58.93258 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.0 |
| d7b8ce5d-1ed2-3ca6-91ec-5dd0e3eef818 | -2.77299 | -48.56804 | 2026-08-17 00:33:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| c5b83fad-f528-3fd9-801a-589278cf5dd3 | -6.6881 | -59.07709 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.4 |
| b80ed785-2fa7-3c15-8bba-fbc2294254dc | -6.70291 | -58.94596 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 9e628e7f-01b3-3b48-8394-edaf23ffd6ad | -6.10851 | -57.72853 | 2026-08-17 00:33:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 31e3d67b-0fce-3c6f-8632-32bda8c1a5b5 | -6.8388 | -58.97705 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 62be3c30-c0c4-3487-bc12-af79ebddce27 | -4.09489 | -49.07026 | 2026-08-17 00:33:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 81556932-440a-37cc-a7fe-6da0972bcf3c | -6.62634 | -59.06285 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f0bb42f2-4acd-38f9-99f4-4008d59264dc | -6.69461 | -58.95819 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 696a7fd3-5d4e-3fd8-9643-abf103893e6a | -1.83291 | -54.4814 | 2026-08-17 00:33:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 71ecd8b8-9d64-333e-a9ca-29c20c9e7d33 | -6.10978 | -57.73789 | 2026-08-17 00:33:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| c4f77859-efcc-3d64-a6bd-63b2829117a0 | -6.61477 | -58.97482 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.7 |
| a315664f-a350-3bb6-8f38-4369df61ca07 | -6.69317 | -58.9472 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 08680ddb-eb4d-3c74-b593-df759e47976b | -6.63279 | -58.96128 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.0 |
| a2b8c703-a9e5-34a8-93c2-28550a0432bc | -6.77259 | -59.478 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c2200e03-af16-3c9a-98b4-2a9231ce443b | -6.71122 | -58.93391 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |


[Clique aqui para ver as próximas entradas](README6.md)
