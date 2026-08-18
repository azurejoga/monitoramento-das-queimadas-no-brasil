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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb7d7cad-bb5f-370f-aff2-3463e80e5ff5 | -6.841 | -59.0132 | 2026-08-18 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 196.2 |
| adc2859d-c2e7-3165-804b-b198f8cbc277 | -6.8411 | -58.9939 | 2026-08-18 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 129.2 |
| d091a32c-19c5-325c-b9d3-9c2c2e386b51 | -9.1706 | -59.6762 | 2026-08-18 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| ed2dc25d-5a4a-30bc-bc1b-938cec4e2357 | -6.7123 | -58.9412 | 2026-08-18 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| d23d374a-cc89-32e4-8794-e01e7d535392 | -6.8017 | -59.4394 | 2026-08-18 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| f7c9fdfd-bf20-33a4-91c0-3fe78708c306 | -6.9516 | -59.028 | 2026-08-18 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 6952df0b-6358-3f67-a7f1-c985d47ceb63 | -15.3037 | -56.445 | 2026-08-18 14:30:00 | GOES-19 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 5fe8b44e-3fd4-30ee-b670-916e930d931b | -9.0673 | -50.8419 | 2026-08-18 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 9794ed2e-924e-348c-b25d-821ff12ece01 | -6.9884 | -59.0457 | 2026-08-18 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 9e116f2f-2d5d-3478-8e46-c185c1c23f2b | -12.7601 | -48.4231 | 2026-08-18 14:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 7300dbb3-55c0-3ad2-93bd-3fa03748492a | -6.0366 | -57.804 | 2026-08-18 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 2a27bcde-2465-3bec-8f8f-3feefb032ef0 | -7.2007 | -43.2814 | 2026-08-18 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 113.0 |
| c923138b-c44c-3ffe-9c2a-339af0b35ad6 | -11.3491 | -45.9292 | 2026-08-18 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 315.1 |
| 457db594-b7bd-3ccd-b23b-d22d62041aa0 | -12.7793 | -48.4205 | 2026-08-18 14:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 176.0 |
| 4c5df29b-8bfb-3572-b49b-d200c37019ac | -14.1824 | -52.9089 | 2026-08-18 14:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 175.0 |
| fb87151b-b2e2-324b-80d9-cc6f2ea5a15f | -8.5853 | -50.3543 | 2026-08-18 14:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| c9019903-7c76-3d7c-81a9-bf041e1e1dd0 | -12.7981 | -48.4399 | 2026-08-18 14:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 9f187fcd-107f-3864-a2b4-43fa319d43d1 | -6.0181 | -57.8047 | 2026-08-18 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 3231165a-3940-3ad5-9fdd-f89b5fa23da5 | -6.0179 | -57.8437 | 2026-08-18 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 6ddcc0a1-9931-3aaa-b907-78495d118bc9 | -12.7597 | -48.4453 | 2026-08-18 14:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| bdec8f9a-9bae-3959-a247-4f34c88dcc25 | -14.3733 | -51.8679 | 2026-08-18 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 904c9e87-e609-305a-9c11-5247c8265db1 | -6.7815 | -59.748 | 2026-08-18 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 1986c2eb-5ba8-3ebc-a234-8953cb9099cd | -9.1705 | -59.6955 | 2026-08-18 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 0de44218-a370-33d3-9241-0993c3d18b5a | -14.1821 | -52.93 | 2026-08-18 14:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 172.8 |
| 55e26071-1128-3f6d-823b-ae50312a7b96 | -7.8068 | -47.8591 | 2026-08-18 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| d688ed0a-f4c8-381a-a1c2-557e53db4a55 | -14.4704 | -51.8337 | 2026-08-18 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 8b1db2d5-809a-31e4-a0fc-24ce67f70dc9 | -6.6014 | -58.9844 | 2026-08-18 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 431028fd-4e69-3981-aa9c-baee796a7384 | -8.4899 | -48.821 | 2026-08-18 14:30:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 107.1 |
| bb1f2f77-a56a-389d-8be7-2793cbb6a5a3 | -11.1368 | -47.263 | 2026-08-18 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 4ef9c98f-eb64-3397-a6e5-bf997d94f004 | -14.1628 | -52.9323 | 2026-08-18 14:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 268.8 |
| 0b52d58b-d562-33af-aad6-1f2865f82c0d | -13.4117 | -54.3737 | 2026-08-18 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| f25ddc51-6a25-35d6-b64b-cdd3c2d7b534 | -12.7601 | -48.4231 | 2026-08-18 14:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| adfc778e-1a2c-33f8-8fee-a1af6ba4a7de | -6.7478 | -59.1716 | 2026-08-18 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 08e2ee16-10d7-3197-9565-55037dd99eba | -10.2765 | -50.4313 | 2026-08-18 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 176.7 |
| c8850881-b32e-3d5d-b777-0b13eab16f5b | -14.3525 | -51.9559 | 2026-08-18 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 3dc48815-3483-3793-a98d-fb55cfc98b3b | -11.3055 | -46.2527 | 2026-08-18 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 60c7f068-7af1-3e6f-afa7-7f8fbbf160c4 | -12.7597 | -48.4453 | 2026-08-18 14:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 5ae3757a-2a9b-3eb6-8480-a45650a38b69 | -9.1706 | -59.6762 | 2026-08-18 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 01eadede-9af6-34ec-b61b-f969bb54d73c | -6.9886 | -59.0264 | 2026-08-18 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 3c567805-4aa3-3ed1-8530-57be89b777ea | -14.4656 | -52.1112 | 2026-08-18 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 5467a816-ad39-3bf6-954a-ae63a6f6c094 | -6.6199 | -58.9643 | 2026-08-18 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 5c26a9d2-9980-340c-a1d7-9310f1856f3e | -6.8017 | -59.4394 | 2026-08-18 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| ee43de9d-54d4-3047-ab03-fd54fb5ea15b | -9.1705 | -59.6955 | 2026-08-18 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| b096f073-a272-32a3-884f-7f5d170d5bef | -14.47 | -51.8551 | 2026-08-18 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 1a1a3f2d-4b11-31cb-82e4-de5cffd277c0 | -6.0181 | -57.8047 | 2026-08-18 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 6f82387d-807f-303b-829d-2c6e74824edd | -8.5853 | -50.3543 | 2026-08-18 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| dbf0b944-ae03-37b6-88ee-00ec10e8a94d | -6.8411 | -58.9939 | 2026-08-18 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 138.9 |
| c29a957f-12ee-3382-aad1-a06e1361a424 | -6.6014 | -58.9844 | 2026-08-18 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| fe22494b-ca21-3b65-9fd2-fcc8f92caad8 | -6.9701 | -59.0272 | 2026-08-18 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 80e41c56-1f6d-3131-953e-75ce0b9973cf | -6.7814 | -59.7672 | 2026-08-18 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 126.3 |
| eaeb5ff0-94d0-3ad9-90bb-9ba4730d5f93 | -12.7009 | -48.5195 | 2026-08-18 14:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 11e46098-2284-3387-b611-6dd32db1eccb | -14.4475 | -53.1913 | 2026-08-18 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| a6f8ae3c-18e2-3840-92c4-97c3dcca5dee | -14.1824 | -52.9089 | 2026-08-18 14:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 121.7 |
| ab400254-fdc1-3fef-a23b-55fd4429cc77 | -12.7789 | -48.4426 | 2026-08-18 14:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| e2f18da2-c118-3a5f-9955-6c392bc63448 | -14.451 | -51.8363 | 2026-08-18 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| bc906673-6ddb-3993-acb1-962ece50bb17 | -6.0366 | -57.804 | 2026-08-18 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| e88dca9d-c83c-39e5-97b7-78564165da32 | -6.7122 | -58.9606 | 2026-08-18 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| fb9ab601-cf73-35f8-b9a2-f0da7333d4aa | -8.604 | -50.3527 | 2026-08-18 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 101.9 |
| f1dbf48e-97c5-3beb-a16a-7c106b72d22b | -14.354 | -51.8705 | 2026-08-18 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 0ff2301a-0861-37d8-90f6-688e745fd94b | -9.0673 | -50.8419 | 2026-08-18 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 2f8c7e03-20b3-35ed-92bd-03bf12269651 | -7.0069 | -59.0449 | 2026-08-18 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.0 |
| b1bb8a8d-7bd8-31a9-a5a8-0937e31b510d | -7.6236 | -60.9594 | 2026-08-18 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 67c7f240-8968-3a34-b6c2-854c3da2209a | -6.9516 | -59.028 | 2026-08-18 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 6c412139-c1f4-341c-98f3-f00c37d69867 | -11.1174 | -47.2877 | 2026-08-18 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 1e153c69-601d-362e-a5f6-de6e100825c5 | -14.1628 | -52.9323 | 2026-08-18 14:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 170.5 |
| 8fa111c0-6914-35ff-8dad-71f823fb7bd7 | -7.8068 | -47.8591 | 2026-08-18 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 15b69c13-d1e3-3a52-b4a5-f7ec94920351 | -3.8816 | -50.3259 | 2026-08-18 14:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 22623793-404f-3700-b968-0c9d0b4d39c8 | -6.7831 | -59.4594 | 2026-08-18 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| f2b7b831-4c0b-3af4-a6ae-15ccad49c8f1 | -8.4899 | -48.821 | 2026-08-18 14:40:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 9c16838b-2504-3d53-8d3e-7873567fa006 | -11.3491 | -45.9292 | 2026-08-18 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 193.1 |
| 9b0c23ca-f099-33c0-ab3c-adbad39c12c5 | -14.3729 | -51.8893 | 2026-08-18 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| de07d87e-24f5-329d-a7af-61bd39a3e08f | -12.7793 | -48.4205 | 2026-08-18 14:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| f0a92a34-69d1-36b8-a246-3dada80a1e58 | -9.152 | -59.6772 | 2026-08-18 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 23752629-9eb0-3921-8c3e-4629e050fec4 | -14.1631 | -52.9113 | 2026-08-18 14:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 14feb019-3077-3f44-8a6d-37b1afd3dcf2 | -13.4117 | -54.3737 | 2026-08-18 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| fdd83697-7ab0-3c38-b065-ab2693eec91b | -6.7832 | -59.4401 | 2026-08-18 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| f06b7e11-3e50-34ad-8464-fa972425f8b5 | -13.5666 | -51.7805 | 2026-08-18 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 6ba46cb3-e8ff-380f-be3f-c5388ac9581e | -11.1178 | -47.2654 | 2026-08-18 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| e529dc93-25c6-3818-85c3-deb3357cf3ae | -14.4704 | -51.8337 | 2026-08-18 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| ffa40f7c-f3cf-367a-bfd9-970a5365b9a0 | -12.5204 | -47.8804 | 2026-08-18 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 971a6840-5837-3abd-b453-ad53ca3a6e61 | -6.9884 | -59.0457 | 2026-08-18 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.9 |
| e2a1a485-380a-3907-92fa-1340615c97a9 | -6.8596 | -58.9931 | 2026-08-18 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 12d0c7a7-6bcf-372f-8a83-315691b2dce2 | -6.6384 | -58.9636 | 2026-08-18 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| fd99f97a-9340-36bc-97b0-ee7f3f679e13 | -12.5396 | -47.8777 | 2026-08-18 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 52b9305f-61af-3a7c-bbaf-56ffa5ef5d2e | -14.3529 | -51.9345 | 2026-08-18 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 828bb02b-2a17-3fa6-b243-beefb5140aac | -13.5676 | -51.7166 | 2026-08-18 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 211339c5-cdf4-3b5d-a9e9-6ab2dc3da080 | -15.3037 | -56.445 | 2026-08-18 14:40:00 | GOES-19 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 98e7f686-6cf1-37ee-a017-7cd23f377459 | -6.7123 | -58.9412 | 2026-08-18 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 3d5900ce-ffa5-3a4f-8cf3-8a2763e234b7 | -7.2007 | -43.2814 | 2026-08-18 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 120.6 |
| e5bd7859-b705-311c-aa28-a5bb023f5730 | -7.7881 | -47.8607 | 2026-08-18 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 208.3 |
| 1f08db7b-3d0a-3cba-ae9e-0a6238a5414c | -11.7351 | -54.5636 | 2026-08-18 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| f8fdec4f-ce03-39dc-88a4-2f90c6cd91aa | -8.4275 | -62.676 | 2026-08-18 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.9 |


