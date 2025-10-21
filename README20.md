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
| 4b40f210-3785-381b-b408-0eb0eaa8b46f | -3.86899 | -52.26297 | 2025-10-21 05:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2380b015-b997-3bca-850d-522b5a5358bc | -4.55277 | -49.65323 | 2025-10-21 05:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d089ff76-3fa4-3d98-ae3b-65bb372be37e | -3.0961 | -51.29581 | 2025-10-21 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c742e4d-9f6d-3b1e-91e6-3ced28dba0be | -8.63769 | -63.05203 | 2025-10-21 05:14:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b5a9b9f-7f85-3795-b352-bb331f8ffd71 | -3.12288 | -57.61231 | 2025-10-21 05:14:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92226175-b9c1-3717-8f53-8795d7c2e75b | -3.59842 | -55.26295 | 2025-10-21 05:14:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0574ea80-91a3-3cd2-b5bf-464b853ad419 | -3.14913 | -50.24844 | 2025-10-21 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 083f2f3e-137f-3444-820e-496f8c7ee51b | -4.34228 | -56.06312 | 2025-10-21 05:14:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3f21f597-6692-375f-a317-d241dc7e7e1d | -3.23751 | -54.78068 | 2025-10-21 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1584fa5-df37-3a8f-a398-c4a39a6e7973 | -3.13032 | -53.00109 | 2025-10-21 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 39c2ade7-8e32-3602-be32-4ffa4fdc8948 | -8.72052 | -49.59865 | 2025-10-21 05:14:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 967fca71-428b-3498-8243-fb5230c585fe | -5.04613 | -49.64531 | 2025-10-21 05:14:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f3aa6f66-004d-3386-bc93-c7e36ea38d5b | -3.32 | -53.35434 | 2025-10-21 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| db166aba-a615-3213-bb82-91f84dbaddb7 | -3.11552 | -51.2797 | 2025-10-21 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce665d6a-5024-3c94-8465-db7cc6dbb645 | -3.85332 | -48.96184 | 2025-10-21 05:14:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6f0cc8d5-8ce7-3b49-8c3e-e429ed1e3265 | -8.64175 | -63.05274 | 2025-10-21 05:14:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 45b90f07-86bc-3fec-983c-2170be806260 | -2.91198 | -54.16165 | 2025-10-21 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c305de0-1442-3545-996f-42a2a305eeb8 | -2.406 | -57.65897 | 2025-10-21 05:14:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb0dcc37-cb52-3400-8dda-d21ccf64cdb8 | -3.85477 | -48.96289 | 2025-10-21 05:14:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 482a451a-09c5-3344-bd85-97d9b639c8ee | -3.24635 | -48.76614 | 2025-10-21 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1cded2a-95aa-3ce3-9d12-0f74cc22e488 | -8.29441 | -49.30634 | 2025-10-21 05:14:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c0c115a-13d9-3c59-bbee-35370e360e91 | -9.30221 | -59.42387 | 2025-10-21 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 78a5ded7-3d32-3bd3-a863-943d097174a9 | -9.48469 | -57.92776 | 2025-10-21 05:14:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aeedebad-b166-3377-b912-008d2feb5923 | -3.66025 | -51.95185 | 2025-10-21 05:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a016be0b-718d-3bde-a200-a2561f97dcf0 | -3.13405 | -53.00165 | 2025-10-21 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6333c2d4-c046-3640-abc7-982cdb6d17ce | -3.33265 | -53.24645 | 2025-10-21 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f21cf6e-4bae-3572-9445-745e6fe2104e | -9.88445 | -64.24161 | 2025-10-21 05:16:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| efd6a515-64f0-397a-9a23-f6e07f90c6bb | -9.55881 | -63.26005 | 2025-10-21 05:16:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 684b0cf1-e9cd-3f7c-876e-5d25f30853d0 | -14.82646 | -54.70852 | 2025-10-21 05:16:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4539d8c6-caac-30c6-b2a3-882c8bb3035c | -9.71964 | -67.49126 | 2025-10-21 05:16:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71b77ca6-00f7-3080-bd2e-a364cb1767ba | -9.5377 | -63.50474 | 2025-10-21 05:16:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0f3034c-e510-3d38-b8ab-052b87492277 | -9.88876 | -64.24233 | 2025-10-21 05:16:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab8ecb7f-7596-30ef-8fce-7534525d50b4 | -9.55331 | -67.42083 | 2025-10-21 05:16:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ff98b93-c5f0-3d87-85f3-ea122ba90de8 | -17.40673 | -55.05893 | 2025-10-21 05:16:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 92d3fb4b-eb06-3d33-8a59-34899f3ff3ea | -17.42409 | -55.05058 | 2025-10-21 05:16:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4f96182a-a49e-3d62-8124-773250de0945 | -9.81857 | -64.2271 | 2025-10-21 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f48b3db-98cc-3f02-ab42-732fce2887fd | -12.42548 | -54.42043 | 2025-10-21 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c00baab-acaf-3d5f-b05c-2c9eeaf62549 | -9.04708 | -65.69669 | 2025-10-21 05:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 990ac060-2d0f-3182-a8b0-c9f1923ec96a | -10.30715 | -68.86388 | 2025-10-21 05:16:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad6b2b01-316c-305d-8b1b-152e28161d07 | -9.37907 | -62.62698 | 2025-10-21 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 091ce3df-59ec-3a18-8ae1-73e3c57e924f | -9.11622 | -65.36073 | 2025-10-21 05:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 34939945-a821-3d1d-9965-251905c8df34 | -9.62318 | -64.74823 | 2025-10-21 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c209e8b5-880e-3c5b-ac99-318cfc7a4d9f | -17.43747 | -55.04165 | 2025-10-21 05:16:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| ad97e87f-65c6-381a-b2a7-9f1b6b3d6a1b | -9.55519 | -67.41074 | 2025-10-21 05:16:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb2aae39-71f9-3ac8-b57c-365b9dd7bcf6 | -16.5375 | -53.72948 | 2025-10-21 05:16:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f8a1085-8aa7-3f21-9ac7-65b9f05245a4 | -9.7168 | -67.4908 | 2025-10-21 05:16:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e6cd786-7f9c-3b39-af1c-46507d689dd1 | -17.68524 | -52.25117 | 2025-10-21 05:16:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 85be3b6d-5dd6-3a3d-aa79-cec8342f2602 | -8.9982 | -65.94332 | 2025-10-21 05:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5a0336e5-feee-343b-98a9-c7725d7eceae | -17.42362 | -55.02331 | 2025-10-21 05:16:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 41a5c8a4-601b-3aa8-bcab-b88534e3dc58 | -9.64336 | -64.73822 | 2025-10-21 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a9b7fba-993c-3fae-8be6-a2dfb9ad6a1c | -14.84785 | -52.43685 | 2025-10-21 05:16:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6fc7906-d7df-38d5-b727-15d8298b5dbe | -9.58556 | -66.47531 | 2025-10-21 05:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12f38190-6388-3656-b08b-7933f06465e1 | -17.41611 | -55.04943 | 2025-10-21 05:16:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7a95a7c3-b7e5-3f46-9070-b4126d828be4 | -8.99331 | -65.9424 | 2025-10-21 05:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fc2e2206-bef9-35ad-b875-e749fdff586f | -17.43348 | -55.04107 | 2025-10-21 05:16:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 5d6acd3c-a5b1-30c1-aa21-8cba546390a3 | -14.79497 | -54.70412 | 2025-10-21 05:16:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95fb87eb-2102-3158-92c7-7ae96c741a5a | -16.41291 | -53.62534 | 2025-10-21 05:16:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0332e45f-f567-3458-a2d2-45ab4ff064e6 | -9.00896 | -65.9396 | 2025-10-21 05:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 778dbd01-c4fd-372c-8969-10c9a22fbfd3 | -9.62765 | -64.74899 | 2025-10-21 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a9f087e8-2a19-3b7c-9678-23e4a2449591 | -9.38173 | -67.91378 | 2025-10-21 05:16:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76d7aa49-df04-3b36-9c61-27cab76283c2 | -9.5919 | -63.49942 | 2025-10-21 05:16:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ebb92fb4-8758-31a7-a61e-f2377ab544c9 | -9.00016 | -65.9323 | 2025-10-21 05:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 83852329-2e00-321c-bc12-68a92ee4cdbf | -10.3006 | -68.86674 | 2025-10-21 05:16:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24a9965d-f29c-3764-a4b1-03ccd47e230d | -9.18974 | -61.38643 | 2025-10-21 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dffded08-6e64-3807-a439-d33bd8ca4344 | -9.72089 | -67.4844 | 2025-10-21 05:16:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 928c9993-568b-38b6-b689-590bcdae513c | -17.42807 | -55.05116 | 2025-10-21 05:16:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2ef8f898-34f0-3321-aab1-5346e96e53f5 | -17.68042 | -52.25065 | 2025-10-21 05:16:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 184ed8f4-f159-32cc-a89c-b0b3e1329b3f | -17.42878 | -55.04583 | 2025-10-21 05:16:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| e233921f-4880-36fb-9338-303257425c73 | -9.71875 | -67.48054 | 2025-10-21 05:16:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da95bb55-baab-317b-b7b5-ec690788b65e | -9.78343 | -63.81217 | 2025-10-21 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b784ffc2-9be4-30c6-95b4-9c63bf4d95e2 | -9.80112 | -64.96276 | 2025-10-21 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d43d8f73-b63d-31e1-aa94-d20bb4a6c1df | -9.64444 | -65.26121 | 2025-10-21 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e51f61d7-1d02-3889-b1b3-f8f17633496f | -10.30629 | -68.86652 | 2025-10-21 05:16:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 048d0039-480f-3c35-9f3e-f296af7eb667 | -9.04132 | -65.70116 | 2025-10-21 05:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| feef0e7e-4186-3e52-9405-64d9d612d7fa | -17.41869 | -55.0607 | 2025-10-21 05:16:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0a451906-d44b-3f10-abcf-1ad9b1e7fa85 | -9.61984 | -57.842 | 2025-10-21 05:16:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8d62b37-1096-3708-a229-6b09f9f3cfe3 | -9.98044 | -68.85114 | 2025-10-21 05:16:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9e7bca6-b94b-3ec4-aa5d-29feeb7f25f4 | -9.54076 | -64.57603 | 2025-10-21 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5c5155e-51b2-3cb5-8260-00ef42622767 | -17.67979 | -52.25598 | 2025-10-21 05:16:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 24742c67-d1ba-3859-96ca-a70ddd317a69 | -8.92485 | -66.88969 | 2025-10-21 05:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9abdb614-6f99-39c0-9142-b7eb4762279d | -10.30053 | -68.86524 | 2025-10-21 05:16:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e9dbe16-48ad-3868-bda6-c0829cfc637a | -9.72214 | -67.49188 | 2025-10-21 05:16:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ac48183d-1356-39d9-8991-919fd67f9586 | -9.00505 | -65.9332 | 2025-10-21 05:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 30196c9e-7c43-3293-b33f-d9dd2a33f3ec | -9.11535 | -65.36568 | 2025-10-21 05:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08ba3480-6dfc-3438-a549-0c0354d0541f | -8.99232 | -65.94792 | 2025-10-21 05:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5018c761-b784-37e9-9e8a-30fbfe2f7587 | -17.42338 | -55.05592 | 2025-10-21 05:16:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9bf77c53-3cc6-37bc-ae12-3eaccba56397 | -9.58902 | -63.37722 | 2025-10-21 05:16:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4de3e783-0dc2-356c-82b3-8f34d2cf4a9c | -8.78268 | -66.72208 | 2025-10-21 05:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0018f6fd-502b-371b-83ac-41b3cdfb5b30 | -9.53358 | -63.50402 | 2025-10-21 05:16:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e8469bd-5208-3ea3-9f7c-762212e275b1 | -10.3071 | -68.86242 | 2025-10-21 05:16:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efdcebb9-f721-3c79-ada0-25cf0b91a7a1 | -9.58714 | -63.50235 | 2025-10-21 05:16:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18989920-4422-377b-b5b3-add71a9eece0 | -17.41002 | -55.06483 | 2025-10-21 05:16:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 67a7be7a-dbbc-3ce4-9209-0a54aed016e1 | -8.99919 | -65.93777 | 2025-10-21 05:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 39edc457-68df-3c86-9d4a-b34942956b7d | -9.11065 | -65.36481 | 2025-10-21 05:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9fb5301-3d65-38d0-8fa5-c91b3645d67e | -15.89899 | -59.6095 | 2025-10-21 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ae383663-38bd-3037-a562-de77271f677a | -17.68168 | -52.24001 | 2025-10-21 05:16:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 486ed4d9-b9f2-362f-b118-ca1f16cb3e24 | -8.91964 | -66.88871 | 2025-10-21 05:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8d174e5-d5ca-30c2-a374-68a8eeb96e2c | -17.43676 | -55.04699 | 2025-10-21 05:16:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 37fcc3c9-315c-3966-99eb-a5384a6990b6 | -9.58451 | -66.48119 | 2025-10-21 05:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0ec204f-b3d2-3d3a-bdfb-07229e2819e9 | -9.12091 | -65.3616 | 2025-10-21 05:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README21.md)
