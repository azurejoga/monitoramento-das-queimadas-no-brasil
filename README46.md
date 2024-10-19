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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72b29beb-a546-37c5-bd76-6729a6e8767c | -12.50693 | -63.2901 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bb7d218c-4acd-3508-b92b-3f2d22ad8fa8 | -12.50623 | -63.29422 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06d72e9d-6bb6-3e8c-aeae-e91e4eb21701 | -12.50553 | -63.29833 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 908b8697-f602-3a8f-8731-c5355cf06172 | -12.50483 | -63.30246 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a5c92f7b-c5ff-3ebf-9f34-9f6c016cd260 | -12.50413 | -63.30658 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2bbdfe82-c159-3eac-9cbe-f375b7eb10e3 | -12.50408 | -63.28536 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a32ab294-cc74-367a-ab6f-7eac3767a295 | -12.50338 | -63.28947 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 326f55be-7525-33af-aff5-2cf1406c6d1a | -12.50268 | -63.29359 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 642c7278-ba02-39b8-adc3-fabd9f790e94 | -12.50198 | -63.29771 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15f6a083-6869-3362-8522-c14c85fb0b37 | -12.50127 | -63.30183 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 569ca406-ca18-3ba8-91be-0160de5008ad | -12.50052 | -63.28474 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e6bc00a-9e08-3838-aeaa-ef5ffa2328d8 | -12.49982 | -63.28885 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 71831589-1064-3323-bc14-5300370c6cca | -12.49912 | -63.29297 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e2a4b800-9ccd-3b99-ab54-f2d3e20df261 | -12.49842 | -63.29709 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b526fcb5-11f7-3eb1-a8b2-f02df99fbb96 | -12.49775 | -63.28561 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f1c6646-2784-39a1-8ee1-85d25220671b | -12.49772 | -63.30121 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b7e3cb0-0180-3fb4-b6fe-c6eb223a2db7 | -12.49706 | -63.28973 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3245c1f2-2eb1-3d5c-a0e8-517e6319d591 | -12.49697 | -63.28412 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e45ff6f6-c056-38e3-a7e0-d62774722380 | -12.49627 | -63.28823 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc46cbeb-826c-3d43-bb01-8f7d3c75f797 | -12.49419 | -63.28499 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8154e90f-2b85-369a-9b6c-69604fcab8cd | -12.49342 | -63.2835 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b0cc669-cb10-31c7-9355-77f9e2f78339 | -12.49064 | -63.28436 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 285fd443-9da1-3b92-a0bc-edeff9ff4824 | -12.48708 | -63.28374 | 2024-10-19 05:18:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c2f02c9-1140-31ae-987e-75c5bfe61ac7 | -3.4202 | -50.2164 | 2024-10-19 05:25:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| dffc51e2-701a-34bd-b7e6-9b9ae8c4cba0 | -3.4387 | -50.2158 | 2024-10-19 05:25:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 54275f0d-6e77-31e3-8165-6e4f20d84a78 | -3.4388 | -50.1948 | 2024-10-19 05:25:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 584c226d-ec54-32bd-af96-862ae147d3a1 | 4.25724 | -59.94222 | 2024-10-19 06:03:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5a7c861c-b6a7-3586-a4f7-fd13abbc2cf7 | 4.25539 | -59.94475 | 2024-10-19 06:03:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72a0194c-65d2-3a65-8ad9-d31947496ce5 | 4.25486 | -59.94173 | 2024-10-19 06:03:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd91aebc-6523-3b82-95be-45f5ac05f853 | 0.99526 | -59.44882 | 2024-10-19 06:05:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 89010515-9ee3-35d6-b820-6f4cfdeb7429 | 0.99459 | -59.44464 | 2024-10-19 06:05:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0d886b34-0a2d-3280-9f7f-a75534aba84d | 0.9939 | -59.44036 | 2024-10-19 06:05:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a4aebfc5-0346-334c-b3c4-9819588173e1 | 2.14128 | -60.85147 | 2024-10-19 06:05:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b352332c-682f-377f-ae94-52353c487154 | -3.95905 | -65.25408 | 2024-10-19 06:08:00 | NOAA-21 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 122e59da-07fb-3252-b859-c65d4622ab00 | -8.93925 | -65.90289 | 2024-10-19 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9d854586-96ad-34ed-aaea-81fd765301a6 | -8.93547 | -65.89796 | 2024-10-19 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07f2c678-450b-3aa8-bcfe-ebe52211f10e | -8.93487 | -65.90227 | 2024-10-19 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 12f77a71-a2a4-33b9-9a2b-d19b55bf75eb | -8.45645 | -66.95708 | 2024-10-19 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8f73f524-e9e1-3815-a987-a2652ae3e445 | -8.45594 | -66.96064 | 2024-10-19 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 980be0d1-a23e-3569-a814-0f2eb1b56358 | -8.45284 | -66.98219 | 2024-10-19 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07db2297-4f1b-3b70-b541-ca332ab72212 | -8.4524 | -66.95647 | 2024-10-19 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c759417e-2922-39be-b462-31e9d9714af3 | -8.45189 | -66.96005 | 2024-10-19 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 11cebba9-d349-37d1-b6a1-42b99d5e983f | -2.7223 | -66.80961 | 2024-10-19 06:08:00 | NOAA-21 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6abc986c-34c4-3142-8945-715c888576a8 | -9.04292 | -67.44922 | 2024-10-19 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 8efe8e63-f485-393a-8d26-5deb13cead79 | -9.04045 | -67.43837 | 2024-10-19 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e6f0fd1b-71f9-3c93-8088-de721db7c510 | -9.03823 | -67.45374 | 2024-10-19 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bd8890dc-3bf6-3754-acb0-05458da05d86 | -9.0375 | -67.45885 | 2024-10-19 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e59f3cb6-bbbd-303f-bf95-82b28a1213a2 | -9.03676 | -67.46397 | 2024-10-19 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99a2ef0e-57f9-341d-8efd-9ca1f85b1837 | -9.03428 | -67.45315 | 2024-10-19 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e84e2b74-4801-3a88-853c-e7d1a7eca14e | -9.0318 | -67.4423 | 2024-10-19 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 168aaf81-e999-39f9-aa65-66b3d647c562 | -9.03107 | -67.44743 | 2024-10-19 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cfac8386-7a90-3e62-83eb-344f4e619391 | -8.96267 | -67.72938 | 2024-10-19 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 823ecf81-94cb-3a30-9d07-793705e27526 | -8.89698 | -68.72829 | 2024-10-19 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74a8cbb0-5827-3214-9993-200616a6b7eb | -8.89723 | -68.72616 | 2024-10-19 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79cbc653-08f4-3756-9928-5fd54f042f6a | -9.04614 | -67.45493 | 2024-10-19 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ba932d55-899e-3a50-8f89-292b2fb51da6 | -9.0454 | -67.46005 | 2024-10-19 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 05d14d89-61cd-333c-b945-6dea7e4eef0a | -9.04218 | -67.45433 | 2024-10-19 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 6a3e556b-fee6-3b11-a35b-8937871544cb | -9.04145 | -67.45945 | 2024-10-19 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 56715ae7-1127-3743-b271-bb188690eb56 | -9.03897 | -67.44862 | 2024-10-19 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0f5a4e2a-c3ef-3ea9-bafd-15998765f1e4 | -9.03575 | -67.44291 | 2024-10-19 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 58dd5b83-4178-323d-95dd-1b58c19266f9 | -9.03354 | -67.45825 | 2024-10-19 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 28b70d0b-ff9d-3edc-b1fe-ef1f006223e8 | -9.03281 | -67.46337 | 2024-10-19 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55ca79bf-d331-3b17-9e9d-d969563fb5b2 | -8.96655 | -67.72997 | 2024-10-19 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aae583a2-45fa-3dfb-916d-cf8d1a2686fd | -8.96585 | -67.73488 | 2024-10-19 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0b4d0ea-90de-35f0-89d6-2d6188972389 | -8.95162 | -67.36057 | 2024-10-19 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30437094-c5dd-3032-9fc4-65c735b38c55 | -3.06752 | -59.19381 | 2024-10-19 06:08:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb7fa0b2-68bd-3a7b-a684-7d8b29109b80 | -3.06448 | -59.1905 | 2024-10-19 06:08:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 16055b95-fc17-32ac-b012-44fed1fd2a29 | -3.06374 | -59.19545 | 2024-10-19 06:08:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7fd8c122-2f62-39d8-9123-895a700f2d9d | -3.06194 | -59.18784 | 2024-10-19 06:08:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e68476b1-6bfd-3db0-9ead-0d331b82335f | -3.06123 | -59.19282 | 2024-10-19 06:08:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e774b5ff-3d57-3718-9713-d7764ee5fe9b | -3.98954 | -59.21539 | 2024-10-19 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a0a3599-884a-330e-8083-18c5aecaa845 | -3.98883 | -59.22054 | 2024-10-19 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7e39d84-c8c6-3175-87a7-710cf436d03a | -3.987 | -59.21567 | 2024-10-19 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e9f9e4d-752b-3601-a975-7cb7368541d2 | -3.98625 | -59.22079 | 2024-10-19 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b4f82b60-fd7b-3ef0-8173-d76902320239 | -4.50827 | -61.11336 | 2024-10-19 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 057859ac-d9a1-3c67-a314-346072a8429e | -4.50772 | -61.11726 | 2024-10-19 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5f34902-e6d2-32b8-b7f5-13412ee2b190 | -3.05723 | -61.67325 | 2024-10-19 06:08:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a863fb75-bff7-3fae-9e51-43ff35225c51 | -3.05673 | -61.67663 | 2024-10-19 06:08:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e1de8d4-4c91-3b87-8ebf-d277c8c23bce | -3.05623 | -61.68002 | 2024-10-19 06:08:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a7fd99f-ecb4-3831-9600-8e8fbe2ff4db | -6.62783 | -62.93487 | 2024-10-19 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48750730-c8e5-3275-b054-3241f24f096b | -6.6274 | -62.93801 | 2024-10-19 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7ee0bc4-1d06-3499-82f7-3cff21e1681b | -6.62221 | -62.93726 | 2024-10-19 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17e13cdb-735a-365c-9664-ccef5ed42b75 | -9.06332 | -63.66538 | 2024-10-19 06:08:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a629605b-0ad8-3b11-8055-16e7f565cbd3 | -9.06071 | -63.66785 | 2024-10-19 06:08:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cfc4b029-fccd-3412-b67a-e7d946f65bb9 | -9.05992 | -63.67395 | 2024-10-19 06:08:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7eae7d30-2fe4-3c04-afa8-b569040dcf44 | -9.05953 | -63.67699 | 2024-10-19 06:08:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 76c5ae28-8e2f-314b-9723-450a9081ad7f | -9.05779 | -63.6677 | 2024-10-19 06:08:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e15e5c9-2cee-33ba-b5b3-ea02ce318f8a | -9.05559 | -63.66711 | 2024-10-19 06:08:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5c4f16e7-f60b-37ed-af6f-feddc7956581 | -8.70611 | -63.22075 | 2024-10-19 06:08:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6a1077e-60e4-37d7-89a4-3abaf7000da7 | -8.70168 | -63.21281 | 2024-10-19 06:08:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7942894-5535-3f84-a361-5e9ad8b92e33 | -8.58683 | -63.43559 | 2024-10-19 06:08:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94e803e2-3ca1-39da-9db7-d7b6f4c1c189 | -7.91055 | -63.7195 | 2024-10-19 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 605b2a64-1107-3d92-8915-264f61d0b7d1 | -7.91016 | -63.72241 | 2024-10-19 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38eff2ff-29d3-3bd7-b46b-1fadd86c05b3 | -7.90555 | -63.71876 | 2024-10-19 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 745a90f4-76fc-3803-8030-8cce54e2e4b2 | -7.90515 | -63.72166 | 2024-10-19 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc643c41-a132-3c26-9877-24d363559a4d | -7.90053 | -63.71804 | 2024-10-19 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22e7d438-bdf7-3435-af94-f0ddf39555dc | -7.90014 | -63.72094 | 2024-10-19 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2742d0b0-8575-38a9-89f3-3956c38ca09f | -3.70521 | -64.45322 | 2024-10-19 06:08:00 | NOAA-21 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b268677-52ea-33b6-95c9-806135a2d526 | -3.7036 | -64.55665 | 2024-10-19 06:08:00 | NOAA-21 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13fce2a8-84b9-3677-8323-4d4e9142e07d | -3.68966 | -64.55894 | 2024-10-19 06:08:00 | NOAA-21 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README47.md)
