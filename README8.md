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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08a4a264-2763-3dfa-b174-9495207737ed | 3.03404 | -60.81263 | 2026-03-05 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8e645730-5840-35e1-8273-f5360f27f4b6 | 0.30768 | -60.459 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d872031-f223-36f8-afaf-1bad5b094edd | 2.99354 | -61.03796 | 2026-03-05 05:03:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7e8a689f-2d1e-3d82-97db-b2a27f303640 | 3.06727 | -60.62946 | 2026-03-05 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 23643ae9-8abf-377c-a6d5-5478989365f2 | 0.30337 | -60.4597 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b49cdd16-bb55-31ae-ad68-43b0db81dca5 | 0.62428 | -60.21439 | 2026-03-05 05:03:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b20e1f2-00a1-3dfc-b881-48ffbdf06553 | 3.19056 | -60.57232 | 2026-03-05 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 17a3fa36-6548-3f24-b74f-a40df356f360 | 0.97213 | -60.53035 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5d8e46f-cac5-354d-928e-202174809f59 | 0.66314 | -60.30349 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 24942b14-fa4d-39d1-81e0-ef92301d4d79 | 1.15078 | -60.89434 | 2026-03-05 05:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a88d1052-8a99-388b-abba-5d56aa617fba | 0.77311 | -59.89618 | 2026-03-05 05:03:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0aaa6ca1-3a27-365e-b7c4-f936887970d6 | 0.31372 | -60.44124 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 41ad8d03-d9a6-3fc8-b310-d96e1d9d6250 | 0.27886 | -60.61669 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27321fa1-6785-3091-bf51-ce65862a4216 | 0.46302 | -60.39488 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 78c2c1a0-344e-3bb2-9ca5-faa39b2c6b8f | 2.72251 | -60.67436 | 2026-03-05 05:03:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b99117e2-706c-357d-9b68-09c92bf34f44 | 0.27838 | -60.62001 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32f56190-6cfb-3005-9542-04450fb1660c | 0.73187 | -59.90651 | 2026-03-05 05:03:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29801332-108b-34a5-a206-cbd5724743ea | 0.45872 | -60.39555 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5c136e5f-2419-3180-8563-1a42c2efe3fe | 0.66743 | -60.30283 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 23832ff4-49fd-39f7-9a4c-6cd32b48e719 | 0.47134 | -60.31936 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19a6d26c-fd02-323c-85b2-c2de465353e1 | 1.94752 | -60.82059 | 2026-03-05 05:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f4560a1c-e057-3ba9-ac3a-19173f55564e | 2.97407 | -61.03594 | 2026-03-05 05:03:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a1a96ec4-976a-3366-8324-f5eb1b748492 | 0.04832 | -60.98829 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f94599e6-3723-3496-8c63-87486a10cf0a | 3.062 | -60.62552 | 2026-03-05 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| edbfc42c-d245-3255-a2c4-d6ec63f4718a | 0.5823 | -59.8433 | 2026-03-05 05:03:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f1abe68-66ee-3955-b0e7-e0b9b3bff1b4 | 1.10833 | -59.1945 | 2026-03-05 05:03:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| acc5a0c2-39e0-390e-b54e-50dca219c9ea | 0.45376 | -60.39214 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d1aa560f-3d93-3021-a593-9f8ae9fb4183 | 1.5104 | -59.90441 | 2026-03-05 05:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 80d5eb26-6596-300c-8ac7-d3000754ddb0 | 4.96317 | -60.26131 | 2026-03-05 05:03:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a00035ce-2841-3af5-a7dc-46dbf2550dd8 | 0.48816 | -60.51434 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 057db23c-0cb0-3533-a3f5-e590f20b90c3 | 2.69486 | -60.7071 | 2026-03-05 05:03:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| daa72f21-e7a1-3efb-a866-8b8c96237941 | 1.00838 | -59.5126 | 2026-03-05 05:03:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7017fb9b-eeae-33bb-9861-1140787ff86b | 0.48117 | -60.32609 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39686574-378d-3296-a698-582bc3f9a23f | 2.09605 | -60.19824 | 2026-03-05 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 168e31bc-7474-3f97-a7b6-a5ec15907874 | 0.73129 | -59.90269 | 2026-03-05 05:03:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b11ae87-0348-39c0-b56d-cc218dad54d5 | 2.96346 | -61.09329 | 2026-03-05 05:03:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| af425ae4-81c4-3e97-a870-a7057ee38f4f | 3.50915 | -61.90866 | 2026-03-05 05:03:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2a2c703-2c66-3075-8a58-3b75d818685f | 2.95728 | -61.08408 | 2026-03-05 05:03:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 688541c5-be09-30b8-85a4-9144774c4501 | 3.51375 | -61.90504 | 2026-03-05 05:03:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79c4fb31-eccf-3d9c-9bbf-e9646fab1544 | 2.72635 | -60.66904 | 2026-03-05 05:03:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e233fb6d-7a49-3576-8604-28c81850d109 | 2.78903 | -60.3438 | 2026-03-05 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ea01e881-7e3b-3e3a-8508-08193b790558 | 3.18533 | -60.56842 | 2026-03-05 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aac1daf8-a464-37b0-b085-d7c84b0a88f2 | 0.47751 | -60.33081 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9167bdc1-15f6-31f3-a9f1-6870a849bb00 | 0.97146 | -60.52609 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96768e56-6259-345f-bcfc-a914094050c7 | 1.0254 | -59.48747 | 2026-03-05 05:03:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d3ab89f-9a25-3010-9d52-8705f6b46db5 | 2.70117 | -60.68709 | 2026-03-05 05:03:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 17.0 |
| e110fe3f-751c-3668-aa0c-90b684d417a1 | 0.04626 | -60.97513 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca293b0d-9a6b-3eb4-93d4-cd0d9d0b2a1c | 2.23075 | -60.22556 | 2026-03-05 05:03:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d410417b-ef48-3b05-8119-251fb70e28b0 | 2.22637 | -60.2262 | 2026-03-05 05:03:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d9712f83-e2b8-3ae5-b148-ed8f96ad6b7b | 1.51475 | -59.93255 | 2026-03-05 05:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6dbe3b5a-7235-3f72-b715-c12849dee12e | 1.49715 | -59.93106 | 2026-03-05 05:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72d28043-0382-3406-8d62-7f34f2c7b315 | 1.50742 | -59.91318 | 2026-03-05 05:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5edacdbf-17c6-3963-93a9-890a0e6c4628 | 1.51225 | -59.91638 | 2026-03-05 05:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b692d11-21d7-323d-b59e-594278d7ae26 | 2.69346 | -60.69779 | 2026-03-05 05:03:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c3069c5-08fd-372a-a7de-5192dc2e4d7f | 1.34725 | -60.02265 | 2026-03-05 05:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d2ac5fdc-7c9b-3534-ace9-dddec557647d | 4.96838 | -60.26504 | 2026-03-05 05:03:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90c60e59-6f8c-3d30-800c-3f2f8fe6133b | 0.03943 | -60.98983 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac2a5d0c-b3e2-34f2-9d5e-b95cb727564b | 0.94412 | -60.18338 | 2026-03-05 05:03:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6c4a5cd-a593-3050-99c5-f005a3ed0af4 | 2.7211 | -60.66513 | 2026-03-05 05:03:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51547ead-0a37-3cfe-9922-8d736d5c6f26 | 1.51413 | -59.92854 | 2026-03-05 05:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35e2082b-5b73-3c0c-8165-89676f2b1ffc | 4.54038 | -60.57287 | 2026-03-05 05:03:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a0d0122-99b0-3be4-90ac-603362a7a134 | 2.92286 | -60.45201 | 2026-03-05 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33b197b0-8a4c-3378-93cd-0b98a7c852fd | 1.11399 | -59.20435 | 2026-03-05 05:03:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ef72275-8ec3-3e77-aa5a-30a91f57354a | 1.11289 | -59.19736 | 2026-03-05 05:03:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f9c1885-a908-3932-9147-da89b7678c9b | 5.00692 | -60.37041 | 2026-03-05 05:03:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 963798e2-8d6b-3d2d-9df3-45d459948239 | 2.9928 | -61.03305 | 2026-03-05 05:03:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1abb87f4-d120-39fd-9927-d89cfdc7388c | 0.05276 | -60.98746 | 2026-03-05 05:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7562f4d5-8a9e-3ea9-8366-938a424abc39 | 1.49291 | -59.93172 | 2026-03-05 05:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce90c5ce-8745-3893-93cc-773309fa2eaa | -4.7054 | -55.9606 | 2026-03-05 05:05:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e78a751b-b629-3f83-8a8c-f2cd5f8d66d7 | -1.84325 | -60.00359 | 2026-03-05 05:05:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1c1401c-a43f-3f54-acd0-bd044ee6e7c7 | -15.07593 | -57.78018 | 2026-03-05 05:08:00 | NOAA-20 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e822a0b-061e-388d-a12c-60ff9579a913 | -15.08199 | -57.78484 | 2026-03-05 05:08:00 | NOAA-20 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26667aac-e708-3dcb-95d8-f2ad4f171c73 | -15.08444 | -57.63989 | 2026-03-05 05:08:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c54eb604-0e73-3554-8c5e-94c70bbd48bc | -15.07537 | -57.78373 | 2026-03-05 05:08:00 | NOAA-20 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28116f6b-c196-3881-944a-63fd12429e2e | 2.7816 | -60.3528 | 2026-03-05 05:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 6dc6d367-1607-3dfc-89b4-8e93b1121d13 | 2.7816 | -60.3338 | 2026-03-05 05:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 154.1 |
| 9d3ec1d4-8946-332c-b0c6-6779fc68205d | 0.0455 | -60.9799 | 2026-03-05 05:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 21.5 |
| e8628b9a-6375-3fcf-b7d6-ad68f53287ad | -16.58954 | -57.80681 | 2026-03-05 05:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| b1350341-d828-3ebb-954e-fff396d18166 | -21.0911 | -49.22012 | 2026-03-05 05:10:00 | NOAA-20 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 814f1126-cf26-3e7b-b447-088b983e5578 | -21.70723 | -56.32375 | 2026-03-05 05:10:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f153fe00-12b4-38aa-a108-e2e1ad3e76d9 | -19.90459 | -49.41216 | 2026-03-05 05:10:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 88d9f59b-ce53-3d70-ae25-11ffbd0d6e02 | -16.58898 | -57.8104 | 2026-03-05 05:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 9f049e2f-81ac-345f-b1a7-f9d937ea120b | -20.91959 | -50.5344 | 2026-03-05 05:10:00 | NOAA-20 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| ce73e87f-1f6c-395c-b32b-3abce6f3a125 | -16.57767 | -57.7977 | 2026-03-05 05:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 3b614138-6ff2-3335-8fb7-e03a94858529 | -20.9405 | -48.71397 | 2026-03-05 05:10:00 | NOAA-20 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e9e88781-f8ba-3aed-aabd-bb85031dcf78 | -16.58098 | -57.79825 | 2026-03-05 05:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 639f1ab0-b7f6-3183-8660-72b0f09ea8ed | -19.90422 | -49.41566 | 2026-03-05 05:10:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| eb5c2906-9468-3af8-9d5d-70078dc67ff1 | -21.30349 | -48.60014 | 2026-03-05 05:10:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b66e97b2-f7cc-3498-9d6c-044b062516ed | -18.8968 | -54.72629 | 2026-03-05 05:10:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5689654e-b36e-33dd-adb1-74fd3b95fecd | -22.96573 | -49.91014 | 2026-03-05 05:10:00 | NOAA-20 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e79fbd8c-f9f6-3f10-816e-a5a3810aff2d | -17.52383 | -53.69683 | 2026-03-05 05:10:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 16a27a1a-5d02-3bc7-b641-b9f126872730 | -20.94011 | -48.71803 | 2026-03-05 05:10:00 | NOAA-20 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 247cc7c6-25fd-3c6e-9a2e-8bc1e7a891aa | -16.58566 | -57.80984 | 2026-03-05 05:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| fd3cfc54-e9bb-3ab6-b7eb-998eb9ac92ef | -17.52777 | -53.69732 | 2026-03-05 05:10:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4b428564-a67a-350f-8862-d5af63429744 | -16.58623 | -57.80626 | 2026-03-05 05:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 88b0594d-7bab-36bd-a88c-f62ea9fd12ba | -21.30388 | -48.5961 | 2026-03-05 05:10:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 84fbecd0-2b98-3777-bdbf-de41c6cfeb8f | -21.09072 | -49.22396 | 2026-03-05 05:10:00 | NOAA-20 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7942042d-75f9-398a-9606-7aba04911f84 | -20.91451 | -50.53387 | 2026-03-05 05:10:00 | NOAA-20 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f2482f80-ab9e-3c2c-b610-5ce47cbbf0d5 | -30.25911 | -56.6059 | 2026-03-05 05:12:00 | NOAA-20 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 92f73a18-ee12-3e11-80e3-70dd44b51318 | 0.0455 | -60.9799 | 2026-03-05 05:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 22.7 |


[Clique aqui para ver as próximas entradas](README9.md)
