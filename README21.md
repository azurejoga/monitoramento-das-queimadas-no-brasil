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
| 603260cc-25da-3cdd-b6b2-8ddc3f7539b5 | -11.712 | -64.9777 | 2024-10-13 01:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 70.3 |
| ea6077fc-6a71-38e6-a4d7-dc844793b615 | -11.7308 | -64.9769 | 2024-10-13 01:26:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 87.1 |
| a80037a2-a8d2-3054-bfeb-bc2ea2a7e041 | -12.2754 | -47.6473 | 2024-10-13 01:26:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 5af4d6fe-3734-3662-ad13-c8ec79ab09c2 | -12.3793 | -63.7294 | 2024-10-13 01:26:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 56dd431f-2800-3815-864b-9c2ad0a722ce | -12.3982 | -63.7284 | 2024-10-13 01:26:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 5316bb84-4f37-3819-b17c-0174c04fc18b | -13.1363 | -41.9683 | 2024-10-13 01:26:20 | GOES-16 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 98.9 |
| bf4510ff-ff12-3d03-be11-ae3f8eb5d19f | -12.9182 | -62.5287 | 2024-10-13 01:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 83.4 |
| bb13ae07-8b7f-3535-b72b-732f93b5736f | -12.9372 | -62.5275 | 2024-10-13 01:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 136.1 |
| a020bfe7-d817-3b2f-bcfa-f557eac0f1c4 | -13.1475 | -62.3215 | 2024-10-13 01:26:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 94968e9c-974d-3fa5-920e-e50194b754ed | -13.7346 | -60.6079 | 2024-10-13 01:26:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 2e44f3b9-fae6-3120-befd-95b53e96fd92 | -13.7348 | -60.5883 | 2024-10-13 01:26:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 2a1f9c64-636d-3f33-bd91-150a845629d1 | -15.6419 | -59.9767 | 2024-10-13 01:26:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 13cdf2c4-1f84-3c2f-924f-876bac982403 | -16.9995 | -57.4791 | 2024-10-13 01:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.9 |
| 9ac643ed-1433-30b6-b758-72a021f3e6cd | -16.9998 | -57.4586 | 2024-10-13 01:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.4 |
| f9658633-3482-3362-90db-6978f2818d90 | -17.1758 | -57.479 | 2024-10-13 01:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 138.7 |
| 786324ae-b09b-3ffa-b37a-4c365940631a | -17.1761 | -57.4585 | 2024-10-13 01:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 181.8 |
| a63ac9ed-df12-3d1d-86bb-fa9c33ee8658 | -17.1764 | -57.438 | 2024-10-13 01:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.6 |
| a598d61d-2c27-3f17-80a0-bd6e27dc61db | -17.1954 | -57.4767 | 2024-10-13 01:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 131.7 |
| d3c2bddd-1a67-393d-adb0-b0fdacbabfd9 | -17.1957 | -57.4562 | 2024-10-13 01:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 163.8 |
| 1f8f3fce-0a9a-3fdc-86ad-f6da04d7e258 | -17.6474 | -56.2876 | 2024-10-13 01:26:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.1 |
| e13af378-2999-3f5a-8d35-961939427725 | -17.6478 | -56.2668 | 2024-10-13 01:26:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.7 |
| 4c4f1bb2-307a-3cb5-9ff2-4b78f78d42e0 | -17.964 | -57.3843 | 2024-10-13 01:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 134.3 |
| ef6c084e-ffe3-3237-930a-768bba7d43a1 | -17.9643 | -57.3637 | 2024-10-13 01:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 159.3 |
| cc5524c8-31a5-3e43-9b37-c9e9c38317df | -17.9837 | -57.3819 | 2024-10-13 01:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.9 |
| e01408cc-cab3-3219-ae09-d1a302125f4f | -17.9841 | -57.3612 | 2024-10-13 01:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 161.6 |
| abe7cc09-4aea-3502-92fa-f61a07a006d6 | -18.2147 | -56.5873 | 2024-10-13 01:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.1 |
| 56eeb5f5-6db4-38a7-ba5d-95aa5e321490 | -18.2151 | -56.5665 | 2024-10-13 01:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 139.8 |
| ccc32df4-23e1-35c2-a875-422a90a41d35 | -18.2155 | -56.5457 | 2024-10-13 01:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.9 |
| 13360233-e6b7-3f07-af56-bd2def8d4308 | -18.2166 | -56.4832 | 2024-10-13 01:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.8 |
| d8cf38c0-cf89-3823-abf1-51b91f5ea44f | -3.0731 | -54.2473 | 2024-10-13 01:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 6f4dc79e-96ef-392d-8a4f-a3129d0a727b | -3.0956 | -53.0559 | 2024-10-13 01:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 137.3 |
| 9fefeb98-547a-346b-af44-5602ee291f46 | -3.0957 | -53.0355 | 2024-10-13 01:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 251.3 |
| 2ba2a126-a7d2-3c78-8217-5f348ece2846 | -3.1141 | -53.0351 | 2024-10-13 01:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| d6f120fd-d81b-39f2-8630-b6bb116a7891 | -3.1791 | -50.476 | 2024-10-13 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| d82b5c75-ee66-3bba-840f-4581b8da8b77 | -3.1792 | -50.4551 | 2024-10-13 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| f66f0b81-9e25-342f-9008-727b514e60fd | -4.1148 | -48.2515 | 2024-10-13 01:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 32a3f079-45c6-3530-937a-98d9ab12dfc8 | -4.1149 | -48.2299 | 2024-10-13 01:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 559f937c-c031-3cbe-955f-da04e7ce2373 | -5.5796 | -46.1753 | 2024-10-13 01:35:38 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| b8f91907-f2f0-3ee7-aa4e-7f7b3cc4f89b | -6.1299 | -47.2884 | 2024-10-13 01:35:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 2abeb170-04ed-37d7-b993-407adf77f1eb | -6.1301 | -47.2664 | 2024-10-13 01:35:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 8163a5c6-bc15-305a-8c3f-99073f67c4d6 | -6.1487 | -47.2651 | 2024-10-13 01:35:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 33.3 |
| e00879a8-f2ee-3ab0-b91a-ab480c082f2b | -6.8734 | -59.802 | 2024-10-13 01:35:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| f7817fe5-8a9d-34ce-aa3f-5f128201c548 | -6.8918 | -59.8013 | 2024-10-13 01:35:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| cae76de7-782b-3747-9630-8fdf805d9818 | -7.3841 | -64.665 | 2024-10-13 01:35:49 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| c66bdfc3-e8f0-329a-8994-9d58181d8666 | -9.7359 | -64.2295 | 2024-10-13 01:36:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.9 |
| cdef4cbd-b358-39fc-bd97-7cd9de13f988 | -10.5091 | -49.9798 | 2024-10-13 01:36:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| c0699dd5-0f44-3388-b1aa-815df349eea2 | -10.5281 | -49.9778 | 2024-10-13 01:36:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 249.2 |
| 1482ff49-d325-3e43-8473-3b8d24a01445 | -10.5283 | -49.9564 | 2024-10-13 01:36:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 192.5 |
| 36d2b16e-8c28-350f-be74-a28e39768111 | -10.4692 | -63.1574 | 2024-10-13 01:36:06 | GOES-16 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 84.5 |
| b3969218-b503-3eea-9220-436cadd9c529 | -10.4693 | -63.1384 | 2024-10-13 01:36:06 | GOES-16 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 63.5 |
| e7815b9b-b51a-3572-bb9b-d95e0fd38dc3 | -10.9502 | -44.6762 | 2024-10-13 01:36:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| dece3be4-5bf9-32a3-ab4b-0f0bfa69e4d1 | -10.9506 | -44.653 | 2024-10-13 01:36:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| cca831b3-b55e-3b25-be7d-ed64ea2a8799 | -10.6913 | -63.47 | 2024-10-13 01:36:08 | GOES-16 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 0ad68d5b-ecc1-37ff-b8c8-9e7b9b007f57 | -11.2532 | -50.9249 | 2024-10-13 01:36:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 111aedee-19aa-35eb-a2ba-1a3fe6920711 | -11.2535 | -50.9036 | 2024-10-13 01:36:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 22494e83-f0da-34a2-af63-2e1b9b432878 | -11.6334 | -48.3736 | 2024-10-13 01:36:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 3ef13d0f-591a-3fe7-87a5-b8b3c6232938 | -12.2754 | -47.6473 | 2024-10-13 01:36:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 8703496a-bc41-35cd-a394-448d9c53192f | -12.3982 | -63.7284 | 2024-10-13 01:36:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 1777cac7-c534-3d3d-ab2b-d39607a423a4 | -13.1363 | -41.9683 | 2024-10-13 01:36:20 | GOES-16 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 74.2 |
| 45796681-680c-337e-b620-1378964a45da | -12.9372 | -62.5275 | 2024-10-13 01:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 80cafdbd-1261-3f0f-a2bb-36be2c828084 | -13.1475 | -62.3215 | 2024-10-13 01:36:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 1c501bc1-812d-3f37-b9b8-b6d5f8e5c72b | -13.7346 | -60.6079 | 2024-10-13 01:36:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 0e7ab8b2-fbe1-3ec3-9713-97a6d0dd3676 | -13.7348 | -60.5883 | 2024-10-13 01:36:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| bea93023-199b-3026-8fff-8da779d3d7af | -15.6419 | -59.9767 | 2024-10-13 01:36:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 86c88c99-04fe-37fc-9f8b-a398e0b8ffbd | -17.0001 | -57.4381 | 2024-10-13 01:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.0 |
| d4c83eac-1137-33bf-899f-6d013c69a94d | -17.1758 | -57.479 | 2024-10-13 01:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 141.7 |
| 4bdce750-d092-304d-bcd8-c41ede1549a7 | -17.1761 | -57.4585 | 2024-10-13 01:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 178.8 |
| cd1b3f2a-39c0-3fbd-91f2-259f66385132 | -17.1764 | -57.438 | 2024-10-13 01:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.1 |
| 5cfd3681-5edb-3e89-854b-4e02907e774f | -17.1954 | -57.4767 | 2024-10-13 01:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 136.0 |
| 7ec5b365-93dd-30c4-8376-f94ef064149d | -17.1957 | -57.4562 | 2024-10-13 01:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 146.5 |
| 2f2e83dd-aacb-3e56-99bc-e914b2b8c37e | -17.6474 | -56.2876 | 2024-10-13 01:36:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.4 |
| 61b6c8d6-4632-3a19-ba4a-8a047cc55813 | -17.6478 | -56.2668 | 2024-10-13 01:36:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.0 |
| d6a9ba8e-decd-3f8a-bfd5-b3dabefb4f72 | -17.964 | -57.3843 | 2024-10-13 01:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 129.0 |
| 6338a563-32cf-3f73-82d8-e90bc61fd3a6 | -17.9643 | -57.3637 | 2024-10-13 01:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 148.4 |
| 98ac31de-fccb-35c3-8738-06a91bcc68ac | -17.9837 | -57.3819 | 2024-10-13 01:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 117.8 |
| 8da3e92a-2296-34e2-9a65-cad9da9e9374 | -17.9841 | -57.3612 | 2024-10-13 01:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 164.3 |
| 43c111b2-4377-318a-9e51-8b038cb9cda9 | -18.2147 | -56.5873 | 2024-10-13 01:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.7 |
| 3b26f1fc-a802-39b1-a09a-051581ce00cb | -18.2151 | -56.5665 | 2024-10-13 01:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 131.5 |
| 9da76888-ccd5-3084-926e-22d9bfc3a3f1 | -18.2155 | -56.5457 | 2024-10-13 01:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.6 |
| 684682e0-51a4-371b-964b-99fe0e271f70 | -18.2166 | -56.4832 | 2024-10-13 01:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 139.4 |
| 7b9a68e3-8058-3978-b9d9-3b060e7c2022 | -18.2364 | -56.4806 | 2024-10-13 01:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.9 |
| 5b092990-1f2b-3c67-87cf-267d908e0dc8 | -18.2127 | -56.422798 | 2024-10-13 01:41:23 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3f19c1e7-65fe-3f57-a661-de8dc896e933 | -18.2162 | -56.436401 | 2024-10-13 01:41:23 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8d58d683-130c-3e7c-852a-13314d0419e2 | -18.219601 | -56.450001 | 2024-10-13 01:41:23 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 90ba41ab-ab0c-3c35-be76-4e8982bd846c | -18.223101 | -56.463501 | 2024-10-13 01:41:23 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 04067cc9-5e24-3868-8c36-9d08f194fd26 | -18.202999 | -56.425499 | 2024-10-13 01:41:23 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9a3b0e03-5b95-3a22-864c-3540ef188fe2 | -18.206499 | -56.439098 | 2024-10-13 01:41:23 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 06fdb0dd-e93c-3c12-8d80-7d9b9ac68735 | -18.2099 | -56.452702 | 2024-10-13 01:41:23 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 945d0e5b-e389-34a0-9a20-cf3bf078ab08 | -18.2134 | -56.466202 | 2024-10-13 01:41:23 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 25e96634-eda0-31ca-91e4-18af9eac4fc7 | -18.2169 | -56.479801 | 2024-10-13 01:41:23 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2690a066-d776-3c62-9ec5-7e8bba160c2f | -18.2204 | -56.493301 | 2024-10-13 01:41:23 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bf7349db-f84a-3118-892b-f1756f3f9814 | -18.223801 | -56.506699 | 2024-10-13 01:41:23 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d041c56b-3d91-3018-9aeb-f0df911c2a24 | -18.203699 | -56.468899 | 2024-10-13 01:41:24 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e0834b5d-942a-300b-9f1c-735b33ba0503 | -18.207199 | -56.482498 | 2024-10-13 01:41:24 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4ba3dd66-ffd5-34b0-a5a8-6f58355c4c25 | -18.210699 | -56.495998 | 2024-10-13 01:41:24 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5939c35b-a927-39fe-899d-eef98911a1e7 | -18.207899 | -56.5256 | 2024-10-13 01:41:24 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4438dbf6-f766-3007-a959-32497a262e7c | -18.2113 | -56.539101 | 2024-10-13 01:41:24 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ed261e6a-731c-3574-9afa-1835ca27ff5c | -18.2148 | -56.552399 | 2024-10-13 01:41:24 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ca08dfe1-74ba-3cf6-a25b-f3d9c72bb0b4 | -18.218201 | -56.5658 | 2024-10-13 01:41:24 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ba4869bd-e234-3f85-a4b4-a0a8f3682631 | -18.2017 | -56.541801 | 2024-10-13 01:41:24 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README22.md)
