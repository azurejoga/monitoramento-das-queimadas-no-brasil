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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57461452-655c-34c2-a98d-9051a2b07c18 | -7.16223 | -35.14489 | 2024-10-31 03:10:00 | NOAA-20 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6a401042-f843-3c52-bbaf-ca8becf03db4 | -7.06906 | -39.9905 | 2024-10-31 03:10:00 | NOAA-20 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f880dfe5-b294-3844-a954-0b2332c9890b | -7.06253 | -39.98907 | 2024-10-31 03:10:00 | NOAA-20 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 746fb90d-7410-30fa-b9b9-1a32f7db9e72 | -6.96484 | -39.83613 | 2024-10-31 03:10:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 4cb52a49-e468-357b-ad31-55477a1b92b1 | -6.96377 | -39.84204 | 2024-10-31 03:10:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e22672cb-1796-3751-81a5-906f5bd33bb0 | -6.96355 | -39.83847 | 2024-10-31 03:10:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| fe96eca2-2646-3d6b-8ed2-bbbc0f3925eb | -6.70823 | -37.49688 | 2024-10-31 03:10:00 | NOAA-20 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 15242728-cde9-371c-b898-b320c025a63b | -6.70324 | -37.49199 | 2024-10-31 03:10:00 | NOAA-20 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bd9a0406-f165-3bde-8554-db7ebd0af2a9 | -6.70244 | -37.49652 | 2024-10-31 03:10:00 | NOAA-20 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4fea19e9-5f7d-3098-b364-188bbdc0fa7a | -6.6841 | -37.46812 | 2024-10-31 03:10:00 | NOAA-20 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8a7de1f3-855f-3ff5-83bc-ab9806796472 | -6.68342 | -37.47193 | 2024-10-31 03:10:00 | NOAA-20 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a87f440b-487b-32c1-82d5-4d333c3caa98 | -6.68256 | -37.47673 | 2024-10-31 03:10:00 | NOAA-20 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c4f98e58-7159-387e-9940-f2983da5fca2 | -6.6784 | -37.46733 | 2024-10-31 03:10:00 | NOAA-20 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 70b212d1-8ab1-326f-9a79-be206ece6115 | -6.67768 | -37.47133 | 2024-10-31 03:10:00 | NOAA-20 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 4.6 |
| c914173b-6089-393d-bd66-22d430c94cf9 | -6.65388 | -39.27235 | 2024-10-31 03:10:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 63b00948-aa30-327b-b451-8c0fb2b440ee | -11.70147 | -37.5481 | 2024-10-31 03:10:00 | NOAA-20 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9c0fc030-8166-392f-aab8-ecdf97c71ddb | -11.70085 | -37.55133 | 2024-10-31 03:10:00 | NOAA-20 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3d439b28-2ae4-31f8-a330-1bf2a2e03ee2 | -4.1942 | -38.9731 | 2024-10-31 03:15:29 | GOES-16 | GUARAMIRANGA | CEARÁ | Brasil | 2305100 | 23 | 33 | nan | nan | nan | Caatinga | 92.6 |
| 33be786f-476c-3d92-bb6d-d313ad0998fe | -4.2749 | -43.4357 | 2024-10-31 03:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| f2fb3c63-f5a0-3426-81f0-3045657c6b43 | -6.1414 | -43.9794 | 2024-10-31 03:15:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 479a5efd-3f36-3572-9750-e0c17e2ee59e | -6.1416 | -43.9563 | 2024-10-31 03:15:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 144c7eab-6a22-3b5d-8661-bcaefa78e278 | -6.1226 | -43.9809 | 2024-10-31 03:15:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 43943f52-5643-3367-9c7f-c4a686eefbb0 | -6.1229 | -43.9578 | 2024-10-31 03:15:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| dbf1809e-8249-3cab-b4a1-6041525d4665 | -10.0118 | -64.8023 | 2024-10-31 03:16:03 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 41.4 |
| c8d0ba00-c194-3d59-8cc3-c1388a39cb70 | -10.6819 | -65.002 | 2024-10-31 03:16:07 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 67566fc6-4f8b-3953-94b5-075c8fe4908b | -2.5216 | -48.4591 | 2024-10-31 03:25:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 6c397f15-0f08-34ae-a323-7bba4282059d | -4.2749 | -43.4357 | 2024-10-31 03:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| d28f04d2-1e47-3d78-bd3e-92a6da2e4afd | -4.8178 | -45.8429 | 2024-10-31 03:25:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 128.0 |
| d618f420-4b43-3e5b-971e-a7cbef25ab6c | -4.8364 | -45.8418 | 2024-10-31 03:25:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 439a967b-d972-3b83-a59c-de693844401c | -6.1414 | -43.9794 | 2024-10-31 03:25:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 6855eb7c-75a4-37c3-a272-a79044af6c5f | -6.1416 | -43.9563 | 2024-10-31 03:25:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| bfb475b4-0143-352e-9534-fb7e0813bfb9 | -6.1226 | -43.9809 | 2024-10-31 03:25:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 57a95178-8763-3671-9017-edf5b7cf961e | -6.1229 | -43.9578 | 2024-10-31 03:25:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 16766777-d975-3980-a8f4-c2f718d855dc | -10.0118 | -64.8023 | 2024-10-31 03:26:03 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 5c32f45d-689f-33a6-ab64-ac8c35c0b741 | -10.6819 | -65.002 | 2024-10-31 03:26:07 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 32.5 |
| bb686d44-96ad-33e5-bf19-033c1fb49d15 | -2.5215 | -48.4806 | 2024-10-31 03:35:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 471b5d90-7e67-3a28-b622-b34dcdc163a0 | -2.5216 | -48.4591 | 2024-10-31 03:35:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| a5ab047f-b709-3f0e-8849-7c9c26f63f3a | -4.2749 | -43.4357 | 2024-10-31 03:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 4f455494-355b-3b42-b8e7-7962cae318cf | -4.818 | -45.8205 | 2024-10-31 03:35:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 47.2 |
| e9675781-da40-37b9-90f2-4f236f749901 | -4.8364 | -45.8418 | 2024-10-31 03:35:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 9e0115c1-57a4-3332-ab68-a51796725bc2 | -4.8178 | -45.8429 | 2024-10-31 03:35:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 125.4 |
| 41c3b464-4cbb-3d2b-b081-6a6599763f93 | -5.0466 | -45.1542 | 2024-10-31 03:35:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 811147d4-1a95-3125-8463-b83b0d4402f0 | -6.1229 | -43.9578 | 2024-10-31 03:35:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| ed32169f-1f21-3609-8669-1708487cc685 | -6.1416 | -43.9563 | 2024-10-31 03:35:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 98ba3160-7eca-31d3-acf3-ba8799fad83e | -10.0118 | -64.8023 | 2024-10-31 03:36:03 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 1ebe0b3a-2613-3861-ab69-4513756a11b5 | -10.6819 | -65.002 | 2024-10-31 03:36:07 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 3bb275bc-26b6-3874-91af-505ec3135ff7 | -1.4426 | -52.273 | 2024-10-31 03:45:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 0fc9a21b-a1d0-31a8-8387-e1b9cdca8378 | -2.5215 | -48.4806 | 2024-10-31 03:45:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 26604dac-7660-377a-beb7-c792ff895d04 | -2.5216 | -48.4591 | 2024-10-31 03:45:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| d97b989e-124f-39bc-9a57-9e67b8b8c8bb | -4.8364 | -45.8418 | 2024-10-31 03:45:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 3866d7dd-b282-3a5c-9366-f896d677bf59 | -4.8176 | -45.8653 | 2024-10-31 03:45:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 47.8 |
| d0129843-f652-3516-9c82-9898dda6ab96 | -4.8178 | -45.8429 | 2024-10-31 03:45:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 111.8 |
| f70bc229-d601-3fe5-b2ae-054e488947b7 | -4.818 | -45.8205 | 2024-10-31 03:45:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 2273b507-ffa2-343f-bc92-c1307901fb0b | -6.1229 | -43.9578 | 2024-10-31 03:45:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 9e83da88-457c-3003-88dc-585935cd9317 | -6.1416 | -43.9563 | 2024-10-31 03:45:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| eb58be0d-33a8-3848-97b5-b145a0892e13 | -9.7414 | -36.1043 | 2024-10-31 03:46:00 | GOES-16 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 121.9 |
| 070bb81f-80a2-3402-aa85-4a09ecfd5d86 | -9.7419 | -36.0772 | 2024-10-31 03:46:00 | GOES-16 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 81.9 |
| 8b90731f-868f-3a29-bfac-cc2116da9d6e | -10.0118 | -64.8023 | 2024-10-31 03:46:03 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 546d5043-8f69-3891-8162-9f4db606e8d2 | -10.6819 | -65.002 | 2024-10-31 03:46:07 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 32.7 |
| ec9d3073-f465-3d67-8360-bfcf1b6f1145 | -12.4204 | -63.2874 | 2024-10-31 03:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 88869994-29fe-360b-8fad-a19e29870358 | -19.5083 | -56.5989 | 2024-10-31 03:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.8 |
| 60ce4188-27e3-31df-be7b-afbd24f1cb57 | -2.5215 | -48.4806 | 2024-10-31 03:55:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 34f0c996-c547-3d2f-a476-4afde44cdc95 | -2.5216 | -48.4591 | 2024-10-31 03:55:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| ba23a652-6272-36b9-a34c-6a28ec15448d | -4.8178 | -45.8429 | 2024-10-31 03:55:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 1aa95bde-75a1-3ec6-92a3-df61f043b1df | -4.8364 | -45.8418 | 2024-10-31 03:55:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 252422e2-999b-3a6d-a245-fb47ce725063 | -6.1229 | -43.9578 | 2024-10-31 03:55:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 6834bad8-02d4-32e7-832a-b5f8b1e5f636 | -6.1414 | -43.9794 | 2024-10-31 03:55:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 72d63718-48d1-36ec-9f4a-27cd3592368f | -6.1416 | -43.9563 | 2024-10-31 03:55:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| da501372-9e7f-3e0d-9343-dec450aa797c | -10.0118 | -64.8023 | 2024-10-31 03:56:03 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 35.2 |
| b54b9da1-0f31-3c77-91d1-d18da70e867e | -10.6819 | -65.002 | 2024-10-31 03:56:07 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 16184f48-410d-31f9-9956-f1734c0ae57d | -12.4204 | -63.2874 | 2024-10-31 03:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 33b809ad-3845-3fc3-8a59-625bb9f6f18d | -12.4206 | -63.2682 | 2024-10-31 03:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 46789923-1876-331a-92b3-3643cbb9f537 | -12.4393 | -63.2864 | 2024-10-31 03:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 62fbe0c1-9a8f-37d3-b8e8-0ca20cdc41cb | -19.4882 | -56.6017 | 2024-10-31 03:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.6 |
| a2c1d0bf-8154-3f9f-b455-d1e18215ead1 | -19.5083 | -56.5989 | 2024-10-31 03:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.0 |
| 92065c51-e89a-3906-bd58-981405086675 | -2.5215 | -48.4806 | 2024-10-31 04:05:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 1ad86b24-6991-3a2e-a8f5-fd60bc9335d0 | -2.5216 | -48.4591 | 2024-10-31 04:05:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 5901ede9-999d-3541-83f5-763948d3fbec | -4.8178 | -45.8429 | 2024-10-31 04:05:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 117.2 |
| e2af8b6a-7086-38f9-ab0a-2c8290e8d410 | -4.8364 | -45.8418 | 2024-10-31 04:05:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 30ade002-496f-3c8b-8bb2-39919a29c0b6 | -5.0466 | -45.1542 | 2024-10-31 04:05:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 8c3d4f99-ebfd-3400-97cb-8de9ea9b6f44 | -6.1229 | -43.9578 | 2024-10-31 04:05:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 7e0f3fed-1473-382f-a743-a66d723ed211 | -6.1416 | -43.9563 | 2024-10-31 04:05:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 33c8eb41-66b1-318b-841b-4a06c816bdb0 | -22.82118 | -42.05915 | 2024-10-31 04:06:00 | NOAA-21 | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 142968dc-fd92-318c-8bf9-cef4611ce228 | -22.17846 | -42.4685 | 2024-10-31 04:06:00 | NOAA-21 | BOM JARDIM | RIO DE JANEIRO | Brasil | 3300506 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1373dbcd-8f24-33c5-b3d1-7b0fad3c7c49 | -21.62448 | -43.46817 | 2024-10-31 04:06:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d7509ba9-3436-33f3-8bf4-040777aa9aa1 | -22.28151 | -45.46448 | 2024-10-31 04:06:00 | NOAA-21 | PEDRALVA | MINAS GERAIS | Brasil | 3149101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b85b1923-a54c-31c6-a3ad-bac4678ed44c | -22.53329 | -44.43065 | 2024-10-31 04:06:00 | NOAA-21 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| be6d0ed3-8480-3462-b7da-06ea371b3ed2 | -22.53269 | -44.43439 | 2024-10-31 04:06:00 | NOAA-21 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 68e0cb90-4fc6-32c8-bc6a-df29845cd4fe | -22.52997 | -44.43005 | 2024-10-31 04:06:00 | NOAA-21 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 629d48fe-3735-356e-b252-26e53a413737 | -23.76084 | -45.72903 | 2024-10-31 04:06:00 | NOAA-21 | SÃO SEBASTIÃO | SÃO PAULO | Brasil | 3550704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| caaa90aa-2fbc-3632-a73a-972ef579f63f | -20.93931 | -46.62569 | 2024-10-31 04:06:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 15d3d0f7-2d59-3408-9bcf-4623ffc7b2cd | -23.70478 | -46.47649 | 2024-10-31 04:06:00 | NOAA-21 | MAUÁ | SÃO PAULO | Brasil | 3529401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6b262deb-7e64-338d-ab5b-2da3978050aa | -23.63097 | -46.42704 | 2024-10-31 04:06:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 75ff97a1-e9be-3d13-b8a1-8cee16153c70 | -20.9565 | -47.17108 | 2024-10-31 04:06:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 16.7 |
| dd433b83-f2e6-3937-b9f6-d7fc90d38ade | -20.70967 | -47.28821 | 2024-10-31 04:06:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 741dd02a-dd38-31f0-858f-03830366cc7a | -20.64765 | -47.22615 | 2024-10-31 04:06:00 | NOAA-21 | ITIRAPUÃ | SÃO PAULO | Brasil | 3523701 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 018f2c4b-c968-3bc1-9813-37d4d9fd8cb5 | -20.76412 | -46.76806 | 2024-10-31 04:06:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ff768c2c-a538-3644-8846-6b9fc492975a | -22.42476 | -48.58244 | 2024-10-31 04:06:00 | NOAA-21 | BARRA BONITA | SÃO PAULO | Brasil | 3505302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 8c2b4810-21e1-35eb-abe6-34c0a045bcde | -22.28002 | -48.97818 | 2024-10-31 04:06:00 | NOAA-21 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c132190f-6052-3284-a1d0-5cc4e4523a70 | -22.27852 | -48.97826 | 2024-10-31 04:06:00 | NOAA-21 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README14.md)
