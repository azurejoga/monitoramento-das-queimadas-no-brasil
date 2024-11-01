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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db9ae794-97f1-3885-a170-35a8dc5c779a | -3.11544 | -54.26204 | 2024-11-01 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56253271-cfa6-3d11-b0b1-49ddabd2f121 | -3.11516 | -54.29296 | 2024-11-01 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| baf7c363-02da-3ee8-9221-84e86404e017 | -3.11488 | -54.26585 | 2024-11-01 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3beb07c8-4849-3a49-b64d-b3d0120867e4 | -3.11461 | -54.29673 | 2024-11-01 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7c38c5d0-b161-3094-8842-b0a83767f95e | -3.11294 | -54.2929 | 2024-11-01 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11017e45-6ab4-3f34-b118-483c1a68bd60 | -3.11236 | -54.29667 | 2024-11-01 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae995f94-e03d-34b3-9947-62f8104274ce | -3.10852 | -54.28036 | 2024-11-01 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 658bb993-11a5-3511-951a-14099269ac5d | -3.10011 | -53.71646 | 2024-11-01 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59e395a5-33ab-3fff-90a9-279a0d2b0160 | -3.0958 | -53.7158 | 2024-11-01 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9ea6e01-fcbd-307b-80d2-8a4dc7e24482 | -3.09402 | -53.71317 | 2024-11-01 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0e892b2d-5a64-3ac1-b3c9-912da3dd1d84 | -3.09339 | -53.71726 | 2024-11-01 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 669876b2-1f78-322f-9b20-db01a5cdf24f | -3.07254 | -54.16617 | 2024-11-01 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 12cbdba8-a80d-3e2e-9ba8-e6c1dd81f82c | -3.06835 | -54.16557 | 2024-11-01 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4efd19fa-448d-3bc0-a214-d5a0491927f7 | -3.06777 | -54.16944 | 2024-11-01 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2998eb42-771c-3262-a56f-21b88065fa97 | -3.06417 | -54.16496 | 2024-11-01 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3c47a6a6-7ce4-3cf5-a78f-094790e8d5f8 | -3.05105 | -54.16685 | 2024-11-01 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 732b5b84-97bc-3a07-a725-63c8ecadb7ea | -3.05049 | -54.17067 | 2024-11-01 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 19b16c31-71f2-3f7e-87b9-b4928110c73c | -3.04631 | -54.16999 | 2024-11-01 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 753db9c7-5195-38f6-af13-925457db2c1c | -3.04575 | -54.17382 | 2024-11-01 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 45f24b4e-63d2-3762-aed5-7540edf5b970 | -3.03326 | -53.79436 | 2024-11-01 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b4637de-f122-3b22-a233-d0010105d645 | -3.01553 | -54.1391 | 2024-11-01 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98af2fcb-93e6-30cd-8ef6-a0b17d35f784 | -2.9429 | -53.7045 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 775137e2-c472-3775-ac11-854e67f09237 | -2.92172 | -54.19485 | 2024-11-01 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d1333dc-63fb-3680-af64-2a77b235040b | -2.91755 | -54.19421 | 2024-11-01 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a918a4d4-b83f-3d2c-99d6-7c1e6cdb3ecd | -2.90888 | -53.87197 | 2024-11-01 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 83aa59be-33d1-3b51-8a1d-11611727230e | -2.87525 | -53.98055 | 2024-11-01 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2691e27c-851a-3069-ac2b-ecc1c11d3ce8 | -2.80276 | -54.00165 | 2024-11-01 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11756318-e851-39b9-bec9-e8b35c115f1b | -2.55964 | -54.00665 | 2024-11-01 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ffc93d2a-6c9c-3eb2-a5d2-8d8594dd0a73 | -2.47533 | -53.98944 | 2024-11-01 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1bb8d3d0-e49e-39a2-a62c-844eb0b50920 | -2.4717 | -53.98503 | 2024-11-01 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8779cf5c-f77a-38d5-a51f-f0b31438076c | -2.25365 | -53.93804 | 2024-11-01 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c829f1ac-e738-336e-a68c-7e3f361d147c | -2.11064 | -55.92073 | 2024-11-01 05:23:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d882a347-4fd1-3d7a-8a11-7f39e662b840 | -2.1084 | -55.91809 | 2024-11-01 05:23:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da08364f-641c-3a8e-8a0d-1752609ddabc | -1.97356 | -55.49119 | 2024-11-01 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2f7d9eed-3441-3b30-8044-6fdfa674d3aa | -1.97209 | -57.04895 | 2024-11-01 05:23:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fd7ad0a3-ae79-31f0-8da9-7b634c3c3208 | -1.06061 | -57.40756 | 2024-11-01 05:23:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c266e1c8-db9c-3892-9a03-428896d5de83 | -1.05778 | -57.4033 | 2024-11-01 05:23:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 88a711e6-45f6-304d-9829-ca8ffdc36a0f | -0.86582 | -57.67204 | 2024-11-01 05:23:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb5cd037-3f6b-36a7-822c-b3fcc7af98bb | -2.62431 | -57.09632 | 2024-11-01 05:23:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e775cf2-3ee5-3a23-b080-c4be22548241 | -2.55693 | -58.10668 | 2024-11-01 05:23:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a621f09b-7a90-35ba-a452-b6e39de9f2c0 | -2.53104 | -57.79372 | 2024-11-01 05:23:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac5282e3-0585-34be-8a08-429c8acf3b39 | -2.39185 | -57.00695 | 2024-11-01 05:23:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20231363-9113-3c85-8046-7cca92c9ec88 | -2.3798 | -57.15644 | 2024-11-01 05:23:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 245252c3-11d8-3949-993c-76b640037b80 | 0.23217 | -60.57084 | 2024-11-01 05:23:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b131441-8052-3115-8578-39e83cd4cd96 | 2.57614 | -60.69786 | 2024-11-01 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6ff4b5e3-c0d8-3da2-bd78-25fe9378fa41 | 2.57269 | -60.69838 | 2024-11-01 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b945b9a1-4e15-3b6a-ac6c-ea262e674135 | 2.57212 | -60.69461 | 2024-11-01 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7413b8fc-91a4-3f69-8f16-0e26517a6cc0 | 2.56924 | -60.6989 | 2024-11-01 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bbbfa1ab-f53b-3134-b2ba-40b848680b8d | 2.56867 | -60.69513 | 2024-11-01 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2d961b35-40b6-387c-9c4f-acd73f98c4c3 | -0.75891 | -62.89962 | 2024-11-01 05:23:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc4bd43b-c79d-3322-ba2a-e48b00cd39f3 | -0.75589 | -62.89466 | 2024-11-01 05:23:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f5414b2-131a-30bb-8af6-7b7e5591e6b7 | -0.75521 | -62.89905 | 2024-11-01 05:23:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3397320d-2825-3ed2-a5fc-0e1d364ea950 | -1.07132 | -62.65305 | 2024-11-01 05:23:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c698175-310e-38c5-8057-92209cfcdcb4 | -0.79703 | -63.0816 | 2024-11-01 05:23:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 559afacd-4474-39ed-a29c-8627ffda0690 | -0.7933 | -63.08104 | 2024-11-01 05:23:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf090cce-478e-31b4-8021-97874872cad8 | -16.93099 | -57.65731 | 2024-11-01 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| e2ff310c-761f-3261-b6c1-bbbbeb479fc9 | -16.92694 | -57.65673 | 2024-11-01 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ec2f025e-ebbd-32bc-b5b6-19f7ed369879 | -16.92288 | -57.65614 | 2024-11-01 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| fde300db-d10e-316f-8c88-3e257e7199f3 | -16.91468 | -57.52675 | 2024-11-01 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| cfa025d8-f607-3f30-bdcd-4ace560c37b4 | -16.9145 | -57.52527 | 2024-11-01 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 4cd3c366-6732-3393-8a65-b737a95ba37f | -16.91418 | -57.53052 | 2024-11-01 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 6b518cf9-b47a-34cb-b8f4-3a2dc1981f8a | -16.91403 | -57.52905 | 2024-11-01 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| f1f9596f-3f8b-3bc5-8cbc-5a6f0c7c4ab5 | -9.40452 | -66.53001 | 2024-11-01 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b60f167d-3e6b-3332-bd85-4e2633b41559 | -9.80314 | -66.69413 | 2024-11-01 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c21b2e80-4dc8-310b-894d-a343e9e7af09 | -16.91208 | -57.51483 | 2024-11-01 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 045ca2c6-c729-3a65-b624-1d150c66ebff | -9.57104 | -66.63142 | 2024-11-01 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 73522768-0ca3-39f8-9dfa-bd8b8af7b3e2 | -9.56976 | -66.63882 | 2024-11-01 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 976ce128-d045-3ac9-9314-df7f7592484c | -9.52675 | -66.64982 | 2024-11-01 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 76a2ec69-c4d7-3420-ba56-d04df4fff119 | -9.52612 | -66.65353 | 2024-11-01 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ae0e1de-7ac5-3cab-8e31-315e47cac5e6 | -9.52549 | -66.65727 | 2024-11-01 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 206cf5a9-65c3-3128-b308-1b1fbc8f48c7 | -9.52201 | -66.65285 | 2024-11-01 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff041bd0-3a3f-33ab-a542-0adc2a54f69a | -9.50433 | -66.55843 | 2024-11-01 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 218c64f4-f009-356b-aac4-559493c0b7f3 | -9.42623 | -67.24281 | 2024-11-01 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b9d492b-c1b2-3655-ae3c-c48979d48215 | -9.91963 | -67.15293 | 2024-11-01 05:25:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac062d78-7477-3ce3-8273-3a7727cd0f5b | -9.91893 | -67.15692 | 2024-11-01 05:25:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6cb25c56-9dea-3d6a-8ef9-d7aac52d4961 | -9.82159 | -67.06725 | 2024-11-01 05:25:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ea1f518-3028-3d3e-9b4a-cfada6cee162 | -9.67002 | -66.51963 | 2024-11-01 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 085519e9-82d1-3d6b-9dd4-6eab0828bbf1 | -9.66992 | -66.51978 | 2024-11-01 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eda863f0-03f6-3371-bed3-61e1bddc5efa | -9.5704 | -66.6351 | 2024-11-01 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e734dc93-2959-3ade-9bc6-4e318b2e6e96 | -9.53023 | -66.65422 | 2024-11-01 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 593a6b31-6924-3f55-8839-983b0e7bf578 | -9.5037 | -66.5621 | 2024-11-01 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2ffd50a-5d72-3a58-b91c-ce3629afed9f | -9.43358 | -67.14813 | 2024-11-01 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e7d976c-f2c2-3445-b3b4-cd015c979ee5 | -9.4305 | -67.24358 | 2024-11-01 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f351be0-2bed-3959-b773-5526afde6644 | -9.42905 | -67.24344 | 2024-11-01 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e47f3f29-92e5-3aa9-b27c-ac381b7e335c | -9.4086 | -66.53072 | 2024-11-01 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4fb1d4a-a222-39c2-8325-edd5722da471 | -2.73511 | -66.02061 | 2024-11-01 05:25:00 | NOAA-21 | JURUÁ | AMAZONAS | Brasil | 1302207 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 511cc195-0e4e-3138-b62f-34e53057ac74 | -9.26186 | -68.33345 | 2024-11-01 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 12278930-f175-3197-b3ae-6e80165e3b23 | -9.25725 | -68.3326 | 2024-11-01 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b2f2d07f-cbac-3060-ab60-9989d324e62a | -9.13311 | -68.18139 | 2024-11-01 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 212c329c-5397-327c-9745-be079e2b4410 | -9.26358 | -68.32388 | 2024-11-01 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9fbf5211-6884-3913-b9d7-49039519246e | -9.5395 | -68.52213 | 2024-11-01 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ac59baa-c980-315d-bd6f-b1e473524b0a | -9.53629 | -68.5231 | 2024-11-01 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c8cc714-495e-3b5b-b868-326209f6ab22 | -10.48865 | -67.96069 | 2024-11-01 05:25:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9990b548-b589-36c8-871a-c891c255d0f5 | -10.12192 | -67.59487 | 2024-11-01 05:25:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0596790b-1455-3d10-8752-2bf8ce228722 | -10.1176 | -67.59404 | 2024-11-01 05:25:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 114d52f1-19dc-3c6b-9507-688640f5d97d | -10.09978 | -68.37723 | 2024-11-01 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4cde3379-e6e3-3701-ab2e-b376912e5772 | -10.09917 | -68.37925 | 2024-11-01 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 34da750c-920f-3d25-9bc2-9e84098a1289 | -10.0978 | -68.36228 | 2024-11-01 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4bdd5233-7bd0-30d1-b384-4e79f112567c | -10.09694 | -68.36696 | 2024-11-01 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 52933be6-8d4c-3dd6-98aa-70097a658b86 | -10.09626 | -68.36894 | 2024-11-01 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README49.md)
