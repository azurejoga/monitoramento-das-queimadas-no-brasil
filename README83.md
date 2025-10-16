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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7aac35a-e36f-3e9c-9620-d156b5857c7b | -12.60215 | -56.51284 | 2025-10-16 05:29:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8768e44-6446-3efe-8a8f-0204fdc4cef7 | -11.93774 | -63.11209 | 2025-10-16 05:29:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2fa8bb53-57a0-3e95-9e96-c295fa2385c0 | -12.70271 | -62.18593 | 2025-10-16 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7300149-a934-390d-9bf8-7ff00a1e1c7e | -13.36171 | -61.34077 | 2025-10-16 05:29:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0cac9ff5-923c-37b7-a843-e04f87f738a6 | -11.72872 | -62.29734 | 2025-10-16 05:29:00 | NOAA-20 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d0fe932-4ac4-3e25-9d47-c8a4057cd9b7 | -10.77164 | -62.0774 | 2025-10-16 05:29:00 | NOAA-20 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bac2918a-56c0-3c6b-bc81-5cdbeb3ce200 | -12.23365 | -63.6036 | 2025-10-16 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0ad27f4a-031c-38b0-b822-bacd084832b2 | -12.60731 | -56.50877 | 2025-10-16 05:29:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ea436c0-5905-31ca-9f85-1e2a0653b453 | -11.76087 | -61.0769 | 2025-10-16 05:29:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 413d3595-dd77-37bc-8ef7-d0530300ecf2 | -11.38064 | -61.2091 | 2025-10-16 05:29:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5150139f-1f4c-3f7f-b624-db0ef76a6adc | -9.53264 | -64.54795 | 2025-10-16 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf28c938-963f-33a5-b2b3-3c234856ce87 | -10.92923 | -57.63691 | 2025-10-16 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3561c825-efd1-30dc-bb92-9f38563e4840 | -18.64922 | -55.01021 | 2025-10-16 05:31:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6e750ac-37df-3cde-ac20-bf9217cf916b | -18.64961 | -55.00661 | 2025-10-16 05:31:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 54ffe169-bca6-395f-a9c8-2a810ef102ae | -2.86688 | -50.72405 | 2025-10-16 06:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| dd2312bb-0b3f-37ae-91d6-18774e729edb | -2.86813 | -50.72962 | 2025-10-16 06:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 49de5e55-0ca8-3cbe-a15c-a68102064ce4 | -3.51538 | -52.49332 | 2025-10-16 06:42:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 5d0d0a5c-53fa-39db-a8b2-426dda276c5a | -2.87952 | -50.72581 | 2025-10-16 06:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 54de6fb0-8824-3a2c-b4ac-2f3b3262796f | -4.11921 | -47.98971 | 2025-10-16 06:42:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 5a0df915-eacb-3c2b-9ab0-744813299e16 | -4.10613 | -48.0291 | 2025-10-16 06:42:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 128.1 |
| c6dac0ec-8de0-35f8-b43e-4a330a6d7819 | -4.11441 | -48.02293 | 2025-10-16 06:42:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 88d1cb32-c383-3c4c-939f-91d9249094d6 | 1.82733 | -55.75169 | 2025-10-16 06:42:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 052cc01d-aab9-3f81-b014-cfc2665ead18 | -4.0984 | -48.02065 | 2025-10-16 06:42:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| fc805804-0f18-37bd-80c3-d7de95076c7f | 1.83258 | -55.78655 | 2025-10-16 06:42:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 54ae512e-f600-36f9-be4a-be62a9f6a9ae | -2.88076 | -50.73142 | 2025-10-16 06:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 68bfde73-305a-3682-ac47-35c6f1dfa2e2 | -4.11058 | -47.99646 | 2025-10-16 06:42:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 139.0 |
| fa48dcb1-2481-3db3-a60f-27fecf49a388 | -4.30561 | -50.39324 | 2025-10-16 06:42:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 7c70723f-6f8f-3860-a1d8-5e1d3d13193b | -4.10316 | -47.98743 | 2025-10-16 06:42:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 4e981d20-e08a-33e7-aa8d-c23949ff863d | -4.30072 | -50.39974 | 2025-10-16 06:44:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 5b01f45c-8135-37eb-a135-adf3f1f84742 | -12.2844 | -47.1319 | 2025-10-16 10:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 123.9 |
| ced92ce8-f796-3129-8b71-fecbf416d388 | -12.2652 | -47.1346 | 2025-10-16 11:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 122.3 |
| e928d038-22f9-3d81-b736-f076aaacbaa1 | -12.2652 | -47.1346 | 2025-10-16 11:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 611f7c22-d65e-3add-ac08-6b4bec5acb3b | -13.9127 | -45.5808 | 2025-10-16 11:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 465b50cd-7ed8-331a-b6a9-22ecd37b686c | -12.2652 | -47.1346 | 2025-10-16 11:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 8a7176d6-64f5-3a70-91ec-d753842da1b2 | -13.9127 | -45.5808 | 2025-10-16 11:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 163.7 |
| fe9a0198-8f66-3b18-9c83-b48dc9551be5 | -11.5917 | -44.0707 | 2025-10-16 11:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 76e68265-3cd3-37bb-809d-96271aa104c5 | -12.2652 | -47.1346 | 2025-10-16 11:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 049015fd-1231-347d-b479-d21e570bda29 | -13.9127 | -45.5808 | 2025-10-16 11:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 281.2 |
| 45df8b46-2f85-3f91-a4bc-912a530e634b | -13.8933 | -45.5842 | 2025-10-16 11:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 665ccab6-d407-3f6e-b843-b216527cf3e2 | -11.4372 | -44.1407 | 2025-10-16 11:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 00abf500-fb17-3cb7-8aa8-ce4acaf50a1d | -13.8933 | -45.5842 | 2025-10-16 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 74118ba3-a9c1-343c-8092-72b5def83184 | -10.6024 | -47.4178 | 2025-10-16 11:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| f7922985-f25d-344f-bd56-655e6324e6a7 | -11.4368 | -44.1641 | 2025-10-16 11:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 127.1 |
| d33ed8a9-6ac6-383b-b94f-98f222506e5a | -12.2652 | -47.1346 | 2025-10-16 11:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 136.8 |
| d1a880dd-db1a-3077-a5a2-cc7ea9925734 | -11.418 | -44.1435 | 2025-10-16 11:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 190.1 |
| 2c779f3f-60c3-3197-b613-7aa0ebac44f9 | 1.0582 | -51.0198 | 2025-10-16 11:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 10a13a1f-a1b7-31f3-af6a-b1b4b97547d6 | -13.9127 | -45.5808 | 2025-10-16 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 309.8 |
| 10559a1b-baac-3049-bcce-995e8fad0a4d | -11.418 | -44.1435 | 2025-10-16 11:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 98706017-bbd7-3711-b988-908c8aac2751 | -10.6024 | -47.4178 | 2025-10-16 11:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 8647f99c-84d5-370f-a26d-aed7f5328b06 | -13.9127 | -45.5808 | 2025-10-16 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 293.4 |
| a766e4cb-a219-320a-b18b-26cccfbd4a18 | -11.4368 | -44.1641 | 2025-10-16 11:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 143.7 |
| bfa318b6-de71-32df-9e69-8c25183406bc | -11.4372 | -44.1407 | 2025-10-16 11:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 122.6 |
| f0ef18a9-207a-3821-a9cc-eb2958f97b98 | -13.8933 | -45.5842 | 2025-10-16 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 9068554c-ef6f-30e4-a677-ce3d3717721e | -11.5724 | -44.0736 | 2025-10-16 11:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 59ec6f48-5759-3e13-bc88-c42baa0f3076 | -11.4556 | -44.1847 | 2025-10-16 11:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| afbc3699-f314-3bf4-9e4c-93e5cd7aa186 | -11.5917 | -44.0707 | 2025-10-16 11:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 4bea6c11-e818-33a2-bc1e-aa9b55176831 | -12.2652 | -47.1346 | 2025-10-16 11:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 7d231495-4409-32c8-8765-f43cd9b24d54 | -6.2354 | -41.54816 | 2025-10-16 11:57:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| afa4f2b9-9767-3000-a8e5-4b200cf4078b | -3.85168 | -41.57174 | 2025-10-16 11:57:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 36.3 |
| d5fbb68d-a5c0-3809-870a-643902eb2bff | -4.3681 | -40.60503 | 2025-10-16 11:57:00 | TERRA_M-M | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| b0853aef-7021-3e21-85b3-303dc3ae2b74 | -6.07221 | -41.91938 | 2025-10-16 11:57:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 7cceafa6-dad6-309f-80ff-845805d3b471 | -4.37232 | -43.39908 | 2025-10-16 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 2bf61ed9-ee69-3a4a-bf4e-51be8df9b4c0 | -5.37017 | -43.13725 | 2025-10-16 11:57:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| a7587c4f-2c67-3fca-bf94-cb86a0f98207 | -6.06589 | -41.90046 | 2025-10-16 11:57:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| db8d0ab1-6706-3d91-982b-3abb82db81b7 | -5.50078 | -43.06105 | 2025-10-16 11:57:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| cf3e0813-9b00-3045-a256-5643fd38522a | -6.03572 | -44.13882 | 2025-10-16 11:57:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 3769aab9-de0f-35e9-8721-f30d2ae6275a | -5.46431 | -42.93748 | 2025-10-16 11:57:00 | TERRA_M-M | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 50.4 |
| a1a3ccbb-6f9a-3b3e-82cb-48303ea2d02e | -4.01802 | -44.18366 | 2025-10-16 11:57:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 41f8f340-c2ca-3ff1-8eaa-8a54ff190144 | -5.7611 | -45.7703 | 2025-10-16 11:57:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 47046514-8aaa-3a7d-ae7a-36f645a1e31c | -6.3631 | -41.48982 | 2025-10-16 11:57:00 | TERRA_M-M | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 27.2 |
| f32e86ca-fbd2-3789-aed4-e7919543491a | -5.1376 | -43.34154 | 2025-10-16 11:57:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 9656ad23-b10b-3761-ba9a-1ffe320cf9db | -4.38272 | -43.39107 | 2025-10-16 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 202.4 |
| afd7f307-3e5d-3c86-950e-988641fa9518 | -4.87336 | -44.57618 | 2025-10-16 11:57:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 14b5d46d-46fa-3e1b-a3d6-8a0c24cc00fd | -6.2265 | -41.54693 | 2025-10-16 11:57:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 8f4ca345-8a24-38dd-9f6d-1d0c8ab7fd1f | -3.98003 | -39.23677 | 2025-10-16 11:57:00 | TERRA_M-M | APUIARÉS | CEARÁ | Brasil | 2300903 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| c33378c1-90b2-3908-a461-9d21e19f04ee | -5.6884 | -45.10095 | 2025-10-16 11:57:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 108.6 |
| a376f8e7-c514-3cc3-85d6-fe73271817e6 | -3.55631 | -41.38667 | 2025-10-16 11:57:00 | TERRA_M-M | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| d1dac87c-48d4-34a3-96c0-5f8c6c8f376d | -6.15966 | -40.91027 | 2025-10-16 11:57:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| f2325b03-32e0-3536-af12-075ee711a837 | -6.37331 | -41.48201 | 2025-10-16 11:57:00 | TERRA_M-M | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| e7f6eb54-20bd-3123-8d9d-f10ff4d82620 | -5.27391 | -43.22777 | 2025-10-16 11:57:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 14affced-3a6e-3a06-a4c8-5625e3676d82 | -5.47577 | -42.92091 | 2025-10-16 11:57:00 | TERRA_M-M | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 35.4 |
| 264dd8e9-fad2-35fc-86dd-3c77197d2938 | -6.36181 | -41.49887 | 2025-10-16 11:57:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 670f2301-6ac4-3e63-9c59-a15d8a7bbb53 | -6.28796 | -43.6791 | 2025-10-16 11:57:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| f6dacb7a-bb76-3da8-8abe-7b42a9c98a62 | -5.9808 | -42.806 | 2025-10-16 11:57:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 19d3940f-da65-3e6b-bccb-0824e1eb41a6 | -5.36126 | -43.13599 | 2025-10-16 11:57:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| b8fd58c5-b906-3104-9e66-33746dd93328 | -5.83627 | -42.34153 | 2025-10-16 11:57:00 | TERRA_M-M | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| b9f40652-0a1b-3576-911f-a3e99fd54c3b | -5.98209 | -42.79711 | 2025-10-16 11:57:00 | TERRA_M-M | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| fc336243-b0d2-3949-9e05-aecc2b0b0d43 | -5.83753 | -42.33274 | 2025-10-16 11:57:00 | TERRA_M-M | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| a719637d-fb5f-353d-83d3-51cdd051268b | -3.3381 | -42.20045 | 2025-10-16 11:57:00 | TERRA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 1848b4ec-e25d-368d-b55a-2cb6113d55e1 | -6.41802 | -43.09812 | 2025-10-16 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 4f239100-c7fa-39f5-aa0f-76cbda169247 | -5.30198 | -43.86126 | 2025-10-16 11:57:00 | TERRA_M-M | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 1d41a0d2-acd7-338c-8a70-63fe12dac515 | -6.41931 | -43.08918 | 2025-10-16 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 79c1b81d-8896-30a1-ae33-5f049b69c67e | -5.6787 | -45.09955 | 2025-10-16 11:57:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 144.2 |
| d256fbc9-2e76-33d9-ae02-46022299b34f | -4.37368 | -43.38981 | 2025-10-16 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| cb22387f-0e69-37ee-aea1-f561c0dcdaae | -6.03773 | -44.31708 | 2025-10-16 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| fa45b344-2d67-3402-8472-cd265ae8e3d8 | -3.48702 | -41.54095 | 2025-10-16 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 670693d6-2d5b-3508-a95d-338c07780be6 | -5.47019 | -39.11359 | 2025-10-16 11:57:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 11.3 |
| abe303af-5919-3c31-b52b-4d23fa6b686d | -5.49948 | -43.07 | 2025-10-16 11:57:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| d4d7fc92-40b4-3835-afc2-c543c06c7125 | -6.25321 | -42.89913 | 2025-10-16 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4aa9628e-c748-3358-a833-b179d6c0d6ca | -3.67054 | -42.57867 | 2025-10-16 11:57:00 | TERRA_M-M | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |


[Clique aqui para ver as próximas entradas](README84.md)
