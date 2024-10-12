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
| 701273dd-bd31-3564-b318-58b81b288f64 | -3.0486 | -51.124599 | 2024-10-12 01:20:19 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e307f46-da7b-3083-8953-bbbbc1d513d2 | -3.0515 | -51.1367 | 2024-10-12 01:20:19 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93e25abb-ff9a-34b4-8f12-80460a47e222 | -3.9646 | -55.345501 | 2024-10-12 01:20:20 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ad0e63f-e11a-374f-a899-d06ad633ce8e | -3.9629 | -55.338402 | 2024-10-12 01:20:20 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc2309b9-b2ff-340f-980b-5a12cd2593c4 | -2.9627 | -51.283298 | 2024-10-12 01:20:21 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acdf9bff-9a60-3604-a390-6ba95b982424 | -3.9992 | -56.076599 | 2024-10-12 01:20:22 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6396e1d4-003d-378b-aa51-c903aa9ddf96 | -4.0008 | -56.0835 | 2024-10-12 01:20:22 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7861c77-966a-372b-93e7-1b3e909bf1a8 | -4.0126 | -56.269402 | 2024-10-12 01:20:23 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e23dd788-6e15-3962-a69d-e28896fbd8f1 | -2.829 | -51.326801 | 2024-10-12 01:20:23 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d335db7e-7e44-3c28-a0fd-2456d1ef3279 | -2.8318 | -51.338501 | 2024-10-12 01:20:23 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ec7023b-1543-381c-9b14-b6b08ce90225 | -2.8193 | -51.328999 | 2024-10-12 01:20:23 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfa19af6-a80a-3a3e-8b02-6379a08bdcca | -2.8221 | -51.340801 | 2024-10-12 01:20:23 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 599be3c3-bf5f-3685-b55c-2b54ae7531e0 | -3.6156 | -54.730099 | 2024-10-12 01:20:23 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65934760-66c9-3d62-9ad9-d7a3d2c4d5ba | -2.8856 | -51.6535 | 2024-10-12 01:20:24 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f16bb3ed-9d0d-3048-a617-92a5dd9c092f | -2.8882 | -51.6647 | 2024-10-12 01:20:24 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd610fa7-e61d-3d78-9670-66debc974450 | -2.9092 | -51.7537 | 2024-10-12 01:20:24 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7376e40a-1504-35aa-8643-2c913ed0ae8a | -2.8758 | -51.655701 | 2024-10-12 01:20:24 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76706e2d-dab0-3fd7-98fe-2cd3401be4fd | -2.8784 | -51.667 | 2024-10-12 01:20:24 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b69b73f5-d8cf-3eab-9d9a-18b43c71316b | -2.7928 | -51.3475 | 2024-10-12 01:20:24 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 124cbf17-09bf-3e28-9c3e-680b38fe7a10 | -2.7955 | -51.359299 | 2024-10-12 01:20:24 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5008cf1d-5034-356f-8be6-69aef333f4a1 | -2.7983 | -51.371101 | 2024-10-12 01:20:24 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a88d569-b82b-3176-844e-e33e11497f9d | -2.7831 | -51.3498 | 2024-10-12 01:20:24 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f5562fe-b6ae-3bf5-bd48-13f0edd451b6 | -2.7858 | -51.361599 | 2024-10-12 01:20:24 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 645cc269-d830-3d86-8556-e1542595a67c | -2.7886 | -51.373402 | 2024-10-12 01:20:24 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b891c27-708c-3535-b99f-5b23d552270c | -2.776 | -51.3638 | 2024-10-12 01:20:24 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b499611-d0d5-3673-b2ea-d0a9ca8de144 | -3.6068 | -55.449001 | 2024-10-12 01:20:26 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f101674-937e-37a5-bf1d-63dbf14d5dbc | -3.6085 | -55.4562 | 2024-10-12 01:20:26 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47bc5399-dadd-33ca-9b6c-19f93f795236 | -3.6102 | -55.463299 | 2024-10-12 01:20:26 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b0f4952-3529-3208-949b-020fa580e01c | -2.9931 | -52.900398 | 2024-10-12 01:20:27 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccdcd2e7-ff46-3f49-a45e-1b44977479be | -2.9953 | -52.909801 | 2024-10-12 01:20:27 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 364328e5-f086-32e6-9991-2e635f502596 | -2.9834 | -52.902599 | 2024-10-12 01:20:27 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d42ddb7b-3ad2-3214-b283-104ef256587b | -3.6005 | -55.555401 | 2024-10-12 01:20:27 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24a55e96-9b5e-3e8e-93b2-c2b459aa80d1 | -3.5349 | -55.450199 | 2024-10-12 01:20:27 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 062be0f3-1daa-3843-9f42-1f19e74b661f | -3.5366 | -55.457401 | 2024-10-12 01:20:27 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d042d9a-3f15-395b-af12-2ea5d28d1d18 | -3.5202 | -55.431 | 2024-10-12 01:20:28 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58b9e9d3-b479-3374-a9b8-e15c793dd9ed | -3.5218 | -55.438099 | 2024-10-12 01:20:28 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1855f6d4-0871-3652-a8a8-e79e0833748b | -3.5235 | -55.445301 | 2024-10-12 01:20:28 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab468954-143e-32a5-a96c-8ef087a29d67 | -4.7354 | -60.772099 | 2024-10-12 01:20:28 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 239b3f9a-38bc-3b9f-9f39-eb5b54daaccc | -4.7374 | -60.7813 | 2024-10-12 01:20:28 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 939a2fe7-fabc-32ce-83ed-9d8bbfad2747 | -4.7395 | -60.790501 | 2024-10-12 01:20:28 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2ea84c59-91d7-3f3a-9e0d-75117dfc58b2 | -3.5137 | -55.447498 | 2024-10-12 01:20:28 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f08a1e5-73df-3c02-8823-de29b9c7a03e | -4.7235 | -60.764999 | 2024-10-12 01:20:28 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 76b07e0f-4851-3810-9f91-b5a7a89eef54 | -4.7256 | -60.7742 | 2024-10-12 01:20:28 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0adf6131-98d2-354d-9972-8557b9b8345b | -4.7276 | -60.783401 | 2024-10-12 01:20:28 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 13e62023-142a-3c6b-b270-653abd72139c | -4.7297 | -60.792599 | 2024-10-12 01:20:28 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2d824ecc-a050-3ae4-8ab8-3e345b609e85 | -4.7178 | -60.785599 | 2024-10-12 01:20:28 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5a688e7c-5628-31ca-b20f-882ae102a8d3 | -4.7199 | -60.7948 | 2024-10-12 01:20:28 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 192eddff-b362-34b0-bd68-cb7ef67a24ac | -4.7101 | -60.796902 | 2024-10-12 01:20:28 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 37908867-9556-3e91-8252-e9e4176b1739 | -4.7121 | -60.806198 | 2024-10-12 01:20:28 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cfe1ba68-8dd5-389c-b063-117a0b3dc0c4 | -4.7142 | -60.815399 | 2024-10-12 01:20:28 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 708010a9-bbb9-36c4-b3fb-c49160d6a92a | -4.7004 | -60.799 | 2024-10-12 01:20:28 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7c88d636-4206-3b17-9f56-cedd5c1855e2 | -4.7024 | -60.8083 | 2024-10-12 01:20:28 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 48056b3f-d800-3394-8934-8569aad6c5b4 | -2.6515 | -52.541401 | 2024-10-12 01:20:31 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab0ef636-4ffa-3299-b51d-427cd70a7fed | -4.2716 | -59.987499 | 2024-10-12 01:20:32 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 211b294d-1d49-3fbb-94f3-6a4587238d32 | -4.2735 | -59.9958 | 2024-10-12 01:20:32 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8881f955-7afd-3e5d-a85f-acd7b7651e1c | -4.2618 | -59.989601 | 2024-10-12 01:20:32 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0bf22c77-6699-30b9-9208-c668055b76eb | -2.9672 | -54.1138 | 2024-10-12 01:20:32 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45653767-877b-3a05-b3bf-19556d62e8b6 | -2.9691 | -54.121899 | 2024-10-12 01:20:32 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3071cd1f-821c-3fe3-b547-351f81794dfd | -4.2213 | -59.946701 | 2024-10-12 01:20:33 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d4c18220-d72c-3162-bbb7-41afaa7f8e5b | -4.2232 | -59.954899 | 2024-10-12 01:20:33 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0e6f835a-dbb8-3f88-b53b-1ca98614fde5 | -2.6832 | -53.337601 | 2024-10-12 01:20:33 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b79a4a46-0e12-3773-b6d1-273494c7b399 | -2.6853 | -53.3466 | 2024-10-12 01:20:33 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a197bf25-8ceb-3c3a-bbe3-cd7a340e86d6 | -2.6734 | -53.339802 | 2024-10-12 01:20:33 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b7c5a02-37b4-3cee-89be-08a8a3b7b338 | -2.6755 | -53.348801 | 2024-10-12 01:20:33 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26730c3d-4860-38b5-b03b-9ab885a7cb40 | -4.1901 | -59.944801 | 2024-10-12 01:20:33 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0950d520-9c20-3e67-9942-993d3db09683 | -4.1919 | -59.953098 | 2024-10-12 01:20:33 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 67643d19-77a8-3b64-b43e-b9b393bd01ad | -2.6637 | -53.342098 | 2024-10-12 01:20:34 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5109d955-38d9-33bf-b710-5026f026afdf | -2.6658 | -53.351002 | 2024-10-12 01:20:34 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54ad89a0-21f3-32db-893e-c1162372f1a7 | -2.7978 | -54.006199 | 2024-10-12 01:20:34 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1030fcb8-d645-3a5e-9361-798e5e8a37f0 | -2.7997 | -54.0144 | 2024-10-12 01:20:34 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7be430fa-1aef-3667-b4bf-2c33221e170c | -2.8016 | -54.022598 | 2024-10-12 01:20:34 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95600f5a-7b7b-393a-816b-76919dc9ca42 | -2.815 | -54.080002 | 2024-10-12 01:20:34 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 185330e5-10a5-3fd9-a722-73acbaa3ef99 | -2.7918 | -54.024799 | 2024-10-12 01:20:34 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab33f62b-94b8-3658-8340-b9e575425b9a | -3.9399 | -59.111099 | 2024-10-12 01:20:34 | METOP-C | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 170d9335-9253-3f3d-95c9-99ef6e9f4d62 | -3.9416 | -59.118698 | 2024-10-12 01:20:34 | METOP-C | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 57710f5d-c795-3fb9-a682-55b1e3616344 | -3.733 | -58.472401 | 2024-10-12 01:20:35 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b6cd18a3-f97f-3c44-add6-db836c6cad54 | -3.875 | -59.7341 | 2024-10-12 01:20:38 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a1e4df19-0f9c-35c2-948d-fcf6a3262216 | -4.0087 | -60.371899 | 2024-10-12 01:20:38 | METOP-C | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3d9a7e02-d4d3-3ed2-956a-b2b29c0a99fe | -4.0106 | -60.380501 | 2024-10-12 01:20:38 | METOP-C | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ecd8bda1-7246-30db-b924-cf170a6fa591 | -4.0125 | -60.389099 | 2024-10-12 01:20:38 | METOP-C | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ddf2f524-8f95-3dc8-8abb-b7fad65bf57e | -4.0008 | -60.382702 | 2024-10-12 01:20:38 | METOP-C | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 83cd04ef-393b-350b-96e5-6add7036610d | -4.0027 | -60.3913 | 2024-10-12 01:20:38 | METOP-C | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 23c759ce-69ca-35d3-868c-952a9c5e4585 | -2.5886 | -54.2593 | 2024-10-12 01:20:38 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5916f91f-9a83-3dc3-a7ff-45aff8be834d | -3.1784 | -57.397202 | 2024-10-12 01:20:40 | METOP-C | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e7996b22-f6af-39ae-98e4-cd997288da85 | -2.2632 | -53.480202 | 2024-10-12 01:20:41 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45775ba4-253f-3a4c-a960-e01269fab951 | -3.1786 | -57.938599 | 2024-10-12 01:20:42 | METOP-C | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8b0f5c54-f2aa-3118-86f5-dc34560f397b | -3.1802 | -57.945599 | 2024-10-12 01:20:42 | METOP-C | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 59d3b810-7b67-3e78-bcee-7103c0c24bc7 | -3.4824 | -59.5 | 2024-10-12 01:20:43 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7492ac52-ddd8-3adc-a7a8-056258d32f56 | -3.4563 | -59.6115 | 2024-10-12 01:20:44 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1fd13d4e-e86c-3edc-af7f-b7afbb87a849 | -3.4447 | -59.6059 | 2024-10-12 01:20:44 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1a5ebc23-6e5f-35c7-9099-e11cce80efc9 | -3.4465 | -59.613701 | 2024-10-12 01:20:44 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0f80e481-97fb-3627-8dd7-1dab769588a8 | -3.4483 | -59.621498 | 2024-10-12 01:20:44 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3f3e9ac0-5bc8-36b9-8aea-0494a3365444 | -2.1972 | -54.482498 | 2024-10-12 01:20:45 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcfc0644-3869-3de4-9b3f-e98f97abb5d9 | -3.2204 | -58.935398 | 2024-10-12 01:20:45 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1a3fc62d-0652-3f5b-a59e-960e2f22d65b | -2.1135 | -54.699799 | 2024-10-12 01:20:48 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52dce615-5922-361e-9131-938c8076b51b | -2.4318 | -56.4361 | 2024-10-12 01:20:49 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41285b8e-6915-387e-9a50-ee01fc32a56f | -3.1041 | -59.375099 | 2024-10-12 01:20:49 | METOP-C | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6c70ea25-fc78-3271-a142-2885132b090f | -2.6822 | -57.436199 | 2024-10-12 01:20:49 | METOP-C | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4fc68adc-d0a2-3226-986f-031e28960e84 | -3.058 | -59.3536 | 2024-10-12 01:20:50 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 347f3d14-9772-3e51-a004-d13ea1970f8f | -1.8933 | -54.416698 | 2024-10-12 01:20:50 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README20.md)
