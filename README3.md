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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0aa41ce9-24c5-3d8e-b40f-65ca65d09ae5 | -6.1657 | -57.7793 | 2026-08-28 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 571306dc-15dd-3eb7-b5ac-e2f476f046e4 | -12.4994 | -43.8095 | 2026-08-28 00:40:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| c46ef15f-7f8c-3560-8934-04b3abedb27a | -10.7596 | -54.0384 | 2026-08-28 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.0 |
| f82c7388-c7df-3471-82d9-4b9af3229bf8 | -12.4494 | -43.415 | 2026-08-28 00:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 1c68d22e-717e-30ea-8ab8-89a8068b8dc5 | -6.1472 | -57.7995 | 2026-08-28 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| ed79a07e-1d70-3e85-9971-a13d2ceaacf1 | -12.5187 | -43.8063 | 2026-08-28 00:40:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| de25fcdd-9020-36a4-939f-0ad989bdd883 | -12.4305 | -43.3944 | 2026-08-28 00:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 205.1 |
| 9b4687ba-44b4-3aa1-8510-ab16a0c2bc2e | -10.3895 | -61.231 | 2026-08-28 00:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 75c7a311-751f-3fd2-8cb4-db945f79673e | -8.5783 | -54.7768 | 2026-08-28 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 6cdf1530-64b4-350d-bcd3-0823845084dd | -8.5968 | -54.7957 | 2026-08-28 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 357.0 |
| dbadab5f-0c3b-3053-951f-4fb2e3dede4e | -4.8583 | -45.3915 | 2026-08-28 00:40:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 220.9 |
| 6e9d0b62-6fac-3eef-a399-ea4490ddef62 | -7.2474 | -45.846 | 2026-08-28 00:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 343.2 |
| 99678e47-48da-3353-a10b-438523de3dec | -7.8828 | -46.1028 | 2026-08-28 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 3b6ca6e3-fa83-392a-934d-b3ed1e30e3c8 | -4.8397 | -45.3926 | 2026-08-28 00:40:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 0aa32bb9-a17d-3b5a-9c9a-b2652564fd07 | -12.4498 | -43.3911 | 2026-08-28 00:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 0e5bb5a2-d409-3b9e-b341-ced9863eb580 | -20.3458 | -47.5939 | 2026-08-28 00:40:00 | GOES-19 | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 219ae043-a5c8-3f66-bd5e-16cbb087f71c | -7.2657 | -45.8893 | 2026-08-28 00:40:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 9d2f541d-0889-3e5d-a58c-3afcfc81048c | -11.6586 | -50.4532 | 2026-08-28 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 72d6c9a2-ff3a-35ea-9802-c9c3465fb38a | -8.5969 | -54.7755 | 2026-08-28 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 421.9 |
| 92d14e9d-d4ac-3474-9131-c78d8b7e8eee | -6.1656 | -57.7988 | 2026-08-28 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 148.7 |
| d4b050c8-99e7-3f26-bed2-fe489327821e | -12.4107 | -43.4214 | 2026-08-28 00:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| fea98366-68e8-32cf-960f-b740819005e0 | -10.4981 | -64.5005 | 2026-08-28 00:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 0f242dfc-e851-3345-9ace-56cd8c52f24c | -11.6583 | -50.4746 | 2026-08-28 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 7c080065-98e0-3789-9df1-241e3c174b7c | -11.2317 | -53.9958 | 2026-08-28 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 5fc8f554-8f8a-3cce-996c-cd47d0450f3b | -11.7357 | -54.5227 | 2026-08-28 00:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| ec6cdaff-2bdf-34ce-914f-f733140f3c68 | -4.8582 | -45.414 | 2026-08-28 00:50:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| c50034a9-90b5-36c5-ae72-303c5f43d912 | -7.2474 | -45.846 | 2026-08-28 00:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 339.8 |
| f0a18e83-a632-369d-91f2-037cc4b8046c | -12.43 | -43.4182 | 2026-08-28 00:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 273.1 |
| b9619989-e9a8-3f58-9078-07ee16ebf07f | -10.7596 | -54.0384 | 2026-08-28 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 298e0592-1b6c-367d-bb7e-63eda5946476 | -7.2661 | -45.8443 | 2026-08-28 00:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 431.7 |
| f4bf8224-0630-33f6-b0f0-07c54a21af6e | -11.6773 | -50.4724 | 2026-08-28 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 0f7f9d88-351b-3d22-9cf7-723a2088dbe6 | -7.2284 | -45.8701 | 2026-08-28 00:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 33a512fa-d216-32b0-ad7c-7b91d4aeffb4 | -11.2314 | -54.0164 | 2026-08-28 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 3511bf41-d85c-3dcb-bade-deed82d50619 | -4.8397 | -45.3926 | 2026-08-28 00:50:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 164.3 |
| 362b6d37-2f5d-3e2a-96f8-bcec49cde073 | -4.8395 | -45.4151 | 2026-08-28 00:50:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 44110cee-bf68-3b94-801c-b20996a9abdd | -8.5781 | -54.797 | 2026-08-28 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 3f916d7b-1cdb-3304-a17e-dab096bba5ef | -12.4305 | -43.3944 | 2026-08-28 00:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 161.2 |
| ba73d281-d4e6-310b-95de-d0031d3da16e | -7.2471 | -45.8685 | 2026-08-28 00:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 647.8 |
| f58913a7-fc06-3c95-8f4c-24d11500adb1 | -12.2847 | -50.5938 | 2026-08-28 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 9296c7f1-4498-3f78-832b-0066b535e640 | -6.1656 | -57.7988 | 2026-08-28 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 154.5 |
| eb6550cf-555a-366b-8e28-3b019ef258f2 | -12.5187 | -43.8063 | 2026-08-28 00:50:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 1c072e97-27a4-36ff-a41a-5b8909251a59 | -20.3458 | -47.5939 | 2026-08-28 00:50:00 | GOES-19 | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 71.4 |
| b58acf13-6d5d-3ba8-a152-58e3504a568e | -12.4107 | -43.4214 | 2026-08-28 00:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 1dc1a259-66bf-3133-b64f-1ba547689834 | -12.4498 | -43.3911 | 2026-08-28 00:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 8ebb91a9-75aa-3a60-9e4d-95a9091d6bad | -14.8624 | -52.6318 | 2026-08-28 00:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 33.7 |
| ec2c62a3-afa7-3aea-8d55-cf29c8965089 | -10.4081 | -61.2492 | 2026-08-28 00:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| a019be2b-b1f2-341c-b9f3-44246dd21ac1 | -8.5783 | -54.7768 | 2026-08-28 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 6fc3761e-6473-3fe1-b5a6-1464a1d7b92b | -8.5968 | -54.7957 | 2026-08-28 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 292.0 |
| aa889255-7e65-3914-b5c6-8c4cae3554f6 | -14.8627 | -52.6106 | 2026-08-28 00:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 28c977da-c513-31cf-b486-c8e5bbb87f9e | -10.3894 | -61.2502 | 2026-08-28 00:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 0292bc58-a221-3df7-9b15-4158507322fd | -10.4082 | -61.23 | 2026-08-28 00:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 4d07e5ba-e5d0-3a0c-84f0-886365232e5d | -12.4494 | -43.415 | 2026-08-28 00:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 124.1 |
| e0984205-2ca0-35a1-8d96-663800bd63d2 | -4.8583 | -45.3915 | 2026-08-28 00:50:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 130.0 |
| dde572f7-fb37-320c-b088-08e8d78448a0 | -10.4981 | -64.5005 | 2026-08-28 00:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 74.7 |
| c94e4df8-ad3b-3a4b-8d7c-ce5c6aaa1dd7 | -8.5969 | -54.7755 | 2026-08-28 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 275.6 |
| c6d66f69-d323-378d-a50a-809409fd3e37 | -12.7603 | -44.2608 | 2026-08-28 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 391aee99-003c-33a7-b040-8fcbde08294f | -7.0289 | -55.6909 | 2026-08-28 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 7be4291a-2a9e-3d30-bf9b-9c44764f616f | -11.7165 | -54.5449 | 2026-08-28 00:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| b69346d7-ad07-3c1f-9cd5-86fc3850d3d6 | -7.2659 | -45.8668 | 2026-08-28 00:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 827.5 |
| 2fd790a2-c935-30f6-849e-f357c0a31733 | -16.1444 | -58.6073 | 2026-08-28 00:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.4 |
| ba942275-0bd0-3fe0-96c4-3a827f1dbcfb | -8.6154 | -54.7945 | 2026-08-28 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 8d1f6351-64e1-3849-86f9-60ac762630f9 | -12.4994 | -43.8095 | 2026-08-28 00:50:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 95ad3917-bbf4-3107-91fa-ef1c31ad2ec9 | -6.1657 | -57.7793 | 2026-08-28 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 975500d7-962c-3b34-b94a-a0de31850d2d | -6.1472 | -57.7995 | 2026-08-28 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| b49e00a5-d689-32c8-8757-6eba6f482507 | -11.6586 | -50.4532 | 2026-08-28 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 5330494e-e24f-314b-a5d4-9a4935913b12 | -8.6156 | -54.7743 | 2026-08-28 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 0d259efb-75e4-33bc-933b-087b89d242c1 | -10.3895 | -61.231 | 2026-08-28 00:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| f0a5fafb-d36c-38a3-af57-950bbf570ddf | -15.5403 | -41.9175 | 2026-08-28 00:50:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 64.0 |
| 0eed6f8b-f29e-338d-9666-5327aeefa909 | -7.2657 | -45.8893 | 2026-08-28 00:50:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| b946707b-084a-3d93-a151-26c1e503d01e | -5.3453 | -45.1576 | 2026-08-28 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| be730f39-cfa8-35c6-a3e4-8231528235fb | -7.3324 | -46.6656 | 2026-08-28 00:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| a303fb6d-e177-384a-a40c-15dd39acc0c1 | -13.4363 | -53.9988 | 2026-08-28 00:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| e4622e2b-cda3-3a6d-8a20-4fa98d45207a | -11.2314 | -54.0164 | 2026-08-28 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 25f8ae60-feea-371c-a13c-a63acac411fd | -12.2847 | -50.5938 | 2026-08-28 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| f0bea0b6-67af-3a9a-9c7e-b35e8e300a29 | -12.4107 | -43.4214 | 2026-08-28 01:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 44dc7c70-c68c-3edf-b134-94fd3420b16f | -13.4363 | -53.9988 | 2026-08-28 01:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 0cafe7a5-92ee-37d5-b76b-ded6e413c21e | -12.43 | -43.4182 | 2026-08-28 01:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 304.7 |
| 1b2af6da-5848-3154-b45d-076fd8d905e3 | -7.2659 | -45.8668 | 2026-08-28 01:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 691.8 |
| 45481fe3-1d9a-3495-aa42-c432a21a685c | -10.3895 | -61.231 | 2026-08-28 01:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 128f4f4e-fb57-30bb-a135-8966fcc03841 | -12.7603 | -44.2608 | 2026-08-28 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 194b45c9-db91-30b6-a759-5e88c9558384 | -10.3894 | -61.2502 | 2026-08-28 01:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| cb1d1182-bc01-3e39-a23d-d8cbe9fefb1d | -7.2661 | -45.8443 | 2026-08-28 01:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 345.8 |
| 76928ab0-95fe-365e-92cb-fdcaf19b5716 | -10.4081 | -61.2492 | 2026-08-28 01:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 8d0306aa-b75b-3b73-8ca7-66e8d862e25b | -14.1645 | -52.8269 | 2026-08-28 01:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 6a7b76ae-91ad-33fa-82aa-55cf0c885a84 | -12.4305 | -43.3944 | 2026-08-28 01:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 208.4 |
| dad82238-5c14-36b0-9120-f117e21cac2a | -4.8395 | -45.4151 | 2026-08-28 01:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 43df208c-88c2-3831-9c66-c770cce6fb86 | -11.6586 | -50.4532 | 2026-08-28 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| e52a06e9-a549-3011-b3fe-167b1e36c4ec | -10.4981 | -64.5005 | 2026-08-28 01:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 87.1 |
| df65f79e-1075-3b86-b59a-4554d91abee4 | -20.3458 | -47.5939 | 2026-08-28 01:00:00 | GOES-19 | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 4a94a1f6-34e1-31e5-a379-52494f0e5bdb | -11.7167 | -54.5244 | 2026-08-28 01:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 88862157-06c9-3774-b8cc-1abccaa8c852 | -11.7165 | -54.5449 | 2026-08-28 01:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 6d86084b-8c15-3a12-96a8-bc3472d7c80b | -6.1657 | -57.7793 | 2026-08-28 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 9183effd-82df-31b1-9f55-3af588063d1b | -6.1656 | -57.7988 | 2026-08-28 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 145.2 |
| 1fe70e1f-7c92-31bc-8635-f1c9c31ea4ec | -6.1472 | -57.7995 | 2026-08-28 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 90646027-a8c7-3648-ae45-bf8b4345b463 | -15.5403 | -41.9175 | 2026-08-28 01:00:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 74.3 |
| 6174c330-b68c-357e-821a-825418058a16 | -11.6396 | -50.4553 | 2026-08-28 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 6119d88a-07cf-3cab-bb58-10657d90b838 | -11.2317 | -53.9958 | 2026-08-28 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| d16c9e02-6ab3-3f7d-8777-7315f6d1d8c2 | -10.7596 | -54.0384 | 2026-08-28 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 859cf8e5-c748-328c-af44-6e0b072dca1c | -4.8582 | -45.414 | 2026-08-28 01:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| eb01e8de-97cb-3825-a239-71f270e8cdbd | -4.8583 | -45.3915 | 2026-08-28 01:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |


[Clique aqui para ver as próximas entradas](README4.md)
