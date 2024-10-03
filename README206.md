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

## Dados Diários - Página 206

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3349fae8-b94c-39d4-a631-4212cbc36746 | -22.3711 | -47.9225 | 2024-10-03 08:17:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 0b494b08-bb0f-3ad3-8dcc-b717932aa962 | -22.3719 | -47.8987 | 2024-10-03 08:17:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 9202c70c-e69a-3a20-8db0-8408012133da | -22.3921 | -47.9172 | 2024-10-03 08:17:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 208.4 |
| 688f24b3-c3a9-3ba2-bc7f-78f9266242fb | -22.3928 | -47.8934 | 2024-10-03 08:17:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 176.8 |
| 5bb0dd97-9728-3fb1-9e44-13f8b5217f76 | -9.0515 | -67.871 | 2024-10-03 08:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 52f98215-974f-372c-859c-f6007591e391 | -12.4038 | -63.0009 | 2024-10-03 08:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 201.0 |
| 99414fef-9c7b-3423-a439-76ff316f8c6d | -12.404 | -62.9817 | 2024-10-03 08:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 6d6f55e1-761d-3b84-9e4c-ca921f3515b3 | -12.4227 | -62.9999 | 2024-10-03 08:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 264.3 |
| 0c3b0e97-78fe-3487-8d30-7a7218827d67 | -12.4228 | -62.9807 | 2024-10-03 08:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 127.4 |
| 400d3dd5-a725-3702-9679-8599986f4593 | -12.4416 | -62.9988 | 2024-10-03 08:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 13263a78-afa4-3c28-871e-2f18c85e0563 | -12.8996 | -62.4913 | 2024-10-03 08:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 555c51da-faf2-37f9-b7f8-6b64ee716cb1 | -12.8998 | -62.472 | 2024-10-03 08:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 5be05af8-ee74-3102-965a-c4eedd1154a0 | -12.8999 | -62.4527 | 2024-10-03 08:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 08c7f434-27b9-3231-b5f4-da8763378a3b | -13.0594 | -51.1409 | 2024-10-03 08:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 39.4 |
| cc5c1098-5f5f-3872-b93c-68cb9f548cfd | -12.9741 | -62.6409 | 2024-10-03 08:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 893d4dda-1cce-3c07-80ee-304c7d7e463c | -16.1094 | -50.4489 | 2024-10-03 08:26:36 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 396e1d76-c108-3d6b-911d-35765baa5a47 | -16.1098 | -50.427 | 2024-10-03 08:26:36 | GOES-16 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 79.2 |
| ac1572e8-2180-34d0-acd2-a751140524b8 | -16.5317 | -57.41 | 2024-10-03 08:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.1 |
| 0058f8ad-b23a-3c01-be21-8aadd81ea508 | -16.5509 | -57.4282 | 2024-10-03 08:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.0 |
| 0e170ab9-a4cd-30de-9768-bb73106c7faf | -16.5512 | -57.4078 | 2024-10-03 08:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 180.0 |
| 6a94fc00-aac0-32de-a898-bd290e9b37db | -16.5733 | -57.2419 | 2024-10-03 08:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.0 |
| fe7a1244-53fc-3132-a720-acf8a0a4b3f5 | -16.5928 | -57.2397 | 2024-10-03 08:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 144.9 |
| d0f2d695-939d-38f7-ae9e-841bcb938f61 | -16.5931 | -57.2192 | 2024-10-03 08:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.5 |
| 8006b5ba-632e-3f82-9eaf-0a2187b86aeb | -16.6127 | -57.217 | 2024-10-03 08:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.9 |
| 771c1634-7dd7-3732-9f6f-c877afd9aa77 | -16.6326 | -57.1943 | 2024-10-03 08:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.6 |
| 686c6afb-8045-3571-8320-eeccf6ef9ee5 | -16.6698 | -57.3126 | 2024-10-03 08:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 130.9 |
| c2c4a9d4-780d-3eb3-af3f-4ead58c8528d | -16.6723 | -57.1488 | 2024-10-03 08:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.5 |
| 3701a3fe-5549-3878-95ba-aad3fa0d0865 | -16.6868 | -57.4741 | 2024-10-03 08:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.8 |
| 1c6039a4-9f1c-3ace-9814-8487cd6eca38 | -16.6893 | -57.3104 | 2024-10-03 08:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.0 |
| 6b656ebd-bc01-3fd2-9172-1146bbacabfc | -16.6919 | -57.1465 | 2024-10-03 08:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.7 |
| d90cadb9-c04e-3894-82bb-e332e15fe183 | -17.0692 | -56.7939 | 2024-10-03 08:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.3 |
| 3f308560-80f0-31e7-a6a5-b3fa9cd35a39 | -17.0695 | -56.7733 | 2024-10-03 08:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.7 |
| 24c86029-906e-3d0d-962a-51e6d6afcb44 | -17.0888 | -56.7915 | 2024-10-03 08:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.1 |
| 9b6bba04-db67-3f75-8bde-bf895a429050 | -17.0892 | -56.7709 | 2024-10-03 08:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.5 |
| 2727329f-3b4a-342e-b6ce-e0216ad3880e | -17.1574 | -57.3993 | 2024-10-03 08:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 118.3 |
| 42d959db-6279-3681-9109-ba2b5d7f9bdf | -17.1577 | -57.3787 | 2024-10-03 08:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.6 |
| 0b5f3d1d-a669-3b78-b010-2b074986b71a | -17.1771 | -57.3969 | 2024-10-03 08:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 315.6 |
| d71463b6-fc7a-3c66-a8d1-bc5b44ddb9f8 | -17.1774 | -57.3764 | 2024-10-03 08:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 231.4 |
| 1f34e221-f44b-3fb3-8abd-7bbc1987d3c7 | -17.197 | -57.3741 | 2024-10-03 08:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.7 |
| add19296-83a1-3503-9b85-d3e4d188bd60 | -12.4038 | -63.0009 | 2024-10-03 08:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 125.6 |
| a84c29c5-0039-3890-ae87-6c2b3c6a4deb | -12.404 | -62.9817 | 2024-10-03 08:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 77.2 |
| f624e154-f8b8-3942-bea5-0c2424a78a94 | -12.4227 | -62.9999 | 2024-10-03 08:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 275.4 |
| 3f96603f-28f1-3f14-9ea3-183599bda671 | -12.4228 | -62.9807 | 2024-10-03 08:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 161.3 |
| b53dbab5-f445-317e-aa0c-afcb5c93b1a4 | -12.824 | -62.4766 | 2024-10-03 08:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 9c7cf63b-c547-3beb-aae9-39ebbe432869 | -13.0594 | -51.1409 | 2024-10-03 08:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 6e65c4a6-7ba3-34c8-936f-caf990f83aab | -12.9187 | -62.4708 | 2024-10-03 08:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 8ec1d5ba-ec3b-39da-8903-b07697a30129 | -12.8999 | -62.4527 | 2024-10-03 08:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 769347be-0046-33b4-90df-bef953b56281 | -12.8998 | -62.472 | 2024-10-03 08:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 80.8 |
| c49ee246-bc9f-3122-88de-8d71338ece79 | -12.881 | -62.4538 | 2024-10-03 08:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 4259e7fd-eefc-3e52-b51a-c38bc9720058 | -16.5512 | -57.4078 | 2024-10-03 08:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 234.6 |
| 9656f6d6-4b71-32ac-b8ae-09fe4d8650cb | -16.5509 | -57.4282 | 2024-10-03 08:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.2 |
| b3814230-9166-397b-9fb6-6ef3c475d571 | -16.5317 | -57.41 | 2024-10-03 08:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.2 |
| 43e6394e-8065-307b-97db-14818cb5d803 | -16.5931 | -57.2192 | 2024-10-03 08:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 120.7 |
| a691bdf4-0a5b-39ea-9a48-7b161216e1ad | -16.5928 | -57.2397 | 2024-10-03 08:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 191.8 |
| f6df730f-048c-3cf8-affc-1fff80087b10 | -16.5733 | -57.2419 | 2024-10-03 08:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.5 |
| 74c391a2-f140-3230-ab3c-dc8b5ca6d471 | -16.6127 | -57.217 | 2024-10-03 08:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.1 |
| da251f02-66e6-34a9-82a3-c1da90817c2b | -16.6893 | -57.3104 | 2024-10-03 08:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.8 |
| b8359002-7ba6-31b6-acad-eaf06f4f69ec | -16.6723 | -57.1488 | 2024-10-03 08:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.1 |
| c68fbfc8-eda9-3535-839d-fdb5b7d08fa9 | -16.6698 | -57.3126 | 2024-10-03 08:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 138.5 |
| 912e6d96-755a-3114-af85-f59e72d59abd | -16.6496 | -57.3558 | 2024-10-03 08:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.0 |
| eb14d0be-3e5c-3d1d-a973-65d09ae1714a | -16.6492 | -57.3763 | 2024-10-03 08:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 273.2 |
| 5f564f81-afb5-32d7-9106-c2fbc3c17ad0 | -16.6489 | -57.3967 | 2024-10-03 08:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 143.5 |
| 0334bdc2-94e5-352b-8ce0-925599a7ab73 | -16.6297 | -57.3785 | 2024-10-03 08:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 223.8 |
| 8733a326-c88c-3ba1-95b7-52142e513cab | -16.6294 | -57.3989 | 2024-10-03 08:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 120.9 |
| d289960d-8d15-3c28-8c5a-f97cbcd3b7a4 | -16.613 | -57.1965 | 2024-10-03 08:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.5 |
| 594facee-1cf5-3678-8343-252ec09d979a | -17.197 | -57.3741 | 2024-10-03 08:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.2 |
| 1fa9f921-fd19-3852-9196-bdff339c2c1a | -17.1967 | -57.3946 | 2024-10-03 08:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.0 |
| f53c5f8b-b97d-30a3-b479-9f5374796b64 | -17.1774 | -57.3764 | 2024-10-03 08:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 235.8 |
| d1b316c0-2738-3694-add9-7008b134da9a | -17.1771 | -57.3969 | 2024-10-03 08:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 278.1 |
| ebd90ba1-6853-331b-8743-708175689c0b | -17.1577 | -57.3787 | 2024-10-03 08:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 148.5 |
| 0e401cd1-b300-3cac-a609-255528b5ea1e | -17.1574 | -57.3993 | 2024-10-03 08:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 180.2 |
| 297e109e-8d68-3d5b-9d0b-52f20ebfb328 | -9.0515 | -67.871 | 2024-10-03 08:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 89efdcbc-cba0-335b-8481-085901272d26 | -12.4038 | -63.0009 | 2024-10-03 08:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 186.9 |
| 0ca37ca4-bc09-3a1b-8c50-deb120dbbb93 | -12.404 | -62.9817 | 2024-10-03 08:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 103.0 |
| bb808688-51d3-39eb-8540-8be8ff0315a6 | -12.4225 | -63.019 | 2024-10-03 08:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 73.4 |
| bb9cae19-a7f7-3b36-a4f5-0782d0666d9b | -12.4227 | -62.9999 | 2024-10-03 08:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 259.4 |
| eba34af3-5505-32d0-b3d5-2e9b3b0690a0 | -12.4228 | -62.9807 | 2024-10-03 08:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 127.2 |
| d0ad4dfe-26fc-3d15-bc62-22b4f94acb0a | -12.8049 | -62.497 | 2024-10-03 08:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 64.9 |
| b47215f0-8e89-3031-ba8e-6b6c307d21bb | -12.8996 | -62.4913 | 2024-10-03 08:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 2eaefefb-edc0-3ce4-8d7b-6ef175235cee | -12.8998 | -62.472 | 2024-10-03 08:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 95.4 |
| e6df40eb-3d9e-3634-9886-376b4d0985e9 | -16.5387 | -58.2427 | 2024-10-03 08:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.2 |
| abc25674-84e3-3439-9099-bfc0e297e046 | -16.539 | -58.2225 | 2024-10-03 08:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.8 |
| 63ccf84c-3049-38a6-8d20-6b8c40bc9792 | -16.5393 | -58.2022 | 2024-10-03 08:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.7 |
| 531ff8d3-66cc-33e3-980c-22d124fcdae6 | -16.5509 | -57.4282 | 2024-10-03 08:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.9 |
| 31e04fc8-1bd3-389b-b6fa-7a6228ac7756 | -16.5512 | -57.4078 | 2024-10-03 08:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 159.2 |
| d666d7af-bb92-3edc-a318-98e536506c5f | -16.5317 | -57.41 | 2024-10-03 08:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.4 |
| 8a47e3c1-5971-39af-8b7e-e3943ef34b60 | -16.5582 | -58.2407 | 2024-10-03 08:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.3 |
| 97501439-5031-379f-bbde-c34b321fafab | -16.5585 | -58.2204 | 2024-10-03 08:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.2 |
| f2c7dfbf-1686-3f00-b607-d65b32fcb189 | -16.5588 | -58.2001 | 2024-10-03 08:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.1 |
| dd800469-342e-31be-8f04-fdb812027c8b | -16.5733 | -57.2419 | 2024-10-03 08:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 118.7 |
| e0e36b72-0e6d-3969-8a50-4f8d050d7eeb | -16.5928 | -57.2397 | 2024-10-03 08:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 221.0 |
| 5bf1f1f8-61f9-3a8c-9912-c277dd47d8c5 | -16.5931 | -57.2192 | 2024-10-03 08:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 145.4 |
| 5bc7e3e7-6952-327a-9f66-494588cd96ba | -16.6294 | -57.3989 | 2024-10-03 08:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 117.4 |
| 33ed62f0-3095-3404-a6ba-ad0e8801ecc2 | -16.6297 | -57.3785 | 2024-10-03 08:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 232.8 |
| fdc84b7b-c646-3922-a333-6b272344b1d9 | -16.63 | -57.358 | 2024-10-03 08:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.1 |
| 5ba805c8-2f74-3bfb-8d69-32f691b4c8f6 | -16.6723 | -57.1488 | 2024-10-03 08:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.1 |
| 3e5d688d-fcc4-318f-9d4c-a09f4cc471cf | -16.6868 | -57.4741 | 2024-10-03 08:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.9 |
| 4654a1e7-be5b-31f9-81c8-406092edad92 | -16.6893 | -57.3104 | 2024-10-03 08:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.6 |
| f45a7187-2576-30ec-9cb4-c83eff8f41cd | -16.6489 | -57.3967 | 2024-10-03 08:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 175.3 |
| 00220d43-d1d4-3954-ba98-7faf62e2409e | -16.6492 | -57.3763 | 2024-10-03 08:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 435.1 |


[Clique aqui para ver as próximas entradas](README207.md)
