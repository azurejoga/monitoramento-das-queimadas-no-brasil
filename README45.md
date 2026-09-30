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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7fe6a24-b004-306f-bddb-89e95606b285 | -17.10123 | -46.47101 | 2026-09-30 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7722dc38-404b-37e0-aa0f-f2f72ecec1aa | -10.8341 | -48.71611 | 2026-09-30 04:53:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4964928-362e-3700-8a28-d74aee71b495 | -7.02277 | -45.29986 | 2026-09-30 04:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3daca663-c9f9-3e75-9187-d54cc4be6225 | -8.06148 | -61.27347 | 2026-09-30 04:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d717afae-10c7-3af8-9496-89d05f4c4b8b | -5.09613 | -46.04273 | 2026-09-30 04:53:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 28ef6c28-dad7-3d7f-b177-cf8bc88d06d9 | -9.99178 | -50.26721 | 2026-09-30 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7223a227-a5fa-3959-a7eb-ed534550a464 | -5.09485 | -46.03903 | 2026-09-30 04:53:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ade357c9-292a-3d15-9dd5-8e9ad26f0992 | -10.41911 | -53.7716 | 2026-09-30 04:53:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5f88b91-24f0-306b-8655-f397ccc319fd | -4.02818 | -54.2008 | 2026-09-30 04:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 23659346-8314-3bb0-bd0f-df97e1d83857 | -3.96788 | -48.00433 | 2026-09-30 04:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11093913-0cbe-3eed-bab7-fb5747346874 | -6.1062 | -55.70525 | 2026-09-30 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af8172a7-14e7-32b3-a6ea-231a0167cecc | -9.07213 | -49.86928 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b7bfeb5-4aaa-3095-a0af-5d89a0860bac | -3.01389 | -54.22658 | 2026-09-30 04:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 003bf481-1a1c-368e-9991-4f82511484cd | -4.02512 | -54.20221 | 2026-09-30 04:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4be00007-844b-3546-9217-a5f0a847a628 | -11.17026 | -44.82506 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 8a335557-49fc-396f-abdc-53ed1697bfb2 | -3.56532 | -50.25469 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b0afa0d-b5a7-3c54-b039-0d70456fcaef | -11.26258 | -43.52902 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d5d9050-77f6-324a-85f5-25bf6bb883c6 | -14.50253 | -48.28273 | 2026-09-30 04:53:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01eff945-c8fc-3756-b63d-138fca4a1db8 | -14.89942 | -51.86901 | 2026-09-30 04:53:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4fa93ed9-40d5-3494-8a95-2f012666cc0d | -8.11857 | -54.85207 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b6a5690-998f-3844-a942-510ffeee11e5 | -7.43013 | -64.34813 | 2026-09-30 04:53:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c04a4ba0-263a-3f8b-a349-cbb368b65977 | -7.02811 | -44.62686 | 2026-09-30 04:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ee67194-a320-38df-b2fb-3e773ff7400a | -3.00641 | -54.22541 | 2026-09-30 04:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d7cc5000-8621-32f3-9215-673c9a7dc2f0 | -7.56078 | -55.02995 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2e7a0b46-e492-3354-b757-db6b7e3c4957 | -17.12337 | -52.13577 | 2026-09-30 04:53:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ec47423-0d56-3e14-a374-1b33f5f15872 | -6.07011 | -44.87536 | 2026-09-30 04:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b995793-2d50-34a8-a1f4-c770645028d9 | -17.91497 | -44.40473 | 2026-09-30 04:53:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a237915e-6c97-3521-8ab5-e62975277e49 | -3.7096 | -51.33758 | 2026-09-30 04:53:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd69b072-c38e-339b-9d6d-d43e316a0605 | -9.15976 | -51.52426 | 2026-09-30 04:53:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24485b39-32a5-3737-9463-15b935cfd72f | -9.93565 | -50.15193 | 2026-09-30 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 96be7f70-0236-3ca5-af89-70b5b4add970 | -8.94063 | -49.79215 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 84b9fbb7-82d1-3181-b160-54794e3624b0 | -11.38465 | -43.37363 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5f95b505-8a77-32d7-b519-82990d5a2622 | -4.02371 | -54.21104 | 2026-09-30 04:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40ad4656-922a-3d06-865c-5a56bd0b6af6 | -4.06153 | -50.42461 | 2026-09-30 04:53:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c082610c-28a4-3087-bc1a-4bc1e6eadbaf | -5.74141 | -45.05951 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d2ec809-6082-3353-8247-1f58857bb7c1 | -5.18263 | -48.26546 | 2026-09-30 04:53:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9ae6e99-9092-3e5d-b81b-6e1156dc8233 | -10.94805 | -47.27821 | 2026-09-30 04:53:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 69acd057-5069-3cbf-9342-602643a2533e | -5.73918 | -45.16249 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f1108fd9-d7db-3ee1-bcd8-aba2d565dd7f | -6.12502 | -53.27705 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1c351046-90a8-3af2-a855-eb0d1b8408c6 | -18.07709 | -44.36762 | 2026-09-30 04:53:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1470b310-dd2c-33fb-b2e5-91ed158218ba | -3.60961 | -48.91304 | 2026-09-30 04:53:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e0a922da-4fd7-385f-bd26-b72dde9e7635 | -3.37409 | -50.94777 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 101616e8-9f9d-3278-9519-f4b6a677018b | -8.31828 | -54.75833 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71c4a6f3-f059-3444-bcc8-4595a25e31f7 | -2.27395 | -57.01923 | 2026-09-30 04:53:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90c0c7ec-a293-3e8a-8aec-6c81c909642b | -8.1215 | -54.85689 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ace2f96a-96d1-3ce3-8ea7-6217dd1a8b1f | -7.1722 | -55.40938 | 2026-09-30 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bab539cb-7041-3807-87a3-7d595e26642b | -3.37576 | -50.95864 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 03747646-bb90-36fc-8ca8-2ca55a2533e8 | -6.13867 | -53.06075 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43addbee-a9c7-3949-969d-5d0f5bc26492 | -11.25571 | -43.541 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 06ac92e7-618a-338e-bf48-49769361339d | -3.15729 | -54.08062 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cdecf6bb-4c5d-3672-8401-aa6ceb2088f2 | -10.95206 | -47.2788 | 2026-09-30 04:53:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 710b8942-2ff5-36d1-a7b8-43a13683e223 | -2.75087 | -54.674 | 2026-09-30 04:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f45dbe22-a652-32a3-8f96-d431f20bd21f | -3.37464 | -50.94431 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c9cbf341-c3a8-3450-8352-07103b8c0ff1 | -7.49552 | -55.59052 | 2026-09-30 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ce4ccfe-b3d5-3677-87d3-0170a5bb2f4c | -3.56863 | -50.25521 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0bab9f2f-795b-3620-9f3c-92978f1adc44 | -6.10188 | -53.09294 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4f9003de-216f-3ae9-8d58-f3a582905fa6 | -7.93343 | -47.36786 | 2026-09-30 04:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1b5f7c1-5e2b-3841-b39a-57982d5786f9 | -7.53657 | -47.12312 | 2026-09-30 04:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| decb0d62-807b-30f5-a4b4-87206c0302e5 | -15.11017 | -54.71491 | 2026-09-30 04:53:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 230db0fe-2bed-3259-ba65-1940b1fb9710 | -6.30293 | -43.60587 | 2026-09-30 04:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8757c9d6-eedb-32f3-8e85-75fd7bf43d9c | -7.49084 | -54.9738 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93763255-7067-38ea-bbce-7104988dc780 | -7.80336 | -49.85641 | 2026-09-30 04:53:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4149dd5-86cc-36f7-bc52-b74472225e99 | -11.25964 | -43.55112 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da51fd88-8e45-39c9-9005-69732de4b33e | -9.1704 | -60.79406 | 2026-09-30 04:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3c03455-e636-3c50-b1ef-582e058dfa01 | -6.29524 | -43.65818 | 2026-09-30 04:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 60f25fa4-329a-35ea-9b1c-6bf34cecc6ec | -9.08357 | -49.88639 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56ceffe5-f158-3261-8ce8-eb123492a4a3 | -3.24956 | -50.81119 | 2026-09-30 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 7119d604-944d-36cb-a00c-64fbe8dedec6 | -8.11788 | -54.85628 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8f37b1d2-8ff1-3e29-a5e7-6754935bc4a0 | -6.12961 | -53.05169 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 846546af-9791-3b1f-90b5-473a8db51321 | -10.49349 | -49.27882 | 2026-09-30 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82b2aa25-a1ca-3459-9bcc-83419c3edefb | -10.72196 | -44.4307 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7b1beaf2-ea4d-3be0-b62a-cc9c1389829c | -14.90279 | -51.86955 | 2026-09-30 04:53:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6488c73b-ee83-3bf7-92e2-35350adf5aba | -4.3043 | -48.61298 | 2026-09-30 04:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d546ba8b-2d66-34bf-b1f7-7829ef82f2df | -7.82097 | -45.82874 | 2026-09-30 04:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c5340969-f095-360a-aae8-f68647fba2a3 | -3.18158 | -51.24004 | 2026-09-30 04:53:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9fa2cc03-f5f1-3584-a138-6dd574b38bc4 | -5.72945 | -45.1691 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 49c11595-afd8-334c-8b21-ef998f2e75eb | -6.1053 | -53.0935 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e95fdc98-6410-38ec-b894-7daabbb6b976 | -7.83932 | -45.82337 | 2026-09-30 04:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b26094ae-aa5f-35af-913a-70ec4aee8ed6 | -6.10872 | -53.09405 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8762deae-cd14-33e9-a2f2-b7da2d9095e8 | -11.40598 | -43.41629 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8739b92e-3847-3e2f-b6b2-b171ac4fbe79 | -6.71812 | -45.57836 | 2026-09-30 04:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a46f0a79-4ca7-3709-8ddf-19786c8f4bcf | -15.75797 | -46.03894 | 2026-09-30 04:53:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 08dae778-6ae9-3fb6-b9e3-26486899fdf6 | -17.12394 | -52.13202 | 2026-09-30 04:53:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d46427e-50b5-3b59-8386-0b9a3d314d17 | -3.82707 | -55.90792 | 2026-09-30 04:53:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0842d07-7afe-3cef-a86b-d8860457dfa6 | -9.93223 | -50.1514 | 2026-09-30 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 734bee8c-4b53-30de-8c71-9ec23134fc73 | -10.6686 | -50.74237 | 2026-09-30 04:53:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe343d6e-b171-3b44-80f4-8c1de31ed0f6 | -9.19632 | -49.63265 | 2026-09-30 04:53:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49257a92-8d8d-39c3-81de-0a5ba48111de | -10.7624 | -52.12862 | 2026-09-30 04:53:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8747ef69-c049-3431-ae58-b26c82bb4cde | -8.27617 | -54.73561 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c58f6f1e-46b2-396a-9d3e-1ab7e287b0bb | -5.32557 | -46.20079 | 2026-09-30 04:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 984b2b53-fa4d-3c3f-b4c3-06184640489a | -11.43976 | -43.4438 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19f53a0b-1cd0-37b3-af8d-a4b244d30e5b | -10.703 | -50.83344 | 2026-09-30 04:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28f287e4-1237-31d1-9131-507aa55f8f02 | -10.08144 | -50.31907 | 2026-09-30 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6485aa5-692c-3d51-b199-74636a5dcbdc | -9.15921 | -51.52774 | 2026-09-30 04:53:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be20b269-bec6-351b-b181-ac6b7bcdb3a9 | -7.09711 | -46.45604 | 2026-09-30 04:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aba0a9fd-bc01-32f6-914b-36a70aaad506 | -9.37809 | -49.15458 | 2026-09-30 04:53:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 469641f7-a576-357b-b797-320cb0967b80 | -4.02888 | -54.19654 | 2026-09-30 04:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 023a275c-235c-3783-af5c-d9bbd70f3fe6 | -7.71695 | -54.78616 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37be83ce-7464-3eff-a2eb-b03395788a61 | -3.15082 | -54.0974 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73aa1e56-dd91-3a4d-9ab4-27f2308a3c51 | -5.75836 | -45.17252 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README46.md)
