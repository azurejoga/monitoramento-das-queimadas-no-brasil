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
| e6e1cb7a-9152-3de6-bb9a-aaecef22bb0f | 2.19505 | -61.80946 | 2025-01-14 04:42:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71e1857f-26b1-3f66-b6ef-1f34fc6c9085 | 1.11407 | -59.46217 | 2025-01-14 04:42:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4a7bb330-f788-3c49-acf6-75e7f758f43f | 2.18834 | -61.81051 | 2025-01-14 04:42:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a107f4db-492a-3854-afa3-6177b7db45b7 | 1.32214 | -60.0416 | 2025-01-14 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 92215199-933b-3d7d-9f9e-35852e18db11 | 1.11977 | -59.4613 | 2025-01-14 04:42:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6d4c850-606b-3557-82eb-9cde4a277714 | 1.31485 | -60.43192 | 2025-01-14 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 8850f6ec-6d35-377d-85a2-b296a36d6c92 | 1.32804 | -60.04046 | 2025-01-14 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 734bbc25-ac29-3628-a1fd-7a34802265a4 | 2.95729 | -60.18148 | 2025-01-14 04:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d03a6802-2574-3dea-9f8f-ac3381b459e4 | 1.17547 | -60.50653 | 2025-01-14 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38b29201-c5ba-3fed-a93f-78701563f492 | 1.33093 | -60.03621 | 2025-01-14 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| df5c9198-36d9-3f35-a786-558a49d010d0 | 1.33159 | -60.0406 | 2025-01-14 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5c153c2a-57de-39fe-bda1-ebd39af067b1 | 2.95127 | -60.18163 | 2025-01-14 04:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2ebc3a86-558a-305c-a393-007c512fc9e7 | 3.59761 | -60.94014 | 2025-01-14 04:42:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e764c3b8-658b-33e1-91c7-d217d9aac348 | 2.95815 | -60.1856 | 2025-01-14 04:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e670138-6139-3d46-af43-ddeed6422b84 | 1.31912 | -60.03856 | 2025-01-14 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f8a4ffef-06a4-37f2-9191-9a7a5cd7315b | 1.18011 | -60.49631 | 2025-01-14 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e838f9b-25cd-30b3-917e-9bde387d1d53 | 2.94584 | -60.18721 | 2025-01-14 04:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 34208016-4538-395c-9086-505b2e292e0a | -1.35383 | -55.21099 | 2025-01-14 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd17f1db-46b3-3725-b8dc-88b6af5648e6 | 1.32023 | -60.42635 | 2025-01-14 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52d1a110-c04a-39d1-b508-ac67db482d8b | 2.43253 | -60.65257 | 2025-01-14 04:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 3ed42642-4eae-3e8f-81be-a9fbd8b253e1 | 1.3303 | -60.032 | 2025-01-14 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 51c82c4d-750a-35d6-a086-9da81104cf1c | 2.952 | -60.18645 | 2025-01-14 04:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8966b994-ea47-3b7a-9b84-ae7b736b394e | 1.18623 | -60.49181 | 2025-01-14 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b0d9a36-4360-326b-a73f-b1db5332f10e | 3.59832 | -60.94516 | 2025-01-14 04:42:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6e83354-97b6-3952-b720-3db5a46cc5a6 | 1.17473 | -60.50189 | 2025-01-14 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8b8cb8d-f77e-3e00-b9a9-3a7b46d6be54 | 2.08053 | -61.84327 | 2025-01-14 04:42:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee7ec6e2-0c23-3e28-a774-932f1088291a | 1.32438 | -60.03307 | 2025-01-14 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7cdb828a-7159-36a5-adc0-9ec845447db6 | 2.95742 | -60.18084 | 2025-01-14 04:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77304248-35b6-3ba0-af76-c167d5df9447 | 2.18251 | -61.81733 | 2025-01-14 04:42:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 343df924-1827-369f-b8c3-60806b773424 | 2.2018 | -61.80876 | 2025-01-14 04:42:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32a8ca1b-39ac-3260-837a-c630ff6f48bb | 1.32145 | -60.03723 | 2025-01-14 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 6d58f1b6-785a-3b9f-b8d6-4c807cbca3c3 | 1.33227 | -60.04512 | 2025-01-14 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 34366042-4698-3f00-9cd5-dd1924603e2e | 2.94511 | -60.18242 | 2025-01-14 04:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b0eb5e5e-43e8-3a95-bf10-d74e459b6645 | 1.17544 | -60.50311 | 2025-01-14 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| de567ddd-7447-381b-a786-3d06b40dff5d | 1.32076 | -60.03283 | 2025-01-14 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 26ff7134-affe-37c7-b2d2-8a6a09e80765 | 1.18546 | -60.49066 | 2025-01-14 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10ae1323-2c2c-3a25-bed0-143eb4885992 | 2.94567 | -60.18791 | 2025-01-14 04:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d34f1684-0727-391c-8a8e-3756dd6f437c | 3.59742 | -60.94019 | 2025-01-14 04:42:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23b45199-5ffd-3620-b6ec-44e2591305a4 | 1.18154 | -60.50211 | 2025-01-14 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a83f140b-ce2d-3a27-a82a-9a1de65fcbcc | 1.32503 | -60.03741 | 2025-01-14 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 63becd4b-2951-3b57-9086-3a13b84fffc3 | 1.32569 | -60.04182 | 2025-01-14 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a2609c7e-1a3f-3a7c-adcc-4dbb9269a1d6 | 1.18014 | -60.49285 | 2025-01-14 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89c207d8-ad42-3170-a7e3-39086e1f7ff3 | 1.32735 | -60.03608 | 2025-01-14 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 6d197b2a-78c7-3dec-838d-948dc900cb5b | 1.32668 | -60.0318 | 2025-01-14 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 39cabe49-ddf8-3d74-a1ea-f693d3860971 | 1.18084 | -60.49749 | 2025-01-14 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d067e361-527f-3949-8722-f69c62a8f97c | 2.94498 | -60.1831 | 2025-01-14 04:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 12.6 |
| bf780389-f8da-39cf-baf1-2d7d17be06fe | 2.07384 | -61.84449 | 2025-01-14 04:42:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38c2021d-27b1-3019-8c45-9d8a006762d9 | -20.24918 | -45.5495 | 2025-01-14 04:46:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2452aa53-d4bf-33ff-83e9-ee5a30acd941 | -20.2495 | -45.54644 | 2025-01-14 04:46:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c47a43d-5a80-3c6a-80c6-f3e959a94ab9 | -24.82839 | -53.62097 | 2025-01-14 04:48:00 | NOAA-20 | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b23f7f5e-6500-3b20-901b-8dbc2b45811e | -23.74847 | -55.41327 | 2025-01-14 04:48:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 15ffc5b0-97a9-3cbf-ba0a-bab5bb58c52b | -20.22717 | -54.20942 | 2025-01-14 04:48:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1cfebea-f68a-3e49-876c-a24b9e127a2e | -23.40016 | -47.00908 | 2025-01-14 04:48:00 | NOAA-20 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e4b43066-5dc9-3b8f-8102-867729d1c633 | -23.08279 | -55.49702 | 2025-01-14 04:48:00 | NOAA-20 | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 64c167e3-0da8-325b-8c82-f0b61aeb83e3 | -25.19039 | -49.32853 | 2025-01-14 04:48:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c42a877c-6319-30d4-b78e-2d130e0ccf22 | -23.7551 | -55.4145 | 2025-01-14 04:48:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 98e7455f-1b64-351f-a499-96ee0566642b | -21.74384 | -48.45335 | 2025-01-14 04:48:00 | NOAA-20 | NOVA EUROPA | SÃO PAULO | Brasil | 3532900 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38bc7a66-5a1b-3d3c-a231-a7d7e7edd873 | -23.98191 | -48.9174 | 2025-01-14 04:48:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3ba712f-608c-3397-8f23-cd5242756d8b | -19.97831 | -50.38188 | 2025-01-14 04:48:00 | NOAA-20 | OUROESTE | SÃO PAULO | Brasil | 3534757 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a89598f5-a824-3e8d-9b08-a91d2f2d0f1d | -23.40265 | -46.557 | 2025-01-14 04:48:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9129570c-3d63-3733-bb5e-bef21b1dcb22 | -21.74332 | -48.45767 | 2025-01-14 04:48:00 | NOAA-20 | NOVA EUROPA | SÃO PAULO | Brasil | 3532900 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d5f4196b-4c97-3b4d-82ee-e1b5d8e1ee64 | -20.79858 | -56.48436 | 2025-01-14 04:48:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e6f8d496-255c-395b-980c-197a35f4aaec | -23.33823 | -46.7719 | 2025-01-14 04:48:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 689fddfa-5b69-3e01-bfdd-3e9c6286a2a2 | -25.19934 | -49.3254 | 2025-01-14 04:48:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 83f1892b-22d1-3a5e-a475-b0f84887db99 | -20.87522 | -57.24678 | 2025-01-14 04:48:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1a8d4b1-9fc6-3bdc-a32d-65763b115f28 | -21.44657 | -48.60608 | 2025-01-14 04:48:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 3ba9d96c-1ebb-3361-aea5-27dc88f9978a | 1.3221 | -60.0463 | 2025-01-14 04:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 681016a3-ec52-3018-b89b-2a1927b09478 | 1.3221 | -60.0272 | 2025-01-14 04:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 138bfa93-b113-3f9b-b60b-310d1e3b0252 | 2.9463 | -60.179 | 2025-01-14 04:50:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 53.2 |
| bbb4a09d-97a4-33fc-9b53-c1854251e292 | -28.77571 | -55.60442 | 2025-01-14 04:50:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 7.7 |
| e75f9b27-89c8-30e0-9f41-ab0409504680 | -28.78059 | -55.61765 | 2025-01-14 04:50:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 13.9 |
| c4d3afa6-ed9e-3be1-b327-aca3e7d1b6e8 | -27.79592 | -50.38292 | 2025-01-14 04:50:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 589aba89-bd9b-3529-9d66-6e7e7ae469ef | -28.77724 | -55.61701 | 2025-01-14 04:50:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 13.9 |
| 474139f3-8412-39e3-aaf7-a7e5fff47e7f | -28.77878 | -55.62959 | 2025-01-14 04:50:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 10.3 |
| b0513eb4-9cf4-3855-a3b2-d655c75dfaed | -28.77511 | -55.6084 | 2025-01-14 04:50:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 7.7 |
| ac38854b-ab6f-3be0-af67-08ba0be27d82 | -29.73577 | -53.86971 | 2025-01-14 04:50:00 | NOAA-20 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 3.0 |
| 0b2af4e2-e07f-3a32-a2e0-c1eb03a0e263 | -31.38423 | -53.892 | 2025-01-14 04:50:00 | NOAA-20 | HULHA NEGRA | RIO GRANDE DO SUL | Brasil | 4309654 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| b5fc02c0-62a9-347f-aed0-2fa0e039c415 | -29.73516 | -53.87423 | 2025-01-14 04:50:00 | NOAA-20 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 3.0 |
| 2386aaae-c5a7-3bf9-8475-b674fa617245 | -28.77303 | -55.64486 | 2025-01-14 04:50:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| ab760cbe-435a-3805-b1d6-15aaa848a8f3 | -28.77845 | -55.60905 | 2025-01-14 04:50:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 10.5 |
| 3e655610-ef2c-35a5-b17a-a6516620bb4b | -28.77237 | -55.60378 | 2025-01-14 04:50:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 7.7 |
| 521771fc-a1f2-3caf-9861-8ee24ba66e80 | -28.77023 | -55.59518 | 2025-01-14 04:50:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| 525b36b7-f765-36f8-b8f1-78720960eb31 | -30.50495 | -54.03868 | 2025-01-14 04:50:00 | NOAA-20 | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 52f9f29d-7f1f-3323-ba83-3f73e1fab7f6 | -30.11766 | -52.07867 | 2025-01-14 04:50:00 | NOAA-20 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 333ff3c4-c0bb-31c6-a88d-bdc3f0658cce | -28.77784 | -55.61303 | 2025-01-14 04:50:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 13.9 |
| 9ae718fc-e6bb-3245-9caa-5550af8f2da2 | -28.77938 | -55.62561 | 2025-01-14 04:50:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 13.6 |
| de67100d-9ea2-3782-9257-7edab8aa6a89 | -28.76963 | -55.59916 | 2025-01-14 04:50:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| b73c0616-3661-35e2-b614-c975618b6cce | -30.36155 | -52.30832 | 2025-01-14 04:50:00 | NOAA-20 | DOM FELICIANO | RIO GRANDE DO SUL | Brasil | 4306502 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| c385607b-1d64-3166-a4bb-2e311c3b3ad2 | -27.4487 | -48.44537 | 2025-01-14 04:50:00 | NOAA-20 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9a381bb6-2a0a-3ca6-a7b2-495dbe901d6b | -28.77998 | -55.62163 | 2025-01-14 04:50:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 13.6 |
| 4be62d51-6cc1-3d20-806a-13bb4da636e9 | -25.97057 | -52.60164 | 2025-01-14 04:50:00 | NOAA-20 | CORONEL VIVIDA | PARANÁ | Brasil | 4106506 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ef3c200a-8786-3a1e-8d9d-6593d8e4e772 | -28.77818 | -55.63357 | 2025-01-14 04:50:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 10.3 |
| 83201e63-bdc7-3ca9-a417-49a9649856b3 | -28.76689 | -55.59453 | 2025-01-14 04:50:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| 8f1e7c90-27b9-3201-a995-d457ee9a7f1e | -6.77961 | -35.17269 | 2025-01-14 04:59:00 | AQUA_M-M | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 1a59b780-6dc6-3399-b1f7-6ed20aef07e7 | -28.7817 | -55.6294 | 2025-01-14 05:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 71.9 |
| 64b6a64d-45d1-33fa-989a-ca11c23463a6 | -28.7824 | -55.6063 | 2025-01-14 05:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 88.3 |
| f0fdfbe3-e6f0-3992-9faf-724fd67e6324 | 2.9463 | -60.179 | 2025-01-14 05:00:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 5a2c52e8-6ec2-3e0c-8a92-276adcf9a2fc | 1.3221 | -60.0463 | 2025-01-14 05:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 87.0 |
| dba437c9-5083-3244-90c4-eb0478efd3c9 | 1.3221 | -60.0272 | 2025-01-14 05:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 666128c4-81b0-3ca2-830d-16e14c54e70e | -28.77803 | -55.6259 | 2025-01-14 05:05:00 | AQUA_M-M | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 39.8 |


[Clique aqui para ver as próximas entradas](README5.md)
