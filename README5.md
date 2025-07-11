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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a08e4785-41c6-3b2a-8dd9-e67aedd6cfb1 | -5.5427 | -43.9096 | 2025-07-11 01:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 9b4e5a44-0c6e-3d6c-a8ce-473f76863c56 | -9.9337 | -47.8261 | 2025-07-11 01:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 7033ac64-7b2b-33e3-b592-70ff4c77816a | -7.2025 | -43.1171 | 2025-07-11 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.2 |
| aeca3ffc-76bc-3ed7-83a5-10b19516f25f | -10.6669 | -49.5111 | 2025-07-11 01:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 38c2198d-f63d-3c6e-9387-42f46992be49 | -22.2852 | -54.9409 | 2025-07-11 01:50:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 0c9ff787-bb83-36e7-8689-06a12055bf68 | -10.6672 | -49.4895 | 2025-07-11 01:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 206.6 |
| e7a05746-7260-3822-80d8-6a39deb3acad | -7.2025 | -43.1171 | 2025-07-11 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| 88d8d0d9-aa2a-3953-90a7-29fae9a2d1cf | -10.6862 | -49.4874 | 2025-07-11 01:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 164.5 |
| 0aede26b-990b-3f01-8b2d-dc42dfc92d97 | -9.9148 | -47.8282 | 2025-07-11 01:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 173.8 |
| d454cf27-f870-3dc6-bacd-1894d3228858 | -10.5776 | -49.1316 | 2025-07-11 01:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 54972ff9-b4da-3493-92f2-64297937cfdc | -9.8958 | -47.8303 | 2025-07-11 01:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 7b9bfcbe-2025-3708-9fb5-2ce630b0b3bd | -9.9145 | -47.8503 | 2025-07-11 01:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| dfafc6b5-444c-3440-bf23-a0516e837327 | -10.6669 | -49.5111 | 2025-07-11 01:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 5ec65c93-2a2b-3d2d-8f42-daecafe0789c | -10.6859 | -49.509 | 2025-07-11 02:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 81b74d42-3e92-3386-b412-e7d8920bce94 | -9.9148 | -47.8282 | 2025-07-11 02:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 101d0096-7d50-325a-9497-c0e06f07bbaf | -10.5776 | -49.1316 | 2025-07-11 02:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 135.3 |
| 49298834-02ea-3ec2-a6fa-e724f564cc01 | -10.6862 | -49.4874 | 2025-07-11 02:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 349c475c-ede8-3aee-99ba-fc764ab80c88 | -9.8958 | -47.8303 | 2025-07-11 02:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| c410010f-3852-361d-b35d-50df912b0d23 | -9.9145 | -47.8503 | 2025-07-11 02:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 6e3ddbda-def9-3afe-be11-b4a68ab30e91 | -10.6672 | -49.4895 | 2025-07-11 02:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 152.2 |
| 05efa2d1-c866-30b6-b099-fa74a847b4a8 | -9.9337 | -47.8261 | 2025-07-11 02:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 2fc53caf-a2ba-38e4-a417-086ae2203668 | -7.2025 | -43.1171 | 2025-07-11 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.0 |
| 5d8b2fe0-2539-3e7a-89d7-6016900c20b7 | -10.5965 | -49.1295 | 2025-07-11 02:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 6258976b-b32a-3a80-b048-389a98736386 | -10.6859 | -49.509 | 2025-07-11 02:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 152c8c24-d076-3ac0-9be2-a46001cb0b45 | -9.9145 | -47.8503 | 2025-07-11 02:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| c8e405d0-4043-3d6a-a0d3-d52018602417 | -10.5776 | -49.1316 | 2025-07-11 02:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 5d08920e-d26d-3e79-89de-da5429745e04 | -10.6862 | -49.4874 | 2025-07-11 02:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 169.8 |
| a58c9165-f6b7-3e35-b70c-5118af7b7193 | -7.2025 | -43.1171 | 2025-07-11 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| f0051701-4782-3ed3-a006-f74df0051a42 | -9.9148 | -47.8282 | 2025-07-11 02:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 192.6 |
| 5c5d282e-9592-3384-bf5b-e4bd49956763 | -10.6672 | -49.4895 | 2025-07-11 02:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 9fe91f13-1a67-3e0c-bfcc-8614a825a4d7 | -9.9148 | -47.8282 | 2025-07-11 02:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 0e8ea69b-6591-3aae-ba83-22b37217b100 | -7.2025 | -43.1171 | 2025-07-11 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.9 |
| 4296b449-8751-3043-bf73-46010a1eda96 | -5.5616 | -43.8851 | 2025-07-11 02:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 3728c0d5-6074-313b-abf8-1b998bc10dad | -5.5427 | -43.9096 | 2025-07-11 02:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 2e7de2ed-fc05-3127-981d-fba341f44997 | -22.2852 | -54.9409 | 2025-07-11 02:20:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 8d95fd0c-5a33-3b0c-a542-3ea03a523b29 | -9.8958 | -47.8303 | 2025-07-11 02:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 66f5baa9-9f68-3fcf-893b-6d6b0a8dc108 | -5.5614 | -43.9082 | 2025-07-11 02:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 21efd46a-d644-318e-897f-8d43ffb95bb6 | -10.5776 | -49.1316 | 2025-07-11 02:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 9951a212-fc9d-32e3-8c62-11cc197eda9a | -5.5429 | -43.8864 | 2025-07-11 02:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| fa64c434-3b29-370a-bf83-21072eab4a17 | -10.6862 | -49.4874 | 2025-07-11 02:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 156.2 |
| 2af9fd07-e75d-3d29-b22e-ea64b99d0405 | -10.6672 | -49.4895 | 2025-07-11 02:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 181.4 |
| e83fbb92-d04f-33f4-88cf-35b6bcd852c9 | -9.9616 | -64.957497 | 2025-07-11 02:26:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| eac8a26a-0aae-3b8f-bfd7-6fa2f54559b7 | -9.952 | -64.959999 | 2025-07-11 02:26:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1f4a86b3-b8e5-37d4-b523-962b44cf1946 | -9.9665 | -64.976501 | 2025-07-11 02:26:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9f4d0473-2bc4-3a92-8663-7b850cdb3bb8 | -10.6862 | -49.4874 | 2025-07-11 02:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 2bf4cdc0-cb54-3a63-865d-ee478dc2eff9 | -10.6672 | -49.4895 | 2025-07-11 02:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 172.5 |
| a37ae028-e62c-35b0-953f-3f4f4d3c941d | -10.6669 | -49.5111 | 2025-07-11 02:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| a71c87a6-0bfa-346d-b92c-76364735a502 | -10.5776 | -49.1316 | 2025-07-11 02:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 9622b9fe-36d9-3f42-a004-a1b262360999 | -9.9148 | -47.8282 | 2025-07-11 02:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 98173f36-76dd-3d98-908b-6e5b1c54739f | -9.8958 | -47.8303 | 2025-07-11 02:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 83666a92-4425-3eca-87be-28729eb0f39c | -22.2852 | -54.9409 | 2025-07-11 02:40:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 55.8 |
| fc841d62-e86d-3477-b1da-ee1c889104c1 | -9.8958 | -47.8303 | 2025-07-11 02:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 338be45b-4e63-3a36-a01f-fd809dbf6918 | -9.9148 | -47.8282 | 2025-07-11 02:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 594d9e7e-0687-3a9f-8f5c-caddd38f2c15 | -15.4732 | -50.0459 | 2025-07-11 02:40:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 57.9 |
| fddf7e39-aae9-3c52-a37e-4820ee57464d | -10.6862 | -49.4874 | 2025-07-11 02:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 79ad9a6b-e785-32d9-b938-52e46d47693b | -10.6669 | -49.5111 | 2025-07-11 02:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 9e5d331a-2339-3667-9477-546af14f0318 | -10.6672 | -49.4895 | 2025-07-11 02:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 179.2 |
| af76b21e-46ae-3905-81e0-be1b7aa9cb9b | -15.4928 | -50.0428 | 2025-07-11 02:40:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 71.5 |
| e9ef48d0-7a5f-3e7c-bb0d-8d84111038ac | -10.5776 | -49.1316 | 2025-07-11 02:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 8dda22f9-5435-3ba9-a000-e982b1404716 | -10.5776 | -49.1316 | 2025-07-11 02:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 7b464614-0053-3745-9aae-6581e86e4c90 | -10.6672 | -49.4895 | 2025-07-11 02:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 150.2 |
| 7f9687d2-8f2a-33fd-903c-75922cedbfb0 | -5.5429 | -43.8864 | 2025-07-11 02:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 75158d4a-f022-3267-a7a4-9b3509660c89 | -5.5427 | -43.9096 | 2025-07-11 02:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 809a640c-a0d8-3c0f-8377-d378e5846db1 | -10.6862 | -49.4874 | 2025-07-11 02:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 132.3 |
| c4046622-f52b-3bd9-bc87-89a82b7b8487 | -5.5616 | -43.8851 | 2025-07-11 02:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 44.4 |
| ad90c699-27bb-3217-9f32-cbd8ff3ac3a6 | -22.2852 | -54.9409 | 2025-07-11 02:50:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 2730e639-3bf9-363e-98c6-1ec9f7705f7c | -22.2847 | -54.9627 | 2025-07-11 02:50:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 8c20eaf5-6238-3b71-a6c0-09cf0f3fd680 | -9.9148 | -47.8282 | 2025-07-11 02:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| af6f78c5-8a29-3d71-b1f7-3800e041d497 | -7.2025 | -43.1171 | 2025-07-11 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.6 |
| e348cc83-e4f8-37f7-afc1-0b64ff8ce002 | -10.6672 | -49.4895 | 2025-07-11 03:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 141.8 |
| e43a1857-f366-3b46-834c-df88b7a5b6e3 | -10.5776 | -49.1316 | 2025-07-11 03:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 0f499203-9ec8-34e9-b1b4-547d1299e860 | -22.2852 | -54.9409 | 2025-07-11 03:00:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 143.3 |
| e7b7fc53-074c-3a93-8b55-9068ab409fa5 | -10.6862 | -49.4874 | 2025-07-11 03:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 142.2 |
| d3567e3b-0f2c-375b-a821-ed0b6aea7ab1 | -9.9148 | -47.8282 | 2025-07-11 03:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 0c36514c-afc7-3fb9-a5e1-7a682ff53020 | -22.2847 | -54.9627 | 2025-07-11 03:00:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 77.8 |
| eaa9f6e0-3b5a-3dcd-ada9-374740e5e68d | -9.9148 | -47.8282 | 2025-07-11 03:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 05204481-56ec-312e-92a6-959de3d12ddf | -10.6672 | -49.4895 | 2025-07-11 03:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 290fcf68-8398-3575-931b-66ab37cd55b7 | -10.5776 | -49.1316 | 2025-07-11 03:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| f4f3ea0f-4a85-32e6-a05b-3ea15093858b | -10.6862 | -49.4874 | 2025-07-11 03:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 119.0 |
| a634609b-6e8b-3748-8f89-643292b1214a | -7.19129 | -43.12582 | 2025-07-11 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| a4d0e568-4c1d-3551-b934-0ed17f067a58 | -7.1091 | -40.38316 | 2025-07-11 03:17:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 35c2a2e1-96ad-308a-bfe2-1a6f93fb42d5 | -7.19842 | -43.12703 | 2025-07-11 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 9328ca7f-e6ac-3789-86b8-c9adf25b05b2 | -7.10829 | -40.38766 | 2025-07-11 03:17:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 481c11eb-ae00-3ac4-97ae-7fa2bf678a84 | -7.19721 | -43.1152 | 2025-07-11 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 0822d3a5-5db8-366f-bc19-83ad87ed07fa | -7.20433 | -43.11644 | 2025-07-11 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| cb8571fb-da53-387f-81f2-746b1ba228ea | -7.19975 | -43.12004 | 2025-07-11 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| f6a0b687-f852-3e10-88c5-d11474cd7612 | -7.19264 | -43.11872 | 2025-07-11 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 8bbaf912-3323-38d3-8f4e-d736a3afed82 | -7.19395 | -43.11184 | 2025-07-11 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| c5ec07b1-e453-30ab-8e38-c8fa0d05265d | -7.31626 | -38.138 | 2025-07-11 03:17:00 | NOAA-21 | ITAPORANGA | PARAÍBA | Brasil | 2507002 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4a5172c3-75b6-3c14-841e-bfb7cabb37f1 | -6.85503 | -42.80082 | 2025-07-11 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 3e01e79c-d45e-39c4-9a8e-3b86394dd02b | -7.19586 | -43.12206 | 2025-07-11 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| f984747a-a1d8-38ba-a559-88ea3c5c1d92 | -6.85421 | -42.79438 | 2025-07-11 03:17:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| b15a61e2-9adb-3c4d-badb-717845c1ee4e | -7.11049 | -40.38285 | 2025-07-11 03:17:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 54358684-dc4c-3b71-a765-a9b5add44e9f | -7.20817 | -43.11441 | 2025-07-11 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 15da2deb-09ef-3aa7-80e5-23a3361fa847 | -6.85297 | -42.80083 | 2025-07-11 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 4559c073-9fdb-3f68-a7d5-960a6f14d289 | -7.19447 | -43.12914 | 2025-07-11 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 9211b78e-9303-354e-b11b-16e0a06bf07b | -7.10965 | -40.38734 | 2025-07-11 03:17:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 16b834eb-9680-3229-a7c8-0662c9e70dfd | -6.85624 | -42.79433 | 2025-07-11 03:17:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| ea906b17-2adc-3d25-b257-484c3bba5a9e | -7.18555 | -43.11731 | 2025-07-11 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 00eb1c78-5b14-3cc7-ba3b-d738006b6dbf | -7.11436 | -40.38871 | 2025-07-11 03:17:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |


[Clique aqui para ver as próximas entradas](README6.md)
