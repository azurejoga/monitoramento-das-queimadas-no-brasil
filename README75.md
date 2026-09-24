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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f578e167-8713-3151-8b8f-51bf1a4b4a75 | -11.96008 | -50.75364 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63bd918c-d968-32c1-aa60-ab40ccb766de | -13.79282 | -54.06131 | 2026-09-24 05:06:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 48c5b80b-b456-3fc8-afe5-f5c8ac5b97f2 | -9.86998 | -48.3167 | 2026-09-24 05:06:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5f0f7f24-ea34-3ebc-91e3-b569d0ac9af8 | -10.09669 | -50.19493 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa6de0bb-8455-38fe-87a1-edd652004c71 | -11.62797 | -50.60904 | 2026-09-24 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| aa87e9e2-232e-3194-a597-c18c2538727b | -11.46995 | -47.39183 | 2026-09-24 05:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b1e135f7-5f20-3154-8ebd-a84602e2274e | -8.45473 | -57.61942 | 2026-09-24 05:06:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ca691dd2-3081-3588-acf6-768f2efc09f3 | -9.12973 | -57.55157 | 2026-09-24 05:06:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee4cc77a-22be-392a-bcdf-aaa1a7dda596 | -14.5723 | -54.13018 | 2026-09-24 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 73cd6c87-317b-3d87-8fc5-e119f5c7c539 | -12.92478 | -50.91441 | 2026-09-24 05:06:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2cd7a2c-a84c-39bc-b5ba-aae825deba1e | -12.02952 | -50.28854 | 2026-09-24 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 574deca5-6bf7-3416-8557-57540dc68f16 | -9.75001 | -64.31096 | 2026-09-24 05:06:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 210af10b-5aa9-37b6-b93f-fa5d02b8fc69 | -11.91449 | -50.73005 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4b9cdf5e-0dae-3025-a5df-2fd15a3a4fd8 | -7.8983 | -61.17661 | 2026-09-24 05:06:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ea1658f2-a438-3c02-8d97-55c3e1f644ff | -13.18108 | -51.54127 | 2026-09-24 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| afb92969-5297-3b80-a090-7db465a1fa03 | -9.33213 | -56.81515 | 2026-09-24 05:06:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c2fb167-0f42-32b5-a9ab-ff22325c44fb | -14.62332 | -50.60728 | 2026-09-24 05:06:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 28aa3bf7-a0ed-3a44-9a3d-cc654980bf48 | -7.8858 | -61.17014 | 2026-09-24 05:06:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e8a6a275-b1f4-339b-b1f9-3dd56887c351 | -10.41266 | -49.36479 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| f88d7405-8dbf-330e-b7ee-f8560c9c55af | -13.45754 | -46.2617 | 2026-09-24 05:06:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0f69af33-5362-3943-90a3-590a32fb5a0b | -9.49836 | -64.03506 | 2026-09-24 05:06:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d8f544bb-f62b-3a51-a6e6-30db233f804a | -11.44271 | -47.40686 | 2026-09-24 05:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a4ab2560-3cba-33e6-be44-1bdcfb8c8c1b | -9.498 | -64.03362 | 2026-09-24 05:06:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3dc4c761-24cc-3e62-b6e4-6ee164aa476e | -8.04411 | -61.32166 | 2026-09-24 05:06:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| beb73713-0fb1-3414-839d-4c5dbea5f342 | -11.43767 | -47.40675 | 2026-09-24 05:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c121b916-6b5f-3a1e-a494-216cc1c6baf9 | -10.97806 | -54.09551 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3dcad67-658d-3e7c-a954-8ba78d077656 | -11.42754 | -44.19245 | 2026-09-24 05:06:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e4866317-deb0-3f1b-9735-c6b2d3a71bab | -8.68779 | -62.89671 | 2026-09-24 05:06:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 726c885b-e210-339e-8733-0c784185c086 | -8.68394 | -62.86193 | 2026-09-24 05:06:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dac53d61-184a-3ee9-8f7e-a8270e2059dc | -10.27098 | -49.96394 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a0176f0-6f9c-3687-80bb-c7649cbd3c2d | -10.9111 | -53.95831 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0cb4e62-a829-3288-9ed2-9067e0568d5a | -12.17039 | -47.37596 | 2026-09-24 05:06:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7fd9b807-532c-37b1-8fc7-0109f590e5f0 | -10.22613 | -57.82481 | 2026-09-24 05:06:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f40b6551-d4ba-35cc-98e8-9989a0ba1414 | -10.26742 | -49.95963 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f1542b4f-b52f-32df-aa39-6c0315fa6940 | -11.3911 | -47.37062 | 2026-09-24 05:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec8a326d-cd28-38e0-b27a-c01292eb0e49 | -14.56598 | -54.12518 | 2026-09-24 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0f5d8772-c1c2-3c82-b094-7724b6cd7f9b | -12.41004 | -46.9594 | 2026-09-24 05:06:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cf070eec-69ff-3175-9a2d-96fe5a2235fe | -13.78424 | -54.04824 | 2026-09-24 05:06:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 96a5b00d-8ea1-3f55-8c5c-e0f3fe607c42 | -12.11058 | -50.74038 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e5a714b-d9e6-36b3-ad60-9614f41ac1b7 | -12.40789 | -46.96424 | 2026-09-24 05:06:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fbf6a07c-cb41-3c65-b4a2-409e1a225c60 | -11.62445 | -50.60492 | 2026-09-24 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9dc00362-bfc3-38fa-8b9b-46802314efa5 | -10.38671 | -54.41084 | 2026-09-24 05:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17ecfcec-8bc2-3efe-8af7-5aeb14c5dc3e | -10.6224 | -53.98821 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ff85735-8608-35fe-a048-6a8e358208b9 | -13.46355 | -46.25799 | 2026-09-24 05:06:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 586fb56b-dd73-3b60-a4ab-9ee4f7064f01 | -10.719 | -48.73584 | 2026-09-24 05:06:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c32a0eed-ceca-370a-8560-2d33323eff83 | -10.44008 | -46.28573 | 2026-09-24 05:06:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a6e58594-14c9-346b-bf8f-d716340f0f5c | -10.43642 | -46.27282 | 2026-09-24 05:06:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 919f5022-3579-3c72-b21c-f45c52f3822e | -11.95283 | -50.74724 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| be5ebf05-45df-3dd7-afb6-160a9ad91483 | -10.91277 | -53.94736 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 572a4fe2-df95-3292-b9be-926b6c8ee608 | -12.15944 | -50.72527 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79187251-0a42-3772-aad0-d10c1361053d | -9.32814 | -56.81825 | 2026-09-24 05:06:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| da8a6756-e920-3c99-9929-4a453cb712a6 | -9.03957 | -65.42754 | 2026-09-24 05:06:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc1c4e50-3f14-391b-b094-cfe7496a5342 | -7.90423 | -61.16864 | 2026-09-24 05:06:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 79d4d5b6-9aac-36e2-bb3d-72e3aae85198 | -11.64486 | -43.4898 | 2026-09-24 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| fffbf906-fb0e-361e-9a92-9476a06b677c | -13.17932 | -51.54403 | 2026-09-24 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dbbd22f0-94d7-35fe-9715-20c23a5b290b | -9.48193 | -56.75977 | 2026-09-24 05:06:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 34fddc6e-9b9c-364d-9a49-f040633ff70d | -8.48634 | -57.60414 | 2026-09-24 05:06:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7913a6bf-4699-305f-a836-6ad4f2a29282 | -11.86062 | -49.95339 | 2026-09-24 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e67d3be-6bdf-3ca6-86ef-9b1a0fe35dde | -11.92199 | -50.73472 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5bc7d692-28c0-3caf-b782-659d5582baf4 | -11.63197 | -50.60962 | 2026-09-24 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca024ac6-a4a3-3a53-bdf3-6765ee95eae5 | -11.39936 | -47.39065 | 2026-09-24 05:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 6a2dccc2-b74a-369e-8cb8-a76aa0f1daa8 | -10.42119 | -49.36614 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9aa51cb9-9afc-3892-9052-9f7ef77ae6d4 | -14.70193 | -45.57987 | 2026-09-24 05:06:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9291d2ec-caef-3421-b7a1-4ccc41e2208b | -9.9672 | -50.25866 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ad89047-b5c5-3756-aa07-af2ccb2f734a | -10.2822 | -49.97309 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8c04a30-0a94-3af8-aa43-c3fd633aa62c | -8.03968 | -61.32084 | 2026-09-24 05:06:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0702b8e9-b0e9-3fa6-8a60-afef539d6109 | -11.6625 | -43.49598 | 2026-09-24 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| dcedce4e-1dea-3a6c-ad7d-4fb8c1a3ec60 | -11.48772 | -47.33848 | 2026-09-24 05:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb0d796c-27c4-3a4a-a0e6-cf6d3591137a | -12.15951 | -50.75406 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 676c8665-5c37-3116-8022-a2c04ce47af3 | -12.10708 | -50.73628 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 873b1038-1803-3592-aea4-64f410199ddc | -13.46227 | -46.26891 | 2026-09-24 05:06:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c519c3b-cb46-35a5-8464-0189df9994d6 | -10.88936 | -52.04981 | 2026-09-24 05:06:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35699f4d-b190-373d-ba8c-ea48b48bac7f | -11.99688 | -52.46589 | 2026-09-24 05:06:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 4faaf722-695f-3476-891c-36818cc2412c | -11.39717 | -47.40057 | 2026-09-24 05:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 0dca165b-c886-3dc1-9746-e84e435c7530 | -10.90828 | -53.95412 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0e07aeb-d35e-38ee-a49f-1a499c7ec826 | -8.49628 | -57.60988 | 2026-09-24 05:06:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1262f400-f88b-3072-bd54-ac4c857909e8 | -11.12961 | -48.32678 | 2026-09-24 05:06:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6587f310-01f5-3efd-be76-06f088eb8d47 | -11.65672 | -43.48992 | 2026-09-24 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 28c91174-21a9-301b-b626-1b9eb61f08da | -14.56999 | -54.12189 | 2026-09-24 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 686a0d72-e10e-3c71-92c5-8f56cc02948b | -8.92331 | -61.49108 | 2026-09-24 05:06:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8f87a5f-1a2f-36e8-af83-2c558d454cc5 | -11.62044 | -50.60434 | 2026-09-24 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a40281cf-c5e4-3db3-b378-62ec1d5be42b | -11.45225 | -47.63703 | 2026-09-24 05:06:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d9f882c-215d-3153-be90-6b6315dd8b26 | -12.13939 | -50.72236 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dcec01ae-b1cc-3d07-9c89-b9359fd8faa6 | -11.86792 | -49.96239 | 2026-09-24 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7fffe21-0763-3f6f-b2da-8403623b35c4 | -12.14048 | -50.74411 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4e685ede-e897-320a-848a-2312e4180cb2 | -11.79306 | -51.00005 | 2026-09-24 05:06:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5eeb2e0-4631-3ff6-b136-d0cfc67483e1 | -10.97525 | -54.09135 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6ccf8cb-c3af-3aab-ae96-bac3d0bfd60a | -10.28146 | -49.97296 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 263463ce-75c9-31b6-893c-2a1c9d68c9df | -10.41322 | -49.36075 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 5d75d5c6-894a-37f7-994a-ea33578c3170 | -10.27864 | -49.96882 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d2b2ce6-57a3-3523-9674-8b8321f92656 | -12.1475 | -50.75232 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1523fe9-bf60-380c-be05-e94c96456585 | -14.56023 | -54.11631 | 2026-09-24 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a7d21b45-0d46-366b-8733-5d8287da4d83 | -7.8747 | -61.18157 | 2026-09-24 05:06:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f3fb062-9eb0-3af1-94f1-3402b9a8a7ec | -10.4329 | -46.25874 | 2026-09-24 05:06:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c6f5e5af-b3db-33f8-8de0-d79d98018aa2 | -14.65418 | -50.59947 | 2026-09-24 05:06:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe19ee20-78ef-3d4f-af72-aab8695503b4 | -8.04079 | -61.32248 | 2026-09-24 05:06:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6296f528-4169-3623-881a-e81904efa4c2 | -11.465 | -47.39102 | 2026-09-24 05:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 62e507bd-f273-3dee-94e9-252743c317ec | -10.45513 | -44.94934 | 2026-09-24 05:06:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5113281-cbbb-376f-9e30-cb1130c0a0bb | -10.24269 | -49.9862 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41a38498-dcbc-3a3e-a0c2-a862cb45297f | -11.48844 | -47.33265 | 2026-09-24 05:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README76.md)
