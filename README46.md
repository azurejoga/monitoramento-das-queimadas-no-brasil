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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0fd5cd16-1a71-310e-a373-2871ce8113d9 | -9.4866 | -62.3849 | 2024-10-03 01:56:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 720ccb20-c2da-39ff-b4f7-bb85a9c6254e | -9.494 | -68.4895 | 2024-10-03 01:56:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 788dcecf-d186-3445-a910-845c53efa963 | -10.1802 | -57.2848 | 2024-10-03 01:56:04 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 6c2a1b26-ae26-3619-b529-0d5a5315bdcd | -10.5736 | -48.0839 | 2024-10-03 01:56:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 2b0b2bb1-0f9d-32b5-88b4-682dec47f75d | -10.8942 | -63.8971 | 2024-10-03 01:56:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 5b1f4668-ceb3-3fe9-ad70-bc4aeee0be43 | -11.2566 | -60.5825 | 2024-10-03 01:56:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 36bd5c3b-12da-3a9c-97c5-f3dc7d41b0e5 | -11.6742 | -65.0172 | 2024-10-03 01:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 3ca122c4-ce02-3314-8dd7-f36be634b04d | -12.4038 | -63.0009 | 2024-10-03 01:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 35f6eac5-3223-389b-b817-33fcb394ee4a | -12.404 | -62.9817 | 2024-10-03 01:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 8306bd0e-cbfb-3d49-b8b3-8758ecda11ee | -12.5329 | -53.1212 | 2024-10-03 01:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 96.6 |
| d0238bd7-25c2-328a-9b7e-9aadcaba5e22 | -12.5332 | -53.1003 | 2024-10-03 01:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| d850579b-7933-3f80-beab-08678a0b15b8 | -12.6295 | -63.1225 | 2024-10-03 01:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 68.8 |
| a4b18d7b-7492-3c01-91d7-e379c88dd378 | -12.6484 | -63.1214 | 2024-10-03 01:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 96f45d45-e503-3ad5-b566-67583b561513 | -12.6486 | -63.1022 | 2024-10-03 01:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 75.4 |
| a4f4e56f-cf85-350e-9e47-4286965b3fd9 | -12.8049 | -62.497 | 2024-10-03 01:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 8b6b469a-3486-347c-8136-e577bb6cc255 | -12.8808 | -62.4731 | 2024-10-03 01:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 194f1004-beaf-329b-b977-daa2157c0236 | -12.881 | -62.4538 | 2024-10-03 01:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 67584fc3-80df-32d8-82cf-e05f03b1a292 | -12.8996 | -62.4913 | 2024-10-03 01:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 4694807d-b232-39f5-822b-affef40175c7 | -12.8998 | -62.472 | 2024-10-03 01:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 149.4 |
| c69e5d9a-9e57-39b4-ba47-eba742d1d7a0 | -12.8999 | -62.4527 | 2024-10-03 01:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 16c3790c-606d-3156-b5f7-90621aadb9d7 | -12.9741 | -62.6409 | 2024-10-03 01:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 19c3a993-8779-3461-8e18-5841d680bcc7 | -13.5195 | -51.1467 | 2024-10-03 01:56:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.7 |
| a04e2817-5b3f-3fa3-b5dd-ff27eabf39dc | -13.5562 | -51.2489 | 2024-10-03 01:56:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.3 |
| c026ca11-1d19-34c4-ade8-d0fd63c6ad86 | -16.6688 | -57.374 | 2024-10-03 01:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.0 |
| 1a46d53d-6f75-3a73-9c8f-9c89d4fc2ba1 | -16.7594 | -57.8328 | 2024-10-03 01:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.3 |
| 958fb0fd-3ffe-3a0b-afb1-b442632f997d | -16.779 | -57.8306 | 2024-10-03 01:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.6 |
| 15751418-d8e1-3103-b304-3c6de85bc124 | -16.7793 | -57.8102 | 2024-10-03 01:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.1 |
| 47f95c91-4de6-3093-b2a6-3e4d7bb52767 | -16.9176 | -57.7131 | 2024-10-03 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.6 |
| 33faad37-4623-3971-9da9-f4c932b1293f | -16.7985 | -57.8284 | 2024-10-03 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.4 |
| 2eed1006-902d-3ae0-aa1a-24f6ed83f3c2 | -16.8787 | -57.6971 | 2024-10-03 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.6 |
| 0e48b537-fa86-3df0-8f98-4742e9aec58e | -16.898 | -57.7153 | 2024-10-03 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.3 |
| b24bd42d-0c59-3304-90bb-41f26049fe04 | -16.8983 | -57.6949 | 2024-10-03 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.5 |
| a1b60a13-bee6-3b09-91fe-aaba7c1d45d1 | -16.9179 | -57.6926 | 2024-10-03 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.0 |
| 0579ff35-884f-3e85-bed9-5fbf1b46a547 | -17.197 | -57.3741 | 2024-10-03 01:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.1 |
| 2a1fb268-16dc-37fb-920d-3dc5c7e8dc05 | -19.0344 | -43.1944 | 2024-10-03 01:56:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.0 |
| 7331abbf-7741-34b6-a7ce-61010224ed22 | -19.3159 | -42.5976 | 2024-10-03 01:56:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.4 |
| 7ac01d68-13b0-397e-93ea-3babdcd487c6 | -19.8803 | -42.1132 | 2024-10-03 01:56:55 | GOES-16 | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 129.8 |
| 45e3782e-cec5-3c49-9377-7ce616de16af | -19.8812 | -42.0877 | 2024-10-03 01:56:55 | GOES-16 | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 112.4 |
| 35d199dd-0173-3446-88b4-ee71f30cce9b | -19.9009 | -42.1074 | 2024-10-03 01:56:55 | GOES-16 | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 86.4 |
| b91831a0-5fc3-3edd-bd09-d4282a58e93e | -19.9018 | -42.0818 | 2024-10-03 01:56:55 | GOES-16 | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.7 |
| 2162fcea-0267-38cd-b4b7-6d8a8fdb748d | -20.5479 | -46.2492 | 2024-10-03 01:56:59 | GOES-16 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 8f59b5e7-4975-3e87-b2e5-8587f892e548 | -21.346 | -55.6626 | 2024-10-03 01:57:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 3b2162c2-3665-3d41-8865-91ebdb134e2b | -21.8799 | -48.4195 | 2024-10-03 01:57:06 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 68.3 |
| da381cbe-ab78-3e81-a959-fcd5ee60c95f | -22.3711 | -47.9225 | 2024-10-03 01:57:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 85349965-ae39-3793-9806-ec6142300008 | -22.4452 | -46.8817 | 2024-10-03 01:57:09 | GOES-16 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 885b6410-17b8-3ade-a156-7558742b92e8 | -22.446 | -46.8576 | 2024-10-03 01:57:09 | GOES-16 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 88.8 |
| bbc6371d-8878-334a-88f2-7b51a615c6c8 | -23.5556 | -53.31771 | 2024-10-03 02:04:00 | TERRA_M-M | MARIA HELENA | PARANÁ | Brasil | 4114708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 23.7 |
| 6243c8f6-37e5-373d-a0fa-07ae653dc98d | -23.54341 | -53.32626 | 2024-10-03 02:04:00 | TERRA_M-M | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 32.8 |
| 5e31e793-2753-3cbe-a879-3aca73e271db | -18.89116 | -54.50308 | 2024-10-03 02:04:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 6ba6a1bc-5b3c-3565-aa9d-b86cc234c748 | -21.37055 | -55.70663 | 2024-10-03 02:04:00 | TERRA_M-M | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 6106d9c6-74c1-3291-b6d7-ffd2debc233f | -21.3663 | -55.68393 | 2024-10-03 02:04:00 | TERRA_M-M | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 19.4 |
| e2998fa6-4756-3bfc-8ba2-7e8b81e9147c | -21.35308 | -55.68727 | 2024-10-03 02:04:00 | TERRA_M-M | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 59bc5d31-7dba-3bd4-a5c4-8521296a6348 | -21.34875 | -55.66434 | 2024-10-03 02:04:00 | TERRA_M-M | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 450be81e-9e2f-34cc-b8cf-1e077c1b070d | -21.34498 | -55.69558 | 2024-10-03 02:04:00 | TERRA_M-M | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 22.5 |
| f3407287-e7f9-3045-b74c-1116d92a460b | -21.34081 | -55.67268 | 2024-10-03 02:04:00 | TERRA_M-M | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 88bdd419-c4fd-3b6e-bbaa-9dae795957f2 | -21.33981 | -55.69031 | 2024-10-03 02:04:00 | TERRA_M-M | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 39.2 |
| debd815f-3212-3a42-817f-9057a0e09e55 | -21.33547 | -55.66745 | 2024-10-03 02:04:00 | TERRA_M-M | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 7e49e695-e6ba-3fb3-bd54-224e32bae683 | -20.05846 | -55.96031 | 2024-10-03 02:04:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 22.1 |
| ea4ed918-6984-371a-9c21-dcb0b7cb1fcb | -20.05417 | -55.93692 | 2024-10-03 02:04:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 24.0 |
| e571f987-3b7d-3fdb-a1cd-d576688e3e00 | -18.72121 | -57.33371 | 2024-10-03 02:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.8 |
| b018c350-4391-3184-92a7-7951a00f4430 | -18.69288 | -57.31915 | 2024-10-03 02:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 1b3cac1e-93d1-3870-a92d-483d86efcba0 | -8.85 | -45.51 | 2024-10-03 02:04:35 | MSG-03 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d6cc2ae1-c403-39d7-b2c3-257c66e31038 | -3.3854 | -42.2866 | 2024-10-03 02:05:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 217bc04a-ec01-3cfe-a120-119164add314 | -3.3855 | -42.263 | 2024-10-03 02:05:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 0d4c7343-1e06-3ed5-ab39-31e29257cd37 | -3.404 | -42.2858 | 2024-10-03 02:05:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 1088577d-d020-3096-8fd2-9ace236defbd | -3.4042 | -42.2621 | 2024-10-03 02:05:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| e4db9790-72e4-3efa-94bd-57b30a1aa1d3 | -3.4227 | -42.2849 | 2024-10-03 02:05:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 5e486557-5042-314e-9722-577fa75c46e1 | -3.4229 | -42.2612 | 2024-10-03 02:05:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 3a7f1424-7779-39ce-bd7b-64376729cf83 | -4.0949 | -48.4894 | 2024-10-03 02:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 98ac5e22-520b-39a0-9951-3ac18d403522 | -4.095 | -48.4679 | 2024-10-03 02:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 3aefa7cd-d6fa-3787-b50a-c071c9c54cc2 | -4.4844 | -42.8866 | 2024-10-03 02:05:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| eca82315-f51e-3a8d-979b-a8bb5a70a671 | -4.5375 | -43.304 | 2024-10-03 02:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| af46c505-a01a-338c-9b45-e4d3b2d19c4d | -4.5562 | -43.3028 | 2024-10-03 02:05:32 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| e97bc18c-dbcd-39c6-adbc-ea375d645d4d | -4.58 | -48.0132 | 2024-10-03 02:05:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| c0e4af10-105d-34fd-b277-6c5d58c20bfe | -4.9264 | -43.79 | 2024-10-03 02:05:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 943dce2e-42e7-3019-b5ea-62c766c3ce0f | -4.9265 | -43.7669 | 2024-10-03 02:05:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 56664c7f-5b5e-39ff-8dc9-b2d008c2ab79 | -6.8777 | -59.0504 | 2024-10-03 02:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 9454e2e0-a8fc-375e-847f-e7ce471582c7 | -6.8778 | -59.031 | 2024-10-03 02:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 0cae7133-5852-316b-9531-7f8b2738f165 | -8.8506 | -45.5086 | 2024-10-03 02:05:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 139.7 |
| c2aa0154-aa34-3e6f-8ef5-7a2d2cd7b53d | -8.8509 | -45.4859 | 2024-10-03 02:05:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 38.1 |
| bf19c4f9-382c-384b-bb83-8231bc180e75 | -8.8695 | -45.5066 | 2024-10-03 02:05:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 38.0 |
| f41be8cd-0490-3b99-a2d7-b565075d88c5 | -8.8926 | -62.3348 | 2024-10-03 02:05:57 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 0d3ed83f-f26d-3b2b-b09e-f6b615a0fbe0 | -9.0516 | -67.8525 | 2024-10-03 02:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 51be6c2d-a211-3ba4-816c-a2bce8937584 | -9.0515 | -67.871 | 2024-10-03 02:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 9f53f307-96af-39ef-abdd-6168b8eea234 | -9.0149 | -67.7423 | 2024-10-03 02:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| b1b79a87-41c3-337d-81d0-a913fe8bf27c | -8.9791 | -67.4099 | 2024-10-03 02:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| c39c2bc8-68bc-3179-84fd-fdca9098235e | -8.9976 | -67.4094 | 2024-10-03 02:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| d4cada63-932b-3f38-bcef-c8cdc82696b0 | -9.1752 | -61.6749 | 2024-10-03 02:05:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 620888e6-48b0-3c96-b183-3bf0e7a5f900 | -9.4866 | -62.3849 | 2024-10-03 02:06:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 3b8b4748-9c1c-367e-8f73-05ac272643a4 | -9.4368 | -64.5419 | 2024-10-03 02:06:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 0652a479-8286-3888-a52a-1c46d6e54285 | -9.3839 | -61.0526 | 2024-10-03 02:06:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 57b987cf-92a1-385a-b84c-3ebf975bb9e0 | -11.4578 | -56.28975 | 2024-10-03 02:06:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 31f4558e-e802-3d65-8529-1b003b2640ab | -11.28597 | -56.14194 | 2024-10-03 02:06:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 410d5cb5-e8ee-3d85-9bf0-77375e2f21f3 | -11.27917 | -56.13649 | 2024-10-03 02:06:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| ab900fda-c676-317d-823c-9901088408e9 | -17.19716 | -57.36666 | 2024-10-03 02:06:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.5 |
| d753b6ce-ed09-3c46-914e-aad701444510 | -16.91452 | -57.70991 | 2024-10-03 02:06:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.7 |
| 65d86dd5-01eb-301b-9a6a-b7355b14dfd1 | -16.91107 | -57.69022 | 2024-10-03 02:06:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 27.3 |
| e1a9a70c-bafc-3a9d-8e02-a3243849a1b8 | -16.8013 | -57.82455 | 2024-10-03 02:06:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.2 |
| 8d93ecac-a2e8-3a71-bf5c-766fb77d40f9 | -16.78885 | -57.82696 | 2024-10-03 02:06:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.9 |
| aaf828c7-2f78-378b-ac10-5569ddec721a | -16.7764 | -57.82936 | 2024-10-03 02:06:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.9 |


[Clique aqui para ver as próximas entradas](README47.md)
