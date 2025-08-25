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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38700451-09e5-3878-9182-ea6c5b3f9d56 | -9.6414 | -59.6241 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 26023589-871f-3d24-8557-49fd22f34f9b | -9.2098 | -59.508202 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0ad605a3-628a-3256-a0d3-a697d389d24d | -9.1542 | -59.4505 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 75f8e166-47e4-3ac5-a9de-2d9fa85a5b6f | -9.0413 | -65.7276 | 2025-08-25 01:53:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 743b062e-432f-3403-b7e7-d8339b3eb11d | -9.0919 | -65.723297 | 2025-08-25 01:53:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 767115c4-cd8c-3d86-9b41-adf570d8fc99 | -9.2652 | -59.772999 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dc4e0c0e-e1c8-3a1d-8c33-0a91a20bc068 | -8.9891 | -65.4104 | 2025-08-25 01:53:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3eafc39c-c930-35f4-9d30-2149d9ce4a73 | -10.4142 | -64.430702 | 2025-08-25 01:53:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e243e2d9-4bf0-3b31-9905-d9a190427c7e | -13.1515 | -53.7122 | 2025-08-25 01:53:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 15cbe325-09e2-3337-8be6-569cc62f05fa | -9.6511 | -59.621601 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8d71e8a4-7549-3f28-8c57-51a232b3861c | -8.8783 | -62.4282 | 2025-08-25 01:53:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3a7c14cd-feb5-388d-ab1d-2faf7a16e2bb | -8.2234 | -61.423 | 2025-08-25 01:53:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 37f76b1a-b869-3ba9-a2e9-d51d59b7b6d6 | -9.6446 | -59.6371 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1ba6a2fd-4307-3470-90db-8e968cfa5bec | -9.5238 | -60.528801 | 2025-08-25 01:53:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7ae0cc04-73d4-339a-b6d6-b5f4f5888560 | -8.902 | -62.441299 | 2025-08-25 01:53:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7ed6942d-bb90-36a1-98bb-883b6527cd08 | -9.1931 | -59.4408 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2b95c551-b11d-3c4b-bf3a-99ecc9ca4cde | -8.9927 | -63.6511 | 2025-08-25 01:53:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 448dc09f-3cbb-38eb-8ac5-5ad0d2702f83 | -9.0511 | -65.725304 | 2025-08-25 01:53:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3b988cb6-3276-3b94-b535-6197b57015aa | -9.0707 | -65.720802 | 2025-08-25 01:53:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3184a03e-ad18-3c46-ad03-b880041ac532 | -8.989 | -63.635502 | 2025-08-25 01:53:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4917328b-9dca-333d-a165-dd40b7b64c26 | -9.1576 | -59.4641 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3157d96e-7e9a-36c8-8d14-cc0346f25b99 | -10.4257 | -64.4356 | 2025-08-25 01:53:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 77bc0a94-0b59-3606-a853-cb41f1dad2fa | -9.1965 | -59.4543 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a88efe81-33d7-3dbf-86ef-95b5135bb7fd | -9.2032 | -59.4813 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 60e79032-149b-3e4b-888b-b2bb859e2d31 | -7.66 | -63.518002 | 2025-08-25 01:53:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ad14e4a0-49e8-3b2a-8655-e89719f6ecdd | -7.5328 | -63.8106 | 2025-08-25 01:53:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 48193cd0-28c0-3c96-a0c2-e93859f94419 | -8.2256 | -61.389301 | 2025-08-25 01:53:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b0e836b7-e415-3e04-af33-8518178e1b10 | -9.8143 | -64.248596 | 2025-08-25 01:53:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b4f959da-80c1-3312-ac34-270511b0ae42 | -9.0153 | -65.389702 | 2025-08-25 01:53:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c1c7251b-2515-3e08-89c1-eb5fb82b83b2 | -9.1968 | -59.497299 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 52992841-f048-34d8-920b-092eb02bd411 | -9.1379 | -60.766899 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7be5349b-4ff4-3f07-8ce0-f40b31c5221b | -10.424 | -64.428398 | 2025-08-25 01:53:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a940f564-d17e-353a-823c-a8dd68fa0b3f | -9.8022 | -61.203201 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5a6b55d3-acf3-3d66-86d2-e7abe9c0f8d9 | -9.8551 | -62.842098 | 2025-08-25 01:53:00 | METOP-C | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 049e0442-f882-31be-9d8b-5d499c39cb10 | -8.8945 | -62.452599 | 2025-08-25 01:53:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bb21c1ee-51eb-31d7-a1a2-da08d6177fd0 | -9.0039 | -65.385002 | 2025-08-25 01:53:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e5172400-038e-3f72-985d-5a3d053b708d | -8.5057 | -63.863899 | 2025-08-25 01:53:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 32754ad0-eb8e-3b79-92bd-21c515f6b164 | -9.0023 | -65.377998 | 2025-08-25 01:53:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4be2c1c7-5e56-373f-b98f-c021ab6e5189 | -9.2074 | -60.924599 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e09fd358-b3e3-3bbe-903a-5d744d8f9b91 | -8.2208 | -61.412601 | 2025-08-25 01:53:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f6363602-1c9c-367c-bf41-6c23caba0460 | -9.2045 | -60.7859 | 2025-08-25 01:53:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3ad89bb3-0e0f-35be-9429-9691f6fda924 | -7.5309 | -63.802601 | 2025-08-25 01:53:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 833919cf-5949-36cd-b973-852afe5155db | -9.0495 | -65.718399 | 2025-08-25 01:53:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e9c5ae74-cbd4-3508-8d37-ae77f6266d4b | -9.0415 | -65.7349 | 2025-08-25 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 9b897298-4f93-39f7-bb5a-dcfbdb591219 | -8.9875 | -65.4006 | 2025-08-25 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 91.0 |
| a5f878c3-c3eb-3d71-ab74-416b9f72ced0 | -9.06 | -65.7344 | 2025-08-25 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 02ad9e0b-c806-3cfb-a4e9-58d53d8e2679 | -9.0061 | -65.3813 | 2025-08-25 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 6284c581-afcc-3f3a-829e-51aedee7848a | -11.4593 | -55.4836 | 2025-08-25 02:00:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 3a9cc46a-5cec-351f-aa45-95901aed9df4 | -11.4782 | -55.4819 | 2025-08-25 02:00:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 5e9fe589-6ca7-332e-a41b-ec0c352b9ced | -9.1722 | -59.4629 | 2025-08-25 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| ed2db145-db4a-311d-8b83-cf4f8dbf45bc | -22.5518 | -46.8053 | 2025-08-25 02:00:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 103.9 |
| 415b0ae2-3b74-3785-9ce4-fbe54d3d5965 | -8.8733 | -62.4685 | 2025-08-25 02:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 202.4 |
| 8c716088-bbe6-3a70-b668-0b99d9a221b3 | -13.1534 | -53.7397 | 2025-08-25 02:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 09d75506-6686-3287-9cde-c204199bd964 | -5.118 | -43.2198 | 2025-08-25 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 29d4838f-7416-3460-ac29-35b20b69dd6d | -11.4784 | -55.4617 | 2025-08-25 02:00:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| edf0068d-ead7-31d1-b57b-2774ef6b074e | -9.2092 | -59.4997 | 2025-08-25 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 5e87a1e1-bf4b-398f-85a7-dffcf73ada1d | -8.9874 | -65.4192 | 2025-08-25 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 126.0 |
| caf84975-31f5-3227-9d3a-874471a8009b | -11.4595 | -55.4633 | 2025-08-25 02:00:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 3a803a01-fa79-3589-afe0-1768610d1e25 | -8.8547 | -62.4692 | 2025-08-25 02:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 53.6 |
| b9afa696-ada2-3b6f-ac23-a69426315fda | -3.4254 | -49.0517 | 2025-08-25 02:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 1bdddb60-fa3a-372a-9563-2fcc707992b9 | -5.1181 | -43.1964 | 2025-08-25 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 4d79ed48-ce16-3677-8771-904af1ec5f81 | -5.0992 | -43.2211 | 2025-08-25 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| f6a52d76-8ba2-3f32-a8eb-b76aad69b8cf | -10.6128 | -44.3284 | 2025-08-25 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 2ecd333c-4216-312a-8e95-7ac5885c3a3d | -8.8734 | -62.4495 | 2025-08-25 02:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 201.2 |
| bd762c94-b5db-33db-81b5-ad3f2dee4363 | -9.006 | -65.4 | 2025-08-25 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| cbbde530-7446-3aa5-8ac2-9fec9d935d15 | -10.7093 | -50.5572 | 2025-08-25 02:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 04543177-231d-38d6-82d3-2743892852bb | -8.5136 | -63.8799 | 2025-08-25 02:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.0 |
| bc3a7795-cc25-302a-8608-e3863aeeefb9 | -9.0786 | -65.7338 | 2025-08-25 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.7 |
| d8574380-3fef-3fa7-ab17-926dbeeaf3d9 | -22.551 | -46.8295 | 2025-08-25 02:00:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.1 |
| 25127afa-de84-327d-a857-49b502edd541 | -7.6326 | -62.7243 | 2025-08-25 02:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| c52ccdad-6273-31c2-959c-d2e1785b9df8 | -5.0994 | -43.1977 | 2025-08-25 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 64b5539e-5690-3a5b-9e0b-47948a7c9fb1 | -9.1623 | -60.8332 | 2025-08-25 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 033e884c-f40b-3361-ac50-479ce5d1a445 | -8.969 | -65.4012 | 2025-08-25 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 9de3779d-61d9-384b-8609-a54b2148aecf | -8.8919 | -62.4487 | 2025-08-25 02:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 41c5834e-e8df-3227-952f-ed4fd4b14c8d | -9.0416 | -65.7163 | 2025-08-25 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 30.7 |
| c10ca3b3-8a3a-3169-87e6-112dda5d9387 | -8.9689 | -65.4198 | 2025-08-25 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| cae2f73e-9e48-3b98-88d8-7b332ca215ff | -8.8918 | -62.4677 | 2025-08-25 02:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 2f283feb-e7c4-3e1d-a56a-ceb4c4611dd0 | -8.8548 | -62.4503 | 2025-08-25 02:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 51.4 |
| b0f02445-5ce1-32e0-890f-fe7d09ca9c79 | -7.6326 | -62.7243 | 2025-08-25 02:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 9a14bead-1393-397c-a349-4bcc2d782f70 | -11.4595 | -55.4633 | 2025-08-25 02:10:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 195.5 |
| 20513ce4-dae1-3c61-98f1-14b578f87b24 | -8.8919 | -62.4487 | 2025-08-25 02:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 510aa253-96d9-33b2-aaa0-9fec7e4c1702 | -9.006 | -65.4 | 2025-08-25 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.2 |
| f8c7b659-64f4-35ed-a182-3c7fcc05ab59 | -3.4439 | -49.051 | 2025-08-25 02:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| bb7e6694-7018-3a23-9ec7-23da4dd35359 | -13.1534 | -53.7397 | 2025-08-25 02:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 1a7140a6-e086-3f0b-a5f7-a85261e17749 | -8.9874 | -65.4192 | 2025-08-25 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 137.4 |
| e62e2c81-7e19-3593-b7f7-bf3e31d4b722 | -8.9689 | -65.4198 | 2025-08-25 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| b583b423-f337-33c9-968f-00a1c60b0487 | -8.8733 | -62.4685 | 2025-08-25 02:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 137.2 |
| da14b304-eaec-36a0-a547-321ac4d252e9 | -8.5136 | -63.8799 | 2025-08-25 02:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 61cb43cc-aff3-3e43-9f46-51128e4216b5 | -8.8918 | -62.4677 | 2025-08-25 02:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 6bf8031d-07e9-3df8-b3d8-a500522a4796 | -13.4995 | -46.9063 | 2025-08-25 02:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 8ce51e79-dad6-3d73-8c08-237ed828df11 | -8.8734 | -62.4495 | 2025-08-25 02:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 161.3 |
| 8161e303-cfc6-3ff6-810a-d1c659e03438 | -11.4782 | -55.4819 | 2025-08-25 02:10:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 223.5 |
| e618042c-09d6-3c5a-b4f2-14bc19fc333a | -3.4254 | -49.0517 | 2025-08-25 02:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 48b4ff20-18b0-3361-822d-1cdc7bc53b8f | -11.4593 | -55.4836 | 2025-08-25 02:10:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 228.1 |
| d35abccd-af6a-3a85-9532-eeeff0e4cca3 | -13.5188 | -46.9032 | 2025-08-25 02:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 9a74e14c-2761-3d76-b311-ef50536d4142 | -9.1722 | -59.4629 | 2025-08-25 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 6ba9377e-cc97-3f98-8327-2524b75530ca | -8.9875 | -65.4006 | 2025-08-25 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| d6100369-1cff-33d4-8520-7b49105196cd | -8.5943 | -62.6315 | 2025-08-25 02:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| c935559d-ae68-3981-834b-187fa1c13ba4 | -11.4784 | -55.4617 | 2025-08-25 02:10:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 190.6 |
| 72be7f6c-f3d1-3793-9237-319383c949fb | -9.0061 | -65.3813 | 2025-08-25 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |


[Clique aqui para ver as próximas entradas](README16.md)
