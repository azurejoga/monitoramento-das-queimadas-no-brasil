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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d19bdbf-2ec8-38d6-ae05-a4c3eed719d0 | -9.1708 | -50.0049 | 2026-08-26 15:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| d763f986-ca5e-3844-8348-c4dc350f17b3 | -3.1267 | -61.1811 | 2026-08-26 15:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 15d75a61-32a5-3bef-8fa4-cf89ac8809c1 | -8.0733 | -47.5066 | 2026-08-26 15:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 74262442-1db5-3201-9b85-f4f07c6def05 | -6.0992 | -59.9267 | 2026-08-26 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| ad4866e6-b6e1-35c2-b3f7-0214cd313996 | -11.3892 | -50.6972 | 2026-08-26 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| f6d8fe3a-67b1-3032-94b9-37e5780dfcd1 | -11.175 | -54.001 | 2026-08-26 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 112.0 |
| f09a30e9-694b-3568-b01e-43e96a3b9475 | -8.7772 | -49.955 | 2026-08-26 15:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 8999ecdb-36f3-3df1-934f-5e36a9164a85 | -9.7246 | -49.3512 | 2026-08-26 15:30:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 120.0 |
| c9e17e81-504e-3728-8e50-6373f419d6ba | -8.9418 | -45.748 | 2026-08-26 15:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 280.0 |
| 7d585dd7-2e60-349c-91d0-8d6f309fa09b | -5.9977 | -45.3381 | 2026-08-26 15:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 37207ff9-cebc-3dfd-9405-854dc309e825 | -8.1482 | -47.5218 | 2026-08-26 15:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 294.2 |
| 1e8776dd-9167-3107-9290-238e677f0f17 | -8.616 | -54.7339 | 2026-08-26 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 93270dbf-6ce7-3ba9-b3ea-392e5cbb560a | -8.6344 | -54.7528 | 2026-08-26 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| fb2b4fd5-de4e-3db6-978b-964ec190104f | -9.4519 | -51.67 | 2026-08-26 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 152.3 |
| db672a03-6e13-30bb-8d27-f89877b9d852 | -6.3323 | -54.7272 | 2026-08-26 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 0faeec5c-3430-3fd0-90fc-ad7edcf65f6f | -6.0353 | -58.0376 | 2026-08-26 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 4ae6d2af-3dd0-3d69-8905-94e18e8e2a59 | -6.7692 | -58.6679 | 2026-08-26 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 2521824a-51da-388c-a06f-10d02151186f | -7.0242 | -59.2374 | 2026-08-26 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 0b1cb3ac-7895-3496-aaf5-1fb94b868343 | -6.7094 | -59.443 | 2026-08-26 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| a7ca6581-0283-3334-aa29-79846ce33e7a | -6.1743 | -53.4834 | 2026-08-26 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| bd41ae26-5f62-3207-ab70-4af4edd6450d | -8.1482 | -47.5218 | 2026-08-26 15:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 213.4 |
| a7731729-37a2-3d91-a5b5-0ad5c1dff8d5 | -8.5591 | -54.8386 | 2026-08-26 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| fe3ad205-edf9-3938-b059-c638ffa46961 | -10.7982 | -50.973 | 2026-08-26 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 146d440c-caf2-3a74-afb0-6494a932b029 | -11.1939 | -53.9993 | 2026-08-26 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 225.9 |
| eb523322-cbe5-30f1-9714-e312e15f0fd0 | -6.8387 | -59.4186 | 2026-08-26 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 14e4836d-e868-3601-ab97-04c1a086efc6 | -7.0058 | -59.2382 | 2026-08-26 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| c9411c2a-6e1b-3656-a1e6-e091d02764e8 | -9.7249 | -49.3296 | 2026-08-26 15:40:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 1b33edd0-71cf-35df-9a30-a997f82a5d1f | -8.1855 | -54.9637 | 2026-08-26 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| ffa068eb-0e93-3aa6-a398-6a22e8027992 | -6.676 | -58.8267 | 2026-08-26 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 88e7932f-d44c-3519-95f5-f927a414942e | -13.6337 | -49.0051 | 2026-08-26 15:40:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 4047976c-3dfe-3c5d-8f48-bcffd3f47441 | -10.7596 | -54.0384 | 2026-08-26 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 260.8 |
| 95e29975-15b9-39f8-bfb6-1c851144d90c | -10.7784 | -54.0368 | 2026-08-26 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 228.6 |
| 8989a829-0efa-3e17-9eb8-b1f53ed048ee | -7.4947 | -55.3662 | 2026-08-26 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 138e5fc2-6b1b-35d7-b40d-43e57136beeb | -7.6649 | -47.1242 | 2026-08-26 15:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 044f1038-2595-3022-a235-b709059cb974 | -9.9708 | -53.9419 | 2026-08-26 15:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 5be5f90a-b7eb-3d44-b4f1-1ab824c1e1b9 | -6.5829 | -58.9851 | 2026-08-26 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| f26211ae-c3ba-3962-b60c-c1a81f449624 | -11.1561 | -54.0028 | 2026-08-26 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 0d1e44fb-b69c-3c7a-a477-78c6faa5e1e2 | -6.7692 | -58.6679 | 2026-08-26 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| f4f2a634-1517-306c-a547-2e41156d10de | -6.5138 | -55.2387 | 2026-08-26 15:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 1449e4c0-9e7d-3c11-aa32-d5d8175a1036 | -10.3145 | -50.4061 | 2026-08-26 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 99386424-60aa-3a2d-89ec-70c415ca79c0 | -13.2479 | -51.3308 | 2026-08-26 15:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 163.5 |
| dfbde181-410f-3219-a136-7a43ce4aa83f | -6.3323 | -54.7272 | 2026-08-26 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 3d4b1efc-6566-3b8f-9610-deb2eeb9873a | -7.6461 | -47.1258 | 2026-08-26 15:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 426.0 |
| a62a8392-8e20-3f48-bcd6-6de5f20e6198 | -9.7246 | -49.3512 | 2026-08-26 15:40:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 5b9f88fa-9533-3925-9546-5a8d8b3cebc6 | -9.5898 | -45.3794 | 2026-08-26 15:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 4e359606-495f-3e83-a8a2-9aac0123f47d | -10.9851 | -51.1443 | 2026-08-26 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 7e663a1e-e903-35aa-846d-ecc37d168931 | -6.621 | -53.1945 | 2026-08-26 15:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| e41b4769-9851-3333-b540-1f53936e0db6 | -6.7661 | -45.2551 | 2026-08-26 15:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 7cadfe1c-29e6-37e7-8001-ec07f674b57b | -3.1266 | -61.2 | 2026-08-26 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 5609dcaf-05e4-3c77-af0a-97ee1667045e | -10.5596 | -50.4449 | 2026-08-26 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 68d0aae0-5705-3083-b72e-3f9832dea28f | -6.1177 | -59.9069 | 2026-08-26 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 9f33a223-fe68-30e6-bc27-57ae2d471b85 | -6.0992 | -59.9267 | 2026-08-26 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 580455e1-42af-3ac6-8826-6bf4cf08f64f | -13.2284 | -51.3545 | 2026-08-26 15:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 32f726db-7ada-3e6f-8343-5704c3408f6f | -8.2226 | -54.9814 | 2026-08-26 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| d898de37-933c-3e06-93ba-ae19910958b3 | -10.7598 | -54.0179 | 2026-08-26 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 365.1 |
| b531d617-4eff-3a5b-857a-62c8ebb89e18 | -6.6227 | -58.4801 | 2026-08-26 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| aba849f1-324d-3f0e-a3c1-bcf1deef7c5b | -6.8246 | -58.6655 | 2026-08-26 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 671d4ac6-ef75-3de3-bfce-3bf655597c53 | -8.7769 | -49.9763 | 2026-08-26 15:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 431.1 |
| 7fb5e96d-0444-3ee3-9220-095362dfad86 | -6.6225 | -58.5189 | 2026-08-26 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| e01ebae6-c2b5-309a-9d05-a70b4fb34688 | -10.7603 | -53.9769 | 2026-08-26 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 329.1 |
| 154c9848-0587-3205-8058-1d9d5d9add2f | -10.7412 | -53.9991 | 2026-08-26 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 560b0311-1507-363a-b197-352b09422be4 | -3.2178 | -61.2362 | 2026-08-26 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 297.7 |
| 01735906-6ef2-32aa-88f5-9debbb1dfe98 | -15.7878 | -56.452 | 2026-08-26 15:40:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| bede8ca9-92ab-3c1f-a000-9aebe2f09eb4 | -7.1121 | -42.7963 | 2026-08-26 15:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 840.0 |
| ee78a8c5-f74e-3ce6-ae05-d9ab935177a6 | -6.1741 | -53.5037 | 2026-08-26 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| a4c08828-5ca2-362e-bc00-89d3d46f771b | -8.6344 | -54.7528 | 2026-08-26 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| c52b5e8f-a5b8-3c3e-8643-999d12832c91 | -9.1315 | -57.5703 | 2026-08-26 15:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 060a54d9-dadc-39ea-9a7a-e775c85261bd | -10.779 | -50.9962 | 2026-08-26 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 4bf1a5ce-0b95-3406-aeb1-6b02f37186c3 | -6.8019 | -59.4008 | 2026-08-26 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| a4b69e3a-f2d8-3641-92cc-3cd9b825d066 | -11.3702 | -50.6993 | 2026-08-26 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 165.3 |
| e0d32cb4-12c2-3f71-b474-ac8e007bbb85 | -13.2287 | -51.3332 | 2026-08-26 15:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 157.2 |
| 410197d7-ac83-3377-b80d-23e231ef2f45 | -9.1711 | -49.9835 | 2026-08-26 15:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 128.8 |
| f62dee94-efa0-3922-90c4-8184be2990cb | -6.4233 | -54.9432 | 2026-08-26 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 2001b22c-6ff3-312a-91ad-03ac0c0e08ce | -5.9196 | -43.6497 | 2026-08-26 15:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 408c647b-1c1c-3aa6-a443-c88f2fa6c675 | -12.6836 | -48.4116 | 2026-08-26 15:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 7fd1a602-1fe9-33fb-a1b8-8f9f3bfd9d95 | -6.7833 | -59.4208 | 2026-08-26 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 75d2087f-e971-3045-a054-6f4d8011b4f1 | -6.3547 | -45.1751 | 2026-08-26 15:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 105.9 |
| ace1b618-32c6-3171-96b8-7f00617eb4d3 | -13.3038 | -51.4304 | 2026-08-26 15:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| af855fed-5bbf-311b-9bb4-a334c510ab6d | -8.6415 | -50.3495 | 2026-08-26 15:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 4ca211c7-4875-38e1-8fae-14840b599f81 | -11.175 | -54.001 | 2026-08-26 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 8aa5a41b-7859-36a3-a3b4-479a62337a76 | -4.8002 | -43.1709 | 2026-08-26 15:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 1344aab0-47e2-3407-92fe-8e58ec17c299 | -10.9661 | -51.1463 | 2026-08-26 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 2e2188e4-8133-3672-867d-65d06c2622df | -6.7279 | -59.4423 | 2026-08-26 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| c6cf0113-ba75-337f-a84d-292c2105b796 | -6.6233 | -58.383 | 2026-08-26 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| f3f626dd-f110-39bf-83b6-2d8f5dfb7bc4 | -10.9664 | -51.1251 | 2026-08-26 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 161.6 |
| 6f222d34-3725-34c5-a75c-171437566f41 | -8.5177 | -55.3039 | 2026-08-26 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 154.3 |
| adcc2c2d-07ae-31ce-b26f-3c35dd4f723b | -7.0242 | -59.2374 | 2026-08-26 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.7 |
| d34dfa15-ad7b-3dc6-a59e-8def691a5fde | -6.8008 | -59.5934 | 2026-08-26 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| d3cf1f46-3c03-3a19-8738-5ff33d3de909 | -6.8061 | -58.6663 | 2026-08-26 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 83382080-4d6c-37f0-859f-ee0c3b7663e1 | -7.5015 | -44.9397 | 2026-08-26 15:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 20dd5d36-17aa-3035-bda7-64db65034dd1 | -6.6917 | -45.1932 | 2026-08-26 15:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 4d1aa90e-90df-33c9-8be8-b1297c31411d | -6.7834 | -59.4016 | 2026-08-26 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 96c96fd4-5466-336f-874b-ef42526eb019 | -6.7296 | -59.1337 | 2026-08-26 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| a78261d3-e40f-3e0d-86fb-7d9b3e66401b | -9.1708 | -50.0049 | 2026-08-26 15:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 14f14ffe-a068-30ed-b681-15107650eb30 | -8.7584 | -49.9566 | 2026-08-26 15:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 179.0 |
| 68ea7016-e9dc-39f2-845c-edb443c0560d | -6.0806 | -59.9657 | 2026-08-26 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 327007ec-6d95-32c0-9b33-4f5fde6e4cbb | -10.95 | -49.5877 | 2026-08-26 15:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| b9b545a2-47ab-33a0-a278-1b7e6b32ea1b | -8.8187 | -49.6093 | 2026-08-26 15:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 423.3 |
| 4ad0c9ab-763d-3bc2-a7b4-289fb5578c06 | -6.0807 | -59.9465 | 2026-08-26 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 2b2b1c08-4bab-3924-8ae6-2219ceee76ae | -8.8189 | -49.5879 | 2026-08-26 15:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |


[Clique aqui para ver as próximas entradas](README92.md)
