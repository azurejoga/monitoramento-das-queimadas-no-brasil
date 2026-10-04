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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f73b9738-4391-305c-b628-c039e03a5f7e | 2.8909 | -60.465 | 2026-10-04 16:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 2bf9bde3-2e76-3ff6-8268-79c1fe9838df | -8.334 | -62.8498 | 2026-10-04 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 246c5976-a395-3171-bd45-3bc6f5c3439a | -8.3525 | -62.8491 | 2026-10-04 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 93de6ee3-67ce-3a45-af79-b0d800d2a60b | -9.0232 | -65.6982 | 2026-10-04 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 66dc171f-8d11-3ccd-9717-5c7627b80b29 | 1.9239 | -50.9035 | 2026-10-04 16:10:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 60.3 |
| eabfff0c-963c-3bce-814f-9aa49fb0f59a | -11.8814 | -64.9323 | 2026-10-04 16:10:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.5 |
| a0f36901-4d36-3065-af67-e7a29fd85ea9 | -9.4115 | -65.9099 | 2026-10-04 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 76b4d6d1-bc34-3d9a-b1e8-0a9abfe36e76 | -1.4672 | -48.9097 | 2026-10-04 16:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 1fd2b9bb-b34a-341c-8a2f-494f113ce1e1 | -5.97 | -41.35 | 2026-10-04 16:15:00 | MSG-03 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ab60b190-5607-3ee3-a3b8-30008610af60 | -5.97 | -41.31 | 2026-10-04 16:15:00 | MSG-03 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 57fdd46c-9b53-39f2-bd59-d6a8918611a1 | -6.0 | -41.31 | 2026-10-04 16:15:00 | MSG-03 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cabe4b30-d481-378b-9b90-5d9afa4e2615 | -2.85 | -53.91 | 2026-10-04 16:15:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b571d1bf-d382-33ed-a1aa-29a1b730efff | -6.25 | -52.83 | 2026-10-04 16:15:00 | MSG-03 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e4bb465-4cd3-3f66-8820-2d2be3c97dc9 | 2.8909 | -60.465 | 2026-10-04 16:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 45751ab2-2263-39ee-b650-cb979dbb495a | 1.9793 | -50.84 | 2026-10-04 16:20:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 82.5 |
| b221a292-1ceb-3c47-a8ea-e28190667ba0 | -11.8814 | -64.9323 | 2026-10-04 16:20:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 82e0867a-7252-3bb7-b79d-7c163a7f9493 | -1.4672 | -48.9097 | 2026-10-04 16:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| be013e31-d39e-3408-90b6-5d6db60b8c2e | -1.4672 | -48.9097 | 2026-10-04 16:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| b4951eee-2f3a-3df5-a366-b98e22ffcfc6 | 2.8909 | -60.465 | 2026-10-04 16:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 32127bc1-dd81-3497-b91e-e3319021a32e | 1.9793 | -50.84 | 2026-10-04 16:30:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 36b7796a-c13e-3416-a6c0-a1e34c125f91 | -1.8693 | -50.6127 | 2026-10-04 16:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 4aee2595-172b-37be-a85f-74d72c0a5f27 | -1.8693 | -50.6127 | 2026-10-04 16:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 259fe01b-924b-36ea-9bd1-d9bf9af70c35 | -9.8618 | -65.0146 | 2026-10-04 16:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 9ddd7e2f-45ae-35a3-8dbd-e9d880969512 | -1.8693 | -50.6336 | 2026-10-04 17:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| e418a5dd-6c60-36ee-9eca-5e132308e09a | -1.8693 | -50.6127 | 2026-10-04 17:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 3ecc1a46-6ed7-3878-8cdf-ae375d6fbc25 | -9.1168 | -65.4711 | 2026-10-04 17:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 49a57996-1739-3567-ba65-79de26464723 | -9.8618 | -65.0146 | 2026-10-04 17:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 40.5 |
| b988c7a8-e236-3133-86d1-3da97cb58625 | -9.1168 | -65.4711 | 2026-10-04 17:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 993c3daf-aeff-3356-a4d7-113121586939 | -0.4687 | -52.0354 | 2026-10-04 17:10:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 80.3 |
| ab43a816-d1e3-3fab-81cb-0c5c504c3f4a | -9.0046 | -65.6988 | 2026-10-04 17:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| fb9f61bf-e159-3bb7-b598-9b80c467ab0d | -1.8693 | -50.6127 | 2026-10-04 17:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| a22c3408-2e1f-3241-9973-115b7a289b57 | -9.4819 | -66.7836 | 2026-10-04 17:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| f21e8078-775f-3e3c-9391-7fe9501128a8 | -9.0232 | -65.6982 | 2026-10-04 17:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 1eed4466-8f38-3927-8afa-72db7db1ad52 | -11.8814 | -64.9323 | 2026-10-04 17:10:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 435c7590-a91e-3b1a-b967-82aff5c88d1a | -9.1147 | -65.9379 | 2026-10-04 17:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 364dea08-ea01-3143-b746-3b0558f4554a | -11.65 | -43.54 | 2026-10-04 17:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b39b5293-e52c-31cf-b0aa-9f7702b0362a | -2.49 | -48.02 | 2026-10-04 17:15:00 | MSG-03 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb0b42d0-1222-3100-ada4-d77b017f9375 | -5.97 | -41.35 | 2026-10-04 17:15:00 | MSG-03 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c8863906-d4f8-3f80-b14f-7d366940c349 | -6.9 | -43.69 | 2026-10-04 17:15:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 49ad6130-9c74-3879-a2f3-0c27f3a5d8f1 | -3.9 | -55.81 | 2026-10-04 17:15:00 | MSG-03 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 805f056b-493d-3e49-9afc-4cec3aa4a507 | -11.66 | -43.58 | 2026-10-04 17:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ae25e1b0-a51f-31ab-8cc3-0ed1fae23030 | -3.87 | -55.8 | 2026-10-04 17:15:00 | MSG-03 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8da184c6-e004-35b1-acb7-393ee72eac46 | -6.93 | -43.7 | 2026-10-04 17:15:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bd7f1f19-2c16-38ae-94d8-813a9bd7be13 | -5.94 | -41.35 | 2026-10-04 17:15:00 | MSG-03 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5887df48-5cf6-303b-aa16-87b7fbf617fe | -6.93 | -43.65 | 2026-10-04 17:15:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ee69556b-12c9-35ea-8dcb-ef4a56c7a0cb | -6.9 | -43.65 | 2026-10-04 17:15:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cd8fc0e4-249a-3c16-b7fc-71d2fe41d398 | -5.94 | -41.3 | 2026-10-04 17:15:00 | MSG-03 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9241e293-a52f-37d9-a067-38c8b3c16640 | -8.334 | -62.8498 | 2026-10-04 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 7752c104-53d1-35b3-b3a1-c5b3c68780cd | -9.0982 | -65.4904 | 2026-10-04 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 0e257239-6436-372c-a08a-4788ab51c40e | -9.6573 | -65.0033 | 2026-10-04 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 40.2 |
| ecb1a0ec-f99d-32c0-88c0-7ddb53235912 | -9.1168 | -65.4711 | 2026-10-04 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 7c3aa116-91eb-3bd3-bf76-22abb5ff6a1d | -8.3339 | -62.8687 | 2026-10-04 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 103.3 |
| a4e4888b-03b4-320e-91e0-56bf536b2977 | -9.1332 | -65.9373 | 2026-10-04 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| e80bfa5d-ab5f-3b54-a07f-c69b5f77efc4 | -9.1147 | -65.9379 | 2026-10-04 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 64dd314c-c88f-35db-8724-3a0012c28da3 | -11.8814 | -64.9323 | 2026-10-04 17:20:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.1 |
| b99cd2ae-e116-33c4-b2d1-05f76ffe1f7c | -9.256 | -67.6438 | 2026-10-04 17:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 1a9c959d-15d2-33b5-9e07-94fe5d9e8cef | -9.0232 | -65.6982 | 2026-10-04 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| b0ab1b11-6908-3388-93b5-bf4e3334cc3b | -9.0982 | -65.4904 | 2026-10-04 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 87b8cdf0-4ddc-3650-992e-2bb9d1c67c7b | -11.8814 | -64.9323 | 2026-10-04 17:30:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 53da2063-ec0d-3801-9c09-dc221ad05d07 | -9.0981 | -65.5091 | 2026-10-04 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 87e6a4bc-ff76-37e8-b78c-17aae3e42a0b | -8.3339 | -62.8687 | 2026-10-04 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 101.1 |
| a035b92b-9de9-3861-a013-d5900b12743f | -8.334 | -62.8498 | 2026-10-04 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 30ae0762-80f8-3edc-af95-88b7a7d2bcb7 | -9.1168 | -65.4711 | 2026-10-04 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| f8104d2e-9737-3448-a3b4-db87c2172e9a | -9.0045 | -65.7174 | 2026-10-04 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 11775f73-a971-3715-b391-a7f843e10196 | -1.8693 | -50.6127 | 2026-10-04 17:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 01981f61-8872-3297-b7a8-e182ded10ef9 | -8.3341 | -62.8309 | 2026-10-04 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 142.7 |
| 6151a78c-3982-36fa-9ece-5c61f8888e33 | -9.0429 | -65.4361 | 2026-10-04 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 4686576b-f95d-3e50-aac6-38fc69e43d9a | -8.7129 | -61.4095 | 2026-10-04 17:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 01bf196c-8274-389d-9521-0e5919ce0372 | -9.043 | -65.4175 | 2026-10-04 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 570319b7-68ec-3e7e-8806-5e77919c819a | -9.0981 | -65.5091 | 2026-10-04 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| f096be94-ef27-3e28-995a-21575fa3e90d | -8.3341 | -62.8309 | 2026-10-04 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 143.4 |
| 33630b44-a9fe-3f11-8b98-5c3831f34b82 | -9.9175 | -65.0313 | 2026-10-04 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 3553e51c-3ffb-36c1-a121-41eacb895941 | -9.9174 | -65.0501 | 2026-10-04 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 8b33bac7-461f-3cb8-8e69-7fa40ad5a8f8 | -11.8814 | -64.9323 | 2026-10-04 17:40:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.8 |
| e30f8a75-ae21-3910-8262-0de5a00534a8 | -12.1202 | -57.1767 | 2026-10-04 17:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 5e5b4267-b768-322b-a4a1-a502f2896d71 | -9.1777 | -68.9027 | 2026-10-04 17:40:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 0d3f7bd2-8f8c-39ae-b4ec-503afda42df3 | -9.1261 | -67.7211 | 2026-10-04 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 97839f10-23be-3833-a182-1f55962dfe09 | -9.1168 | -65.4711 | 2026-10-04 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 86c92f5b-e3b6-39eb-9a6c-64385d4dd6fd | -9.7318 | -64.9818 | 2026-10-04 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 2274e148-7fc1-31b6-a7ed-4f7e6f5d5330 | -8.334 | -62.8498 | 2026-10-04 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 89b06a2c-fcf9-341f-b627-2acc8799608e | -8.3526 | -62.8302 | 2026-10-04 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 224.9 |
| 1bbaab0f-9bcd-3b1b-9aaf-e84157522cec | -9.1147 | -65.9379 | 2026-10-04 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 6bf4302e-f003-3ad3-8dac-aa8f0edcea0b | -8.3525 | -62.8491 | 2026-10-04 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 131.6 |
| 97dcfe1f-9ffc-3061-9cd4-78a91bdf63d8 | -9.0982 | -65.4904 | 2026-10-04 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 69a364aa-be71-33ea-9022-83dd6d2fc6f8 | -9.0232 | -65.6982 | 2026-10-04 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 7de64f74-3af8-3b0b-9c90-7187bddb6c5d | -8.3339 | -62.8687 | 2026-10-04 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 899d48df-7cf7-3d32-baf9-53e224d8eb34 | -9.4819 | -66.7836 | 2026-10-04 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 7ae6a90a-1906-3432-9d32-20994458dfc2 | -9.4115 | -65.9099 | 2026-10-04 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |


