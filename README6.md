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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f91076ab-9a15-3fe6-9863-426a69d5a6c2 | -8.5853 | -50.3543 | 2026-08-18 02:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| fe1d699f-4ab7-37a1-8a0d-d29b5f543e31 | -14.2759 | -51.9234 | 2026-08-18 02:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 9eb16176-50d3-3839-b444-24d408be7c9e | -6.8594 | -59.0125 | 2026-08-18 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 653e0156-fc1f-36f4-ac9a-cb6ae9527fc3 | -6.841 | -59.0132 | 2026-08-18 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 0321d351-4202-35de-9f2e-fd31da303b09 | -6.748 | -59.1523 | 2026-08-18 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| c61c1d38-0fbf-3096-a9fd-75d70554c96d | -6.8411 | -58.9939 | 2026-08-18 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 1b16aee9-7fd9-3cf9-b50a-97cdc9c3248e | -6.8596 | -58.9931 | 2026-08-18 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.6 |
| d9f29f06-6378-30fb-a211-c13afb8b0e2c | -6.7123 | -58.9412 | 2026-08-18 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 71349ddb-4dc4-348b-99d4-69c23a0a0f29 | -14.1824 | -52.9089 | 2026-08-18 02:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 108.5 |
| bfd3ee1a-6fcd-33a6-8044-5ae80a91ab6b | -8.604 | -50.3527 | 2026-08-18 02:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 1f76347e-1607-3c25-a2bf-455ae857a2d9 | -14.1631 | -52.9113 | 2026-08-18 02:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 99.0 |
| dd0d5075-4615-3c9d-b29f-9ab21cbf12e0 | -14.1821 | -52.93 | 2026-08-18 02:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| acf07907-1581-3b28-a70f-2ab07bc0ca34 | -9.4254 | -60.4545 | 2026-08-18 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 54741f03-7f39-36e1-b9c2-88e18ff286e0 | -6.8594 | -59.0125 | 2026-08-18 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 7d5c9921-0e6e-3d55-be10-3728f014328e | -9.4256 | -60.4353 | 2026-08-18 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 2bb8271f-5005-30fc-bfce-1a2404336af4 | -6.7477 | -59.1909 | 2026-08-18 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 86830c4d-8a2a-3b17-961e-6a4dab8d87ca | -6.7478 | -59.1716 | 2026-08-18 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 3fd8559d-0938-3f42-a529-4f81c2ab8194 | -8.5853 | -50.3543 | 2026-08-18 02:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| d39ccf20-278e-3df9-86ea-32a0588a795f | -6.7663 | -59.1708 | 2026-08-18 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 922c0615-9270-3a94-bdfc-49f949d43d95 | -6.841 | -59.0132 | 2026-08-18 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 20aad90b-dcbb-3461-a584-8c5c6d148469 | -6.7664 | -59.1515 | 2026-08-18 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 29efa52e-697a-3ab3-b896-a5843188d951 | -8.6042 | -50.3315 | 2026-08-18 02:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| fb54a7af-5dfc-373f-90a4-1e48456e50e5 | -10.8691 | -44.9646 | 2026-08-18 02:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 64.3 |
| dcc48c61-0cd9-30ca-81df-9d408f32a20f | -14.2759 | -51.9234 | 2026-08-18 02:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 49.3 |
| e1235077-fad7-37ef-8a9a-733f3633266c | -14.2755 | -51.9447 | 2026-08-18 02:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| bd26206b-43f5-3f59-a9b0-a410cdf76786 | -8.5855 | -50.3331 | 2026-08-18 02:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| d010d9d4-a75e-3f30-a7ed-3650fba375a9 | -8.2036 | -55.0228 | 2026-08-18 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 5063805b-76e0-3a85-b541-0c1c626068a2 | -8.6 | -54.74 | 2026-08-18 02:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab336000-d4de-3ab6-8446-16f5b137e6da | -8.58 | -54.79 | 2026-08-18 02:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ffacf49-f698-3a07-b0d1-26abc96b2230 | -8.57 | -54.66 | 2026-08-18 02:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38df9421-4ece-37c7-9389-873788434f50 | -8.57 | -54.73 | 2026-08-18 02:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba19b8bb-15b5-3640-844c-c4d5b09c7370 | -8.185 | -55.024 | 2026-08-18 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 347b86fb-f3f7-371b-b428-94f933e0e4ce | -14.1821 | -52.93 | 2026-08-18 02:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 9876f4ba-1220-328a-b36a-c1f2c4c7914d | -6.8594 | -59.0125 | 2026-08-18 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.4 |
| f5586744-4ec7-3f2d-9257-f8ad3c1509b8 | -14.1628 | -52.9323 | 2026-08-18 02:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 0ad37135-a989-3821-ba54-6489cde49951 | -6.8411 | -58.9939 | 2026-08-18 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 31b9e99a-0aa6-3033-a6ce-7f5c7e6ab581 | -9.4254 | -60.4545 | 2026-08-18 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 0ec7a326-8c7d-3f26-bb04-efb134dd7d59 | -8.5853 | -50.3543 | 2026-08-18 02:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| ebd534bc-2307-32b4-a443-c48ff5d16681 | -6.841 | -59.0132 | 2026-08-18 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 541d0fb4-5f4f-358e-830b-c824e8ab72f6 | -8.5855 | -50.3331 | 2026-08-18 02:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| b04f0898-30a5-37f7-a2de-e29d8a7fcb62 | -9.4256 | -60.4353 | 2026-08-18 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| ab034119-976a-356e-862b-93e2d7a655ef | -6.6938 | -58.942 | 2026-08-18 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 2710320f-e70e-38d7-b27d-f983de8efd8a | -6.7477 | -59.1909 | 2026-08-18 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| ef9097df-11db-302e-a5d1-684793e88677 | -6.748 | -59.1523 | 2026-08-18 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 8a2b1ab3-3665-356f-90c0-74801b8fa747 | -6.8596 | -58.9931 | 2026-08-18 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 517f8c77-e24e-3d93-a4b0-cc7279e601c4 | -14.2566 | -51.9259 | 2026-08-18 02:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 7371522f-f46b-3db3-8d05-fd9dd254ccc0 | -21.3484 | -54.6289 | 2026-08-18 02:20:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 04c706b6-572b-3035-8af0-6673d40dd790 | -8.6042 | -50.3315 | 2026-08-18 02:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 823e911f-52ee-37ce-8c71-7115b536f401 | -14.1631 | -52.9113 | 2026-08-18 02:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 99.4 |
| a6ce8f20-e6dd-3659-95f7-41df8544fffe | -6.7663 | -59.1708 | 2026-08-18 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 23164db5-3db2-3717-b5a1-9caebcdea365 | -8.2036 | -55.0228 | 2026-08-18 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 96988e29-c667-3e68-b7a4-441dd763cd81 | -6.7478 | -59.1716 | 2026-08-18 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 4653149c-365a-3b20-a59b-e6b19d839a7c | -8.604 | -50.3527 | 2026-08-18 02:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 142.6 |
| d051e950-3bd2-35af-9605-4cfebb361315 | -14.1824 | -52.9089 | 2026-08-18 02:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 543ec60a-45ff-34cf-b46e-5800c8abe038 | -6.7477 | -59.1909 | 2026-08-18 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 09bf85d0-df01-3838-8415-ad760e778968 | -14.1824 | -52.9089 | 2026-08-18 02:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 115.3 |
| e777b365-37a0-3fc4-867e-07c1c3cb73d9 | -6.7478 | -59.1716 | 2026-08-18 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 792a339b-304e-345f-ad86-ccaa17e0e4b3 | -8.6042 | -50.3315 | 2026-08-18 02:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| b7d1d9b0-ee45-34dd-bf9f-75e976acaec1 | -6.8411 | -58.9939 | 2026-08-18 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.8 |
| dd4640ac-6163-3dad-ad07-90cb8c81257b | -6.8594 | -59.0125 | 2026-08-18 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.2 |
| c9554165-a42f-3d57-8a95-4744f7b85835 | -8.604 | -50.3527 | 2026-08-18 02:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 124.8 |
| 6b50cc44-3781-39ad-80d1-169cdf90fe22 | -8.5853 | -50.3543 | 2026-08-18 02:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 413a6ca9-d902-3025-873a-3e9b3c0623e2 | -14.1821 | -52.93 | 2026-08-18 02:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 4d777e63-2591-35a3-8499-18939b2b2556 | -6.8596 | -58.9931 | 2026-08-18 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 7ce99574-5510-39df-993e-869c290a3f23 | -6.6938 | -58.942 | 2026-08-18 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.2 |
| a4668dbb-69d5-35ec-bd35-aa0d8ff5f53f | -8.5855 | -50.3331 | 2026-08-18 02:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 5a4414c2-3f79-3024-bf0a-5456b28f2ac7 | -6.748 | -59.1523 | 2026-08-18 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| ec411be7-4633-3599-8c45-49ca89419fb8 | -8.2036 | -55.0228 | 2026-08-18 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| ff1c3610-145d-3787-8dc4-089a0159c935 | -6.7663 | -59.1708 | 2026-08-18 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| a18187de-51f2-3a66-9bb8-bc1e7c9e03e3 | -9.4256 | -60.4353 | 2026-08-18 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| ea695bff-ea8f-3b9d-b145-d596c0bcb2e8 | -14.1631 | -52.9113 | 2026-08-18 02:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 3b35f11e-4a2f-3a6a-bd1e-13145d697e6b | -6.841 | -59.0132 | 2026-08-18 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 12b888d6-880c-3251-8090-63041bfe3857 | -14.1628 | -52.9323 | 2026-08-18 02:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 57.8 |
| f7ea82af-2aa4-3586-9396-24c6f93e1e7b | -8.5855 | -50.3331 | 2026-08-18 02:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| fc1a559e-adb0-3349-af76-503c2db6a519 | -6.8594 | -59.0125 | 2026-08-18 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.4 |
| ff850cf2-248f-3195-abce-e8725892e090 | -6.7663 | -59.1708 | 2026-08-18 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 150605f1-704e-39b3-8a8a-5646cfbf83c8 | -8.604 | -50.3527 | 2026-08-18 02:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 127.0 |
| 3133fb3e-06b1-337c-a65f-a279efef25a3 | -19.7577 | -42.1229 | 2026-08-18 02:40:00 | GOES-19 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 129.4 |
| 4e8536bc-b9d4-3f3e-b448-41a36c1f90e9 | -9.4256 | -60.4353 | 2026-08-18 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 76a7ed54-34b6-3b0b-8b4d-db88e35e19a0 | -14.1821 | -52.93 | 2026-08-18 02:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| f49f3819-cc9f-3ccc-aebb-164d488ce337 | -8.2036 | -55.0228 | 2026-08-18 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 1a29422c-b52c-3d68-888e-e8cab50e9c9d | -14.1631 | -52.9113 | 2026-08-18 02:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| af904c3d-508e-31b6-aaa0-2c3d34d1efe9 | -6.7478 | -59.1716 | 2026-08-18 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 53972b89-a849-31ce-818d-d9855973337c | -6.8411 | -58.9939 | 2026-08-18 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 93404c29-6940-3206-a75a-e0ce449036a1 | -8.6042 | -50.3315 | 2026-08-18 02:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 983d2ac7-5716-3922-be0a-2e63b95e7d0f | -14.1824 | -52.9089 | 2026-08-18 02:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| c1334c0f-8c3a-3061-b56f-38acb7577c3c | -8.5853 | -50.3543 | 2026-08-18 02:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 3dfd884e-dbb6-3d55-aad6-a54143104ff5 | -6.841 | -59.0132 | 2026-08-18 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 57c6ad3f-9abe-35dc-be1e-9cbc112e70c9 | -6.748 | -59.1523 | 2026-08-18 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 50041af5-5051-3edb-a70e-683dd33aa2eb | -14.8228 | -46.6419 | 2026-08-18 02:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 0880f806-ad14-3204-8c82-73c7d061b6ca | -14.1821 | -52.93 | 2026-08-18 02:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 106.7 |
| d95e263d-4689-317c-b653-1a23f577ed60 | -14.1824 | -52.9089 | 2026-08-18 02:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 84.3 |
| ae71a9c1-aa24-3487-8730-528cea84d3db | -14.8228 | -46.6419 | 2026-08-18 02:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 67.2 |
| e8b684ca-c572-35dc-b860-7a3cf51b8738 | -8.604 | -50.3527 | 2026-08-18 02:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 213.4 |
| 9edf2964-5152-392f-b8c5-dc917ed24a05 | -14.2759 | -51.9234 | 2026-08-18 02:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 33a998b8-d6a8-3e0e-a7c6-3768e5dbbc81 | -6.748 | -59.1523 | 2026-08-18 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 08182ff4-1851-30e1-ab22-7c0164294ae8 | -8.6042 | -50.3315 | 2026-08-18 02:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 67750443-b1c8-314f-bf61-d88565a8c193 | -14.1631 | -52.9113 | 2026-08-18 02:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 8b4c40fd-2d23-399c-bb2b-91538f31cd17 | -6.7663 | -59.1708 | 2026-08-18 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 50a81236-3b97-318d-b666-74996b833914 | -6.841 | -59.0132 | 2026-08-18 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 30.0 |


[Clique aqui para ver as próximas entradas](README7.md)
