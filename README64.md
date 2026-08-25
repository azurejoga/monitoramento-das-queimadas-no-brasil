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
| ca1af229-5de7-3cb1-aa75-d7a802192d27 | -6.80932 | -58.66151 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8801e37-0780-3a5f-9ee0-78ea3e9dad45 | -6.54429 | -58.51431 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e00b6793-bc0f-3ba8-ac08-2b15c2cef275 | -6.72557 | -59.45124 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 97b504a4-25c1-3f68-9646-ededb07eaf2b | -9.06589 | -60.43979 | 2026-08-25 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b8bc019-05f1-3513-ac45-b90ac4ba5f17 | -8.57451 | -54.87456 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be1a7d66-8a7e-37a6-99db-c5f7a2fa507e | -7.49258 | -55.35102 | 2026-08-25 05:48:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df286e74-2c3c-3971-9da3-2e175719f2d8 | -6.1343 | -57.82476 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65085100-6531-3121-a998-41b4a23e13a9 | -6.51224 | -55.22327 | 2026-08-25 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5df9037c-121b-3ce2-8f42-46d4bd978377 | -6.63832 | -58.49335 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| ff89d771-904b-37d7-b47c-9c8b48bab943 | -6.21438 | -55.48666 | 2026-08-25 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3aede6d-88e4-3c88-82c7-7232d46599ee | -6.51744 | -55.22392 | 2026-08-25 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0425cc4e-209d-3bfd-81bc-bed101cc5de5 | -6.33299 | -54.75397 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09eb4700-be3b-3ce2-b685-0b372d0e39b3 | -6.82554 | -58.65687 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5cef151b-8b2a-35ec-a83c-87e1b7527843 | -6.17125 | -53.70275 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33a27e1d-96de-3775-bb26-e475abbeb27c | -9.16339 | -59.39877 | 2026-08-25 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a926ece-8b38-3c9e-931a-887ca9f53a84 | -6.62416 | -53.19239 | 2026-08-25 05:48:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8543c077-ee5b-365c-93e7-3223f2ec254d | -6.61471 | -58.38274 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ee0b7cc-9dee-3a8e-bfda-03b8ff7b9b95 | -6.98718 | -59.2485 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e7aa50e8-d4e2-32fe-b01b-42acc0480e07 | -6.12452 | -57.83151 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4095d3ae-d3e9-3d6c-8cc5-16c5d2dc87fe | -6.86271 | -59.41311 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d0669fe6-a774-3a87-a73f-ec520310147b | -6.96337 | -59.07708 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b25aa395-8295-3100-b6f3-532b21e90d35 | -7.44341 | -59.7758 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a38c7f90-d13a-33a3-8de8-276a314eabb5 | -6.62698 | -58.48394 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6f2f45c6-9dc7-31dc-98ae-9149e6e58bed | -8.68779 | -54.69969 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8443d411-7900-3174-8ab0-fcc8c3a847ad | -6.89085 | -59.03085 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4accfb5-7e39-3e31-bdca-12e6b68ce82a | -7.49173 | -55.35734 | 2026-08-25 05:48:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6357a0b9-eb4e-3966-b96c-47535cdefb87 | -6.95248 | -56.4953 | 2026-08-25 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 612011c5-e3ee-3aa9-91b6-dfa433fa1cdd | -6.22567 | -55.47987 | 2026-08-25 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab453790-a4fe-36ad-a7b7-e53dee1fd151 | -9.15882 | -59.40171 | 2026-08-25 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e348452b-b4da-30a7-b32c-5e57eef54f51 | -6.80043 | -59.45745 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f0c07a96-fcf7-3e39-8760-de17c7fc6032 | -6.91827 | -60.07029 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0c11bcd9-fec0-3502-b6cf-8caa9ca213c8 | -10.79712 | -50.91562 | 2026-08-25 05:48:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 68ce20a7-ab84-39e8-9424-c3bc6055bb3c | -5.94252 | -57.72773 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e68ad211-384e-3414-921c-ee621c1a7d7a | -7.01964 | -59.24827 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0928be69-c877-30f5-8aaf-ba69d6ed5403 | -6.85244 | -59.40138 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cba3fc47-2b02-37d7-b7a1-d37de2e63fa3 | -8.80421 | -62.32953 | 2026-08-25 05:48:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3635a47-a3fd-3557-a43b-c37bdf6fc8c8 | -6.35101 | -54.78049 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2dfcb17-c03a-349a-b8c5-d3c9cc99e75f | -6.86659 | -56.41268 | 2026-08-25 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ba25121-8f91-315f-b5ee-421d5d79ab02 | -6.22317 | -55.92236 | 2026-08-25 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c979a55-ad64-39fe-a6ef-a84d27ddfeab | -8.6208 | -54.73896 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 708fa5c1-4146-3212-a5d5-ffabe3b3a1ad | -9.02897 | -50.81396 | 2026-08-25 05:48:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f78af5e-7be4-363d-96c7-480f99f0dfc8 | -7.00133 | -59.23508 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4a39b1c5-c33c-3cac-9f78-5aec91bcb5bc | -6.32766 | -54.75321 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36af03e0-a8bd-3ba1-b082-14f7002bbf06 | -7.21653 | -60.62475 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5971643-7241-33f5-8fb0-f10fea1f4bdd | -7.0117 | -59.24713 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 821a6e3b-2583-3d6e-a7b7-463ccde3884e | -6.93878 | -52.79461 | 2026-08-25 05:48:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60a656a4-58ae-3edd-84ea-772f8c7db72d | -6.85953 | -59.40755 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7eb71044-d72e-3fda-b0eb-060ce31f6ad9 | -6.63364 | -58.49644 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 00d3a547-10e4-329c-a374-1ad811c143b8 | -7.38796 | -55.18194 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9a66ae6-6c8f-3d56-92d6-d8615f777068 | -5.78801 | -57.56265 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1bfb748-8889-3bd1-a671-ae5801782d89 | -6.63112 | -58.4846 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf0d20ba-cbde-3015-a44e-678c5d66f880 | -6.83598 | -56.45612 | 2026-08-25 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b869ca28-b09f-3499-83aa-78d8c81744e7 | -6.61157 | -53.34699 | 2026-08-25 05:48:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9dd170cc-3e5b-3029-a233-cb3e0b16cc51 | -7.2105 | -60.61496 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 7298605a-e274-3f7c-8d9d-0b9b7cc1488c | -5.78861 | -57.55845 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4009422-fed1-39a8-a5dc-4cac6c1dfde1 | -6.63257 | -58.50387 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b9e86489-b20d-329b-9568-52eb800e33ce | -9.0621 | -60.43922 | 2026-08-25 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f9ed59e-ea01-3554-b366-dc77058d3aa6 | -6.17858 | -57.70531 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cceed463-0756-3f10-8e58-f96ccf460a2b | -6.14454 | -59.91134 | 2026-08-25 05:48:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23d2f31f-76ac-3e28-a9aa-473b9f2e46d9 | -9.16707 | -58.3302 | 2026-08-25 05:48:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c7821e1-8b21-3b5f-a727-12f5af9975fc | -8.66312 | -62.83937 | 2026-08-25 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed65d28a-1535-3caf-bd1f-20bd1a1ca8c8 | -6.33206 | -54.76064 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 414b9fe9-b775-3d58-a195-70cc11914584 | -8.57823 | -55.27773 | 2026-08-25 05:48:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf4dcfdf-dd8e-30f4-8ea0-741ec8703c43 | -6.14879 | -57.69679 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 52b431e1-9c09-3404-9c2e-859793dc1f09 | -6.26117 | -55.41241 | 2026-08-25 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| adbad66e-58ad-3d11-ac36-8034fe5f3da1 | -6.34459 | -54.74886 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77576b02-031a-370f-a7a1-43ea4821f695 | -6.63004 | -58.49208 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 53bb70da-4f00-37a8-8c2f-14e2479374d0 | -7.32374 | -64.69406 | 2026-08-25 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13e43bb2-f8ee-3c0a-b30d-6519c03ce094 | -7.5396 | -61.3672 | 2026-08-25 05:48:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e93280fb-08c1-39a0-b04c-3771b81f39b7 | -6.69562 | -58.72267 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cdf93747-97d2-3d69-97c4-3722595e2071 | -5.94127 | -57.73609 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a32f8bbe-c26e-3507-a4c7-d7d4a3e39b39 | -7.23229 | -60.64449 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74d10176-e7ac-34c9-8c6a-3149c454fcd6 | -10.77798 | -50.9295 | 2026-08-25 05:48:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 40.6 |
| b73d6e02-dcbe-3301-8af0-d8c8d58caa62 | -6.33346 | -54.75063 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9611a293-2c90-31ca-80d7-44e3bf323ff6 | -6.93814 | -52.79928 | 2026-08-25 05:48:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8324e168-b801-3a92-adc6-aef33923802f | -6.71923 | -59.44017 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c0491ca1-fd02-310a-b69c-e97bfefd8157 | -6.23074 | -55.48061 | 2026-08-25 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 63cdeb19-0a7f-3f6e-8dff-e088d86d369d | -8.57424 | -55.27776 | 2026-08-25 05:48:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 84d6a2f7-cd3a-3e3c-bec6-0a2629ba3e7a | -6.32719 | -54.75653 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a6574b9-28ae-38a5-8071-d0d2d688929b | -7.54081 | -61.35924 | 2026-08-25 05:48:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da6dad53-db4e-3b20-8f98-02ef3e165fc7 | -6.15235 | -57.93858 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0b9c41f-006f-3fe1-90cf-97a18a276268 | -6.35871 | -54.76447 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1d19ce5-4756-3bd0-adc7-9beb5ce96777 | -6.3402 | -54.7414 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c84a385-f8aa-3dec-a1b2-bf0aab3c75f7 | -6.17921 | -57.70106 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3899555d-e9f1-3eb7-8a0c-61d6d0e3508d | -7.54436 | -61.35977 | 2026-08-25 05:48:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 39dc6484-b780-3a14-a744-3c95f5be4543 | -11.15664 | -54.00287 | 2026-08-25 05:48:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b475eea8-5900-36f8-9cb8-668c785533df | -8.81685 | -62.33924 | 2026-08-25 05:48:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2699d51b-0de9-3e89-8745-a414620523ea | -6.6367 | -58.50452 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| aa965746-a7f9-3c7b-9dfc-de9277c54ee2 | -6.64193 | -58.49765 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2f7d1883-d67b-38b5-8f25-f81296aec184 | -6.12393 | -57.83549 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92c24d2c-40b1-3de6-a023-3550daf593cf | -6.62644 | -58.48772 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4f32ccf4-bbb7-3944-aef2-1a2897f67942 | -6.34851 | -54.75971 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 400387ae-0631-348b-b411-4529d88e7ebe | -6.34945 | -54.75301 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18997045-9688-3639-a182-e07c2f466cdd | -7.49608 | -55.35781 | 2026-08-25 05:48:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d606cecb-1c28-3b05-956e-63886ce45702 | -6.84364 | -59.46063 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7cbcf7d8-9c73-32cd-aff1-01114c410daf | -9.15124 | -59.397 | 2026-08-25 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a36294e2-da34-325d-93f2-af422a3cf6f7 | -6.17849 | -53.48107 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1728edb9-ac7e-352a-9426-e06fb2013cf3 | -8.58543 | -54.8761 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79ccc611-6063-36ad-b5f5-89ec17325cc3 | -7.00529 | -59.23573 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f1eef384-3cf9-3c74-bb47-f17dba2f34ca | -7.63603 | -63.3862 | 2026-08-25 05:48:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README65.md)
