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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a21571d-ccbf-3f27-878a-c497277855da | -2.8738 | -48.2552 | 2024-10-19 00:55:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 62bfc0ae-521c-3657-88e2-c7679056cc2b | -2.8739 | -48.2336 | 2024-10-19 00:55:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| d8a87c81-1520-3e52-8dea-a37eb79b2ffd | -2.9489 | -52.9174 | 2024-10-19 00:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 3a1545be-2a52-3635-85dd-47f245176ee9 | -2.9489 | -52.897 | 2024-10-19 00:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 1c027605-1772-3e53-91f3-7e779ace6f7b | -2.9673 | -52.9169 | 2024-10-19 00:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 2b5d9342-c7dc-3520-a5ae-44c3181068c7 | -3.3007 | -44.1762 | 2024-10-19 00:55:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 32589e92-3bbf-3938-bfe1-03a00bed589f | -3.3008 | -44.1533 | 2024-10-19 00:55:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 59.0 |
| b67fc298-c2d0-34e0-83ac-59c3421ec094 | -4.1727 | -51.2337 | 2024-10-19 00:55:30 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 58474b82-3bd0-396c-887d-66c8823550e3 | -4.4167 | -50.535 | 2024-10-19 00:55:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 48cc0e35-7378-3849-b352-6b0b52c072c1 | -4.6028 | -44.6133 | 2024-10-19 00:55:32 | GOES-16 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 8f461d24-d73e-3f5c-9daf-9095c59c9d68 | -4.7436 | -45.8024 | 2024-10-19 00:55:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 150b6b19-e1a0-3d0b-8588-01216d731a31 | -7.6815 | -47.3213 | 2024-10-19 00:55:49 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| eb5dd70d-276c-3bb6-b36f-ffbf4680c091 | -9.0344 | -67.4826 | 2024-10-19 00:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 35.1 |
| b29762c0-13e6-3ae8-beb5-b836b0ded298 | -9.0344 | -67.4641 | 2024-10-19 00:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 282.0 |
| c1f1a168-c81a-3e21-8b49-49a3e66eef90 | -9.0345 | -67.4455 | 2024-10-19 00:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 216.4 |
| eef5bc3c-37c4-3c03-8f36-8d052722724e | -9.053 | -67.4636 | 2024-10-19 00:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 511d8d5c-3a06-3d2d-9535-1521577342fb | -9.053 | -67.4451 | 2024-10-19 00:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| c68df489-585b-3e72-9129-f6cd844a9a16 | -10.1384 | -36.4921 | 2024-10-19 00:56:02 | GOES-16 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 104.7 |
| fb50eff3-6df1-3158-a112-647058f12e8a | -10.1389 | -36.4652 | 2024-10-19 00:56:02 | GOES-16 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 93.2 |
| 20fc4932-c449-33d2-a80d-357a701a8a68 | -12.004 | -63.5199 | 2024-10-19 00:56:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 67827ae9-a21f-3ca8-a495-561eed523f22 | -12.0041 | -63.5008 | 2024-10-19 00:56:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.1 |
| a4c2df9c-ed07-3e26-9d7e-c060f26283b5 | -12.4958 | -63.3024 | 2024-10-19 00:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.3 |
| d3e198f3-16bc-3009-9e7b-d7451fe72734 | -12.496 | -63.2832 | 2024-10-19 00:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.5 |
| df6c0199-b541-3d8c-a66f-d12baa7581c2 | -12.5147 | -63.3014 | 2024-10-19 00:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 83ce3391-6ab3-34b1-9528-5b8975698261 | -12.5149 | -63.2822 | 2024-10-19 00:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 7e8cb6ba-0a72-34da-bbfb-223e1e7226f9 | -12.5336 | -63.3003 | 2024-10-19 00:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 11a59b12-6059-3f4c-a098-8ac9109834ce | -12.5338 | -63.2812 | 2024-10-19 00:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 6f28667a-e21c-35d3-8d7a-a63abb6ea107 | -1.1375 | -47.3179 | 2024-10-19 01:05:12 | GOES-16 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 580439d3-df77-3b77-8021-ff9ab1d513f7 | -2.6509 | -48.4985 | 2024-10-19 01:05:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 57bc4ff3-5f56-35f8-afa2-b111566f499f | -2.7885 | -51.3618 | 2024-10-19 01:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| a166528c-f259-3339-b7a1-8995fdaeb5c7 | -2.8069 | -51.3613 | 2024-10-19 01:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| e7a0420d-8cea-38fe-97f6-b1a9b353bd2f | -2.8738 | -48.2552 | 2024-10-19 01:05:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| a7890d2d-18d7-36dd-98f6-871ecf90f334 | -2.8739 | -48.2336 | 2024-10-19 01:05:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 31c088ca-c529-3f74-843d-70053c960b8e | -2.9489 | -52.9174 | 2024-10-19 01:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 135.1 |
| b4e79379-e71c-352d-a020-223cb8acbdbb | -2.9489 | -52.897 | 2024-10-19 01:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 5160e113-992a-30c6-989c-318e28607172 | -2.9859 | -52.8554 | 2024-10-19 01:05:23 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| b62a2a41-048a-38c9-b3da-13616faecc0d | -3.4202 | -50.2164 | 2024-10-19 01:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| dffd6ce6-ee94-3829-9d5d-d3ed9294dd86 | -3.7116 | -51.1261 | 2024-10-19 01:05:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 94b576de-3df3-33c7-8ccb-d8cdea10a0af | -3.7117 | -51.1053 | 2024-10-19 01:05:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 18dcb7e9-3d1a-3b5c-8d16-7b4569ed10d1 | -3.7301 | -51.1047 | 2024-10-19 01:05:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 9956f633-ef80-38d6-ab69-9b6ad4f27f30 | -4.4167 | -50.535 | 2024-10-19 01:05:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 2991eee4-2eff-365e-9a23-e5576b2514ab | -4.6873 | -45.8504 | 2024-10-19 01:05:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 0d5b7619-2f9b-3192-b7c9-5e7952e4e83a | -4.6875 | -45.828 | 2024-10-19 01:05:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 56197210-1828-3862-9893-cca4f4d8d949 | -4.706 | -45.8493 | 2024-10-19 01:05:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 80ff0b0f-e701-3072-bd86-0c94c6405071 | -4.7061 | -45.8269 | 2024-10-19 01:05:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 92.5 |
| b5019baf-caa0-35fc-977a-b05beaa92ff8 | -5.721 | -68.6862 | 2024-10-19 01:05:39 | GOES-16 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 2214da68-12d9-39d8-8db3-fa09fee2a501 | -9.0344 | -67.4641 | 2024-10-19 01:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 308.9 |
| 39c9c3c8-e944-3e9d-9894-0856dfaeb3ec | -9.0345 | -67.4455 | 2024-10-19 01:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 223.1 |
| c5e36c1c-673e-380e-8f59-2388e1fe427f | -9.053 | -67.4636 | 2024-10-19 01:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 8ce122a3-4b55-3eb8-8a74-8973397c0a20 | -9.053 | -67.4451 | 2024-10-19 01:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 8003f0b4-c145-3854-ba5e-75ddeb6491e6 | -9.7177 | -36.3511 | 2024-10-19 01:06:00 | GOES-16 | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 69.5 |
| 278b5383-9804-3e02-bb12-1b2288944d86 | -12.004 | -63.5199 | 2024-10-19 01:06:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.7 |
| d91e24aa-80ca-36a9-8f61-4cd13b60afe3 | -12.0041 | -63.5008 | 2024-10-19 01:06:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 8f7ec339-efd7-3983-88cb-8b2edad85b2f | -12.496 | -63.2832 | 2024-10-19 01:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| f26308b6-ed94-3ac4-a5bb-d1d989f9d0b0 | -12.5147 | -63.3014 | 2024-10-19 01:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 670eb5e9-9447-3fb3-bf99-1050e5a38ef7 | -12.5149 | -63.2822 | 2024-10-19 01:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 7ad6d80b-ed8f-3e27-9f6d-f90643010cce | -12.5336 | -63.3003 | 2024-10-19 01:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| f4a57c8e-d06d-3d76-8d7b-35ce1278b00e | -12.5338 | -63.2812 | 2024-10-19 01:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 72076e7f-c542-3ccf-a0c6-b570a1c4bcea | -1.1375 | -47.3179 | 2024-10-19 01:15:12 | GOES-16 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| cb6a0d59-e195-352e-93f0-8146aaf880ea | -2.7885 | -51.3618 | 2024-10-19 01:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 7e062fb7-c734-3fc1-a711-13543bdcef09 | -2.8069 | -51.3613 | 2024-10-19 01:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 74eee0d8-4010-325b-8616-907912959731 | -2.9489 | -52.9174 | 2024-10-19 01:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 0f6788e5-d831-394f-8696-3784b503104d | -2.9489 | -52.897 | 2024-10-19 01:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 1a591e0d-f378-3bc4-a92c-a83b75eeb8ad | -2.9673 | -52.9169 | 2024-10-19 01:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| d38c8d55-b80c-3ce4-a4d8-cfbee9f9be7c | -2.9859 | -52.8554 | 2024-10-19 01:15:23 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 729c576c-7afd-3b5e-8a9b-029edc7ccf21 | -3.4387 | -50.2158 | 2024-10-19 01:15:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 9bedc0f2-30af-3081-a07c-030ef74131bd | -3.4202 | -50.2164 | 2024-10-19 01:15:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 16377266-d62e-3bf9-9c93-a9277a2abd2b | -3.7116 | -51.1261 | 2024-10-19 01:15:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 3f4feb57-b3af-30f1-a5c5-212c956a66ef | -3.7117 | -51.1053 | 2024-10-19 01:15:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 6c575be2-bc8f-3acd-8712-37eb566db9a8 | -4.4167 | -50.535 | 2024-10-19 01:15:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 1dc9e12a-89c1-30ea-83ad-0f13c9816345 | -4.6028 | -44.6133 | 2024-10-19 01:15:32 | GOES-16 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 694841c9-4aba-34c2-aec4-eb0db0a47709 | -4.6873 | -45.8504 | 2024-10-19 01:15:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 379d1bc1-f415-3fe2-b0c2-1f7c19f49768 | -4.6875 | -45.828 | 2024-10-19 01:15:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 3ae1c83f-16a6-3380-aeec-627089cb5140 | -4.706 | -45.8493 | 2024-10-19 01:15:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 253.9 |
| 2884aad0-e55e-33b8-9ca7-52155ec2fea6 | -4.7061 | -45.8269 | 2024-10-19 01:15:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 184.8 |
| 84628548-e866-3809-815a-9f3a05387c2d | -4.7246 | -45.8482 | 2024-10-19 01:15:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 84.8 |
| f7a2e4e2-000c-3f07-bc3f-2e7b25d43812 | -4.7248 | -45.8259 | 2024-10-19 01:15:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| a2159bf2-388c-3e46-8999-e8d3add1a637 | -9.0344 | -67.4641 | 2024-10-19 01:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 199.7 |
| e24a3772-caa4-31d4-b501-6a15b73e978a | -9.0345 | -67.4455 | 2024-10-19 01:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 125.3 |
| 45edec7e-d4e7-3bc9-bdee-9ba1159debf1 | -9.053 | -67.4636 | 2024-10-19 01:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| f8c9cb03-fdc7-3086-874f-e21d1d6c482d | -9.053 | -67.4451 | 2024-10-19 01:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 59173acb-2aba-31f0-84f4-e0cb411b2ed3 | -12.004 | -63.5199 | 2024-10-19 01:16:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 4a5af207-af0e-3308-8c0c-ec2db535eea1 | -12.0041 | -63.5008 | 2024-10-19 01:16:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 72.3 |
| bd4959ef-fb8e-3a93-bca4-ee6968aea46a | -12.023 | -63.4998 | 2024-10-19 01:16:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 7e1448f8-f722-3cb2-92b7-da7b92a18b07 | -12.5147 | -63.3014 | 2024-10-19 01:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 77c846b6-0509-3efc-a08b-243e20be53b4 | -12.5149 | -63.2822 | 2024-10-19 01:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 8d63376f-36fc-36b9-b08d-814d4bdcb2b7 | -12.5336 | -63.3003 | 2024-10-19 01:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 68.8 |
| d7f16001-dc88-3dd1-bf65-08bc7e2ee49a | -12.5338 | -63.2812 | 2024-10-19 01:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 3f517ee8-7674-3c32-a37f-f9b8c9de0641 | -17.8214 | -41.3384 | 2024-10-19 01:16:44 | GOES-16 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 75.0 |
| 835a09ed-d76a-376e-8336-94f5e726e2fc | -17.8416 | -41.3331 | 2024-10-19 01:16:44 | GOES-16 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.9 |
| d44e82a8-7af1-3f57-b422-4544eb69ea19 | -16.809601 | -53.9417 | 2024-10-19 01:16:47 | METOP-B | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 64653c97-0ca2-39fe-b64a-afcf8d1dd0af | -16.811701 | -53.950401 | 2024-10-19 01:16:47 | METOP-B | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 03d1bbd5-9516-35fa-b8ff-2a516c2c866f | -16.7999 | -53.944099 | 2024-10-19 01:16:47 | METOP-B | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 14c56354-f4b3-3ddc-8c5b-332f18cce08a | -11.266 | -54.235199 | 2024-10-19 01:18:18 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 93097353-1a3d-35d7-b106-d6fb3f07cc47 | -12.7647 | -62.962799 | 2024-10-19 01:18:25 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b49ea2b2-1893-349a-8920-f185286143f2 | -12.7626 | -62.952801 | 2024-10-19 01:18:25 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 93f0805a-40c7-39fc-a595-15e2b2952c5f | -12.533 | -63.276699 | 2024-10-19 01:18:30 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6faab4bd-9f60-3ec0-b85d-7f40ebeb2cee | -10.6587 | -54.894199 | 2024-10-19 01:18:30 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6b83fe55-998a-33b2-883b-2cb4ccfb2ac6 | -10.6608 | -54.9034 | 2024-10-19 01:18:30 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1f3a0294-a608-33c8-8c38-0086da6e5895 | -12.5134 | -63.2808 | 2024-10-19 01:18:30 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
