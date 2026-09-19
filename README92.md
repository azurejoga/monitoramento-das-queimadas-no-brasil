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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a97de1c-e9d5-331a-b2f9-2ab54b5ee135 | -13.00085 | -46.98928 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 6958fa5b-80f3-33f2-b35c-bda6405c73a7 | -10.70071 | -60.74123 | 2026-09-19 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2aab148-854c-37cf-b322-0b9cc186d2fa | -10.69163 | -60.73956 | 2026-09-19 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6892b55a-e9f2-3be7-a3ee-f63778a37347 | -12.15011 | -46.97169 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5b77e6dc-89a9-33ba-aceb-10cfe6007592 | -15.02638 | -48.56293 | 2026-09-19 04:59:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ecfc9fde-f3c5-3743-9ed4-228e64a78098 | -11.86212 | -47.59568 | 2026-09-19 04:59:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cfffe831-db4f-3739-9544-1fc1b0a2b517 | -12.27775 | -49.16588 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| f771bf13-dbb9-31a3-8600-0ade5a4fb570 | -12.8639 | -46.33941 | 2026-09-19 04:59:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4565a5f7-75de-3203-9a3d-127016c2d822 | -11.91265 | -50.12208 | 2026-09-19 04:59:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4fcac50e-ff82-34be-a4cc-1a726a86310c | -13.73732 | -48.79074 | 2026-09-19 04:59:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 39c6e114-ac2e-311e-9bfe-bdc2017ffd4c | -10.8738 | -56.20168 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 249029b4-3376-31e7-b216-cb5ae2788f1a | -13.33558 | -51.66555 | 2026-09-19 04:59:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4ab7858-3a21-392c-9df9-f81222d83e7b | -16.79907 | -46.99173 | 2026-09-19 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 867a9737-c596-3497-a0e6-3d5a370935b9 | -12.13917 | -47.01955 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b4e3fb90-b946-3dd0-9f25-453c0af0fcb0 | -15.64034 | -52.7169 | 2026-09-19 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf6620ac-09e4-373c-84d1-2ac389e18b92 | -14.92599 | -49.92486 | 2026-09-19 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 883529ce-bf8a-3cf1-a9c7-f033f5edbbc6 | -13.61111 | -46.93416 | 2026-09-19 04:59:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f161d281-9015-3211-aa50-99bf42717d8d | -11.94166 | -50.10747 | 2026-09-19 04:59:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 847cc22e-6652-3d52-a8ee-27aa22d51ce4 | -10.87907 | -54.06571 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ab1d0f7-1cb3-3514-8332-a9495a14b47e | -10.8642 | -54.09567 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42958085-1106-3e95-9375-1f6d84aa6d9f | -12.28127 | -49.16998 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 59ceaf6d-2c22-3cd1-b18f-2d7875b9848b | -11.41286 | -47.28072 | 2026-09-19 04:59:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2437161b-61f2-37e0-b3a3-52155a89efc7 | -11.8317 | -46.83784 | 2026-09-19 04:59:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a09d8fbf-a002-3fe8-9355-7b181cbd8953 | -11.77099 | -47.44058 | 2026-09-19 04:59:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d48fefd-66f7-3d5d-90e6-68ec6e622b83 | -11.90824 | -50.12613 | 2026-09-19 04:59:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 2e7df452-8e22-37e2-91a7-bdda256f7cec | -12.54057 | -47.09566 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 764e991c-ee66-3ed4-aadd-1f65e8018b3c | -10.86653 | -53.99546 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76ddf0a2-3919-3d51-bab8-f0285f360607 | -11.68139 | -54.4451 | 2026-09-19 04:59:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7749f77f-7086-3edc-95be-b4480ab68052 | -12.99725 | -46.98008 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 42a7284e-f5b8-3436-8c52-60e9cff78a0d | -9.25378 | -60.7929 | 2026-09-19 04:59:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d9b64b1-d281-39c2-8762-dde1473f63b5 | -11.94344 | -50.12192 | 2026-09-19 04:59:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9306317d-6005-3fb2-a7be-196c15f3a13e | -11.27211 | -54.11525 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dafb5275-f29a-3ac4-a3f0-432322731975 | -15.63293 | -52.76764 | 2026-09-19 04:59:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 451a1f01-6d4c-3142-b311-bfd4ad4a82d5 | -11.24343 | -54.10337 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 78e9eca9-b491-379f-9cbd-714835160c2b | -12.33513 | -50.71774 | 2026-09-19 04:59:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1f8e4627-ceb7-355b-9354-0d993b3d8b1f | -10.91339 | -53.97797 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 762f611e-b478-312e-8af2-847ca160aa69 | -14.17223 | -48.75625 | 2026-09-19 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdf9a87c-f055-39f8-b4e5-9477ccb5b59a | -10.48753 | -55.61066 | 2026-09-19 04:59:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65332275-42a5-3dfc-a138-265039081ac6 | -10.86489 | -53.98442 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5527251b-50ba-385a-9ddd-ff69a4029d90 | -11.94522 | -50.13635 | 2026-09-19 04:59:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f0f70cf-7664-33fc-b635-ab033acd140c | -11.43321 | -51.4658 | 2026-09-19 04:59:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 831ba2be-8dc1-35b4-bd3a-5d3a23bdbdef | -13.62675 | -48.30025 | 2026-09-19 04:59:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 017ffc69-76b0-3bf3-a8fe-d581a4ff919c | -17.03367 | -47.2958 | 2026-09-19 04:59:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d777a771-e0ec-34bf-aa34-e5f27d96e7c7 | -13.62147 | -46.96551 | 2026-09-19 04:59:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5be7f295-0940-38cb-985d-a4215cd2042a | -13.62998 | -48.30905 | 2026-09-19 04:59:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 015e6bbd-fbe9-3df6-a56e-fd347f5da491 | -11.14413 | -54.02225 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 979887c3-e7ec-3ae5-bef7-d54aa1cb5957 | -13.01682 | -46.97625 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9ffcb563-acc4-334a-a63b-231261e95521 | -10.87073 | -54.09668 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a869d1f5-7e1c-3b15-adcf-79c900f909e5 | -11.42039 | -51.45578 | 2026-09-19 04:59:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92a4ce62-53e8-313c-a04e-a8afe91f31e1 | -10.89461 | -53.98929 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3f59b56-cc53-3d12-b39b-a3b0e04fc2bc | -10.91008 | -53.97744 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2771b250-d4e4-3489-b6fc-84d31d1c8809 | -10.69784 | -60.73102 | 2026-09-19 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a138a78e-5cad-36c2-b0a2-f1a88658d4e4 | -12.12392 | -47.00036 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ba27656-fef8-3396-9e61-c7f435477e43 | -11.05723 | -49.73606 | 2026-09-19 04:59:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7fc8ea5d-989b-310f-a870-8d9e475153fa | -10.69533 | -60.74509 | 2026-09-19 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72ea39db-4fd4-3441-9a4e-4858d1bed71c | -14.15394 | -45.17143 | 2026-09-19 04:59:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5218a08e-501b-3635-94c6-7af7230ef5ed | -10.87119 | -56.21728 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a3470980-f261-376b-8812-45a32348403e | -13.74471 | -48.79936 | 2026-09-19 04:59:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b0df84e-1699-38fe-b19f-51c14cda3d19 | -11.79493 | -46.80584 | 2026-09-19 04:59:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ebf2d95-7a2f-3162-8158-f8cb60eb530c | -10.86364 | -54.09917 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffab497d-4d0e-30f3-9341-e83d14d96399 | -11.44253 | -51.47531 | 2026-09-19 04:59:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52baa85d-7edd-312e-bceb-d8f05efee4f3 | -9.37485 | -60.32096 | 2026-09-19 04:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f16be3cf-6fe6-355a-bd2f-329ee7001514 | -14.92669 | -49.91979 | 2026-09-19 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9ec3fca1-7af7-3e2c-8868-c33152713d2d | -10.86251 | -56.18378 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a13dd251-8a42-3f14-ad56-26c0ae016f55 | -11.01876 | -54.12764 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 48f1b1e7-3a65-3edb-93b5-c0a32bb4b47e | -12.70337 | -45.95241 | 2026-09-19 04:59:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8e95cdf2-eb15-3980-a74c-3a9aaf4365c6 | -10.86555 | -56.20826 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddc56d0d-06bd-3909-a3cb-d0db74d752e5 | -11.27486 | -54.11929 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef3a6639-4d2d-3b82-8251-54f2bf82b68d | -14.10032 | -44.83025 | 2026-09-19 04:59:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c28273f-9f9f-34e2-be94-2af6aaff95b1 | -14.93138 | -49.91512 | 2026-09-19 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 66aa9434-79f2-359e-84b3-0b31f3160756 | -10.88359 | -53.99461 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef2d4c4b-a2f3-36eb-8c9c-f98368524266 | -14.14894 | -45.21245 | 2026-09-19 04:59:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff0b85b4-14f2-39bb-b61d-21e0d3b4a95e | -15.594 | -56.57006 | 2026-09-19 04:59:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6934a4c5-3023-3178-9530-256bc7d051e6 | -16.60164 | -46.99539 | 2026-09-19 04:59:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5bc60cdb-35b8-3309-a19e-92ab730f854d | -10.93439 | -53.95264 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2001c633-bd8d-3212-af7b-ba0a3ed9a8e0 | -16.88925 | -50.5769 | 2026-09-19 04:59:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 14de0ced-a286-3529-b808-8c5f5b15e79f | -12.14488 | -46.97566 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6ab945ab-14c2-356b-9933-c199b9ebbb83 | -12.34446 | -48.20277 | 2026-09-19 04:59:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f2ac2dd-a40b-35b4-949e-5642b07bbd1b | -11.85711 | -47.59941 | 2026-09-19 04:59:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a52ea30-f92d-3a6d-971b-bd422a21ea21 | -11.43789 | -51.45845 | 2026-09-19 04:59:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a51aa1a4-5e54-31ca-87f6-f3c7d5128de4 | -13.67981 | -48.57576 | 2026-09-19 04:59:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| a54214c2-41b7-3784-a2e1-1d820c71b917 | -13.8786 | -48.60103 | 2026-09-19 04:59:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e0f1833e-c8fc-3de7-aa93-cf0b422807ff | -12.14152 | -45.14385 | 2026-09-19 04:59:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05595ad5-57b8-355e-b364-267372f9ee7a | -11.27542 | -54.11579 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 127323b8-fe33-3450-a13e-e4e7821095d2 | -12.14423 | -46.98065 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4e2aa57f-6b54-3d25-a226-d928f98b682e | -13.01519 | -46.95177 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43f1956d-34b0-308e-a41b-2feb8ace776b | -11.81983 | -46.85639 | 2026-09-19 04:59:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| da8f399a-1621-3b84-af0c-5a795bc1c83f | -13.00672 | -46.98061 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d25be0b7-cf97-3c38-89de-f1848758c081 | -16.04642 | -49.98422 | 2026-09-19 04:59:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c092986c-514a-3a4d-9127-ac53a910215a | -11.82094 | -46.85878 | 2026-09-19 04:59:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 359ecd41-0745-3cf4-900c-e2cb9b5eae60 | -10.69617 | -60.74039 | 2026-09-19 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8517f90e-075e-31e7-aa15-8aa0196deac2 | -11.01817 | -54.15272 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6dbe55e-90a4-3037-8c9b-4a57f8e0b050 | -14.1694 | -47.84443 | 2026-09-19 04:59:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe2f467f-4407-35ba-918b-b5f403af3320 | -12.13748 | -46.99636 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ad0c4f14-d3be-3ca7-9357-2ebc318d2c77 | -11.43849 | -51.45449 | 2026-09-19 04:59:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7134c85a-9a36-3aa2-923c-e0bff287089a | -10.85773 | -56.19098 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2b84a17-d1ef-39de-926f-ee3de57febda | -12.69446 | -45.94214 | 2026-09-19 04:59:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef176943-609e-3632-97da-94ff9697277f | -14.78898 | -48.58581 | 2026-09-19 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a98f94c-57d8-36b7-91cf-4d53ee23a955 | -10.89407 | -53.99272 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 733f85df-5b60-38ef-9d4e-f8ab37c780dd | -12.33623 | -50.7357 | 2026-09-19 04:59:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README93.md)
