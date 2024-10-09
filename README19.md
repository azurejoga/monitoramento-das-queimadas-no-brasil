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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d69a7be3-9cc3-336e-ada9-d30248f017d9 | -3.1194 | -46.646599 | 2024-10-09 00:42:17 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f27c3293-9b70-31b6-876a-bb8b5d3e7b4d | -3.121 | -46.6535 | 2024-10-09 00:42:17 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2041b156-0070-3135-93df-854fa3fc63b5 | -3.7301 | -49.68 | 2024-10-09 00:42:18 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0486a79-e4d8-3e16-bb37-f86c64c73bd5 | -3.4874 | -48.883801 | 2024-10-09 00:42:19 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32c50a4a-f8f8-3552-bf35-6f71c0d0b92f | -3.489 | -48.8909 | 2024-10-09 00:42:19 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f74a062-e70f-3e3f-9308-9de60a9a1b64 | -3.6305 | -49.558998 | 2024-10-09 00:42:20 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 021bdf4b-55e7-3f82-afce-bcf314213e05 | -3.6842 | -50.113998 | 2024-10-09 00:42:21 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10f7707a-89f8-34fb-85bb-bbce56c4a1ff | -3.686 | -50.121899 | 2024-10-09 00:42:21 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d6a6ddb-910b-30b2-aad6-976cd079a1a2 | -3.6967 | -50.169601 | 2024-10-09 00:42:21 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76509b12-e95b-3758-bd52-fbb3ebc08640 | -3.2569 | -49.093201 | 2024-10-09 00:42:24 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 919b7337-cb03-3931-9e23-5f6798187f70 | -3.2585 | -49.100399 | 2024-10-09 00:42:24 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57e9d34c-96dc-3d68-b58b-b76b3a084a05 | -2.7136 | -46.810299 | 2024-10-09 00:42:24 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c4c8a58-9c37-3167-9a27-4b5a8dc4d7d1 | -3.4031 | -50.326801 | 2024-10-09 00:42:26 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 942523ae-02ce-35c5-9c8c-89e763ccc0df | -3.3331 | -50.108501 | 2024-10-09 00:42:26 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd0d5cf0-e0ae-3cc7-9af5-d9058e36c7ab | -3.3349 | -50.116402 | 2024-10-09 00:42:26 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bd59799-b7d1-3e71-b137-30ae737a2b57 | -3.3367 | -50.124298 | 2024-10-09 00:42:26 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d303b4fc-9d6c-3742-b531-4ff782ddaab2 | -3.4803 | -50.8046 | 2024-10-09 00:42:27 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f98c848a-174b-38af-b0a2-557cae58f16b | -2.6437 | -47.358601 | 2024-10-09 00:42:27 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0368991-f5bb-3d84-803f-b5298769c701 | -2.6452 | -47.365398 | 2024-10-09 00:42:27 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1bea2d1-4344-337b-ae63-8feb07382137 | -2.9389 | -48.737701 | 2024-10-09 00:42:28 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be185e7c-8036-39fd-ad8a-e88f329920b4 | -2.9405 | -48.744801 | 2024-10-09 00:42:28 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ca245ab-cb1d-3bc7-8ea0-ae58b19480c9 | -2.608 | -47.338001 | 2024-10-09 00:42:28 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52b48f31-44f6-30cc-90cf-1c434f5ba98f | -2.6096 | -47.344799 | 2024-10-09 00:42:28 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2738112-b505-3605-8352-8480899081b7 | -2.539 | -47.217098 | 2024-10-09 00:42:29 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 091bba6f-fdc3-3be2-863d-2433ec4a6501 | -2.5406 | -47.2239 | 2024-10-09 00:42:29 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17c6e722-164a-3c95-ae1b-10b5dfc6153f | -2.5422 | -47.230801 | 2024-10-09 00:42:29 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64d4b211-5ec8-3bd5-a2db-f8e225bec561 | -2.361 | -46.488098 | 2024-10-09 00:42:29 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41b57b7a-dfb3-31b5-8ea6-1fc40437d040 | -2.5292 | -47.2192 | 2024-10-09 00:42:29 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd155871-80b5-388b-acd6-603262c51e49 | -2.5308 | -47.226101 | 2024-10-09 00:42:29 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bbead9b-be34-392d-a664-c20eaa229dc7 | -2.9496 | -49.191601 | 2024-10-09 00:42:29 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb0cca13-a1c3-3886-b8f2-fe9d42f135b2 | -2.9513 | -49.198799 | 2024-10-09 00:42:29 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99595fb5-592f-3180-aaef-c1814b5d2322 | -2.7945 | -48.556702 | 2024-10-09 00:42:29 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcb68fae-38ad-3dd5-b4bb-c735abe29fb5 | -2.796 | -48.563599 | 2024-10-09 00:42:29 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b3296ff-6fe2-34b6-a51c-0df2054cfde0 | -2.7847 | -48.558899 | 2024-10-09 00:42:30 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8acd5f48-d2ee-3e8a-86ba-a43c3f14f7e2 | -2.7862 | -48.5658 | 2024-10-09 00:42:30 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a89b7e2-e17e-3a3f-b3cd-022b6e3575b4 | -2.7878 | -48.5728 | 2024-10-09 00:42:30 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9e5d413-dcc1-34f0-b5c5-8210f46ee494 | -2.9218 | -49.159901 | 2024-10-09 00:42:30 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc38ab5e-4e65-37c0-b483-0c8398a81032 | -2.9837 | -49.521801 | 2024-10-09 00:42:30 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9eeb0925-9954-36f8-9717-554be8fff548 | -2.9854 | -49.529301 | 2024-10-09 00:42:30 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e580a1d7-e1bf-382d-b7b9-3373de39974e | -2.5399 | -47.625301 | 2024-10-09 00:42:30 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b61ebfd-b8fb-3d69-b338-a261aaca2f1f | -2.3208 | -46.716702 | 2024-10-09 00:42:30 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f27311e7-7adb-3b6a-a3c1-db882d069745 | -2.5368 | -47.611698 | 2024-10-09 00:42:30 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b949031-c578-35cc-87db-9138b9739e6a | -2.5384 | -47.6185 | 2024-10-09 00:42:30 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1f1c226-091a-3b90-aa7e-a2b2c73cc307 | -2.1503 | -46.066299 | 2024-10-09 00:42:31 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 36497fd1-a9ed-3a39-a361-101edf9c0d95 | -2.7414 | -48.685699 | 2024-10-09 00:42:31 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd0757db-3474-3f74-bfa5-f7976763887e | -2.8042 | -49.005501 | 2024-10-09 00:42:31 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d473e11d-311b-3be4-8404-9417ae7bac2c | -2.8058 | -49.0126 | 2024-10-09 00:42:31 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30503903-6462-30f8-9976-3d6a7865c0d0 | -3.1055 | -50.3755 | 2024-10-09 00:42:31 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5bb83b5-39fb-33a7-a201-8fe6426a63cd | -3.1073 | -50.383598 | 2024-10-09 00:42:31 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd55304d-1a50-3238-922b-5d0c2e4457cf | -2.7201 | -48.727402 | 2024-10-09 00:42:31 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46619e88-2034-31b5-a1f1-ebb4b2613935 | -2.7217 | -48.734402 | 2024-10-09 00:42:31 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f17eb189-ca62-35b2-8bb8-9419a92acc3e | -3.2058 | -50.909698 | 2024-10-09 00:42:31 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a993fcd8-a648-3105-a49a-51df8bb643f1 | -3.2572 | -51.227901 | 2024-10-09 00:42:32 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0863cd81-d6cd-3f54-a254-3c6afc580cbd | -3.2592 | -51.236801 | 2024-10-09 00:42:32 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13732157-ef56-3079-8475-38b87ef52c6d | -2.2016 | -46.736198 | 2024-10-09 00:42:32 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8e50683-083e-3332-8aeb-fdc46887d951 | -2.7926 | -49.587601 | 2024-10-09 00:42:33 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31246395-9c14-3ac3-b9d3-e80cb9d4b999 | -2.7943 | -49.595001 | 2024-10-09 00:42:33 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c49ab66e-4e43-3604-a0ee-f45a7557531a | -2.3877 | -47.680901 | 2024-10-09 00:42:33 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adff5e51-ac38-3c63-9395-0efd6838f938 | -2.3764 | -47.676201 | 2024-10-09 00:42:33 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27af00f7-0051-38b4-8d9b-d80c2b2f00f7 | -2.3779 | -47.683102 | 2024-10-09 00:42:33 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8330d6ea-2815-3ef9-acf7-2e83ea763beb | -2.7481 | -49.5275 | 2024-10-09 00:42:34 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1156c85-371b-379d-8224-a44751fc53ea | -2.8924 | -50.388901 | 2024-10-09 00:42:35 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 525b876e-6a52-3fb1-be13-186934d74830 | -2.8921 | -50.705101 | 2024-10-09 00:42:36 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f469482d-c015-3f50-821e-6f5a369dc5fb | -2.5994 | -49.779202 | 2024-10-09 00:42:37 | METOP-C | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0382b91a-cca7-33a3-bc82-0522c4f4d008 | -2.6011 | -49.786701 | 2024-10-09 00:42:37 | METOP-C | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e17fac04-2769-3124-bed4-e833d657b992 | -2.6028 | -49.794201 | 2024-10-09 00:42:37 | METOP-C | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bdb428e-1f45-3a77-8b08-9494477c1b00 | -2.3566 | -48.9856 | 2024-10-09 00:42:38 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07d30851-6ac7-323d-8c2e-08bae1ada70d | -2.3582 | -48.992699 | 2024-10-09 00:42:38 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 625603ed-e3ac-3a14-a4a2-74f519e65ca0 | -3.5609 | -54.318001 | 2024-10-09 00:42:38 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba9035f7-4890-3b2c-a4e2-9adc56d67fdc | -3.564 | -54.3321 | 2024-10-09 00:42:38 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78183782-1637-3dd3-a7c4-3b4ffcbecb64 | -2.3468 | -48.987801 | 2024-10-09 00:42:38 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e610cfad-6f32-3f97-b066-a0937179ef09 | -2.3484 | -48.9949 | 2024-10-09 00:42:38 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15889dae-4238-3a02-9222-21e37fbc3b2e | -3.5511 | -54.320099 | 2024-10-09 00:42:38 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1a36518-43da-3ee0-9602-2bc914ac2aaa | -3.5542 | -54.334202 | 2024-10-09 00:42:38 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 561e5192-f204-3440-80ea-7d533965fddf | -2.4777 | -50.239799 | 2024-10-09 00:42:41 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06b47991-cda9-3231-86a7-6f3e5ab816e7 | -2.4661 | -50.2342 | 2024-10-09 00:42:41 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f66f74e0-00c5-3a63-a33c-17f1309b829a | -2.4679 | -50.242001 | 2024-10-09 00:42:41 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f1bca52-e76c-31e7-bb2b-079ea5b4d9be | -2.4696 | -50.249901 | 2024-10-09 00:42:41 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efd9a2f7-30b9-3778-a20a-6894c5c82fbb | -3.251 | -54.166599 | 2024-10-09 00:42:43 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 248d248a-36c6-38b8-bb0a-45501bfe3fd6 | -3.2541 | -54.180302 | 2024-10-09 00:42:43 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3ba658e-a6ef-3e18-8997-a8aee5762305 | -3.1216 | -53.726002 | 2024-10-09 00:42:43 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8aec4e65-62ed-3f08-b74b-056d0e0558f1 | -3.1245 | -53.738701 | 2024-10-09 00:42:43 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc2c13a3-62a4-3248-809a-099ff69bd89e | -3.1119 | -53.7281 | 2024-10-09 00:42:43 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c3155b3-0244-3d93-a8a0-afa2ded37cf0 | -2.8353 | -52.953499 | 2024-10-09 00:42:45 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f455b7c1-b00e-32e7-8105-f09123b42108 | -2.9737 | -53.7052 | 2024-10-09 00:42:45 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1a09155-0fe6-35c4-8ad1-c92a8e40379f | -2.9765 | -53.7178 | 2024-10-09 00:42:45 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c118016-fdf8-3522-bd79-0fa61a051db6 | -2.9639 | -53.707298 | 2024-10-09 00:42:46 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e548c36d-a7d4-367a-b8ad-8d2c29922d91 | -2.9667 | -53.719898 | 2024-10-09 00:42:46 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a0f1a70-4e1b-3515-8ccf-70e0cd84bd9e | -2.8345 | -53.3144 | 2024-10-09 00:42:46 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afe2149e-02aa-3cc3-8de6-8be27cb4c67c | -2.8732 | -53.941601 | 2024-10-09 00:42:48 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 372788fa-e812-35f3-b11d-94dc6f6d2390 | -2.8635 | -53.943699 | 2024-10-09 00:42:48 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb8133c9-52d3-30db-8ddc-a8f9a32e192c | -2.8664 | -53.956699 | 2024-10-09 00:42:48 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f9cf848-8117-3763-8b4b-f17d325ddf98 | -1.3734 | -47.485001 | 2024-10-09 00:42:48 | METOP-C | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10fc47e2-d2d4-3a3d-ba37-071d6b37c641 | -1.375 | -47.491798 | 2024-10-09 00:42:48 | METOP-C | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a878f2f-e755-3d18-8d10-4a718c5d014d | -2.7405 | -53.943298 | 2024-10-09 00:42:50 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9c50ad2-d3b2-3c9e-83db-42e63f428e73 | -2.8081 | -54.334801 | 2024-10-09 00:42:50 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e47f8012-8a95-3582-8b3b-3d03b78705b8 | -2.8112 | -54.348598 | 2024-10-09 00:42:50 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ac5e96b-c507-3166-a70c-941dfea6bcab | -2.8015 | -54.3507 | 2024-10-09 00:42:51 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5aa456a6-6e14-3344-a9b5-0e91990a0211 | -1.9542 | -50.834202 | 2024-10-09 00:42:51 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b40341c5-1c9a-3bca-b022-ea5c25ddf653 | -1.9561 | -50.8424 | 2024-10-09 00:42:51 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README20.md)
