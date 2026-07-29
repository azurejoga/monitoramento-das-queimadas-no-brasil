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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07a0090e-ffc3-3d32-b220-52f2dc06084b | -4.3774 | -47.7627 | 2026-07-29 01:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| ab8f4da6-1ff8-3399-8bdd-f15f89e012f7 | -10.9401 | -43.0355 | 2026-07-29 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 3d0e7058-2c48-39c4-a96d-7f8d0456af92 | -10.9397 | -43.0593 | 2026-07-29 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.3 |
| c4250054-684a-34ff-9a54-a01a88686c61 | -6.8708 | -46.0126 | 2026-07-29 01:50:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 0bcb9ac3-c8c5-3619-9177-2d17354d9a64 | -7.3603 | -45.8136 | 2026-07-29 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 113.6 |
| bd21213c-b181-3f16-96a1-257839e4fe91 | -18.7999 | -51.2638 | 2026-07-29 01:50:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 1af64adb-ab69-3d96-a035-e1ebb33de696 | -7.3598 | -45.8586 | 2026-07-29 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| fc74962e-7a91-3882-bcb6-6f9e9ce7fc1f | -18.8004 | -51.2417 | 2026-07-29 01:50:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 1915f661-1b81-3c3d-9c61-0e2ec0a875ae | -7.36 | -45.8361 | 2026-07-29 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 276.1 |
| d3c3af32-e27c-3039-ae01-e19f52df2f22 | -20.917299 | -57.4865 | 2026-07-29 01:57:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4fad0ca4-79a0-3e36-8c23-4f576b1596ba | -20.9076 | -57.489498 | 2026-07-29 01:57:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| dd7b2e70-ecaa-3a89-b539-f92f11b20aa3 | -20.6112 | -57.239899 | 2026-07-29 01:57:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 065a20a7-7363-3810-aade-5bcde3f7e25f | -20.9035 | -57.474201 | 2026-07-29 01:57:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ec80dd21-84cb-310a-9ab6-a36e9bceab41 | -14.3431 | -58.943802 | 2026-07-29 01:57:00 | METOP-C | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 74955b45-70bf-3002-8b52-28d2b64a9518 | -20.601601 | -57.242802 | 2026-07-29 01:57:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 8d37807e-401b-3cff-8928-1a68224dc96b | -8.9513 | -65.001198 | 2026-07-29 01:58:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e6c48d92-8e20-3821-8928-11711d11e278 | -8.9532 | -65.009399 | 2026-07-29 01:58:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8887db71-21b6-3855-b207-1f31c42f34ad | -8.8396 | -65.053299 | 2026-07-29 01:58:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5dbaafc6-280d-3fb8-8bb7-db3d51fbb3fa | -8.8215 | -66.747704 | 2026-07-29 01:58:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 811951f1-7fc3-38af-a1c7-d39dc2094bb5 | -8.8377 | -65.045197 | 2026-07-29 01:58:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d04ec636-87e9-3c64-87f5-bdbb5d82d160 | -8.9415 | -65.003502 | 2026-07-29 01:58:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 159cc6a8-4519-3e17-b665-a310a73f9e32 | -8.8232 | -66.754799 | 2026-07-29 01:58:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3fff2298-32ff-30f4-95eb-f6ab737477a1 | -10.9397 | -43.0593 | 2026-07-29 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| acd67322-32c2-3e45-aaf3-dca33c02fe5f | -6.8708 | -46.0126 | 2026-07-29 02:00:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 48a25c59-3201-31a4-b5eb-1d8aa6298fd4 | -10.9205 | -43.0622 | 2026-07-29 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 279b78b0-fc31-3e85-8de4-55582e143bf6 | -7.3598 | -45.8586 | 2026-07-29 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 794ebfbd-0bf5-3774-94b5-615317a46afe | -7.341 | -45.8602 | 2026-07-29 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 065e0628-140c-3d69-bf72-4205b0692bcf | -7.3415 | -45.8152 | 2026-07-29 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 559f1aab-5a30-3cb9-9271-fc1d5f2c9046 | -7.36 | -45.8361 | 2026-07-29 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 290.9 |
| 46d12e0a-921f-31de-be48-3d6640159efa | -7.3603 | -45.8136 | 2026-07-29 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| dad3de42-45c9-3dd4-9908-42f552084470 | -7.3413 | -45.8377 | 2026-07-29 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 299.4 |
| b8685539-8f76-3ca4-9be1-fde122b39522 | -7.3413 | -45.8377 | 2026-07-29 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 273.7 |
| aaa24f6f-ab33-37b1-91e9-708e94b99a10 | -7.3415 | -45.8152 | 2026-07-29 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 39e74faa-85ed-3bf7-b8f9-d5f98ecb596d | -7.3603 | -45.8136 | 2026-07-29 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| d6c99d14-a2ad-3a1c-9e24-e0a787bff046 | -6.8708 | -46.0126 | 2026-07-29 02:10:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| e7a22dc6-b3bc-3fe4-a30b-db36daed0c10 | -7.36 | -45.8361 | 2026-07-29 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 267.5 |
| fea82bad-6663-3692-a020-043d86e11ae9 | -7.3598 | -45.8586 | 2026-07-29 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 7506ea9a-5090-3418-85e7-078fc8576282 | -10.9205 | -43.0622 | 2026-07-29 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 9fa7a2a9-6158-3784-8770-05d69a58ee33 | -10.9397 | -43.0593 | 2026-07-29 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 334ed162-2aa9-3910-875b-a109ea91437b | -7.341 | -45.8602 | 2026-07-29 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 86da70ac-95e5-3cc1-b640-a333a7412057 | -7.34 | -45.85 | 2026-07-29 02:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af5a387d-8731-33fb-8463-fe7856a59999 | -7.37 | -45.85 | 2026-07-29 02:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 89f09661-d7d0-3900-b3d3-6c654898ab25 | -7.36 | -45.8361 | 2026-07-29 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 284.7 |
| 0bbf35c0-21ac-34ea-a1c1-fe73742755c3 | -7.3603 | -45.8136 | 2026-07-29 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 1931dc5a-350c-35f1-8e4b-9a37bd23d50e | -7.3415 | -45.8152 | 2026-07-29 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 8dca82a1-7f99-3985-9322-2fd9e6b06e56 | -7.3598 | -45.8586 | 2026-07-29 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 1c41d34d-371f-394e-9b6f-4db48cc6215f | -7.3413 | -45.8377 | 2026-07-29 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 262.3 |
| d666878f-433e-3358-b225-ef312073e0ea | -7.341 | -45.8602 | 2026-07-29 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| fd3d0623-7263-3f62-8182-9c14b42d8276 | -10.9397 | -43.0593 | 2026-07-29 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 5299d771-6a2c-3353-80c3-c589b88cfe5c | -10.9205 | -43.0622 | 2026-07-29 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 6430192a-81bc-336f-8332-e2118b740fca | -6.8708 | -46.0126 | 2026-07-29 02:20:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| f8fab288-bcab-3025-ae23-9a72dc3d7af8 | -7.3603 | -45.8136 | 2026-07-29 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 6286703d-c2d2-37d2-8354-f4eca8e159e9 | -10.9401 | -43.0355 | 2026-07-29 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 27118280-2d06-350f-a2fd-f6b8203aaa4e | -13.1523 | -51.3214 | 2026-07-29 02:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 3c256a2d-5682-3f4e-9ba3-cc4198c648a2 | -7.36 | -45.8361 | 2026-07-29 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 210.6 |
| 6d866f60-4fe1-34a7-b4fe-2ad9f5ec0706 | -7.341 | -45.8602 | 2026-07-29 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 0cfe74da-6151-3ef2-8198-df7e2ff80bfc | -10.9205 | -43.0622 | 2026-07-29 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| bfabe9af-361e-36ea-b8e1-c34994b92d4a | -7.3415 | -45.8152 | 2026-07-29 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| b7328fcc-2552-3ebd-acae-ebae35ef8dc4 | -7.3413 | -45.8377 | 2026-07-29 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 293.3 |
| 3732da3f-987b-3d35-8a87-6a8d0424a90c | -10.9397 | -43.0593 | 2026-07-29 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 149.4 |
| c59f43bc-f405-3cc7-9510-6350aa739fff | -7.3413 | -45.8377 | 2026-07-29 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 194.6 |
| fa7add0a-22fc-3b0c-b922-96435f45a1cc | -6.8708 | -46.0126 | 2026-07-29 02:40:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 70e8dae4-47d7-32d3-b4bd-c53a6d6dca1d | -7.36 | -45.8361 | 2026-07-29 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 205.6 |
| 7e21f898-b4e5-3477-b2ea-10af0a3ac720 | -7.3603 | -45.8136 | 2026-07-29 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| a84829f1-a972-3a0a-a6e0-19a953c639be | -7.341 | -45.8602 | 2026-07-29 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 6370034d-b571-3cc9-9fc7-c8746d301f17 | -10.9397 | -43.0593 | 2026-07-29 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 34ca4927-c9e3-3c42-bfac-da3bec09b725 | -10.9205 | -43.0622 | 2026-07-29 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 53d7ce1c-dae2-32c6-988c-6d7f616d36ef | -10.9205 | -43.0622 | 2026-07-29 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 62baf547-5e2a-3d13-9c0b-3035ea27ce7e | -7.36 | -45.8361 | 2026-07-29 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 178.6 |
| b8cb5f4b-9f98-344d-b1f0-acd7a5d97267 | -7.341 | -45.8602 | 2026-07-29 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 52cc9f1a-b6dc-30fd-8b97-db0cd0ad46cd | -7.3413 | -45.8377 | 2026-07-29 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 166.8 |
| 85a8940e-0329-301b-b2d6-888b8404dcb0 | -10.9397 | -43.0593 | 2026-07-29 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 6a65ebe7-acc3-39bc-b8be-1985909c63b5 | -7.3603 | -45.8136 | 2026-07-29 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 7712028c-1a42-38ee-919f-385df8804ce1 | -6.8708 | -46.0126 | 2026-07-29 02:50:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| d5464ef6-14e0-36f7-b101-b11a4a4e4ef6 | -10.9401 | -43.0355 | 2026-07-29 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 8cff8053-51f0-398f-bd6c-1a76b35ed62e | -7.341 | -45.8602 | 2026-07-29 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 876fa554-8d4d-3a03-98dd-22d94dc991c2 | -7.3413 | -45.8377 | 2026-07-29 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 178.2 |
| 788828c4-ccd7-3818-b625-327343762862 | -7.36 | -45.8361 | 2026-07-29 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 41c8dc37-abe3-372d-ba1d-c804dc74d593 | -6.8708 | -46.0126 | 2026-07-29 03:00:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| b1e3a894-f808-3c75-9ef2-e6c4c6dd77ba | -10.9397 | -43.0593 | 2026-07-29 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.6 |
| e93aa486-0b89-32f9-b304-f61504a84d8d | -6.8708 | -46.0126 | 2026-07-29 03:10:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 49.9 |
| af4fb6f7-7fc6-3d35-bf60-ce20a9ec6b4d | -13.1338 | -51.281 | 2026-07-29 03:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 66f39627-67b6-37b7-be3f-facceb89b3f2 | -7.3413 | -45.8377 | 2026-07-29 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 138.2 |
| df745be6-2aa6-35b3-ab56-3b3546546f13 | -13.1526 | -51.3 | 2026-07-29 03:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| dc78e108-11d6-3e04-971a-67e43b36f659 | -13.1334 | -51.3024 | 2026-07-29 03:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 7c366ac6-c4f7-3845-9ed7-2d7529961cb3 | -10.9205 | -43.0622 | 2026-07-29 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| dc0d7d65-49ae-35c1-94f1-de32e528bdde | -10.9397 | -43.0593 | 2026-07-29 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 7c37b820-cee1-3c8e-b3a7-f4011b841947 | -7.36 | -45.8361 | 2026-07-29 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 31569e9f-a50d-323e-8d0c-6ebfad0654f2 | -7.34 | -45.85 | 2026-07-29 03:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| becfec90-4955-381c-a0a2-59da156f4db9 | -7.3413 | -45.8377 | 2026-07-29 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 137.0 |
| b12727f3-e122-3cf6-a4a9-97c27eb1e7f9 | -13.153 | -51.2786 | 2026-07-29 03:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 39fe8a72-c9aa-3078-b557-719371c2b1cb | -10.9397 | -43.0593 | 2026-07-29 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| feca91b4-c458-3781-8257-4d057ef27827 | -7.341 | -45.8602 | 2026-07-29 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 31870457-2b40-3bd6-92f3-8e88f5e4ca75 | -13.1526 | -51.3 | 2026-07-29 03:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.8 |
| beed0f4d-9617-3524-b688-7d8445b36de9 | -13.1334 | -51.3024 | 2026-07-29 03:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| be6bb058-635b-3f0f-b0e3-8f744086e780 | -7.36 | -45.8361 | 2026-07-29 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 119.2 |
| a03b6761-c524-3162-bc9b-f8f243ee0e21 | -7.36 | -45.8361 | 2026-07-29 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| c4ba7ae7-b2a0-3ece-85db-d4e4d54b555c | -7.3413 | -45.8377 | 2026-07-29 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 949b37e3-4e37-3523-8a6e-d8daba2704a1 | -10.9397 | -43.0593 | 2026-07-29 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| d40087ce-9300-319c-a74a-87198e4d5037 | -5.83877 | -44.89716 | 2026-07-29 03:36:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README4.md)
