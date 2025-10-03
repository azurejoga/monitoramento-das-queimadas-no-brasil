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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa926355-a2d9-3e1f-b58a-aea2faaac424 | -16.3577 | -42.3737 | 2025-10-03 01:40:00 | GOES-19 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 8abb6c0f-716b-38ee-bbdc-89c7e67b699a | -8.6138 | -54.976 | 2025-10-03 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| dd987a13-7129-31e2-9b43-5856437feb83 | -13.1345 | -47.882 | 2025-10-03 01:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 4e51046b-4596-3bd9-8023-a764aeb93737 | -4.6877 | -45.8056 | 2025-10-03 01:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 40.3 |
| b6ac75bf-67f7-3866-bd17-9f7d5897ad75 | -12.6323 | -46.9697 | 2025-10-03 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 82a64a2c-9636-3ec8-98d9-6dfa56727ad8 | -7.7746 | -42.5865 | 2025-10-03 01:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 180.3 |
| 45d2f981-7786-3f73-b398-6d3b2db9cfd8 | -11.9163 | -46.2817 | 2025-10-03 01:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| d5dc126a-d2eb-32f4-be1a-24596d477f79 | -11.144 | -43.4082 | 2025-10-03 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 146.4 |
| 0399c7cd-9e4c-39ea-869d-c8cf7b0a6602 | -4.6504 | -45.8077 | 2025-10-03 01:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 163.0 |
| 550608be-5206-3fc0-8903-485fdbcda01f | -11.1631 | -43.4054 | 2025-10-03 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 78.0 |
| c92e58d8-87cc-3d90-abbb-4a1cc49931f0 | -9.9182 | -43.7212 | 2025-10-03 01:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 78.1 |
| 03cd1f1f-9598-3bd8-8ecf-3253c3db20aa | -6.0605 | -44.6061 | 2025-10-03 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 8c444935-b80c-3294-a13d-00a32c810fe2 | -7.7743 | -42.6103 | 2025-10-03 01:40:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 87.4 |
| 7e18e35b-800f-3a1b-a7b2-30f01c5d1fc8 | -5.655 | -43.9013 | 2025-10-03 01:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 226b34e5-769e-322c-951b-5ecb05fe8381 | -13.9775 | -48.157 | 2025-10-03 01:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 4e9aa0ac-70fc-3a81-ad73-c917e940ec08 | -5.6361 | -43.9258 | 2025-10-03 01:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 6a215bc7-e0ef-3016-84ad-3af9f562a528 | -13.7769 | -47.5392 | 2025-10-03 01:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 82.6 |
| fde914f9-817f-388d-8279-4ea6d39b5c98 | -8.6324 | -54.9747 | 2025-10-03 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 68ee8102-76d0-38ee-a6cb-61deeb184bbe | -11.1444 | -43.3845 | 2025-10-03 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 88.9 |
| 05479f7e-32e5-3c58-9d63-53c898cffc87 | -6.3301 | -58.0453 | 2025-10-03 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 9cdf28ae-340c-32f4-b74a-1203ec22d724 | -4.6505 | -45.7853 | 2025-10-03 01:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 177.1 |
| 5b0e8d63-e4e3-3d7e-b5f6-911bdfb3bbc4 | -7.7749 | -42.5628 | 2025-10-03 01:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 103.3 |
| 4367a46f-d7a3-380e-bcfd-e4e3a324667c | -16.3378 | -42.3783 | 2025-10-03 01:40:00 | GOES-19 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 97.7 |
| afd8643c-fbdd-3fe5-b326-e1f7618219a4 | -4.6692 | -45.7842 | 2025-10-03 01:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 258.7 |
| 9bf16b97-b502-3131-b052-060417a01290 | -12.6135 | -46.9499 | 2025-10-03 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 6c140aff-872d-3509-bd45-761c84aad9b3 | -12.6131 | -46.9725 | 2025-10-03 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 65dc1f60-ebc2-302b-b4d8-df1c6af8ba55 | -7.756 | -42.5648 | 2025-10-03 01:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 95.5 |
| 8e09eef2-b3fb-3037-859a-dc5cb94e9fb0 | -4.669 | -45.8066 | 2025-10-03 01:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 284.1 |
| 3e7d3ff9-33b2-326a-b750-bd6241b20600 | -6.0416 | -44.6304 | 2025-10-03 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| de9a6b1e-98a2-353f-86ce-0a2a89310d45 | -6.0418 | -44.6076 | 2025-10-03 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| f10960f5-c377-352c-9c17-63a4fdd65e8f | -4.6878 | -45.7832 | 2025-10-03 01:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 0527d0a9-df34-395b-a7ae-8df468917ad2 | 1.5103 | -55.8259 | 2025-10-03 01:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 00fd20e7-ee3f-3f83-a13f-3de87d0b8e19 | -4.6505 | -45.7853 | 2025-10-03 01:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 264.6 |
| cf3dab9e-5b92-3fab-b056-c1273381f94b | -7.7557 | -42.5885 | 2025-10-03 01:50:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 110.1 |
| 32d03f3d-5044-3718-aca5-01275a551e0b | -5.6361 | -43.9258 | 2025-10-03 01:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 92cbba3f-cd58-3b97-b318-b3e827038241 | -14.9538 | -46.8931 | 2025-10-03 01:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 60.2 |
| f6f2d7c5-1229-30a6-aeed-6d009b18559f | -7.7746 | -42.5865 | 2025-10-03 01:50:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 159.5 |
| 62454935-b71e-30fe-ac03-13eed3050ce0 | -4.6878 | -45.7832 | 2025-10-03 01:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 48.6 |
| aaa3120e-fd2d-3298-9b30-336beecec378 | -5.6363 | -43.9027 | 2025-10-03 01:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 436990ff-2156-31da-882b-2421454658db | -13.9775 | -48.157 | 2025-10-03 01:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 9cf65aef-1928-3787-b6d2-d97d7185e172 | -6.0418 | -44.6076 | 2025-10-03 01:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| fb23c65e-4199-3c68-ab81-3a88d84ab165 | -7.756 | -42.5648 | 2025-10-03 01:50:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 92.0 |
| a300b878-2954-324b-9ab8-f821c84f0d49 | -10.2781 | -50.3032 | 2025-10-03 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 733dc4ee-f385-3558-95fb-64f3bf833550 | -4.6504 | -45.8077 | 2025-10-03 01:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 208.2 |
| c2368897-e89f-3514-bada-a34210765d3c | -12.6131 | -46.9725 | 2025-10-03 01:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 8470a3ce-348a-34f9-bf97-5d87a851f585 | -6.0605 | -44.6061 | 2025-10-03 01:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 8878d138-832f-3e3e-86af-135f7e43d578 | -11.1631 | -43.4054 | 2025-10-03 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 118.1 |
| 695e31b0-f7f7-3e5e-9485-87584e41a6bc | -4.669 | -45.8066 | 2025-10-03 01:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 464.5 |
| 498e1067-1980-352b-b633-cc3c90c614e2 | -8.6324 | -54.9747 | 2025-10-03 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 677a447b-b8de-3f8e-92ba-ed6ca65bae0f | -12.6135 | -46.9499 | 2025-10-03 01:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| dc5d65ef-8a9e-3b22-8199-304ec87a8588 | -6.0416 | -44.6304 | 2025-10-03 01:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| b5029ab3-9d52-3f22-ad54-0fa0c1d53355 | -12.6323 | -46.9697 | 2025-10-03 01:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 7de48e41-f8e1-33d4-9791-ce5a8190be7d | -4.6692 | -45.7842 | 2025-10-03 01:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 487.1 |
| db985d95-6718-3edd-8c2c-f59c46a24f08 | -14.9132 | -46.9684 | 2025-10-03 01:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 73.1 |
| c02e59b8-ca6d-399e-b742-4c8ab7688c13 | -11.1444 | -43.3845 | 2025-10-03 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 93.2 |
| 94541002-92f3-3d8e-b606-7c56653943b7 | -9.8991 | -43.7237 | 2025-10-03 01:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 62.4 |
| b43f5707-c27d-3e0c-9833-894bee31271d | -5.655 | -43.9013 | 2025-10-03 01:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 983f0a41-ed44-3ed2-b254-b3b0f3c79b0a | -14.7083 | -43.8869 | 2025-10-03 01:50:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 67.1 |
| 94e05ecd-4f12-3508-bc32-126f31a7840b | -10.2584 | -50.3692 | 2025-10-03 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 31.5 |
| e91a10df-5b20-3817-8f49-e2191d3cd95f | -14.9342 | -46.8965 | 2025-10-03 01:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 0b009f22-8215-314d-a43a-42e128001b61 | -8.6138 | -54.976 | 2025-10-03 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| e16bf091-d2b5-333b-a4a0-4a5eb848e95b | -6.0603 | -44.629 | 2025-10-03 01:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 4d4e8eb8-fe00-3926-95e0-a0f724c4e540 | -13.7769 | -47.5392 | 2025-10-03 01:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 0ca9d516-ada8-3686-b10b-8884b8beaf06 | -13.1345 | -47.882 | 2025-10-03 01:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| bc6e4e0a-e84a-3c74-a959-d59b77d347cd | -4.6877 | -45.8056 | 2025-10-03 01:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 5df3f1cf-01fa-3aef-afcf-3d569773ee94 | -9.9182 | -43.7212 | 2025-10-03 01:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 81.4 |
| bfae1f82-c760-392b-b7a0-e7e01a515590 | -12.6327 | -46.9471 | 2025-10-03 01:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 153b2ef7-6e0a-3d09-abeb-c73d6f50be87 | -11.9163 | -46.2817 | 2025-10-03 01:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| c60ec322-a94c-35a0-a9c7-cc96e71fb961 | -11.144 | -43.4082 | 2025-10-03 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 143.4 |
| ee565bdc-57c3-3335-82c1-a11a371312dd | -10.2587 | -50.3478 | 2025-10-03 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 42.1 |
| fe90cf6e-dd47-311d-be3e-23687438ff7f | -7.7749 | -42.5628 | 2025-10-03 01:50:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 110.2 |
| 8b5550dd-0647-387d-9bf9-396bbc5952e4 | -9.9182 | -43.7212 | 2025-10-03 02:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 72.7 |
| e6bd8273-c007-3ed6-804d-2b1006265534 | -11.9163 | -46.2817 | 2025-10-03 02:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 488776fa-41e0-32f1-b135-704e111e04b2 | -9.8991 | -43.7237 | 2025-10-03 02:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 67.4 |
| ccb2439b-83b9-372f-a3d8-73fbf596fa4c | -5.6361 | -43.9258 | 2025-10-03 02:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 20118422-4b01-378a-bc40-f53a2680adcb | -10.2587 | -50.3478 | 2025-10-03 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 39.6 |
| f99e8952-1463-320b-8279-43490f7e201e | -8.6138 | -54.976 | 2025-10-03 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| e046f444-b228-3182-90d8-3d0998fa3a34 | -12.6135 | -46.9499 | 2025-10-03 02:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| eeb83729-caad-3e68-913a-342034926763 | -12.6131 | -46.9725 | 2025-10-03 02:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| cc6fda6f-9bca-30dc-9a3b-0951d8032c14 | -5.655 | -43.9013 | 2025-10-03 02:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 1a4dca05-60d3-3cc7-bb5e-c744e87eee63 | -10.967 | -51.0826 | 2025-10-03 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 33.0 |
| b1f6bb7c-a7ff-34fd-b776-8667d50dc1cc | -14.9538 | -46.8931 | 2025-10-03 02:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 59.5 |
| e1aa4db3-6a9e-3e2d-b7e4-9d8ce25217d1 | -5.6363 | -43.9027 | 2025-10-03 02:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 07923143-a8a9-37e3-b505-f61bd746ad8a | -8.6324 | -54.9747 | 2025-10-03 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 76430b2a-92aa-32a4-b148-f51ed21cc3b5 | -6.0416 | -44.6304 | 2025-10-03 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 189e6fc3-e389-3bb6-9bf5-9ddab711a731 | -12.6323 | -46.9697 | 2025-10-03 02:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 5f91b8aa-0906-3bf5-a783-be35dec3181d | -6.0418 | -44.6076 | 2025-10-03 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| bdba6705-b773-3dd3-a8c7-e68c329a4dad | -13.3418 | -48.1188 | 2025-10-03 02:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 0b81a463-a98a-39b4-9c6d-72d3eb09c70f | -10.2781 | -50.3032 | 2025-10-03 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 62102ea2-61c5-37b5-9eea-ce324b32f684 | -9.0808 | -46.6545 | 2025-10-03 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 2adbad1e-a4c2-36e9-993c-ce0221c0fafb | -7.756 | -42.5648 | 2025-10-03 02:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| e1ee1832-7fc4-3d5a-a45f-558e7c70a35d | -9.062 | -46.6565 | 2025-10-03 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 520cf87a-cd4d-3aeb-8f94-cdc1667abb8f | -11.1444 | -43.3845 | 2025-10-03 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 82.5 |
| 1b85bd34-8684-3fed-958a-a2a1a0568ea3 | -6.0605 | -44.6061 | 2025-10-03 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 39199e64-0a84-3100-a7e6-a2d5f0443984 | -13.9775 | -48.157 | 2025-10-03 02:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 95.7 |
| e1038918-065a-3ca1-8f68-8ba580ee687b | -13.1345 | -47.882 | 2025-10-03 02:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| cc88e883-7fcc-3cd1-bd90-1008fb93adbc | 1.5103 | -55.8259 | 2025-10-03 02:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| bd084e07-7ecf-3163-9c98-aae08980eeb5 | -11.8967 | -46.3071 | 2025-10-03 02:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 205030cb-1e5a-39c6-ba41-187bf169e0f7 | -14.9342 | -46.8965 | 2025-10-03 02:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 80ec1693-4899-36c8-8d38-dfb64d588c1e | -11.1631 | -43.4054 | 2025-10-03 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 73.7 |


[Clique aqui para ver as próximas entradas](README13.md)
