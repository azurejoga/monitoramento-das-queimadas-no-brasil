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
| c2f353bb-b65c-313f-ad0c-ed3cf2d82061 | -10.94083 | -55.33516 | 2025-06-05 04:59:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7a5ec1c-4b27-3e0a-9c62-23e8c00fdda9 | -9.22692 | -48.85081 | 2025-06-05 04:59:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bcfa44e8-0498-38a4-938d-1dab3cc00511 | -10.67963 | -57.60691 | 2025-06-05 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee508e79-3ba9-39d7-93ee-4bdb74762381 | -10.85318 | -46.85643 | 2025-06-05 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73c553e5-1828-3d63-b5c7-33d87c06be74 | -12.05922 | -47.3323 | 2025-06-05 04:59:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe62e487-30aa-3e8c-aacc-7264bc4c976e | -7.01497 | -44.59517 | 2025-06-05 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1d2201a5-083f-3590-b0c3-52a916a67700 | -12.0635 | -47.33309 | 2025-06-05 04:59:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| df73500d-d41b-31b7-927d-20a6bc83f325 | -6.98364 | -47.08437 | 2025-06-05 04:59:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bde358c7-5c96-3710-aa31-fe7f97633309 | -11.57234 | -47.44748 | 2025-06-05 04:59:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 449929a3-bc50-3889-9e46-bbcd06653aba | -7.20622 | -43.13437 | 2025-06-05 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8b51cc5f-ec88-3e7a-97a4-67fbcda61475 | -10.85358 | -46.85343 | 2025-06-05 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c38a8143-12a8-34d9-9cb0-c0a388ce418a | -7.2192 | -43.13153 | 2025-06-05 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 08618a69-bec9-3dea-b399-71a3db0de228 | -10.68707 | -57.64841 | 2025-06-05 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59e647ee-cacc-33c7-b567-11fc42a9584c | -7.01556 | -44.61906 | 2025-06-05 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bef457ca-8a07-3ed3-9038-837c772b3a60 | -7.90413 | -50.36121 | 2025-06-05 04:59:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| ba25bcfa-ff79-3d12-9f74-307a78eaff56 | -8.9663 | -47.97081 | 2025-06-05 04:59:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9765e454-cffe-3c81-865b-50ca8e1538cd | -10.82233 | -56.95886 | 2025-06-05 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 640ad902-54ac-3ad0-8b83-a243af4292ba | -10.94527 | -55.32866 | 2025-06-05 04:59:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11e163ff-cd8c-3535-82b9-03b86aed35c0 | -11.45019 | -54.09319 | 2025-06-05 04:59:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a839b0a6-e819-3f5a-95b9-9b035e882f9c | -9.51895 | -47.2302 | 2025-06-05 04:59:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| abb7364a-0a75-31f1-9b2e-0678c7ea4059 | -11.83771 | -51.2844 | 2025-06-05 04:59:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1fb4057-0db1-3af0-87a9-20f444092f10 | -11.13469 | -54.22182 | 2025-06-05 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 75902823-f54e-3b3e-8695-be9fc92bfc5a | -7.01338 | -44.6065 | 2025-06-05 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9d4f9f6-2c10-311b-9c60-a91e03883136 | -6.63614 | -47.34895 | 2025-06-05 04:59:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4476d60e-cc1c-3e77-b3e3-522ac636b179 | -11.4361 | -54.09471 | 2025-06-05 04:59:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6aa4fb1d-6070-3c1a-95f5-6ab15435c566 | -9.35476 | -47.6913 | 2025-06-05 04:59:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 515ea0f7-0cf8-38c2-ad19-bc655b521de8 | -10.81489 | -56.96146 | 2025-06-05 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 7cddccf4-7d73-3584-8bb9-23cb18c69ce8 | -7.53956 | -45.82557 | 2025-06-05 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e5f1f92-0a00-3557-9a2f-cabc65ceae53 | -7.19942 | -43.13811 | 2025-06-05 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 350e4af0-0400-31d9-83e7-0fcd1c2ae50f | -7.01098 | -44.61064 | 2025-06-05 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3f717e82-6e39-3325-8a51-15c55d643099 | -10.65162 | -49.43776 | 2025-06-05 04:59:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 435624fe-b60f-34ce-8d52-2aa5cc771ce5 | -8.95419 | -47.28741 | 2025-06-05 04:59:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 142fe97a-8c2f-3581-a05e-6da9443d8061 | -6.64077 | -47.34956 | 2025-06-05 04:59:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b84df64-1a0c-3cc2-88d8-f31c1cec766c | -10.88134 | -46.85981 | 2025-06-05 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4ed0682-3151-3cd9-8d67-75ca0ba574d4 | -11.37516 | -55.11669 | 2025-06-05 04:59:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da5ae841-aae7-346e-a6a4-95628f57201e | -10.85278 | -46.85945 | 2025-06-05 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d327698-c59b-310a-b372-16c9e85d8dea | -7.54475 | -45.82642 | 2025-06-05 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 582c53c2-437a-3966-9d43-4288f5648ce9 | -10.3073 | -57.14088 | 2025-06-05 04:59:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67716a2c-fd2a-387b-a040-3e9205c9d60e | -10.4958 | -53.658 | 2025-06-05 04:59:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8110959-d3d3-3e01-b24c-8f07dc9ce789 | -8.96172 | -47.97015 | 2025-06-05 04:59:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c6400655-db89-3e36-98bd-c279f85d40d8 | -7.62362 | -45.7548 | 2025-06-05 04:59:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9d88f9f-80a5-3c00-9b0f-8422b1d35c5b | -9.24882 | -63.29101 | 2025-06-05 04:59:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ad346b20-b66d-3704-b534-3e50ff117c8e | -6.98395 | -47.08592 | 2025-06-05 04:59:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a70e831d-f3d7-341f-bbdc-f5362ece255c | -10.69405 | -57.64964 | 2025-06-05 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea99051c-cf71-32b8-a411-00d5586a3312 | -10.21172 | -54.29789 | 2025-06-05 04:59:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b20a3f73-4368-31d4-a2ef-47a0e40466d0 | -9.39002 | -48.409 | 2025-06-05 04:59:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9fd12d7-4cc5-3189-9585-7623511109aa | -11.29967 | -53.98723 | 2025-06-05 04:59:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e0f08e2d-a17c-3fa0-a966-cda20464b76e | -9.48312 | -45.45534 | 2025-06-05 04:59:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05f3a227-80dc-3338-98e3-fdf57a5a254d | -11.45118 | -54.09299 | 2025-06-05 04:59:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 027db1fe-d913-3bc7-a422-d17985073c7d | -11.45075 | -54.08955 | 2025-06-05 04:59:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 356a10fe-4c43-3efb-a652-9fabd967ef09 | -9.60464 | -63.21966 | 2025-06-05 04:59:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f72d735-f9f7-3f20-b2ee-159ef309be20 | -10.65217 | -49.43376 | 2025-06-05 04:59:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8e0e3d75-0752-3cbc-affd-cc616289fd9d | -10.53757 | -56.3865 | 2025-06-05 04:59:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec54401e-094b-321e-9562-7c6e5f5fe5f7 | -9.5026 | -57.14485 | 2025-06-05 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b79c12d-6cd5-35df-93cc-6a0961a3145e | -10.64737 | -49.43713 | 2025-06-05 04:59:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 96b21dae-5372-3c24-b62b-bbcbaeb2f997 | -7.90236 | -50.35803 | 2025-06-05 04:59:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b9abe6ae-056a-33bb-9eee-c8695210322e | -10.30385 | -57.1403 | 2025-06-05 04:59:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cc83f13d-1eb9-3b76-81c3-6aad919b4e86 | -8.46507 | -46.48464 | 2025-06-05 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eebbd0e5-4997-3133-85e6-e6400b317708 | -8.46429 | -46.48515 | 2025-06-05 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0571c009-1caf-307d-be28-3c45bd2c38bf | -10.49692 | -53.65064 | 2025-06-05 04:59:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5546bd55-f80e-350c-ad83-8e5e6d0881c0 | -7.61924 | -45.74773 | 2025-06-05 04:59:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 31e6cb3a-7585-3b98-a172-b0e977f7c43a | -7.01298 | -44.59566 | 2025-06-05 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e898894-e488-3e3c-9a46-e635b086042f | -7.01553 | -44.59126 | 2025-06-05 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6bbd0c85-e05c-32d6-9f2e-9867c8df2dd1 | -10.76115 | -54.7833 | 2025-06-05 04:59:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a04f36e-5322-3e1b-96cc-8c92e2d6a2de | -11.13188 | -54.21768 | 2025-06-05 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7f706f8-4bf5-3034-ba93-df5c21f5c403 | -10.8155 | -56.95774 | 2025-06-05 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4bdc11bb-8c3f-3fd9-9875-eb4a52da5a5e | -7.70061 | -45.77928 | 2025-06-05 04:59:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fafd21c-b838-32b7-a73e-9ba5162c3f42 | -11.43325 | -54.99902 | 2025-06-05 04:59:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa3a05e5-d524-3172-a521-8589b61b7951 | -6.97891 | -47.08368 | 2025-06-05 04:59:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5c9689f1-b32f-37d9-a134-af7136a49337 | -7.70146 | -45.77294 | 2025-06-05 04:59:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6336271-79c4-3329-9874-3cbc40505dae | -7.01391 | -44.60275 | 2025-06-05 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a78ace3-144a-367e-bd57-5c9b7483f00b | -11.43552 | -45.10386 | 2025-06-05 04:59:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 68d203f8-1380-33dc-8599-70d8945c06f7 | -11.07276 | -55.03904 | 2025-06-05 04:59:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 24ee2f41-0c7a-3fad-b268-c267636b84b2 | -7.20005 | -43.13347 | 2025-06-05 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c0422b04-99e0-34c5-b8ca-87946b03f4e3 | -10.29635 | -57.14291 | 2025-06-05 04:59:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0255896d-c1f0-3f1b-b384-da95e3fb4937 | -7.21846 | -43.13052 | 2025-06-05 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a3dca478-c78d-3ac9-8b9a-b63ccf7c4119 | -10.05402 | -49.66317 | 2025-06-05 04:59:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f0f94c9f-a575-3704-a771-49b0ce7d88b5 | -9.24326 | -63.29294 | 2025-06-05 04:59:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fab8ef43-555b-302d-a685-ebad0a0ebf99 | -10.81891 | -56.9583 | 2025-06-05 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1098c306-c307-324b-be27-83f28a26c6f3 | -10.85168 | -46.82886 | 2025-06-05 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3dba8916-220f-3814-8462-7b7a9501c22a | -9.41199 | -62.45299 | 2025-06-05 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3bcf7075-d204-3454-9a18-7fa9b453e638 | -7.70104 | -45.77611 | 2025-06-05 04:59:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04b0bf7e-33b6-3e00-abfe-e06f89ccf2ca | -7.19874 | -43.13706 | 2025-06-05 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| fde3c5bc-3bc4-3682-b8af-fa73ae04219f | -8.72633 | -47.98837 | 2025-06-05 04:59:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 016f943f-62d2-3866-972f-54e31b41d720 | -8.46003 | -46.48398 | 2025-06-05 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1bc4637-210b-374f-bac0-615f1540e903 | -10.7606 | -54.78682 | 2025-06-05 04:59:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9ff1b0b-644f-3022-814f-47f664890496 | -7.90621 | -50.35862 | 2025-06-05 04:59:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| aae65c94-1f69-3bd5-b6f1-56c36f611fe6 | -8.73089 | -47.98902 | 2025-06-05 04:59:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 560ca1e8-fb6c-36ca-9571-9d9456e10321 | -8.94722 | -47.30245 | 2025-06-05 04:59:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2cb1eecd-2a26-362c-8a67-7541eb11e5e5 | -11.13918 | -53.94072 | 2025-06-05 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a4db714-bc24-34b5-b5ee-8b48b6075f0e | -7.01444 | -44.59897 | 2025-06-05 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8392844c-15ab-32af-a9bb-42f1011cba7a | -11.40985 | -54.71971 | 2025-06-05 04:59:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b9cf6b4-d5d0-3bd4-968f-5ff76bb52d56 | -11.54791 | -47.31784 | 2025-06-05 04:59:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5872084f-b242-3173-b0d1-aa7bbec542db | -6.98291 | -47.08937 | 2025-06-05 04:59:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ae1086c-1255-37cb-94cd-674946638bb2 | -11.83004 | -51.28318 | 2025-06-05 04:59:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84b14515-eca5-3899-ad89-d7b505361533 | -10.69056 | -57.64903 | 2025-06-05 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4cdf11da-6c2a-30fa-8443-64efd2fe4200 | -7.01351 | -44.59169 | 2025-06-05 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 559b8550-a591-3597-9ec6-3554b4eeceb4 | -10.93751 | -55.33462 | 2025-06-05 04:59:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ec79b5c6-20f7-3426-8538-c22b50f80118 | -7.90798 | -50.3618 | 2025-06-05 04:59:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 3ba5079e-ff95-315c-8f04-9a911b660617 | -8.6879 | -48.29634 | 2025-06-05 04:59:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README14.md)
