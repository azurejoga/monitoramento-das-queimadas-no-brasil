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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29e162af-ca30-329f-b430-0584fd0927b1 | -8.95033 | -60.59071 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6be0d338-e151-3ef5-b4cd-5fa2ca0f2dfb | -7.88131 | -61.1911 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c543938e-aad3-3406-a614-de1cadc68348 | -6.74366 | -59.17741 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f67661b-0540-3051-bd71-3e6c09e08f4c | -8.95071 | -60.54409 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8cd9d841-aebc-3343-bdd4-e75d145e3121 | -8.57711 | -54.72839 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| db806697-ea97-3617-84ab-6d591618eaab | -6.70415 | -58.95082 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c65188df-5f80-3508-9aff-ad29c1a28196 | -6.70354 | -58.9319 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3d23a91d-ae91-3a6c-a4cc-00e9e6147958 | -8.57273 | -54.75899 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a90d33be-090a-30a5-a99d-775682debdc2 | -8.50062 | -54.85762 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3c2cd196-ed64-30de-b06d-8bd6c09d2a04 | -8.95805 | -60.58474 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbd1a0dc-b670-361f-a7f6-2483e6809bcc | -8.55 | -54.72909 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 23e5f896-1f3b-379d-90b3-fc1d84e192c0 | -9.41083 | -60.58004 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d91aff25-0c06-3416-84f2-734a49aa85c7 | -9.42137 | -60.42271 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7304382e-fd0e-393e-b463-35249736f975 | -7.53437 | -55.58354 | 2026-08-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c050774c-f373-3f9a-81e9-6f9e245ac5dc | -6.79829 | -59.44336 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdd5fe82-455e-343a-baed-d1f32bdaf8d3 | -8.54832 | -54.7728 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5a06d258-f161-3a66-8590-97b09fcd7438 | -8.57616 | -54.73438 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3f830253-7611-30e3-a4eb-a0d16b91dc38 | -2.77097 | -48.57361 | 2026-08-19 05:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 82929472-f336-3fff-a4e5-3331dae6b665 | -6.7737 | -59.45458 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efa139f1-bb84-3c83-9e68-beb6e85e8a5f | -9.01369 | -60.51082 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e6d67d07-6158-3987-9d44-b7594ac3e179 | -6.78207 | -59.44488 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77601fa0-35c7-39e8-b454-a81d886cd8ba | -6.69393 | -58.94931 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39a4a797-f48b-3a3d-92dd-8068a5b66045 | -9.14287 | -58.30623 | 2026-08-19 05:23:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a84eceb-7765-38b1-a450-cd9ac00f78b6 | -8.54392 | -54.77218 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3b291988-4972-3816-bc32-024ee1c8dadb | -8.57261 | -54.76064 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ac795e34-9b37-32fd-aacd-57f15e193e58 | -8.58701 | -54.75384 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fb3c7fda-f33a-3fe8-94f2-ac2400307448 | -8.55271 | -54.77347 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d5785b3d-80d8-33f5-b2d1-2bf3f40d1623 | -8.58407 | -54.77541 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d4023d9-93f7-3d72-bad6-9ee2c27f7556 | -6.60606 | -59.10817 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec14ddcc-eafd-361d-be50-544ba032b02e | -9.11937 | -61.6027 | 2026-08-19 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d45f7679-67ef-30c3-bcc9-9b5e14a4a570 | -6.7616 | -59.15046 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b8181d0-13af-3c19-91e2-dab38e3262e7 | -8.96284 | -60.53162 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abab49de-27a4-3575-9be5-7497eef1e63a | -9.15098 | -59.6939 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fd808b7-6206-39b0-999d-29043971e561 | -2.08121 | -56.58652 | 2026-08-19 05:23:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 64acce1a-6fcd-389e-880f-bb6c281bfd99 | -6.99747 | -59.05106 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c289d40-a178-3683-9e31-464f3f0f4c71 | -6.74312 | -59.18103 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 729ac620-e4f4-37a7-8f99-d7c6d9501148 | -8.02747 | -54.01441 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f7933dc0-9e0d-304b-82c6-463dda4f0e53 | -9.40364 | -60.58252 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e16129ce-ab30-3e60-acb6-1a98fbc633e1 | -6.83528 | -56.45758 | 2026-08-19 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d33d5f02-7c03-3076-a910-737d6c479908 | -8.53253 | -54.75742 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dfef2964-8841-35b8-9eb4-31026d8e4e04 | -8.47254 | -57.6619 | 2026-08-19 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a63f423c-47b9-384a-b8fa-01e3db1fbfe6 | -10.11428 | -54.28747 | 2026-08-19 05:23:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5524b123-ce2f-3711-9c21-1a2d16be1694 | -6.75042 | -59.17851 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0467cdd-1ecf-3fae-9aa6-23d0d095b11b | -7.04666 | -59.84482 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdcd760f-3bac-3d1d-b2e0-ea17b1ec3b9b | -7.4678 | -63.64478 | 2026-08-19 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d431bddb-15ca-3349-9b27-30f6fa242906 | -8.58939 | -54.73633 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4e0bacb-bc0f-36c2-9b92-96963b60bf1a | -6.88564 | -59.04938 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32debc6a-4dd5-31d1-890e-2c0cb53aec9c | -8.56956 | -54.74974 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5efceaeb-e93f-31d1-971a-f3a865dc6f8a | -6.84036 | -58.9981 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a62db660-cb13-3b52-83c1-e9d564b6c985 | -11.16276 | -49.61605 | 2026-08-19 05:23:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ba469f8-8432-3727-8446-b54ece72d8f4 | -8.57877 | -54.7483 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c636d2f-019d-38c9-a66d-29716d5670e0 | -2.82741 | -52.29543 | 2026-08-19 05:23:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a1223561-265c-3ee7-b037-c20d29f9164c | -8.54953 | -54.76424 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| dd362274-8c74-30ff-95b9-4acc86dab8e8 | -7.61178 | -60.95651 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7354a6b7-98f1-3bbf-aad3-c00b59526bd0 | -8.58675 | -54.72265 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e34994d6-4e66-3b10-b11a-e99c951ef391 | -7.10916 | -59.76758 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d11d769-4ee3-302c-a0a6-4459912e9b28 | -9.12268 | -61.60323 | 2026-08-19 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 147f722e-e4ab-3d4a-9c04-b4c034f2b01f | -8.56515 | -54.74918 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0bcffc05-9aa0-3262-adc0-ead51787fbb1 | -10.12686 | -52.11695 | 2026-08-19 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 54399214-ea42-3fd6-97c1-c86f53fbdae6 | -8.54058 | -54.73206 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d45c5ab4-44a0-34ee-87ed-213728217659 | -9.19435 | -59.68191 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e457cfd6-c966-3878-95e1-252bf300174f | -6.90732 | -62.90452 | 2026-08-19 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f1ec6ab-6ba1-3ab4-9cf2-ecbdd1ca1055 | -8.55698 | -54.74337 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0890b37c-0f41-37a8-8d97-ec6e15839d05 | -8.56647 | -54.77282 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ad32839e-0a2e-306b-afdb-7f9db4376283 | -6.76781 | -59.15511 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f680876a-a656-3ce1-bb61-b8b3672b1252 | -9.42688 | -60.40908 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ddbf382c-1fbd-3107-ab4b-19134c3fd2ca | -6.80446 | -59.44796 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f4fe76a-82a0-3316-94e0-441eff861273 | -8.57702 | -54.76124 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| adefb2ff-ed21-39bf-890a-c99888cdd524 | -9.44762 | -60.29602 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74690461-ab7e-37df-98fd-7aaacc356a99 | -6.76498 | -59.15097 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1d14728-344c-3c4d-a9a9-7ff04f3903bb | -6.84376 | -58.99863 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4f28400e-2298-3fd8-8cbd-218b32e020e6 | -6.68634 | -59.06782 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6de4d431-597b-3a15-90ff-39492522c712 | -9.39412 | -60.55582 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7442e867-a2e0-33eb-be49-b481d0fa6f25 | -6.85342 | -59.02636 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14fc45a9-1d75-3d31-be3c-898679796440 | -6.74224 | -59.04284 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d4801cd3-509f-370e-94be-2105411d3286 | -9.39358 | -60.55933 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 583e963f-5864-3e8e-995f-b77f143153eb | -8.57174 | -54.7338 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f545876e-4292-39a0-b4da-4efcb80ade05 | -8.5746 | -54.74598 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2c4412f8-ad06-3ba0-baf5-f69ae77cf0ed | -8.53753 | -54.75378 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 276d8487-309d-352e-ad7d-7ec0360b9ce1 | -8.57556 | -54.73878 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e38b0a01-666b-3b70-855b-b28047a02b3b | -9.40356 | -60.56088 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 25b2b85f-4ee6-37f1-8c51-d1904dd8dc0c | -4.71208 | -47.15331 | 2026-08-19 05:23:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 0e443770-049d-34d1-8b77-29a4e43b0b8b | -7.55289 | -55.57132 | 2026-08-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 820fc51d-4a80-3259-8c1d-c71201fb99c1 | -9.42315 | -60.45557 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65d81191-802c-378f-88a3-f382cde59848 | -9.13998 | -60.61715 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de7227d1-6e83-3eda-b92b-71bba78a7c76 | -9.39134 | -60.55177 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| edc09ad3-6783-37f4-822e-128f988f72a8 | -6.88682 | -59.06456 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f10b31fc-73bd-3483-be63-24f61e58c613 | -8.54633 | -54.7551 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c066bc67-dc8b-38bc-aa25-06f2d096f34f | -8.52874 | -54.75239 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 230e0feb-e39e-3aef-a525-8380ff72cdc9 | -6.87996 | -59.04103 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2fcbc0c-102a-3a6f-a07c-7aad3a8cb013 | -8.54377 | -54.74135 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4a9c8da4-4cc6-3e85-a4ed-943338ef3bb1 | -9.0828 | -50.80549 | 2026-08-19 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e5ef541-6b3d-347a-954e-cf8c6e6f1460 | -7.61232 | -60.95304 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f5a241a-d134-3c7d-bc06-4fbf85d5b7e8 | -6.84207 | -59.00967 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e49e488c-eacb-386e-ad31-aa4d03315ed2 | -9.42416 | -60.42677 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 20b72074-e434-312c-91df-26d3af6fe95f | -8.95017 | -60.5476 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0afda217-df7d-3097-9304-9a5d52099cb7 | -8.27507 | -57.35372 | 2026-08-19 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77a56b89-e674-39f5-a488-79b47617aa23 | -3.68453 | -47.65862 | 2026-08-19 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 16a035f7-8824-36c6-b662-bb856ce05ea2 | -6.88336 | -59.04154 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 357f1186-a4d6-3a49-a0ef-ffe5b3700efc | -8.5494 | -54.73337 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README57.md)
