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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7937d1b-da79-336b-9e74-943afa553205 | -9.44425 | -62.32359 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ee9a3e8-2c35-3b43-8070-db072c0572e6 | -8.63999 | -67.25552 | 2025-08-30 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f97183e4-cc61-39da-a9f8-0544840b1e0e | -9.44537 | -60.53537 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2bc2c576-c0f4-3f37-a1bb-ae0faf0e1b7d | -9.46005 | -60.55787 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ce419f4-40cb-34df-b750-af01440f5980 | -8.44434 | -70.14152 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 467b6185-87dd-3ce7-a334-db8ab1a5a690 | -9.80748 | -61.20207 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83587075-1a3c-3597-9366-c9c138d85f93 | -8.85226 | -70.62283 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5ba2dfa3-b484-3130-93f4-9451b1ec8187 | -8.93341 | -64.16107 | 2025-08-30 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7bf855e3-331e-33fd-83d8-51abd194c0bd | -9.45669 | -60.54454 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 98423ce0-6c0d-35a9-8619-4f5e69a5ad8a | -8.55083 | -63.02993 | 2025-08-30 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eab7a5a5-188c-34b2-8c66-2a0e6b079145 | -9.80795 | -61.20362 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f71e0e8-31a4-37f6-bfff-9a046f170a1b | -9.45558 | -62.33778 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 89d893f4-8479-3211-a746-f4b3ce6d2cf9 | -9.82154 | -63.8623 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 2d34acd8-a172-3542-ade7-c2dfc60922c6 | -7.90445 | -63.00375 | 2025-08-30 06:01:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| aeae3d73-56fd-31f3-a6ea-433e889ad4fd | -9.45848 | -60.56985 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c010dea4-bce2-3098-bef6-66ec94690a25 | -9.44273 | -60.55575 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 76f5dfc2-42ed-3c1a-9386-2e50dd94122d | -9.12321 | -65.76656 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 270632db-3b75-3e0e-8266-4c3c7e120092 | -6.53924 | -68.28313 | 2025-08-30 06:01:00 | NOAA-21 | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9616502-f709-3171-8e89-2415aed442e3 | -9.07213 | -65.45101 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c0e287b2-3c0a-390b-89c8-cb55a71b505a | -10.07496 | -58.35893 | 2025-08-30 06:01:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0f784f24-c67c-346f-8428-5883d64ebc1b | -9.44744 | -60.5646 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4e2a3c95-bb80-34b5-b610-7939d8e12466 | -10.74282 | -59.82222 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aa0bb4c9-1124-3ab6-aebc-27ad294f5b20 | -9.44656 | -62.36737 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5b2eb4a8-d39b-3fb1-a9b5-4d2849379b57 | -9.12571 | -65.80698 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c539ffa-a2aa-3742-9b8d-789a818ab5e7 | -8.34982 | -62.92797 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 326a5c1d-4660-38a8-af55-4508d33354d9 | -8.66078 | -62.44675 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1d6f17f-563a-3be9-8120-2cbf0a2878ca | -9.06802 | -65.45039 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ff5ae0cb-7723-331f-af97-d5504de4540b | -7.5318 | -70.12576 | 2025-08-30 06:01:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ceea7ac-5501-3bb6-8368-bfbe1575b53c | -7.90301 | -63.01417 | 2025-08-30 06:01:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 49a4d6e9-2c7b-3cc4-b116-0e0115a84696 | -9.06854 | -65.44666 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 65a4a086-4246-369e-9585-7390cd8932d4 | -10.84184 | -61.46539 | 2025-08-30 06:01:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b1c38e3b-81eb-3931-b657-58857602c631 | -9.89628 | -67.01381 | 2025-08-30 06:01:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 543229fb-6b73-3f65-95e4-d695e7d9d2e5 | -9.46623 | -62.33598 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 24.5 |
| f6d5289c-15c3-3f46-9a67-de6b31840e1a | -9.4489 | -60.56015 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5fcfc4ff-8646-3ec0-a204-1e5b7702f8c8 | -9.44734 | -62.32071 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d1d51f4d-ac78-3851-8a33-b258a615a88d | -9.4527 | -60.5692 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5452c9ff-bc94-3b47-ae79-a884e692bc52 | -8.70131 | -64.21477 | 2025-08-30 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b52153ff-8dce-3f00-a71f-e268fe1584cf | -9.08594 | -59.48748 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 17897738-ba74-3bcd-958c-44fdfa35e252 | -9.43831 | -62.35058 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a846579-7109-3c61-b3b8-5d1a5018c67d | -9.4397 | -62.35712 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8cbdb0a-e611-35fe-beb4-a6127cc334e3 | -7.89967 | -63.00307 | 2025-08-30 06:01:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 76edc5a6-1b68-3419-8a77-539fbf48993d | -9.76219 | -65.0877 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7bace20f-6c82-3d41-ab70-9dff36fdb783 | -8.17464 | -61.37777 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8979a75-2c37-3769-b4b3-7866eb53cb08 | -8.04001 | -70.0953 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d299553-d0b1-3919-a05a-d68442103311 | -7.53984 | -63.84388 | 2025-08-30 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 532d4787-2836-307d-a8dc-46046652e517 | -10.5894 | -69.59898 | 2025-08-30 06:01:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd375fc0-1aa9-33aa-9c1c-c01ec23d420c | -9.06548 | -65.43859 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 1f12b080-14c1-3416-9a7a-13e8d49e3f6e | -9.27263 | -65.92121 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 290390d7-5c88-3b33-aa21-19cc9bb0febc | -9.43846 | -62.36626 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a89541e-3aa4-3965-90a9-4c7a3c2cb8af | -9.07319 | -65.44353 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| a9f4d99b-0219-3f04-9f83-fe16caeeb787 | -9.27057 | -65.92155 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 260b91e9-985f-3838-a586-6f2fb8e535ff | -10.84172 | -61.46377 | 2025-08-30 06:01:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fa97762f-c41a-308a-8147-2526ac7556ae | -9.45323 | -62.35602 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 54704706-d878-3f0c-95e9-f7feac3b03bf | -9.43947 | -62.34152 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6b3ae0e4-94cc-342b-9266-d62c56eff00b | -8.89947 | -71.25356 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f2f22051-67e6-327e-a5e4-fc1a527049d1 | -9.27007 | -65.925 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 183f2be0-eb66-3149-a18c-20c36d4cf040 | -8.66295 | -70.04668 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcb20e45-57f4-384a-b78f-135a23cda91b | -9.44257 | -62.33597 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1546b9e6-69be-3c60-b3a7-a6315cfc48e1 | -9.13275 | -65.81525 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dcfe59ba-94bd-35cd-b31b-00a6b616d4a7 | -8.91146 | -62.10488 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f3b631c-1c78-3f9d-a9f1-66e4d216bbdf | -9.44299 | -62.33287 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8aa6484b-24a3-3309-ad62-53be3a564039 | -8.67263 | -62.43361 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8eea962-0a90-3fea-8219-bf6f10cb4d32 | -9.43928 | -62.3602 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0930b5f0-5e2c-3a7a-acf2-a5438da7fd20 | -10.35811 | -64.47011 | 2025-08-30 06:01:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0965c3e6-b43e-3c5c-b3b8-33c3ad7efa7f | -9.4619 | -62.32915 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 83782098-365c-34e4-8f76-78652ff6efd3 | -9.46231 | -62.32599 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| aafb0460-82ea-38e7-b3b2-bcfe8c059aa7 | -9.07266 | -65.44727 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 1761b1ea-44da-3b41-8909-cf5feac1c5a9 | -10.12542 | -68.23373 | 2025-08-30 06:01:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6e7cce30-1d8f-3e57-9493-4eebb8cafa74 | -10.0722 | -62.89539 | 2025-08-30 06:01:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c48eefe1-9ca7-3531-97bc-b188de95d06f | -8.66118 | -62.44384 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 737ae517-082e-3c7d-868f-670b672b34af | -10.24422 | -68.09149 | 2025-08-30 06:01:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 197d480d-e40d-370a-aaf8-1535fc3b0753 | -8.41578 | -71.27973 | 2025-08-30 06:01:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24974ab8-0fc4-304c-9985-74ba4311cd79 | -8.88933 | -60.73262 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b171eb11-4180-3d0b-a0d9-3a3fde4c45fc | -9.5415 | -62.38182 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f355a97-5676-3bc1-9f98-96b243199b4c | -9.45948 | -60.56944 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2bbee6a-3930-3ec7-910c-fd802454ca85 | -9.45691 | -60.53694 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 64d0298d-034c-3e7e-ad07-b1488221946c | -9.45531 | -60.54919 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 328b1218-5c27-3b4f-b43a-8a0de79c9338 | -8.66369 | -70.72121 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2126f644-cf05-3e31-90a8-0f4b4fc4b397 | -9.72726 | -64.90992 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8abd9bca-a356-351a-9698-9e4d677cb8d8 | -9.11363 | -65.77618 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 761faa59-94a7-3716-8a29-7bd6dfb79d58 | -8.1731 | -61.37295 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec47325f-6d16-3cdb-891e-4d2b849eae68 | -9.45244 | -62.3621 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 30a2165f-d176-3dca-9c08-5dc8b3ee0d21 | -8.04102 | -70.06692 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19d1256b-7fd2-3841-b6e9-aaeb31da2ea2 | -9.4387 | -62.34752 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9098633a-e635-3ac9-bf77-081623cbfd56 | -10.36359 | -59.20189 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af6c271d-7d71-3326-9eaa-77a208ee3668 | -9.82677 | -63.85846 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c03b7d74-33f4-3256-a168-da30f169f38e | -9.43909 | -62.34451 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eba64276-5c36-351b-a65c-8fa24c78bf5a | -9.44168 | -60.57131 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b0d51e85-0b18-306a-895c-8dc2bd99c342 | -10.45007 | -57.96865 | 2025-08-30 06:01:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7c025144-defb-3fb3-93cc-e8a1ead4e17d | -9.78425 | -64.24072 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f6ccdff-76f7-337c-adaf-7cd13b1bc16f | -9.54111 | -62.38486 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58bd43e6-49da-3b7e-a07d-62e153b5c919 | -9.46305 | -62.36052 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 021606c8-e921-35bd-b0fc-a2e7d145aede | -10.5799 | -63.48311 | 2025-08-30 06:01:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e3ff8ea-e933-33aa-b59e-56471fcc8faf | -9.25275 | -60.93117 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da844ccd-3a03-3887-92ff-b477cc82be31 | -9.13243 | -65.29443 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 140ff3a0-cff0-35fa-9a0f-e7e8cea1231d | -10.45695 | -57.9692 | 2025-08-30 06:01:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5b2fa2e4-8407-38a2-bd18-72018c17302f | -9.82615 | -63.86309 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e986b56f-5b1d-316a-bde8-d45a6a97ed02 | -9.45677 | -62.3285 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 7c8f5169-f34e-3267-bf8f-0db4c8887821 | -9.72978 | -64.90842 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 89bb688d-e853-341c-851e-e4f38d4dc791 | -8.84368 | -69.10882 | 2025-08-30 06:01:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README81.md)
