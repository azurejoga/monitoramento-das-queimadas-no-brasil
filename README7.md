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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 968c1302-cdc4-3c50-9be4-73d2d161883a | -6.7698 | -55.6844 | 2026-08-29 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| fe512495-606f-3f50-a7c9-2f83df71e6f6 | -4.3588 | -47.7636 | 2026-08-29 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 5198175a-f0cb-33ae-b516-d88932034e9d | -10.8996 | -46.6216 | 2026-08-29 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 65b57d6e-79f5-3372-a694-e4f54d1ded53 | -6.77 | -55.6445 | 2026-08-29 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 7efbd627-5715-3126-a20f-340bb4e5fee9 | -7.5139 | -55.2851 | 2026-08-29 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 85c1e411-1115-3eec-9540-4ef0151ce81f | -5.8895 | -57.7513 | 2026-08-29 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 182.9 |
| 6b30e95f-bf14-3882-975d-586992c5b102 | 2.4155 | -60.8699 | 2026-08-29 00:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 38.5 |
| a294e4f6-b232-3f81-b825-4a1ffb6b2d1b | -8.5358 | -55.3629 | 2026-08-29 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 5ddd5c53-1867-35cc-9c61-bd8c731414b6 | -10.4795 | -64.4824 | 2026-08-29 00:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 8bb5e51e-aa08-371d-a62a-78758cfc1bec | -11.0445 | -57.2023 | 2026-08-29 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 3b9640ac-4f72-3232-8a1d-a4a32aaa73e0 | -5.8894 | -57.7708 | 2026-08-29 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 152.9 |
| eac51c04-e2e4-3f0b-9997-84685d771e95 | -6.6129 | -43.7317 | 2026-08-29 00:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 253.3 |
| 18d7c37e-ecf9-30a6-862c-6be2a89163a3 | -4.3772 | -47.7844 | 2026-08-29 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 35f1edba-f0ab-3ebf-a657-ad6d2ccf077d | -10.4794 | -64.5012 | 2026-08-29 00:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 60acfb17-9fc7-37df-a16e-cba2b2aa09f8 | -10.9381 | -46.5942 | 2026-08-29 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 0b40be4f-072e-3b74-baf5-7a0a22ea36f5 | -5.9078 | -57.77 | 2026-08-29 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 4260402f-3d47-3e69-af4a-ac4e400d25aa | -6.7343 | -55.4671 | 2026-08-29 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 53ba6f5e-f542-388e-a664-67109fcea4f2 | -7.5137 | -55.3051 | 2026-08-29 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| cf04cef9-d419-3c06-aa12-236f68cd4069 | -11.0252 | -57.2436 | 2026-08-29 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 98.5 |
| eeea6d38-037b-3a22-9a1b-c653b23d1dbf | -6.6503 | -43.7516 | 2026-08-29 00:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 3a0625ce-6d75-310b-b398-df50ba23ba4e | -20.941 | -57.5694 | 2026-08-29 00:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 98.0 |
| 32b7272b-dbfc-3372-9fb5-d6d046657e7f | -7.5845 | -61.3423 | 2026-08-29 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 9c6226f5-706e-3102-b6fb-64c49e233928 | -9.2465 | -65.5043 | 2026-08-29 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 0f43da14-b081-3a57-a063-804b06b8ea37 | -7.2847 | -45.8652 | 2026-08-29 00:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| c8139ec8-92fe-38de-a275-0bd9f2af00f0 | -8.5359 | -55.3428 | 2026-08-29 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 2c5ec733-e75f-34d0-b6c8-0bb6eacd561c | -5.871 | -57.7715 | 2026-08-29 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 6d66f16d-ba9f-3d08-a9fd-4c384a0df75e | -11.0256 | -57.2038 | 2026-08-29 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 644ddd74-e72e-37c8-aa98-c7479f734550 | -6.1657 | -57.7793 | 2026-08-29 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| c5670519-a8b9-3c5d-a7ea-f2400b3c87cd | -5.9079 | -57.7506 | 2026-08-29 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 120.7 |
| d662074b-1cf0-3440-b12c-444a10188968 | -10.9 | -46.5991 | 2026-08-29 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 07de7418-11ae-332a-8ded-302dfc29233f | -5.9078 | -57.77 | 2026-08-29 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 341118f0-399a-3e05-a6ac-3875dfc666be | -4.3587 | -47.7853 | 2026-08-29 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| f2460a24-43d0-374d-b4e6-0c7b06488bf1 | -10.9381 | -46.5942 | 2026-08-29 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| fe92bd5c-7e05-3a76-9f62-f572ef838ace | -5.8895 | -57.7513 | 2026-08-29 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 204.0 |
| 5b1383da-598d-35a7-a47c-98d8e54b71c3 | -6.6127 | -43.7549 | 2026-08-29 00:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 1a313fde-afa8-3158-9f3b-b680261354e1 | -4.4099 | -42.8442 | 2026-08-29 00:40:00 | GOES-19 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 8669a028-a4a7-3aa1-8ae2-8a26d1dcda59 | -4.3588 | -47.7636 | 2026-08-29 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| b75155d6-92e3-3f52-876a-7b56cae5c8fa | -7.2847 | -45.8652 | 2026-08-29 00:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 9127c00b-7f2e-34ae-a33e-e0f6482bc659 | -10.4794 | -64.5012 | 2026-08-29 00:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 41.7 |
| ae81210a-ed3a-3c57-8fa5-3f08cbdc2691 | -4.4286 | -42.8431 | 2026-08-29 00:40:00 | GOES-19 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 133.7 |
| cf0f4107-7170-39d9-a4fe-c43956cfe6d9 | -7.5139 | -55.2851 | 2026-08-29 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| f6e54ed4-deef-3ff8-9546-7084ff7c1cc2 | -7.5845 | -61.3423 | 2026-08-29 00:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 15eaee27-7d67-3110-ab8d-0dba6c5c4e21 | -11.0252 | -57.2436 | 2026-08-29 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| b4bd7513-4506-3487-bbb5-48427d2e698a | -11.0441 | -57.2421 | 2026-08-29 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 93227c15-88a8-329c-825e-527792aa4c82 | -6.6317 | -43.73 | 2026-08-29 00:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 36200c91-4abd-32a4-83c3-9c0776fef271 | -6.6315 | -43.7533 | 2026-08-29 00:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 22152330-a195-31cc-bc79-cf09cfc6b589 | -6.6319 | -43.7068 | 2026-08-29 00:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 0511b612-f7f4-33da-afe2-ec9c0fe18927 | -6.7343 | -55.4671 | 2026-08-29 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 62ddc7c2-236e-3209-b43f-9d7190bb3a9c | -4.4097 | -42.8677 | 2026-08-29 00:40:00 | GOES-19 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 774c26f4-4133-3d2e-b577-b2e6c325e950 | -5.8894 | -57.7708 | 2026-08-29 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 137.1 |
| e2280281-78f1-3b88-a8c7-177cd9115bc8 | -8.5359 | -55.3428 | 2026-08-29 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| bba30401-c5d3-3e8b-849e-e0d5e54d5ac4 | -8.5358 | -55.3629 | 2026-08-29 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 2dbca29f-0abe-3a83-9d21-ce2efc1d0663 | -10.9187 | -46.6192 | 2026-08-29 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 219.9 |
| bf09f164-7fc7-3ac3-9c88-2ecf3a163592 | -11.0254 | -57.2237 | 2026-08-29 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 33d0a061-7c82-3945-92e7-b1631052332f | -4.3772 | -47.7844 | 2026-08-29 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 96c23723-deea-39d8-aaff-b49883ff140b | -6.7514 | -55.6654 | 2026-08-29 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 287887de-2f5f-36a6-9cc9-644a4d2e80cf | -6.77 | -55.6445 | 2026-08-29 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| e85ab8c8-30a5-3a00-b73c-1f0390bc7bd2 | -6.7884 | -55.6635 | 2026-08-29 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 477b0255-4cb0-367a-ac43-543a7af9bb9b | -5.8711 | -57.752 | 2026-08-29 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 60f50b31-c4d3-34da-9fda-943c02ac2b9a | -10.919 | -46.5967 | 2026-08-29 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 166.5 |
| fa7f887c-59d2-3d2a-b1f5-579805662adc | -7.5137 | -55.3051 | 2026-08-29 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 5f68ee78-8280-3ffe-a2e6-35a96d6fad2c | -6.6129 | -43.7317 | 2026-08-29 00:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 97e93b8b-50ca-33a9-bfe9-0ee097795276 | -7.2849 | -45.8427 | 2026-08-29 00:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| a86e140c-519f-35c1-a57e-86a76facf800 | -6.7528 | -55.4661 | 2026-08-29 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| f1802da9-13cc-3678-8810-070e1bc789cb | -6.7698 | -55.6844 | 2026-08-29 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 15f6113d-4d7b-36c7-8b30-cc3a93eb9c6e | -6.7699 | -55.6644 | 2026-08-29 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 201.9 |
| 6ff8ecb8-026e-3618-9c76-d2593de36d0a | -10.9377 | -46.6168 | 2026-08-29 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 62eb7dbc-c602-35a9-be6d-68fffd4bf323 | -20.941 | -57.5694 | 2026-08-29 00:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 101.0 |
| 7f216c65-8b59-3447-ba7c-685f1b3c6718 | -12.43 | -43.4182 | 2026-08-29 00:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 88c0bfda-64fb-36df-8a37-f4172dfa2082 | -5.871 | -57.7715 | 2026-08-29 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 4d022437-1f10-315e-9520-448f62e27a79 | -4.4284 | -42.8665 | 2026-08-29 00:40:00 | GOES-19 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 174.4 |
| 0007edd2-3a16-385d-8915-376e38c9f978 | -4.3774 | -47.7627 | 2026-08-29 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| c67fa82f-beca-3dad-83f3-0e48a52b456d | -11.0443 | -57.2222 | 2026-08-29 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 56ed6256-aa1f-3ba0-8817-b572c1496cdf | -6.6505 | -43.7284 | 2026-08-29 00:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 44.4 |
| f07f2c24-06c5-3ad7-92c3-a2553cf840d3 | -10.8996 | -46.6216 | 2026-08-29 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 179.7 |
| 67f06a08-b5a1-3342-b0c1-8bb20f8c77e2 | -11.0445 | -57.2023 | 2026-08-29 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 0cc4b127-b4e3-3fea-a4dc-dfbb9a83adee | -8.9428 | -63.2797 | 2026-08-29 00:50:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 7ceba6f2-fbc5-3c3d-93e3-94bce7086a52 | -5.9819 | -57.6892 | 2026-08-29 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 3fb806e9-8eeb-31cb-b00b-8040902522d0 | -10.4609 | -64.4831 | 2026-08-29 00:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 967f6780-9c80-3887-a3db-804343b60eea | -6.77 | -55.6445 | 2026-08-29 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| a82933ec-a194-3484-bf5b-e06e36bea296 | -10.4795 | -64.4824 | 2026-08-29 00:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 61.9 |
| b335182c-0ae0-3cdf-be2e-f1437fe627b2 | -11.0445 | -57.2023 | 2026-08-29 00:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 110b0511-caf5-3717-abbe-c39fcc4e5302 | -7.2847 | -45.8652 | 2026-08-29 00:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 624eea4e-cb3d-3eaf-a736-c3c9421e752a | -10.9 | -46.5991 | 2026-08-29 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| aae8db9a-8b2a-31be-abd2-da08489d95fc | -10.9187 | -46.6192 | 2026-08-29 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 46.4 |
| c983af7f-3f61-3528-95fc-c086eb5ed0ef | -6.7698 | -55.6844 | 2026-08-29 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 1065cec2-47dd-331c-ba51-3235a72939f5 | -6.7884 | -55.6635 | 2026-08-29 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 459b2230-ce52-3a76-ad4a-3fdb45ef5a28 | -8.5358 | -55.3629 | 2026-08-29 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 9e656263-27fd-3798-a24f-6d3c1f3d5bb7 | -11.0252 | -57.2436 | 2026-08-29 00:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| a850d49a-cafe-32af-9627-a3d86aaae8c6 | -7.5137 | -55.3051 | 2026-08-29 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 8300ff14-abb9-3698-820b-90b2d0e0cca5 | -10.4608 | -64.502 | 2026-08-29 00:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 231492c2-1455-3815-b382-7072ba2d2f53 | -10.8996 | -46.6216 | 2026-08-29 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 157.8 |
| ea2f22af-e3f4-3b79-825f-0ee3be1659d8 | -6.6317 | -43.73 | 2026-08-29 00:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 1eaeea50-4ec4-326c-852a-1a1de2a5aa61 | -6.7699 | -55.6644 | 2026-08-29 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 180.5 |
| cb022a47-40d0-3302-83cd-5060c74f3615 | -5.4179 | -43.1752 | 2026-08-29 00:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| a6d6c8eb-7e15-353c-8b96-a63c1108ba82 | -6.6315 | -43.7533 | 2026-08-29 00:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 5fd3b007-6956-3af0-ba01-1e87901b2cbb | -7.5139 | -55.2851 | 2026-08-29 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| df03330b-7748-3d19-84a0-11611a277f77 | -8.5359 | -55.3428 | 2026-08-29 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 7d992883-921a-3abf-b109-2822fa5eb945 | -20.941 | -57.5694 | 2026-08-29 00:50:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 59.6 |
| 90d16b83-12d5-3418-9e3a-33064149f1cc | -7.2849 | -45.8427 | 2026-08-29 00:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |


[Clique aqui para ver as próximas entradas](README8.md)
