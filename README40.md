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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee593cd3-8361-3637-b30d-58d00a001e5f | -9.47153 | -51.66687 | 2026-08-18 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 944795b9-556f-3436-b663-e0bd8eb6f376 | -11.72211 | -54.61776 | 2026-08-18 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1882a52f-33e2-3c7b-9f65-580d0716145f | -7.91788 | -61.73865 | 2026-08-18 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e910fab0-f3b2-3294-a400-5b85ece8cbbc | -8.89859 | -60.60387 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 92cd7af9-9ee9-353b-b783-b596172c7410 | -11.71378 | -54.62727 | 2026-08-18 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8595b07-3e91-3215-8d47-20d2cc3bd7a9 | -8.74837 | -62.91043 | 2026-08-18 04:57:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 326b604a-30d4-39f9-885c-8d064f1143fc | -11.35876 | -46.39835 | 2026-08-18 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0be3553d-0fc9-3674-a63e-3f69988e32cb | -7.39488 | -46.48435 | 2026-08-18 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c007a46e-cbcf-35dd-9359-223a4f9355f0 | -9.16621 | -59.70735 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58753ea1-a6f4-3675-985a-2dcabca16279 | -6.79448 | -59.44852 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9127bec0-4977-30f5-96f0-2648ddfc2589 | -7.53827 | -46.61542 | 2026-08-18 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5cd0f066-14e0-35fe-88e4-6e3ccf11ae23 | -8.637 | -54.71745 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eeb83695-2cdb-3468-a2ca-a14c522a726e | -9.47041 | -51.60583 | 2026-08-18 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8c81914a-58b2-3810-b01e-7310f8440489 | -6.78482 | -59.45147 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d065ff1e-e67f-3659-a09d-3b4c4edd70fe | -11.36419 | -46.39393 | 2026-08-18 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 904395b0-3ecb-3853-a59a-1fbee6802821 | -7.61777 | -55.63107 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a20fead-5756-3947-9b24-42aa31ec366d | -8.56859 | -54.70249 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bab9a28a-bd64-303f-857c-757e4da09ea4 | -8.59257 | -50.3421 | 2026-08-18 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| dea2f78f-a2cb-36c4-bf71-9b8b96fa7b8e | -8.3324 | -46.47736 | 2026-08-18 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a61054f5-1ca8-3d3e-9b53-cb087eab7f6d | -11.32547 | -55.26792 | 2026-08-18 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1cf3ef17-c12e-3922-9ddc-d0fd3a782d94 | -6.84865 | -58.99725 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c454742e-3478-3bb3-9f40-b894bfe00db3 | -9.82205 | -47.27864 | 2026-08-18 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66bbefec-ed5f-34be-9017-3a0c0dbfd4ec | -8.2238 | -55.03644 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f7d1b39b-2bda-38d3-b904-29f7c2dc227f | -8.58195 | -54.72694 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| f5b4d4fd-1415-397c-b9a9-6fa8c271c836 | -9.8979 | -47.73718 | 2026-08-18 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b733282-6c37-3718-9b3b-4094cb380ca9 | -8.57405 | -54.73306 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| b5c3191a-f801-323d-b43b-032ed4650676 | -9.46074 | -51.62327 | 2026-08-18 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3eff205b-ff53-32c5-baea-9aa0f4e17256 | -6.74234 | -59.16915 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ea4cc42f-2bf4-3658-baa7-78d99f705b3c | -11.20061 | -54.81582 | 2026-08-18 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 970b2803-d60e-3ee3-8e6c-341ff4940195 | -9.50346 | -51.64118 | 2026-08-18 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65dcf795-dbb3-3d64-8fb1-b2578bb95a55 | -7.63751 | -55.64241 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de5a6324-ca75-355d-ad68-6835584e222d | -9.12272 | -46.04498 | 2026-08-18 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 775cc04e-b30f-3b92-a3f6-f325d61389e5 | -7.37285 | -55.49239 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84ce4e30-f413-3545-b9fb-30eaaafcb29f | -12.4689 | -54.19481 | 2026-08-18 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 340dd6b9-d623-3f22-b687-ec7feb30f633 | -6.04223 | -57.9659 | 2026-08-18 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de4241fd-785c-3071-be69-b57f5bbed3f9 | -6.60674 | -58.9617 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40e6962b-516a-3c01-975e-b38ad02663fa | -8.90195 | -60.60212 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8552e2c-193f-331e-b5b4-cc59639b27ed | -6.95989 | -59.03233 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 931f0572-d2ce-3f70-806c-f5e035eeef15 | -8.89563 | -60.59337 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c58d68b-d5be-35b1-9240-c4f1834e189b | -7.61842 | -55.62715 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dab8ca18-e47f-3c45-92b0-910058f32c40 | -11.18898 | -49.68351 | 2026-08-18 04:57:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b55ee8c-66ae-3c2e-8fad-cda23a4e78cc | -9.42392 | -60.45457 | 2026-08-18 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 184878fd-d892-3efa-86f6-412cb67344e8 | -7.61492 | -55.62658 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3fbeb427-a021-3e9e-8869-a3bfe40465be | -6.77943 | -59.76066 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ce09d8d-0373-3798-ad5a-b598db73fbb7 | -14.23329 | -45.41106 | 2026-08-18 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1cf9e0b2-7035-32ff-b004-aff282870169 | -8.72881 | -54.58769 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 380c0439-617d-3d58-9eac-2b8d8ee3fc72 | -7.88917 | -63.76678 | 2026-08-18 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 514d1c0b-d6ac-3a07-8ea3-0f6e6eb17cea | -8.56051 | -55.31697 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce94cc64-4fa9-36f8-94d0-4d7922f0d2bf | -9.16329 | -59.67219 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26a11927-b79b-3284-9a19-d92700e9991f | -9.12615 | -61.60154 | 2026-08-18 04:57:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fad24315-326b-3e14-a993-0253583da059 | -9.42328 | -48.25314 | 2026-08-18 04:57:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 613a4321-0826-368a-9980-a3db31823824 | -8.56685 | -54.71331 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f3cbb1c1-4c87-3fa9-a8a0-02c1f872f548 | -9.08454 | -50.86641 | 2026-08-18 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43b75add-4c8c-3985-bf70-9d4d12f35763 | -8.20247 | -55.03716 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d3ed75f7-1e3f-3a3a-b7e5-c6bf0b56b70b | -11.52921 | -46.64476 | 2026-08-18 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df386296-1709-3f6b-82b6-325c6bf63bb9 | -7.46001 | -46.1582 | 2026-08-18 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5a81b16d-8b1e-3ea1-8b60-78bfd6d53914 | -8.58542 | -54.70528 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 655c3da8-364f-32bb-be6a-d6dc6ae33a5a | -8.36604 | -46.36851 | 2026-08-18 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ebe2651b-7160-39e5-9a59-a87d36a684f3 | -6.31088 | -55.71055 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac111eac-4410-3333-82cd-2f794ac4babd | -8.56465 | -54.70555 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8195549a-b509-38d3-b343-bfa56be6e980 | -6.69293 | -58.95086 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 725e8703-0491-3a94-8b56-5e126f690e21 | -6.87367 | -56.41534 | 2026-08-18 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ee97e4e-8b15-3cf5-b6aa-43cff283ad88 | -9.13655 | -46.01537 | 2026-08-18 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 653a9270-9ba1-3a58-bf85-f5b4e21e2041 | -8.56394 | -55.31755 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a32a0c06-c67e-384e-9667-c1b547f55d37 | -8.7538 | -62.91149 | 2026-08-18 04:57:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3dc62ace-ed1b-373e-9153-df785d3105e0 | -8.57521 | -54.72582 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 0c916a1d-f25d-34bf-b7a3-d96112f6511b | -8.57034 | -54.69167 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b4b79a9-9960-366b-9f44-b716f07395cf | -11.35177 | -46.37323 | 2026-08-18 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 052a400c-9fff-3809-90d7-f95e3039acc6 | -11.26324 | -54.85183 | 2026-08-18 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3675b33b-a4f7-3f4e-ae45-629d92bcee1d | -8.58821 | -54.70943 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03fa628d-a4ab-3c26-9873-c4ec3804fd71 | -9.7959 | -47.30544 | 2026-08-18 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e28ae6a-1580-3de9-9eb2-3345ed8c3dc1 | -6.75111 | -59.17358 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| fd32e661-4d41-3622-ae91-1994b652b2d2 | -9.47696 | -60.50063 | 2026-08-18 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da70143a-9bac-3833-ab18-47253278a9e8 | -7.90367 | -61.72972 | 2026-08-18 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0133b516-3d84-3646-aa4e-704c128a77b5 | -7.39637 | -55.48023 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 102e1062-fa60-36b6-88c8-3f4fbc562207 | -6.75113 | -59.1703 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 96f6d5b0-f9f4-3e57-9118-e4d0f6d92fb1 | -9.93775 | -53.64046 | 2026-08-18 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd1eb433-70db-3f85-ac29-d0754e7660c5 | -10.56798 | -51.96121 | 2026-08-18 04:57:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65790148-ae62-353d-8222-cb11e7907440 | -9.21264 | -50.09777 | 2026-08-18 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0943691e-5d15-3afb-8293-eeaa09ec2cd5 | -12.71549 | -48.48746 | 2026-08-18 04:57:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1f807c00-feb6-3665-bceb-bfe40ee8e2e1 | -7.90823 | -61.7337 | 2026-08-18 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e8535aa-d140-3de8-a692-64df88bf0a94 | -11.45732 | -46.57404 | 2026-08-18 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 757fe360-0aea-3929-9b17-e9d3cc393c49 | -8.61225 | -54.72088 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 525fb577-7fec-37fa-96e0-6b96ef72edb3 | -11.8326 | -55.21819 | 2026-08-18 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca73bb16-999e-3ea5-8367-595b01b60c0c | -8.5859 | -54.72387 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 348630a0-4ac2-31c5-a6f7-68fd87661779 | -11.36487 | -46.38871 | 2026-08-18 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e6170903-ad3d-3734-86a7-0289027dbb1e | -7.63592 | -55.63008 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a11f301f-a821-3050-a7fa-eadea7b1f3e7 | -10.13412 | -62.40275 | 2026-08-18 04:57:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 709846bb-c003-3cdc-a1ae-7464b63ab4ae | -10.56116 | -51.96019 | 2026-08-18 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c50852ba-e473-39fc-9809-0d32083def23 | -12.05743 | -58.04018 | 2026-08-18 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75b6f637-e526-31c6-80f6-b78011a90945 | -9.42186 | -60.43967 | 2026-08-18 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6be7f291-3a29-39f0-a3e4-87a46886938f | -6.1097 | -57.73541 | 2026-08-18 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 889541e8-e5e8-3184-9f58-33abcbfb8d69 | -7.63021 | -55.62104 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b3217ff-e5ba-3591-9332-13c152a51cf9 | -11.18828 | -49.68827 | 2026-08-18 04:57:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ee67c9d-af4e-35ff-a000-54e0102f4994 | -6.68264 | -59.07227 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c68149e-9b27-3f6f-bdb5-a2248ab55836 | -7.5012 | -60.07887 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e78ab620-3c36-3b7a-85cb-e0601a549569 | -7.72685 | -49.31546 | 2026-08-18 04:57:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2548c401-25dd-39ba-a8ea-f612d7c81dfc | -8.08365 | -44.3591 | 2026-08-18 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f5a5bf5e-8e2e-3c6c-82a5-9c2773e8041b | -10.78057 | -50.32701 | 2026-08-18 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37fbdaf0-5def-3816-af32-dd3364431d39 | -8.55708 | -55.31641 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README41.md)
