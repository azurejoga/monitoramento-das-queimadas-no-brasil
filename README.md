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
| d4c29286-bf05-3cfe-bbe9-d6fe7d305498 | -7.2597 | -43.0645 | 2026-01-21 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.2 |
| 2330db74-d186-3273-8539-a367bc329924 | -20.3279 | -57.906 | 2026-01-21 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.5 |
| e3bbf120-bb4c-3072-a0c2-ab687af0e537 | -20.3481 | -57.9033 | 2026-01-21 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.5 |
| 925bc68a-9604-32b0-888e-9ad39f2e0116 | -7.2594 | -43.0881 | 2026-01-21 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.9 |
| abd1c8c4-282f-371c-91f9-ffb0ad9e6bd1 | -20.3481 | -57.9033 | 2026-01-21 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.6 |
| 97948fe6-c147-3d8f-99ca-a6ccd5d3823c | -7.2594 | -43.0881 | 2026-01-21 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.2 |
| c7749593-26ba-3fb3-a93d-ad2ab144fb3b | -7.2597 | -43.0645 | 2026-01-21 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.1 |
| 1e6e9aca-4f43-3355-bdbe-d6e4c615f9fe | -3.1596 | -48.1451 | 2026-01-21 00:31:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14ac95ae-a3f3-35a5-81cd-16ceb15a062b | -7.2706 | -43.061901 | 2026-01-21 00:31:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 76fff545-3a3e-3ef3-bab6-2a95d37316fd | -23.6084 | -48.2519 | 2026-01-21 00:31:00 | METOP-C | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 03e72b75-5b03-36d1-8b93-cde27ffc1bae | -3.5555 | -48.8465 | 2026-01-21 00:31:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a6f6643-c685-311f-ab61-290acd930eab | -4.1007 | -47.300301 | 2026-01-21 00:31:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c2bcd598-bb9d-3cbd-bafb-a93ee10ae2b7 | -3.5573 | -48.854198 | 2026-01-21 00:31:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb559791-c6b0-3913-ba11-edb621e9fa07 | -5.9413 | -44.444099 | 2026-01-21 00:31:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 66b244e2-770c-35e7-bb8b-4a77ea36c461 | -7.2724 | -43.069698 | 2026-01-21 00:31:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 51776f93-a247-3cc0-b707-36d15c492d97 | -7.2644 | -43.0798 | 2026-01-21 00:31:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9dff22d0-daba-3149-b417-95f6684fc91c | -7.2626 | -43.071999 | 2026-01-21 00:31:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e7fba3e0-7cd2-3a73-be8e-e06302a9fd11 | -7.2742 | -43.077499 | 2026-01-21 00:31:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 82ff5a04-7c00-3f0f-b880-4f52b3072f2d | -5.9429 | -44.451302 | 2026-01-21 00:31:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7ada281-0cf8-3d4f-bca0-de908495d308 | -2.6155 | -47.340401 | 2026-01-21 00:31:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc901901-4885-354f-94fd-9cd3e045277c | -3.158 | -48.138 | 2026-01-21 00:31:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b9ecd43-7947-329f-b52b-3a05df1f42e9 | -2.9405 | -48.223701 | 2026-01-21 00:31:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7c15f34-7f30-3a9f-94d0-2c3b401cde86 | -2.5336 | -47.794498 | 2026-01-21 00:31:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4baa7c1f-7767-3a30-ab0b-952de8de3861 | -20.9937 | -48.8321 | 2026-01-21 00:31:00 | METOP-C | EMBAÚBA | SÃO PAULO | Brasil | 3514957 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 840d2e5d-1c19-39d1-b638-fd50cf462a69 | -4.1089 | -47.291199 | 2026-01-21 00:31:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 69f5ae98-5ccc-3409-b460-2d9d1ee3e697 | -2.5135 | -47.255001 | 2026-01-21 00:31:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89393673-149c-3d06-a8dd-cbedac9a1be4 | -1.7741 | -47.132599 | 2026-01-21 00:31:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82bee521-c0cc-3fc8-aa89-fdcf11f91437 | -4.0991 | -47.2934 | 2026-01-21 00:31:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 53458ec8-ed54-3712-974b-adc3d9a48ab5 | -4.1105 | -47.2981 | 2026-01-21 00:31:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| afea9c95-10f1-3795-a494-1944633fda9a | -27.38568 | -49.24796 | 2026-01-21 00:43:00 | TERRA_M-M | LEOBERTO LEAL | SANTA CATARINA | Brasil | 4209805 | 42 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| e3874af1-f075-30c9-9927-6b466c02457e | -23.60454 | -48.2645 | 2026-01-21 00:45:00 | TERRA_M-M | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 8d045a51-aae8-3d52-9f05-80126f403998 | -22.02022 | -56.34011 | 2026-01-21 00:47:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 9b3384e5-1bc9-3f52-b2c7-325e10594cff | -19.44197 | -57.23146 | 2026-01-21 00:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 3ba83ced-fca5-36c5-ad79-87969acf200c | -15.01874 | -57.86012 | 2026-01-21 00:47:00 | TERRA_M-M | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5f355854-2b0a-374a-a66a-b38c664ddac0 | -16.07286 | -56.58658 | 2026-01-21 00:47:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3124546a-71ce-372f-97ff-13ae6e15bdc1 | -20.34109 | -57.89825 | 2026-01-21 00:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.8 |
| bce38fcd-f49b-3ee7-a810-54cee54ab677 | -19.66244 | -56.95104 | 2026-01-21 00:47:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| cb5de803-d33c-38db-8add-8d2f66334bec | -20.33155 | -57.9155 | 2026-01-21 00:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.5 |
| 08b8594f-8bbb-342f-b16d-e4f5779d910d | -19.43617 | -57.27417 | 2026-01-21 00:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.9 |
| 4c2f51a5-b21b-37d8-8ddd-27c16e755dc8 | -19.42713 | -57.28938 | 2026-01-21 00:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 96f27b81-c7c6-329e-8abb-b044c371a07f | -20.99738 | -48.85193 | 2026-01-21 00:47:00 | TERRA_M-M | EMBAÚBA | SÃO PAULO | Brasil | 3514957 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 3a3bd95d-5688-3185-bbd1-6c09ec017f52 | -19.43778 | -57.288 | 2026-01-21 00:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 4ae371c1-d1fe-33e6-b67d-98afcece1ad9 | -19.21018 | -53.44164 | 2026-01-21 00:47:00 | TERRA_M-M | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 72af8fde-3062-314c-b5ec-dac57f8b619b | -20.34286 | -57.9141 | 2026-01-21 00:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.8 |
| 4c8c4e66-2807-344a-8331-13bfebf1837d | -19.64005 | -56.94053 | 2026-01-21 00:47:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 17.9 |
| 9add2d1e-3926-3fbf-8c4e-27c9ebbd67d4 | -19.65201 | -56.9524 | 2026-01-21 00:47:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 422d2f0f-c472-3c25-b42e-4ea6470718e1 | -22.02383 | -56.34535 | 2026-01-21 00:47:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 72ab8c63-f474-3ef3-afeb-41184804453c | -20.98803 | -48.84649 | 2026-01-21 00:47:00 | TERRA_M-M | EMBAÚBA | SÃO PAULO | Brasil | 3514957 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| a10cc3a9-908a-3e3d-bc42-5e2faa436633 | -18.82337 | -51.61882 | 2026-01-21 00:47:00 | TERRA_M-M | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c2c8695b-67c5-3cd5-88a7-dc1ff5f55e8c | -18.93693 | -53.39794 | 2026-01-21 00:47:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 514f21c3-7f95-34a1-bed9-353bd1b8f329 | -20.35239 | -57.89685 | 2026-01-21 00:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.3 |
| 56036e24-1afe-399e-adf8-9092ce017c64 | -20.72972 | -55.15797 | 2026-01-21 00:47:00 | TERRA_M-M | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 11c9c1f3-4528-38d8-9cc7-fcd808d9a6be | -20.72026 | -48.78936 | 2026-01-21 00:47:00 | TERRA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| f348d2e2-53c5-3fd5-99c9-c602b953d487 | -20.99531 | -48.8393 | 2026-01-21 00:47:00 | TERRA_M-M | EMBAÚBA | SÃO PAULO | Brasil | 3514957 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| b82b42f9-d268-3ddb-8b37-8cb9e0530323 | -20.32979 | -57.89966 | 2026-01-21 00:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.7 |
| 2dff41c8-2cdf-3614-a2a2-5c2d303872c5 | -15.97543 | -56.27839 | 2026-01-21 00:47:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 136ddb62-e368-320e-8c92-38b7176d29e5 | -19.39361 | -57.27969 | 2026-01-21 00:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 68ee975c-37e5-3497-8118-819189f48463 | -19.67705 | -56.89545 | 2026-01-21 00:47:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 12.7 |
| 9ea92c92-5a7c-3056-9f45-966dc748cebd | -6.5631 | -51.1126 | 2026-01-21 00:50:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| b782eee5-f1b7-3236-b66d-ccb551f5f792 | 2.10477 | -61.53492 | 2026-01-21 00:52:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 917954da-0e8c-335d-b0d2-50c2216664c8 | 1.99768 | -61.44341 | 2026-01-21 00:52:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 828cb175-f33c-3218-8a6f-2b20993516a8 | 1.01707 | -60.5486 | 2026-01-21 00:52:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 423642bc-b03c-32a2-8d59-f700ab3d74bf | -1.61389 | -54.70701 | 2026-01-21 00:52:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3feaf69e-1c7c-3426-bc4a-d75812202417 | 3.8191 | -60.27777 | 2026-01-21 00:52:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ee485c53-b29e-3f13-8f0d-4d8afafa41b3 | 3.44134 | -60.99986 | 2026-01-21 00:52:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 5991fd98-44fe-3b90-a233-47ccd24eb947 | 3.32645 | -60.09496 | 2026-01-21 00:52:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 34.8 |
| c5ec498b-7921-3afd-b0a6-0ed5218a9068 | 2.91815 | -60.94034 | 2026-01-21 00:52:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e8804424-27d9-34cf-9b05-d90dd046e19e | 2.53999 | -60.57299 | 2026-01-21 00:52:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 2e1919c8-a290-3703-94c3-9c30139b2767 | 1.35449 | -60.03682 | 2026-01-21 00:52:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f0eed516-183e-3d7d-97ca-75e4b5515bf7 | 3.32789 | -60.08493 | 2026-01-21 00:52:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 26cc3c9d-6018-3c88-994f-25070b747251 | 3.44292 | -60.9886 | 2026-01-21 00:52:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4c80ee0c-4875-32c8-896e-82cce52d135b | 1.54959 | -60.26627 | 2026-01-21 00:52:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d866b800-48e0-3c6a-b4e8-bc0c854e2855 | 3.43975 | -61.01112 | 2026-01-21 00:52:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cfa93d11-c7ac-308c-964a-fe893d7d5652 | 1.1327 | -60.52504 | 2026-01-21 00:52:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.4 |
| cbf71e0f-b1de-3783-bf73-0be50a4006e9 | 1.13458 | -60.51963 | 2026-01-21 00:52:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 57c8cedc-d8aa-3a64-95c8-d874349102bf | 1.13296 | -60.53093 | 2026-01-21 00:52:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| db0ca7ad-eafd-33d0-9d06-e058a0e33905 | 2.54972 | -60.57439 | 2026-01-21 00:52:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c412a849-e47a-37ba-b131-396a58165a33 | -3.06348 | -54.59313 | 2026-01-21 00:52:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1a657a27-9187-3343-b9fc-26cc60c4ddf4 | -10.1058 | -36.1748 | 2026-01-21 01:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 76.5 |
| f29f57da-9561-3abf-815f-0f08af85f42f | -20.322701 | -57.881901 | 2026-01-21 01:32:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 871c3352-451a-3508-992a-c475c9bd0e06 | -20.337299 | -57.859001 | 2026-01-21 01:32:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3dea2c3b-0707-30d7-b4fd-b981449994cf | -20.3277 | -57.862 | 2026-01-21 01:32:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 865982ee-7609-3a91-8b75-6303f55fc9c7 | -20.3515 | -57.8731 | 2026-01-21 01:32:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 31407015-337c-3408-92a7-e3e5f6dfb1f8 | -10.2907 | -65.264503 | 2026-01-21 01:32:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a3e6dcf3-5fdb-3242-bb49-bc17cc67adaa | -20.3323 | -57.879002 | 2026-01-21 01:32:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 524b94bd-f3a5-36d9-aff6-a08749fc9339 | -19.6308 | -56.913502 | 2026-01-21 01:32:00 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 480003f3-a72f-3096-93c2-69a95dec796e | -20.3181 | -57.864899 | 2026-01-21 01:32:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a27b9f7b-37c4-3363-bec8-4fce701a565c | -19.596701 | -56.928398 | 2026-01-21 02:10:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a4cff48a-522c-3758-865d-ab3efeade8fb | -19.606199 | -56.925301 | 2026-01-21 02:10:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ca558291-c8a5-3176-ab16-644a9ef286b1 | 3.4376 | -61.0055 | 2026-01-21 02:30:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 5cc48fd5-81ba-3584-8cbe-adfa8388b2f6 | -4.88857 | -37.28733 | 2026-01-21 03:10:00 | NPP-375D | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 765d96bf-f9a2-3e63-bd5b-d38e08c32aa0 | -4.8896 | -37.28886 | 2026-01-21 03:29:00 | NOAA-20 | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d74b24cc-874a-3194-9734-9ebd4b6abf25 | -5.09334 | -37.7889 | 2026-01-21 03:29:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 157158bb-a11f-3140-8725-c92eec2c0ca3 | -10.25088 | -36.52569 | 2026-01-21 03:32:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| af522672-b080-3a4a-8484-b9035945f336 | -10.24722 | -36.52505 | 2026-01-21 03:32:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cf759aa1-e3bd-36d4-b16d-639edfa20af8 | -10.24796 | -36.52072 | 2026-01-21 03:32:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 29f14ee4-f737-33f1-ac32-38daea3e1b03 | -11.92434 | -38.32408 | 2026-01-21 03:32:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e2c0f653-cd48-33cb-952a-5ec8f6429646 | -10.25162 | -36.52135 | 2026-01-21 03:32:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5c2212e6-112d-3c94-8b3c-30b2b6f3725a | -23.60498 | -48.26218 | 2026-01-21 03:36:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 8.3 |
| fd81b422-c8c6-381b-bbd8-e60c7a3f029b | -23.60388 | -48.26672 | 2026-01-21 03:36:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |


[Clique aqui para ver as próximas entradas](README2.md)
