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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 716425df-431c-362a-aec0-1a82738a8657 | -9.87221 | -46.4845 | 2025-09-12 05:18:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6c58513-c3b3-354c-90a5-4cdade40c8d3 | -9.14402 | -58.91563 | 2025-09-12 05:18:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5773085-a0d6-3d32-a0f9-f66ca7da426d | -8.55199 | -48.9555 | 2025-09-12 05:18:00 | NOAA-21 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 14578c4a-a2fc-3e7b-876c-22cafb1a46a2 | -11.88109 | -58.82333 | 2025-09-12 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 82f27235-fd4a-3d94-b727-58f3b88b03d4 | -11.1989 | -55.08297 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a86ff4d-74cb-3de8-8db5-36772c350c4e | -6.40374 | -58.20801 | 2025-09-12 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 125c4426-ae58-3a94-b0a7-fcd7d3061903 | -11.70653 | -50.5982 | 2025-09-12 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c400bd95-972c-3c84-a438-e4df3130ad28 | -8.88058 | -49.93371 | 2025-09-12 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3f814f5b-da7e-38c5-95e9-d807443ee647 | -10.71298 | -48.61887 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5fc9a765-d07a-32e0-8498-9b5c2dd034c1 | -10.40547 | -60.81115 | 2025-09-12 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61bc54a1-08bd-3744-9f5b-11f4846878a4 | -8.89715 | -49.93612 | 2025-09-12 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 574cd471-bc99-31b0-9c79-6bca008406d7 | -11.18476 | -55.0663 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c03728b0-3f84-3353-96e9-8714687831cf | -10.43249 | -50.62162 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d580913f-74a5-3a9f-b119-56415666da93 | -7.72172 | -50.35484 | 2025-09-12 05:18:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dafb1c2c-3df3-3d73-ac9a-c0b73c915d07 | -9.77756 | -47.85287 | 2025-09-12 05:18:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f85e6edc-a9a1-3afd-ae66-6f9287ee64dc | -10.44135 | -50.61592 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 239ce546-239b-3015-bd0c-a7e96f3c04c0 | -8.09607 | -54.75671 | 2025-09-12 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 35f40fef-0ae3-3c7f-8648-8a153d385f0d | -7.49529 | -54.94734 | 2025-09-12 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d315945f-bbbe-37c2-b4b1-d744e0e35af3 | -10.14424 | -46.31508 | 2025-09-12 05:18:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3311fd00-67b5-3f23-b09c-9629741b94e4 | -11.79462 | -50.56904 | 2025-09-12 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46daef2d-4320-35ed-9362-31be5f2b50cb | -10.42495 | -50.5952 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 22101f88-bcf0-3541-b688-61ea43cd508d | -10.52242 | -51.52367 | 2025-09-12 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 124674f7-e9cc-3a79-8309-29842e17c2ea | -11.18779 | -55.07417 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 818b025e-15e0-36d4-880e-117a60baf1df | -8.48599 | -47.27593 | 2025-09-12 05:18:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| afd99e36-e65f-325d-9e1f-f16e147d6690 | -9.03481 | -47.10342 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| edcbbfe3-0252-3f16-bc52-354a9a01e41f | -9.71537 | -64.92506 | 2025-09-12 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cda8978c-8bff-39e3-a1c6-9498663c75c1 | -10.68928 | -48.6607 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1145168e-d70a-3d0e-bf5e-1a94baaa9d6e | -11.16409 | -57.18178 | 2025-09-12 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 984864b9-bd50-3d80-9db7-9d4c0449f69c | -11.54346 | -50.60348 | 2025-09-12 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6a33c63e-0e39-32a7-851a-3e38fda0008d | -11.96517 | -51.1749 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 50.3 |
| c271908e-f846-37e7-9ac6-ac58f9005b53 | -10.55003 | -51.53939 | 2025-09-12 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 62d1128b-7eff-3842-9f93-e3fc7ea19bf8 | -9.48482 | -55.99031 | 2025-09-12 05:18:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d82f9cb-f5c8-3b98-a490-b783455adc8c | -11.18426 | -48.4322 | 2025-09-12 05:18:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec7ad56e-8bfc-3b6f-856f-3a5817f8dbeb | -11.18527 | -55.06265 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 006033e3-2c16-3c7c-922e-9cfedcb9029f | -10.85381 | -48.15736 | 2025-09-12 05:18:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 28dbbda9-6d87-328c-a159-bee5504d1b6e | -11.5297 | -50.39183 | 2025-09-12 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 65c577fb-c3a4-302a-8768-7b3018550827 | -10.4212 | -60.47509 | 2025-09-12 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd493f15-d60d-3cf4-8e79-5d252c43ccf3 | -9.07784 | -50.49791 | 2025-09-12 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5abde0c9-e819-3f7e-8098-fb6f28758a79 | -6.14977 | -57.91287 | 2025-09-12 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c1ee8946-b8f5-3167-a03a-e27af9b7dda5 | -12.87617 | -47.95236 | 2025-09-12 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 268f6680-a329-3e44-991c-b34ba8f98272 | -10.33751 | -58.02104 | 2025-09-12 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c912500b-3452-3dea-b44e-36811a2bd564 | -7.94214 | -63.67962 | 2025-09-12 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58b6f7ed-6688-39ff-9468-3df9fc6dc90c | -11.98509 | -51.13381 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c216b4cd-ce11-3c4d-8073-4caa1988752a | -11.19382 | -55.06038 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70701eba-4da1-3157-88fd-117f3c1894cd | -12.4664 | -53.83399 | 2025-09-12 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ecf1a6a-ddd3-3153-9706-35ec80d7a568 | -9.48739 | -55.97224 | 2025-09-12 05:18:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7d327f0-ef4c-38c0-90b4-63e3cd77a190 | -7.65806 | -50.27222 | 2025-09-12 05:18:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 532e1677-8a29-3544-b1a4-73078725da30 | -7.79278 | -50.77808 | 2025-09-12 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bbd64991-4b05-3707-852a-7ef92fa8aded | -11.1772 | -55.06145 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4765cb22-3cd2-37a0-a7d1-249200b49758 | -7.71637 | -50.3546 | 2025-09-12 05:18:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ead87af-c644-31f9-8e68-34a0fd750537 | -9.95856 | -51.69125 | 2025-09-12 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 40fa740f-7ec4-3526-878e-e256f8cc21aa | -11.52958 | -50.39791 | 2025-09-12 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 487cd949-46f5-3cac-9a6c-449367580eba | -9.4251 | -58.98862 | 2025-09-12 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94a2a53e-f8cf-3f86-9cce-72db87652c86 | -10.38753 | -50.49993 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d06fedd-b5e2-3b2f-b945-d7c56b35c9ee | -12.84889 | -52.97561 | 2025-09-12 05:18:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c5dd136b-e733-356c-9450-d85bbdb936ab | -11.98468 | -51.13719 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b29d9e1d-f8c4-3779-ab07-64c5923259d1 | -11.69529 | -46.53382 | 2025-09-12 05:18:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e9bea00b-c32a-3ead-8031-8a1285275244 | -9.06917 | -47.04121 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6b173b4f-694d-3e42-851e-6664008de32c | -8.89065 | -49.9427 | 2025-09-12 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f7f74567-1c42-35fb-933b-151c5e8dc34c | -11.10594 | -51.97649 | 2025-09-12 05:18:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4e4623ca-83aa-3559-bfb1-474e19fd0928 | -6.82869 | -52.79672 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 68b6fb51-beba-33bf-9f5a-dd6b28e9cc65 | -8.08141 | -52.37918 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c1d13e9e-3c2a-3af6-9dd0-a4e6ca2159dc | -10.13731 | -46.31327 | 2025-09-12 05:18:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ac69ce27-d317-3995-9110-8a2c31076e32 | -9.03681 | -47.10458 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f6b53a11-2d9b-31c8-873d-a162d96bc210 | -9.06931 | -46.95279 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 70c43aac-7098-340d-b6f4-a94566956b59 | -7.22913 | -55.05312 | 2025-09-12 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56410a21-d85c-3815-a1b4-b51ec0365405 | -12.00703 | -47.77068 | 2025-09-12 05:18:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 75d9266b-8dc2-3a49-aa61-5653d5805a57 | -12.22713 | -53.87738 | 2025-09-12 05:18:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a38fb70-011c-3c6a-942a-eec153da9134 | -10.84688 | -48.16155 | 2025-09-12 05:18:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6bacb1f1-8bf9-3450-953a-d70569dcf36b | -6.82049 | -52.79092 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 87667097-499e-3f5a-93a7-aba3c0838181 | -10.44359 | -50.59785 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2082cacc-8431-3af0-a070-d5c6cba571dd | -9.99495 | -51.72797 | 2025-09-12 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 60051bf6-7f1c-39c4-8420-c3b6fc3807dc | -9.89789 | -51.88097 | 2025-09-12 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| aa04dd8c-8204-393a-be44-3513e0ce6eb0 | -10.56171 | -51.48824 | 2025-09-12 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e9377f3e-61f3-315b-9a35-8b8762896dc9 | -10.42258 | -50.61344 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f6b22a0e-44e6-3f3f-a9ce-eaa0e246f065 | -12.09128 | -47.59965 | 2025-09-12 05:18:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| b48678c8-1e33-3e06-8d8e-a54579dc75f0 | -7.22412 | -55.05415 | 2025-09-12 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c52911fa-275f-3744-b0a0-32767f71021b | -9.72341 | -64.92641 | 2025-09-12 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 116ef2dd-5b74-32a1-8536-601ebd394d37 | -9.80205 | -59.10185 | 2025-09-12 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a136b24b-66af-3ac2-b399-fddc151a836b | -11.95935 | -51.16809 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 57ceb99f-0fd8-365d-92f3-a13d59e4a5de | -10.42924 | -50.62513 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2ff172ad-1738-360f-9e10-e1e34fa78387 | -9.03549 | -47.09758 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 813c8f8e-e22c-33c6-9e73-5665be958d24 | -9.0472 | -47.05557 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| eb26b2f5-9809-3cd3-a97e-1c70226460a3 | -10.85262 | -48.16768 | 2025-09-12 05:18:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 63308314-7e19-327f-a050-603f79ba0b15 | -11.94713 | -51.1801 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3bb3eada-21ff-3cf9-8c53-0bc42802b572 | -11.96072 | -51.16745 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f83ae91b-2a89-36e4-b9a8-c08ff9875446 | -10.68402 | -48.65226 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 48c51576-6624-33bb-9072-bdc16fa5ab85 | -9.45899 | -62.36349 | 2025-09-12 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e7e698c-58a4-353a-9e1f-41d7d22c2408 | -7.81175 | -55.22095 | 2025-09-12 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4053b93-cbe5-3f76-adde-2569bf21aa2c | -11.78404 | -50.56389 | 2025-09-12 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c078af03-0e58-39ae-afdb-1c29e871dd47 | -9.80077 | -48.88791 | 2025-09-12 05:18:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ab15ea53-85f2-32dd-91a8-b2bdf323c5c8 | -10.44268 | -50.60516 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6d97430d-fbf5-34c7-917d-1abb63c4a807 | -10.27305 | -47.02093 | 2025-09-12 05:18:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec53288b-1a2b-37ca-b17c-115e0d1424c4 | -9.83326 | -54.53455 | 2025-09-12 05:18:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 117941e5-0154-3d58-958d-e34ad963c477 | -10.43509 | -50.62218 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3ac38722-21fd-3848-8e11-db6c6c706ddb | -11.54503 | -50.40535 | 2025-09-12 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 60356d57-3f6a-35ab-890f-5ff04a9f8328 | -6.81428 | -52.80315 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f167ff05-0ce6-3ae4-8414-a462a95036f7 | -9.33877 | -65.45822 | 2025-09-12 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbba6170-a7bd-3a7d-81a2-7e47937f9234 | -11.0872 | -48.41007 | 2025-09-12 05:18:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 51923325-6f4c-38cf-bb6a-966fddb9ed1d | -10.35097 | -50.52719 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README106.md)
