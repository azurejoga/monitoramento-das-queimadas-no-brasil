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
| 202baa48-4855-3f34-91fc-e4f164c9a590 | -12.70626 | -48.14484 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45f77a42-b4dd-3811-9355-1c0fe7026d85 | -14.00765 | -44.59454 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 214f9c44-447f-3e7d-b3e3-0e46150c1f12 | -11.83036 | -46.45628 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 42f0f107-f981-3e03-a145-0f1d6fcb0bf4 | -11.32866 | -43.62427 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6319acd8-37cb-34a7-bb8f-a6290bff74fd | -11.14465 | -47.152 | 2025-08-30 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d890c87-3a10-3e3e-8180-90cbe7e34613 | -12.83081 | -48.09216 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6ac0a811-3b84-3f35-9c3c-57cfc79839c5 | -14.00248 | -44.58208 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7e6304b-e046-300f-83f4-91874249bd08 | -13.47294 | -46.95408 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c0a4eb3c-ce50-387e-908b-cb4fb0b1c164 | -9.57961 | -54.49689 | 2025-08-30 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c7011b8-3048-3540-80ad-0728c73d3e55 | -13.39065 | -46.95897 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b61d44fa-b6de-3ee2-bde3-37242cf4d95a | -9.22407 | -46.75416 | 2025-08-30 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0351af4a-6697-3e27-add5-5fda936e695a | -10.84654 | -53.77167 | 2025-08-30 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80c3c7a8-6ecd-3a42-9e67-8199c8ebf979 | -10.0247 | -48.08623 | 2025-08-30 04:21:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c831d9f-faf8-3a3c-b8e4-f9b51b4cafa2 | -11.88167 | -46.38895 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e5399eaa-5225-33e4-8fcd-9a36f83966c3 | -10.36531 | -59.20696 | 2025-08-30 04:21:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0e480114-fbf3-33af-ae12-8321de469cd7 | -13.50127 | -46.83915 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8503ae8a-60cf-3926-8995-cdcbb4415cdc | -11.85689 | -46.39569 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 37ebad3e-b49b-39bf-9415-d6a9cf7c546d | -13.36648 | -47.02445 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 799e5c77-76bb-3b55-adc0-85b42d44bade | -10.1981 | -48.47108 | 2025-08-30 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26811143-01bb-3fdc-817f-8e16575aca9e | -11.36048 | -43.57739 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 725ff517-9dff-30fd-a905-b45cfa5c7c47 | -11.272 | -44.92807 | 2025-08-30 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 605543fe-db94-3c21-894b-66bb6d7f28ca | -12.85213 | -48.15439 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b994906c-cd69-37ca-a6a6-5a612fb6dfad | -10.80859 | -46.35465 | 2025-08-30 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a7d1d26-efff-3f59-88d5-586b13497f00 | -11.15249 | -47.14591 | 2025-08-30 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bc6dc618-7642-3117-8b0e-1318540a8ef7 | -13.47181 | -46.96125 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e592356-4c53-3377-9d1c-3a03dd3956b2 | -14.02632 | -44.49174 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ce11edc-f7c0-3b41-90d6-567c50176acc | -13.62782 | -48.18676 | 2025-08-30 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| db4721a8-60b5-392e-8b72-9db0c9001a92 | -13.99993 | -46.32647 | 2025-08-30 04:21:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1dc64fb5-6e7b-31ed-832c-6512607c55d0 | -11.31012 | -43.6055 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 75c91208-58e4-38af-8865-7809d5f4cf17 | -11.15667 | -48.29389 | 2025-08-30 04:21:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60178b8f-a683-3e87-9813-cbfa8cf0390f | -11.83006 | -46.86522 | 2025-08-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3658e324-f9a2-3671-9519-d8a75f59e7c9 | -11.32461 | -43.62765 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7f186930-ea5a-3694-9a30-a8e3a733f296 | -13.41759 | -51.82126 | 2025-08-30 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 770b9647-1df7-3398-93cc-8fbc8e2c4132 | -10.65045 | -48.6558 | 2025-08-30 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 65ee8594-26c0-3ab0-8bde-aba0cc78dd0b | -12.41287 | -46.47233 | 2025-08-30 04:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b010b8e5-497e-35f9-a283-34b650e4842d | -10.67379 | -47.07158 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a41b29f6-d8dd-3aca-b91b-342b0346efa3 | -11.88773 | -46.39354 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 216d5195-cf84-3ec1-a3f4-f2dce13aad25 | -16.26737 | -43.61657 | 2025-08-30 04:21:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e3df7245-5656-3b84-8ed8-51b1911804ea | -9.69655 | -47.05326 | 2025-08-30 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1608034-d5c1-3c2c-bb28-2ec6e4b3078d | -13.96799 | -46.33578 | 2025-08-30 04:21:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17ffae40-fd3c-36cd-a8c2-60d48614908d | -14.00136 | -44.58967 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 518159c1-68a5-330e-a348-8431cdfae0f3 | -13.62661 | -48.19414 | 2025-08-30 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f425f619-d96f-385c-a176-6b3151a4270f | -13.40199 | -46.84465 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bdfdefbb-42b1-3836-b281-dd5f47bb0deb | -10.95003 | -44.83374 | 2025-08-30 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 69ac08f8-bd52-3c6c-ac96-fad1f5af5c7b | -11.14857 | -47.14895 | 2025-08-30 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c2043c24-afed-320d-9ac8-7a81caf6c31f | -11.00696 | -46.86156 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6ca230c9-0f07-3a9b-a19b-c5e913727830 | -11.83256 | -46.46385 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 10b2da87-36fc-32ae-867e-564ef702879f | -11.93006 | -46.68599 | 2025-08-30 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aeae3135-4bc2-3fa0-9369-ce4394c39566 | -11.86461 | -46.38974 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0ff97c2a-0b9d-315f-a79b-4d1ba9589481 | -13.38927 | -47.03168 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f484ea5-0031-3165-a281-2b66bb46c4ed | -12.29337 | -42.00475 | 2025-08-30 04:21:00 | NOAA-21 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 97ea938c-1a92-3bd4-8347-92ddc8f0bbe5 | -12.71872 | -48.19732 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f93b824-984f-342d-8eca-d069c742bf4a | -11.8359 | -46.44274 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0cd33bf2-893a-3abb-80f1-aed11eb13372 | -11.85745 | -46.39217 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| edba8391-ddd4-3345-9c99-a23740cfcb33 | -11.86791 | -46.39028 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 65a82cf3-2309-3d1a-9c2e-bce0eedf57c6 | -11.92231 | -46.69199 | 2025-08-30 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 24e17966-55cd-3cca-808c-e7db2cc4319f | -12.85302 | -48.12734 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14f3bc69-1eaa-37d6-a326-6411eea26e3c | -11.84581 | -46.44435 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 68e5fea8-92dc-39c2-abd1-d66304264ffa | -12.79959 | -48.17636 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f4a7c8e-31ee-3056-bc80-380c52a7f645 | -12.66136 | -48.1838 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e68d5e1-2dda-34a5-abfd-dbc1dae884ef | -13.38717 | -47.00216 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ab4c30c2-3c20-33f4-b087-56bd74b088ab | -12.71314 | -48.18853 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ac46b49-e646-38f2-ac7a-fd152bc412f7 | -9.85839 | -44.59342 | 2025-08-30 04:21:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4dfe9011-f125-31a8-bbeb-c2339525a445 | -16.81056 | -41.75053 | 2025-08-30 04:21:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f9bce0f7-9d51-380f-9894-a3d79baaa759 | -11.07819 | -52.03247 | 2025-08-30 04:21:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| baeda0fb-c0b9-3086-81e0-5d9d3355ef44 | -14.00646 | -44.57883 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17153768-4e50-30ea-9e89-864aee4f5dc1 | -15.31058 | -46.09292 | 2025-08-30 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05816150-8af7-3ab4-8b67-a320d638f300 | -13.36704 | -47.0209 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 41a0c50a-48a2-37ee-be54-4c850f84462d | -11.35933 | -43.56117 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d1b26fb-21f2-39fa-9509-067817ca522e | -14.62647 | -48.07785 | 2025-08-30 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 448e1825-86a0-3a8d-969b-a29eeb14a57d | -11.4147 | -46.91002 | 2025-08-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b502636d-437d-3d1c-b7d4-b30839e96cca | -9.22073 | -46.7536 | 2025-08-30 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b18ade65-1623-335a-9343-0124307f7557 | -12.93606 | -48.11419 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0abdede-4170-30bb-aab3-9eb06f60369e | -11.07225 | -44.60983 | 2025-08-30 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6df9e318-844a-355f-b78b-78365bf041dc | -13.37496 | -47.01474 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 19f66e6c-dcc2-3e54-a960-0e21123797ab | -10.37695 | -57.83575 | 2025-08-30 04:21:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 98e3c0a9-96c0-3495-9f92-9d49eb6b49a6 | -14.02525 | -44.54663 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c21b9b10-1866-3105-982b-1fc943613a9c | -11.34308 | -43.5266 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d3eb8bb5-408e-33c7-86e4-7e53cadfd177 | -10.03007 | -46.02707 | 2025-08-30 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13aa5fc8-737e-3cdf-a5e0-389261bbf935 | -9.69319 | -47.0527 | 2025-08-30 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8054ed1b-18ec-3ffc-ab99-41d8cc086743 | -11.34425 | -43.59095 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f075f64f-92ab-3aef-9a0e-b546b0868d42 | -10.37338 | -59.20218 | 2025-08-30 04:21:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96b969b1-925c-3efe-aced-da71e9dfb909 | -14.51118 | -52.99261 | 2025-08-30 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0bfda3da-2206-3ba3-b2fa-8197da7084ef | -9.58825 | -54.48434 | 2025-08-30 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fffa13dc-f72b-3957-8b45-dc0a3b1b7c5f | -14.83895 | -46.76956 | 2025-08-30 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69acc92c-67c7-3211-b166-796e424cf87a | -9.15263 | -59.56506 | 2025-08-30 04:21:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c9f0db17-76ea-37c8-852d-95b6dde7ec4f | -11.83864 | -46.4468 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 7df78de1-2dbf-34ce-a0d9-6c6ef788382c | -11.92315 | -44.24252 | 2025-08-30 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af95545a-8566-3b69-b4b0-5df25f8b6825 | -12.92928 | -48.11302 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd7488aa-639a-35a6-9ce0-76cb32f377f4 | -15.08083 | -48.62896 | 2025-08-30 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0dd9d769-603e-349d-b89f-30ce526698fc | -11.90237 | -46.71049 | 2025-08-30 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80d817d4-7bf5-3a77-a2bb-b17c45c9b0b8 | -10.01928 | -48.05364 | 2025-08-30 04:21:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00f0f176-389f-36d9-b3ef-ea4a28f2ed6b | -11.86573 | -46.38268 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff9b2c50-fdd9-3ff9-9d93-1a0aac26a506 | -11.07747 | -52.03659 | 2025-08-30 04:21:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb87252b-1069-3ac3-997d-bb0ef846edbc | -13.49851 | -46.94373 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1a34b5b-2bed-33b2-b4d4-ef5ec9228445 | -11.36454 | -43.574 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 504b5038-81a3-3bac-a67e-ea67ce887b4b | -13.98395 | -46.32025 | 2025-08-30 04:21:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2363baa-615d-3c0b-b06c-8b76089803bf | -12.40185 | -46.47776 | 2025-08-30 04:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0d3ec22-edc2-33bc-a80c-58065a1aff4f | -13.36079 | -46.86701 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fcafdc89-eff2-34fd-8d86-3a9aa139aa43 | -10.99296 | -46.8448 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README32.md)
