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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d4d68a4-d204-3ed1-9a55-8fda3eeeabd1 | -8.92228 | -60.74117 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5d982759-614b-30fe-bd04-fe50a01f645e | -8.92614 | -60.7382 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b9d738e-4cb8-373b-94b1-3aec691afa72 | -9.94042 | -60.50178 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88cd7ffb-a89e-3f2c-8de7-b06f8310c728 | -8.9212 | -60.74815 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d346fd24-5577-32b2-90c5-78d434bec560 | -9.47332 | -57.84502 | 2025-08-08 05:25:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| b79fccf3-6c20-3788-8b4e-d672897ef25c | -8.91203 | -60.54661 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08305e98-1a96-3fc2-808c-49fc6bfd56ed | -8.9043 | -60.55257 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c6f0d59-f256-39b8-8c6d-83226ba6710e | -9.71531 | -62.40724 | 2025-08-08 05:25:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bf6c7291-7d84-3af6-9189-e7c4b7d17393 | -9.71047 | -61.3028 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7763bae2-8ea1-3fef-802d-e7750b1a9c57 | -9.93369 | -60.47889 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca846e9e-322b-3fd7-9057-9f8f2bf20738 | -10.00696 | -59.21427 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 64efd7bd-f121-38b2-8282-1fd8744551a7 | -9.94322 | -60.50585 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92aa8344-091d-3e9e-9ba7-e80792097335 | -9.70935 | -61.28833 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9979924c-0afd-346d-bf28-e3045e392485 | -9.93325 | -60.4641 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a6f876f-d46a-34f8-aa87-3d6135f358b2 | -9.92605 | -60.48845 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bad0b89a-c5de-3e33-a5e3-6017d8a9e953 | -8.91039 | -60.55713 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd39ef76-33c7-3b2f-97ee-e396301b356f | -9.71432 | -61.29984 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0faa6957-75e6-3a47-8eae-26deb910aca8 | -8.91652 | -60.58323 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb2b97bc-ced2-3121-ad99-4b2b7782073b | -9.71645 | -62.40014 | 2025-08-08 05:25:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df22f8ce-e9fc-3f5b-b8bb-c998fe1d5249 | -9.93047 | -60.46003 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3849375a-4652-397b-a933-f67572bfe6a7 | -11.19334 | -51.4378 | 2025-08-08 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cfb4f03e-d9f7-3ad1-be80-0ad4c23c9699 | -9.93812 | -60.47231 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a9078ae-9b35-34ed-8b02-a416c6ce822a | -8.91843 | -60.74414 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b69f1b41-bfca-3f6d-86f5-29339429fa3c | -16.36079 | -53.34544 | 2025-08-08 05:25:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bca538e7-1475-3196-960c-df0c8991f448 | -8.92451 | -60.74867 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99b7dc1f-710f-3b81-a11a-e82c4a0948a2 | -8.91211 | -60.58971 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 828acd84-3f98-3d13-8d38-b22269774da7 | -9.7044 | -61.29826 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75d2cc8e-16f0-332e-bd8b-20baf859bf98 | -9.47269 | -57.84935 | 2025-08-08 05:25:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2960f76-9f4a-3228-8b86-73b64719a8e2 | -8.91372 | -60.55764 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9347bc7-90f0-3ad8-94e4-3dd829fb54f7 | -9.93381 | -60.46055 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71901a75-1bb6-3be5-a129-ef589dd576b7 | -15.17361 | -59.32214 | 2025-08-08 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c9fed3d-1a6a-3959-8cf3-2ee10c2049ce | -9.93976 | -60.46165 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85878bc5-3c5b-3ca7-ab74-01bc49a1f717 | -9.9431 | -60.46217 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a35fcaaa-d7b6-3580-929a-adc67c592a76 | -8.91956 | -60.75863 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69533878-8af5-3c3e-bdb6-48702ffcf41c | -8.91598 | -60.58673 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c67a9b5-00ec-38bf-9dce-ea7c614cd9b5 | -8.90762 | -60.5531 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32a8647b-95a9-35d6-aa99-389822d7d2fa | -8.92283 | -60.73767 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90a8b7ca-1919-35d3-a7cc-4c569c3ab0de | -8.92669 | -60.73471 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70f94770-932a-312e-a149-77ba7396aae6 | -9.7088 | -61.29182 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e36b212-acfd-33b8-8ccd-648e380d8518 | -8.90643 | -62.42584 | 2025-08-08 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c90c6c4-b295-3298-8103-8d4fedbaa538 | -9.94255 | -60.46572 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 811ada5d-1e47-3221-84a2-5cd70892153e | -9.93873 | -60.4906 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6789d62c-449b-361f-849d-a042dbaed02f | -9.93151 | -60.49311 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa5fbc3d-2db5-3096-99f6-5fd013adbacd | -9.93988 | -60.50533 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 72a4fb17-36a0-341c-b9b0-9694374b731e | -9.71588 | -62.40369 | 2025-08-08 05:25:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6c8e5704-3ba6-3655-bdbf-17b6ceaa7af1 | -9.93424 | -60.47534 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7fd66471-2ab0-313e-97a0-959d87ab9796 | -7.3731 | -44.6546 | 2025-08-08 05:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 64.8 |
| f1276250-6f4b-31d5-a7f0-618770b72643 | -7.0616 | -59.1586 | 2025-08-08 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| b67a5c16-393e-3e8e-b107-a8e47ff844cb | -7.0615 | -59.1779 | 2025-08-08 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 169.7 |
| 3412071b-1d1f-3b3a-9f10-effa616cbe28 | -16.3662 | -53.3377 | 2025-08-08 05:40:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 6a0cc053-2a27-3579-8293-76f0f72c6d7c | -7.043 | -59.1787 | 2025-08-08 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 236.4 |
| 3411bbe5-1c80-3dc4-a6fb-3fc7f472040c | -7.0614 | -59.1972 | 2025-08-08 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 743a2706-5217-3fd3-ab72-c63d683182ba | -7.0429 | -59.198 | 2025-08-08 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 183.9 |
| d43a0afa-8534-3993-ae29-b3942470996e | -16.3662 | -53.3377 | 2025-08-08 05:50:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 148f0cd6-c4b3-357c-8b0e-8c805a687826 | -7.043 | -59.1787 | 2025-08-08 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 88f78137-169b-3dd9-a7ae-93a8fcb8d98a | -7.0615 | -59.1779 | 2025-08-08 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 105.4 |
| a1fef892-81eb-3600-828f-054f08d8ca9e | -7.0614 | -59.1972 | 2025-08-08 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| e73422b7-d8b2-3dee-b981-c682fdd3d954 | -7.0801 | -59.1578 | 2025-08-08 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| ee64db04-5049-362b-a118-ba2b1fbfa254 | -16.3662 | -53.3377 | 2025-08-08 06:10:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| ef0c0309-3861-3f2d-8cd2-936639accc6b | -7.0429 | -59.198 | 2025-08-08 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 123.3 |
| 63a45658-d00e-3581-b1b5-4488fa5defba | -7.0616 | -59.1586 | 2025-08-08 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 9b018589-6dd0-3666-ab29-71d31aae6851 | -9.71043 | -61.29853 | 2025-08-08 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2be7494c-6395-31ff-b27c-a35e3f25abeb | -9.71114 | -61.29248 | 2025-08-08 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b8347286-28ee-3159-b3e7-10127d9dc080 | -9.70441 | -61.29158 | 2025-08-08 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7e8ce391-598d-38c0-89f2-402e0a694218 | -9.7037 | -61.2977 | 2025-08-08 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 67c0cad2-aa60-3602-a2ee-ae27b16a4ba7 | -8.90891 | -62.43248 | 2025-08-08 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 204ff95a-ae4e-30a0-a2e2-d66d66d0a863 | -9.70719 | -61.29949 | 2025-08-08 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 04b85ba5-f7b1-34a7-a396-8cf8bd5ebd60 | -8.90954 | -62.42761 | 2025-08-08 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff299abf-886e-36bd-b33a-093e166e0261 | -9.70794 | -61.29344 | 2025-08-08 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 837dee47-e16e-3528-a7bb-36a5b643adab | -9.31878 | -62.64578 | 2025-08-08 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81076a36-58a5-3c00-97a2-66bc6c259b3e | -9.31814 | -62.65071 | 2025-08-08 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4646ab97-dd2d-3084-901a-cffa62c31112 | -9.31805 | -62.64851 | 2025-08-08 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ea3e5cb-17fb-30a0-823b-223129616b74 | -9.70973 | -61.30455 | 2025-08-08 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0906e0ab-4a0b-383d-bf9d-dcc252ff08cb | -9.70645 | -61.3055 | 2025-08-08 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e9bdc4c1-a1d0-3e70-b788-32bc85c6e443 | -9.70299 | -61.30372 | 2025-08-08 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 20614375-792b-3be8-9f2a-5bfc4dd3e8e8 | -8.90822 | -62.42733 | 2025-08-08 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ac5a3d53-0fe7-3dd4-b258-b28dd98d580b | -9.71645 | -61.30541 | 2025-08-08 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| deef640f-f8ab-3a37-8f7f-c913b7a66d2a | -8.90762 | -62.43221 | 2025-08-08 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a72a4a0e-e16a-39aa-87e8-05398c3f81d4 | -9.31864 | -62.64363 | 2025-08-08 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ca4c4b6-4a19-38ca-9030-f77e04a2d822 | -9.7087 | -61.28732 | 2025-08-08 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d233aa83-9664-3fab-9e1e-94791338dda9 | -9.7168 | -62.40091 | 2025-08-08 06:16:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 933e0edb-27b6-35f4-989e-5edc5d5a99e3 | -9.92739 | -60.45766 | 2025-08-08 06:16:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 134cd3ad-e5d7-3cc3-bbae-5813e873ea6c | -9.63922 | -67.0014 | 2025-08-08 06:16:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 28ffe1f3-06aa-39e8-865d-ba13878cf5ab | -9.94305 | -60.50842 | 2025-08-08 06:16:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2f09a899-40cf-3c6d-aa9b-e1bc36aa07d9 | -9.94079 | -60.46614 | 2025-08-08 06:16:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd5464cf-90f5-304b-a4cb-b01ac31e998a | -9.93999 | -60.473 | 2025-08-08 06:16:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a189782-d634-36ce-9785-1bae2f30c85d | -9.71618 | -62.40603 | 2025-08-08 06:16:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d97e38cc-fd8c-3ce9-a351-1349f70c3d36 | -9.93597 | -60.50765 | 2025-08-08 06:16:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4f41b14e-199c-3644-aac8-d0e167bd54eb | -7.0615 | -59.1779 | 2025-08-08 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 36c53a6e-4211-34cd-8bd6-f606a6be53de | -7.0801 | -59.1578 | 2025-08-08 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| cbdcce9b-cc5c-35b3-90cc-e313c455f73d | -7.0616 | -59.1586 | 2025-08-08 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 3c45d572-fb30-3662-850b-59e4255b0055 | -7.06041 | -55.41489 | 2025-08-08 06:27:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a03dee09-5359-31c0-a4b0-adb8482c0a57 | -8.90846 | -60.55056 | 2025-08-08 06:27:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 8f348fe8-f2cf-32f8-8f4e-ef18b1b65508 | -9.47236 | -57.84848 | 2025-08-08 06:27:00 | AQUA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4b13896a-ef26-38ec-a979-b3441c0077e1 | -7.05824 | -59.17697 | 2025-08-08 06:27:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| ab1c1c84-cfb8-3705-bc95-e65d71dacb53 | -7.07035 | -59.16641 | 2025-08-08 06:27:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 2507982f-73ca-3232-808d-4eed1f32312c | -7.03774 | -59.17387 | 2025-08-08 06:27:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.9 |
| d1c1e88f-01f5-3be3-91f9-f4c9a05629ad | -7.06862 | -59.16055 | 2025-08-08 06:27:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| c06b78a8-8ba6-3546-a5c6-a368885f9c84 | -9.47386 | -57.83882 | 2025-08-08 06:27:00 | AQUA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| f2130a3c-5407-3b87-9ced-cf0c576cfff5 | -5.80745 | -59.22147 | 2025-08-08 06:27:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |


[Clique aqui para ver as próximas entradas](README26.md)
