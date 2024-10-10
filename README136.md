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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7ce4258-c439-35ff-a57e-d62dded6dfce | -9.63659 | -59.09156 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 123f0f34-4b41-3f09-a2ba-2afb98dbc3db | -9.55945 | -58.96283 | 2024-10-10 05:38:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c3c6b3f-a3cf-3bc2-86b7-605dfbbada7d | -9.55892 | -58.96657 | 2024-10-10 05:38:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4ba917a-ba3a-37de-9d8f-4f5cb07bec15 | -9.55116 | -58.96181 | 2024-10-10 05:38:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 140c7505-9516-3710-b371-18122461c647 | -9.54703 | -58.96115 | 2024-10-10 05:38:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 18498eed-babe-372d-b96f-a1448e069452 | -9.51453 | -59.50595 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4517d3a4-b8c1-3eb6-a507-6a3060050a56 | -9.46703 | -59.02916 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 888f2493-15e4-370b-9847-80f009d0869a | -9.4665 | -59.03284 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d57fcdb6-df6d-35ed-9f12-25e63bf99eab | -9.44939 | -58.94654 | 2024-10-10 05:38:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87a16da0-041d-300b-aae8-e14eb2b75743 | -9.44886 | -58.95028 | 2024-10-10 05:38:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1964042-36b3-3e1b-85eb-18bfe220d4c2 | -9.44526 | -58.94596 | 2024-10-10 05:38:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be6dbfcb-4377-3b45-8d32-06dc8ed8f180 | -9.42935 | -59.0877 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a369b054-1403-3858-bc21-c728a3f10b1f | -9.36971 | -59.39117 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6c9a2e5-1a1e-35a0-8c04-bd6173df1677 | -9.3676 | -59.52011 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 578c475d-fa44-3d35-95fa-547e8db53547 | -10.41024 | -59.1493 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbf01e3c-4e84-37f4-bdc5-665b127ad313 | -10.40664 | -59.14492 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f05fc2f1-72f0-3424-a4b3-4801bc471d5e | -10.40358 | -59.13672 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7dc32020-c2a5-3ef7-9df6-d6a9ac8aa21e | -10.3879 | -59.51714 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 63f1eda5-67c8-3588-87c9-dd07ff0ce99f | -10.38743 | -59.52055 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f18036a7-cb26-3a40-aa3f-c32adf2bf18d | -10.20082 | -58.76529 | 2024-10-10 05:38:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddb702ed-5b57-3448-95b7-901c648976f7 | -10.11708 | -59.01929 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53009bff-cde6-3b11-87c6-54410426057f | -10.0607 | -59.3557 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 69b83d29-d0b7-392b-a7af-57e63597e78e | -10.06018 | -59.35934 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9b83bf2-2dc3-34ab-ac14-b7acc2d51481 | -11.67746 | -59.89492 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ffe4410-70ca-30c6-a30f-de8802f83060 | -11.67296 | -59.89789 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8fc907cb-0d66-3746-b40b-a9b35eae296a | -11.66896 | -59.89727 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d89debd-16ac-3e49-93dd-3493a0ad8718 | -11.66847 | -59.90086 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f338067d-9601-30b8-87df-d50071084333 | -11.57633 | -59.99168 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d304c51-7896-3fd8-82ed-fd1a45798cbb | -11.57297 | -59.98674 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 17b4cb3b-7383-38cb-ac2a-2ba4c3641dd5 | -11.13156 | -59.09188 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1eba7c9d-d078-3094-a613-a4098ba2d67e | -11.12735 | -59.09141 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3fb3ee02-6d6e-3664-9b19-a7dbef1b8631 | -11.12683 | -59.09527 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ddfccced-8cb6-34f3-8333-34eebb1281f1 | -12.32102 | -59.16668 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3631c3c2-9b44-3ed2-ad32-ef69e083b62c | -12.32048 | -59.17069 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9eb9424-b24c-3afb-990a-6c8205d8a47a | -12.31625 | -59.17002 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bce70a0a-e180-34f5-bdad-8487f1e22484 | -12.30779 | -59.16864 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7e43e0af-6fea-3f64-8131-fcb17ae17b2a | -12.30725 | -59.17268 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fdb16989-b6db-373d-b723-dbf3d552d51c | -12.30671 | -59.1767 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a15facf6-baff-3e90-8fcd-95adac32c9b7 | -12.30302 | -59.17199 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9ddfed63-e0af-3f0f-a3b0-b15b8a23704c | -12.30248 | -59.17603 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e5371e7d-a9d5-3a60-8be1-0b3712d7f1e8 | -11.89684 | -59.45381 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb798c4d-749e-3697-9353-b197b39fb87d | -11.89271 | -59.45318 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82096d7f-a05e-345c-9e0d-c51f78f51b08 | -11.89217 | -59.45698 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46258f16-a641-3ad5-90ab-c6d5c2c3073c | -11.82008 | -58.85016 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 40b4c8fe-d727-31bb-bfe8-3a386b2a0740 | -11.8169 | -58.84121 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 706e91a5-aa2c-3ec1-bd10-85f5a1541c07 | -11.81634 | -58.84537 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 69799b12-31e0-3976-a7c6-db8e95398040 | -11.81579 | -58.8495 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 116dd88d-37fc-3fb2-9b87-5f1bc048e3a0 | -11.8126 | -58.84055 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d96b28b6-4e99-357d-9823-9c7a4b81b457 | -11.81204 | -58.8447 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a60cb9e4-62fe-3af0-a332-1b5a04f7a5ba | -11.81149 | -58.84883 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 83caed6e-0115-3728-b0b1-423dc5d4b422 | -11.80774 | -58.84403 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01d18b0a-7578-38ac-a3e4-d58bdbf0667d | -11.72186 | -59.29304 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28e9b0eb-858f-3392-826c-ee56b34351ce | -11.71404 | -59.28798 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f10ba74d-0d6b-31ff-baf1-745dfb63e8f7 | -11.7131 | -59.28413 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5c9a721-6b95-3fa6-9767-fe3f1c55d0ee | -11.71256 | -59.28798 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 641d46cc-edbb-3744-a1ad-43ee39acdbf4 | -11.71202 | -59.29181 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eaf86df5-49bc-36c9-9578-d8f55af7accd | -11.71038 | -59.2835 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f079cfda-65a0-30e8-bf28-d35c87bc3ffe | -11.70986 | -59.28737 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9bc94845-0ef1-351b-a80e-0c78d8008cbb | -11.70893 | -59.28354 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0400451-29cb-348b-af55-f35cbe682adc | -11.70838 | -59.2874 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 441a8bc9-68aa-300f-91f3-a3ecda14df72 | -11.67184 | -58.89191 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a4912c9-c97d-37b1-83b5-67ac96fc901a | -11.67129 | -58.89606 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ee8c0cd-5791-39be-8884-63dda2878b02 | -11.66757 | -58.89124 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad707af6-e986-3fd9-983d-daa37f4ec1d7 | -11.66702 | -58.89542 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 546b0b64-8482-3715-8e6d-212eaa0fdefd | -11.66648 | -58.89948 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 662f2c8f-bbed-3238-a4c1-2950b3a0fb2d | -11.57303 | -58.95462 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f9d1fcd8-0537-3d14-88a7-41a856acc426 | -11.48871 | -59.09912 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2835d4bf-9416-39ad-a5a1-b6430d50ba31 | -11.38004 | -59.19593 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c75c793f-928c-3678-89e2-a9fa310a8083 | -11.34011 | -58.98629 | 2024-10-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 23fa8c47-9f27-3521-8da0-5f9877a10dff | -13.74621 | -60.59561 | 2024-10-10 05:38:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 353586e0-a423-3663-a521-505a81569624 | -13.74551 | -60.60077 | 2024-10-10 05:38:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| f89e1292-1903-3b53-a82d-f177520b80c5 | -13.74156 | -60.60019 | 2024-10-10 05:38:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7fa10e9c-169c-370b-8272-929e1fa4e436 | -9.2582 | -60.27651 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffd5241b-d278-3ab8-af2b-dd96dbfbd02a | -9.25752 | -60.28115 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e40e86ca-c857-3423-bac9-60f176ae821c | -9.24729 | -60.48204 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fee39206-d508-3233-b262-4e056fc8c972 | -9.24423 | -60.4769 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e67b16bb-2393-3ffd-b655-a5c7d5b67620 | -9.24355 | -60.48147 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9dbf3385-a1c6-3123-abc6-905ab88eb80f | -9.23981 | -60.4809 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d1b1773-5569-372d-b78c-cf987337ff47 | -9.23941 | -60.45757 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ddf59fc7-e5db-3822-89f3-164a2ef36618 | -9.21386 | -59.78127 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99d1c869-c817-3705-bd47-f6ffe350f5c0 | -9.20996 | -59.78067 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff262a39-44c4-3f33-ac13-d9ea9731cd53 | -9.1857 | -60.3511 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 690a7483-d462-3b48-aff7-18c966ebb875 | -9.18505 | -60.35572 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 440cdce5-e80e-3d3d-bb54-99271b35cea8 | -9.18481 | -60.35367 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56e49800-e1c9-3ef2-99bd-2de9b25fe7ca | -9.18193 | -60.35053 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 214b52a6-cbee-39a9-989c-fd93eb246e8c | -9.18128 | -60.35514 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 755f1873-afe1-3590-b935-083feaee9edc | -9.18104 | -60.3531 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 25f4862a-58dc-3686-8058-977ef6b0c641 | -9.18036 | -60.3577 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02fd634b-8d21-3fbb-bef0-2b86c2de7311 | -9.17659 | -60.30515 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9379a6e0-4664-3077-8101-2f9f4931c15a | -9.17281 | -60.3046 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17685110-9032-3371-a82d-160eb7293c44 | -9.05115 | -60.45521 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 45c3524a-2f36-32aa-9c3c-09035f651f00 | -9.03053 | -60.58361 | 2024-10-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8038a901-7315-3097-ac86-c6aec64e2510 | -10.37891 | -61.25551 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 865ff961-c304-35c4-b47e-e65848349123 | -10.37651 | -61.24646 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 568f491f-fc20-3bc1-adec-e612c5983fbe | -10.3759 | -61.25068 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5923c3bc-c9b4-3bb1-8495-23c1f922b2a3 | -10.37529 | -61.25489 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f984eed-131f-3fe0-8767-b9509397c88c | -10.37351 | -61.24142 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e00a8307-e55e-3923-ab97-14a4a65ac927 | -10.37288 | -61.24585 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b542cd62-8c7a-3103-8feb-6f8d2b222278 | -10.37227 | -61.25005 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 022cd8ab-c080-3c38-961c-3b10846529db | -10.37166 | -61.25425 | 2024-10-10 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README137.md)
