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
| ca530297-7b89-30f6-b7fd-2f47f79fdfdf | -11.2516 | -47.226 | 2025-09-30 01:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 7f036792-060e-3bd1-b441-df4d7d779713 | -12.8429 | -47.0063 | 2025-09-30 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| b02bb421-399c-3e30-9b13-490717c7137f | -15.8024 | -59.5235 | 2025-09-30 01:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 4da506a0-8c97-3bed-922e-2883c19ec8cc | -12.8433 | -46.9837 | 2025-09-30 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 646c5b94-66ee-34f8-a7a4-d319b23dc5db | -11.1548 | -54.1054 | 2025-09-30 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 2a5a5ce7-4efc-3bbf-9351-c24dff2616cd | -14.5327 | -48.4715 | 2025-09-30 01:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 0c320ce2-8509-332b-9997-f0336b0456db | -13.4005 | -48.0657 | 2025-09-30 01:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 75.5 |
| f128bb1d-b152-3a10-91b7-72c9b96a65c4 | -11.2326 | -47.2285 | 2025-09-30 01:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 254.4 |
| f1751738-9fe6-3e7a-b4f2-5f39ef453a06 | -11.1546 | -54.126 | 2025-09-30 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 206.9 |
| 343221e5-a968-377d-b95c-61ff98340553 | -15.8024 | -59.5235 | 2025-09-30 01:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 65992f1a-b327-3206-bf91-8c84f0828e60 | -11.7712 | -44.7432 | 2025-09-30 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| ddcd4438-671a-3759-bcc2-631d666629b7 | -12.8425 | -47.0289 | 2025-09-30 01:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| c490fd8f-d6d2-33cd-bf36-ee1574cc5036 | -14.5327 | -48.4715 | 2025-09-30 01:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 470b9d1d-98b2-3d1d-a13d-06f63db9923d | -10.1851 | -44.8939 | 2025-09-30 01:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 173.9 |
| 3d69535c-f882-34fc-9943-8a421e7753e2 | -14.5522 | -48.4684 | 2025-09-30 01:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 1f6dc740-5ae3-3f3a-8d7c-441325df8cd0 | -4.4013 | -44.0755 | 2025-09-30 01:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 87cdf172-5855-327c-a205-ce3abbf81738 | -13.4005 | -48.0657 | 2025-09-30 01:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| f093579c-5965-3ac6-bd20-dafe6d630973 | -12.8433 | -46.9837 | 2025-09-30 01:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 41048f3e-eccf-3aad-b65e-5e1e5c2a8eb1 | -11.7519 | -44.7461 | 2025-09-30 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| ccdcda3e-747c-3c3f-8303-82588999322a | -15.2658 | -49.7052 | 2025-09-30 01:50:00 | GOES-19 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 57.5 |
| d2ef83d7-00cf-3133-9ae3-405e99454f61 | -14.5752 | -48.2865 | 2025-09-30 01:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 343c3c14-47cd-3f44-a435-fcffc6bbec7d | -10.841 | -47.9644 | 2025-09-30 01:50:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 5280de65-b07f-3c19-95e7-2d339a5f355b | -10.1855 | -44.8709 | 2025-09-30 01:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 3ceed36d-8483-3c91-a2a7-f266ee295494 | -12.8429 | -47.0063 | 2025-09-30 01:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 204.0 |
| b05892e6-60b0-33b1-95f6-a63eeae99b2d | -10.2041 | -44.8915 | 2025-09-30 01:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 340453b0-881c-3a47-bf93-71f5a906ee3b | -14.5946 | -48.2834 | 2025-09-30 01:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 4279bb34-698e-38e2-bd07-d273bc56fcaf | -5.5241 | -43.8878 | 2025-09-30 01:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 274cf5db-d208-31c4-be3a-53cad1fb9b07 | -5.5243 | -43.8647 | 2025-09-30 01:50:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 2b5f9205-2c26-34f4-81a6-c98a5c254c71 | -4.4011 | -44.0985 | 2025-09-30 01:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 0ff8ada4-d04f-3f41-bc7d-2787f2e46117 | -11.1548 | -54.1054 | 2025-09-30 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 4988e7c2-94f3-35f1-95de-bca2e4dc4dac | -11.1735 | -54.1242 | 2025-09-30 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 0a2bd1c8-c99d-300b-a33b-785a1487c294 | -14.5327 | -48.4715 | 2025-09-30 02:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 82.4 |
| cf03365e-ebd3-3915-90ed-46402c222b9a | -11.1548 | -54.1054 | 2025-09-30 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 615f0e55-aaf2-374c-b9a3-64c4ef691fd9 | -14.6608 | -46.9435 | 2025-09-30 02:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 1f1d1177-c1be-30e1-a11d-de4fc704ca8e | -10.2041 | -44.8915 | 2025-09-30 02:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 98.0 |
| ba862321-5be3-3344-a616-0f9129f3790b | -14.5752 | -48.2865 | 2025-09-30 02:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 72100727-f73d-339d-8748-6399999e5d9c | -11.7712 | -44.7432 | 2025-09-30 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 888dd431-c023-3948-96e5-d6254b1a9baa | -10.1855 | -44.8709 | 2025-09-30 02:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| e49dd58e-7f4c-3436-932c-18ab7919722d | -10.1851 | -44.8939 | 2025-09-30 02:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 143.9 |
| e348dfb7-39c4-3ab1-829b-3b4c82aaff61 | -10.0717 | -50.2173 | 2025-09-30 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 63a65330-9da9-3c72-bdc3-11129ef7b570 | -14.6603 | -46.9663 | 2025-09-30 02:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 5a604d96-63b9-3eed-a9ee-7fec69d532fc | -13.4005 | -48.0657 | 2025-09-30 02:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 2d1aacc3-a82e-3ce0-8a6a-f4cd07b7ebaa | -13.2216 | -47.3322 | 2025-09-30 02:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 116.9 |
| cfc5b1c8-7c2f-3849-a45e-87448b53354f | -4.3826 | -44.0766 | 2025-09-30 02:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 93fb7261-91e0-3ad4-9693-4e7e73feb8fe | -12.8433 | -46.9837 | 2025-09-30 02:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 66e39db1-ee31-35bb-8d6a-195a1753d429 | -12.8429 | -47.0063 | 2025-09-30 02:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 145.6 |
| 310eaa89-a769-373f-bf6f-84187aa43f4f | -14.5323 | -48.4938 | 2025-09-30 02:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 3927a675-195a-327f-a56c-52e1e318884d | -5.5241 | -43.8878 | 2025-09-30 02:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 7878861c-ac16-3b81-b0ae-776f0496a911 | -11.1546 | -54.126 | 2025-09-30 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 211.4 |
| a10b9f73-0209-37bd-864a-25b01d6c4272 | -11.1735 | -54.1242 | 2025-09-30 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 854f175b-fba5-3ff3-a6e3-231e115d12b6 | -7.9191 | -44.6245 | 2025-09-30 02:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 5b0834bb-d155-3064-a65c-678b8cf26363 | -10.841 | -47.9644 | 2025-09-30 02:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 245f7b60-ff7f-38f3-86e7-7d69ddac1252 | -13.222 | -47.3097 | 2025-09-30 02:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 75e38013-25cb-35a9-8ad5-7fe03f2dbe57 | -5.5243 | -43.8647 | 2025-09-30 02:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 0557c6d6-decf-3c15-a81a-d0db5376dcca | -11.7519 | -44.7461 | 2025-09-30 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| f2bae14f-9b42-315e-aa39-73aa9e9054d8 | -4.4013 | -44.0755 | 2025-09-30 02:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 51b94a17-5fe5-3ccd-83d7-2c61b0016981 | -10.0717 | -50.2173 | 2025-09-30 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 72810a72-15cb-3f74-8a4b-db2e3f79012d | -17.7356 | -46.6356 | 2025-09-30 02:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 48.8 |
| c55252bb-5759-373d-9b23-385571b56d3f | -12.8429 | -47.0063 | 2025-09-30 02:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 3189eacc-2e81-3d6e-9a1e-e8f93200e5f2 | -10.0906 | -50.2154 | 2025-09-30 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| db05cd91-9b70-3fd8-afd4-00d47b4a9000 | -4.4013 | -44.0755 | 2025-09-30 02:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 353851de-b84d-34d0-8fc0-9584e5196f38 | -3.1013 | -47.0082 | 2025-09-30 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 3fdc158f-50f5-3850-b369-6e28c413aad7 | -12.8433 | -46.9837 | 2025-09-30 02:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| a99f1b34-f7dc-33d2-adae-01a390b38fce | -13.4005 | -48.0657 | 2025-09-30 02:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 886d14b3-b63d-39f8-8884-80dc14d4e35c | -14.6408 | -46.9696 | 2025-09-30 02:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 74b06e50-6415-3e45-b2ad-ff7ce845fe81 | -11.1548 | -54.1054 | 2025-09-30 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 40d3d45d-5f9d-3ab0-a2c7-039568c67afe | -14.5323 | -48.4938 | 2025-09-30 02:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 3799f159-728a-3151-8000-47e2bef1fc93 | -5.5241 | -43.8878 | 2025-09-30 02:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 701ae8f2-c0ec-38a7-bf10-38807475075a | -7.9191 | -44.6245 | 2025-09-30 02:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| e2aef72a-1030-3e36-93c7-663ace1068f1 | -11.1546 | -54.126 | 2025-09-30 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 214.9 |
| 55ae69f8-145f-3c4f-80da-0b97ece9bcc3 | -10.2041 | -44.8915 | 2025-09-30 02:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 59b95500-e1df-38db-9638-78b4a6a1bd38 | -5.5243 | -43.8647 | 2025-09-30 02:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 41ec67f9-a8be-32f3-8836-a9bd04323bea | -14.6603 | -46.9663 | 2025-09-30 02:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 208.3 |
| d5e60e3a-6c5e-31e0-8472-98ee3d226cc8 | -14.5327 | -48.4715 | 2025-09-30 02:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 84.2 |
| b1fff85b-795a-3a4d-b1cc-d4f886feb67e | -17.7155 | -46.6398 | 2025-09-30 02:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 58.0 |
| e1dca354-42e2-3edc-9bb7-9fd42cd30ee6 | -14.6608 | -46.9435 | 2025-09-30 02:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 9e7db4b2-8195-32b4-b270-08f4aba6fd98 | -10.1855 | -44.8709 | 2025-09-30 02:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| a980e213-df9d-3b60-8b02-4bffb1dacdcd | -11.7519 | -44.7461 | 2025-09-30 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 98023dae-95ae-3745-93ba-fe70b0e9fc60 | -11.1735 | -54.1242 | 2025-09-30 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| e25269a2-974c-3a2d-bc25-70337da5cdef | -10.1851 | -44.8939 | 2025-09-30 02:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 169.2 |
| 15cccb7c-f4b1-375c-b4aa-85392229d7d4 | -14.5522 | -48.4684 | 2025-09-30 02:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 43ac55ab-71f9-35ee-94c9-c5677d47d00c | -14.2778 | -52.9601 | 2025-09-30 02:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| dc7a8000-a75f-3433-b55e-d0c37b3d86b0 | -4.4013 | -44.0755 | 2025-09-30 02:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| d62a117c-2702-3b92-bdbe-2040a6d9eb78 | -12.8429 | -47.0063 | 2025-09-30 02:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| df9fc904-ba2e-37f2-86e7-9168b6b01bfe | -14.5522 | -48.4684 | 2025-09-30 02:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 74.7 |
| f5905415-3dbe-39fb-bca5-911cfdd9077b | -14.2782 | -52.9391 | 2025-09-30 02:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 14c849f9-da8e-3fb9-9487-3e50f516cbe1 | -3.1013 | -47.0082 | 2025-09-30 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| c71b5152-4f65-3911-91d7-b57e020e1efd | -14.5137 | -48.4522 | 2025-09-30 02:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 4946e7aa-dee3-314f-98d8-05c11406ff14 | -17.7155 | -46.6398 | 2025-09-30 02:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 93.1 |
| bb78bcf6-3595-3bbd-927d-1d6b88b47502 | -5.5243 | -43.8647 | 2025-09-30 02:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 684f28ba-1189-3dc4-bf74-0bb133262b68 | -10.2041 | -44.8915 | 2025-09-30 02:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 137.6 |
| f80b8989-7805-306e-a27f-11613b0c751d | -11.2516 | -47.226 | 2025-09-30 02:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 568ecedc-1042-334f-ac8d-9698ee1e9c22 | -14.5327 | -48.4715 | 2025-09-30 02:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 43eb9d05-1d19-37d5-b000-f07211daed90 | -14.6608 | -46.9435 | 2025-09-30 02:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 82829182-3aff-324c-95e7-9898c9a2976d | -7.9191 | -44.6245 | 2025-09-30 02:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 89d2c0e2-cc25-3f4b-8b98-c2e461df4dfc | -5.5241 | -43.8878 | 2025-09-30 02:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 2dab6439-6a93-3df8-9ec6-c6f174c87a08 | -14.6798 | -46.963 | 2025-09-30 02:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 3197eaea-5653-3047-8115-e3909e9bdcfe | -14.5517 | -48.4907 | 2025-09-30 02:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 4bde4cf8-874a-33b7-b8fc-d60f8a01db0c | -11.1546 | -54.126 | 2025-09-30 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 197.9 |
| ea50377d-0fac-3e14-a7be-3e01b5601128 | -14.5323 | -48.4938 | 2025-09-30 02:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 85.2 |


[Clique aqui para ver as próximas entradas](README14.md)
