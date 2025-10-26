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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 646431ae-2894-34cb-a03c-640361c12843 | -23.46324 | -47.01035 | 2025-10-26 12:02:00 | TERRA_M-T | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| 8b35811a-3959-3efd-87b1-6e39fc700a0f | -18.46333 | -47.16579 | 2025-10-26 12:02:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8304d1e6-8e12-34fc-b302-a18d8a4279ed | -17.32164 | -43.64913 | 2025-10-26 12:02:00 | TERRA_M-T | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 206.2 |
| d3b8c2a3-a676-3491-a2a3-aa07d71c5f88 | -18.61208 | -46.05189 | 2025-10-26 12:02:00 | TERRA_M-T | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 5f46a0a1-fb47-3317-8988-3c73c157ca46 | -17.41268 | -46.72522 | 2025-10-26 12:02:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| edeaf643-bdb5-3b77-a127-c4b7ccd48140 | -20.30168 | -46.42312 | 2025-10-26 12:02:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d5640523-0ccb-3352-8e64-100762184d85 | -19.64097 | -44.79165 | 2025-10-26 12:02:00 | TERRA_M-T | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 439e6c00-493a-310d-8654-1e5d92f0f072 | -17.42569 | -46.87608 | 2025-10-26 12:02:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 6bd967ac-0442-39dc-a01e-968e53882b7c | -23.46183 | -47.01994 | 2025-10-26 12:02:00 | TERRA_M-T | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| c27b0895-cab8-3ce3-947d-2b9378e36767 | -18.47253 | -47.16715 | 2025-10-26 12:02:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e47d5bfe-dd15-315f-b3e6-9b790adbc474 | -19.35181 | -45.59334 | 2025-10-26 12:02:00 | TERRA_M-T | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1007db4d-4a8b-3a3c-ac62-9cef634b6d90 | -22.05635 | -44.28718 | 2025-10-26 12:02:00 | TERRA_M-T | LIBERDADE | MINAS GERAIS | Brasil | 3138500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| bbeb7f85-89af-396d-a88c-bfe551a33bca | -24.68343 | -49.62192 | 2025-10-26 12:04:00 | TERRA_M-T | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 33e78c27-33f0-3b58-ad1b-f9abdac58e05 | -24.68534 | -49.61033 | 2025-10-26 12:04:00 | TERRA_M-T | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 026c0393-d98f-386a-884f-81b42fc05193 | 1.6203 | -55.7457 | 2025-10-26 12:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 2c95a878-62c1-33a0-857b-916dd6a7cad6 | 1.6203 | -55.726 | 2025-10-26 12:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| c5a2c598-965e-3d80-9fdd-c9707fbaa388 | 1.6203 | -55.7457 | 2025-10-26 12:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 5b7d0883-3349-306b-9b40-f06344093623 | 1.6203 | -55.726 | 2025-10-26 12:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 235331c7-1512-3432-815f-8a81a48e5eeb | -17.3165 | -43.643 | 2025-10-26 12:20:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 7690d2da-a331-361a-af5e-ed7ab56373c4 | -15.8352 | -53.5798 | 2025-10-26 12:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 153.0 |
| 5c5ca23c-b0fd-384c-8659-90506aeee546 | 1.6203 | -55.726 | 2025-10-26 12:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 1d159cdf-b161-3b7d-8982-7307cc89d82d | -17.4311 | -46.884 | 2025-10-26 12:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 47bbda72-8014-3f76-b53f-43eac6f59bc3 | -14.6313 | -48.389 | 2025-10-26 12:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 106.3 |
| b78757e3-f854-303b-a20d-2dcc4b995791 | -17.3365 | -43.6383 | 2025-10-26 12:40:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 43460024-3ab2-37f1-8eae-cf8921730fc4 | -14.6313 | -48.389 | 2025-10-26 12:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 995295da-6f3b-3730-aa48-eafe37f631e3 | -17.3165 | -43.643 | 2025-10-26 12:40:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 197.5 |
| 6d49f592-cab2-3c19-96b5-c9eed2cfd3a7 | -17.4311 | -46.884 | 2025-10-26 12:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 95.0 |
| e3fd0cf7-71ad-3d20-90eb-bb679969f638 | -17.3365 | -43.6383 | 2025-10-26 12:50:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 44bfff69-26e9-3bec-9cc5-7966a0ab15d6 | -17.4311 | -46.884 | 2025-10-26 12:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 4fedaddf-d00c-357f-babc-ed018c32cec5 | -12.0482 | -46.3989 | 2025-10-26 12:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 139ff138-0216-3ece-ba32-86ff65f34e1c | -12.3634 | -48.1016 | 2025-10-26 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| cf6e5d66-e4a5-3ff7-ac8c-f5eacfa25b48 | -15.8547 | -53.5771 | 2025-10-26 12:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 129.4 |
| b0233946-2106-3015-8ed5-9b18ae15a999 | -15.8352 | -53.5798 | 2025-10-26 12:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 7e4db079-e8e9-3274-a449-187b5f9cd588 | -13.547 | -49.5434 | 2025-10-26 13:00:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 118.3 |
| c0c92399-337a-3421-9c0b-d3deaffa9f47 | -5.4673 | -37.8536 | 2025-10-26 13:00:00 | GOES-19 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 282.8 |
| d61aa3da-3bc8-36c6-b9c5-c90e50443622 | -15.2649 | -50.7535 | 2025-10-26 13:00:00 | GOES-19 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 6c891840-8df1-3877-910b-9328f89d1016 | -5.4676 | -37.8278 | 2025-10-26 13:00:00 | GOES-19 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 109.4 |
| 8b909e0c-8865-371d-98ab-19c5f3f4e87f | -17.3165 | -43.643 | 2025-10-26 13:00:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 149.1 |
| a82ae0b9-4b04-3283-bc4b-2076b7ff002e | -15.2454 | -50.7564 | 2025-10-26 13:00:00 | GOES-19 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 39f9171f-1c69-326c-96ea-cb0ed0289358 | -14.6031 | -53.1087 | 2025-10-26 13:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 90.5 |
| ce2eb12d-3d55-3c9d-8cbe-2d1f943b6778 | -17.3365 | -43.6383 | 2025-10-26 13:00:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 1002d449-9008-36f6-8d4b-f4dacecf7870 | -12.3169 | -47.4631 | 2025-10-26 13:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 7607eb6d-50c8-39e2-9d22-aa0f3412b2ba | -15.2454 | -50.7564 | 2025-10-26 13:10:00 | GOES-19 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 2cb78272-ef1e-3e56-a4b1-077720328bf9 | -17.3365 | -43.6383 | 2025-10-26 13:10:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 17660dd2-ff47-3231-a577-99e1c9e9d486 | -12.2977 | -47.4658 | 2025-10-26 13:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| ed1ba81a-dd5e-39c4-b673-bc29834d724f | -13.056 | -45.9059 | 2025-10-26 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 409dc477-5b4a-3836-82da-a3296f5e54ef | -13.2482 | -47.9768 | 2025-10-26 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| af643c9b-22bb-306e-8a32-35db2143dfa8 | -17.3165 | -43.643 | 2025-10-26 13:10:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 275.0 |
| 555d7de0-1f49-3f8c-a648-d22a92fb6994 | -5.4676 | -37.8278 | 2025-10-26 13:10:00 | GOES-19 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 147.9 |
| 88bddd6d-3cae-341e-8d3c-4c9c14be6338 | -16.1901 | -45.0841 | 2025-10-26 13:10:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 165.2 |
| a7da8c1f-f556-39c2-af31-cb06bfb2cb42 | -3.85 | -42.7114 | 2025-10-26 13:10:00 | GOES-19 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 2a32864c-3ed2-3802-8321-49f132b93dd6 | -3.964 | -45.4173 | 2025-10-26 13:10:00 | GOES-19 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 698597df-930b-35f1-b887-2e201509429b | -3.0148 | -41.6851 | 2025-10-26 13:10:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 106.4 |
| 8bc4af99-2c77-3b25-bd9c-f961dab01dab | -3.2533 | -42.5288 | 2025-10-26 13:10:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| f4a663ba-9d6b-3fc8-87d6-ab08374b47d8 | -15.8352 | -53.5798 | 2025-10-26 13:10:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 031f05c2-024d-3296-9289-9537f6008684 | -12.3165 | -47.4855 | 2025-10-26 13:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 0ee57003-6dc6-345b-a093-21fa4fd0419a | -12.3169 | -47.4631 | 2025-10-26 13:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 271.1 |
| 7b2255d8-d693-3a7b-861b-63ab348b85fe | -14.6031 | -53.1087 | 2025-10-26 13:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 0a23d757-83bd-39a8-846e-be2c09365c85 | -17.3158 | -43.6674 | 2025-10-26 13:10:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 028cc27d-6cc7-3e29-a5b0-d60a3ffc4bd0 | -12.0032 | -46.7892 | 2025-10-26 13:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 525040d5-48ed-3772-bc2a-906641ca235a | -5.4673 | -37.8536 | 2025-10-26 13:10:00 | GOES-19 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 374.3 |
| 5fc02a24-79bf-32f1-ac2e-dcaacab36386 | -15.2649 | -50.7535 | 2025-10-26 13:10:00 | GOES-19 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 14cf0efb-0982-31f5-b9e4-f58bea6efb44 | -5.1235 | -40.3479 | 2025-10-26 13:10:00 | GOES-19 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 102.3 |
| 53744ddf-edcb-3e4d-876b-bc2ac094e66d | -13.3262 | -47.9207 | 2025-10-26 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 51.2 |
| ef7b5138-b7e5-35ea-93d7-f2fe674142fa | -16.1901 | -45.0841 | 2025-10-26 13:20:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 177.7 |
| 89335cec-1e44-325b-b30a-a10a7a62d471 | -15.8547 | -53.5771 | 2025-10-26 13:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 25c50cc4-67e5-3d8e-be48-d73b10c963ee | -17.3165 | -43.643 | 2025-10-26 13:20:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 178.5 |
| 71144706-cc71-3475-845d-273b268c4157 | -4.8933 | -43.2349 | 2025-10-26 13:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 153.9 |
| ef4d55cd-10ae-3c9a-9ca0-e1f29253cab4 | -3.6533 | -41.2464 | 2025-10-26 13:20:00 | GOES-19 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 113.8 |
| dc8f585d-0496-3c0f-8caf-00fb2bcfab19 | -12.3169 | -47.4631 | 2025-10-26 13:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 187.9 |
| 6dde2093-0b1f-3271-b143-5f55dcfc8465 | -3.964 | -45.4173 | 2025-10-26 13:20:00 | GOES-19 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 43f052ff-9530-32ec-9510-26aea131c486 | -4.8931 | -43.2582 | 2025-10-26 13:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 781f8e2d-8920-3eca-a412-886a1b03c28a | -4.8935 | -43.2115 | 2025-10-26 13:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 6d78f9fe-38c3-3167-bd07-2d1f5b43e723 | -17.3365 | -43.6383 | 2025-10-26 13:20:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 222.5 |
| dc3a80e9-9c2a-3fd0-9cee-7f47fca4e40e | -15.8352 | -53.5798 | 2025-10-26 13:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 168.4 |
| 696ae8ca-0739-38b9-9499-590d353e5d1e | -5.4673 | -37.8536 | 2025-10-26 13:20:00 | GOES-19 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 218.8 |
| d364a582-0606-3715-9edd-51c0155efa6c | -12.2977 | -47.4658 | 2025-10-26 13:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 10ac7c72-5cca-3a87-ac6d-59f37850e6f2 | -17.3158 | -43.6674 | 2025-10-26 13:20:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 85e11efc-f464-3e3a-8c44-0344604c32ac | -15.2649 | -50.7535 | 2025-10-26 13:20:00 | GOES-19 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 4c549b81-d26f-3cfe-a85f-9e1df758dbb2 | -12.3165 | -47.4855 | 2025-10-26 13:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| b79b75d9-1b91-3bd2-a212-e00c1b65aff8 | -5.4676 | -37.8278 | 2025-10-26 13:20:00 | GOES-19 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 127.4 |
| 0403f07b-307d-3f3c-bf8e-9f7f7a172fa0 | -3.7896 | -43.4153 | 2025-10-26 13:20:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 2f9166c8-8dc8-36ee-abbf-7437a04a8880 | -14.6031 | -53.1087 | 2025-10-26 13:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| df03b723-e54a-3fdf-862f-e6c5c2feeb24 | -13.056 | -45.9059 | 2025-10-26 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 0a3c848d-6ca0-37d4-a143-012d584e8d04 | -3.6531 | -41.2705 | 2025-10-26 13:20:00 | GOES-19 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 94.7 |
| 0da37e06-48e5-3c5a-b052-9fbbe465b13d | -12.0032 | -46.7892 | 2025-10-26 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 4f3f49a4-7b2f-350f-b705-b29a8f480798 | -15.2454 | -50.7564 | 2025-10-26 13:20:00 | GOES-19 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 75.9 |
| ded6a4c8-2104-3802-8fa3-368cd9a5d7f5 | -13.2482 | -47.9768 | 2025-10-26 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 6a2f4c63-396b-3760-b028-7924e9ade0c6 | -3.2533 | -42.5288 | 2025-10-26 13:20:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 6fec5ab9-439a-3d1f-8eb4-a106f387af49 | -15.8352 | -53.5798 | 2025-10-26 13:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 4db7d565-00ed-3673-9ddb-0dc786c727c9 | -4.8935 | -43.2115 | 2025-10-26 13:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 110.7 |
| c158bbba-2b41-393f-b214-5159b3eb2a16 | -3.0148 | -41.6851 | 2025-10-26 13:30:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 105.6 |
| 73b22beb-815d-3b7f-9710-96be10dc1b00 | -5.4673 | -37.8536 | 2025-10-26 13:30:00 | GOES-19 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 258.1 |
| e1f30d23-2abb-3d36-ae18-61d3f45825f0 | -12.0032 | -46.7892 | 2025-10-26 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 39c4254c-dffe-3024-ad67-87ce3413d3e1 | -3.7024 | -42.3892 | 2025-10-26 13:30:00 | GOES-19 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 108.0 |
| 11bf320f-383a-3e7c-94dd-d2cd1e7beca9 | -5.9045 | -41.3072 | 2025-10-26 13:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 131.7 |
| 29340a4e-abfc-336a-8d59-d3d57ebf0715 | -4.8931 | -43.2582 | 2025-10-26 13:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| e0ca9a16-b619-3d59-bf86-7b85e974cd31 | -3.2338 | -50.6417 | 2025-10-26 13:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 2f7b0c92-1860-38f7-a20a-7ade33c45c7e | -4.8933 | -43.2349 | 2025-10-26 13:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 196.5 |
| 6a052c80-02f5-393f-909c-b6427492f0cc | -17.4311 | -46.884 | 2025-10-26 13:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 125.7 |


[Clique aqui para ver as próximas entradas](README58.md)
