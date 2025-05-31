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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3f01c6f-a9fe-3a83-809b-3906205950f8 | -10.462 | -47.9428 | 2025-05-31 01:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| e0022a27-f727-3c20-af85-831a87f21fcc | -12.0345 | -49.5248 | 2025-05-31 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 7d97575f-8929-366b-8fa1-c80ece32dbcb | -7.2405 | -43.0899 | 2025-05-31 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.6 |
| 9aa37e50-1611-31b1-86ab-726e68d1ca1b | -11.8337 | -51.265301 | 2025-05-31 01:32:00 | METOP-C | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 618206ad-57bd-35d8-b906-817601c124eb | -10.8319 | -56.947201 | 2025-05-31 01:32:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c655799e-bc9f-34cb-a274-afc5d51411aa | -12.0279 | -49.5205 | 2025-05-31 01:32:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fdb133e0-aa87-3b79-9e3c-615e59519cc8 | -11.8433 | -51.262699 | 2025-05-31 01:32:00 | METOP-C | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5ce41c36-417e-36be-be4e-ceecad0136ca | -10.834 | -56.956001 | 2025-05-31 01:32:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e6531bff-97eb-31d1-8706-3a0412389f09 | -14.5948 | -58.758598 | 2025-05-31 01:32:00 | METOP-C | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e13bddca-2424-39fb-897a-e324ced8bfdf | -12.1875 | -54.2523 | 2025-05-31 01:32:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62b935d2-a4f6-3775-a66a-29060ef8a1c0 | -10.6524 | -49.423 | 2025-05-31 01:32:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 64ba34b0-e244-3ac7-8dec-4caa3ba290ac | -14.0321 | -55.136101 | 2025-05-31 01:32:00 | METOP-C | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cf783d00-4da4-34f2-8031-fd1a583902a6 | -10.4713 | -47.965801 | 2025-05-31 01:32:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 55c0b70c-5810-33fb-8607-25460e70967c | -12.0347 | -49.545799 | 2025-05-31 01:32:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 724e7aa3-b287-36e8-8fd5-dc5136cea0a2 | -12.0183 | -49.523102 | 2025-05-31 01:32:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 872fe708-3fe5-3289-84c4-9c661bfc8943 | -10.8298 | -56.938301 | 2025-05-31 01:32:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 369046b5-eee5-3c9d-b2b3-c42c87e4d17e | -10.65 | -49.452801 | 2025-05-31 01:32:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ce6ac372-ac90-3135-817f-0ec7c7d576c0 | -13.1056 | -52.294399 | 2025-05-31 01:32:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6f37d229-6f47-3f22-8e0e-dd815c4cc96e | -11.4628 | -49.109299 | 2025-05-31 01:32:00 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a688e528-afde-37db-bb01-c741156fe423 | -18.8426 | -53.6008 | 2025-05-31 01:32:00 | METOP-C | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2ecff96b-8c99-39b6-9796-6bfa4f98ba8f | -10.4618 | -47.9314 | 2025-05-31 01:32:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e85bd002-f0ee-3854-9be3-9630cf380c71 | -11.1469 | -53.937302 | 2025-05-31 01:32:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 82f4bbbb-5a05-37d1-a244-19b16d190b65 | -12.1043 | -54.6647 | 2025-05-31 01:32:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7813befc-913c-3231-b4d7-62348d06e113 | -12.0252 | -49.548401 | 2025-05-31 01:32:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6bbd03aa-80ad-3731-956b-50704a37fd4a | -11.9159 | -54.822102 | 2025-05-31 01:32:00 | METOP-C | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 30427ee8-f3d7-3c26-aed2-141076069229 | -10.6427 | -49.425701 | 2025-05-31 01:32:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 636fb5cf-55fb-37dd-b9c4-27e99d5d8290 | -11.8484 | -51.2822 | 2025-05-31 01:32:00 | METOP-C | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 164ff5ff-6fd5-3564-ba8b-8437b8d265fe | -11.8388 | -51.284801 | 2025-05-31 01:32:00 | METOP-C | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 74dba685-709b-37b2-9d7d-cb7575b11c4f | -12.0375 | -49.517799 | 2025-05-31 01:32:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4144bb94-527d-37a6-8497-ac4ab2232c41 | -10.6597 | -49.4501 | 2025-05-31 01:32:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 52451af9-1059-3fba-b94c-1db5129d5ece | -11.8368 | -51.2641 | 2025-05-31 01:40:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 114.2 |
| f963a2e6-b0e7-3ac1-bbf1-a2e7f4503f3c | -12.0154 | -49.5272 | 2025-05-31 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 2dcd9b5e-bea0-30e5-bc43-63c4d2a3c69f | -10.462 | -47.9428 | 2025-05-31 01:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| fcbd3777-33c0-37f8-8975-419c5a339ee7 | -11.8365 | -51.2854 | 2025-05-31 01:40:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| b7dd38b0-b6c6-3245-bb3f-fea7faf783e8 | -10.6492 | -49.4267 | 2025-05-31 01:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 46e6cd16-1275-32a2-98b1-5b901fc76cfd | -12.0345 | -49.5248 | 2025-05-31 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| a4a2b977-516f-3fb6-acf5-255d627d508a | -7.2405 | -43.0899 | 2025-05-31 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.1 |
| 5ba68b9e-ebb9-3682-a6ae-c63ce0c3554e | -11.8368 | -51.2641 | 2025-05-31 01:50:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 145.0 |
| 9199fee8-cd3e-3433-8f44-d760a1a99cfc | -12.0345 | -49.5248 | 2025-05-31 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| b42ae71c-4023-378b-8f0d-fe8628d548a1 | -11.8365 | -51.2854 | 2025-05-31 01:50:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| f910e119-8604-3410-aa4d-3c20deb8f463 | -10.6492 | -49.4267 | 2025-05-31 01:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 28738a91-140a-32b4-8f40-7aaf0820df53 | -12.0154 | -49.5272 | 2025-05-31 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 182f2b07-0b57-3c28-94f5-7c6cbcfd24f5 | -12.0154 | -49.5272 | 2025-05-31 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 81445f27-9f9c-3438-87ca-c64b8b5f66d3 | -10.6492 | -49.4267 | 2025-05-31 02:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 2b955691-9029-3696-9bc1-581317c55c2f | -12.0345 | -49.5248 | 2025-05-31 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| c27313ac-a2ad-3993-b92b-aa1d2c5be374 | -11.8368 | -51.2641 | 2025-05-31 02:00:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 516c87c3-9000-3623-bd2f-847a1cc34272 | -11.8365 | -51.2854 | 2025-05-31 02:00:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 4a62672d-2bd2-3a05-8cd1-91f0fe5cb0d3 | -11.8365 | -51.2854 | 2025-05-31 02:10:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 63.8 |
| f52b3598-6461-3afb-aa23-eaa2c8079be0 | -10.462 | -47.9428 | 2025-05-31 02:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 80d8ecec-4e9c-32ad-9090-8a02fe33d6c4 | -11.8368 | -51.2641 | 2025-05-31 02:10:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 66708e26-54f7-3f7e-863e-207c81c2c9f9 | -12.0154 | -49.5272 | 2025-05-31 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| bb5be7c9-504d-367b-9987-4b4274ada568 | -10.6492 | -49.4267 | 2025-05-31 02:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 02184eb3-6ef6-3857-87dd-065d548f4c32 | -12.0345 | -49.5248 | 2025-05-31 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 5bba82b5-a474-32ac-8499-c5004b83e7fb | -11.8368 | -51.2641 | 2025-05-31 02:20:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 110.9 |
| d8d68f36-625d-3b88-b8a8-54d29ae1a4a3 | -12.0345 | -49.5248 | 2025-05-31 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 4942e454-fbe1-3ea2-b622-cdf75bf90557 | -12.0154 | -49.5272 | 2025-05-31 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 1ef20fe8-e348-3cb2-bb9f-9ada24d4fe05 | -11.8365 | -51.2854 | 2025-05-31 02:20:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 354748ce-ad5a-34d1-b4be-a2eb7d3f88eb | -10.6492 | -49.4267 | 2025-05-31 02:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 60953639-3732-361b-b160-f8472f80cd73 | -11.8365 | -51.2854 | 2025-05-31 02:30:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 0851c56f-dfab-32f4-93f4-235010d4c0a1 | -11.8368 | -51.2641 | 2025-05-31 02:30:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 060a6828-b0f2-37c6-8e87-ce84edd476a1 | -12.0154 | -49.5272 | 2025-05-31 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 1772c0f7-6cdf-3c65-a17a-4ffd7feba3b7 | -10.6492 | -49.4267 | 2025-05-31 02:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 72c05b28-67d9-39fe-9929-20a6803ecf63 | -10.462 | -47.9428 | 2025-05-31 02:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| c1273718-434c-399f-84c0-247d8d0951fe | -11.8368 | -51.2641 | 2025-05-31 02:40:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 5a5353ee-d552-3a8d-a004-43066156aded | -10.462 | -47.9428 | 2025-05-31 02:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 22d34944-9a38-32c2-9f25-3338c8b10d0f | -12.0154 | -49.5272 | 2025-05-31 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 5ab29220-29c7-3a36-81fd-529efd25d698 | -10.6492 | -49.4267 | 2025-05-31 02:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 11fc5bd4-b8f1-32bf-bd7f-41a2205db5d2 | -11.8365 | -51.2854 | 2025-05-31 02:40:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 0a16b275-1518-30eb-8b24-39d5cf248c29 | -12.0154 | -49.5272 | 2025-05-31 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| f2cdee64-3a8b-34df-b93f-2bb62a3956c8 | -10.462 | -47.9428 | 2025-05-31 02:50:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| c843701e-c2d8-3af5-b060-efe1361d691c | -11.8368 | -51.2641 | 2025-05-31 02:50:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 05a989f9-bbe6-3053-a538-028b73161e86 | -12.0345 | -49.5248 | 2025-05-31 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| f4f89bfd-cdd4-3ef0-8b8c-93249a62245a | -10.6492 | -49.4267 | 2025-05-31 02:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| be4ba153-94cc-3eaf-9b70-361b5fd98906 | -11.8365 | -51.2854 | 2025-05-31 02:50:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 64.1 |
| d734d278-e617-3abb-8d83-79379459c06b | -12.0154 | -49.5272 | 2025-05-31 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 6a3d9b19-3aa5-371d-a87d-1129a69ef7bc | -10.462 | -47.9428 | 2025-05-31 03:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| d76b0c4e-647e-3f83-83d9-1350a4d974a5 | -10.6492 | -49.4267 | 2025-05-31 03:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 78a7d246-6d36-3c40-b1b9-3558ad0669b8 | -11.8365 | -51.2854 | 2025-05-31 03:00:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| d2665f10-8bc4-34c1-8856-af344bfc4b0b | -11.8368 | -51.2641 | 2025-05-31 03:00:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 109.7 |
| f7727427-4cf1-364a-8382-68425541091e | -10.462 | -47.9428 | 2025-05-31 03:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 34de7f5e-a39e-3a56-9dff-84eced9e5c0c | -11.8365 | -51.2854 | 2025-05-31 03:10:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 9d7b6943-d8ac-316f-bb1d-323bf31c9cd1 | -11.8368 | -51.2641 | 2025-05-31 03:10:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 8131fa7c-3d85-35ec-a650-c3b382c67a83 | -12.0345 | -49.5248 | 2025-05-31 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| dfac568d-1a4d-3fc1-a191-c833a15628c7 | -12.0154 | -49.5272 | 2025-05-31 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 085d4c9c-4fc2-3928-aeb0-633c5224a51d | -5.22383 | -37.65784 | 2025-05-31 03:13:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a9999fb2-f809-339a-8a23-001fed91cde2 | -5.22971 | -37.65896 | 2025-05-31 03:13:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0335cab2-12a4-3d76-b857-edf19cd0204f | -5.22721 | -37.66137 | 2025-05-31 03:13:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 8cb49f9c-b4bc-311c-8e20-cbb1170b7854 | -5.22898 | -37.66316 | 2025-05-31 03:13:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cffe7afb-8841-3d3d-ab51-3bae8072b011 | -5.2231 | -37.66205 | 2025-05-31 03:13:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9c2abb82-89c0-3994-ab44-6394e94d9abb | -16.02574 | -43.68494 | 2025-05-31 03:15:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 82595254-ccdd-3d00-acb3-db9252da8882 | -11.8365 | -51.2854 | 2025-05-31 03:20:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 4043e2a4-33a1-35ac-8288-adcda2b5b975 | -11.8368 | -51.2641 | 2025-05-31 03:20:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 2c3e6fc0-23f6-3b47-b8da-12a93328dc92 | -10.6492 | -49.4267 | 2025-05-31 03:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 4a6ce951-b4fc-39c6-b807-674935f2e5ed | -10.462 | -47.9428 | 2025-05-31 03:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| d3077c9e-5206-34f9-a413-a5c1a342a6ae | -12.0154 | -49.5272 | 2025-05-31 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| bbd8eb93-c009-330a-a06a-cdd7aef4d185 | -11.8365 | -51.2854 | 2025-05-31 03:30:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| a749fdcb-b91d-32c2-9fb6-477e65a328e3 | -10.6492 | -49.4267 | 2025-05-31 03:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| b6bca375-e6af-31ee-a6f6-86209132fc0d | -12.0154 | -49.5272 | 2025-05-31 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 4530a7d6-1643-3150-ab11-bd38b76823b7 | -12.0345 | -49.5248 | 2025-05-31 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 41f1a09d-eecd-3882-baf8-368c69b49f80 | -15.8757 | -43.4566 | 2025-05-31 03:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 77.7 |


[Clique aqui para ver as próximas entradas](README5.md)
