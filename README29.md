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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2bab9061-b7bc-38f3-8227-49f5cea6d580 | -15.4216 | -53.9073 | 2025-08-11 06:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 48.2 |
| f6101adf-7be4-38ef-92d7-64c388e8a89e | -8.9399 | -60.7481 | 2025-08-11 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| a9be8772-899a-3fea-bd76-d5107b094a45 | -15.4407 | -53.9258 | 2025-08-11 06:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| eda594bb-1b60-371f-9b7e-e60c72d5d3ac | -7.0614 | -59.1972 | 2025-08-11 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 72972fb2-0af7-31c0-9fd6-2c1e4b2477e4 | -15.4216 | -53.9073 | 2025-08-11 06:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 53.5 |
| eae8baab-8d3f-3fe5-803e-07a24d65d853 | -15.441 | -53.9048 | 2025-08-11 06:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 33f3a241-1b70-3f8e-8023-522b4519d0d2 | -7.0799 | -59.1964 | 2025-08-11 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 365b9d36-38f4-3dc1-9a9f-24b0a6f20a4e | -6.5856 | -44.564 | 2025-08-11 06:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| a232b38f-4156-3c45-9fbf-e3d02c1b362e | -8.9401 | -60.7288 | 2025-08-11 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| ac67c552-6bf8-3a0f-9537-22894aaa660d | -15.4212 | -53.9283 | 2025-08-11 06:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 17b09f8e-ac36-3724-9174-4b895ea9d153 | -7.25343 | -59.99363 | 2025-08-11 06:44:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 799a3c20-9de5-36f1-af56-bc78b5aed2b8 | -8.57026 | -54.70479 | 2025-08-11 06:44:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 8064948c-b8dd-3a6d-b859-6ac7a56105a8 | -8.93435 | -60.74764 | 2025-08-11 06:44:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 3af89c16-cbc2-3f38-adf3-1072b83f466d | -8.9269 | -60.73745 | 2025-08-11 06:44:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d08b96d5-56c2-3031-a341-62557116dd33 | -9.37974 | -61.52224 | 2025-08-11 06:44:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| f34d9150-44bf-3de6-8718-7eb2b31563d3 | -7.05995 | -59.19635 | 2025-08-11 06:44:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 95a979de-88a1-38fe-aa26-efa984b7ff1d | -6.10166 | -59.9193 | 2025-08-11 06:44:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3f6f427c-c17b-3282-8b48-437a51b8efd6 | -9.36942 | -61.52999 | 2025-08-11 06:44:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ff17ad42-34c8-3e1d-b3c2-f9719f1d4188 | -8.92824 | -60.72859 | 2025-08-11 06:44:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.8 |
| b57e029c-9ea7-3a1e-802d-0ac34efb3a31 | -8.57262 | -54.68757 | 2025-08-11 06:44:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 66fb6add-5b5b-3009-b4dd-495fb0d7e00f | -8.93301 | -60.75651 | 2025-08-11 06:44:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4078536c-6ca4-3182-b194-9c3ea9fc3b2c | -7.06881 | -59.19763 | 2025-08-11 06:44:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.3 |
| a6239118-4b36-35bf-b1d5-470b01bdffde | -8.93704 | -60.72992 | 2025-08-11 06:44:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 2475d225-c34e-3213-9946-5a59df9eb6ff | -7.05863 | -59.20527 | 2025-08-11 06:44:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 57fd0b7f-cfc4-3b06-8877-09f81e968405 | -7.06748 | -59.20655 | 2025-08-11 06:44:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.5 |
| a719763b-6676-39a6-b532-812d1302e062 | -8.55831 | -54.7032 | 2025-08-11 06:44:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 2e326e3e-6233-3889-9134-1623ad31daa2 | -8.9357 | -60.73878 | 2025-08-11 06:44:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 671a2b33-0c6c-3d10-95ea-1f65dcacede2 | -8.92421 | -60.75518 | 2025-08-11 06:44:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 069e9254-ffda-3599-916e-94e7fc2346e4 | -9.37083 | -61.52088 | 2025-08-11 06:44:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 6657240c-e54a-3e29-859e-9b4b01b0bff0 | -9.37833 | -61.53136 | 2025-08-11 06:44:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 25.3 |
| cca3a04d-8e56-3b19-ab56-911337ae37f3 | -7.07767 | -59.1989 | 2025-08-11 06:44:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| f5534bf2-c764-3216-8fd3-ca676df1132b | -8.56066 | -54.68596 | 2025-08-11 06:44:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 94c7a8ba-26a7-3833-9377-a33aab1181e8 | -15.42046 | -53.90451 | 2025-08-11 06:46:00 | AQUA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 5d0659a6-2520-3ff4-9fd8-58b78131955c | -15.4389 | -53.91164 | 2025-08-11 06:46:00 | AQUA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 11340a90-5a0a-3e27-b1e4-335bc3ed035c | -15.42466 | -53.90982 | 2025-08-11 06:46:00 | AQUA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 2bb982ba-62e5-384b-8751-25b322914c89 | -15.43167 | -53.93222 | 2025-08-11 06:46:00 | AQUA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 36.2 |
| bd863190-58a7-3cd6-bbc6-3b16d921cae4 | -15.4347 | -53.9063 | 2025-08-11 06:46:00 | AQUA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 6cef1f5f-52a0-3a2a-a783-b0593bd8a845 | -8.9401 | -60.7288 | 2025-08-11 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 0fb515ac-6dc2-3c0f-9a15-0ddf356d1624 | -15.4407 | -53.9258 | 2025-08-11 06:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 83bb4ad6-f913-346d-aca3-e00d1d340d4b | -7.0799 | -59.1964 | 2025-08-11 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| febc284e-344b-3b38-8bef-c10ec92e1e3d | -15.4216 | -53.9073 | 2025-08-11 06:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 7f988139-d7b7-3af6-aa33-f3e716127039 | -6.5856 | -44.564 | 2025-08-11 06:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 94242806-0648-3956-bf9f-7cc7ec030c44 | -15.4212 | -53.9283 | 2025-08-11 07:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 48.1 |
| d1d53e5c-4155-3463-8f67-7c1fd4960e0f | -8.9401 | -60.7288 | 2025-08-11 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.8 |
| fbf654d6-f264-3d17-a38e-96a7f91dd755 | -6.5856 | -44.564 | 2025-08-11 07:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 13746b4c-58e5-3aa2-a9ab-f788add0e82e | -15.441 | -53.9048 | 2025-08-11 07:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 1b4d904a-14a1-3c71-a3f1-7ec411d17c9e | -15.4407 | -53.9258 | 2025-08-11 07:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| fa48a020-1d62-37bd-91d1-f437d269a712 | -15.4216 | -53.9073 | 2025-08-11 07:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 620f398f-7089-368e-bf28-3933ddc2caa2 | -6.5856 | -44.564 | 2025-08-11 07:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 4fc6820e-ac38-3d77-9dd6-258bcf6bf756 | -7.0799 | -59.1964 | 2025-08-11 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 9d28c3a6-5a28-3a63-a692-aa5565ccb517 | -6.5856 | -44.564 | 2025-08-11 07:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| ac663df6-5cbe-3718-9264-50f03c493382 | -7.0799 | -59.1964 | 2025-08-11 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 9d04cc1f-d0a0-3843-ae04-45319abde34a | -15.4216 | -53.9073 | 2025-08-11 07:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 821a4717-bf33-34dd-875a-a987eed23fbc | -15.4212 | -53.9283 | 2025-08-11 07:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 39.4 |
| b360d1b1-f330-37ee-a6cd-ee3f6365f6cc | -15.4407 | -53.9258 | 2025-08-11 07:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 57.1 |
| bacf9539-e3f1-3494-91c2-da3a5b554e62 | -6.5856 | -44.564 | 2025-08-11 07:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| e718570c-72b6-34f6-bc79-b9d8a0062e01 | -7.0799 | -59.1964 | 2025-08-11 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 7b221083-dec9-349d-8f70-c381e75726c4 | -6.5668 | -44.5655 | 2025-08-11 07:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| e5aaf301-c630-3b87-ab94-9a2420a0d6c4 | -6.5856 | -44.564 | 2025-08-11 07:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 9c15611c-21dd-3fe8-88ac-b513ce4f3e4f | -7.0799 | -59.1964 | 2025-08-11 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 511ae53e-47d4-3876-9151-5eb48d9c3756 | -6.5856 | -44.564 | 2025-08-11 07:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 2864ba6b-e5c5-34d6-9b89-e058fe127391 | -7.4752 | -43.9536 | 2025-08-11 07:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| da411734-b3eb-3e9f-b8c0-2fe6a18017c2 | -6.5668 | -44.5655 | 2025-08-11 07:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| e1c85bce-614e-3d62-8d42-8a9684041a3b | -6.5856 | -44.564 | 2025-08-11 08:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 4acd0737-f67d-3e6c-b810-7ec9c03687c0 | -7.0799 | -59.1964 | 2025-08-11 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 88e3ade9-8ed3-3cbc-8cec-0cf46aaa80e9 | -7.4564 | -43.9554 | 2025-08-11 08:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 6713f1d6-1672-35fd-8fd9-a0daecb813ec | -7.4752 | -43.9536 | 2025-08-11 08:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 057a1baa-2857-3519-91ea-b82131573753 | -6.5856 | -44.564 | 2025-08-11 08:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 124.3 |
| f1d535ae-ed56-3230-bb90-3f44e53ea3bb | -9.3806 | -61.5315 | 2025-08-11 08:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.8 |
| de97e4f3-e9cf-347c-82a4-9062cb229da0 | -15.4216 | -53.9073 | 2025-08-11 08:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 051ca4e0-4f69-3dde-9d0e-a6d29b6b7026 | -15.4407 | -53.9258 | 2025-08-11 08:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 8fb7c1b8-762d-3377-befa-0513ba3fbdb0 | -6.5856 | -44.564 | 2025-08-11 08:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 117.2 |
| e6be0d41-794b-39fc-8b37-8247d0577370 | -6.5858 | -44.541 | 2025-08-11 08:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 6db46220-9408-3227-bc93-86063b8349df | -15.4216 | -53.9073 | 2025-08-11 08:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 6c710243-8cc4-32fb-af7c-b75e23b09100 | -9.3806 | -61.5315 | 2025-08-11 08:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| fbde7b3d-79d4-3562-997b-02187721d641 | -6.5856 | -44.564 | 2025-08-11 08:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 75ffae01-5779-30c3-93da-aa2aabdc4810 | -9.3806 | -61.5315 | 2025-08-11 08:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 6eb463f8-5a0c-3058-bb89-53c787656f18 | -9.3806 | -61.5315 | 2025-08-11 08:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 32c61d15-30fa-35cd-979c-4531b9070cbb | -9.3806 | -61.5315 | 2025-08-11 09:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.6 |
| e9bd81da-7082-3c63-a055-8aba87f14f07 | -9.3806 | -61.5315 | 2025-08-11 09:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| f87af846-e172-3da6-9b0e-5dac229e2965 | -6.5856 | -44.564 | 2025-08-11 09:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 116.8 |
| ea5501a5-9e57-3eb5-9a5d-300cc5161ddc | -9.3806 | -61.5315 | 2025-08-11 09:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 658ca60f-3992-30c1-b532-ec296083ee8b | -9.3806 | -61.5315 | 2025-08-11 09:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| c8de29e0-27e6-3f36-9277-0bcb62755419 | -6.5856 | -44.564 | 2025-08-11 09:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 8c96b870-de87-367b-98f0-0abe7778952c | -6.5856 | -44.564 | 2025-08-11 10:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 0720e004-0b02-3340-a570-5e5e840a5131 | -14.1297 | -45.4043 | 2025-08-11 11:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 3dadb656-97f4-3c08-bada-b0635cd07a54 | -14.1103 | -45.4077 | 2025-08-11 11:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 6c47f2d5-2006-3ff9-b577-c9ca332f7c21 | -14.1297 | -45.4043 | 2025-08-11 11:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 110.0 |
| f6a60e74-8f5f-38ce-8a13-c140b9b8e0ba | -14.1297 | -45.4043 | 2025-08-11 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 157.9 |
| 8f7d9d0e-1303-3bc4-9b25-1818802b70a7 | -14.1297 | -45.4043 | 2025-08-11 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 173.0 |
| 74d47520-881b-3ee0-a6e4-2e71e71c0f23 | -14.1108 | -45.3844 | 2025-08-11 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 65ec125a-d56a-3b23-aadd-9f26f59c1069 | -14.1212 | -44.8933 | 2025-08-11 12:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 2a76c8e6-c3b1-3018-b03a-65b7b83174cf | -14.1217 | -44.8699 | 2025-08-11 12:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 135.3 |
| 35a26def-0b4c-38a0-97b1-fec08c14cf2c | -14.1212 | -44.8933 | 2025-08-11 12:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 587eaaba-0141-34a5-89fd-cdd7816fd01c | -14.1217 | -44.8699 | 2025-08-11 12:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 157.3 |
| 0d5c1296-b607-35a1-a160-574f1be947d9 | -14.1297 | -45.4043 | 2025-08-11 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 2096a471-626e-327b-846b-dc56e0e405d6 | -14.1103 | -45.4077 | 2025-08-11 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 2b353a92-3b7f-3950-9901-1a2dcd5823f8 | -14.1212 | -44.8933 | 2025-08-11 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 95.8 |
| fe98387c-6663-39c9-8f76-767e7427cb3e | -14.1297 | -45.4043 | 2025-08-11 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 776b9ada-56bd-3c65-b419-055082e914e0 | -14.1217 | -44.8699 | 2025-08-11 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 106.2 |


[Clique aqui para ver as próximas entradas](README30.md)
