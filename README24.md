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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc59f521-b2ea-34b5-a4b8-fd827f5aadbe | -10.47924 | -46.97617 | 2025-08-03 04:53:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0da6303-d8c4-313d-aed8-266185e54a5c | -6.61527 | -59.95361 | 2025-08-03 04:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e2e06dd0-3ee0-366b-a9e7-3b7ae5e2fb65 | -8.02873 | -43.11965 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9d72d69f-e08e-300e-826d-af19a1e1e83b | -12.44717 | -44.86604 | 2025-08-03 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 273331f1-0e81-355e-9b72-a52698cc3fc5 | -12.61977 | -44.50658 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2083a95e-436c-3ead-a819-b1fb402d3d66 | -12.65116 | -44.48856 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d68dcea5-4141-36c9-a275-890ffa7e6325 | -12.66325 | -44.52578 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d9a7581-a07c-3575-93e8-bb8125ad4172 | -12.64446 | -44.49844 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 865ade0c-330f-3d2e-841c-0449305688de | -12.64238 | -44.51593 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9525eb2e-4f8d-35bd-8f98-c59568d8f2d2 | -7.99822 | -43.19349 | 2025-08-03 04:53:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 045b1b9c-6063-315d-875e-fa4c8c8e4bb0 | -8.04137 | -43.11006 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 571f6149-635e-3b63-a898-d0b6b841c1d2 | -11.20961 | -51.53371 | 2025-08-03 04:53:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8878a5b-7116-301a-a5e6-a81c8a06e9a9 | -10.34432 | -44.90549 | 2025-08-03 04:53:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a7158401-a9c9-3939-b9cc-c08ad4754537 | -12.66367 | -44.52229 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4cabf885-1e42-3c49-88d0-877b2dfd06fe | -6.81491 | -59.27439 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 19ed266e-c76e-354c-a5e1-f5013d80d026 | -10.47785 | -46.95351 | 2025-08-03 04:53:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8fc8d194-ea49-37d8-8404-06ba5ee7433b | -10.47863 | -46.98053 | 2025-08-03 04:53:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| deaf852e-f2df-3b79-b04f-945cfa25f9a7 | -11.21307 | -51.53425 | 2025-08-03 04:53:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3d03a70-ef63-3d87-b48c-654e3d4178e8 | -12.43076 | -47.03974 | 2025-08-03 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 085b8086-43fa-31ad-bd07-36dba757e24d | -8.04992 | -43.10697 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e70d7a9e-beed-39e0-a701-616da33aaa8d | -8.87928 | -44.7938 | 2025-08-03 04:53:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1661552-d0d4-3630-94f0-b7cfefb6adac | -12.66409 | -44.51879 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5fb3f75d-fad5-39b0-b641-377e2d84cdfc | -8.41803 | -47.45867 | 2025-08-03 04:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 94891e8e-e16f-33ea-8b26-876294807c69 | -6.63671 | -59.94184 | 2025-08-03 04:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05749460-3d58-3798-9222-79a1c1874039 | -11.18944 | -51.47963 | 2025-08-03 04:53:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1e2c7ad9-9dc0-3847-ba5a-b1ca04955fae | -12.65533 | -44.49985 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 78580078-628e-37e4-95d1-150c44fb7124 | -8.03769 | -43.1129 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| f5d89708-04f9-3400-9145-4480a667a7fc | -12.65198 | -44.5278 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e579009e-c2d7-3bea-8829-430e2c349a9f | -8.02851 | -43.13818 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| ee855a28-b2f6-3e00-a297-4b2b186c388e | -7.01103 | -45.55999 | 2025-08-03 04:53:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| beaef0ea-c1e8-30ca-84fa-95ecbe0eae27 | -12.63781 | -44.49476 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9ba472d-8f4f-33b8-940a-019471a8bf5b | -8.34716 | -46.90641 | 2025-08-03 04:53:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e03823f8-3ec6-3dc7-ba67-a3c966c326f0 | -6.61409 | -59.96588 | 2025-08-03 04:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8ba0ec9-8dbe-343d-b1ef-5c41c0d43e63 | -6.63272 | -59.9431 | 2025-08-03 04:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 43e9ca1f-b235-3f43-b002-08ec5f9dd748 | -12.62107 | -44.49613 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 97dd858e-6179-3787-aa8e-148ae3d207a8 | -9.35268 | -50.7408 | 2025-08-03 04:53:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1d7a5e0-6080-3cb0-9fce-cf6c943a7291 | -6.64565 | -59.10769 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 497b8846-ef2f-36ac-8e06-a2223df9cb67 | -8.01233 | -43.17321 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 0cb348ce-b092-3e24-941b-b6d3f347d507 | -11.93729 | -46.72464 | 2025-08-03 04:53:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8dd25cc-537e-3116-98a4-ffdec9e3027d | -6.7365 | -59.18058 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d07bdce-40aa-31b6-92b2-6e13eb61f5d6 | -7.8823 | -45.5275 | 2025-08-03 04:53:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d5cde04-ddf8-39fc-aa80-d9a6dd284721 | -7.12611 | -44.38244 | 2025-08-03 04:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4adfaecd-49de-36f2-93bf-f211f25118dd | -11.21249 | -51.53807 | 2025-08-03 04:53:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c72ea46-da85-365e-94bf-6d038471fbe5 | -6.64491 | -59.11207 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 3986597e-4fad-3c47-a9c8-3dc1c0016c77 | -12.62519 | -44.50731 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a39e02a-2343-3b63-86cf-61167e892d47 | -6.82621 | -59.26235 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4009fbd6-ed0e-3a76-86f2-1b21f10bcdeb | -8.87966 | -44.7909 | 2025-08-03 04:53:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31aa2e8d-3f04-3807-aea5-a95bde9e48d7 | -10.78797 | -48.80595 | 2025-08-03 04:53:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 37224cc2-14d0-32ed-b5cb-d8929bd959fb | -11.41191 | -54.71725 | 2025-08-03 04:53:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f207ea5-14f7-3b85-9259-0894c9e2c67d | -12.66452 | -44.51528 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 937efb64-0315-3785-b974-70018149ff04 | -8.01481 | -43.15511 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 13eb39f3-44dd-399d-b563-4d703814ec12 | -12.64413 | -44.48845 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c94fcb8-b0c8-301f-88e3-9c6726b810c5 | -7.75702 | -45.10945 | 2025-08-03 04:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 38c4abc9-5309-3a2a-9435-88294a32cbd5 | -12.63359 | -44.49697 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 72926b19-2367-3351-a530-52dc447885ab | -7.51717 | -61.32093 | 2025-08-03 04:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b10ca141-7d68-3164-b706-a1357d61b840 | -6.66947 | -59.16851 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| acee4c22-a0e1-38d4-b83a-c2d9ab6238d6 | -8.00874 | -43.15794 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.9 |
| 268b90be-5c14-3200-a2eb-adb89c14cd59 | -8.43056 | -47.46055 | 2025-08-03 04:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30e99a73-68d8-3b6b-a928-0119ab0f7fd7 | -8.0314 | -43.14285 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 0d30ce01-3dd4-3453-862b-81f205354026 | -8.01633 | -43.14402 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b0c0586a-510b-3f96-bf26-b073ff48c6c6 | -8.0212 | -43.13378 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 725e676f-9290-3add-a6a3-32873b845ec9 | -8.01879 | -43.15236 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 37883061-d030-39c0-a53f-6591330ee7b1 | -8.11504 | -49.75646 | 2025-08-03 04:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 771b8412-7156-3925-8352-42841a29c181 | -12.6453 | -44.4914 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f704d78d-0354-36a8-8b22-3a9c7d9917d7 | -8.33671 | -46.9175 | 2025-08-03 04:53:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91ca8cf7-a9be-3d52-ba03-ae9362e5d964 | -8.04088 | -43.11381 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| e7a9e242-7a16-3513-8003-f799752142f9 | -8.01735 | -43.13657 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f28ac747-07d7-3792-81e8-0e7dbf765332 | -8.05355 | -43.10413 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| bf93246d-86f2-370b-b644-d36a951d0e5c | -12.62563 | -44.50384 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e22f858-8a7d-3c83-9e59-2a87581fc10c | -7.60159 | -44.99139 | 2025-08-03 04:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5d2faca-f1e9-32ae-9198-5889f5506f71 | -7.75836 | -45.11719 | 2025-08-03 04:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| deba7480-c50c-39eb-95db-02d5af6b2764 | -6.635 | -59.95202 | 2025-08-03 04:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 374689aa-42f6-3252-ba80-53c3f2aa7cb2 | -12.63561 | -44.51227 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 970b50d8-3e11-3d52-aed6-036c85466ae4 | -8.87605 | -44.79268 | 2025-08-03 04:53:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 389c5194-a7fd-315d-8f43-28a11081fb25 | -7.11774 | -43.48049 | 2025-08-03 04:53:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4a9fa1c4-aaa8-358a-9c3c-8d1acfcb51bb | -8.03188 | -43.13913 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 31428c81-72c7-3553-8e07-7f68dff671e3 | -6.62534 | -59.95734 | 2025-08-03 04:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dd038e4c-9f05-34eb-a7a5-3b15f060b6df | -12.63194 | -44.49757 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6294210b-2f28-3336-bf91-b36264a78ef6 | -7.4126 | -47.00334 | 2025-08-03 04:53:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a8e78a3-18ff-345e-80d3-a32691183b48 | -12.6406 | -44.51645 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25f5ac6d-cf7f-3292-85c5-377e9f99dc80 | -8.00776 | -43.16516 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 46.6 |
| 6389c80d-8df0-3eb3-9a90-6709b0233019 | -12.6428 | -44.49899 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dcc4ca64-51b0-30b7-8451-c607e530cd92 | -12.44757 | -44.86284 | 2025-08-03 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33a36b7c-f20c-3b45-a737-cd32e05cd506 | -12.63517 | -44.51574 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b757dcc-2139-3087-a0b7-d6d3b6f3f073 | -8.88148 | -44.7907 | 2025-08-03 04:53:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a2dfa49-df75-323b-a65d-ce16e3cd1d4e | -12.48878 | -47.1614 | 2025-08-03 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a0837bdf-2c72-3fbb-92d1-647258a7b38e | -8.00375 | -43.19447 | 2025-08-03 04:53:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| b135fe40-fa7d-3042-9a04-f914897f94ed | -6.68442 | -59.16198 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5fe034af-a162-3e9b-ba34-bea97031cdb9 | -8.0199 | -43.15946 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2b3181e5-ce1c-3faf-9feb-8bc2cf77dd48 | -8.43003 | -47.46434 | 2025-08-03 04:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9edd5af2-5264-3cc4-af6e-c9bc907908d7 | -12.61477 | -44.50238 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 877ee174-df0a-3659-8dbe-eb60356dcaff | -12.63106 | -44.50456 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e71364e9-1b12-36b6-9c28-3a3bc19d9944 | -6.62063 | -59.95647 | 2025-08-03 04:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 01001000-1d26-316f-b463-8d99a932c10e | -6.9552 | -44.22372 | 2025-08-03 04:53:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4bf163aa-7c62-304d-bf61-7a2eaaa45dcf | -12.64488 | -44.49492 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9370543-7db0-3ea8-83e2-7431b320e6d5 | -12.66119 | -44.49701 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 25368db1-e7e5-3ae0-9069-39ec92a0262f | -6.61499 | -59.96081 | 2025-08-03 04:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3fee6fab-08d2-37f7-a637-97aa50d05a19 | -7.52257 | -61.34993 | 2025-08-03 04:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f712b8d-3104-3116-8a52-c87b423fc68c | -7.96746 | -45.09955 | 2025-08-03 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6f8e249f-3e74-3a81-9f5f-8af86acc8e6c | -12.66494 | -44.51177 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README25.md)
