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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 410b3f80-3810-3186-8150-c0f6d3d84e5d | -11.49661 | -50.29037 | 2025-08-06 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c307197c-3ad9-3452-b73c-749e08572e79 | -7.81176 | -55.22288 | 2025-08-06 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6d7abfb-41f3-3294-99d0-324b025c337c | -8.91339 | -60.54819 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.3 |
| dd0142e5-4987-3160-95fe-528aaeb1af79 | -9.69642 | -57.42436 | 2025-08-06 05:12:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b655f17-e563-33c8-88cf-2a1e30919f48 | -8.92187 | -60.60553 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 02e8764a-ae51-339a-8f3d-d7512b0819b6 | -11.76105 | -47.5318 | 2025-08-06 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| da10cb97-9228-3116-a1b9-0c6773ce0b88 | -8.90954 | -60.57157 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3313b193-651a-38a8-9b02-9dcb03ec3ed7 | -8.62666 | -50.01981 | 2025-08-06 05:12:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c118132-6eb6-3e2f-aae0-798429df8931 | -8.90798 | -60.5593 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 55766c14-fdad-3c3c-8626-87304026ebfc | -11.37643 | -54.33245 | 2025-08-06 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e83070ed-cb88-3a7f-9673-a7fcb43723c3 | -8.91816 | -60.54097 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.2 |
| e212df70-8c2a-35a3-b652-e01ea4f25e28 | -8.92506 | -60.58607 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b9d45eca-0315-3018-bbd8-eeeabbc2b60d | -9.70621 | -56.09754 | 2025-08-06 05:12:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae8831ab-319d-3e55-b62a-7a023fbce48d | -12.54368 | -47.16825 | 2025-08-06 05:12:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6530e201-0f83-30e7-ae68-c6c708e59729 | -8.99086 | -45.69087 | 2025-08-06 05:12:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6be8c4c3-d2b2-3b26-ae88-b96d1e0a0614 | -11.43976 | -45.14251 | 2025-08-06 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 26.6 |
| c0a2ce45-648a-32dc-8691-eb3fb4458138 | -8.91332 | -60.59214 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 23.5 |
| dda99ebe-cfe0-3445-a088-acb62730dd8d | -11.37797 | -54.33508 | 2025-08-06 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e1a83bf-a46a-3862-a4dd-95884bd0a40d | -11.73472 | -47.54631 | 2025-08-06 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c64d6a5d-8a22-3a57-9aaf-47e258487473 | -8.91549 | -60.75402 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 6029a1b3-3d56-3b05-bc34-f2707cdace55 | -8.92157 | -60.58551 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 744c5a1e-c59f-3250-b1d0-b45121128c68 | -11.72398 | -47.52088 | 2025-08-06 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6fb28076-3116-3ccc-a06b-1b3916ee280b | -8.91614 | -60.75006 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| d6471729-062d-3d60-baaf-3d6d49792cdd | -8.0654 | -49.71856 | 2025-08-06 05:12:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b66823c5-cfb8-3355-948b-a772610bfd11 | -11.72997 | -47.5223 | 2025-08-06 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c2521391-d6e0-3450-a3b8-c1c49735369d | -9.28237 | -57.79422 | 2025-08-06 05:12:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8e92b6c5-fdac-3258-8295-5ce3a7922a24 | -13.69473 | -50.77023 | 2025-08-06 05:12:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| da9cf343-25ee-3464-b921-18a490277344 | -8.92413 | -60.56993 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a9e430d-86d7-3cb2-8c3c-004aba715220 | -8.99015 | -45.69644 | 2025-08-06 05:12:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 57c23bff-eb91-3a92-9102-543a7da5f4c0 | -12.72806 | -46.3936 | 2025-08-06 05:12:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b690bca-d265-359e-b32f-ae281422d790 | -11.90498 | -44.97937 | 2025-08-06 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3a717a16-d5a9-321e-b36f-11b251a80a03 | -11.73622 | -47.53325 | 2025-08-06 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1312ca05-102d-39e6-8114-7e3f7e6db40f | -11.43533 | -45.13039 | 2025-08-06 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| a44d67c4-3d7e-3da6-b8e3-2e97e6b461c0 | -8.5278 | -47.46836 | 2025-08-06 05:12:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 003f65f1-393e-3fc4-baa5-ab6b1097f6a3 | -11.90743 | -44.98444 | 2025-08-06 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a13ec3bb-6584-38d6-8ac8-f270607474eb | -11.8762 | -52.30066 | 2025-08-06 05:12:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3fac532-9dca-3552-90dd-944de275cae4 | -8.926 | -60.60219 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a4835a0-d003-314e-af98-4efc1ff6eb37 | -8.92605 | -60.55823 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00a81ffa-ed74-30b7-8343-eed5c1aff28c | -8.90927 | -60.55153 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 6de5e528-786c-3e1c-a2d3-ccc7dd7ffab1 | -9.69722 | -48.87643 | 2025-08-06 05:12:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 547e6f4d-4497-318b-98c1-05387e19aa95 | -8.90156 | -60.59822 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0e25a77f-31fb-3e0e-88bf-8a69e9ff6d1e | -8.92164 | -60.54155 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 187548d0-a4fd-3d4d-8ea3-0c0776f598d7 | -11.39277 | -55.41144 | 2025-08-06 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64c63e7f-99b9-3472-916f-479ce450ff10 | -12.54318 | -47.17265 | 2025-08-06 05:12:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dfcbdeff-d20b-3144-a183-e4b4c1c7dbc4 | -11.54414 | -62.44324 | 2025-08-06 05:12:00 | NOAA-21 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a1b9748-22bf-3865-a0fb-b5daae33f9e1 | -12.52448 | -47.16927 | 2025-08-06 05:12:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 555e63f7-dd23-34ad-afe9-2ca6cc6231b9 | -8.91874 | -60.73423 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| aa012f07-c846-30ab-b749-2ea2b811f4dc | -8.9022 | -60.59432 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0df8d408-6148-353c-beac-656980c4c7bc | -11.33229 | -47.30339 | 2025-08-06 05:12:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7334d254-e739-3c3f-929d-07b7cedd31fb | -8.91838 | -60.60496 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 32dfc257-121c-3f80-ae01-23a652f9b4a2 | -8.89522 | -60.5932 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6dd46f2-b25a-3e34-8cc4-228793084be8 | -8.91367 | -60.56823 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ce81dffe-c29d-3d71-aca0-a7dac9decc30 | -8.8456 | -47.62095 | 2025-08-06 05:12:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66fb7562-cb8e-327a-9515-dfb4da88774c | -9.70455 | -61.29708 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 946e97d1-7155-373b-a0da-d628f093ea27 | -9.93413 | -60.47524 | 2025-08-06 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 06dbfa18-71af-37a4-be2c-f711ada10aef | -12.52391 | -47.17445 | 2025-08-06 05:12:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cc64c34b-34d3-38f4-8215-63724989164d | -8.91808 | -60.58494 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| af8743e8-8b4b-3598-baaa-be5b0a98c614 | -12.61796 | -54.2082 | 2025-08-06 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8934bb13-a162-3e1e-87e8-f8d2490963ab | -11.03858 | -49.15895 | 2025-08-06 05:12:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 35fae0d8-e520-3f02-a342-967f7e2c928e | -8.62745 | -50.01416 | 2025-08-06 05:12:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6f29ee34-9ce1-31f7-bf5b-e0eaa9152f25 | -9.70305 | -48.87396 | 2025-08-06 05:12:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9d1966e2-f0ec-35cb-8146-c9e012688a23 | -8.87949 | -44.79405 | 2025-08-06 05:12:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 33d8cccc-e103-37b0-8756-3934a1367596 | -8.91587 | -60.57658 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 8d932789-fa65-3ac1-aaf3-8be3dc20bb01 | -11.49119 | -50.29265 | 2025-08-06 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 849bdfbb-8918-321f-8ed1-a09896c1e017 | -11.32225 | -55.22757 | 2025-08-06 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 218e54f0-ef33-3ea4-be0d-fc9f76f3d132 | -12.54269 | -47.17705 | 2025-08-06 05:12:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 29604d84-1e6b-361f-9f4e-16971b6e15ac | -9.5128 | -63.52903 | 2025-08-06 05:12:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df6ef8cf-3cff-3cdb-be49-55f2cc9ea62b | -10.23548 | -56.76645 | 2025-08-06 05:12:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd30c3d6-bef7-377e-8ae5-152999575217 | -8.90256 | -60.57044 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 906d292f-6cc0-390d-b182-7ed241dade11 | -11.044 | -49.15962 | 2025-08-06 05:12:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a01e84fa-119e-308a-ac32-9be35723ea23 | -8.62844 | -50.0201 | 2025-08-06 05:12:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63a2cf8f-000d-34b4-921c-39205c191787 | -11.76663 | -47.53677 | 2025-08-06 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eed829a4-f0e4-31ca-9068-a041987d9e38 | -10.1201 | -51.67695 | 2025-08-06 05:12:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e90cfbf0-1f07-3045-ab13-975bb41d023f | -11.4335 | -45.13483 | 2025-08-06 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 457d54c3-ce21-366a-a8d8-9eaffdba54a0 | -8.90321 | -60.56654 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 3cc5be1e-80e8-302a-9d3f-ce590fa4fc75 | -11.91149 | -44.98564 | 2025-08-06 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 65378ff9-118a-33ab-b495-a50d65394e2a | -8.91211 | -60.55598 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 87a6b558-33d7-3281-8f62-a5608541f3b0 | -10.75762 | -60.74591 | 2025-08-06 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 017ddea0-bd93-3e3d-86b4-feb4ba25e6d5 | -9.18169 | -60.83333 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f4ae5d2-1d15-340f-a416-75d5fff4e066 | -13.69438 | -50.77318 | 2025-08-06 05:12:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 485e1d92-4221-3262-9f98-1326746894de | -8.92541 | -60.56213 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3d44eef-9ed3-3e3e-a4d2-4616a6b49ed7 | -8.91459 | -60.58437 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 1a26050a-d86a-3bbc-b220-af002f08d121 | -8.91175 | -60.5799 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| c243993a-e2ad-3ee3-a9a1-55fcd7f240cd | -11.74227 | -47.53424 | 2025-08-06 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c12ba0ba-3242-3844-bdc1-e3eea8cabbc3 | -8.98966 | -45.69211 | 2025-08-06 05:12:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 89939d7c-326e-3b89-a50a-1cac5ab82068 | -8.91716 | -60.5688 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bb140075-7e49-32fb-946a-e6d735242a7f | -8.90633 | -60.591 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 141.2 |
| ddf02951-9f79-32d4-8c03-eb6279ff3e3e | -9.65533 | -62.93814 | 2025-08-06 05:12:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8e2c5499-2327-3af0-bacc-647952a91314 | -8.9178 | -60.56489 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a905ee27-f072-3f63-9f70-c665e15e1277 | -8.90605 | -60.57101 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 923f7eab-3a8c-3e59-a4d8-212cacda2714 | -9.46725 | -57.85184 | 2025-08-06 05:12:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 4c3803dc-cb3c-326e-ba3d-39b87b7380f6 | -11.48742 | -50.2891 | 2025-08-06 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa56d766-ca5d-3520-bb34-627cb0e38e02 | -13.49518 | -47.73601 | 2025-08-06 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b87d0d8-2d83-389a-8875-ebf85b88519d | -8.90505 | -60.59879 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| d779b020-bf40-36a2-945c-74548b830732 | -11.50708 | -50.28881 | 2025-08-06 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 069e5db8-5740-3bf7-bdc3-41095c5104e8 | -11.90025 | -44.98444 | 2025-08-06 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 48fee3e6-ba20-302d-aa5a-7a1d7f408da6 | -8.90284 | -60.59044 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d036e764-c414-3fb7-943e-e762812a4d77 | -8.83431 | -47.61749 | 2025-08-06 05:12:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21a32aa3-5774-33cb-8732-9bac8fe9eb20 | -8.8398 | -47.62004 | 2025-08-06 05:12:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08c28f86-7283-3b72-96d6-866b4ded0bac | -11.32717 | -55.21939 | 2025-08-06 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README24.md)
