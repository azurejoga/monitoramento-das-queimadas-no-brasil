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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32386dac-ad19-302c-8303-c40e0b5f0440 | -19.6167 | -57.2317 | 2026-01-25 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.2 |
| 1507318d-51f0-3c21-b6a1-5eba3af7612f | -5.5682 | -39.1182 | 2026-01-25 00:00:00 | GOES-19 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 135.8 |
| ee08c809-896c-3976-9b3e-c13ff64ba03d | -19.6364 | -57.2499 | 2026-01-25 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 267.0 |
| 0b8bf4ea-1177-3780-a8d3-ca5cfe616d91 | -19.6368 | -57.229 | 2026-01-25 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 281.2 |
| 2caa7795-9321-359f-adab-6c85ed076c3a | -19.6565 | -57.2472 | 2026-01-25 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 123.9 |
| 5d3b2936-4963-3c6a-8559-ea9c5adf955b | -19.6569 | -57.2263 | 2026-01-25 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 153.4 |
| 2a4e7afb-8019-3d92-854b-d9e78b9d9e54 | -19.6163 | -57.2526 | 2026-01-25 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.9 |
| 15a03293-f939-356d-9912-cc1e716349d6 | -23.46642 | -48.90183 | 2026-01-25 00:05:00 | TERRA_M-M | PARANAPANEMA | SÃO PAULO | Brasil | 3535804 | 35 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 2d53b74b-8daf-3b7e-850c-c27a82502344 | -23.46566 | -48.90748 | 2026-01-25 00:05:00 | TERRA_M-M | PARANAPANEMA | SÃO PAULO | Brasil | 3535804 | 35 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 8eaa1d1d-c7db-3b47-bbe5-00098f1d7561 | -5.5458 | -39.0284 | 2026-01-25 00:06:00 | METOP-B | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 39d50f7e-bd9a-325a-a1c2-60c960212205 | -5.5513 | -39.050301 | 2026-01-25 00:06:00 | METOP-B | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 5abee6b2-c875-3beb-a543-72f4a0a33f71 | -5.5567 | -39.072201 | 2026-01-25 00:06:00 | METOP-B | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d805b49d-7764-300b-acb0-4e8dce0f26bb | -5.547 | -39.0746 | 2026-01-25 00:06:00 | METOP-B | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 750a8674-c71f-3559-b686-42535f17819c | -5.5416 | -39.0527 | 2026-01-25 00:06:00 | METOP-B | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| a5fa7e70-e1d1-3310-bf7c-108a9f47db53 | -18.82183 | -51.61925 | 2026-01-25 00:07:00 | TERRA_M-M | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 24.1 |
| b8908972-a4df-3d33-aac0-e0d8a4dd8fb6 | -21.07427 | -49.52641 | 2026-01-25 00:07:00 | TERRA_M-M | NOVA ALIANÇA | SÃO PAULO | Brasil | 3532801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.0 |
| 048d4567-394a-3ad1-96ac-c46cef8b73e9 | -18.80458 | -51.59378 | 2026-01-25 00:07:00 | TERRA_M-M | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 12d372bf-a9da-323e-8b15-581d5f7eec4f | -21.07477 | -49.533 | 2026-01-25 00:07:00 | TERRA_M-M | NOVA ALIANÇA | SÃO PAULO | Brasil | 3532801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 36.7 |
| e8fadbf3-2bc7-3662-959c-8016e64e9da8 | -18.80877 | -51.61558 | 2026-01-25 00:07:00 | TERRA_M-M | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 861ce21a-e9cd-39e1-9c4c-bece65ba9547 | -18.81913 | -51.59208 | 2026-01-25 00:07:00 | TERRA_M-M | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 48e541fc-4560-366a-8e63-37e3fdbce6c2 | -18.80726 | -51.62112 | 2026-01-25 00:07:00 | TERRA_M-M | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 75152868-ddf0-36f0-8385-1fc5311d28d7 | -15.83984 | -41.43591 | 2026-01-25 00:07:00 | TERRA_M-M | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 55.1 |
| ad691d98-97ac-35d5-a1f1-bca3b1ddba22 | -15.84144 | -41.44645 | 2026-01-25 00:07:00 | TERRA_M-M | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 41.4 |
| f91d6fd2-80cc-328e-9421-184007ebcb68 | -6.20034 | -39.28364 | 2026-01-25 00:09:00 | TERRA_M-M | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 27.1 |
| bca7d002-ffcd-336d-8083-fc7cdd420ec0 | -6.20308 | -39.2888 | 2026-01-25 00:09:00 | TERRA_M-M | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 11837be0-1d3d-388e-8af3-c8b3e0b862e1 | -5.36029 | -40.60264 | 2026-01-25 00:09:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 4b3a7bcd-a8b7-3608-83c0-7c1cfeeca4a2 | -5.57568 | -39.13787 | 2026-01-25 00:09:00 | TERRA_M-M | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 27.6 |
| ffc0b7d6-bdcb-359e-b7f3-d8475d547914 | -10.07422 | -36.20448 | 2026-01-25 00:09:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.7 |
| 69b2f0e8-8b3c-3f36-a96b-5a42299f5e0d | -6.05964 | -43.74294 | 2026-01-25 00:09:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 2f4971cd-e338-3a49-a9d2-68b60959eb20 | -6.05819 | -43.7328 | 2026-01-25 00:09:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 8afcecfd-9334-3389-9182-b7696850b492 | -4.91296 | -43.46152 | 2026-01-25 00:09:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ec1e75ee-2778-3664-a64c-cee461652f75 | -4.65686 | -37.92009 | 2026-01-25 00:09:00 | TERRA_M-M | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 25.3 |
| 2aceda63-8751-36a0-95f3-22add242a502 | -5.5589 | -39.11783 | 2026-01-25 00:09:00 | TERRA_M-M | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 24.5 |
| 015f9c60-60af-3c4e-808d-7b96323aaef6 | -5.57232 | -39.11576 | 2026-01-25 00:09:00 | TERRA_M-M | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 122.4 |
| 68a79b60-bcf6-3d21-b866-52c0fcf12a51 | -13.43219 | -41.32494 | 2026-01-25 00:09:00 | TERRA_M-M | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 620d8d3f-3667-3f70-a3c1-2c8dfb5d4baf | -19.6565 | -57.2472 | 2026-01-25 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.6 |
| 4c9d4838-8492-32c4-9e36-cac7da119b54 | -19.6368 | -57.229 | 2026-01-25 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 295.5 |
| ee657d0e-8d5b-340c-83bd-f5fa81c0eb79 | -5.5682 | -39.1182 | 2026-01-25 00:10:00 | GOES-19 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 130.4 |
| e257974f-45e7-39e6-bb42-37c6b692138e | -19.6163 | -57.2526 | 2026-01-25 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.2 |
| 54766b1d-3493-36a9-8c6a-306e4bf9bebc | -10.086 | -36.2053 | 2026-01-25 00:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 78.0 |
| b5862cf6-847b-3eca-8179-9e3a60a7edb3 | -19.6569 | -57.2263 | 2026-01-25 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 150.9 |
| b9482666-e92c-3e64-866c-2db794e2927f | -15.8489 | -41.4246 | 2026-01-25 00:10:00 | GOES-19 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 66.4 |
| d81e869d-2976-33ff-93a9-2365699bb0df | -10.0667 | -36.2088 | 2026-01-25 00:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 184.4 |
| 46ea7152-489c-3c82-94aa-b709d544d16f | -19.6167 | -57.2317 | 2026-01-25 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.2 |
| cbb0712f-dd30-304e-a796-0dddbd8dedba | -19.6364 | -57.2499 | 2026-01-25 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 269.5 |
| f0b8e601-76d1-3199-a750-63d49395445d | -3.07102 | -40.10591 | 2026-01-25 00:11:00 | TERRA_M-M | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 99fd4e6c-3bad-3c6a-b5b5-9f5063daef57 | -19.6163 | -57.2526 | 2026-01-25 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.5 |
| b8fcfc6e-f08b-3d2f-81e4-e73a30fa68d5 | -15.8489 | -41.4246 | 2026-01-25 00:20:00 | GOES-19 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.5 |
| df45686d-4603-39f8-b118-c13df4060f6a | -19.6167 | -57.2317 | 2026-01-25 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.6 |
| fb7f633f-5e8b-3636-a396-1d6413a26f93 | -10.0662 | -36.2359 | 2026-01-25 00:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 82.6 |
| a8be3c4b-ae5a-35da-8291-353e374b6e1d | -19.6364 | -57.2499 | 2026-01-25 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 211.1 |
| e37a2ee2-9f34-31fa-9057-dd417d8b21af | -10.0667 | -36.2088 | 2026-01-25 00:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 175.8 |
| c1c70aaa-b1d0-329f-a10a-b77c02102321 | -18.8124 | -51.5914 | 2026-01-25 00:20:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 69.7 |
| bb60da37-89b8-36aa-bd5c-f6a451e029f6 | -19.6565 | -57.2472 | 2026-01-25 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.6 |
| 57d0f58a-c893-3c07-8de6-983ca40e45a9 | -19.6569 | -57.2263 | 2026-01-25 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.1 |
| c38f411d-c62d-35ba-8261-c0331068b54a | -5.5682 | -39.1182 | 2026-01-25 00:20:00 | GOES-19 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 109.2 |
| da7bc2e5-4d13-3f7c-9483-28e5399de718 | -19.6368 | -57.229 | 2026-01-25 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 248.0 |
| d9505f31-ff17-3db3-ad20-d85640560814 | -19.6368 | -57.229 | 2026-01-25 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 199.9 |
| 475f165b-fd30-34d1-ac56-27bbc55198c5 | -15.8489 | -41.4246 | 2026-01-25 00:30:00 | GOES-19 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 59.8 |
| a74f848e-2e22-370d-b216-ac15c92a5b50 | -19.6364 | -57.2499 | 2026-01-25 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 203.1 |
| b003a9a7-690c-336c-8389-27cfadde89a2 | -5.5682 | -39.1182 | 2026-01-25 00:30:00 | GOES-19 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 97.1 |
| 72bd7d9b-5a54-34cd-97cb-5fdbc1607c53 | -5.5682 | -39.1182 | 2026-01-25 00:40:00 | GOES-19 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 96.6 |
| 69bf821f-ef49-359c-952e-e861b52e67b3 | -19.6163 | -57.2526 | 2026-01-25 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.2 |
| 30f73264-f0d1-3d45-a78e-1500dd143887 | -19.6364 | -57.2499 | 2026-01-25 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 207.4 |
| 40e0a268-e82d-346a-a6e5-2a8fee49ef76 | -19.6167 | -57.2317 | 2026-01-25 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.7 |
| cc3fc685-3b8d-343d-a75c-0da0b9aefa59 | -19.6368 | -57.229 | 2026-01-25 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 181.9 |
| f7371fda-debb-3294-a4f4-8f9f0cce9777 | -19.6368 | -57.229 | 2026-01-25 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 168.4 |
| 4f25d5d5-6625-3f53-a713-9e6c4373af85 | -19.6167 | -57.2317 | 2026-01-25 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.2 |
| 89c59fe5-33cf-362d-9b9b-0d3e7d46c2e7 | -19.6163 | -57.2526 | 2026-01-25 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.5 |
| 3f990766-ccc5-3596-8bb4-c530bac31547 | -19.6364 | -57.2499 | 2026-01-25 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 222.6 |
| 3e215d01-633f-3eee-953e-6beccdc92cc7 | -5.5682 | -39.1182 | 2026-01-25 00:50:00 | GOES-19 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 81.3 |
| 50196264-4d5a-3d4d-bf5d-90a5768bb247 | -3.0791 | -40.1063 | 2026-01-25 00:50:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 71.4 |
| 3996f1ce-9092-3b46-aa13-0e08ba5b0f5c | -5.5682 | -39.1182 | 2026-01-25 01:00:00 | GOES-19 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 56.8 |
| 79f1719f-0e48-31fd-b295-067137396bb0 | -19.6368 | -57.229 | 2026-01-25 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 131.8 |
| 9211a580-9eb8-31f6-b4ca-9ae173d993ac | -19.6364 | -57.2499 | 2026-01-25 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 234.8 |
| 0c58fae5-5924-313d-a3a8-6c820f267539 | -19.636 | -57.2708 | 2026-01-25 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.1 |
| 678b2338-6feb-3f09-8eea-c021d718f5ad | -19.6163 | -57.2526 | 2026-01-25 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.2 |
| 98bbac30-a928-3c31-bb7a-53e05561eaa7 | -3.0791 | -40.1063 | 2026-01-25 01:00:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 76.5 |
| 13e79f27-1e16-3061-8b5b-e5d7391c0950 | -3.0791 | -40.1063 | 2026-01-25 01:10:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 98.3 |
| e372b4bf-1340-3e61-9042-ad658b8eb82e | -19.6163 | -57.2526 | 2026-01-25 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.4 |
| 940bab0d-0ad0-356d-8db6-c443473c9749 | -19.6364 | -57.2499 | 2026-01-25 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 192.8 |
| 4d716c6b-243f-3d43-a8d9-3133c33fb92c | -19.6368 | -57.229 | 2026-01-25 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.5 |
| b2d781ac-ee30-3981-8f6e-46c7c3ad3abb | -19.6368 | -57.229 | 2026-01-25 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.6 |
| 06fc3e72-a358-3e64-8f21-7bead6376a5d | -19.6163 | -57.2526 | 2026-01-25 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.2 |
| 1b7ba193-3177-3216-97df-adb6cd457060 | -19.6364 | -57.2499 | 2026-01-25 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 158.6 |
| e570ab5a-6121-34cc-ba57-dfa0a29fb49e | -3.0791 | -40.1063 | 2026-01-25 01:20:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 68.2 |
| 44179edc-5387-3649-948a-417e9466f9dd | -19.6368 | -57.229 | 2026-01-25 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.8 |
| 7524b7b6-84f0-3dae-bcb2-124ef4a23d1a | -19.636 | -57.2708 | 2026-01-25 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.1 |
| 0b375334-876e-3dfa-95a8-5322c80765ea | -19.6163 | -57.2526 | 2026-01-25 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.4 |
| bd8d67db-9826-3b0c-b1dc-6e6e75ee5e20 | -3.0791 | -40.1063 | 2026-01-25 01:30:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 76.9 |
| 42b65f03-6b4d-3768-b960-861c81e63512 | -19.6364 | -57.2499 | 2026-01-25 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 166.1 |
| ee37d98e-e9fb-313a-9474-fc5af3903e41 | -3.0791 | -40.1063 | 2026-01-25 01:40:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 77.4 |
| df4edea2-8ee6-3b09-8052-51060df6cda8 | -19.6163 | -57.2526 | 2026-01-25 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.2 |
| dd7e45ed-bfea-353e-818a-fc54f4501f1e | -19.6368 | -57.229 | 2026-01-25 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.9 |
| 30f54e79-fa9b-330b-9e2f-4659cc0ddf66 | -19.6565 | -57.2472 | 2026-01-25 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.8 |
| 43bb732d-b353-3317-b410-e52345469bf7 | -19.636 | -57.2708 | 2026-01-25 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.6 |
| f3a35d05-fe4b-3d24-b348-ad4d8a6d250a | -10.1974 | -36.4278 | 2026-01-25 01:40:00 | GOES-19 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 67.1 |
| f6291cc6-27af-3595-bda1-42ab67851acb | -19.6364 | -57.2499 | 2026-01-25 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 184.7 |
| 99d223f1-af3e-3beb-935c-d15246a0a6e7 | -19.63026 | -57.27606 | 2026-01-25 01:45:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 170.6 |
| 2964968d-ccff-3d84-8f7b-da2d67c28aeb | -19.62227 | -57.23728 | 2026-01-25 01:45:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 203.6 |


[Clique aqui para ver as próximas entradas](README2.md)
