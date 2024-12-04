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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b6d8035-29d0-3989-8ccd-792c2f6d9cd3 | -2.8197 | -53.0425 | 2024-12-04 06:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| e910ae01-0a29-3ab3-815f-7ef310d53a7c | -3.1086 | -54.6268 | 2024-12-04 06:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| ecae2974-1828-3155-ba33-bff233b5b8bd | -3.259 | -53.659 | 2024-12-04 06:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 0fba83bf-dfb3-3e62-ad30-b9f69554c1ae | -2.8197 | -53.0425 | 2024-12-04 06:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| d60ce72f-ea59-3bf7-9a32-a9c7776ad470 | -2.7942 | -55.3703 | 2024-12-04 06:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| cab07665-d6f5-348c-9773-1d96fc1ae5d1 | -3.2774 | -53.6585 | 2024-12-04 06:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 8228abb4-ca7d-37b6-8c09-6f1527ea848d | -2.7943 | -55.3505 | 2024-12-04 06:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 3abf697f-367a-3b1c-b51e-ccd0787c568a | -1.7545 | -52.6159 | 2024-12-04 06:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| a74153a5-b67c-357d-9f82-732b809ec6f7 | -3.259 | -53.6388 | 2024-12-04 06:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 0a8199ca-2d07-3717-bd73-dc6a1a35c297 | -3.127 | -54.6063 | 2024-12-04 06:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 4c75cc5c-0c71-31b7-be38-79b9a8feaea8 | -1.7544 | -52.6363 | 2024-12-04 06:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 79a41ad7-26fd-3193-8587-8eb6f030fc53 | -2.8196 | -53.0629 | 2024-12-04 06:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| c91114bf-c87c-3b84-9abe-4fa8c24a4c71 | -3.1086 | -54.6068 | 2024-12-04 06:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| b72f7033-4754-3b0e-9c6f-9891a6fbca6c | -3.1269 | -54.6263 | 2024-12-04 06:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 141.6 |
| 4902d815-c82e-3f5c-89d0-89c8d58ea4ad | -3.259 | -53.6388 | 2024-12-04 06:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 105580e6-8535-3105-a5fc-2abea7699c15 | -3.1269 | -54.6263 | 2024-12-04 06:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 162.9 |
| bb08b622-84bd-3f4c-a4b5-cb6f65d70c3d | -2.8196 | -53.0629 | 2024-12-04 06:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| b32685c7-d908-34ee-ab26-182f65a467d5 | -3.259 | -53.659 | 2024-12-04 06:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 8c8c4dea-2478-3948-94e9-b56db8f68144 | -3.1086 | -54.6068 | 2024-12-04 06:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 2c7f372a-0df1-3e95-886b-5feaed4f77f6 | -1.7544 | -52.6363 | 2024-12-04 06:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| cc6531be-0a6b-323b-9468-948333f95e46 | -3.2774 | -53.6585 | 2024-12-04 06:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 32b6e769-c839-342a-93aa-359b6b849c23 | -3.1086 | -54.6268 | 2024-12-04 06:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 5157f183-fead-3010-81bf-9a2d1f68c262 | -1.7545 | -52.6159 | 2024-12-04 06:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 0aa7cc37-35b0-3e56-b3d3-b6102c33231f | -2.8197 | -53.0425 | 2024-12-04 06:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| a95e5797-946d-3fec-8296-f0142ea3f0de | -3.127 | -54.6063 | 2024-12-04 06:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 49c6cde0-b137-361c-af9c-10737a655cdd | -3.259 | -53.6388 | 2024-12-04 07:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 9ebf9e89-8a0e-3189-955c-374f48cb1919 | -3.259 | -53.659 | 2024-12-04 07:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 1d8adad1-6d44-3305-8be2-188f7b9f4be3 | -1.7728 | -52.636 | 2024-12-04 07:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 47cfcf93-5352-3a56-9ce0-0926ff5bca32 | -2.8196 | -53.0629 | 2024-12-04 07:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| efba69fe-8192-38a8-8421-0b59c5c77ecc | -3.2774 | -53.6585 | 2024-12-04 07:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 3fa8d45f-4042-3ea5-901a-b490e661d95b | -3.1086 | -54.6268 | 2024-12-04 07:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 3771860c-54fc-33fb-a2c4-3da5fb4f6a81 | -3.1086 | -54.6068 | 2024-12-04 07:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 7ac88d7c-da6d-32f9-89be-ecd8164d95a2 | -3.127 | -54.6063 | 2024-12-04 07:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 6d143e1c-c5bf-3f90-8384-e924f9324993 | -2.8197 | -53.0425 | 2024-12-04 07:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 10c63fc5-fc14-3877-a218-8ceb6abe8c95 | -1.7361 | -52.6162 | 2024-12-04 07:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| fe5aa7b3-4b9f-30fb-8ddb-5ece656005af | -1.7544 | -52.6363 | 2024-12-04 07:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 48f89563-3616-3d1e-ae42-fe83e80ba742 | -3.1269 | -54.6263 | 2024-12-04 07:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 151.2 |
| 226de9aa-c921-3216-9d68-4e69b5d1f3cd | -1.7545 | -52.6159 | 2024-12-04 07:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| e9632e50-dd0c-3230-8db8-687bd2e73d42 | -2.8196 | -53.0629 | 2024-12-04 07:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| a5f46de0-b854-30b9-ae1f-6f23c27f9779 | -3.1269 | -54.6263 | 2024-12-04 07:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 145.2 |
| 76fd92cb-de90-3bf1-b14a-a2555e62974f | -3.2774 | -53.6585 | 2024-12-04 07:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 8b5b6022-ffd7-305c-bb93-4fc5398d1658 | -2.8197 | -53.0425 | 2024-12-04 07:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 8a54d6d0-1ce7-37b1-bbdd-d845626f9e16 | -3.259 | -53.659 | 2024-12-04 07:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 82f451f4-e0b8-3559-9e31-3729d0d2e2b7 | -1.7361 | -52.6162 | 2024-12-04 07:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 5bb5456e-a933-34d3-8dd3-48ef29d7da41 | -1.7545 | -52.6159 | 2024-12-04 07:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 140.9 |
| 8d280f9d-31df-3ba2-81ee-2aa62322302d | -3.1086 | -54.6268 | 2024-12-04 07:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 507608f8-f900-379b-b284-0e6dcbc501d5 | -1.7728 | -52.636 | 2024-12-04 07:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| dc7ec6af-61a2-3439-b11e-e46a6ce06d80 | -3.127 | -54.6063 | 2024-12-04 07:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 107.0 |
| a180bb6a-4a03-30e0-a781-50f2c2ad00ba | -3.259 | -53.6388 | 2024-12-04 07:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 4a50981a-f8f0-3191-a9ff-bf69db0d385e | -1.7544 | -52.6363 | 2024-12-04 07:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 81b1478e-e4a7-3110-aecb-f3834d92eef5 | -3.1086 | -54.6068 | 2024-12-04 07:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 293e4017-f966-329d-938a-064545e86893 | -2.8197 | -53.0425 | 2024-12-04 07:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| f470e169-e40c-39ec-b650-b88d89088b9b | -3.259 | -53.6388 | 2024-12-04 07:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 7f5c8199-6c42-3a6d-bcd5-648cd6dad53a | -3.259 | -53.659 | 2024-12-04 07:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 0f9af5f6-09ad-3a90-8312-b8888aa4bf40 | -3.1086 | -54.6268 | 2024-12-04 07:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| cc10d4a3-705c-3d8e-8b40-aa09ca2fd13b | -1.7728 | -52.636 | 2024-12-04 07:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| e4abda3b-6891-3276-b2d4-70a16e84e178 | -2.8196 | -53.0629 | 2024-12-04 07:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| c9fb9c9f-4dc7-3172-8f3a-f7246dc6e57d | -1.7544 | -52.6363 | 2024-12-04 07:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| e78ac8e3-13fe-3f2f-8fae-06dff9080135 | -3.127 | -54.6063 | 2024-12-04 07:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| ddb6aa69-5168-3262-9c51-4bda88c39763 | -3.1453 | -54.6259 | 2024-12-04 07:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| f0894232-070f-3f7a-828a-67d5b7afc679 | -3.1269 | -54.6263 | 2024-12-04 07:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |
| ad97ce33-72f3-329f-959d-fb5a9dc41420 | -1.7361 | -52.6162 | 2024-12-04 07:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| e154a97f-8ce7-3dc6-b8c6-be31d6b78f88 | -1.7545 | -52.6159 | 2024-12-04 07:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 71f65e2f-c702-3c1a-a138-ee5e7caae029 | -1.7728 | -52.636 | 2024-12-04 07:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 05a6baa1-0e2a-3244-99b4-a964629ac81f | -3.1086 | -54.6068 | 2024-12-04 07:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| d780fa1d-e9bb-352f-a357-9c302e95dc98 | -1.7545 | -52.6159 | 2024-12-04 07:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 21c501bb-9b61-3ac2-a651-775d75902895 | -3.1453 | -54.6259 | 2024-12-04 07:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| acd1f276-1fbf-3aea-8d6c-1909386811ad | -3.259 | -53.6388 | 2024-12-04 07:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| d55bdf04-7d4b-37ba-b972-3a536c45dc9e | -2.8196 | -53.0629 | 2024-12-04 07:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 84d86ef6-8b29-352c-9614-f03b78554d10 | -3.259 | -53.659 | 2024-12-04 07:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 9cee472a-7db9-38ec-a2db-d389cf4e19bb | -3.127 | -54.6063 | 2024-12-04 07:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| cbc91817-3226-3f2a-b396-7d54ef3df9a6 | -3.1269 | -54.6263 | 2024-12-04 07:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| bf50402f-2c9d-3dd2-bb35-f994f478ac9a | -1.7544 | -52.6363 | 2024-12-04 07:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 9abdd308-673b-33ca-9bbe-1425faa12ea2 | -3.1086 | -54.6268 | 2024-12-04 07:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 0c55d56c-3d7b-31dd-94b8-d23489c2608b | -2.8196 | -53.0629 | 2024-12-04 07:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| eb5d162a-2b10-3ae9-bf70-df7c01a1b258 | -3.1086 | -54.6268 | 2024-12-04 07:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 992d9c04-72dd-3e2e-a5c6-71439ed87e5c | -1.7545 | -52.6159 | 2024-12-04 07:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 3b389de8-75fd-34d8-8d06-0d07353d9cd2 | -5.588 | -45.1638 | 2024-12-04 07:40:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| ce13e5ce-9a92-34e3-a6ae-d383a6573a01 | -3.1269 | -54.6263 | 2024-12-04 07:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 3c0a63ec-8861-30df-bde5-b81373a245aa | -5.5882 | -45.1412 | 2024-12-04 07:40:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| f9624337-8cd6-3bdf-93af-fbe989deda9d | -5.5693 | -45.1651 | 2024-12-04 07:40:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 8e57da72-a9a3-351b-8cce-54e36d9a3e02 | -1.7544 | -52.6363 | 2024-12-04 07:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 07c0c983-dd49-3cd0-947b-6621b4e9e93d | -3.127 | -54.6063 | 2024-12-04 07:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| d2d4bd76-cef5-342a-a233-34a37134696b | -3.1086 | -54.6068 | 2024-12-04 07:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 1da56eef-f575-3175-ac5e-05c405d822e2 | -5.5695 | -45.1425 | 2024-12-04 07:40:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 4c8ff850-5597-3620-abc7-725420f1ef97 | -3.259 | -53.6388 | 2024-12-04 07:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 1bbdc7ea-4f88-34b7-b27f-0baad6952f30 | -3.259 | -53.659 | 2024-12-04 07:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| f85f0a08-5056-3627-a85a-64cdc6e6f2bf | -5.588 | -45.1638 | 2024-12-04 07:50:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 1597b50f-6e53-3223-aac2-9cad440bb507 | -3.1269 | -54.6263 | 2024-12-04 07:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| ae43bcef-9386-3222-b244-3e7b9efd7934 | -1.7544 | -52.6363 | 2024-12-04 07:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 55956c54-8af3-38cd-bb57-e22037e8f976 | -3.1086 | -54.6268 | 2024-12-04 07:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 6ad31a60-6462-38e7-8126-9adbe33dd111 | -1.7361 | -52.6162 | 2024-12-04 07:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| d2760b90-56b2-3f80-9337-0992a645b3c3 | -5.5882 | -45.1412 | 2024-12-04 07:50:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 566ef419-c81c-3d0b-b326-ac42868e73a8 | -2.8196 | -53.0629 | 2024-12-04 07:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 7c8d11fd-99cf-34bb-8b2c-bd6c59e7408a | -5.5693 | -45.1651 | 2024-12-04 07:50:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 9a6ae0f6-c81e-3d9b-8b17-ad9d3444dec6 | -3.259 | -53.6388 | 2024-12-04 07:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 6bd4e093-8596-3d0c-b38a-ad81b8eaaec8 | -2.8197 | -53.0425 | 2024-12-04 07:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| d8ce9f9e-5ce7-30b1-9097-a3d90dc1fabe | -1.7545 | -52.6159 | 2024-12-04 07:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 591af091-782b-317c-9d93-6b133d1b5f1b | -3.259 | -53.659 | 2024-12-04 07:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 02f7c2e5-4481-3653-9618-138cfc0daded | -3.127 | -54.6063 | 2024-12-04 07:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |


[Clique aqui para ver as próximas entradas](README62.md)
