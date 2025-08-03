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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14c2c5b6-58ba-37fa-9dbd-e43caf20af0a | -8.0126 | -43.1749 | 2025-08-03 08:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.3 |
| f2aa4c45-e0d1-35bd-aeab-16ef895df9dd | -8.0129 | -43.1513 | 2025-08-03 08:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 182.3 |
| 2336d6b1-46b2-3a85-b747-3665e6261ba8 | -7.9937 | -43.1769 | 2025-08-03 08:20:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 55.6 |
| 09ce1286-4895-33f6-bfe2-cc899b48aee0 | -7.994 | -43.1534 | 2025-08-03 08:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 109.5 |
| 1b5edffd-6160-326f-8163-db81bd255dda | -8.0126 | -43.1749 | 2025-08-03 08:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.7 |
| d4dc607a-081a-387c-b7bc-02fc0692233d | -8.0129 | -43.1513 | 2025-08-03 08:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 168.6 |
| c257f74b-d8c0-32ad-a87c-9a6a1b7cbc2c | -10.476 | -46.9877 | 2025-08-03 08:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 68a52f4e-c74e-3272-9b61-349a1d00b2d6 | -10.495 | -46.9854 | 2025-08-03 08:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 81f281ec-1e91-3a94-92d0-42665d86d2ab | -7.994 | -43.1534 | 2025-08-03 09:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 141.2 |
| b5e6f973-8ad1-363a-aa96-abf22cfceb0a | -8.0129 | -43.1513 | 2025-08-03 09:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 254.5 |
| e55bb920-8087-383d-ac74-ed9894fa8315 | -7.994 | -43.1534 | 2025-08-03 09:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 271.7 |
| 2c9c0765-1457-34e2-bb0c-490a59583a5c | -8.0129 | -43.1513 | 2025-08-03 09:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 289.6 |
| 89741153-1742-3ac3-8c78-8621e9f339f3 | -7.9937 | -43.1769 | 2025-08-03 09:30:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 111.7 |
| 91a84def-ebd3-3a62-a37e-caf2f41582dd | -10.4757 | -47.0101 | 2025-08-03 09:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| ef7fd0c1-f234-3391-9084-ebe6a891d376 | -7.994 | -43.1534 | 2025-08-03 09:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 275.7 |
| 28f1181c-1914-3f3d-beaf-d710687c1ff8 | -8.0129 | -43.1513 | 2025-08-03 09:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 268.5 |
| 9d37ca8c-4188-3509-8798-6b9268fb4ed1 | -7.9937 | -43.1769 | 2025-08-03 09:40:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 116.7 |
| a5251d5b-024d-3624-8905-222f791b5ba6 | -7.994 | -43.1534 | 2025-08-03 09:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 276.5 |
| b926719e-602b-3fd8-9bc9-ef2019c67495 | -8.0129 | -43.1513 | 2025-08-03 09:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 307.6 |
| 2ce26703-7e92-3f08-8453-b2dd04866401 | -8.0129 | -43.1513 | 2025-08-03 09:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 335.6 |
| 80e8ba84-c5b3-36b2-af42-97473873275b | -7.994 | -43.1534 | 2025-08-03 09:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 242.8 |
| 7a0544f1-c61f-3bc8-9430-a90e375ab9fb | -8.0129 | -43.1513 | 2025-08-03 10:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 304.9 |
| a17d114b-4c6f-355b-84ca-c24f6a157807 | -7.9937 | -43.1769 | 2025-08-03 10:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 111.0 |
| 00ff52ad-23ce-3171-a0b0-891c6a0899e3 | -7.994 | -43.1534 | 2025-08-03 10:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 289.5 |
| 1792755c-c0da-3c46-8c88-aa6f37991a1d | -8.0126 | -43.1749 | 2025-08-03 10:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 101.4 |
| 3471c097-cddd-38aa-a6fc-3569c326b86d | -7.994 | -43.1534 | 2025-08-03 10:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 242.1 |
| f32d2321-b909-3688-a68c-385d111e188a | -10.4757 | -47.0101 | 2025-08-03 10:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| fea22f07-91c4-3435-8174-db96977efa00 | -8.0129 | -43.1513 | 2025-08-03 10:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 369.4 |
| e9a9f678-f437-3b91-adb5-5671af945e6d | -7.9937 | -43.1769 | 2025-08-03 10:20:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 110.4 |
| 9aaa4961-8015-3573-8a50-ca3d54cdcf54 | -8.0126 | -43.1749 | 2025-08-03 10:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 121.3 |
| aade9f6e-4b73-3572-8919-0734ef6c2368 | -8.0129 | -43.1513 | 2025-08-03 10:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 320.4 |
| d3577267-c3bb-3c6a-85cd-f76ea76106ce | -7.994 | -43.1534 | 2025-08-03 10:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 194.4 |
| cf6aff4d-0b53-3754-b3c2-3f4902791b1c | -8.0129 | -43.1513 | 2025-08-03 10:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 538.4 |
| e79479eb-e2ee-3366-a081-536a0403fc24 | -8.0126 | -43.1749 | 2025-08-03 10:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 215.8 |
| 3653cf95-33c7-3cc0-bcc2-83a2c8cf0d74 | -7.9937 | -43.1769 | 2025-08-03 10:30:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 168.9 |
| d6cf894e-1b98-3d54-a2e3-ed5912eff8cd | -7.994 | -43.1534 | 2025-08-03 10:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 430.9 |
| 8a75fa50-aa26-329e-9c00-4e9dd90c8eb0 | -7.994 | -43.1534 | 2025-08-03 10:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 668.7 |
| 695ce8b9-8148-3a66-9240-7549c86fdc09 | -8.0129 | -43.1513 | 2025-08-03 10:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 483.0 |
| 39ff4e63-7c05-3449-ace4-e2176d68e91f | -8.0126 | -43.1749 | 2025-08-03 10:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 169.4 |
| adcab067-203f-3123-ac38-ad0af7c6c019 | -7.9937 | -43.1769 | 2025-08-03 10:40:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 221.9 |
| 66b8442e-14c6-3e97-aeef-6ddbb160e652 | -8.0132 | -43.1278 | 2025-08-03 10:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 128.1 |
| 83e3adc5-c22f-31c5-a5da-828c1b7ba78f | -10.4757 | -47.0101 | 2025-08-03 10:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 146.5 |
| c9759eaa-d978-3322-a58d-1bc21d7e93f4 | -7.9937 | -43.1769 | 2025-08-03 10:50:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 164.0 |
| e8b28b22-0751-351d-a4c0-32d074822192 | -8.0129 | -43.1513 | 2025-08-03 10:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 369.4 |
| 23db7490-783c-3810-b94b-80795e0853da | -8.0126 | -43.1749 | 2025-08-03 10:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 145.2 |
| 5447bcc2-b1b5-3f23-807a-19530e9a9e1b | -7.994 | -43.1534 | 2025-08-03 10:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 312.8 |
| 5662a506-16cb-3dcf-812c-05b4d40d46d5 | -8.0129 | -43.1513 | 2025-08-03 11:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 385.7 |
| 7090ce24-8a68-3477-8655-41ee306b993c | -7.994 | -43.1534 | 2025-08-03 11:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 222.4 |
| b880dcc2-69f8-3844-acb3-f06e505a69d3 | -7.9937 | -43.1769 | 2025-08-03 11:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 127.5 |
| 4fdc22a9-fa48-3b6d-8998-9b8a3bfda704 | -8.0126 | -43.1749 | 2025-08-03 11:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 182.6 |
| 16feb30d-25e8-32ca-8352-17d2419f49e1 | -7.9937 | -43.1769 | 2025-08-03 11:10:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 166.3 |
| 664a5b5d-8d41-379f-b0d3-9095b8f731ed | -8.0132 | -43.1278 | 2025-08-03 11:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 185.7 |
| 055ab17e-14b8-3443-ad76-bd2e2501e314 | -8.0129 | -43.1513 | 2025-08-03 11:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 600.7 |
| de152e3c-73d4-37de-9cd5-9d800c68bd07 | -7.994 | -43.1534 | 2025-08-03 11:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 362.5 |
| f8eeea87-cfe7-36af-986a-2b0d58dfc370 | -8.0126 | -43.1749 | 2025-08-03 11:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 238.1 |
| 1750c65a-f685-3720-ad71-64af2a4f7cad | -7.994 | -43.1534 | 2025-08-03 11:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 416.6 |
| dcafae3e-8777-3db4-bd30-cce9f8a834b1 | -8.0321 | -43.1257 | 2025-08-03 11:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.5 |
| 8dc5f263-bb38-3d88-ac72-2257fb1bbf02 | -8.0129 | -43.1513 | 2025-08-03 11:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 491.0 |
| d916e3f0-3a6d-31c0-b943-70920f76d737 | -8.0132 | -43.1278 | 2025-08-03 11:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 126.4 |
| 4fa7c04a-c814-3600-ab30-2f46d21c41c5 | -8.0318 | -43.1493 | 2025-08-03 11:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 116.0 |
| 698f5611-6968-305a-babc-e782393dbf05 | -8.0126 | -43.1749 | 2025-08-03 11:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 199.2 |
| f4434e19-3e8f-33ea-a0c6-74ff2c10db9e | -10.476 | -46.9877 | 2025-08-03 11:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| c58ec428-235e-372e-9fc3-30711016e148 | -8.0324 | -43.1022 | 2025-08-03 11:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 100.1 |
| a0cda1c3-fa9d-3be4-97e3-c4847c2827fa | -10.476 | -46.9877 | 2025-08-03 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| e32186a7-71fc-3286-9b07-7b9a47f13a04 | -12.4588 | -47.0173 | 2025-08-03 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 9f68547e-c004-3d95-b447-564624c87c56 | -2.73652 | -43.67985 | 2025-08-03 12:29:00 | TERRA_M-T | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 67a8905c-caa9-3de2-b320-ee94ce739cf5 | -1.01703 | -47.98436 | 2025-08-03 12:29:00 | TERRA_M-T | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| b7c98e49-8bc7-3d2e-baee-0731b208673c | -10.476 | -46.9877 | 2025-08-03 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| df777d0e-3ae1-3222-9af9-d3377f0a29ed | -8.01326 | -43.17067 | 2025-08-03 12:32:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 411.1 |
| 24cbd33a-ea27-30dd-a1de-f3ff0b18f35b | -10.7165 | -48.72601 | 2025-08-03 12:32:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 65877db1-45d3-3a0d-ac55-0553cb90c0f4 | -10.26469 | -50.1564 | 2025-08-03 12:32:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 5a996181-2824-3e6e-867b-f68ae3c00367 | -7.96394 | -45.09628 | 2025-08-03 12:32:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 21.7 |
| eff78e87-5ced-3bbe-a98c-26096025afaa | -8.02976 | -43.13824 | 2025-08-03 12:32:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 120.2 |
| c0793282-4030-3f1b-ae41-1195cca16fd4 | -7.75749 | -45.10052 | 2025-08-03 12:32:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e9a20950-1c8e-3e88-88ea-e021281be3cc | -8.36565 | -46.53992 | 2025-08-03 12:32:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 8d7b6270-2c1b-329a-af55-9c2ae067a7ce | -7.81754 | -44.81057 | 2025-08-03 12:32:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7e5bc198-1199-3fec-baca-1e9cf2a6fb16 | -6.61609 | -59.97042 | 2025-08-03 12:32:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 438c0571-1dbd-3055-b6fc-4ebcc948a997 | -7.1111 | -43.4735 | 2025-08-03 12:32:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 3acace5a-d00a-3585-834b-e0bbf2e2ea62 | -8.33455 | -46.91204 | 2025-08-03 12:32:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 8efe5a8d-3524-305c-81b4-ce92f890b043 | -8.01678 | -43.13655 | 2025-08-03 12:32:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 108.4 |
| a0f8eb2c-8b37-39bb-971f-c5a718f4f438 | -7.6865 | -45.1135 | 2025-08-03 12:32:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 2d673d1d-00b6-3bd3-bad5-cbcdfcd3b50f | -8.02886 | -43.1522 | 2025-08-03 12:32:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 106.6 |
| 6a38ca0f-b3c9-3fab-949f-6f1c11703c7d | -10.2735 | -50.15766 | 2025-08-03 12:32:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| cb0912cf-59ec-33fc-86c4-986971a9f7c7 | -8.04531 | -43.11937 | 2025-08-03 12:32:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.1 |
| 442c611f-bdd5-3bd5-9d59-406784c82efc | -8.02723 | -43.15856 | 2025-08-03 12:32:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 42.4 |
| 57905119-a3c3-3321-8453-2a2f9e2910c9 | -8.03156 | -43.13182 | 2025-08-03 12:32:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.8 |
| eed53bd9-059f-3d42-a3b3-89c9c2761f8f | -10.48136 | -46.99288 | 2025-08-03 12:32:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 35.6 |
| e014d64f-897b-38cb-913c-c4a41bd15847 | -8.01427 | -43.15692 | 2025-08-03 12:32:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 326.4 |
| ad1a293d-7fb0-37a8-ba96-ca219abb92a6 | -10.26341 | -50.16529 | 2025-08-03 12:32:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d1b802d4-ccfa-3f8e-8399-c9fe0e94e9ec | -7.38082 | -43.73656 | 2025-08-03 12:32:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 092b402e-41c9-3a60-9e99-626aceffb77e | -7.99885 | -43.17533 | 2025-08-03 12:32:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 124.1 |
| 64f16153-aa82-37b7-b097-d1fe4da7a6a7 | -8.00562 | -43.12836 | 2025-08-03 12:32:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 34.8 |
| 9c679832-4895-3a8a-9f68-88dec80f717e | -8.01859 | -43.13014 | 2025-08-03 12:32:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.3 |
| 9f6b69f9-460d-3c52-a088-7e5b480d0dc5 | -4.77993 | -45.33464 | 2025-08-03 12:32:00 | TERRA_M-T | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 8e24163c-174f-3474-b877-bd7e2c8c9b93 | -8.03428 | -43.11131 | 2025-08-03 12:32:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 138.5 |
| 936e863c-b278-3372-a36a-f342c9caba8e | -8.04793 | -43.09856 | 2025-08-03 12:32:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 40.5 |
| 2ef1522f-08df-3dba-bcb4-a75bbf947d09 | -7.37153 | -44.1902 | 2025-08-03 12:32:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 26.3 |
| a49cd4b4-e535-3ebb-b644-df9005ccd867 | -8.36409 | -46.55136 | 2025-08-03 12:32:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3011e0df-3827-37e2-ad90-5e57f9731063 | -7.55628 | -44.87893 | 2025-08-03 12:32:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| f08628b3-8edc-3c7b-8992-23e2a5cb69a1 | -7.76536 | -45.10934 | 2025-08-03 12:32:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |


[Clique aqui para ver as próximas entradas](README32.md)
