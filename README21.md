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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a974cc2-9d28-3719-8614-f428eb9ac77c | -3.0689 | -50.3326 | 2024-11-12 05:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 648672fd-7543-36d2-9b45-30b318415273 | -2.1271 | -50.6912 | 2024-11-12 05:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 146.8 |
| 7dde99df-8806-31f5-9be6-75e4c3aea0af | -3.9668 | -48.1932 | 2024-11-12 05:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 6e4728df-3a4f-3856-ab05-1865d1fde8f8 | -3.1097 | -54.2865 | 2024-11-12 05:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| b7f42be6-ec54-3f73-ba29-42fc0b5b0ab8 | -2.7587 | -49.3497 | 2024-11-12 05:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 34b57b02-a72f-38f1-9839-6285bff6649d | -8.73926 | -63.49081 | 2024-11-12 05:20:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4843f113-b011-3731-95fb-8c3471452da8 | -15.03429 | -57.19094 | 2024-11-12 05:20:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 079d0ab7-2830-32bd-972a-e2af0ab11318 | -9.85301 | -62.14742 | 2024-11-12 05:20:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bc6733a-04e3-33c5-bb1e-92fdf382eb08 | -13.4863 | -60.66536 | 2024-11-12 05:20:00 | NOAA-21 | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| feedc58e-5130-330d-89f7-cc15b74f6098 | -8.74179 | -63.48856 | 2024-11-12 05:20:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d9d6c019-05c7-3c0b-85db-779661bd645c | -7.92883 | -61.5567 | 2024-11-12 05:20:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f19d5a83-d4e7-3f7f-9da6-f57cca1838a2 | -9.16981 | -63.2097 | 2024-11-12 05:20:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c21f0ca8-13bc-3d79-9d9a-8a10560e80c0 | -8.64342 | -63.45827 | 2024-11-12 05:20:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 637636c4-2221-38d2-a251-687f49839821 | -8.99559 | -62.10498 | 2024-11-12 05:20:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12cfe663-9e29-3ae9-ae8f-2900fa0f1b54 | -9.16184 | -61.68786 | 2024-11-12 05:20:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4531da86-260a-3e50-b485-a7150e5c6730 | -15.03187 | -57.18791 | 2024-11-12 05:20:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36690c4b-6d55-3dba-9799-9494713cb10e | -9.36748 | -61.82806 | 2024-11-12 05:20:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 9.5 |
| dc1f8c5e-a9d7-38ad-aab1-2236844f25e8 | -14.72023 | -60.02283 | 2024-11-12 05:20:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8e1d4cd-2e3f-3c0f-adb2-0b166b93b19c | -8.6397 | -63.45766 | 2024-11-12 05:20:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80f8267c-c443-3e75-8417-aba02dd0c258 | -15.30214 | -56.50571 | 2024-11-12 05:20:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fbbb58b0-b081-3367-b3ab-7dee844ac951 | -15.50798 | -57.53492 | 2024-11-12 05:20:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6a0fcd7-b886-356c-93e6-91793a232e5b | -9.3709 | -61.82861 | 2024-11-12 05:20:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 410ca4a9-88eb-39d2-b01f-559093ab6e7e | -15.30926 | -56.51203 | 2024-11-12 05:20:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 85096784-89e7-355e-9922-7cf683cfe110 | -10.3827 | -60.33109 | 2024-11-12 05:20:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b952584a-66ec-3c94-a60b-cab0c4850df8 | -8.79954 | -63.24572 | 2024-11-12 05:20:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88840cc3-f65b-3cef-8ec4-38e7616a1bb2 | -14.71355 | -60.02176 | 2024-11-12 05:20:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3406a9c-71bf-3bac-b74e-19c22d700502 | -10.33695 | -62.15502 | 2024-11-12 05:20:00 | NOAA-21 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53bf118a-b027-3be9-b54d-265484f993b7 | -15.31638 | -56.51835 | 2024-11-12 05:20:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b50ea1a-1e97-3386-9422-a0274411ca0a | -14.72746 | -60.02028 | 2024-11-12 05:20:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8469a47-cbba-33d6-b80a-9f52ff557999 | -8.80027 | -63.24136 | 2024-11-12 05:20:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1dd913e-09c1-3202-a6b7-872e696ae3d6 | -10.37939 | -60.33056 | 2024-11-12 05:20:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c600a59b-e221-3e8e-bea6-60239302e582 | -14.71744 | -60.01867 | 2024-11-12 05:20:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6b3cfd4-6fde-3284-a371-b21833306410 | -9.35822 | -61.99357 | 2024-11-12 05:20:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a80a4171-cfc0-38db-a710-8d0419d11231 | -8.99211 | -62.10441 | 2024-11-12 05:20:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c40a2920-5ea8-30a4-91aa-64c14ecf5cd2 | -8.74002 | -63.48631 | 2024-11-12 05:20:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2dba6fd-7d5e-3b73-9194-c3e7cf17ad2e | -9.86939 | -60.22016 | 2024-11-12 05:20:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c28778f6-bada-31e1-8607-530c9158661b | -17.24594 | -57.48167 | 2024-11-12 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 5d199f33-8955-3196-ae4c-7057849c235a | -15.9817 | -59.37011 | 2024-11-12 05:22:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7ea2114-21f5-3090-a246-0bc01027955f | -15.95649 | -59.32692 | 2024-11-12 05:22:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6359604-c906-38b1-bc8f-b2d105963352 | -17.59278 | -57.54082 | 2024-11-12 05:22:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 4d8465e4-2930-37c4-83e8-a79b2645eded | -16.08885 | -60.11136 | 2024-11-12 05:22:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42f24f26-8a6b-3d05-b293-958de0e0722a | -16.21039 | -57.43554 | 2024-11-12 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6e7f55bf-b328-3f48-803b-a954defb7bad | -17.23705 | -57.49015 | 2024-11-12 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 29ca9868-f522-3fd7-a819-ba49f269cecd | -17.24972 | -57.48223 | 2024-11-12 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 7adf49b0-045e-3e93-a436-c9b68f5d8093 | -15.93604 | -59.34713 | 2024-11-12 05:22:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d44b6d78-0f05-36c0-8735-f3cb2a60b42a | -17.26422 | -57.48928 | 2024-11-12 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| bc198d45-14dc-3132-b4e0-8020b50c920a | -17.28793 | -57.48458 | 2024-11-12 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 2f2dd807-6e58-3681-8740-4be1c7bf7e36 | -16.08604 | -60.10714 | 2024-11-12 05:22:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 133e062e-d1c0-3921-bbb4-5c506c525fd1 | -15.96101 | -59.29579 | 2024-11-12 05:22:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d110eb8d-f907-359a-a941-5ff3082593fd | -15.99822 | -59.37686 | 2024-11-12 05:22:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9230544-96ce-3e97-bf4a-c4179999327c | -15.95475 | -59.31477 | 2024-11-12 05:22:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43c699fb-e1bf-3089-91e4-bbfc333dc65c | -16.21027 | -57.52121 | 2024-11-12 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2fb6dbb8-b6c4-3764-ba41-e88fea350133 | -15.41785 | -60.28237 | 2024-11-12 05:22:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 32a10f34-282a-35e9-b3d1-7868d784dd8d | -20.11272 | -49.19335 | 2024-11-12 05:22:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cf79f431-dafe-3f68-815f-01f50d7a5379 | -17.58532 | -57.51331 | 2024-11-12 05:22:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 7b007bec-8cfd-377c-b63a-2361f1e50443 | -15.97829 | -59.36953 | 2024-11-12 05:22:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6a9927e-e77b-3d5b-864f-550905b5c201 | -15.92607 | -59.58235 | 2024-11-12 05:22:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9723728b-ffa9-32fe-867f-1727d2aa94e0 | -15.97937 | -59.33825 | 2024-11-12 05:22:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f67d850-8372-355c-88b6-e6912c3a41fe | -17.28921 | -57.47496 | 2024-11-12 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 10855705-aa02-3dcd-b24a-27d415c272e1 | -15.93373 | -59.33884 | 2024-11-12 05:22:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5ee90c7-1630-3963-a7f9-362518da55a8 | -17.24907 | -57.48704 | 2024-11-12 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f2a6f050-f646-377f-bfe8-84226c69d0c5 | -17.27592 | -57.48769 | 2024-11-12 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ac57aba1-c99e-3bae-b536-483ecb97131a | -16.0894 | -60.10768 | 2024-11-12 05:22:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 27fbd85d-d34d-3e38-a28a-a8fd24e02513 | -17.58466 | -57.51814 | 2024-11-12 05:22:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 2bbb1181-9715-3ab6-ba0f-55e7a48fcd98 | -17.25351 | -57.4828 | 2024-11-12 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 77f13506-a8ba-344a-b055-54efdd96a669 | -20.32078 | -48.83111 | 2024-11-12 05:22:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cbf26263-43e8-3c29-b812-4162990ede09 | -17.30939 | -57.49759 | 2024-11-12 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 71167d6a-4590-3b26-8a0b-c91c5c652d73 | -17.58978 | -57.50904 | 2024-11-12 05:22:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| d3f8ab12-1264-3ead-9a8d-991e4a569bb7 | -15.9536 | -59.29855 | 2024-11-12 05:22:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 381c6a93-e6da-37aa-be1c-a87a0cb636ed | -15.95702 | -59.2991 | 2024-11-12 05:22:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 6c39a340-84b9-3176-a29d-c4caf1891720 | -17.24659 | -57.47687 | 2024-11-12 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| f53e235c-54cb-3c6e-a0c5-b2f61391da69 | -17.28478 | -57.47921 | 2024-11-12 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 1d2f0447-d0e9-3de3-850d-e83726e7ad8a | -15.95303 | -59.30248 | 2024-11-12 05:22:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0fa8b3c9-bcb5-37d8-9289-810d6d975ce8 | -15.9788 | -59.34216 | 2024-11-12 05:22:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1229aace-a689-399f-b1c7-f6e9fc69dde9 | -17.58912 | -57.51388 | 2024-11-12 05:22:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 78c3ab8f-f5db-30d2-8d79-a24f221f9c8e | -17.31318 | -57.49815 | 2024-11-12 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5ac2d983-a376-329d-b055-8089f02cdfb3 | -17.31382 | -57.49334 | 2024-11-12 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d230f849-3c20-3afa-bfd9-0e3aa4881291 | -19.62146 | -54.15417 | 2024-11-12 05:22:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93c6811d-d03e-3d84-a66c-c2a687b6145c | -21.31614 | -53.92202 | 2024-11-12 05:22:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 05e4675a-c776-34e4-b945-5f0d2dffbf6e | -19.62689 | -54.14926 | 2024-11-12 05:22:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 670106c3-238f-34a3-b37e-a89f2235e330 | -17.59657 | -57.54139 | 2024-11-12 05:22:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 90029805-8c12-3a15-afd2-46be876ad204 | -16.00506 | -59.37789 | 2024-11-12 05:22:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7353c277-a7af-3bc3-9623-d44bf29de261 | -15.99138 | -59.37571 | 2024-11-12 05:22:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c52d753f-1716-35b7-b40e-763aece441f6 | -21.32117 | -53.92254 | 2024-11-12 05:22:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cf440da8-5eca-3216-8c21-cc81757a337a | -19.62242 | -54.15424 | 2024-11-12 05:22:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a742f73c-594a-3f13-8d53-914e9a4a89f0 | -15.93716 | -59.3394 | 2024-11-12 05:22:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55e10f85-d0b4-3392-8b89-241512634e1f | -17.24725 | -57.47206 | 2024-11-12 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| d1eba93c-f96f-3215-a625-f8fddd9933af | -15.94233 | -59.352 | 2024-11-12 05:22:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b08d211-c7a4-3804-9481-9a94860d6d5f | -21.31647 | -53.91889 | 2024-11-12 05:22:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| abeb55e1-f6f5-3fd9-a710-7d2a487bec1b | -17.2428 | -57.4763 | 2024-11-12 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 636d745f-9827-3107-ae38-e04cd571718c | -22.37048 | -54.41599 | 2024-11-12 05:22:00 | NOAA-21 | VICENTINA | MATO GROSSO DO SUL | Brasil | 5008404 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b7d5c5b3-9b5c-3f72-85b3-dfeebe8c3a82 | -15.95419 | -59.31863 | 2024-11-12 05:22:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0eb9de7-b0d9-343e-ae36-4e8d55a7820b | -17.25417 | -57.478 | 2024-11-12 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 48c3e3d7-fca9-307a-8fcb-99cdfbd9818c | -15.95246 | -59.30641 | 2024-11-12 05:22:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 32aa9616-76ca-31a5-97ce-03ea09feb113 | -17.28885 | -57.30971 | 2024-11-12 05:22:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| dfe4596a-66b1-309e-a5a6-3be2386e7863 | -15.95936 | -59.33133 | 2024-11-12 05:22:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2b2d6c2c-a8cf-3fac-9878-8cb21e7012de | -17.29236 | -57.48034 | 2024-11-12 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e8173cbc-ce96-3b58-95f2-8a7feb745285 | -17.61318 | -57.41486 | 2024-11-12 05:22:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| aaf85836-ae86-3562-8a16-1ade4d2e6f35 | -16.00563 | -59.37403 | 2024-11-12 05:22:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31ad02a8-3382-3e36-bd46-c72f552264be | -17.31761 | -57.4939 | 2024-11-12 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |


[Clique aqui para ver as próximas entradas](README22.md)
