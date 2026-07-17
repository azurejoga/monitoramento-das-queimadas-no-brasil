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
| 180a35c4-6a40-30ae-8c81-9a90f309fba2 | -10.8092 | -45.1338 | 2026-07-17 00:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 98.8 |
| c0972444-25f1-3074-b7ed-2e151bcdc1b0 | -19.8436 | -57.9917 | 2026-07-17 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.4 |
| 0d10f391-c91e-30e6-9fe0-df7332038865 | -11.5079 | -50.3633 | 2026-07-17 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| b4634a60-91b1-3763-bed2-162c26ea6dca | -19.8641 | -57.9682 | 2026-07-17 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.4 |
| 2e60a915-af22-3136-9112-e936fa83e143 | -19.844 | -57.9709 | 2026-07-17 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.5 |
| b6aeeb05-e986-391b-8101-4d8feed6747d | -10.8283 | -45.1312 | 2026-07-17 00:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 150.2 |
| 946679b6-7ad9-3260-a2d5-2b2060dd6699 | -8.5173 | -48.0796 | 2026-07-17 00:00:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 00ebbf7b-805e-3f05-b0ef-7c007c9afaf0 | -8.4985 | -48.0813 | 2026-07-17 00:00:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 2d421fbb-1538-3d3d-8ae9-b23546153a08 | -13.4448 | -43.8604 | 2026-07-17 00:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 1b57e696-1020-3730-842a-1c751bbe1be8 | -19.8637 | -57.989 | 2026-07-17 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 263.8 |
| 633ea2a7-088b-30c7-a938-86e515a25dcd | -2.79265 | -49.5325 | 2026-07-17 00:01:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 317f8754-204e-372c-8f4c-0871e2197064 | -3.41842 | -49.12445 | 2026-07-17 00:01:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 719ff905-cdbf-3071-9995-b173e09d3110 | -2.79141 | -49.5233 | 2026-07-17 00:01:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 75a5c428-9550-374c-bafe-e716b8f26215 | -3.41719 | -49.11543 | 2026-07-17 00:01:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| cd489723-f5fe-38a4-ae86-9b9641ed52eb | -19.8641 | -57.9682 | 2026-07-17 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.1 |
| 51751e0e-a349-3ae8-8b6c-bb6e0524f848 | -22.9154 | -49.1927 | 2026-07-17 00:10:00 | GOES-19 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 54.8 |
| bc4bb9a3-2d73-315f-81b4-3dcb63f00c45 | -11.5079 | -50.3633 | 2026-07-17 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| de44316c-d768-3e81-91e7-034036c1dce9 | -10.8283 | -45.1312 | 2026-07-17 00:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 09208458-f4ac-3183-bd52-c4e3cf166565 | -19.8637 | -57.989 | 2026-07-17 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 210.8 |
| 01541d88-6686-3dee-b493-5dc0e1472c27 | -22.9365 | -49.1875 | 2026-07-17 00:10:00 | GOES-19 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 45836936-74f6-3fb4-9277-32768c656119 | -10.8096 | -45.1108 | 2026-07-17 00:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 506d6e62-8405-3bda-bfff-3fefba6f917f | -22.0069 | -48.3185 | 2026-07-17 00:10:00 | GOES-19 | TRABIJU | SÃO PAULO | Brasil | 3554755 | 35 | 33 | nan | nan | nan | Cerrado | 79.8 |
| c4d37271-751c-3947-ac4d-d58bae749756 | -13.4448 | -43.8604 | 2026-07-17 00:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 27b9f040-8e92-30dd-a1f6-10b20c0ebd61 | -10.8092 | -45.1338 | 2026-07-17 00:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 111.0 |
| c7db00ab-7a48-3867-9c13-13b70e6644ec | -19.8436 | -57.9917 | 2026-07-17 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.8 |
| 0b151389-b987-3a89-aa1f-8fdbf03465ed | -19.844 | -57.9709 | 2026-07-17 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.8 |
| 5ae29e4b-b1ec-33b7-ab81-e30f7ec58bd6 | -10.8287 | -45.1082 | 2026-07-17 00:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 9061847e-2f24-3947-bf81-8fe7e6a4417e | -19.844 | -57.9709 | 2026-07-17 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.1 |
| 75162b9f-9c18-37b2-a71a-876dbc6d89d1 | -10.8287 | -45.1082 | 2026-07-17 00:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 46.4 |
| e5b6c459-0c47-384b-a723-ee5fa5c44bbf | -19.8436 | -57.9917 | 2026-07-17 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.7 |
| 52e8f2a6-5302-39ac-ba49-71df75b7c36b | -22.9365 | -49.1875 | 2026-07-17 00:20:00 | GOES-19 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 7d06cd85-b0f8-3db2-86ca-afea30b156f1 | -19.8641 | -57.9682 | 2026-07-17 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.3 |
| 5164c8db-0053-3958-85e6-2684d0405246 | -10.8283 | -45.1312 | 2026-07-17 00:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 8b302c41-452c-32b0-ba4c-6f11ab6761cd | -19.8637 | -57.989 | 2026-07-17 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.5 |
| ceb268c1-2b3a-30b6-b03d-ffdd81bbb1ff | -22.9154 | -49.1927 | 2026-07-17 00:20:00 | GOES-19 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 59.9 |
| eee4e26c-dc92-326d-879e-7cede2771232 | -10.8092 | -45.1338 | 2026-07-17 00:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| ba16a726-11c3-30cf-951c-d0bc8540cff3 | -13.4448 | -43.8604 | 2026-07-17 00:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| ac4127f4-7118-3745-8f7e-c9c51bede520 | -10.8287 | -45.1082 | 2026-07-17 00:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 0eccc48d-1d34-30e8-94e0-ef70ffce7dd9 | -19.8637 | -57.989 | 2026-07-17 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.9 |
| 30451b85-b230-3ab4-a742-a17719a49ace | -8.5173 | -48.0796 | 2026-07-17 00:30:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 48.2 |
| a09f229e-3f04-377b-adba-e933cbe292f6 | -22.9154 | -49.1927 | 2026-07-17 00:30:00 | GOES-19 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 3b63fa18-b368-3458-ace9-015f01aff63b | -19.844 | -57.9709 | 2026-07-17 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.8 |
| 8bbf6387-2907-3d66-9fbe-f82654441261 | -19.8641 | -57.9682 | 2026-07-17 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.8 |
| 9984124c-b434-3461-ba1b-77d89a96cd6d | -10.8283 | -45.1312 | 2026-07-17 00:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 171.8 |
| 54a9768c-0f6f-3eb5-ba99-32a9609dc857 | -22.9147 | -49.2161 | 2026-07-17 00:30:00 | GOES-19 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 2be45bd0-6454-3901-a6ca-2c7f4e7604a7 | -19.8436 | -57.9917 | 2026-07-17 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.0 |
| 9575d913-a472-3333-bb99-f079689ea96d | -13.4448 | -43.8604 | 2026-07-17 00:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 9a1f0597-1dab-3578-8225-fea49a819d1e | -10.8092 | -45.1338 | 2026-07-17 00:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 4dfd3c4a-b103-3a28-9437-ed3697393886 | -10.8287 | -45.1082 | 2026-07-17 00:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 0ca704f1-14d9-3cb6-a960-53b15166dc51 | -19.8637 | -57.989 | 2026-07-17 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.3 |
| cf1092bc-0720-3bbc-8e5b-347d9de5357e | -19.8436 | -57.9917 | 2026-07-17 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.5 |
| a4facf97-0f48-3d3b-b3f3-02d48a14254d | -10.8283 | -45.1312 | 2026-07-17 00:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 117.1 |
| d437981d-340e-36b1-93f4-7b338deb00ad | -22.9154 | -49.1927 | 2026-07-17 00:40:00 | GOES-19 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 49.8 |
| ef583481-33f1-3222-9451-dfc8819a1a11 | -22.9365 | -49.1875 | 2026-07-17 00:40:00 | GOES-19 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 04a1eac5-496f-3f39-8a28-6f9bb7c839ad | -13.4448 | -43.8604 | 2026-07-17 00:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 1bb297be-3172-31b1-a87d-3ee0ce5d8244 | -10.8092 | -45.1338 | 2026-07-17 00:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 106.6 |
| a424b198-5c83-3844-a7a1-b01a2b5e7ccb | -9.4565 | -64.011002 | 2026-07-17 00:41:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dcd9605a-18a4-37f9-b4c4-fceb511fb6fe | -21.666401 | -56.304901 | 2026-07-17 00:41:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e39305b2-295f-3800-94cd-258593aea511 | -21.7756 | -56.288799 | 2026-07-17 00:41:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 58cf3e92-3369-3117-8fb8-8bd43a156485 | -28.6399 | -56.048698 | 2026-07-17 00:41:00 | METOP-B | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 6071455c-bfe2-3d81-90b2-d28ab2521ca8 | -22.236601 | -56.088402 | 2026-07-17 00:41:00 | METOP-B | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5cea062f-146e-3e1b-bb53-3b7bdc4ff380 | -21.7642 | -56.2827 | 2026-07-17 00:41:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c3c2cf24-05c6-3366-bf74-44054376fc84 | -20.632799 | -41.383801 | 2026-07-17 00:41:00 | METOP-B | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d7d2c599-afdf-375f-b02e-94fb0a5f29e2 | -19.8291 | -57.955502 | 2026-07-17 00:41:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 46d3ad4c-689f-33b8-a171-6c2f2f8d83cd | -19.833401 | -57.925499 | 2026-07-17 00:41:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a89e980e-55ea-3d55-a787-c99304691239 | -13.4229 | -43.820301 | 2026-07-17 00:41:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 00ca4676-3178-3846-8614-8e682c6fc362 | -13.4215 | -43.8522 | 2026-07-17 00:41:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0c6d8777-c571-3939-af79-c938c3f85e6a | -22.9146 | -49.181702 | 2026-07-17 00:41:00 | METOP-B | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1fe552a5-8249-3397-9865-f479043ae780 | -21.6681 | -56.313301 | 2026-07-17 00:41:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 88eb370a-fc96-3637-9159-3549eca91c1e | -12.4408 | -49.576599 | 2026-07-17 00:41:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8a79b5a3-2950-30ac-a878-ce9e986bca36 | -12.4537 | -49.5867 | 2026-07-17 00:41:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 49a88d99-29b4-3de3-a3ff-9ee61bc013aa | -11.5062 | -50.3545 | 2026-07-17 00:41:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2822b7b0-a1ea-3078-8cb0-26a62e1f8f7e | -22.247801 | -52.868599 | 2026-07-17 00:41:00 | METOP-B | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 67da3b32-d771-3e34-b059-7e1834415056 | -11.5034 | -50.3428 | 2026-07-17 00:41:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4a83fb29-c7e7-3c63-9334-2f001badfe5b | -10.8117 | -45.128399 | 2026-07-17 00:41:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f13817d7-af00-3269-b117-181a3c631d7f | -22.9737 | -48.913601 | 2026-07-17 00:41:00 | METOP-B | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2693a46c-de13-3f7f-98ff-93110a446ee7 | -10.8047 | -45.1017 | 2026-07-17 00:41:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e081fb9d-c80b-399a-8a92-d8cbe6ed88ce | -10.0356 | -51.659401 | 2026-07-17 00:41:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c6cd0793-d6dd-3874-a5a4-45a67448dffc | -19.817499 | -57.948299 | 2026-07-17 00:41:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1965ce67-ce88-3fa7-b388-6bd8f7deafa1 | -7.9029 | -48.253101 | 2026-07-17 00:41:00 | METOP-B | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 88ae87bf-2742-33aa-8591-1205bebb5580 | -21.767599 | -56.299301 | 2026-07-17 00:41:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b5cbd1cc-3082-3c6d-92cd-24cf37e84b5c | -10.0453 | -51.657001 | 2026-07-17 00:41:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 27ac8f04-481d-328b-a504-35435e9f3172 | -10.795 | -45.104401 | 2026-07-17 00:41:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4cb0eb3a-7729-33de-97e2-e8b0b039d161 | -22.226801 | -56.090599 | 2026-07-17 00:41:00 | METOP-B | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f3b680b7-106a-362d-a2ca-101cbfaf4e70 | -19.863899 | -57.9771 | 2026-07-17 00:41:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7a8d3e9b-91fe-35dd-aa07-a4ae6e3f4a54 | -20.648199 | -50.1021 | 2026-07-17 00:41:00 | METOP-B | FLOREAL | SÃO PAULO | Brasil | 3515905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0512665b-c11f-3580-be51-1bea918e6334 | -22.2656 | -55.978199 | 2026-07-17 00:41:00 | METOP-B | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2988058c-ec04-3269-b93a-1a666608e68a | -19.1674 | -47.337399 | 2026-07-17 00:41:00 | METOP-B | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 636275a4-dbf3-376c-802d-a0baa3fe76ca | -19.823601 | -57.927601 | 2026-07-17 00:41:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b8850954-9215-36b4-8642-64ec71d8500a | -9.5003 | -47.1236 | 2026-07-17 00:41:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 38ad27eb-0df2-3c22-a953-9614d2ff22d9 | -22.916901 | -49.191299 | 2026-07-17 00:41:00 | METOP-B | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 04299bd5-fa98-3eca-a1eb-2e1fdd9de36b | -29.764601 | -53.8685 | 2026-07-17 00:41:00 | METOP-B | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | nan |
| ec9f4b4b-ecc8-3e40-a03f-93e4adacc77e | -21.345699 | -51.0341 | 2026-07-17 00:41:00 | METOP-B | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f0e9b16c-eb13-38dd-8dff-7ad079dc2d58 | -19.177099 | -47.334499 | 2026-07-17 00:41:00 | METOP-B | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0b21195f-9159-3642-9392-4f454b08e1ab | -9.51 | -47.121101 | 2026-07-17 00:41:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 153c7cb1-b5fc-3339-a0fb-711c867a1a51 | -10.8021 | -45.1311 | 2026-07-17 00:41:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e224e941-2cdd-3af9-99a4-985906bd3fd0 | -22.246099 | -52.861198 | 2026-07-17 00:41:00 | METOP-B | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5524ba2d-1729-3fe0-89c3-31a8a3ba5e57 | -19.8407 | -57.9627 | 2026-07-17 00:41:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| dfa5a744-1b04-37cb-8f7a-728704cea098 | -29.691 | -51.701698 | 2026-07-17 00:41:00 | METOP-B | TRIUNFO | RIO GRANDE DO SUL | Brasil | 4322004 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 16c9a9f3-aed4-3382-a8ed-ccf984fd5f5d | -19.862101 | -57.9678 | 2026-07-17 00:41:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README2.md)
