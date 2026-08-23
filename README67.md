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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6a27325-c56a-3428-bf6b-d1db610c1d2a | -6.81259 | -59.65335 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| baf80fab-66fa-3e70-8060-52c4154878b9 | -6.7672 | -58.66648 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b147cda5-5f2c-3c64-a223-9a850e2f6ed3 | -8.69592 | -62.87794 | 2026-08-23 05:50:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de0ae779-9cc3-340f-9c81-8d3ab610afd3 | -9.16686 | -59.46549 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 27e53e8b-cce9-339a-baae-9096e039f1f7 | -9.04106 | -60.44702 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c7339261-b0e1-3d45-9fd0-ef99345361a9 | -9.23306 | -60.38528 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 185fc484-61d6-305c-82a5-c95ca164e189 | -6.79429 | -59.43435 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| de19b15e-c7ef-3c83-9a52-2bbc9cfe68e0 | -6.79601 | -59.59863 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d075e3ff-9f65-3978-a03b-e24c70ac999a | -9.15143 | -65.95485 | 2026-08-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea300df2-8f89-34a3-84ac-6b77498154e0 | -8.90158 | -60.54369 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0903e04f-5c65-3cc8-96da-9bbd43fef166 | -8.53565 | -54.8433 | 2026-08-23 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5b2ded96-182a-327a-808c-46f2afbabf72 | -6.78743 | -59.66018 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d7c63af9-13fa-36d4-9d72-595c43ae0a4b | -8.92425 | -60.71999 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2fa30c1f-84a5-398b-bf0c-9f2769a00a07 | -9.16617 | -66.11746 | 2026-08-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f8665f4f-1b1f-3e3b-bcac-033b91c8f164 | -6.76549 | -58.6785 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97ad5731-1480-313e-9e6f-549e345d5e35 | -6.82064 | -59.66491 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8566e145-1bb9-33ab-9e74-be7ddce5c759 | -6.93899 | -59.07704 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4e53a72f-b61f-3ba8-9f70-6e765962e341 | -9.12669 | -61.59156 | 2026-08-23 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dae9eb57-9800-381f-97ae-311054625c0b | -9.65288 | -63.83735 | 2026-08-23 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87ab0ba4-21f0-3bf5-9d54-c7e81ad35f46 | -9.21419 | -60.89435 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f8f9a70-0593-3f32-8959-b22772106997 | -9.84454 | -60.2812 | 2026-08-23 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9abdc281-8bab-313c-adb5-a2318f0369e7 | -6.78813 | -59.65512 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ea0ce658-759c-3a77-a955-f94bed5bbf70 | -9.40504 | -60.31662 | 2026-08-23 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8aeaed87-eade-38a5-ab54-77dec9498bf9 | -6.76508 | -58.68145 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1880d67-0a74-355c-b521-c35e6f93ad15 | -9.06631 | -60.43547 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9be1f5b9-2f70-32fc-8e64-ea4655b021e7 | -6.82974 | -59.95739 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 16cc4044-8ca8-3fa2-a85b-685a420180b6 | -6.67557 | -58.73134 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ec2cfb9e-8c91-38ee-b797-e3eade2535e5 | -7.32052 | -64.70703 | 2026-08-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ca41b0f-abca-3700-86bb-ae5831fc6f6f | -6.80148 | -59.59425 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5b30e2ef-634d-3ed1-9651-9b6185eea821 | -7.68463 | -63.35019 | 2026-08-23 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b247f5ff-4447-3391-9d01-04a05792953a | -6.76367 | -58.6813 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0dafa64f-a8be-3ba1-a387-e1a8c98154c2 | -6.76425 | -58.6873 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28984b9c-d910-3f04-afbd-bac3cbf747c6 | -9.14069 | -65.95695 | 2026-08-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d482a771-b8ce-3912-bd7a-979aa36ed50c | -9.40932 | -65.94455 | 2026-08-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5647cada-ecbe-3c6a-bacb-474e84911b80 | -6.80367 | -58.65351 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f40a029a-578a-3ee1-94bf-8609ac94745f | -6.77843 | -59.44258 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f0634b1b-9acb-3bd3-ac90-2a78ac793723 | -7.67225 | -63.32962 | 2026-08-23 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2dbe91c-51d0-3e3a-9935-b7a601120c5e | -9.86144 | -60.11848 | 2026-08-23 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f70e2704-78bb-3d35-b0cf-3901344f6e4d | -6.67012 | -58.7336 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 391485e2-4b17-347e-9311-2edd11f70de8 | -6.67778 | -58.75292 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c42fa221-462e-3f84-a7c2-a93e28c49b8f | -6.80263 | -62.90357 | 2026-08-23 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 175d14bc-1344-3509-ad2f-4c4bd632d973 | -6.96804 | -59.05903 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 77f44380-4dd1-345b-b24e-d12fd58b7ae9 | -6.9509 | -59.07361 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1594351c-d4a8-3a8c-9f7b-1aa70fccf73d | -6.76794 | -59.45003 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b50fa973-a43a-3389-b366-8cca1720c255 | -6.6907 | -58.73362 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3185b8de-c601-3378-ad2d-6036bc3ee2c8 | -6.55714 | -55.09739 | 2026-08-23 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7d1b4cf9-b320-3024-8f5c-994602aa68be | -6.68102 | -58.72914 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2d8dd827-5209-3da3-b7e5-c8284c868e2b | -9.14464 | -65.95381 | 2026-08-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6d546fe-369b-32b6-ba15-bd233f813cb3 | -6.76608 | -58.66332 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f2cff30a-2843-3456-a325-531a6ce6195f | -6.97642 | -59.07164 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4152fb71-faac-31a7-82cb-c2a280eb5e9e | -6.66639 | -58.79881 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a7ac7b2-a5f0-3e3e-8c59-2b6781fc7a36 | -6.88451 | -59.41589 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f4b2df68-4435-35fb-9784-c91bca4a48c8 | -6.77036 | -58.67001 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0570fa5e-e460-3000-93c9-7c088be7d267 | -9.04172 | -60.44209 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e2d35869-892e-336a-a517-4a4ad86480ef | -8.95286 | -60.5803 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9e4808c7-3dfb-3732-8df8-84bc227666d2 | -7.67066 | -61.11078 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fc561a36-9e33-3548-913e-54e251848296 | -6.80285 | -58.65952 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9f6c9e7a-fbd3-3e4a-b682-4dd0e1b320e2 | -6.60421 | -58.38865 | 2026-08-23 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4617b4c-db78-3d97-a7fb-2d4d2eeccd44 | -6.6685 | -58.74549 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| a8de509c-3267-3563-821a-460228abcdf1 | -9.15491 | -59.55631 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3c649fdc-358e-39c7-acea-b6a9b284deba | -9.32657 | -68.8942 | 2026-08-23 05:50:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e5061268-4f6f-3b5b-a644-8b9e3c7a0475 | -8.53503 | -54.82464 | 2026-08-23 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 806d53c8-04bb-30b1-8132-d0c082e48b56 | -9.17259 | -59.46046 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a2bc92b-7641-3776-8e16-d4cf96f077fe | -9.14915 | -65.94698 | 2026-08-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c96322f1-ceca-3757-b7f9-09fca1514740 | -6.81986 | -59.42722 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6d32c9ee-b6c1-3039-8a6b-9908ec2b38c1 | -9.10466 | -61.59234 | 2026-08-23 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2bdfb4bf-0fcf-386f-a39c-5257539ec1fa | -6.84024 | -59.45717 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6b892a85-ea69-3f15-9621-6784f7236741 | -14.49681 | -59.82495 | 2026-08-23 05:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad98bb02-77a0-381f-b941-3d3c7579e217 | -14.49646 | -59.82787 | 2026-08-23 05:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d38feee2-5719-35b9-bc1d-9d0142fd01f9 | -14.50165 | -59.82895 | 2026-08-23 05:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f371187-5266-374b-baad-b07cb4179477 | -14.50199 | -59.826 | 2026-08-23 05:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d06cd996-f3bc-35e9-ac46-0110e41a1fc7 | -14.50614 | -59.83582 | 2026-08-23 05:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76dafd22-bc4d-3353-908f-96d41aebfc81 | -14.50097 | -59.8347 | 2026-08-23 05:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be6bc799-091d-3ecb-9040-b4c661823a61 | -14.50062 | -59.83759 | 2026-08-23 05:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a0b1f2a-6398-3d93-8a2f-0747b5da7332 | -15.73038 | -56.01658 | 2026-08-23 05:53:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 1e2da3ec-fa46-35c3-8897-b0fb734c1403 | -10.4713 | -49.9838 | 2026-08-23 06:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 574e7633-ac43-374b-a831-1c070fee3aee | -10.4716 | -49.9624 | 2026-08-23 06:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| e2e9ef50-a70c-3b05-b506-94d281ea62c2 | -6.8062 | -58.6469 | 2026-08-23 06:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| c362b3f2-ffb8-3457-a90c-2872a4785470 | -6.6765 | -58.7492 | 2026-08-23 06:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 138.5 |
| 09dd7622-c75e-3363-a73e-c25e34d66f87 | -6.695 | -58.7291 | 2026-08-23 06:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| e39c6216-29cb-3452-8fc7-17728956ce41 | -6.9699 | -59.0658 | 2026-08-23 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| b13d1d06-7e5b-32e7-a787-2925d0cf7b66 | -6.9514 | -59.0666 | 2026-08-23 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| ce73d3a5-f73f-3cff-a5bf-a69de7eec9ef | -16.0509 | -50.4363 | 2026-08-23 06:00:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 347a9c0c-0022-3ba5-a03f-d9d2cbdeccb8 | -6.6949 | -58.7485 | 2026-08-23 06:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 9ac22e99-86ca-37e8-bd37-545d480fad00 | -6.6766 | -58.7299 | 2026-08-23 06:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 47cc3963-faf5-3aa1-8c66-816ebc19d197 | -6.8061 | -58.6663 | 2026-08-23 06:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| b0f1c7b6-74bf-3b1c-828e-fab0b882be4b | -5.7799 | -57.58 | 2026-08-23 06:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 5fe3f2dd-ae34-3180-a5f4-642dbfcb65e1 | -16.0509 | -50.4363 | 2026-08-23 06:10:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 64.5 |
| beccb207-91fc-333e-bd32-7d4f652cab59 | -6.6766 | -58.7299 | 2026-08-23 06:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 690c74c4-0766-3547-a730-d09a822073f1 | -6.8061 | -58.6663 | 2026-08-23 06:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| cd28e16e-8729-3b40-a9a9-4bf3084e9958 | -6.8062 | -58.6469 | 2026-08-23 06:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| bc334d2c-9a10-3d85-8ee2-3c4b061eb9b7 | -10.4713 | -49.9838 | 2026-08-23 06:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 39.6 |
| c106ff02-e3e8-3b6e-837a-12229988ff0e | -6.6765 | -58.7492 | 2026-08-23 06:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 112.6 |
| a520d692-eb5f-310f-b9b7-6432b6c43e62 | -10.4716 | -49.9624 | 2026-08-23 06:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 91975479-dc42-3b85-bdb7-2fb644c050ab | -6.9514 | -59.0666 | 2026-08-23 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| ded49a53-c75d-3736-a9e0-5d6bb031c558 | -6.9513 | -59.0859 | 2026-08-23 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 3f3151ae-fdaf-30d7-b617-d3ad440c0c81 | -6.695 | -58.7291 | 2026-08-23 06:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 7c0b97b5-1511-3025-9d49-1f23dfb38961 | -6.6949 | -58.7485 | 2026-08-23 06:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 88c06e64-b0cb-3170-ab64-30ac269f28af | -6.9699 | -59.0658 | 2026-08-23 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 54d126ec-24f6-351f-8ab4-7ae09462b160 | -16.0509 | -50.4363 | 2026-08-23 06:20:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |


[Clique aqui para ver as próximas entradas](README68.md)
