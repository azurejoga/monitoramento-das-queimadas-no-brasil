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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3afbe98b-70ca-3937-872d-93b73672db53 | -13.84362 | -46.9012 | 2025-07-13 01:02:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 84ae41c9-e60a-337c-b422-e33d34ee685f | -13.13763 | -47.31861 | 2025-07-13 01:02:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 0a020db1-7d30-3747-9205-428436f0c050 | -13.85669 | -46.89832 | 2025-07-13 01:02:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 4655b8a1-954e-3fd4-9e37-3dc3621c511e | -13.83873 | -45.89707 | 2025-07-13 01:02:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 734b03a0-3acf-322a-976d-66bf1cc5d47e | -13.84027 | -45.93059 | 2025-07-13 01:02:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 9acfc574-4fb6-399e-b986-febd104a99fe | -13.13929 | -47.32399 | 2025-07-13 01:02:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 25f30f60-cbe3-3f8d-832f-1ef82c5000cb | -13.8358 | -45.90428 | 2025-07-13 01:02:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 77c096b4-52f8-3c0b-9ee2-11698f6a0b68 | -19.0902 | -56.04235 | 2025-07-13 01:02:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.7 |
| c20d900d-1b8c-3b36-9bab-d9ad64b3eae6 | -13.84338 | -45.92331 | 2025-07-13 01:02:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 5de43b28-b4ce-32a4-b1ac-e80d3e566f8c | -10.57369 | -49.12473 | 2025-07-13 01:05:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 2ffa61d8-8a4b-361b-a232-fa18b82168a4 | -9.02641 | -59.54914 | 2025-07-13 01:05:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 2998fe54-2014-3e7b-8eae-57096090bd7c | -5.74722 | -45.00885 | 2025-07-13 01:05:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 8049019e-be16-3923-abaa-751c8a305087 | -9.02407 | -59.5411 | 2025-07-13 01:05:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 8cf229c0-2545-34c2-bbb8-ce7b60badfe0 | -4.53239 | -48.01608 | 2025-07-13 01:05:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| ffff1488-2f9a-3bd3-9f36-d6aeec6a62de | -5.72664 | -49.10971 | 2025-07-13 01:05:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 7c92f7c9-17bf-393d-861b-56e75c800287 | -11.72893 | -47.46807 | 2025-07-13 01:05:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 26ccd9fd-54be-319b-9de3-cb89e7b314cc | -12.01702 | -49.52723 | 2025-07-13 01:05:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 3834c667-a05b-3117-b21b-fdfed74eab52 | -5.74685 | -45.00387 | 2025-07-13 01:05:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 1bf3c379-bd45-3a1f-9e07-7e39a3bb13ad | -10.50649 | -53.59158 | 2025-07-13 01:05:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| eab53fd4-13fa-303d-9356-36f4bd4a7ef1 | -12.42594 | -50.46205 | 2025-07-13 01:05:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 27255b0a-f96e-3ef6-a85b-a759807e8966 | -10.67239 | -56.54943 | 2025-07-13 01:05:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 25fe7ace-76b0-3e88-ba1f-37785a400c8d | -11.87493 | -58.70946 | 2025-07-13 01:05:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 43e59dfa-a9ad-3ae6-9a42-a7e62dc0e2f0 | -11.86405 | -58.71098 | 2025-07-13 01:05:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b80f42cf-f4c9-3639-adac-8b2ed8e193b6 | -4.54456 | -48.02041 | 2025-07-13 01:05:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 11b19f49-1166-351b-b931-cb2003970db8 | -12.11613 | -58.01314 | 2025-07-13 01:05:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 430d7e7d-4895-352a-82a5-80d121c6b157 | -10.95783 | -54.37692 | 2025-07-13 01:05:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6a0b53cc-b24f-3c61-85c1-908547565cbb | -10.57115 | -49.1083 | 2025-07-13 01:05:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| dcbfa3cb-d960-3d22-888e-09e97777c7da | -4.53013 | -48.02221 | 2025-07-13 01:05:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 40c87b07-ee74-308d-a3ad-b7a4799b3cb6 | -7.9913 | -43.3649 | 2025-07-13 01:10:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 130.4 |
| d5356a71-7c52-3c53-83ce-7a576ad4af25 | -7.9721 | -43.3904 | 2025-07-13 01:10:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 70.9 |
| a0a8ebec-298e-3555-93ff-4be7bc86add0 | -8.0099 | -43.3864 | 2025-07-13 01:10:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 68.6 |
| bb3068c9-a872-363d-89f4-d5a04e515382 | -7.991 | -43.3884 | 2025-07-13 01:10:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 328.6 |
| 6f1e4581-3ac3-3f8f-90ec-8500f2170e06 | -5.739 | -44.9945 | 2025-07-13 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 77a8c827-07ff-3484-8106-c40fc36e0334 | -18.0597 | -50.5142 | 2025-07-13 01:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 040c0333-e129-30c4-9d2a-bf1dfcc171c4 | -7.9913 | -43.3649 | 2025-07-13 01:20:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 106.1 |
| 2f6e778c-641a-3e5b-af2b-3968f6c9bb5c | -7.9721 | -43.3904 | 2025-07-13 01:20:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 80f93e02-272f-3b55-97e5-4a737feae6f2 | -7.991 | -43.3884 | 2025-07-13 01:20:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 308.2 |
| 929fb99e-8fbd-3b9d-ae6a-f90641e1c6b7 | -5.739 | -44.9945 | 2025-07-13 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 8d370e4a-56dd-395c-9c4d-53c4a8c0f87c | -8.0099 | -43.3864 | 2025-07-13 01:30:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 56.8 |
| c9abffda-eaaf-30b9-9b50-83a8d85f077c | -7.9913 | -43.3649 | 2025-07-13 01:30:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 72.0 |
| 602ccca2-120e-348a-a926-cfaf6a6e3d6d | -7.991 | -43.3884 | 2025-07-13 01:30:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 292.3 |
| 67f35048-d37e-3982-a126-b65fa6a409f5 | -5.739 | -44.9945 | 2025-07-13 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| b1cf1086-a096-388c-b225-e5a7a6944bee | -7.9721 | -43.3904 | 2025-07-13 01:30:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 0900e951-d2b2-3dea-a4ec-69a5b5911656 | -5.739 | -44.9945 | 2025-07-13 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 27863d08-eb7e-3ab9-8d19-d82e59d40374 | -7.9913 | -43.3649 | 2025-07-13 01:40:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 102.1 |
| bd5546b3-88d3-3703-aa46-f5687a565713 | -7.991 | -43.3884 | 2025-07-13 01:40:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 217.8 |
| ae619cb2-919c-3b56-89e7-55298957efe5 | -12.0236 | -63.787899 | 2025-07-13 01:40:00 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d25cfa2d-2fc7-33d2-b107-fa14f42224ea | -12.43 | -50.457001 | 2025-07-13 01:40:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b0e87e57-ae99-3ea9-9f93-42dcfb22e31d | -12.022 | -63.7808 | 2025-07-13 01:40:00 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 887c59e5-b792-34f7-a11f-b2cdf3217f39 | -9.0263 | -59.5485 | 2025-07-13 01:40:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 66c2ddde-8b68-3878-b108-172b35edca34 | -11.8719 | -58.7048 | 2025-07-13 01:40:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fc4b7ba7-9922-3975-bdf9-50eae3677264 | -9.248 | -64.406998 | 2025-07-13 01:42:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 099a5c53-68c7-3188-9f88-3229ef9cc38b | -9.2464 | -64.400002 | 2025-07-13 01:42:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c12b05b8-8920-317f-b9ea-64a88b3bd31e | -7.9721 | -43.3904 | 2025-07-13 01:50:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 8dd8c0c5-d4a6-3d43-8664-bc8e1d80e9db | -7.991 | -43.3884 | 2025-07-13 01:50:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 345b6ff1-847f-3f72-8b47-4811fa3b8d3f | -7.9913 | -43.3649 | 2025-07-13 01:50:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 56.0 |
| 473c19ee-670a-3a1a-a46d-d1f7005ffdee | -5.739 | -44.9945 | 2025-07-13 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 21be81f2-62cb-358e-8102-7bf71e070e99 | -13.8474 | -46.8964 | 2025-07-13 01:50:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| d252257b-c72c-30e1-b1cb-b947759180e3 | -5.7392 | -44.9718 | 2025-07-13 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 443b5e3a-d862-3590-8bd7-26520d73a675 | -7.991 | -43.3884 | 2025-07-13 02:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 183.8 |
| bf60c8d1-7edf-3794-abc8-c03b64077d1e | -5.739 | -44.9945 | 2025-07-13 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 86c2e599-2d83-3653-972b-f6367f7f5220 | -7.9913 | -43.3649 | 2025-07-13 02:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 56.5 |
| f636144d-b6f8-3984-8bf7-68c6f5d47714 | -5.7392 | -44.9718 | 2025-07-13 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 2e696ee7-ea19-3358-982a-773d64c4c79c | -7.9913 | -43.3649 | 2025-07-13 02:10:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 61.3 |
| 8a895719-c392-33fb-bc7a-56f820197785 | -13.8474 | -46.8964 | 2025-07-13 02:10:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 56.5 |
| d6f26004-3d53-3941-86d9-98cb37f374c3 | -7.991 | -43.3884 | 2025-07-13 02:10:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 2615105a-6072-39c6-820f-7c88862457fd | -5.739 | -44.9945 | 2025-07-13 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| e66f2d8f-869e-3816-9b73-30f1338fd4b0 | -5.739 | -44.9945 | 2025-07-13 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 4ed16789-97a1-38db-bebc-3919c6e87d60 | -7.991 | -43.3884 | 2025-07-13 02:20:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 128.4 |
| b58cec07-6cd2-3c81-a083-ab47fcf9fdb8 | -5.7392 | -44.9718 | 2025-07-13 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 1fbe66f2-b315-3e58-8032-5d0bd884cac7 | -7.991 | -43.3884 | 2025-07-13 02:30:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 648e17c4-427d-3ad2-a8c9-d4f803ee1b88 | -5.7392 | -44.9718 | 2025-07-13 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 0d499c48-c1ca-395c-a8a0-93da45780400 | -5.739 | -44.9945 | 2025-07-13 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| d92f3202-58fb-364b-9df8-6b07cc7428f0 | -13.8474 | -46.8964 | 2025-07-13 02:30:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 487c4884-c4c0-38ec-927f-d63ac094aa64 | -5.7392 | -44.9718 | 2025-07-13 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 4c0b4a08-330d-3915-8ade-3b2b7252dd50 | -5.739 | -44.9945 | 2025-07-13 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 5e0c762c-dd79-3352-945a-037959e430e4 | -13.8474 | -46.8964 | 2025-07-13 02:40:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 6fb891a7-3545-3f71-9b80-71f56e68b62e | -7.991 | -43.3884 | 2025-07-13 02:40:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 4f37f5f9-589a-34d0-9026-2696899894ad | -5.739 | -44.9945 | 2025-07-13 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| d20f074b-9249-3221-a34e-533a85afaffd | -7.991 | -43.3884 | 2025-07-13 02:50:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 9e84c7dc-88cd-3cd9-932d-1949bfccaa4e | -13.8474 | -46.8964 | 2025-07-13 02:50:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 2f578584-6346-3ba5-8516-374d23425b49 | -5.7392 | -44.9718 | 2025-07-13 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 168a60f4-c3ea-394c-bf5a-2a3c0a59e786 | -13.8474 | -46.8964 | 2025-07-13 03:00:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 5c5fe2c7-5d5e-3e9d-8110-b49485cc1d5b | -5.739 | -44.9945 | 2025-07-13 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| e6287a6a-b999-3595-859e-c9ef14da7abb | -7.991 | -43.3884 | 2025-07-13 03:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 50df3d21-175d-3155-b12c-1034cb21d8f3 | -5.7392 | -44.9718 | 2025-07-13 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 7d5cffb0-cd91-3a40-bdff-66c527833c98 | -5.739 | -44.9945 | 2025-07-13 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 9981ee6b-b45e-3005-9b36-929e861231de | -13.8474 | -46.8964 | 2025-07-13 03:10:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 68.9 |
| a00bb49a-fd0e-31c3-8103-66101a51aebd | -5.7392 | -44.9718 | 2025-07-13 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| cb36132f-8597-3bea-aaf8-fdf6bce60df7 | -22.65806 | -43.29609 | 2025-07-13 03:10:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2b63d713-20c6-38f1-8a55-2173b3dfa102 | -22.6627 | -43.29014 | 2025-07-13 03:10:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7500a3dd-773d-33c7-b992-a3d8a4702b7a | -22.66113 | -43.29632 | 2025-07-13 03:10:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 62109e9c-807d-3e91-8343-e2963e44be38 | -22.65959 | -43.2899 | 2025-07-13 03:10:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fd582890-aeb5-3602-b6b1-4ffdaaa13bc1 | -5.739 | -44.9945 | 2025-07-13 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| ff2a217e-32f7-3753-92ae-977e10ea276a | -13.8474 | -46.8964 | 2025-07-13 03:20:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 8bce6382-a9eb-3aa7-b25c-ed589a5767db | -5.7392 | -44.9718 | 2025-07-13 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 0348c415-65b2-32e5-9280-25ad2e1750d7 | -6.95176 | -42.73703 | 2025-07-13 03:28:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 9e257bfd-c7ab-34cd-9053-f92a02500cb7 | -6.64085 | -39.32882 | 2025-07-13 03:28:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 51ad7e51-6b4b-3367-86e5-bbc6f8bf1c18 | -7.10911 | -40.39154 | 2025-07-13 03:28:00 | NOAA-20 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 30debd0e-fee6-3fd3-ad53-1276af009200 | -6.12878 | -42.9613 | 2025-07-13 03:28:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |


[Clique aqui para ver as próximas entradas](README3.md)
