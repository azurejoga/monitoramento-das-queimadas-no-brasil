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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96787f0f-4f8c-3eff-b23a-770289edda80 | -5.6894 | -46.435 | 2024-10-21 01:55:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 137.6 |
| a5e4370d-9e32-3212-84c8-bb44a4b0de33 | -5.6896 | -46.4128 | 2024-10-21 01:55:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| c72efb1d-6146-32dd-83f3-53224734d97b | -5.7081 | -46.4338 | 2024-10-21 01:55:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| c78af53b-7958-38a6-9061-39a1ad8363b7 | -5.7083 | -46.4115 | 2024-10-21 01:55:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 3edf16bb-173e-3055-b81d-5218eda2bba0 | -9.3718 | -66.4891 | 2024-10-21 01:56:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 682d2c0b-2a68-3e27-99be-a612d4e033b7 | -12.4778 | -63.1885 | 2024-10-21 01:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 33.8 |
| ba5c3187-1216-391c-947c-825412b0f757 | -12.4967 | -63.1874 | 2024-10-21 01:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 24.2 |
| def9ac2a-5bf8-387c-a138-531d3816a21b | -12.5147 | -63.3014 | 2024-10-21 01:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 8cab8d88-5f0e-3c34-abb0-088c2c1453da | -12.5168 | -63.0329 | 2024-10-21 01:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 29.7 |
| e3ac945a-a80f-394b-965e-0dd1700fdad8 | -12.5336 | -63.3003 | 2024-10-21 01:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 68ade33d-945b-36c3-8ed5-7b7168283cce | -12.5356 | -63.051 | 2024-10-21 01:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 71ad4e56-21d9-389a-9772-06f94576b1f2 | -12.5357 | -63.0319 | 2024-10-21 01:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 49.9 |
| a59c8176-fa8c-319a-abe3-d96ef29d1fd7 | -17.7259 | -57.4751 | 2024-10-21 01:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.0 |
| ef0e0155-ed26-39aa-9a3f-db3c0dc236fd | -17.7262 | -57.4545 | 2024-10-21 01:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.4 |
| 8cd26ddf-c0ab-395c-bf33-89e791e0dd8e | -18.263 | -56.1021 | 2024-10-21 01:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.5 |
| 3d39be1b-ff74-3825-9b17-1280c654f95a | -18.2828 | -56.0994 | 2024-10-21 01:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 122.9 |
| 537884bf-ae6f-307b-8b27-6ab10b821e74 | -18.2832 | -56.0785 | 2024-10-21 01:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.7 |
| ceb4a3a5-d5a1-3214-b731-dc2f6bc4b061 | -1.2018 | -53.6164 | 2024-10-21 02:05:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 044a56b6-b974-375f-8c94-e16e182d449c | -1.1834 | -53.6368 | 2024-10-21 02:05:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| e7dee005-820a-368e-ab97-2a8b87d3eac7 | -1.1835 | -53.6166 | 2024-10-21 02:05:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| ed52cc6c-baa0-3f0e-b48d-df13ee793ab5 | -1.2018 | -53.6366 | 2024-10-21 02:05:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 26f1a415-2ada-3a15-9a15-13327bc92569 | -2.2199 | -50.4594 | 2024-10-21 02:05:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 11529723-a8f8-3e2a-8c39-e1709c2a44a2 | -2.4824 | -49.1233 | 2024-10-21 02:05:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 4f324a5d-f2aa-326c-9163-d927908aa774 | -2.4824 | -49.102 | 2024-10-21 02:05:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 41f455c0-3f9f-3730-a37d-2de13cfacb45 | -2.7773 | -49.3067 | 2024-10-21 02:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 60a932dd-7776-321c-93d7-eb7b5fa27cc4 | -2.7774 | -49.2854 | 2024-10-21 02:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 84bc20bb-1bf2-345b-aa4b-4efef87cf81b | -2.8069 | -51.3613 | 2024-10-21 02:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| fc406518-876a-3a3e-b781-58cf8d8c8d0f | -2.8371 | -53.3463 | 2024-10-21 02:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| abd460ba-3e3c-348e-9ad8-3a61298e56ca | -2.8372 | -53.3261 | 2024-10-21 02:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| c3081bcb-7a14-3c26-8db6-0b268b1f2d07 | -2.8556 | -53.3256 | 2024-10-21 02:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 5fd8ae54-d449-3415-a230-b3393f77d678 | -2.905 | -45.2143 | 2024-10-21 02:05:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 69b0246f-1e6e-3e77-8b28-3f667eb606fa | -2.9051 | -45.1918 | 2024-10-21 02:05:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 35dbcabb-d2aa-39e7-8bcf-5dc33347a4a0 | -3.0036 | -53.0583 | 2024-10-21 02:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 64631255-97f5-37d5-8de8-265273893e66 | -3.0037 | -53.038 | 2024-10-21 02:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 55ab3552-63e9-3322-9d46-2a28b73abd6b | -3.0581 | -53.2395 | 2024-10-21 02:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 641cc8e0-d438-3d75-aa15-d4c396737dfe | -3.1138 | -53.1163 | 2024-10-21 02:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| f860f974-bab3-307c-aba5-1a261dd43683 | -3.2585 | -53.78 | 2024-10-21 02:05:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| a07472e5-9411-3261-b653-b0a6386f7996 | -5.7081 | -46.4338 | 2024-10-21 02:05:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 51d91017-581a-3cf4-812a-9a76d1e5e607 | -5.6894 | -46.435 | 2024-10-21 02:05:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 4a886963-6477-37d3-8b9c-cc709226e03d | -5.6896 | -46.4128 | 2024-10-21 02:05:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 2a045ee8-2863-352f-83fc-f2f8d5aa19ce | -9.3718 | -66.4891 | 2024-10-21 02:06:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| fd472d72-a307-3a2b-826c-ed80d0ff0789 | -12.4778 | -63.1885 | 2024-10-21 02:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 32.9 |
| c4d904a7-2f74-315f-b2ec-54d3f4ce6743 | -12.5357 | -63.0319 | 2024-10-21 02:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 911a1e52-106e-3d52-bb42-8313c8c8fb28 | -12.5336 | -63.3003 | 2024-10-21 02:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 707dfa81-aaa2-399e-b3a1-5ff78b65372c | -12.5168 | -63.0329 | 2024-10-21 02:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 215107fe-5f6d-3461-b3ab-dfbb3bc98212 | -12.5147 | -63.3014 | 2024-10-21 02:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.1 |
| a08ed4f4-ff32-3c0d-a619-cb4c7f81bbed | -18.2828 | -56.0994 | 2024-10-21 02:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 159.6 |
| 1c38f208-e5f7-3afd-a9ef-59149c348762 | -18.2832 | -56.0785 | 2024-10-21 02:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.9 |
| 807b7c0a-3956-380b-b2e3-1ae5ea6cedcb | -1.1834 | -53.6368 | 2024-10-21 02:15:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 5a3cc7a5-2205-3449-b57a-5c6872b07d04 | -1.1835 | -53.6166 | 2024-10-21 02:15:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 28c06598-431b-32cf-9204-dfcdc2f56fd4 | -1.2018 | -53.6366 | 2024-10-21 02:15:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 40513149-15ec-3e59-9af2-ffe96e4a2267 | -2.2199 | -50.4594 | 2024-10-21 02:15:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| ce8898cc-1318-33c2-8cb7-b9d14c5b10be | -2.4824 | -49.1233 | 2024-10-21 02:15:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 63b67f47-95c6-33c8-9a99-9822a2f91d72 | -2.4824 | -49.102 | 2024-10-21 02:15:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| f89746d6-63c1-37c6-953d-5c3aad844cf5 | -2.7773 | -49.3067 | 2024-10-21 02:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 59d1505a-54ca-3b05-b592-b1afdf82a0b5 | -2.7885 | -51.3618 | 2024-10-21 02:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 106ea63b-d946-3723-a36e-fcede49554f6 | -2.8668 | -45.4631 | 2024-10-21 02:15:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 49.2 |
| a7b06b0b-dac0-330f-8010-36f5d999a204 | -2.8556 | -53.3256 | 2024-10-21 02:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| d8eb6fbf-77a6-3d9d-9041-941343285e50 | -2.905 | -45.2143 | 2024-10-21 02:15:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 5bb84d1e-f665-3683-97ac-546fb54dea87 | -2.9051 | -45.1918 | 2024-10-21 02:15:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 68.1 |
| f6c5a423-aa03-3128-bb99-3417ac5bbf1f | -3.0037 | -53.038 | 2024-10-21 02:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| d5217539-4f7f-3e63-8bca-666f55e3b1a3 | -3.0176 | -54.3489 | 2024-10-21 02:15:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 1e0a3cfd-ffb8-3544-91f5-068cd58e1d32 | -2.9852 | -53.0587 | 2024-10-21 02:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 2a6f87ba-c527-337b-b39c-8c00028f247f | -2.9853 | -53.0384 | 2024-10-21 02:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| d2484f62-77cd-3e3c-97ba-2c0dbc7f37ff | -3.0036 | -53.0583 | 2024-10-21 02:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| f73578e1-5915-39e8-977d-12c66148d5d6 | -3.1138 | -53.1163 | 2024-10-21 02:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| db62a808-e329-39c5-9e48-f742e3f68265 | -5.6894 | -46.435 | 2024-10-21 02:15:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 071209a9-2f35-3457-bc4c-0bb4c4921362 | -5.6896 | -46.4128 | 2024-10-21 02:15:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 8d955009-1a21-3a58-b8f2-e6d4d4b61a2c | -9.3718 | -66.4891 | 2024-10-21 02:16:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| a2c61b25-8234-3c1f-ba47-e55897f4ae73 | -12.4967 | -63.1874 | 2024-10-21 02:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 2129a7de-fc32-33a9-b7c4-4c018b11c743 | -12.4778 | -63.1885 | 2024-10-21 02:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 27.1 |
| c74e256d-8f0c-3607-b401-c57348a6638b | -12.5357 | -63.0319 | 2024-10-21 02:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 059f0cfc-1364-3793-bc03-aa65c7d91166 | -12.5147 | -63.3014 | 2024-10-21 02:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 18224980-4a9a-3885-b631-6823dea6d598 | -17.7065 | -57.4569 | 2024-10-21 02:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.7 |
| 77868369-1608-341c-8ff3-66d3e3e34ba2 | -18.263 | -56.1021 | 2024-10-21 02:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.5 |
| 08765800-f261-3855-b723-d881aa5df564 | -18.2828 | -56.0994 | 2024-10-21 02:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 162.5 |
| 8001154f-8567-3f77-8de8-cd0b13759ab2 | -18.2832 | -56.0785 | 2024-10-21 02:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.8 |
| 4b0822e8-d5e2-3345-b727-424af37e5515 | -9.6715 | -64.734703 | 2024-10-21 02:18:18 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 77f24950-63ae-30c2-96bc-2a7772b10984 | -9.2904 | -66.499001 | 2024-10-21 02:18:31 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8cc98c3b-4dc0-3405-9c12-88fa239ec081 | -9.2769 | -66.486099 | 2024-10-21 02:18:31 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 82dee0c6-020a-331c-9b59-9fa778ff4bf0 | -9.2807 | -66.501404 | 2024-10-21 02:18:31 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ca4d99a6-4cc2-3a2a-96c5-073a86c4feab | -1.2018 | -53.6366 | 2024-10-21 02:25:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| bef29393-10f1-39ef-978a-c01f614e1b32 | -1.1835 | -53.6166 | 2024-10-21 02:25:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| b385fa00-e0d5-35f0-886b-a541554c1b0d | -1.1834 | -53.6368 | 2024-10-21 02:25:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| c167a83e-830e-3342-b7d8-1cef1b87b682 | -2.2199 | -50.4594 | 2024-10-21 02:25:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| ea78ba6a-1edd-3223-97cd-cd34ae800c76 | -2.4824 | -49.102 | 2024-10-21 02:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| cb9ba1cf-462d-3463-a60d-719dd15f62ba | -2.4824 | -49.1233 | 2024-10-21 02:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 75544f10-7295-3501-8643-4cec1896b082 | -2.7774 | -49.2854 | 2024-10-21 02:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| e4e87cde-7388-3f67-9de5-7a7a7baa002a | -2.9051 | -45.1918 | 2024-10-21 02:25:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 97451c49-6d76-3f54-960d-ed265c3bbef7 | -2.7885 | -51.3618 | 2024-10-21 02:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 57bfcd23-8d31-3eef-84fb-9341ea243e41 | -2.8069 | -51.3613 | 2024-10-21 02:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 8186bb9d-b19f-34a6-a002-dec719a72c8b | -2.8668 | -45.4631 | 2024-10-21 02:25:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 0586b9a5-195c-3870-b728-7ec2285c741b | -2.8555 | -53.3459 | 2024-10-21 02:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 6b9e1ac5-88a9-372d-8347-54d748616732 | -2.8556 | -53.3256 | 2024-10-21 02:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| aedcd896-87c7-3453-a547-c5086de1c84a | -2.7773 | -49.3067 | 2024-10-21 02:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 64ad8401-6600-3072-a992-517effbaf101 | -2.905 | -45.2143 | 2024-10-21 02:25:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 82.6 |
| fabd62a1-f82f-3be6-b9b8-683c476337f1 | -2.9853 | -53.0384 | 2024-10-21 02:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 2bd0b32d-b53e-3015-9b49-8014b1e84d56 | -2.9852 | -53.0587 | 2024-10-21 02:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 82e86e27-54b5-3abc-b48e-3915afbfca8a | -3.1138 | -53.1163 | 2024-10-21 02:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 8f4760f4-9607-3f49-a705-e70414195647 | -4.5356 | -43.5597 | 2024-10-21 02:25:32 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 40.2 |


[Clique aqui para ver as próximas entradas](README19.md)
