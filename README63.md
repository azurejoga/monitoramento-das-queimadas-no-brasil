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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c43e5b5e-2148-338c-88b0-2a24e2b5b0b6 | -4.81031 | -48.34089 | 2025-11-16 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75cd709d-44fa-3e5c-85f5-dc6ef3ca2b4c | -2.96972 | -53.21571 | 2025-11-16 05:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb78130b-29ad-3430-9f70-46184dddcda6 | -3.52816 | -56.3178 | 2025-11-16 05:25:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af75875d-1509-34fd-8413-c8460daf14d0 | -4.04994 | -54.84252 | 2025-11-16 05:25:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d02ecc1-6f92-3e9d-b982-8547b484a759 | -5.12227 | -55.96998 | 2025-11-16 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3e7a1af-b358-32a3-a2b3-e51a6d9e1ccb | -5.12999 | -55.97116 | 2025-11-16 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d80d4b7c-71a3-3feb-abe6-832fd566dba3 | -2.79483 | -54.861 | 2025-11-16 05:25:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9a5917c-522e-3669-9d34-fc92e9b7c05d | -4.15284 | -50.22641 | 2025-11-16 05:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69ea7592-c60d-39ae-96ba-d8f0dd33667d | -2.52031 | -47.80827 | 2025-11-16 05:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d5a6edd5-3c52-310e-9e8b-e982c255a392 | -1.6481 | -53.66957 | 2025-11-16 05:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c540d076-732e-3c3b-83da-6c4af5a03a50 | -2.88581 | -51.42822 | 2025-11-16 05:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f6564545-cb10-325d-ba42-6752fa22f631 | -2.69232 | -49.07707 | 2025-11-16 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40549aa0-4e90-30c8-9eb9-60af2b901e2f | -3.02201 | -51.60135 | 2025-11-16 05:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a2f8339-691a-34c2-bbf1-f8e02b537736 | -2.8859 | -53.28413 | 2025-11-16 05:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 228f9c9f-66a3-3bd7-87ff-45ed6135b8d0 | -3.4207 | -50.35025 | 2025-11-16 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c23d2ea2-4b85-3504-8af7-ac052752a07d | -3.3035 | -53.8472 | 2025-11-16 05:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09b72482-aec4-3f4b-8c35-f991f86df156 | -2.41587 | -53.94469 | 2025-11-16 05:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 825e0fcf-81e1-37f1-be8f-fdbd9dbea11c | -2.69296 | -49.07283 | 2025-11-16 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61400f5d-3dc8-36e0-bb99-f1c282dec98e | -1.64749 | -53.67354 | 2025-11-16 05:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa91370b-0e52-3699-b3f6-2c3f4e498f0c | -2.58322 | -51.87223 | 2025-11-16 05:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba593217-c1c3-3d91-b86a-06299378e817 | -5.12928 | -55.97597 | 2025-11-16 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e19b9917-ed5c-335a-872f-ecf9004f3c8f | -1.22232 | -53.36793 | 2025-11-16 05:25:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea1dcf23-9dbe-3d71-a991-22a7c44ace13 | -3.03556 | -54.59249 | 2025-11-16 05:25:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d12283a-99fd-3273-af7f-5fabd9ced283 | -7.21724 | -47.97857 | 2025-11-16 05:25:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b23465c-64aa-314e-b4f1-c5b8c294289d | -4.72817 | -46.37691 | 2025-11-16 05:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32a9014e-4c96-3c84-9fc2-d40882add73d | -1.93081 | -56.5511 | 2025-11-16 05:25:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30b9e135-7621-3955-a9db-c280b640474c | -4.69942 | -46.30845 | 2025-11-16 05:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7914c767-ebfa-3d60-b0e5-c89dea05c499 | -2.17934 | -52.09093 | 2025-11-16 05:25:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fae2f3f6-54c5-3a68-b4de-db6bf36d4e0f | -3.41964 | -50.35749 | 2025-11-16 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d6d53213-eea2-34f1-9811-223486572ce8 | -1.32638 | -54.21973 | 2025-11-16 05:25:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3bf15820-ea66-3da7-8b7a-cd6562c34763 | -2.51953 | -47.81354 | 2025-11-16 05:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1af4cc20-c7d5-3c29-9cfa-7b5a324e3270 | -3.46555 | -50.12241 | 2025-11-16 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77b3a394-83c8-3903-bbc6-e44cded5766b | -4.70105 | -46.30739 | 2025-11-16 05:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5dc68c5f-6346-312e-b138-152d35fb8132 | -1.84704 | -56.37109 | 2025-11-16 05:25:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 350fb92b-ffdc-39a1-8142-3eb2706c9b0b | -6.81503 | -48.78552 | 2025-11-16 05:25:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc2dc407-1fb7-327a-bc5e-11ebb2455600 | 0.66216 | -56.89182 | 2025-11-16 05:25:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 177383f8-1583-344c-9c0a-7a510a5b5c6e | -7.22897 | -47.98099 | 2025-11-16 05:25:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d50f5e8-b487-3f09-be9d-4e5ddf51c1bb | -2.89103 | -53.28044 | 2025-11-16 05:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| bd02c454-381e-33c1-b6f7-b65613e8dc64 | -3.02982 | -54.60261 | 2025-11-16 05:25:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ebc3b17-a6fd-353b-a739-bf21612d1d54 | -7.71201 | -47.29493 | 2025-11-16 05:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1736ee65-2669-37ea-be96-19b56818d4cc | -1.34765 | -54.61116 | 2025-11-16 05:25:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 84fc8c49-c63c-30ee-84e1-afef4770f22e | -3.45995 | -50.12159 | 2025-11-16 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d67b0e4d-446f-393d-916f-cdcea389c382 | -1.98733 | -47.34789 | 2025-11-16 05:25:00 | NPP-375D | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cff9f642-09e6-352b-a8c4-ec59027f73a5 | -6.81674 | -48.78613 | 2025-11-16 05:25:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76c1ff55-ec90-3180-be84-3e9ce3942407 | -4.74265 | -46.37807 | 2025-11-16 05:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0eab5f38-5830-3d29-8775-57d3c086c75a | -2.6864 | -49.07617 | 2025-11-16 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fa9e71ce-ee35-32ad-86c4-1227d2d44771 | -3.81418 | -49.11031 | 2025-11-16 05:25:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5aa81bf0-b509-3e6a-86ca-7d0572f9911f | -3.42015 | -50.35401 | 2025-11-16 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6493a035-218d-3d0a-a029-3d6c533273f1 | -2.95372 | -48.58706 | 2025-11-16 05:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f183d486-377d-3cd0-85f0-45d5b73af65b | -1.83411 | -53.80408 | 2025-11-16 05:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fbbda8b-d036-3fde-b9da-fec1fb9c634c | -7.71508 | -47.3006 | 2025-11-16 05:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a711afec-0aaf-349f-8c41-bd31c20ddb68 | -3.29943 | -50.07534 | 2025-11-16 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7298cc4-9b73-3c5e-879f-104ff1c41b4a | -1.24954 | -55.87772 | 2025-11-16 05:25:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f61eb33-df40-3af7-84b7-e023400e89ef | -6.14615 | -48.04523 | 2025-11-16 05:25:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 395cecfe-25d2-3e8e-9697-ca9228f4ac79 | -4.72716 | -46.3842 | 2025-11-16 05:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d99f0a79-08f9-3490-b102-df0f2185111a | -1.34366 | -54.61059 | 2025-11-16 05:25:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c1e33e08-496b-3702-8734-48f2d88c6d86 | -4.01998 | -48.80746 | 2025-11-16 05:25:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a221a3db-1bf4-3bc8-8bab-7a3eb0018266 | -3.20327 | -51.5853 | 2025-11-16 05:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b4ee8c5-a4b1-3710-8371-85327e29943c | -0.87459 | -48.0825 | 2025-11-16 05:25:00 | NPP-375D | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ffdf92d-00b2-3f2f-9f0e-2d73a46998b8 | -1.83774 | -53.80864 | 2025-11-16 05:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 803d66f8-e72d-388b-abe4-24a04a66b934 | -3.40021 | -50.18705 | 2025-11-16 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2bd2962f-46e8-3a13-aafd-504eb1372826 | -3.08117 | -52.92243 | 2025-11-16 05:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 168e9731-070f-3e1e-b8ba-e64ab324f4dc | -2.57832 | -51.87148 | 2025-11-16 05:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1cc262f6-369d-37fe-930f-f762e49c0d0e | -2.96239 | -53.21793 | 2025-11-16 05:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51b190a1-e3b7-31a3-a159-f88880ba4edd | -4.69094 | -46.52045 | 2025-11-16 05:25:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| efae7b3a-46f8-323b-9df9-fe4ff6c621e1 | -5.12501 | -55.96835 | 2025-11-16 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f616a04-a64c-3849-bb09-69b1dd3a9096 | -1.19619 | -53.72096 | 2025-11-16 05:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff3d17cb-3d9f-3dc6-85cc-f80aa3c31f4e | -3.19444 | -57.05032 | 2025-11-16 05:25:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74af7dad-f758-3944-87f7-083160215e9a | -5.62367 | -53.43597 | 2025-11-16 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e4c83e5-6d83-3f4c-8f56-b5a0cb48aaa6 | -2.95303 | -48.59173 | 2025-11-16 05:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cbd8f7ec-d4ab-394f-822d-bf524e4e921e | -1.34161 | -54.60728 | 2025-11-16 05:25:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1395597-73f3-32bf-aa7a-d5cb9eea647c | -1.83714 | -53.81254 | 2025-11-16 05:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1df39e89-cbb7-331b-98a5-92d58cf56d84 | -3.33011 | -50.27683 | 2025-11-16 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08e36fcc-dec1-379f-9c46-6a5dcac28398 | -2.52595 | -47.81438 | 2025-11-16 05:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 7d1226e7-3581-3b1c-838c-2a6690df7333 | -5.12575 | -55.96354 | 2025-11-16 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 406c6ef1-24c4-3b41-9ad4-02fff365016c | -3.38573 | -50.13174 | 2025-11-16 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a28f8260-304a-3d8d-9ae2-5716fbcde24d | -1.34561 | -54.60786 | 2025-11-16 05:25:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bdcee2e1-7d5d-38a9-ac2b-add8ba2d0456 | -2.51314 | -47.81248 | 2025-11-16 05:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ee5c03e9-02fa-348d-a878-30ff62361c14 | -4.25001 | -50.05295 | 2025-11-16 05:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 29861a76-43b3-3180-b32d-83af781f8b76 | -4.11483 | -50.05393 | 2025-11-16 05:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e189ed6-2e44-3118-9115-06b66c0e1f55 | -3.41465 | -50.35314 | 2025-11-16 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e99b8952-c20e-31ff-9d1c-8d99039f3a95 | -2.518 | -47.81237 | 2025-11-16 05:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1cae8dc2-b473-3293-b5dc-a04c922e9e9a | -1.18268 | -53.58258 | 2025-11-16 05:25:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5900739-5038-3c19-8f7c-af7af76ea309 | -2.80435 | -52.96106 | 2025-11-16 05:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f4fb312-c6c7-3aef-842c-4f4e0586a832 | -3.08724 | -51.54481 | 2025-11-16 05:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfacb3b4-a709-33e5-af9d-cfa4c38d67a4 | -3.41451 | -52.36417 | 2025-11-16 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ddc30a3-e2f8-3101-8b77-0e8586502776 | -5.12684 | -55.96578 | 2025-11-16 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f61f0c86-ef76-3507-bcb4-60f7cdb4008c | -4.5 | -50.11664 | 2025-11-16 05:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fa3a9132-cad3-39f1-9666-860a90ea7e43 | -3.20282 | -51.58824 | 2025-11-16 05:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bdf15129-6ff9-3075-84b8-f0e24f7707b7 | -2.51161 | -47.81132 | 2025-11-16 05:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0f61e467-b1aa-38d5-ab5b-7b5850cfbc0e | -3.20831 | -51.58608 | 2025-11-16 05:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4795ca51-5a83-3fdc-8b37-7cb137e79758 | -2.79914 | -52.96472 | 2025-11-16 05:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35a0c508-82fa-3542-88e4-47cf6d819241 | -2.51877 | -47.81866 | 2025-11-16 05:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 8549447c-e1c6-3cff-89c8-75115a0a99a2 | -4.73337 | -46.37838 | 2025-11-16 05:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c13627a5-1fd1-3b1d-b664-23f1dc43fa42 | -4.69293 | -46.3131 | 2025-11-16 05:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b8a0ca17-4a49-31b3-a4fa-a7a6cae3ccdd | -2.85639 | -51.27756 | 2025-11-16 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c85c250-4522-3349-983a-d69db74343d7 | -1.99388 | -47.34879 | 2025-11-16 05:25:00 | NPP-375D | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5073293-2bc0-3dca-96ed-bf673a484f07 | -4.7406 | -46.37897 | 2025-11-16 05:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ff592ef3-45fb-309e-9724-5c5ae2ced1de | -5.63981 | -47.74418 | 2025-11-16 05:25:00 | NPP-375D | AXIXÁ DO TOCANTINS | TOCANTINS | Brasil | 1702901 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 15512bd2-5c26-3673-924e-6b805848cb91 | -3.30782 | -53.84787 | 2025-11-16 05:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README64.md)
