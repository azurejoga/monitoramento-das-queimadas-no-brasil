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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ac9c3ba-e498-3cd1-8a9b-d7402970b422 | -7.92838 | -61.74412 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dc065081-3693-3935-aaa1-45af2fd0fd99 | -9.20398 | -59.64691 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ae3b5a0-33b0-32cd-acd9-c0028b18b3c7 | -8.98361 | -60.54718 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1ed591dd-eac8-3eb1-9b01-a99166b95659 | -8.99663 | -60.52401 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1fbb606b-0904-31ff-8ec8-af42a65b3972 | -8.99617 | -60.4921 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 9fdf3d1a-f789-321b-93d1-fa4d933902cb | -9.50409 | -60.5532 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 332b2f91-6c46-3f5e-9246-2ff8395577c6 | -7.95014 | -61.75506 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ac71157-37b6-33ee-a266-fd0de211370c | -7.91706 | -61.73486 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6943ceb0-b1bf-3090-935f-b2a5e6b2177a | -9.26073 | -60.77244 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b499203-f834-3bd8-9e11-946ee3c80998 | -9.16436 | -59.6467 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2a54e21d-5771-3322-ae59-79f2db7cdfe4 | -7.95277 | -63.21313 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6872c8f1-a8af-366e-bc97-762a23901c6f | -9.16363 | -59.65208 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 32acf49a-5d83-3edd-8c24-a36263aef794 | -7.95319 | -61.74768 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 218e7f1a-2c1a-365a-99ae-e0b7cf84fac5 | -7.95654 | -63.2137 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00d2be4c-0bc3-30d4-a063-d3ce6544a689 | -9.21784 | -59.65409 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| eb81286c-f2e2-31e7-9e09-5f6f34ee24b3 | -8.98612 | -60.49846 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| c2f2bb83-1f91-33fa-877c-d35243b29b14 | -8.98155 | -60.49785 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4b21dfde-4990-35c0-aac0-202a68e73d30 | -9.15923 | -59.68417 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b9c08d4-2f93-3f3d-ba2c-5b44dba801bf | -6.9401 | -59.55209 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 66aeac96-ff9d-3ad3-ae1e-d10d111e4721 | -7.95346 | -63.20857 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cbf18fa-f9c6-34e0-bc0d-848a65991f51 | -9.18861 | -59.6505 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4c9bb2af-8b92-39f0-b73a-b544b17b9a6f | -7.45346 | -59.94231 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b22b7bfe-a01c-3ad2-b1af-fa5f932148fa | -7.88051 | -61.81253 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a99e8aa-f2d3-3ef7-aba8-c872d8a8caa8 | -7.52283 | -61.31116 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e6865f8-0dbb-3159-a09e-fda74babfc1d | -9.22016 | -59.65534 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 46b7720c-1e81-3c6b-b96c-9e0b8b27379b | -8.98814 | -60.51794 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f5514bfa-0ad4-3e2b-96e7-03e369f8cc81 | -6.93648 | -59.99907 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3f303724-ffb2-37b2-a44a-cd2b72744544 | -8.71267 | -62.46088 | 2025-08-16 05:50:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08d9ab8f-ab98-3162-86cd-71662210a257 | -7.61822 | -63.34216 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f6be4a5-7ba5-3e7f-a177-d0686c20e3ff | -8.99081 | -60.52938 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| fb95fc1d-5337-3334-a64f-a2ca602f4cf4 | -8.99144 | -60.5279 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 87164df4-a23f-3637-af8d-4cb309d4f3ac | -6.9288 | -59.52968 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5aeafc0-9f06-3a37-a81e-346dde94e363 | -7.49937 | -63.82138 | 2025-08-16 05:50:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| b27aeb03-59ba-3f35-a4bb-afe36a1133a1 | -7.28239 | -64.69848 | 2025-08-16 05:50:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f815345-6723-3c67-a2fa-0e5733f1372b | -9.39858 | -60.54474 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ece7853-bfb7-3e77-b2ad-15c723858d4d | -9.22271 | -59.65469 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8eceec32-51ba-3d9b-a222-d8500618348e | -7.92424 | -61.74352 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dc90fd79-fe9f-37be-9ac7-28422a3a4f4a | -9.20961 | -59.64212 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29c9dec2-83c5-3132-bede-2f5474499666 | -9.50604 | -60.54552 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e770865c-bfb5-39a2-ad06-23643c8f0df8 | -7.53517 | -61.34512 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 743fa10d-6e80-3c90-b8b6-1b5cddfd35a2 | -8.10015 | -61.18544 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7690283d-ef7e-3bba-b5ed-4266963b170f | -7.68257 | -63.3199 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 334e00f0-a95d-3b99-bc13-bec3801e8809 | -7.44522 | -60.02087 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2f448c7-9a5a-3270-919f-a3b73869eacd | -8.69875 | -63.96178 | 2025-08-16 05:50:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6aba237e-60eb-351f-b0d6-9ada8639a0d1 | -7.87693 | -61.80825 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aabcd63d-4d96-38a1-93f1-afbc9b98cbb8 | -7.9149 | -61.74968 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39135022-e64f-3dae-b3d6-b9615b47aa1e | -9.51183 | -60.53022 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9c4c3a5a-1fb9-3f03-bd4d-f275101e7e27 | -9.20351 | -59.63133 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83ef6f83-d679-3077-957e-54a1c0d7a98d | -7.61157 | -63.32991 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb6f9948-9633-3c08-8965-7992428893ec | -6.93681 | -59.54131 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5de23868-bb29-340f-9564-0231094296a5 | -7.62018 | -63.32878 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b99e87e9-b2d3-37a9-874b-096fc4ff8ac8 | -7.53152 | -61.34057 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71f0a7ee-19de-3ba2-8279-9a76a0e2be9c | -7.91436 | -61.75338 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4563a1c4-03f1-3f19-b3b9-2977b892408c | -8.99919 | -60.50516 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4e2f4a35-83d0-3834-a87d-f61eab9dac3e | -7.25272 | -57.62583 | 2025-08-16 05:50:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 362bbf66-5a00-393a-a3dd-4a13a8ac3057 | -9.15759 | -59.62368 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cedaf618-02f1-33f8-989a-509a9c8e489e | -6.66164 | -58.82456 | 2025-08-16 05:50:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 825a8c2d-1977-38d9-b8cb-95c2eaaa835c | -7.82581 | -61.32732 | 2025-08-16 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c091586-662d-301c-84cd-d490d8fb524e | -8.98295 | -60.52193 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f689f571-e3bd-32d5-9300-3509fd46b21e | -7.62326 | -63.33381 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3d8f242-21ee-363b-b712-81af557ef9f0 | -8.99159 | -60.56096 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cbe95acc-b178-3fb4-9187-04891f19b75a | -6.66333 | -58.81998 | 2025-08-16 05:50:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e8b9ebc-e194-3ee8-98ef-4f6d84b73c0d | -7.52227 | -61.37471 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d24c0f46-5925-38e7-bcd8-198db2eb8981 | -9.16585 | -59.63583 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f1610fde-8ee7-3c15-b7d6-2aba3a33dc7b | -9.0011 | -60.49117 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e55e93e6-b71f-3e22-ab0b-9bd79f2a499d | -7.45712 | -59.93454 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ffa451bf-a66f-3358-adee-53573c10e741 | -8.99589 | -60.49518 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd8ba786-e017-3470-8cc8-12f1fa31a37c | -6.79933 | -59.82082 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 845c85ac-3d28-322c-b7d0-af5349613734 | -9.50786 | -60.52489 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ab5da519-aa23-3268-a7db-6df73db07123 | -9.17221 | -59.62563 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 730d1489-7283-3b1b-8bf6-681fc75da197 | -7.52843 | -61.33213 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 313b4c31-3fae-397d-bac7-982527e7fa60 | -8.97465 | -61.70734 | 2025-08-16 05:50:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4ac80641-09f5-3bc1-8ee7-08137f0be9ea | -7.61206 | -63.33212 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c002c8e-2c19-30a4-a27b-2e101d094bc9 | -9.51657 | -60.53733 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9b07d47e-d92e-3631-8ede-bfc98d5e2345 | -7.43634 | -60.02759 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54362e9c-0430-39ee-b6f4-7519d705641e | -7.6795 | -63.31487 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6e82326-305d-3f8b-94a0-910be9fcb490 | -8.94528 | -62.23217 | 2025-08-16 05:50:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ff5b7bf-9846-3a61-8dca-4d6c251424c5 | -7.43106 | -60.03156 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c76be3ab-0d93-36c6-9a8e-58cd6d2a7fe0 | -7.68631 | -63.32046 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afe4031d-5134-3c5e-9926-dffd62b955b7 | -9.50534 | -60.54381 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 98e34553-83aa-309f-89e8-3e49ddaf2657 | -7.67577 | -63.3143 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdd3a4cf-3134-3e23-aa7f-89b551e9e735 | -7.83006 | -61.32793 | 2025-08-16 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a4d9e97b-1468-3e91-8e2f-f0cd6e218f3c | -9.5087 | -60.52664 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5d27ad3c-1ef1-35f5-9a32-9917b6e27c56 | -8.96477 | -61.68608 | 2025-08-16 05:50:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 3d42e9fd-f612-36ac-a411-268131eded74 | -7.52648 | -61.31574 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8e690bf-aff2-3004-8118-2e1a026423fd | -8.98302 | -60.51879 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c33c46fa-1af5-3bdb-b3b1-c386e69b3c7a | -6.93528 | -59.65252 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e3a833a-471f-3219-9c49-5d5fdeb7234f | -7.53209 | -61.33665 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ba5d077-f760-362c-9a05-874d39681909 | -6.14066 | -57.92929 | 2025-08-16 05:50:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7097fed0-1b6c-3e9d-bae5-5dbc62dc2db5 | -7.90771 | -61.74107 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38a8fd8a-5a99-3c23-9f74-7b5141a619c2 | -6.93826 | -59.53118 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 76e38380-757f-36d8-b71e-8cfd01ca41c2 | -7.038 | -59.61884 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af3c998c-8823-316f-9119-1684abd4a93e | -8.6633 | -62.46415 | 2025-08-16 05:50:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d270a19b-366b-3679-bcc3-a0d98d74fa47 | -6.1403 | -57.92924 | 2025-08-16 05:50:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 902b4ded-c6f2-347e-a863-c2a350eed8b1 | -9.20972 | -59.65941 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 994795a4-d5c2-32fd-90f3-dfeda4554ce8 | -7.45022 | -59.93196 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce5cd6b9-d0d1-3cee-b52f-33c7f31f4f16 | -8.98492 | -60.538 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 54415f7c-97ee-3646-83b5-d05931f8539f | -7.529 | -61.32822 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 270c771e-df24-3f0f-8e8d-d651c91f1fbf | -9.19864 | -59.63069 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23f42ab2-9e79-34ae-b8fe-0189e25d2c94 | -9.38973 | -60.54187 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README65.md)
