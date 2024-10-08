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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8addabc2-f95d-385f-8e99-61474d698aa9 | -4.63379 | -50.98111 | 2024-10-08 05:31:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 0f768af3-5337-337a-a605-b9f3dfc5a893 | -12.47265 | -47.31144 | 2024-10-08 05:31:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0bef989f-dda5-3139-92ef-3c576bdb6147 | -12.36126 | -47.08976 | 2024-10-08 05:31:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 4c714031-d9c3-3a0d-bc24-051947a29300 | -12.28546 | -47.6402 | 2024-10-08 05:31:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 28be78f7-e66a-3c42-8515-985bd0a6907f | -12.1665 | -47.75993 | 2024-10-08 05:31:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| afd16e7f-0c64-3775-8fb8-b3f1ae4a203f | -11.32712 | -51.3416 | 2024-10-08 05:31:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f164df80-b5cc-3958-b0e2-af4b092caf7a | -11.31424 | -51.06512 | 2024-10-08 05:31:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c55c81f2-b6c4-31f4-a0c3-2a51415ee60f | -11.3053 | -51.06373 | 2024-10-08 05:31:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 38a47c91-8b24-3822-9b4f-aaf23488285a | -11.30389 | -51.07291 | 2024-10-08 05:31:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3e9f8883-39e4-3726-bf86-1b3c0399b804 | -11.20434 | -51.36358 | 2024-10-08 05:31:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5a376586-92e0-3a66-8eed-4855c13c7826 | -10.63754 | -55.89683 | 2024-10-08 05:31:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 940d2d21-49ed-3c66-8c2e-aef3003b6bd1 | -10.63452 | -55.91468 | 2024-10-08 05:31:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 7730152d-e3f5-3db6-9631-bbc2abb0f4e2 | -7.86932 | -45.35484 | 2024-10-08 05:31:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 20.6 |
| d5e84b29-bac0-36ad-9e28-9f2670455ad2 | -7.86525 | -45.3476 | 2024-10-08 05:31:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| cb1a3f90-3d68-3ef3-a072-c9a61d316eb2 | -7.86341 | -45.36058 | 2024-10-08 05:31:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 695477b5-68b0-329d-9aeb-6f9090b62c2d | -7.85466 | -45.34615 | 2024-10-08 05:31:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 01f2de88-779e-3db9-9c2f-8428d15a5ad6 | -7.85283 | -45.35913 | 2024-10-08 05:31:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| cd959ff1-e485-30fc-b495-6f0afcecd4e7 | -7.77525 | -43.092 | 2024-10-08 05:31:00 | AQUA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 3de242b6-fe82-3f27-a493-91ac130184a7 | -6.32034 | -43.37232 | 2024-10-08 05:31:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 22e7612f-91d6-3517-9ae9-de5efea4572d | -8.7571 | -49.78051 | 2024-10-08 05:31:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| fa489dd8-140c-3178-a3ec-466e73e50581 | -8.6108 | -48.8471 | 2024-10-08 05:31:00 | AQUA_M-M | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0c503647-03e4-3ee1-aa8d-6188451903ca | -8.16882 | -49.45842 | 2024-10-08 05:31:00 | AQUA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 3c821011-2de9-30be-903a-8b4c53e7030b | -8.1675 | -49.46729 | 2024-10-08 05:31:00 | AQUA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 004bb84c-072b-34e2-a69f-e12280ee213f | -7.90025 | -47.71975 | 2024-10-08 05:31:00 | AQUA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ae7635df-fb70-38fe-bfa2-4cf29d29b9f8 | -7.28085 | -44.95845 | 2024-10-08 05:31:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7456327d-7c59-3bf8-8fee-0ced5137bc86 | -7.279 | -44.97213 | 2024-10-08 05:31:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 94f8477d-adef-3f9f-82a4-d1f919f19f89 | -7.27544 | -44.96628 | 2024-10-08 05:31:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 695467d7-7712-3f25-ac5b-377ab9179b71 | -6.67026 | -47.11064 | 2024-10-08 05:31:00 | AQUA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 60e11a8c-605f-3277-be86-9e663c378d44 | -6.45335 | -49.87474 | 2024-10-08 05:31:00 | AQUA_M-M | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 69449dbd-0e9d-3810-b641-03982bd6baef | -5.85639 | -44.86623 | 2024-10-08 05:31:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| adbe567c-8837-3a3d-9628-637f8e4bfd11 | -5.82193 | -44.12591 | 2024-10-08 05:31:00 | AQUA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 90777751-8f5e-39fd-9c1b-770cd8e7a64a | -5.58051 | -44.86303 | 2024-10-08 05:31:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5bc0d199-350d-37b2-b2de-2cc934895858 | -5.57868 | -44.876 | 2024-10-08 05:31:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 192bcbfc-34e6-3b0c-9380-32f4d49af624 | -5.57688 | -44.88878 | 2024-10-08 05:31:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 1b3c2ff6-02e5-37af-9fca-fd9a79a07b6d | -5.56812 | -44.87436 | 2024-10-08 05:31:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| d5f062a2-e102-3ac7-a589-5f5566027e2f | -5.4821 | -44.25394 | 2024-10-08 05:31:00 | AQUA_M-M | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| bb5646be-7e7c-3564-ae8a-c7167b2c7769 | -5.00992 | -49.589 | 2024-10-08 05:31:00 | AQUA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b6d7bd46-9ced-3cd9-a1c1-995e72d7296e | -17.81313 | -53.75252 | 2024-10-08 05:33:00 | AQUA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fce76539-d68a-3aa1-8d3f-165ddd1100da | -17.76944 | -53.80321 | 2024-10-08 05:33:00 | AQUA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 24.7 |
| d0ebe3dd-f86a-34e1-ae9e-6eba52503621 | -17.76776 | -53.81378 | 2024-10-08 05:33:00 | AQUA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 06d60e1b-ee25-3b64-b4ad-df5d4bcc0b20 | -17.16531 | -56.74724 | 2024-10-08 05:33:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.8 |
| 7ae0632d-268e-37c6-bbe3-04654561a31f | -17.16354 | -53.94205 | 2024-10-08 05:33:00 | AQUA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a3bd219f-edfe-3453-8964-e81c89ee8603 | -17.14247 | -56.80977 | 2024-10-08 05:33:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.7 |
| 7bed2743-0c26-30a0-8a4f-eea81d83d1f2 | -17.1396 | -56.82606 | 2024-10-08 05:33:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.1 |
| 73489ef3-45e8-3d30-baa4-e445fc141ab8 | -17.12518 | -56.84016 | 2024-10-08 05:33:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.6 |
| b773972c-7330-390e-a5fb-8fdb5ea018ae | -17.10208 | -56.83576 | 2024-10-08 05:33:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.5 |
| 3ff9444f-7c80-37c4-a2e7-8c9da36d4e11 | -17.09351 | -56.82858 | 2024-10-08 05:33:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.5 |
| a85b72d1-0ce5-36e6-8ae2-f4ff55bf9c8b | -17.09068 | -56.84498 | 2024-10-08 05:33:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.5 |
| 82fcf7cb-673f-3428-bc99-2cab30babe41 | -17.09053 | -56.83355 | 2024-10-08 05:33:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 43.5 |
| da90fce9-7c91-3da5-9a95-b1155e44a57c | -17.01695 | -56.67322 | 2024-10-08 05:33:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.0 |
| 36bb405b-6db9-3355-ba9a-bb37f70ff0e0 | -17.01576 | -56.66352 | 2024-10-08 05:33:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 4561c024-9e35-3039-96dc-4098bf0dace0 | -17.0129 | -56.67945 | 2024-10-08 05:33:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.1 |
| be3e08ac-04e0-33d6-9557-855b6dd26b12 | -17.00552 | -56.67105 | 2024-10-08 05:33:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 32.4 |
| d126b8a1-13b6-3cc9-b4ab-9572dea2aac5 | -17.00274 | -56.68703 | 2024-10-08 05:33:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.4 |
| d8b2c600-5796-3533-8d79-6d6ae893e760 | -16.99378 | -56.60311 | 2024-10-08 05:33:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 62a05a3f-90bf-3d94-8348-5ce3deb64d8c | -16.99102 | -56.61894 | 2024-10-08 05:33:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 0921e9b2-f429-302a-a6d8-9c5d494784d3 | -16.97006 | -56.13714 | 2024-10-08 05:33:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 2b28e5b7-69b8-3d76-a806-eb3163297f4d | -16.93028 | -57.47823 | 2024-10-08 05:33:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 130.2 |
| 8c46c70f-ed7b-3d1b-8ca9-ef47405804db | -16.83429 | -57.43334 | 2024-10-08 05:33:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.7 |
| d7589bb5-eb92-3ab4-8d57-9f4f1f92165c | -16.8133 | -57.41037 | 2024-10-08 05:33:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.3 |
| e074be3f-731a-3e68-afef-104aafe865ad | -16.80998 | -57.42862 | 2024-10-08 05:33:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.7 |
| d4728a10-ce98-31d7-902e-76fc4bdcb6cc | -16.80569 | -57.42253 | 2024-10-08 05:33:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.0 |
| fa60e5fc-0799-320f-8c96-79dd28945033 | -16.80117 | -57.40802 | 2024-10-08 05:33:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 1bf02179-d274-3056-aab6-f08a3faabf4c | -16.79782 | -57.42627 | 2024-10-08 05:33:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 36.6 |
| 62049640-9178-31a3-ab58-633187eb9d60 | -16.69378 | -57.11648 | 2024-10-08 05:33:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.1 |
| 36509bea-37e4-3e01-afcf-fd48dfc7972e | -16.68503 | -57.0968 | 2024-10-08 05:33:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.7 |
| 3a5e9042-e10c-3f92-96c1-a535b7ff9761 | -16.68188 | -57.11422 | 2024-10-08 05:33:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 46.9 |
| 09fabd0e-446e-37b8-8565-3ae2035d656c | -16.67877 | -57.09012 | 2024-10-08 05:33:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.8 |
| 507c5237-fe7e-35b4-b8c4-0ccd96160ccb | -16.67874 | -57.13166 | 2024-10-08 05:33:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 40.0 |
| a4ca6913-9ca5-3645-9a22-5dd5cd463bcf | -16.67575 | -57.10755 | 2024-10-08 05:33:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 193.5 |
| cce19cb5-c14d-3050-a565-7ad8435294eb | -16.67314 | -57.09455 | 2024-10-08 05:33:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 136.8 |
| 31ca5f7d-44aa-3466-8703-c636a7ec3824 | -16.67272 | -57.12503 | 2024-10-08 05:33:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.9 |
| 368820f3-48dd-3619-b7ae-1fc08abf75d0 | -16.66999 | -57.11195 | 2024-10-08 05:33:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 144.0 |
| 1a339af9-0823-36ba-881c-ed27e333dde4 | -16.66968 | -57.14256 | 2024-10-08 05:33:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 40.1 |
| 9066ed20-96d8-3f10-83b1-b616cbc8e159 | -16.66689 | -57.08784 | 2024-10-08 05:33:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.7 |
| 8125b929-3922-3536-a348-7d2f6cf677b0 | -16.66682 | -57.12939 | 2024-10-08 05:33:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 177.5 |
| 9f855ecd-9cf9-34e8-b13a-9a41a23d1e6a | -16.66385 | -57.10527 | 2024-10-08 05:33:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.1 |
| 5c399331-f5b8-3fb1-baa3-470c530f50f7 | -16.66364 | -57.1469 | 2024-10-08 05:33:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.7 |
| aaa3f0c5-3846-3d02-b4e7-e884c63a83a4 | -16.6608 | -57.12274 | 2024-10-08 05:33:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.2 |
| 9f59f38a-4a15-3267-95bb-33562a4a61b3 | -16.65775 | -57.14027 | 2024-10-08 05:33:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.6 |
| 53e4a9bb-ee2a-378c-828b-51db21f8b3a9 | -16.6549 | -57.12712 | 2024-10-08 05:33:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 33.3 |
| 15fce509-f301-3ccb-a812-115584eff8df | -16.59733 | -55.89343 | 2024-10-08 05:33:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 6b8b2f64-4804-3f12-8998-8deb960d9e99 | -16.57239 | -55.89683 | 2024-10-08 05:33:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.3 |
| efc4d22d-d689-3ff7-87a6-29a376ca2eec | -16.47306 | -53.91068 | 2024-10-08 05:33:00 | AQUA_M-M | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| dad89b25-6fec-38e3-a835-dbbed5312dfc | -16.46934 | -53.90466 | 2024-10-08 05:33:00 | AQUA_M-M | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3fb4c607-4f7e-3adf-a503-045834029eee | -16.4676 | -53.91554 | 2024-10-08 05:33:00 | AQUA_M-M | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1f0e299b-d28c-32c4-9b05-8915c893a274 | -16.44114 | -57.25126 | 2024-10-08 05:33:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.8 |
| 95eba7b6-0215-3bc3-a172-73aeb5ab044c | -16.42682 | -55.93839 | 2024-10-08 05:33:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 38.9 |
| a0413ac0-2934-39c3-9ce1-acf51836fd97 | -16.42429 | -55.95288 | 2024-10-08 05:33:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 30.3 |
| 0fb3e464-4e93-3b15-9d3a-26edbe1af41e | -16.16285 | -55.93032 | 2024-10-08 05:33:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 43ec93b8-8c77-3731-b0f9-42ba1cd080f5 | -16.09951 | -57.54894 | 2024-10-08 05:33:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 173c27b1-fcab-3917-b573-9f02e1a9bb13 | -15.87992 | -57.45591 | 2024-10-08 05:33:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 5597342c-8d7f-31bb-be8d-1ee6c09bedb3 | -15.87659 | -57.47425 | 2024-10-08 05:33:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 008a7639-fa56-30bb-ace8-67439c12bf75 | -14.81614 | -53.92266 | 2024-10-08 05:33:00 | AQUA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 51bd4dcf-472e-33f1-86f2-57af799bbe3e | -12.66131 | -54.70997 | 2024-10-08 05:33:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f1c13aab-330e-3d01-802f-329142bd8ed2 | -12.63677 | -53.10957 | 2024-10-08 05:33:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| af082b0d-481b-3829-84a0-ae916c41f1d5 | -12.63502 | -53.12034 | 2024-10-08 05:33:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0a309524-b960-329d-85da-25a60ba9d7b5 | -12.60285 | -53.11927 | 2024-10-08 05:33:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5be66687-0e11-3e00-8abc-d86447e1e7e3 | -12.60114 | -53.13008 | 2024-10-08 05:33:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 72a96bf0-76e2-384f-b3de-b98ce67fd94d | -12.58085 | -53.0714 | 2024-10-08 05:33:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 24.3 |


[Clique aqui para ver as próximas entradas](README130.md)
