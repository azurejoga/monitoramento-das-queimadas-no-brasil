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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 146b27e0-d2b4-3c5b-a6c3-43f2d89cb41e | 2.1585 | -61.8536 | 2025-01-16 00:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 5a9d6049-4b3c-33d4-af35-3c8d09db9a57 | 2.1768 | -61.8158 | 2025-01-16 00:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 63320f10-8b99-3655-8469-502b334a6e38 | 2.195 | -61.8156 | 2025-01-16 00:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 6d86d39b-003b-3201-b082-dfb7b292bf26 | 2.195 | -61.7968 | 2025-01-16 00:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 098daaee-aec1-3034-b49b-0326540bdeb3 | 2.1039 | -61.8166 | 2025-01-16 00:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 85.3 |
| df8c36d0-b401-3d75-9e0d-fe7d3e9a1ca9 | -16.1115 | -58.1868 | 2025-01-16 00:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.4 |
| 3fb93eb9-1e7b-38ac-af50-2f1cb81cac32 | 2.1767 | -61.8534 | 2025-01-16 00:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 115.4 |
| b1867816-5871-3892-82b4-0aedd1394b0f | 2.1585 | -61.8724 | 2025-01-16 00:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 76e6c172-d0eb-3a89-a5b1-f811ad30563c | 2.1767 | -61.8722 | 2025-01-16 00:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 65bd6339-de63-3e03-91eb-22b11c1ffa51 | -16.1118 | -58.1666 | 2025-01-16 00:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.2 |
| f0447d96-5d58-388f-90a3-07ade55cfcf0 | 2.1221 | -61.8164 | 2025-01-16 00:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 9f5c9b49-c47e-3f39-a7c7-e79d6a52c2e4 | 2.1039 | -61.8166 | 2025-01-16 00:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 3b2b2ba8-1730-3ef8-97ff-944e3b43f022 | 2.195 | -61.8156 | 2025-01-16 00:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 2d776a03-3667-3d93-a28b-22886a8801ea | 2.1767 | -61.8722 | 2025-01-16 00:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 0c206d1a-ff88-3db7-8502-010aa5e63dc3 | -16.1118 | -58.1666 | 2025-01-16 00:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.5 |
| f974b19e-5d7b-3186-a8ff-f0eafa077b84 | 2.1768 | -61.8158 | 2025-01-16 00:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 530580fe-643a-3d4c-a41a-b1dcdb849b00 | -16.1115 | -58.1868 | 2025-01-16 00:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.8 |
| 48dfeac7-4e9a-3a86-a712-9637e411a914 | 2.1767 | -61.8534 | 2025-01-16 00:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 0f6856f2-7c7e-3499-aab4-09539088b6b7 | 2.1585 | -61.8536 | 2025-01-16 00:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 77.2 |
| b355b1ff-775b-3805-be6d-78a4e85796ae | 2.195 | -61.7968 | 2025-01-16 00:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 1e4a28e5-93fd-3dd2-9b3e-8b61cf15f7e4 | 2.1767 | -61.8534 | 2025-01-16 00:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 79.6 |
| e9cca7c0-61b8-3c6c-87c7-ff99470ceb11 | -16.1115 | -58.1868 | 2025-01-16 00:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.6 |
| c19c416e-c7f9-3050-bb70-6512c263e4c7 | 2.1039 | -61.8166 | 2025-01-16 00:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 57.9 |
| e4fbe7f1-f6e3-3719-b501-94b26e0e68db | 2.1767 | -61.8722 | 2025-01-16 00:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 53.0 |
| dc088d32-ed6e-3966-8eef-e8c7a1b32a0e | 1.2852 | -60.4265 | 2025-01-16 00:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 94e7f9a8-063b-333c-bffd-15d46a2bb94d | -2.907 | -54.4916 | 2025-01-16 00:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 5a2d694a-bb93-3cf2-80e0-cb6400f5460f | 2.195 | -61.8156 | 2025-01-16 00:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 73.9 |
| d32e15e1-63c0-3351-99ee-d1d90298d7e3 | -16.1309 | -58.1848 | 2025-01-16 00:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.1 |
| 652f00f5-806a-3192-962e-0f694da9680b | 2.1585 | -61.8536 | 2025-01-16 00:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 5fd62ac8-1042-351e-a52a-6aeed3097d3c | 2.1221 | -61.8164 | 2025-01-16 00:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 2f948227-bc1a-3226-b2cb-d526696e6952 | 2.1767 | -61.8534 | 2025-01-16 00:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 93.7 |
| f18b5f33-9cf1-3e86-803d-2278fe19ce2a | 2.1585 | -61.8536 | 2025-01-16 00:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 79.3 |
| db6ff434-a1b8-37a9-8cb9-b916186e84e6 | 2.1767 | -61.8722 | 2025-01-16 00:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 63ff0843-4199-3f07-a677-38ca49429649 | -16.1115 | -58.1868 | 2025-01-16 00:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.7 |
| a70730c5-a7af-34a9-920b-9b7e53f3d5d7 | 2.195 | -61.8156 | 2025-01-16 00:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 93f0b085-6a6e-3204-b1c6-e0fddc46335b | 2.1039 | -61.8166 | 2025-01-16 00:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 1f73034c-ac8c-3515-9e7e-06c7dac5f035 | 2.0999 | -61.7826 | 2025-01-16 00:30:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7fcb704c-b430-3116-a068-6b86517a1bd1 | -16.1285 | -58.153702 | 2025-01-16 00:30:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9a47104f-c90a-3cc2-9d1c-7f3b4781c90c | 3.1317 | -60.655399 | 2025-01-16 00:30:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c968dc8f-1c93-380a-957c-345401b6795b | 0.8288 | -59.512901 | 2025-01-16 00:30:00 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ec5b1160-9ff8-3c2c-99fc-d3b56265c3ba | 2.1729 | -61.7756 | 2025-01-16 00:30:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 11962d7c-da8b-3072-96eb-018ef0c2ed0e | 3.1372 | -60.6758 | 2025-01-16 00:30:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 229673f9-6fd3-31eb-a96b-7c9bfeaa3f97 | -2.9184 | -54.478901 | 2025-01-16 00:30:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d81270f-49af-3fd1-bc13-47a8cc62f2f3 | -27.131201 | -50.758999 | 2025-01-16 00:30:00 | METOP-B | FREI ROGÉRIO | SANTA CATARINA | Brasil | 4205555 | 42 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 800f5f0d-ea85-359a-9e2f-81ab26e3a92d | 2.1623 | -61.8209 | 2025-01-16 00:30:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 082b00fe-191e-31d4-92f2-99f0eca8f52e | 2.1527 | -61.818699 | 2025-01-16 00:30:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 20df80dc-4303-3913-b0ff-72d95ddd73ef | 2.1569 | -61.843601 | 2025-01-16 00:30:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ce933539-d040-3750-b053-6130c9c4dd31 | 2.1096 | -61.784801 | 2025-01-16 00:30:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c2d97822-9c8d-304d-9cdb-343f66e72a92 | 0.8386 | -59.515099 | 2025-01-16 00:30:00 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c0fd604d-d1ca-304a-8d7d-e47e33cbf111 | -23.907801 | -48.170399 | 2025-01-16 00:30:00 | METOP-B | CAPÃO BONITO | SÃO PAULO | Brasil | 3510203 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 01173b75-4bfc-3ea8-99fb-aafc01fa2252 | 2.1473 | -61.8414 | 2025-01-16 00:30:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 68046905-c3fe-31d3-ba60-e2107e6ad12e | -16.1243 | -58.129501 | 2025-01-16 00:30:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6d632642-4447-3509-8d35-c01d067cd0c9 | 3.1275 | -60.673599 | 2025-01-16 00:30:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e85316ea-bed0-3e07-81b3-556ecbc2dcd4 | 2.1585 | -61.8536 | 2025-01-16 00:40:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 71.4 |
| fda1cf12-0a4b-3731-aebb-1c7327935645 | 2.1039 | -61.8166 | 2025-01-16 00:40:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 3c1f88fa-7f13-39e0-9154-06dfb15bd1a4 | 2.195 | -61.8156 | 2025-01-16 00:40:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 81.6 |
| dafce660-8e3b-3106-beec-2d04effea458 | -16.1115 | -58.1868 | 2025-01-16 00:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.9 |
| d6316f71-406c-3fd0-bfea-3364cad95d6c | 2.1767 | -61.8722 | 2025-01-16 00:40:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 7a629437-29c0-39a8-ae37-547909f0aef0 | 2.1767 | -61.8534 | 2025-01-16 00:40:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 103.3 |
| aca6ff36-3560-3fed-80e2-5645496f3a5d | -9.7226 | -36.0805 | 2025-01-16 00:50:00 | GOES-16 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 72.3 |
| f1fe0f5c-b3fe-3436-bedb-fb3b8acbabd8 | 2.195 | -61.8156 | 2025-01-16 00:50:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 9aa2b1cf-44e6-3a34-b056-d8fcbe078893 | -16.1115 | -58.1868 | 2025-01-16 00:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.1 |
| 9544bb39-7002-3f68-8f8e-9e7dbc09d34d | 2.1767 | -61.8722 | 2025-01-16 00:50:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 7a5a99a6-c3a9-3deb-b6fa-b845c07a8981 | -9.7221 | -36.1077 | 2025-01-16 00:50:00 | GOES-16 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 71.7 |
| 6b20d472-3fb3-35ef-9c19-6b93d8923d00 | 2.1767 | -61.8534 | 2025-01-16 00:50:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 29aabe87-04d6-306a-b721-5d71efc30b99 | 2.1585 | -61.8536 | 2025-01-16 00:50:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 0eed41da-0e83-3728-9ac9-8ffb800b8686 | 2.1039 | -61.8166 | 2025-01-16 00:50:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 5be2fc2a-d47b-335f-ac2d-791ea7c721d7 | 2.195 | -61.7968 | 2025-01-16 01:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 199c3c85-75f7-3f11-a83e-b6b5176a5fb3 | 2.1767 | -61.8722 | 2025-01-16 01:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 9d6af803-79b0-34c7-917f-70c5a63a1f29 | 2.1039 | -61.8166 | 2025-01-16 01:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 69d8d851-63be-3fef-bc5c-43b1178f651c | 2.195 | -61.8156 | 2025-01-16 01:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 909c8ccb-8d8d-37d4-b25c-ac9426810e4f | 2.1585 | -61.8536 | 2025-01-16 01:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 49cf59b4-2d4b-37a3-850f-a78ea9f66955 | -9.7226 | -36.0805 | 2025-01-16 01:00:00 | GOES-16 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 100.6 |
| f4ea76cb-cdea-3a43-9160-5bb0e164b21a | 2.1221 | -61.8164 | 2025-01-16 01:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 44.8 |
| e0228eb9-a632-3bba-aa75-a1276af99ae1 | -9.7221 | -36.1077 | 2025-01-16 01:00:00 | GOES-16 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 108.0 |
| fb128a2a-6029-3cbe-bf36-f27a3ebc032d | -16.1115 | -58.1868 | 2025-01-16 01:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.0 |
| e26b2346-b321-3057-8218-8ff20f389102 | 2.1767 | -61.8534 | 2025-01-16 01:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 92.7 |
| afa03cec-6cb1-3369-943b-6a29e49e7a90 | -2.907 | -54.4916 | 2025-01-16 01:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| eb6f433a-13f4-3f0c-9a58-fd8f18505568 | 2.1767 | -61.8534 | 2025-01-16 01:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 52.8 |
| f87af755-925b-3451-9e9c-df1ac07e2d57 | 2.1767 | -61.8722 | 2025-01-16 01:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 33.0 |
| f0e6d646-2efa-3817-9a94-fe6f72900310 | 2.5437 | -60.584 | 2025-01-16 01:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 04f07859-febb-385f-ac12-614919bbe3c1 | -16.1118 | -58.1666 | 2025-01-16 01:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.0 |
| d289a3b2-9824-328f-a156-de11d89377d0 | -16.1115 | -58.1868 | 2025-01-16 01:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.8 |
| 61e039ed-651a-3213-be9f-07c536e33495 | 2.1585 | -61.8536 | 2025-01-16 01:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 45.0 |
| e2c61c89-cca2-36ea-af9d-f210348c297a | 2.1221 | -61.8164 | 2025-01-16 01:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 37.8 |
| fc7f842b-c280-345b-9a02-4f6cb323c4ae | 2.1039 | -61.8166 | 2025-01-16 01:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 4411b060-f83f-3e94-9161-ff2eb6b3ceed | 2.1585 | -61.8536 | 2025-01-16 01:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 699d8c74-b8e8-38b0-b3fd-22502f2e030c | 2.195 | -61.8156 | 2025-01-16 01:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 3837dc8e-5661-385d-8878-fdb76727433b | 2.1767 | -61.8534 | 2025-01-16 01:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 343a1529-79c3-37b4-a34e-266455277d46 | 2.1585 | -61.8724 | 2025-01-16 01:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 36.7 |
| d7a61f6a-7528-30cd-8395-477e8fc0b64c | 2.1039 | -61.8166 | 2025-01-16 01:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 67ba43b6-e9e8-3a3e-9de3-5106d52b485d | 2.1221 | -61.8164 | 2025-01-16 01:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 187d019e-bc3e-35fd-9a00-77d55d258142 | 2.1767 | -61.8722 | 2025-01-16 01:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 82fec2d6-03f4-38d0-924c-2a11dcc82312 | 2.5437 | -60.584 | 2025-01-16 01:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 912c73c8-1e06-3e62-81b8-796f94a8962a | -29.93815 | -52.32891 | 2025-01-16 01:28:00 | TERRA_M-M | RIO PARDO | RIO GRANDE DO SUL | Brasil | 4315701 | 43 | 33 | nan | nan | nan | Pampa | 5.2 |
| dd1896ab-9277-3fbd-82e5-24db0e93c0ca | -2.907 | -54.4916 | 2025-01-16 01:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 092d4c56-c35f-3b05-8bfc-54650585f9cc | 2.1767 | -61.8534 | 2025-01-16 01:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 7fa95b18-99af-3890-9261-9b8aeba3d3e8 | 2.1221 | -61.8164 | 2025-01-16 01:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 36.4 |
| e38a5bf7-ef6e-31e7-92a1-1393f1155fa1 | 2.1039 | -61.8166 | 2025-01-16 01:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 33.4 |
| fd882260-9fdf-327e-80a7-1d2c45fa148f | 2.5437 | -60.584 | 2025-01-16 01:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 56.7 |


[Clique aqui para ver as próximas entradas](README2.md)
