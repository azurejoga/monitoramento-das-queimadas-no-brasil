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

## Dados Diários - Página 149

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70f97be4-846b-3339-913f-8ac2d6072e81 | -17.8571 | -57.29918 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| f0b4a781-12c9-3475-87fc-ed405da4a663 | -17.85585 | -57.28311 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| e1b8e7b3-0032-3029-a7ec-c4b55d75211a | -17.85534 | -57.28841 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| b139ab4a-7cdf-3dc1-ba7d-710557cf3a4f | -17.85518 | -57.32036 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| de8067c8-fa8b-3f41-b7ca-4d136de36636 | -17.85482 | -57.29372 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 5d2ba4c5-2ba4-36c4-beb6-13105266412f | -17.8547 | -57.32568 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 3591e62e-c2ea-3369-a6ef-139900c8fe27 | -17.85431 | -57.29902 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 41da470d-a2bb-3c32-b530-a592a03c8dcf | -17.8538 | -57.3043 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 1ceefcf6-0e63-3757-a740-3788ba166d78 | -17.85259 | -57.25047 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5760aa7e-0f94-394c-b9fe-7136ace3da44 | -17.85174 | -57.32547 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.9 |
| 23b21e9e-c87e-36b0-80be-e69621ec7d3b | -17.85171 | -57.28786 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| ffc474fb-1175-31e5-a2d2-eb4fd36e5159 | -17.85123 | -57.29319 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| b07cd619-7488-35bf-8bbb-e99b9665a94c | -17.85122 | -57.33076 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.9 |
| 7ca058a1-3b37-3998-8264-48fe364f7a2f | -17.85075 | -57.2985 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 89e91e7e-50fa-3f32-b6a5-727a6b3efca4 | -17.84899 | -57.28776 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| f0089990-007e-3322-bd34-6ee29fe2d9bf | -17.84848 | -57.29307 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 919f6ca2-bc06-37af-a76b-de1e7c874957 | -17.84836 | -57.32499 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 447949f5-4e50-30f0-a518-f210992d65ec | -17.84674 | -57.24451 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| ef10f8a7-6833-36b5-a232-748eef1babd3 | -17.83629 | -57.28646 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| ffdc27a2-c3e2-3c1f-a603-fa3d2aa6e2ee | -17.82892 | -57.29643 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 0b3c6323-975f-352e-8e41-2dd5b7ad3611 | -15.62675 | -59.97933 | 2024-10-12 05:50:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c9f4995-baea-3381-809a-e774e7fdb739 | -4.01303 | -60.38243 | 2024-10-12 06:31:00 | AQUA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a4772637-6919-35fd-a8a9-f4e5a2267569 | -3.05825 | -61.67399 | 2024-10-12 06:31:00 | AQUA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 71711216-277c-3796-8ec7-a320e07817dc | -3.05679 | -61.68397 | 2024-10-12 06:31:00 | AQUA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c2b2fee8-b9d5-3ab8-a060-288a5f145a50 | -3.04886 | -61.67265 | 2024-10-12 06:31:00 | AQUA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4abf65c3-91d6-32c7-a08f-d6775e995351 | -1.93261 | -61.7384 | 2024-10-12 06:31:00 | AQUA_M-M | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0f7c5c44-ea68-3674-92c7-0f922b7e636e | -1.89515 | -54.4216 | 2024-10-12 06:31:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 706bcee8-2a02-3cf2-adb3-c93869b8a6c7 | -9.93356 | -59.90467 | 2024-10-12 06:33:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| cc4f5900-f8d0-3be6-bcdb-c788ec58c5c5 | -9.89465 | -64.80354 | 2024-10-12 06:33:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 81e111c1-e674-32f8-baab-bb6db969d674 | -9.89332 | -64.81253 | 2024-10-12 06:33:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 41877840-5a98-325c-9f08-71e373af6e04 | -9.86181 | -60.28039 | 2024-10-12 06:33:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| db49acff-5da0-30de-8ffd-0ba644e63c9c | -9.86015 | -60.2855 | 2024-10-12 06:33:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 26179795-0bc7-3f71-b8c4-d1c89d67cebc | -9.5931 | -64.09578 | 2024-10-12 06:33:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 584864bf-461d-3c7a-b56d-6871ed468066 | -9.56917 | -64.19585 | 2024-10-12 06:33:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ead3aae7-aa2a-35b3-b344-26c6951d9b47 | -9.36698 | -65.74129 | 2024-10-12 06:33:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 06ada4be-6cde-30ca-a094-3b680b20a25f | -8.97705 | -62.35604 | 2024-10-12 06:33:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 8fcd849e-aeab-35d1-bb25-b55360197fbd | -8.97551 | -62.36691 | 2024-10-12 06:33:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 76f69ad9-8ed6-3d1d-b86e-9590ba37d5f5 | -8.96888 | -62.34382 | 2024-10-12 06:33:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 98a9063d-c2a6-3708-bd6c-41a1d8ed5bce | -8.96734 | -62.35468 | 2024-10-12 06:33:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1118a790-56e7-34fd-acf7-7403a1c0e3c2 | -8.91428 | -62.36265 | 2024-10-12 06:33:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8f611e0a-30e5-36f2-b142-0e524cc44e19 | -8.697 | -63.09217 | 2024-10-12 06:33:00 | AQUA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 732630cb-80eb-31b8-bb18-b999b9a92c4a | -8.66368 | -63.25698 | 2024-10-12 06:33:00 | AQUA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 07d4312f-6720-3341-a5f7-f5f6b6d150d0 | -8.66228 | -63.26667 | 2024-10-12 06:33:00 | AQUA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bbc90c49-e603-3547-a2c0-00302b92d716 | -8.23258 | -61.18619 | 2024-10-12 06:33:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 5c3d98e4-c287-381a-b243-806d3d938d52 | -8.22218 | -61.18478 | 2024-10-12 06:33:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 53cf52a5-b453-3af0-a0f6-456831883234 | -7.87633 | -54.70513 | 2024-10-12 06:33:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 0fab2b59-84d8-369d-bd90-d40c5c9fc122 | -7.59357 | -61.22956 | 2024-10-12 06:33:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cbf4d129-8406-3189-af11-6bddb31aa903 | -7.31152 | -64.67646 | 2024-10-12 06:33:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d147f93e-6a1f-3bce-b501-c33212a49dc2 | -7.30532 | -64.65744 | 2024-10-12 06:33:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| c8551ee9-c311-320b-bbd7-5d7cf64e2392 | -7.304 | -64.6663 | 2024-10-12 06:33:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 34ee6f1f-ef87-3e22-9583-8f71ac191e96 | -6.81923 | -60.12959 | 2024-10-12 06:33:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 11d95b1b-12e8-32ae-aa92-9cc0175bd756 | -6.79974 | -59.35373 | 2024-10-12 06:33:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 3e6f7f91-b623-353d-8b0f-5306ed5d0a21 | -6.76083 | -58.87776 | 2024-10-12 06:33:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a9d650bc-24fe-3f83-a53f-803a1a25cbd2 | -6.76026 | -59.32507 | 2024-10-12 06:33:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 9c21c6fb-b439-3f11-9708-15d3cb824d7b | -6.75624 | -58.87186 | 2024-10-12 06:33:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 98d6be76-adfb-368b-9f37-cbd410591fb7 | -6.74863 | -58.87639 | 2024-10-12 06:33:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c540c3a6-7c2f-3d57-9a40-a20ed9631a7c | -6.74852 | -59.32355 | 2024-10-12 06:33:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 0c6f25e2-39b9-31da-bcfc-74f206c814bb | -6.35686 | -58.1817 | 2024-10-12 06:33:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 34d78439-1579-31f4-a037-7f65294d51e3 | -4.73373 | -60.77844 | 2024-10-12 06:33:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 1a5fee04-65b0-354b-a269-f6530a36c3ae | -4.73126 | -60.78463 | 2024-10-12 06:33:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 31e6d2c2-3c07-3cda-ae12-ac12d9f43d51 | -10.92844 | -60.95656 | 2024-10-12 06:33:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 8b21db04-8f60-39fd-9357-af4936d3e40b | -10.50713 | -62.97753 | 2024-10-12 06:33:00 | AQUA_M-M | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d979157b-3b25-3729-9ba8-cc0b4f67073a | -10.47747 | -61.25211 | 2024-10-12 06:33:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 9f8de2df-5c2f-31c0-9781-bba0f6ab2213 | -10.41592 | -61.26637 | 2024-10-12 06:33:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 5ba9437e-5c99-3e6c-aea7-e1a116a1c31f | -10.41405 | -61.28004 | 2024-10-12 06:33:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 102e6f1a-122c-33ac-ac9f-1c3090cc03a5 | -10.40522 | -61.26498 | 2024-10-12 06:33:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 8a5d0fbe-c4d8-38f2-86eb-eb43b2d59314 | -10.40335 | -61.27879 | 2024-10-12 06:33:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| a1f749b1-e86a-3884-9747-0e87773ed2da | -10.39293 | -61.19395 | 2024-10-12 06:33:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 1b250277-633e-3e3b-90cd-967750403904 | -10.39112 | -61.20745 | 2024-10-12 06:33:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 2f291c40-3d7b-36df-bd93-2273e4542fe9 | -10.37679 | -61.23312 | 2024-10-12 06:33:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 591f82c4-a025-3a3e-afd4-4d7e1cc51726 | -13.74242 | -60.59819 | 2024-10-12 06:35:00 | AQUA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 788a5bd3-f021-33a3-8036-1e528436ea08 | -13.73492 | -60.60752 | 2024-10-12 06:35:00 | AQUA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 63051986-dc4d-3451-8cef-e8bb67c00866 | -13.00644 | -62.47819 | 2024-10-12 06:35:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 08be32e2-4d98-3bf7-a015-dd63b2f83780 | -12.99239 | -62.73117 | 2024-10-12 06:35:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8ddf485b-0b79-3dd3-bf94-7de1eb84051b | -12.9517 | -62.51324 | 2024-10-12 06:35:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 38af79cc-2980-3edf-b3c1-afa561729545 | -12.94909 | -62.51953 | 2024-10-12 06:35:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a4e6df84-6fd9-38bf-ba49-cc21f6205c32 | -12.76917 | -62.27648 | 2024-10-12 06:35:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0e23e794-7455-3994-9893-0019424ae0c5 | -12.7416 | -62.24739 | 2024-10-12 06:35:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 23a3c3d5-f7d9-35b9-8cbf-6a1937a6b713 | -12.48573 | -63.00031 | 2024-10-12 06:35:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ad55833a-08fc-39bb-8465-dd0060f4e51c | -12.4842 | -63.01134 | 2024-10-12 06:35:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0e6475a3-5110-3272-b286-efaefd9dfade | -12.46618 | -62.99755 | 2024-10-12 06:35:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 592957f1-c158-3f15-8b77-8f0561b9e0fc | -11.84605 | -58.83032 | 2024-10-12 06:35:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 8dfa807e-d94d-38bb-9c95-0ecf81af40fe | -11.84332 | -58.85199 | 2024-10-12 06:35:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 9e4c9d7a-65d3-3c12-b29e-fcecaf0ca2a2 | -11.8327 | -58.82904 | 2024-10-12 06:35:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 6487e166-6de5-3e91-937c-629743408d05 | -11.83 | -58.85075 | 2024-10-12 06:35:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 027ff02e-3680-310f-973b-6e9275f09e18 | -11.28898 | -60.48952 | 2024-10-12 06:35:00 | AQUA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 7deead06-4763-383e-9755-416a92b5a8b7 | -11.28682 | -60.50555 | 2024-10-12 06:35:00 | AQUA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 11.6 |
| c02e0c67-0543-3fb3-b691-251097f737fb | -11.17939 | -60.62572 | 2024-10-12 06:35:00 | AQUA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 0756eefc-65ab-3efe-a629-d2d5d7b92d2c | -10.97197 | -63.60118 | 2024-10-12 06:35:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a4f3bf3b-dc00-3c25-bfc5-eda0594dec87 | -10.94249 | -63.87488 | 2024-10-12 06:35:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 48ffed60-da93-39e3-a3f0-0f9643d57418 | -10.92825 | -63.84332 | 2024-10-12 06:35:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| e3516137-a35f-3bd8-a7ff-f4e3d87a4c89 | -10.90027 | -63.92145 | 2024-10-12 06:35:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f7aed1b8-568a-3a40-8df8-2ac345c3e853 | -10.89886 | -63.93113 | 2024-10-12 06:35:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 98d63ca4-8124-3037-82c0-a2543c627938 | -10.86644 | -63.89686 | 2024-10-12 06:35:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c86954e4-3cc2-3ed0-b8a5-3a979167c27b | -10.86505 | -63.90656 | 2024-10-12 06:35:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 23.4 |
| c3c7d660-f154-3ab0-bd0d-893f11ee4ebd | -10.86422 | -62.31723 | 2024-10-12 06:35:00 | AQUA_M-M | TEIXEIRÓPOLIS | RONDÔNIA | Brasil | 1101559 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| dd5ca78f-dfbb-34a1-ba45-25da393246d8 | -10.86248 | -62.32352 | 2024-10-12 06:35:00 | AQUA_M-M | TEIXEIRÓPOLIS | RONDÔNIA | Brasil | 1101559 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 54c513e0-3cf6-3378-bf84-c4aad0ca9f22 | -10.83575 | -64.17363 | 2024-10-12 06:35:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8d53eac6-bedf-35dd-aa92-3529a01655d2 | -10.70586 | -64.11051 | 2024-10-12 06:35:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 68f8e69a-1ec4-3443-a5b6-82c60ac6b664 | -10.7045 | -64.11994 | 2024-10-12 06:35:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |


[Clique aqui para ver as próximas entradas](README150.md)
