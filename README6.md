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
| b7a52762-cfe9-38f9-ae04-36b47add0252 | -5.7756 | -45.0826 | 2026-09-05 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| cf454782-c0d8-3f58-a38f-abc09e6681af | -5.7756 | -45.0826 | 2026-09-05 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| bd577fed-cdb1-31dd-84a0-9c4124a6c82d | -6.5963 | -59.9087 | 2026-09-05 00:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| b7277296-1980-395a-95ef-01e7bca0bad4 | -10.4717 | -46.0216 | 2026-09-05 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| df42d9dc-2a98-3e8a-89a3-83bffd0fd1d5 | -5.346 | -56.0454 | 2026-09-05 00:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| f67b54d6-47e9-3e3f-b8d2-cebf274c119e | -3.7645 | -61.7737 | 2026-09-05 00:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| d5d4089b-7749-3990-a64d-c42feb68354e | -17.1078 | -56.8304 | 2026-09-05 00:50:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.0 |
| 3a271b21-2986-3942-833c-641bc6813e13 | -13.4453 | -43.8366 | 2026-09-05 00:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 056b23cc-7210-329c-b02e-52c42c505c3d | -18.1315 | -51.7534 | 2026-09-05 00:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 57.2 |
| f92f9f30-c2b5-3207-9401-776d2f80e75f | -13.4458 | -43.8128 | 2026-09-05 00:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 0561c096-f57a-3266-bb0e-477d2ab65b24 | -6.5962 | -59.9279 | 2026-09-05 00:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 96ccbfa5-e272-3fd1-af3b-f0ae6b5c395a | -5.3276 | -56.0461 | 2026-09-05 00:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 3381031c-d600-32f4-8973-ecba7155451c | -13.4264 | -43.8163 | 2026-09-05 00:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 133.6 |
| b27bd78e-b371-36bc-9c1d-708bcc95d19a | -5.3462 | -56.0256 | 2026-09-05 00:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 8df5239c-80d6-3dfc-992c-c45127d5de9a | -3.7827 | -61.7733 | 2026-09-05 00:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 9992bc86-31d4-3453-ab1f-f380dbe9e83a | -15.0773 | -52.5183 | 2026-09-05 00:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 205d7bd7-b868-3e34-b9ff-2b0af502dfff | -6.0245 | -60.159 | 2026-09-05 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| d27a003d-e3cd-3cf3-8968-a3c1e3bcc563 | -13.4259 | -43.8401 | 2026-09-05 00:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| f00a408b-f4d7-3ae6-b9db-3ecdb791b04e | -14.905 | -44.6782 | 2026-09-05 00:50:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 3beb249d-4a07-3bc1-b954-5dd8dcbf8b16 | -5.3277 | -56.0263 | 2026-09-05 00:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| bfe78570-2ce5-3d13-95d1-45c985a597d8 | -18.1111 | -51.7786 | 2026-09-05 00:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 036fd429-9079-3b7c-88b1-2f429c1256e4 | -3.7645 | -61.7548 | 2026-09-05 00:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 81483fdf-8216-3e4b-8e3c-6c2d844adeb1 | -5.9197 | -47.8927 | 2026-09-05 00:50:00 | GOES-19 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 120.5 |
| e51f5cb9-a8b2-3d19-b8b1-ba9c037141a4 | -6.6513 | -59.9642 | 2026-09-05 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.5 |
| be382d7a-c3a4-349d-8918-110f3154ddb0 | -18.131 | -51.7752 | 2026-09-05 00:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 73.2 |
| fedb7a93-2434-31e7-8b9f-6120159f0614 | -6.6698 | -59.9443 | 2026-09-05 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 122.4 |
| cba69daa-87eb-3fe5-8581-64739fb494e5 | -6.0244 | -60.1781 | 2026-09-05 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 3b3d441a-576e-3295-aefb-3c1cf045c219 | -6.6697 | -59.9635 | 2026-09-05 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 2f59a824-4021-3365-8335-cc33d8f5d5d1 | -6.6514 | -59.945 | 2026-09-05 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 158.7 |
| 6519c368-fb18-3d2c-978f-65eb606995f8 | -5.7758 | -45.0599 | 2026-09-05 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 97f698c6-510b-30ee-873a-0e723b18de2b | -3.7828 | -61.7545 | 2026-09-05 00:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 77c39e11-219c-3935-ac61-36637bbbfa96 | -6.6697 | -59.9635 | 2026-09-05 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 99.1 |
| a7103b35-825b-34b4-97c7-7a4c0e0864a7 | -3.7645 | -61.7737 | 2026-09-05 01:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 7a8101ec-28bd-344e-b6fb-7fbab7ca83f8 | -14.905 | -44.6782 | 2026-09-05 01:00:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 71.3 |
| cb6cc6a8-4550-36d6-8c61-af62853339bd | -6.0245 | -60.159 | 2026-09-05 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 2c4ef39f-9f3e-3041-a02f-e711bc77cb58 | -5.7758 | -45.0599 | 2026-09-05 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 6591efaa-be3e-3bf9-b05f-902ab5fb90f3 | -3.7645 | -61.7548 | 2026-09-05 01:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| b5aa2c7b-4ccd-3e6f-91c1-eb3570b7091a | -6.6698 | -59.9443 | 2026-09-05 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 167.8 |
| aad38384-6348-3ce3-8ff0-9f1774c57b83 | -6.6514 | -59.945 | 2026-09-05 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 212.1 |
| f0735648-999d-35ac-a0f9-a56ab8ad7dc5 | -5.7756 | -45.0826 | 2026-09-05 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 7a8218da-1f0f-3277-ad90-45302a475f9b | -10.4527 | -46.024 | 2026-09-05 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 2a695600-e3dc-3ec3-8598-74d2de28d76d | -3.7828 | -61.7545 | 2026-09-05 01:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| bc797844-4571-3e8e-b106-d8dec734a6fe | -15.0773 | -52.5183 | 2026-09-05 01:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 66d5483a-7eef-3b83-a3cc-3b82b6f2202a | -10.4717 | -46.0216 | 2026-09-05 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 1e70aa79-a295-34d2-a08f-962b93e27ec9 | -6.0244 | -60.1781 | 2026-09-05 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| a5861cd5-f241-30ff-be4b-f05ff277f4ee | -5.7571 | -45.0613 | 2026-09-05 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 74beb002-7ac1-3797-a7f4-b0c7b11725e6 | -6.5963 | -59.9087 | 2026-09-05 01:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| d0c38244-8059-3aa8-8ba1-e73489bc5c31 | -5.851 | -52.0465 | 2026-09-05 01:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 18f12f82-8a27-374f-989b-7092b8246914 | -6.6513 | -59.9642 | 2026-09-05 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 125.2 |
| b15a0540-b38b-3f07-af03-87300794bb3b | -3.7827 | -61.7733 | 2026-09-05 01:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 533c38cf-bb1f-3136-96a7-e7e1c226024c | -17.1081 | -56.8098 | 2026-09-05 01:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.8 |
| d1e048ec-b0b7-3a33-af6c-2e61c00f634c | -17.1078 | -56.8304 | 2026-09-05 01:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.0 |
| 3778d644-200d-3fc7-a3c2-acb7690b28cb | -5.9197 | -47.8927 | 2026-09-05 01:00:00 | GOES-19 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 128.7 |
| c742872d-302c-36bd-bed5-4efc99879e43 | -6.5962 | -59.9279 | 2026-09-05 01:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| ba903a63-156e-3466-8f50-2ac26d9bb80e | -5.7758 | -45.0599 | 2026-09-05 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 1212b644-d300-39fc-b7d9-4a0064cb7942 | -5.9383 | -47.8915 | 2026-09-05 01:10:00 | GOES-19 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| b4509f5f-9d5f-35d4-a3c5-10aca08223aa | -5.6382 | -60.2289 | 2026-09-05 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| c8b3c457-4739-3a78-b747-ae1f057bb145 | -3.7827 | -61.7733 | 2026-09-05 01:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 82c37c71-c453-36a8-84d4-ddef44fd3f7c | -6.0245 | -60.159 | 2026-09-05 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 0e151366-3e82-3957-b1b6-fee955a019ea | -5.7756 | -45.0826 | 2026-09-05 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| a392f7aa-2883-3813-b601-038de3b5e6db | -5.6381 | -60.248 | 2026-09-05 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| b6db9df3-f9a4-31f2-bf06-e50647ec8594 | -17.1078 | -56.8304 | 2026-09-05 01:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.1 |
| 5da13948-6ead-30a8-ac34-1b06a9a3b66d | -6.5963 | -59.9087 | 2026-09-05 01:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 4f6593e3-7dbb-3f22-ac7f-8ac2263e19b3 | -5.6566 | -60.2284 | 2026-09-05 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 6049da04-acd2-3486-b0ff-39c5198347d3 | -10.4717 | -46.0216 | 2026-09-05 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| c2ad32e1-748e-3857-9543-ec58ad898e43 | -5.9197 | -47.8927 | 2026-09-05 01:10:00 | GOES-19 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 5bd46d0f-d466-39e4-8870-8eb2f57b406a | -6.0244 | -60.1781 | 2026-09-05 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 912fd4e9-a2bb-35c5-9f22-c143aefecb79 | -5.565 | -60.1739 | 2026-09-05 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| cc862c5d-c84d-3255-8093-716b77d861c9 | -5.5466 | -60.1745 | 2026-09-05 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| b5665656-009a-3c45-a8be-bddae90c3430 | -3.7645 | -61.7737 | 2026-09-05 01:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 030cd403-17a3-3300-b92f-c12390a4ab19 | -5.851 | -52.0465 | 2026-09-05 01:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 82c3632f-52e8-3176-ad2b-9e45da2dbde0 | -15.0773 | -52.5183 | 2026-09-05 01:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 04bea982-b04f-35ad-bad0-bb8abd7122b6 | -5.6565 | -60.2475 | 2026-09-05 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 95.9 |
| a8b8236c-18a6-3501-a794-837479207f2f | -3.7645 | -61.7548 | 2026-09-05 01:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| ca2bbf86-00a8-3f74-9ef0-c9dcbe485a16 | -6.5962 | -59.9279 | 2026-09-05 01:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 581853e4-3c7e-39be-afd1-8f0778f8e5c3 | -5.565 | -60.1739 | 2026-09-05 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| c377035d-8489-367a-98b6-a477167510e2 | -18.1325 | -51.7096 | 2026-09-05 01:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 79679d88-5260-315a-8bcd-9bdad563c7ac | -5.6749 | -60.2469 | 2026-09-05 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 5638e315-03b4-3ffb-ba7e-c8af6dcae244 | -5.9197 | -47.8927 | 2026-09-05 01:20:00 | GOES-19 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 01c8b1df-def5-3270-b37b-2f20dbf1e352 | -9.5534 | -40.3254 | 2026-09-05 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 73.9 |
| 4155f72d-6b41-3fe6-a831-3ea7458e735e | -4.6669 | -55.635 | 2026-09-05 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| f9c158ec-425b-3393-9d81-26b2ebdc537e | -6.0244 | -60.1781 | 2026-09-05 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| cc63cdc7-8f3f-368f-9408-a5475719403a | -5.7758 | -45.0599 | 2026-09-05 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 89dee860-9fd4-3f4b-aaee-5cee8bdb65fa | -5.9383 | -47.8915 | 2026-09-05 01:20:00 | GOES-19 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| eebf0dce-ffd8-3fb7-a32b-6e87e43ea703 | -3.7645 | -61.7548 | 2026-09-05 01:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 64e64400-8034-3493-9ea8-69d8c4b20394 | -6.0428 | -60.1775 | 2026-09-05 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 9d3b698c-fc7f-3005-9f38-e3c1d0cfc291 | -5.675 | -60.2278 | 2026-09-05 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| bef441b7-1c86-3ef2-bf44-eaba76a16869 | -5.7756 | -45.0826 | 2026-09-05 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| c6b2efd2-9a66-3eab-b13c-bc1f5d2145a1 | -13.4264 | -43.8163 | 2026-09-05 01:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 79447fff-1e2c-3f7d-8fb0-48727fa84111 | -17.1078 | -56.8304 | 2026-09-05 01:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 118.7 |
| 4fec4c9a-f75b-3382-9cf0-fc1575dfe2ea | -6.6698 | -59.9443 | 2026-09-05 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| e9f1063d-89fa-3372-b6bb-633355b1b496 | -3.7645 | -61.7737 | 2026-09-05 01:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 10cec9d2-9617-3732-b14a-5793acfccab6 | -3.7827 | -61.7733 | 2026-09-05 01:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| c8ca5e29-c830-3122-8a0c-f48807cd3867 | -4.6853 | -55.6343 | 2026-09-05 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| b1c5b240-8ef2-303f-bac8-c7fe9f9fdc02 | -15.0773 | -52.5183 | 2026-09-05 01:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| b7d4c3cf-3b91-3f25-9958-068c49d34be1 | -5.6566 | -60.2284 | 2026-09-05 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 7ce4420a-5b39-3b0d-b383-c67218047a51 | -5.6565 | -60.2475 | 2026-09-05 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 9cd1182e-7ce2-3e61-b467-bcbe4056587d | -5.1802 | -56.0518 | 2026-09-05 01:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 3819e0f6-ef54-32e8-91f8-2992be297517 | -6.0245 | -60.159 | 2026-09-05 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 38bcee40-4401-3c50-9072-9836a12640b8 | -6.0429 | -60.1584 | 2026-09-05 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |


[Clique aqui para ver as próximas entradas](README7.md)
