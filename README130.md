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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad46050e-4049-35b6-9350-0391ead1f9bf | -14.45241 | -43.94104 | 2026-10-10 05:06:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bf55f94a-767e-32f1-b783-098c1a918b5e | -6.48636 | -62.85377 | 2026-10-10 05:06:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0daa9c63-14df-3a01-b97d-eb3e674d1136 | -13.72231 | -49.1317 | 2026-10-10 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 582fb633-5e1e-347d-a6e5-74f1cdb0c41d | -9.73996 | -57.36428 | 2026-10-10 05:06:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1997c59-afd4-351c-881d-10e9db52e8d7 | -8.50137 | -54.61479 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2192401b-9010-3f39-949c-bb47b89f91dd | -11.50504 | -60.5528 | 2026-10-10 05:06:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7c150548-5f86-330f-9be3-c8b32c09b9bb | -9.93171 | -44.78688 | 2026-10-10 05:06:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60a5e4e0-6c2a-3c80-b207-8b57fe7ecb63 | -11.9965 | -43.45022 | 2026-10-10 05:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 44492368-9f54-3e17-815c-5365a6c65cfa | -11.384 | -55.15966 | 2026-10-10 05:06:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e7a739c-74b8-3b63-8995-c141e8a5245d | -11.9944 | -57.61228 | 2026-10-10 05:06:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c614149-43da-3a44-8e23-8133b465a8c0 | -12.26733 | -44.75801 | 2026-10-10 05:06:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b1c7f17b-9471-3d52-97fc-08805460d172 | -11.08032 | -44.12012 | 2026-10-10 05:06:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27475611-10ee-3f1e-8dd5-ac5fbea1853e | -11.03583 | -44.02584 | 2026-10-10 05:06:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a48df519-4796-30c7-a0a0-9365f74985d3 | -10.60532 | -60.48641 | 2026-10-10 05:06:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 353c1c29-e87f-3469-a12b-086f6547d463 | -11.02164 | -49.09418 | 2026-10-10 05:06:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db479b55-2545-3dd8-a29d-b9fe6d2dc60d | -12.36069 | -46.5924 | 2026-10-10 05:06:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6aa157c3-10f3-3408-a421-bca76ce7a479 | -11.90503 | -55.90256 | 2026-10-10 05:06:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 228e85f7-ca8c-34b0-a0aa-01e1ed19c440 | -7.91455 | -54.71652 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b52f960a-ae0b-3f32-a728-8d8a25e350a2 | -11.3759 | -54.03182 | 2026-10-10 05:06:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11b55195-fde0-303e-a387-6e25a7ccf105 | -7.92999 | -54.72609 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6035a8cb-c501-36d8-b3e4-bd6abf4aed47 | -9.21396 | -45.66051 | 2026-10-10 05:06:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bdee56b8-2572-3b48-ab67-6bb6b855a09c | -8.98364 | -47.54179 | 2026-10-10 05:06:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38dd9c62-e67a-3027-86dd-9995962759bc | -9.94298 | -44.88338 | 2026-10-10 05:06:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef9f9ecb-ec98-3f8c-816b-d97253d11a3e | -7.9118 | -54.73385 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 254eff9f-0c14-3dd7-95b2-ba6dbc6d54c2 | -8.26124 | -54.67289 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d40cc63c-afb6-3fb1-9a4c-b2e9a34a4409 | -14.73057 | -48.21487 | 2026-10-10 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b864be83-421e-3edc-b7bc-9927b1c0f84a | -7.56986 | -61.54562 | 2026-10-10 05:06:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19ca4205-25dc-3fb9-bc78-f9617482779d | -13.72749 | -49.12756 | 2026-10-10 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f73b7bad-c3a2-37cc-b0aa-d6f231a3d9d3 | -13.14961 | -54.3618 | 2026-10-10 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f77a35b1-e9a9-35dd-864d-46b287f7b6bb | -13.25352 | -42.25973 | 2026-10-10 05:06:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ee16b981-14bb-33d3-9d03-84ab96208be2 | -9.31407 | -47.37763 | 2026-10-10 05:06:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6244b1ae-aaa0-3d58-9434-7309cf883a39 | -9.7639 | -53.87902 | 2026-10-10 05:06:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb900cf6-ed02-342a-8323-358256853908 | -12.25793 | -44.75926 | 2026-10-10 05:06:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b713c98d-48ed-3f44-aa2e-1ad57e9fd762 | -12.77331 | -44.88528 | 2026-10-10 05:06:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a75a836-60c1-3db4-8e56-e732e9ef2391 | -8.17362 | -55.20356 | 2026-10-10 05:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b903a650-36f9-36fc-a6a6-a279f2fea11f | -7.88699 | -54.71924 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ea40461-62c6-3d98-a283-05380b66f55f | -7.91069 | -54.71946 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1810631b-1631-35e6-ab32-9554ff9711fa | -10.5966 | -60.48859 | 2026-10-10 05:06:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 126e29b3-58cf-3fe3-b4f4-ff0ebf3db9db | -12.29352 | -63.38323 | 2026-10-10 05:06:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9612cfb0-0fbc-3803-bc25-5ad33af251e8 | -13.52945 | -47.41921 | 2026-10-10 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71c073b7-c35d-3ea3-8e72-203c42023fd5 | -9.9603 | -55.33435 | 2026-10-10 05:06:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5953685f-7903-3d0a-9672-301946397e10 | -11.84108 | -46.81461 | 2026-10-10 05:06:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 987f03ed-a10d-3a87-8f8a-b7fded306d48 | -14.45245 | -43.94776 | 2026-10-10 05:06:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ce243252-7a62-3715-9df4-ed369394a72b | -12.09783 | -57.15234 | 2026-10-10 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d404902-0c39-35b5-a2e7-424a5e9613c6 | -12.30149 | -47.0476 | 2026-10-10 05:06:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 483b6dcd-561d-3b35-92a5-e7caf903eeac | -14.44717 | -43.92934 | 2026-10-10 05:06:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 361117ca-1e1f-3ea8-880e-59eda5cd113a | -10.60318 | -60.47497 | 2026-10-10 05:06:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| de97cab4-370f-3bec-a99f-c027c092d5cf | -12.36026 | -46.5957 | 2026-10-10 05:06:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d988cf70-e442-367b-9462-df6d3ef8372d | -8.25301 | -54.72495 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f2e5b78-8a53-3de7-a6f7-33d585582e66 | -9.51789 | -54.67358 | 2026-10-10 05:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9039ecca-09b1-307f-9d20-5a8ce5ef8008 | -13.35365 | -43.93057 | 2026-10-10 05:06:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c824bea0-8016-360d-bffb-7b1eb9969504 | -12.22702 | -44.6902 | 2026-10-10 05:06:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d8f43e6c-5213-33f5-a841-893b35f5dfef | -8.3038 | -54.70456 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d96871e-2fe6-3279-b375-42fe88d443e9 | -11.77504 | -45.49976 | 2026-10-10 05:06:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b73e3ecd-aa75-340b-8108-c5daa54c82d8 | -8.50523 | -54.61184 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b13e0132-0269-3bc4-9603-750f9c78040f | -8.22374 | -61.1786 | 2026-10-10 05:06:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9c135ef4-bf8a-3c59-b6f7-7310820080ff | -8.58422 | -53.10254 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37e0c57e-bb5d-37b3-86ad-dba1b0369938 | -13.7758 | -48.12964 | 2026-10-10 05:06:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 996c9316-d909-351e-b655-31b77e6e0aef | -9.95486 | -55.11177 | 2026-10-10 05:06:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef72de8d-e34f-3a7f-a906-322c1c563b1b | -9.95699 | -55.33382 | 2026-10-10 05:06:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43d6ace3-35d3-3933-acc9-770525ce364d | -9.26779 | -47.43002 | 2026-10-10 05:06:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6aaeabb-5057-3b10-8287-61b1bdf6e336 | -8.30104 | -54.70057 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7855d248-e76b-37dd-b448-f73ca7617d73 | -8.32583 | -54.67248 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5873a324-d614-3839-9b66-67b8d0195ea1 | -14.11226 | -49.87221 | 2026-10-10 05:06:00 | NOAA-20 | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb68bd2b-9d69-37de-b5b0-d89120a90471 | -14.45706 | -43.9581 | 2026-10-10 05:06:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 219fe520-5b50-385d-a4a4-3a890acf24da | -7.91787 | -54.73838 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc25d27a-a535-3d07-957c-df9aaa3b753a | -8.6493 | -54.53883 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0562cd0c-862f-39e9-b2f1-f718fc8219ce | -13.22659 | -54.15264 | 2026-10-10 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 66156b4f-f371-3569-a2d2-656d47d7ecfc | -7.91676 | -54.72398 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d168b56-588e-3286-82f4-9c2de06c90f3 | -8.69829 | -62.42104 | 2026-10-10 05:06:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac7fbb5d-27a3-3158-94c4-b240c969cf57 | -8.24253 | -54.72684 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9e46ff2-9326-38c2-8f96-e93aeaa0434f | -8.65371 | -54.53238 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 566aa866-922a-3f71-8b07-96ed0d59759a | -8.17031 | -55.20303 | 2026-10-10 05:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e1568341-0ead-3966-a01d-4a78e50411a9 | -12.29449 | -63.37803 | 2026-10-10 05:06:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 631ecca9-d2b1-3191-9ee5-fe8f348468b9 | -13.15299 | -54.36233 | 2026-10-10 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d86dad81-33d9-323f-8493-c3daeac1592b | -14.72854 | -48.21259 | 2026-10-10 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 389ec047-4fca-32e7-8e67-6ddfc126d8aa | -7.94898 | -54.75791 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82db34e1-426b-39d4-9240-decaa571150d | -11.59863 | -43.74599 | 2026-10-10 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 72f409d4-8643-3bb5-b47d-750667e69037 | -13.25866 | -44.00713 | 2026-10-10 05:06:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64d79777-569e-360c-847c-973d32011251 | -9.75495 | -53.87019 | 2026-10-10 05:06:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc8bfe20-9fbf-3de1-8d77-0b3bce169a20 | -12.28878 | -63.38226 | 2026-10-10 05:06:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0670d5d-6476-3364-9515-3f54ddc8a6f4 | -7.90132 | -54.71442 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da5ffec5-af20-347d-ac50-b6e86961f987 | -10.45489 | -47.8452 | 2026-10-10 05:06:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8d53ec63-3d58-34c7-a107-2093cf76e461 | -8.51784 | -67.03181 | 2026-10-10 05:06:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 242860f4-50b4-34b6-9793-516839d07361 | -7.75511 | -54.95113 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4347a5b6-fa2a-3c37-97e2-329789094825 | -11.45713 | -43.37928 | 2026-10-10 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86bd4f1b-386b-30ee-a586-a39a44c1b615 | -11.37646 | -54.02816 | 2026-10-10 05:06:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31ee6800-a942-3aba-a8f0-94249c98f255 | -13.52489 | -47.42825 | 2026-10-10 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 264fd351-c433-3b73-8e1a-a27b6e56d18f | -9.88117 | -50.51566 | 2026-10-10 05:06:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d10ed22-6d8b-3a9b-b959-60057c0c4170 | -14.45947 | -43.93623 | 2026-10-10 05:06:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2a9095a8-f389-3330-afa1-a648818e973d | -8.50468 | -54.61531 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21997c75-3686-3348-9e63-4f3187f9a29f | -11.79589 | -46.71062 | 2026-10-10 05:06:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 712b1583-ed90-33c6-a436-c7180929d58c | -8.95729 | -47.3808 | 2026-10-10 05:06:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f73b425-4287-3287-845f-9ad69637c08f | -12.37764 | -46.57838 | 2026-10-10 05:06:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b978cd7-596a-3d7c-8aa1-bc302d32226e | -7.56251 | -62.33017 | 2026-10-10 05:06:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2e85ae2-b0b6-3572-aa67-a46c47235bcc | -13.09861 | -46.35977 | 2026-10-10 05:06:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9741fc23-8970-3f2e-90c7-299d82e6b8f4 | -13.6787 | -49.11107 | 2026-10-10 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dc16438c-18a5-3266-aae4-a5cee644570b | -14.05622 | -43.83438 | 2026-10-10 05:06:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c18c0d44-8462-36e4-8a1f-5d7a4b07ae7a | -11.92741 | -46.76824 | 2026-10-10 05:06:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 665e7bf6-1b2b-3628-a7b9-b000b2411ded | -11.98694 | -57.61486 | 2026-10-10 05:06:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README131.md)
