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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20f30e7a-ca13-32c7-bad6-e8e8a68621e8 | -10.4692 | -63.1574 | 2024-10-13 01:46:06 | GOES-16 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 914ad07d-7646-3759-8d50-ab8a36dfbfa0 | -1.926 | -61.729401 | 2024-10-13 01:46:07 | METOP-B | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 74a9962b-2355-3493-9b92-8a3576a3e03c | -1.9162 | -61.731602 | 2024-10-13 01:46:07 | METOP-B | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 42e1c03d-ed7f-3802-a6eb-a2f687c9a921 | -1.9187 | -61.742401 | 2024-10-13 01:46:07 | METOP-B | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 13354b25-8649-3218-a086-4ef0a01f0c09 | -10.9502 | -44.6762 | 2024-10-13 01:46:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| ec7e092d-433f-3a2e-a45d-03f82c34e900 | -10.9506 | -44.653 | 2024-10-13 01:46:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| b4455d60-6dd6-326e-a8a4-8b28f4bf28a4 | -11.6334 | -48.3736 | 2024-10-13 01:46:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 709295c7-2a35-30a3-86a9-8c32a2024b44 | -1.5114 | -61.579601 | 2024-10-13 01:46:13 | METOP-B | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7e4c19dc-097f-3b4c-ab24-901abafd82ae | -12.2754 | -47.6473 | 2024-10-13 01:46:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 0247dc0b-a53b-3032-ad7a-6f8cacd6538d | -12.3982 | -63.7284 | 2024-10-13 01:46:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 83.3 |
| ba1e500a-10af-375a-aeaa-2b6d62d0e337 | -13.1363 | -41.9683 | 2024-10-13 01:46:20 | GOES-16 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 75.0 |
| de8b8c0a-08af-32a0-88fc-e0e077074c88 | -12.9372 | -62.5275 | 2024-10-13 01:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 66b178d5-0815-3007-9a79-4d2e3d33d5d5 | -13.1475 | -62.3215 | 2024-10-13 01:46:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 3ae087da-38f1-3032-994d-8b2b06b9b05d | -13.7153 | -60.6289 | 2024-10-13 01:46:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 25b6e6c7-13bd-3c80-b311-9e122024bfec | -13.7155 | -60.6093 | 2024-10-13 01:46:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 0273a923-5f95-34a6-a838-52f8b3be026c | -13.7346 | -60.6079 | 2024-10-13 01:46:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 93b6006f-3a06-33cb-a50b-1fa44bc8e1b0 | -13.7348 | -60.5883 | 2024-10-13 01:46:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 5953a2b9-c75f-3c26-8cb8-81ef8e623d85 | -15.6294 | -59.4399 | 2024-10-13 01:46:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 1bf47306-65db-3a5e-94ad-c3ab8bbca351 | -15.6419 | -59.9767 | 2024-10-13 01:46:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| c42588f7-8554-34cd-8539-13080011b673 | -16.9995 | -57.4791 | 2024-10-13 01:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.6 |
| 39bfd756-25ce-3ca3-bd2f-ac095b5dea47 | -16.9998 | -57.4586 | 2024-10-13 01:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.9 |
| 7c16b360-513a-3b0f-b5b2-f7426060d82b | -17.0001 | -57.4381 | 2024-10-13 01:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.0 |
| d4029a66-eb0e-3811-a88f-61ad32c23fe5 | -17.1172 | -57.4654 | 2024-10-13 01:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.8 |
| 97765af4-dbfc-33c1-919a-104c5a64850f | -17.1758 | -57.479 | 2024-10-13 01:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 139.6 |
| 1500a672-52d9-31c4-9f41-96778f2ff0dc | -17.1761 | -57.4585 | 2024-10-13 01:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 206.5 |
| 36e2519c-f7b2-3cdc-9be5-83322d856474 | -17.1764 | -57.438 | 2024-10-13 01:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.1 |
| 51b9e29f-1bf8-3a90-879e-6dc0b69088ad | -17.1954 | -57.4767 | 2024-10-13 01:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 124.4 |
| 11293b31-8db0-32aa-adb8-501dfeb73996 | -17.1957 | -57.4562 | 2024-10-13 01:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 148.5 |
| 307a3a23-87d7-349e-98c1-212d60b99c2f | -17.964 | -57.3843 | 2024-10-13 01:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 127.6 |
| 44adff0f-f0bb-3af8-bbfc-21f94c62e4be | -17.9643 | -57.3637 | 2024-10-13 01:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 153.4 |
| 61220836-d81d-395b-bb04-fc1361ef872c | -17.9837 | -57.3819 | 2024-10-13 01:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.3 |
| 859971a2-6382-31ba-9a8b-66cb18dcb7d6 | -17.9841 | -57.3612 | 2024-10-13 01:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.3 |
| 4b8a5541-d335-33d7-9167-845a97aacd1b | -18.2147 | -56.5873 | 2024-10-13 01:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.3 |
| cea3b9e5-aca2-3ac1-8538-ec42d414faf4 | -18.2151 | -56.5665 | 2024-10-13 01:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.6 |
| 1df65bb6-fab9-3df7-8ee9-3c760f72e59b | -18.2166 | -56.4832 | 2024-10-13 01:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.4 |
| 24db44cb-ba41-316d-87b5-6b24160690e5 | -18.2173 | -56.4415 | 2024-10-13 01:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.0 |
| fb4a7182-df2e-3edd-be6d-f9a6fd12068d | -18.2364 | -56.4806 | 2024-10-13 01:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.0 |
| 3bccb5e6-e7b8-394e-becc-03dc6514c798 | -3.0731 | -54.2473 | 2024-10-13 01:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 89f01175-2161-3b25-b661-82b7a0a7b654 | -3.0915 | -54.2469 | 2024-10-13 01:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 2a385880-42bd-3d9a-9267-a8a877ad58a2 | -3.0956 | -53.0559 | 2024-10-13 01:55:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 132.2 |
| da869509-c871-3e9a-9d3f-a7a85f16cbad | -3.0957 | -53.0355 | 2024-10-13 01:55:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 193.6 |
| 7c320d3e-8d15-3386-9bac-3c3846034642 | -3.114 | -53.0554 | 2024-10-13 01:55:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 91ee9ef2-54f6-33a0-a70d-40fe01435bd0 | -3.1141 | -53.0351 | 2024-10-13 01:55:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 129.0 |
| 2f692735-d9f2-3dd0-b717-734bb49cc285 | -3.1792 | -50.4551 | 2024-10-13 01:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 4bd59275-b540-3874-ad98-eae6eb16318f | -3.3595 | -47.3053 | 2024-10-13 01:55:25 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 6a21149d-c6a4-3650-8158-f6d11855cd9c | -3.7128 | -40.7102 | 2024-10-13 01:55:27 | GOES-16 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 58.3 |
| c502fbba-e134-3a84-b216-8f1200d26f91 | -4.1148 | -48.2515 | 2024-10-13 01:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 6bd049f1-b64e-3fbf-8d13-93fc8bbaf942 | -4.1149 | -48.2299 | 2024-10-13 01:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 6a9e630d-07f3-32e2-9280-7dd4ffe63912 | -4.6821 | -60.8081 | 2024-10-13 01:55:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 25ac3198-ae5e-3aef-b336-938d7b2a3dc0 | -4.7004 | -60.8077 | 2024-10-13 01:55:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 86.8 |
| e738ce7b-5d16-325f-a3c2-4d8a82b88d1f | -4.7005 | -60.7887 | 2024-10-13 01:55:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 34d738ae-46cc-3d6a-86ae-174c0f6393d2 | -6.1299 | -47.2884 | 2024-10-13 01:55:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| b457d58c-77d2-3284-a85a-1f87618ef647 | -6.1301 | -47.2664 | 2024-10-13 01:55:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 50a7509a-42fb-31b7-aec4-11ff58d0356b | -6.8918 | -59.8013 | 2024-10-13 01:55:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 79bece59-5744-360a-90b6-62a11d802019 | -9.7359 | -64.2295 | 2024-10-13 01:56:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 7d9be42c-51e9-3400-832e-b1c20d6133a4 | -10.5091 | -49.9798 | 2024-10-13 01:56:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 5d731f9a-b363-3d4a-9beb-550aae0ca929 | -10.5094 | -49.9584 | 2024-10-13 01:56:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| ab70ac66-ad51-3cf3-8bf5-6e9bdf6cd1b2 | -10.5281 | -49.9778 | 2024-10-13 01:56:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 207.4 |
| 7a6e1f43-a315-3151-b8e9-f2335170995a | -10.5283 | -49.9564 | 2024-10-13 01:56:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 335.4 |
| 13840c2c-1c21-390c-a6cb-a10b90204c93 | -10.9311 | -44.6789 | 2024-10-13 01:56:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 376d327a-b697-301b-9f6a-2bc75784b91f | -10.9315 | -44.6557 | 2024-10-13 01:56:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 4acb9580-759e-3f94-b5d3-ad0fef074c79 | -10.9502 | -44.6762 | 2024-10-13 01:56:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 212.2 |
| b30d3501-1853-30f6-a83e-60a8fb4ba443 | -10.9506 | -44.653 | 2024-10-13 01:56:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 253.8 |
| 5436d427-ff91-3b75-9b61-6514a08b08e9 | -10.6913 | -63.47 | 2024-10-13 01:56:08 | GOES-16 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 5bd0f310-f629-3899-94ff-89626a10e2e5 | -11.6334 | -48.3736 | 2024-10-13 01:56:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 326b25db-bf15-3bad-8498-f495f256a35a | -11.712 | -64.9777 | 2024-10-13 01:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 743e32ae-c2bb-3406-b21a-d0eaf3559131 | -11.7308 | -64.9769 | 2024-10-13 01:56:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 7195d81b-3ef8-3d82-8ab5-f6c3bb2754bb | -12.2754 | -47.6473 | 2024-10-13 01:56:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 03e07821-672e-359a-85be-c8980aa4adb3 | -12.3982 | -63.7284 | 2024-10-13 01:56:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 2e3b48b2-954d-3d22-ad20-64f8a26a51d3 | -13.1363 | -41.9683 | 2024-10-13 01:56:20 | GOES-16 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 87.1 |
| d57dd866-d53e-37ac-a8b7-a5a2576ed306 | -13.1475 | -62.3215 | 2024-10-13 01:56:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 3da156cb-4536-36a5-bc1f-965d741885bb | -13.7153 | -60.6289 | 2024-10-13 01:56:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| ab5b91af-f7e7-367d-8c7e-d715a8c03649 | -13.7155 | -60.6093 | 2024-10-13 01:56:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| fa57df43-3352-37fd-8d07-801019f1d3fb | -13.7346 | -60.6079 | 2024-10-13 01:56:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 144.7 |
| db7f8b23-b1c8-30ad-9b65-8199b7194e71 | -13.7348 | -60.5883 | 2024-10-13 01:56:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 92e85fe9-4b8e-376b-baf6-07a06da316fa | -15.6419 | -59.9767 | 2024-10-13 01:56:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 5dfaa606-06ad-3d98-af56-71880bf8379a | -17.1758 | -57.479 | 2024-10-13 01:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 141.9 |
| e3819c35-c252-34cc-9238-e9920f91002b | -17.1761 | -57.4585 | 2024-10-13 01:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 213.2 |
| d427dce4-0ea2-3aa7-9572-1474fbf223fe | -17.1764 | -57.438 | 2024-10-13 01:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 114.4 |
| 4448ca5f-65f1-3b0f-a4d1-ede465666bb0 | -17.1954 | -57.4767 | 2024-10-13 01:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 141.0 |
| f1a18fc9-752a-3093-9374-48500ab8bf9a | -17.1957 | -57.4562 | 2024-10-13 01:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 182.0 |
| 7d221b79-5227-379f-b963-3e949c4a2fc6 | -17.196 | -57.4357 | 2024-10-13 01:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.9 |
| 2f9181c5-470c-327a-b751-329555fa5124 | -17.964 | -57.3843 | 2024-10-13 01:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.2 |
| af22da9e-d8e6-324a-a62b-dec2f1143a46 | -17.9643 | -57.3637 | 2024-10-13 01:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 135.8 |
| 12ed8c83-8139-33e9-bffd-313fc5328752 | -17.9837 | -57.3819 | 2024-10-13 01:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.9 |
| af40ef00-5952-3e18-82d7-91be4f11ce20 | -17.9841 | -57.3612 | 2024-10-13 01:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 143.6 |
| b2fb3e3f-ca90-34b3-b52b-41176af5f8fb | -18.2151 | -56.5665 | 2024-10-13 01:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.2 |
| ff76b1f5-8e5b-391e-8b67-8ae75dc0aae4 | -18.2155 | -56.5457 | 2024-10-13 01:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.7 |
| c9ff9303-4c6e-322d-b2b4-bebb0d70cd0a | -18.2166 | -56.4832 | 2024-10-13 01:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.9 |
| 6f93c4f0-53e6-34e0-b6ae-784368eec3fd | -17.87 | -57.34 | 2024-10-13 02:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a55839e9-61f3-30ee-a4a9-1779ebffeeca | -17.9 | -57.36 | 2024-10-13 02:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7b6550dd-8e35-380a-857d-49ace4c81cd3 | -10.95 | -44.65 | 2024-10-13 02:04:21 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 39188d62-7064-359f-87b0-916c6ed63839 | -2.1693 | -48.8108 | 2024-10-13 02:05:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 41ebed2e-31cc-3d90-a380-9d9f2d55d08d | -3.0731 | -54.2473 | 2024-10-13 02:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 2831e513-3cd7-3a4e-97f0-deb2c6479cc5 | -3.0956 | -53.0559 | 2024-10-13 02:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 146.7 |
| 2c5b3cab-7114-3845-8518-dbd29039dbd7 | -3.0957 | -53.0355 | 2024-10-13 02:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 220.1 |
| 2552fc7b-40b6-3c30-96f5-339a3267fdd4 | -3.1141 | -53.0351 | 2024-10-13 02:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 12426918-117d-3eae-9b55-25012e477089 | -3.1791 | -50.476 | 2024-10-13 02:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 9fdaa46c-8a1f-3d63-8304-bf136f879483 | -3.1792 | -50.4551 | 2024-10-13 02:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 910337d8-d6ec-34b3-8965-475f438401b2 | -3.3409 | -47.3278 | 2024-10-13 02:05:25 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |


[Clique aqui para ver as próximas entradas](README28.md)
