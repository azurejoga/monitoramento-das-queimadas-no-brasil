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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18e5b1a0-e277-30c2-b7fa-5cea9ca1ef30 | -3.50466 | -53.45594 | 2025-10-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b19f63c6-a3ff-3ae8-bde5-3fa9c0eec997 | -3.45389 | -53.83145 | 2025-10-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e731a75c-4ef3-3e7f-b481-27dd0ad907d1 | -3.5407 | -51.15334 | 2025-10-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a50a72f-7090-38f1-89d6-98aa89ba2cbb | -3.10192 | -47.00865 | 2025-10-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ca3355ab-f937-314b-9f3c-0a754cc2249f | -3.49806 | -52.46973 | 2025-10-01 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1ba2cdc7-0268-3a0b-9416-56b4b6692c4a | -4.33328 | -50.85535 | 2025-10-01 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c7d09c0-cafd-3969-8d71-11fe08c4137e | -2.24706 | -47.89098 | 2025-10-01 05:08:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9e328df1-974c-344b-859d-d0d5ff873d92 | -3.0959 | -47.01135 | 2025-10-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2e33cd06-e2dc-3a67-bd76-12584c41aa9f | -4.37217 | -55.8911 | 2025-10-01 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab578e34-4b63-38aa-b051-75617a585b69 | -3.45864 | -50.09137 | 2025-10-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e6f20b2b-dca9-31d1-952b-38a05586f39d | -0.90553 | -47.54627 | 2025-10-01 05:08:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4dd81acd-455f-38a8-a66f-7a6ef4f3d863 | -5.94741 | -45.83691 | 2025-10-01 05:08:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a67e6ee0-922d-3fda-9fa2-632e315888d3 | -3.4689 | -50.08383 | 2025-10-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| caead739-bed6-3394-8414-13455d378fc3 | -2.24753 | -47.88799 | 2025-10-01 05:08:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| abf8c3bf-d1aa-3b76-aa65-37423f145a8d | -3.84691 | -48.96085 | 2025-10-01 05:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 33da52bf-16cb-3481-94dc-94e6f681cc9a | -3.42067 | -51.23055 | 2025-10-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef484d66-afd7-33f9-8528-b1ee006c6ed8 | -5.61757 | -43.23049 | 2025-10-01 05:08:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f4f68c5d-0312-38e6-bbb8-39886da3a7db | -3.09429 | -47.02204 | 2025-10-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7df4c8a0-c312-3be6-9d6b-e24b2c5539d2 | -3.49382 | -52.46616 | 2025-10-01 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ee14f8be-0e1a-3db7-b1d5-f9fd97f81868 | -3.1074 | -47.00945 | 2025-10-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c7d6291d-5a2e-3f04-aab7-1348e31eb7bf | -2.6983 | -54.76642 | 2025-10-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b590f3e4-3b90-3298-a599-a595dc35b10a | -0.90817 | -47.54579 | 2025-10-01 05:08:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1950baaf-8750-3510-bbb6-f463bd75b1c1 | -2.06959 | -56.87791 | 2025-10-01 05:08:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 00fed4aa-0092-37fb-abe4-76112db5c292 | -3.08936 | -47.01758 | 2025-10-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 8e5064a8-91ab-3d6f-aa4a-d448177a9151 | -3.09537 | -47.01492 | 2025-10-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 0c3ce418-ec14-3752-9464-4f433062da86 | -2.0729 | -56.87844 | 2025-10-01 05:08:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ddb7898-b8df-33de-b119-640bffd56817 | -3.55317 | -50.32993 | 2025-10-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2794743a-8ab0-3fb7-a357-069f2356a448 | -0.90307 | -47.54494 | 2025-10-01 05:08:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a9955e7-c8e5-3270-9d7e-cfc0c45172d4 | -6.28439 | -43.66379 | 2025-10-01 05:08:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b02b342a-da5a-389a-9b8f-91391005d9f5 | -5.63705 | -43.91777 | 2025-10-01 05:08:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 59caf88f-8099-332e-a13b-f6a71ed71f79 | -3.23982 | -52.89175 | 2025-10-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52134808-cc79-3454-8041-c2b1c178ce14 | -2.27171 | -47.85285 | 2025-10-01 05:08:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 44980e49-0ff2-3674-9a3c-b12b113980cd | -2.59494 | -48.12203 | 2025-10-01 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 113b78c8-f61a-3118-b77d-53da0a6bb118 | -5.85608 | -43.39937 | 2025-10-01 05:08:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 876f8525-56d7-3b9b-a8c9-cc240da3f2b1 | -3.82924 | -52.04582 | 2025-10-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c4430cc-c985-3bc5-9e1d-1ad6368916e8 | -4.63661 | -47.02109 | 2025-10-01 05:08:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 468ffc7c-90e6-346f-a0cc-3e5535d47068 | -2.82289 | -54.03204 | 2025-10-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd909d19-f3b5-36a2-beb0-27ea28a6cd76 | -4.39855 | -50.84805 | 2025-10-01 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| fc03e39b-0c60-3d40-bfde-da4579b72861 | -4.2592 | -48.55797 | 2025-10-01 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ef754f2-fc35-356a-9144-598378fd83e5 | -4.68586 | -50.48108 | 2025-10-01 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a5d7a85-fc95-364a-95da-ab873d1a3437 | -2.2454 | -47.88923 | 2025-10-01 05:08:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6c9d2ec8-1623-3570-a6b7-1aea22e9cc13 | -5.63012 | -43.917 | 2025-10-01 05:08:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| ab70b68b-c4ca-3ead-ba04-5d7c136de23a | -3.09483 | -47.01848 | 2025-10-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| d9684cb9-aade-3560-97cd-c5db5d7f38ba | -4.25962 | -48.55513 | 2025-10-01 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 405d38c9-6107-3b62-9f5f-8c7ffc14e828 | -1.33093 | -47.57471 | 2025-10-01 05:08:00 | NOAA-20 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 193f46b3-9cc5-3958-a20c-538f56e35af4 | -4.08781 | -54.91342 | 2025-10-01 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ec2c9228-1061-337d-a98e-bfda3ef43643 | -5.24511 | -52.03727 | 2025-10-01 05:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7c18a707-32c9-39ee-bab9-8f15e4b90fc2 | -5.80171 | -43.74244 | 2025-10-01 05:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d5b2dd5f-8a61-35b1-a989-e1b193026b7d | -3.05264 | -51.10093 | 2025-10-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c18ec49-567b-34f7-9e34-1cbe2b24d969 | -3.27157 | -52.50628 | 2025-10-01 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 488eaf4b-3797-3446-95c3-f4549c3d6adb | -4.66715 | -45.68677 | 2025-10-01 05:08:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8caaac80-62d2-3211-b5fa-fe1676dd07b1 | -4.63608 | -47.02485 | 2025-10-01 05:08:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dcb8a14a-e5bb-3b08-b58c-9eae80a9da65 | -4.25374 | -48.56018 | 2025-10-01 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d0aa8ab-33f6-355b-8a4c-4b004e7898a1 | -5.61658 | -43.23781 | 2025-10-01 05:08:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7a0b3bc0-cb18-38cd-8f2e-25d62589a09e | -3.78063 | -51.29063 | 2025-10-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bafe8b0b-b67f-332d-9263-82e0a0c7bf47 | -3.091 | -47.00667 | 2025-10-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 16cf2ca5-73a5-3723-a2dd-96025b7929e4 | -1.33359 | -47.57747 | 2025-10-01 05:08:00 | NOAA-20 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1e1380b-e9aa-3a13-a60f-e8d33dd6de97 | -5.80177 | -43.73357 | 2025-10-01 05:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b9514b4b-9bd3-31bc-8369-66b766ae597e | -4.31192 | -48.09476 | 2025-10-01 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b013bea4-a23b-3e55-bf51-1681ae3fbfb0 | -5.63615 | -43.92435 | 2025-10-01 05:08:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 3c4bc0d7-f8c8-3625-a382-5cb5b3f6b080 | -2.5899 | -48.12123 | 2025-10-01 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 602d4ca1-a6db-3ab2-bcac-8a40501a8bd1 | -3.10084 | -47.01577 | 2025-10-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 63b826c1-83b3-3c44-b985-f0dc95ae1809 | -4.63793 | -47.02576 | 2025-10-01 05:08:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27f6a107-2020-3acd-b8d9-c5e0cac908aa | 1.2914 | -51.24955 | 2025-10-01 05:08:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22e5a139-4923-35f9-8c34-f9aa22a36412 | -3.49764 | -52.46677 | 2025-10-01 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| de019a43-2cc4-3ff2-a06a-d04242b50f2a | -3.49498 | -52.46441 | 2025-10-01 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8375df7e-5dc6-336c-8183-15466a0b128c | -5.64312 | -43.92479 | 2025-10-01 05:08:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| b588c3cf-ed84-3eec-9786-aacd62f14eb6 | -2.89102 | -47.84226 | 2025-10-01 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8fa026c0-0169-39dc-91d5-6ac8bc7b81fa | -4.67256 | -45.69251 | 2025-10-01 05:08:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da69c94d-6200-3edf-ae04-515c01e268cd | -5.8521 | -43.40355 | 2025-10-01 05:08:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 2b949364-2850-322e-b0db-3c07883253ef | 1.16509 | -60.672 | 2025-10-01 05:08:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a4ad974-037b-3018-9095-3c8405e381c0 | -3.89307 | -52.2847 | 2025-10-01 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95ddcbf2-d252-38ab-9e63-c1e687a739f6 | -4.4034 | -50.84489 | 2025-10-01 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bd4ca95b-1542-3b90-a78a-c2732712e7f4 | -3.04795 | -51.10406 | 2025-10-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7810c235-be23-310a-8d59-2f7731e6e382 | -3.0899 | -47.01397 | 2025-10-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 96b08488-c7e3-39d0-bfed-21b070c837e1 | -3.49425 | -52.46912 | 2025-10-01 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d3eaea35-a379-301c-bdfa-fee4f207ba29 | -2.59539 | -48.11912 | 2025-10-01 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 628603a3-1d38-32f2-890d-108dbe89a92a | -2.5945 | -48.12495 | 2025-10-01 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4e16eec5-379f-3cce-a4be-e364d755ea62 | -2.26658 | -47.85213 | 2025-10-01 05:08:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ca7bacd1-a8db-3657-9d9f-53963552a3b2 | -1.6258 | -47.05645 | 2025-10-01 05:08:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 80bdff14-6f6a-3cb4-8c98-970e831cf6a8 | -5.80791 | -43.74102 | 2025-10-01 05:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3a842ecc-e9bd-3613-89d4-564a77856119 | -2.89057 | -47.84534 | 2025-10-01 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1cfa6fd5-78a2-3ffa-ab6e-5cca987164c3 | -3.5191 | -49.44296 | 2025-10-01 05:08:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 93d0a9d4-2b95-3388-b9b3-508834a7837e | -0.90259 | -47.54792 | 2025-10-01 05:08:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b4d4633-b2eb-31f8-b704-fd13e71953ad | -4.39913 | -50.84405 | 2025-10-01 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 981e38ac-475d-34dd-9113-0dd9f3c25d49 | -2.2505 | -47.88996 | 2025-10-01 05:08:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a00cef97-b15a-373d-a774-15d9d079aaad | -3.49834 | -52.46205 | 2025-10-01 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 86b194e5-f702-3704-ba13-18d5d01e4fef | -3.51834 | -49.44788 | 2025-10-01 05:08:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 54925012-7a98-33d4-a027-03de2d1cd5c3 | -3.10686 | -47.01303 | 2025-10-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 175d43d8-2e88-3a02-9bc7-7ac36163c634 | -4.25499 | -48.55168 | 2025-10-01 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99a7d655-f633-3590-9e8c-9184f1e66d1f | -2.69491 | -54.76588 | 2025-10-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 94922baf-ef02-358f-a546-5d61436632e7 | -4.63233 | -47.02491 | 2025-10-01 05:08:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 725b6f2e-d08a-33ca-a471-23ebe26eb923 | -5.2411 | -52.03665 | 2025-10-01 05:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75d5ecf7-cd6e-346a-a99b-fd0d804666c2 | -3.52145 | -49.44601 | 2025-10-01 05:08:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 55d5194d-6002-375c-af9d-6916b9fe2296 | -2.69095 | -54.76897 | 2025-10-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9b89899e-fcac-3af8-b6da-efa3f537e21f | -3.82531 | -52.04525 | 2025-10-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0091e65-0179-3459-8d7c-97b451c8a008 | -3.09977 | -47.02287 | 2025-10-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b07f8a6-dfba-32a2-a035-5c55cb9439f0 | -3.09045 | -47.01032 | 2025-10-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b92ab0fe-4de4-3dc6-92d4-401cd7fd98d3 | -3.89382 | -52.27977 | 2025-10-01 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc849760-ebb9-30aa-b81d-1fa7efc63f9e | -3.46689 | -50.09723 | 2025-10-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |


[Clique aqui para ver as próximas entradas](README120.md)
