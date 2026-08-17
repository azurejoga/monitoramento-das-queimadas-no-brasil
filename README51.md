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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77c3edc6-f231-3f02-a2e6-0726b4a35a1b | -6.86545 | -56.42138 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15db587d-3c7e-3b26-8394-74c8dd512592 | -11.13855 | -46.52987 | 2026-08-17 05:16:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 968c6097-ed91-37ba-b46a-7f931743649d | -8.97069 | -60.52847 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52b56a61-d5ef-3207-be7d-eb12758ee7d9 | -7.88651 | -61.79853 | 2026-08-17 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 59a59c05-896d-394a-a3f1-8e665b7873da | -6.62296 | -58.97734 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 756198a0-6da8-3641-94a5-f02ad7f8652c | -6.96735 | -59.03673 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78adb9a3-ebd4-3bca-acb3-b1de71456544 | -8.64086 | -54.72299 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 614be8df-7d1f-3543-813d-3ee172d71146 | -6.09659 | -57.72539 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30bbe257-0a9f-36cf-b702-35c950bb7f5f | -6.63815 | -58.96877 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82aae8b8-0910-3867-ae69-96ef99c3713f | -8.96751 | -60.50408 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d54c536-bf11-3047-8e95-84cb9c388217 | -6.69762 | -58.96364 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d093f70-c960-3e3c-a53f-dbe53f7c73d6 | -8.96688 | -60.50795 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b147acf-91ea-321b-a002-97c6ce86f01d | -8.8946 | -60.59969 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e1f53657-d9e4-3c0c-8fd0-1236df14a5fc | -6.63421 | -58.97181 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a597825-895f-378b-bebe-0758c68bbe0a | -8.61379 | -54.67933 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81954b6f-af51-31de-91bc-0c1cbc530cb3 | -7.41755 | -60.00463 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06a7ed39-7a9a-348c-9865-6282f9429c90 | -6.11202 | -57.71367 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4cc6e356-6c65-322b-a52c-adbe8fd1eb4b | -6.86881 | -56.4219 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b538679-1655-3ee3-8952-d872dc30ac2c | -6.98973 | -59.0477 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd7dd838-387f-3437-8e75-d168fcfac458 | -8.73519 | -62.91082 | 2026-08-17 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a5e7d061-302c-31a3-b1e0-267cd69ce5b1 | -8.61173 | -54.7184 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5430d511-e5ba-3fe4-912b-e9f8563cf9fd | -6.10156 | -57.7368 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ae99d513-9164-3666-8110-9e466ca43d28 | -8.89653 | -60.58802 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1b6c647-83a3-3403-ba7e-ca01671ab82e | -7.37972 | -55.49144 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3e498416-eaf9-3374-93de-0715c3969c1b | -8.98358 | -60.58896 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef0ec522-eed5-3ee7-b1dc-b21c7e14a99b | -7.38435 | -55.48431 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bdf10aee-4fc6-35dc-aa20-38f73dc3dc81 | -7.37836 | -55.48807 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 248fac47-ee3c-3711-9ad8-46a08a7a1d9d | -6.11149 | -57.73838 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12c934ac-53d4-3938-a79e-cacc9095e508 | -8.5061 | -54.92405 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd6544ae-3798-397e-930d-4d95d1154cbc | -7.77796 | -48.2764 | 2026-08-17 05:16:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7b4b2fb-7bde-397e-bbd8-5006c9e72196 | -8.67698 | -62.8772 | 2026-08-17 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2662dbd7-7346-3a79-81ac-380dcb5481e4 | -6.99367 | -59.04465 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| deeca75f-d8a6-3881-b33d-2f4ce291710c | -8.60032 | -54.69477 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cebd9662-fbe1-3812-9f1f-918e2c961860 | -6.62243 | -59.06591 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5382172b-b680-30b3-9502-19f89f82cdee | -11.09439 | -47.30726 | 2026-08-17 05:16:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18d20fb4-a4dc-3701-9e6b-028b783b4f0a | -7.3836 | -59.99524 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9a807e43-72ff-37be-8641-5c702d7aa1d0 | -8.95773 | -60.58622 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99c1a1dc-c337-3093-9ec3-25ba08a57bf2 | -4.12611 | -56.32708 | 2026-08-17 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 272fffdf-5c93-37cc-9f94-1cb16db30358 | -6.98531 | -59.03227 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4a45185c-f4c0-3894-ae34-baa552a1c837 | -8.52489 | -54.89721 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d65aa55-08e5-3e80-a9d0-60e3c8a347f1 | -10.46602 | -46.30732 | 2026-08-17 05:16:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f9cb918-0d54-37cd-a69d-b81e8788fa09 | -6.85364 | -58.98144 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c7b3001-ab08-31f5-9d4a-a67b444caf0e | -8.95394 | -60.56555 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c14900a1-7efd-3d9c-a837-a62c5f629cb0 | -8.9702 | -60.51892 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87e25a74-113a-32e4-aa2f-c43fc0b3cb0a | -6.82526 | -56.45894 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9020019d-aec6-3824-8cd2-e8800fec685f | -7.421 | -60.0052 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 769da480-d31b-36f6-a839-e48ba5f509f1 | -9.12734 | -46.0223 | 2026-08-17 05:16:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f80f9700-dae7-315e-8c04-f6284426156b | -7.90686 | -48.52649 | 2026-08-17 05:16:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a64bacbe-5dff-3e8a-9730-29d32093dfe3 | -8.95899 | -60.53448 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c99a28ca-9b46-3e93-9b54-5570f4ddf7cb | -9.18912 | -60.7914 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a9acd16-679c-3bbf-81c6-698028d99fff | -8.58308 | -54.68511 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| e9062361-abf7-3ee2-9c1a-3d83082a7529 | -8.20812 | -55.00949 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f189d30-4671-3f48-b918-ebe8e84b43d6 | -7.56139 | -60.8582 | 2026-08-17 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b045aadf-8018-3c35-b572-32e0db5afc49 | -8.97006 | -60.53235 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d45247a-f8b5-35b0-843a-1af3090f5f92 | -6.82191 | -56.4584 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe812b26-5c15-391d-99cc-9342843e2e65 | -8.97457 | -60.53558 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c018c87d-c030-3b90-9456-b87c9e28d97b | -6.77246 | -59.45994 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c8eb810-6967-39e8-8363-903dcfdd4f01 | -6.12912 | -57.73409 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b879980f-6713-3ddf-800a-794a904b814f | -7.55505 | -61.16953 | 2026-08-17 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0923dc39-66f2-3453-b970-918e91417380 | -6.70385 | -58.94626 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0f1180c6-f9e6-3aec-8232-9f2e84222dc4 | -6.76603 | -59.47791 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a46ca7be-d99c-3d11-8361-436273c10d2a | -6.76969 | -59.75806 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb36ff42-3983-39c4-a326-c7c7e67567da | -7.41531 | -59.99648 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23a24c0f-4c92-393a-8b01-1993331b02f5 | -6.63758 | -58.97235 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cafeb33-4898-3b1e-ac6c-1017306a30e0 | -7.87443 | -63.75237 | 2026-08-17 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2bc0860-1511-39c3-8a35-eb3076e849c5 | -9.19792 | -59.66573 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79e082ee-afb9-32c5-915d-5f23d04cc573 | -8.67448 | -54.77151 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3f0e1c3-f2ef-33f3-a533-a73369626383 | -6.24725 | -55.6207 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d79b0fc7-8dbd-3f3e-8321-e6fd8d13e39c | -7.55321 | -61.17963 | 2026-08-17 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| dea50b0a-6dc0-3ccc-af8e-918bacdd5cc9 | -6.10816 | -57.71659 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 293bd199-02c4-3c6f-98f2-dec9c5d6066e | -6.77606 | -46.3388 | 2026-08-17 05:16:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ccb40b83-3c8e-312f-a2fe-c84d0f18afdd | -6.68707 | -59.07266 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c6fc2d33-9590-3efe-89ae-c883c2b55ba6 | -8.97626 | -60.50404 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21657718-df9a-382a-94f6-0ec0e544d0ef | -6.10871 | -57.71314 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a59e538e-f9c7-35c9-877a-332a666243ee | -10.50691 | -50.02291 | 2026-08-17 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 47251486-a423-3d34-939d-377128f79732 | -10.5065 | -50.02592 | 2026-08-17 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dc175f54-899b-3e9b-accf-304f57443b68 | -6.6308 | -59.07836 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db722a75-3ad1-3172-808e-2024944c128a | -7.87934 | -63.74914 | 2026-08-17 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9840ac70-d618-3aea-94f8-613bf10e2fb1 | -6.6258 | -59.06644 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e02c8ce-e0e8-3ea4-b690-17af7e1b5a42 | -7.45584 | -60.00214 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a511b5b5-ec23-35bf-b3da-4b0a1bf9493d | -7.06777 | -56.64889 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65eaddd5-5f4e-3997-a0a6-698427af546b | -8.95139 | -60.58118 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8eb57b16-3aef-35ac-9468-373f6f19ee56 | -6.97129 | -59.0337 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6f939361-aa82-3e6f-a4f3-e0cb0fbc67f3 | -6.86671 | -58.94316 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2b62aab-6905-32a0-9023-a59577b3ba5e | -6.60168 | -58.97047 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3f3a7571-1b67-31dd-a651-677ace9db32d | -6.10818 | -57.73785 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| bc06a97b-3d4e-32ae-b5a1-c0ef9d8ce303 | -9.47129 | -51.62614 | 2026-08-17 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4db8b754-81e7-335d-9b95-74ec6aef7235 | -7.40471 | -60.01825 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0cb2112d-cbed-333f-b12c-691156e8a0cb | -8.89938 | -60.59249 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dc5d0107-27ba-3552-89ee-9231174a2807 | -6.96253 | -59.30276 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 339d7d21-24c5-346f-a46b-796263016999 | -7.77827 | -48.27323 | 2026-08-17 05:16:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 655ddf0d-2c30-3de5-8972-c6f3b1c0b626 | -6.62405 | -59.07726 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2df2d77a-cd8b-35ea-9cd7-f1850febb55f | -6.69656 | -58.94872 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c215f139-a800-3031-bc85-b80427d9a11c | -6.77587 | -59.4605 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b79c9e0-25ba-34ec-a61f-7e149b4b8068 | -6.65334 | -58.96017 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d6df3b35-56bb-377b-927a-422aa2cc8c3f | -7.54957 | -61.179 | 2026-08-17 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d93c9173-69e9-32de-a1cd-49701d408625 | -8.02874 | -55.14113 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 322c01fb-1345-300a-82d3-a13f4f4c531e | -6.12963 | -57.68812 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74ae6c5f-6886-3c90-8866-37b81a8c61f3 | -8.96562 | -60.51568 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f91e19b-ffbf-3764-a8a7-26bebb46cb52 | -3.88989 | -59.34812 | 2026-08-17 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README52.md)
