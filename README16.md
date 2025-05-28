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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c92b57dd-c71c-32f1-a96c-2aae40b033c0 | -7.6762 | -46.0995 | 2025-05-28 08:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| dd8abd39-3678-329a-a89d-cb163ac8b118 | -7.6762 | -46.0995 | 2025-05-28 08:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 0f482f57-f589-3142-bcd7-49477ba3c881 | -7.6762 | -46.0995 | 2025-05-28 08:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| d57d878f-6f21-3418-b838-581001432d44 | -7.6762 | -46.0995 | 2025-05-28 08:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 550616b9-84b1-3dd4-9acf-a501fcae0cce | -13.0874 | -45.2791 | 2025-05-28 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |
| cae1e7ed-f20e-377c-9739-eff2d180002a | -13.0874 | -45.2791 | 2025-05-28 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 71e854b0-d4b0-3c26-a74b-8ed6eb7b113d | -13.0874 | -45.2791 | 2025-05-28 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 179.8 |
| 45bf0ffe-f52b-3ce5-81f1-59c35d10ce42 | -6.3161 | -43.3848 | 2025-05-28 11:50:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| e920f868-f296-385e-8a66-d22245512fdb | -7.9827 | -50.7201 | 2025-05-28 11:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| cda1b03c-04cd-3813-b000-ad7b49bb69de | -13.0874 | -45.2791 | 2025-05-28 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 202.1 |
| 6b2d786d-9b25-3706-81c9-769bfa25a2d7 | -7.6762 | -46.0995 | 2025-05-28 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| a66acef9-cac8-3193-ad04-ee9960d0da4a | -6.3161 | -43.3848 | 2025-05-28 12:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 07fc2bad-8a5c-3176-9c04-70f147694bea | -12.4086 | -49.9978 | 2025-05-28 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 599a3844-4b39-3e95-b9e5-e8ef13baf658 | -7.9827 | -50.7201 | 2025-05-28 12:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 9216eb33-6814-332d-af58-17cb84ee2ba5 | -13.0874 | -45.2791 | 2025-05-28 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 149.8 |
| f0b4c065-e92d-3930-8a86-c5bc6af02327 | -13.0874 | -45.2791 | 2025-05-28 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 188.5 |
| d6437a4c-b4ba-390a-817a-44b10c91ce5a | -6.3161 | -43.3848 | 2025-05-28 12:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 015c3469-d860-32f3-8190-39f0d096fc56 | -7.6762 | -46.0995 | 2025-05-28 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| eca5d7d8-26b5-380e-bf63-26133e91c95b | -7.9827 | -50.7201 | 2025-05-28 12:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| c86fa179-406d-312a-ae74-6893ac1c4eb2 | -7.6762 | -46.0995 | 2025-05-28 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| ae85a5c7-e482-3c45-8eee-a3ee9ecbd48b | -5.9748 | -43.7613 | 2025-05-28 12:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 3e66932b-f114-359a-96a9-6be3843c78f5 | -13.0874 | -45.2791 | 2025-05-28 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 202.9 |
| 981202db-ab4a-3691-9a6b-31b6c0ca4553 | -7.9827 | -50.7201 | 2025-05-28 12:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 9166ca42-e043-3195-b328-8135fed3ca24 | -12.3324 | -49.9857 | 2025-05-28 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 6f8f9805-2ed3-3b27-8d3d-701f50a3bd99 | -6.3351 | -43.3598 | 2025-05-28 12:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 7ae31144-7e77-3e43-850a-8c6746bc9453 | -6.3348 | -43.3832 | 2025-05-28 12:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| ebc18bd7-02c5-3346-b82a-3261860f9a69 | -7.6762 | -46.0995 | 2025-05-28 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 910e5755-22a9-30ac-8c44-7083b153fcb3 | -7.9827 | -50.7201 | 2025-05-28 12:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| eaa6538e-0de3-3269-b4f1-5dc2a7c0c627 | -6.3161 | -43.3848 | 2025-05-28 12:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| c965203a-2cea-3bb2-a06c-953c5c0a6d73 | -12.3324 | -49.9857 | 2025-05-28 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 3b42ca9e-5917-38e0-81d1-cbd55decb0be | -13.0874 | -45.2791 | 2025-05-28 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 173.3 |
| 3d007109-18ee-323a-8682-0f9060938874 | -13.0874 | -45.2791 | 2025-05-28 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 192.7 |
| 87573d05-d719-3a81-bdcb-91ac2f07db8e | -12.4086 | -49.9978 | 2025-05-28 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 3ac34536-82e0-33f1-ba8b-0a8e2126e337 | -14.681 | -45.0956 | 2025-05-28 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 1cacbbeb-d719-3920-8223-664e86757a85 | -12.3324 | -49.9857 | 2025-05-28 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| a5505517-4669-31df-b49f-ede4c657d546 | -7.9827 | -50.7201 | 2025-05-28 12:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 4796f2ab-8980-3f69-911c-e702c724191d | -7.6762 | -46.0995 | 2025-05-28 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 18ff496c-9ce7-3b0d-b2b3-1f956c0b1072 | -7.68617 | -46.0906 | 2025-05-28 12:42:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 8c13e8d2-325e-3a83-b027-a3d173d51875 | -10.63189 | -48.08045 | 2025-05-28 12:42:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| b0596726-660f-3c72-b140-fe12fb8c6bdd | -11.56943 | -47.61306 | 2025-05-28 12:42:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 83cb8b2d-04f2-3f58-9799-e0302a55d60a | -7.25731 | -47.29001 | 2025-05-28 12:42:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 32e0ba90-a6dc-3393-9319-0d9ebca4f265 | -6.23456 | -43.35463 | 2025-05-28 12:42:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 66e74832-8eee-3daf-903c-7079f743d75c | -7.40145 | -44.29902 | 2025-05-28 12:42:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 5a09f791-ac5c-3c2e-ab63-422017dbce57 | -5.97976 | -43.77703 | 2025-05-28 12:42:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 0c816663-e37a-319f-b3b4-dcf14e150197 | -5.98241 | -43.75594 | 2025-05-28 12:42:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 84698613-8070-32f9-ba0f-22358ea9a36a | -10.06192 | -45.3441 | 2025-05-28 12:42:00 | TERRA_M-T | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 50bbef53-45af-3794-9225-c39f08eedea5 | -6.32378 | -43.37072 | 2025-05-28 12:42:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 89fe2c71-eda2-30d7-89f9-fc3ad6f31058 | -10.06733 | -46.36829 | 2025-05-28 12:42:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 3ed6e5a0-2c56-3c2a-95ed-054b436bf5c8 | -5.96914 | -43.76994 | 2025-05-28 12:42:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 94a7ea01-5c20-30e0-909c-5877150c8d44 | -9.17935 | -45.32551 | 2025-05-28 12:42:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 6576ecaf-67aa-3f3e-9ddc-7af815a418c6 | -6.31738 | -43.37648 | 2025-05-28 12:42:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 0b375aa3-4c6e-3326-b98a-ac0de6954d61 | -10.71925 | -45.32715 | 2025-05-28 12:42:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 64a8c0ea-8a28-309e-9710-8f69a2816ac5 | -11.88617 | -47.45659 | 2025-05-28 12:42:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1dbdc0d5-6eba-3062-89e1-10b7839ffbc7 | -8.68328 | -48.28371 | 2025-05-28 12:42:00 | TERRA_M-T | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 498a4294-5cb5-310f-854b-595f22551dc3 | -10.71722 | -45.32092 | 2025-05-28 12:42:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 21.5 |
| f8ed805c-e942-375d-aa57-83b68b2267ce | -11.88792 | -47.44302 | 2025-05-28 12:42:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 253c286d-ad53-31ce-baba-e1ada245a968 | -9.03508 | -47.73343 | 2025-05-28 12:42:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c5d37794-7532-3b8e-af07-8237e3de6b44 | -5.78127 | -43.60517 | 2025-05-28 12:42:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 4678cfdc-8c37-3e51-b87e-a7f8c2181e51 | -10.0053 | -48.4878 | 2025-05-28 12:42:00 | TERRA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 12fae566-cde8-3739-a0bc-0b47eb645a57 | -10.06446 | -48.2728 | 2025-05-28 12:42:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 17317160-fc8e-3fd9-8d67-72bfff41ff33 | -10.0806 | -46.3546 | 2025-05-28 12:42:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 7ac053d1-92a4-3e0f-98d5-979639518953 | -5.77127 | -43.47336 | 2025-05-28 12:42:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 5598716f-44d0-384b-8db0-7b1c88e9faec | -10.22867 | -47.42402 | 2025-05-28 12:42:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 3e2f6284-03be-36e2-89c9-f000f12b73d5 | -6.33383 | -43.35587 | 2025-05-28 12:42:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 830161da-9298-3493-bbdd-137a055d4523 | -9.07085 | -51.14992 | 2025-05-28 12:42:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5fab4b3c-0e6f-3d0f-8eed-9ab37037bd8c | -11.22372 | -48.60894 | 2025-05-28 12:42:00 | TERRA_M-T | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d46c6e13-adaa-3723-8e51-be2f870afb63 | -6.33739 | -43.37254 | 2025-05-28 12:42:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 07429bbc-00d3-3c9e-a568-16ac4f1a6016 | -11.56777 | -47.62601 | 2025-05-28 12:42:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| b27085eb-fc57-328a-9e63-f4167d914b94 | -11.03697 | -46.1217 | 2025-05-28 12:42:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| bb7e18f4-55ef-3f51-ba5e-184261e06fbd | -10.4354 | -46.7984 | 2025-05-28 12:42:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 472d4fd1-2922-33f0-9c5a-5f3cf7b598dc | -6.12834 | -43.94818 | 2025-05-28 12:42:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 4ea5a0b2-8fe8-3652-b2b1-06a84cfe8952 | -6.20738 | -43.35081 | 2025-05-28 12:42:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 26eee7f6-f56e-3ed5-a00d-39cb36f6b339 | -9.17531 | -45.31849 | 2025-05-28 12:42:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 40.4 |
| dc6f7c79-e908-3584-9aeb-4f3a576142c2 | -6.33098 | -43.37835 | 2025-05-28 12:42:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 419c737b-10ae-3613-9bf7-ec6f8837166b | -8.01428 | -47.34914 | 2025-05-28 12:42:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7a7b789f-1d86-3545-9a22-8f0473961453 | -4.01824 | -47.86032 | 2025-05-28 12:42:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 3bf0add2-cc19-37a4-86ae-06bacb0c5c93 | -7.68422 | -46.10506 | 2025-05-28 12:42:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 4faff918-b3cb-3be7-acac-2b74ffa0f916 | -7.40071 | -44.30496 | 2025-05-28 12:42:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 06a5b66f-4b0d-3a31-916b-11af0efdee58 | -8.62675 | -51.54385 | 2025-05-28 12:42:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 81ed1c35-00d2-368e-8e24-489e546de99a | -11.17144 | -49.58604 | 2025-05-28 12:42:00 | TERRA_M-T | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 614e8b7b-ca52-3d9d-b478-eee726406b72 | -11.22509 | -48.61502 | 2025-05-28 12:42:00 | TERRA_M-T | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 27967242-1b84-3a38-ba08-1a1575922e87 | -5.98223 | -43.77171 | 2025-05-28 12:42:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 50.0 |
| d78ef83f-206d-3852-955c-0710e78cd1d0 | -10.66441 | -49.44539 | 2025-05-28 12:42:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3bd3d535-5434-349d-841a-cc370aca91b6 | -10.66259 | -44.48799 | 2025-05-28 12:42:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| e95df1f8-46d2-30a0-a4da-56ba8d82a2fc | -9.04353 | -47.74656 | 2025-05-28 12:42:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 161e3d3d-eee8-3bac-8b56-f00ab10b46eb | -8.75715 | -44.9213 | 2025-05-28 12:42:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 251af06f-5783-31ac-ba29-e96e2a01461d | -5.98505 | -43.75066 | 2025-05-28 12:42:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 3b4d1df4-fd6e-3cb0-9097-d7d45a03532d | -9.94252 | -50.85699 | 2025-05-28 12:42:00 | TERRA_M-T | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 25.3 |
| beb92941-59e3-3a24-9785-ac597be76dab | -4.00884 | -47.85917 | 2025-05-28 12:42:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9a3562ff-bc41-3aa7-9ae7-ebcc465e3490 | -7.67503 | -46.08905 | 2025-05-28 12:42:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 30299abd-8f1e-3eba-a47e-1548e2c611c2 | -10.05959 | -45.36241 | 2025-05-28 12:42:00 | TERRA_M-T | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 8ac9cbf4-432d-3599-8582-22e68717421f | -5.7685 | -43.49499 | 2025-05-28 12:42:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 36.1 |
| ca1384b5-cf98-3d67-ae78-e7e899e9a0a9 | -11.5783 | -47.62741 | 2025-05-28 12:42:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| b0afce2c-f77f-3bae-a4ab-6da143d9db7f | -7.08469 | -46.04993 | 2025-05-28 12:42:00 | TERRA_M-T | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 6b992b39-c59f-3e4e-8066-66e3ba287f6f | -9.75222 | -48.24581 | 2025-05-28 12:42:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 3e894e0c-47c7-35d1-896e-5d7cda207cec | -10.43727 | -46.7841 | 2025-05-28 12:42:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| aca6af9c-5d0d-32f2-8478-6e940a39c2a7 | -10.45553 | -47.94938 | 2025-05-28 12:42:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| a8edce66-766e-3976-807a-b093dce49c8c | -8.62806 | -51.5349 | 2025-05-28 12:42:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| e23349e5-b1bf-3e85-9356-436639083d1f | -10.66125 | -52.69935 | 2025-05-28 12:42:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 666c2f7b-c055-364f-b8af-343bed54b341 | -10.06926 | -46.35297 | 2025-05-28 12:42:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 43.1 |


[Clique aqui para ver as próximas entradas](README17.md)
