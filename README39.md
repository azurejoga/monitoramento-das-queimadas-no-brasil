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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6477cdd-ca8e-3a57-a383-1c79317a890d | -2.79433 | -50.31168 | 2025-11-05 06:26:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| e6657569-8507-3f15-8bd4-a6e07d0b410e | -4.41691 | -48.94222 | 2025-11-05 06:26:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| ca1ea8fa-219d-3442-8a3f-78735db5d1b2 | -3.06767 | -47.77391 | 2025-11-05 06:26:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6b16c184-0b0a-3d04-b76b-cb5cb9df6bb4 | -4.41506 | -48.95501 | 2025-11-05 06:26:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 1319d1cc-58fc-321a-a435-c66faf4c170b | -1.30426 | -49.1445 | 2025-11-05 06:26:00 | AQUA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| a31c40fe-6b9a-38d3-8749-17e4d31ff56f | -4.59567 | -49.54739 | 2025-11-05 06:26:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 17cec7ff-b639-3a69-8c6b-b88b46a5f023 | -3.31835 | -53.84399 | 2025-11-05 06:26:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d01803b4-d495-3283-bdb8-c9c8c4a58b05 | -6.72938 | -44.16172 | 2025-11-05 06:29:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 42.6 |
| aa4f3bad-7641-33c5-8d2b-02c782fdaed6 | -5.23935 | -48.50133 | 2025-11-05 06:29:00 | AQUA_M-M | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ef8ed4c5-8842-33db-bd1e-482ebe838502 | -8.04442 | -49.6308 | 2025-11-05 06:29:00 | AQUA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 3d3b809d-de4d-3a13-bc56-fe7f681841d4 | -8.06043 | -49.63847 | 2025-11-05 06:29:00 | AQUA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2ebc60f4-6d3f-37f9-a6e4-35a3dbaba7ec | -8.85556 | -49.87074 | 2025-11-05 06:29:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| feccd5df-c713-3ae4-aaba-6099cbb9ebb0 | -8.05164 | -49.62399 | 2025-11-05 06:29:00 | AQUA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 775f2a29-f738-321c-8f10-717699fcd115 | -6.73383 | -44.1279 | 2025-11-05 06:29:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| f11cd447-cf24-3e13-ab89-8db18c2dff4e | -8.04985 | -49.63704 | 2025-11-05 06:29:00 | AQUA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 79c7eb5c-a687-3da3-b6d9-08283badb0bb | -5.45402 | -45.39787 | 2025-11-05 06:29:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 9e00f194-ee36-377e-8175-c0d7a5fc33ce | -6.74279 | -44.13375 | 2025-11-05 06:29:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| e92caac2-1ffd-3de8-adbf-e4897a2729b9 | -8.8538 | -49.88364 | 2025-11-05 06:29:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 4673eb30-a177-3b94-a103-815f8c267f25 | -10.38126 | -47.74261 | 2025-11-05 06:29:00 | AQUA_M-M | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 3764691f-76cb-32c6-af2b-8271751990ce | -18.11219 | -53.56944 | 2025-11-05 06:31:00 | AQUA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ffb2a026-6d7a-392d-b0b0-08a381547417 | -18.50901 | -53.50047 | 2025-11-05 06:31:00 | AQUA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0b80458e-4498-37eb-b311-2db8967d5d3b | -20.09187 | -56.83297 | 2025-11-05 06:31:00 | AQUA_M-M | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0264a214-464e-3b70-830f-6e2f23aa51a0 | -1.3007 | -49.1464 | 2025-11-05 07:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| c5115b35-d24f-3d04-b7da-f2a2d42a29e1 | -1.3007 | -49.1464 | 2025-11-05 07:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| b889f688-67fc-3997-8f3e-364c8233881e | -1.3376 | -49.1459 | 2025-11-05 10:50:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 922ce939-832d-3590-a217-6b27c5207128 | -1.3006 | -49.1677 | 2025-11-05 11:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| c4dee304-70d6-3d00-9ea5-4c8a384a7442 | -5.51697 | -41.14463 | 2025-11-05 11:57:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| f23b4306-4979-3cab-bb55-b8fe8604c51e | -2.58992 | -44.67677 | 2025-11-05 11:57:00 | TERRA_M-M | ALCÂNTARA | MARANHÃO | Brasil | 2100204 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4b599f30-1a2a-35d3-bee5-7c91fc5cc268 | -3.94789 | -42.62708 | 2025-11-05 11:57:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| f4fb302e-08f1-328d-b96c-1441977eabe9 | -6.24371 | -40.63527 | 2025-11-05 11:57:00 | TERRA_M-M | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 6a11684c-547d-34a9-862f-f9402d42cfb9 | -3.51109 | -42.14256 | 2025-11-05 11:57:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 34.3 |
| a5e28f04-0618-376f-9f69-edad1af76ba7 | -2.96453 | -42.34131 | 2025-11-05 11:57:00 | TERRA_M-M | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ee5f7dc5-2c26-3f73-b580-e782bb9b21e1 | -3.37883 | -42.17126 | 2025-11-05 11:57:00 | TERRA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 8.2 |
| b78ee202-180c-39f2-8af7-9d66bb20ccb1 | -3.33145 | -44.34836 | 2025-11-05 11:57:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 73443c48-8c1d-3f0a-89b4-da016d4e095b | -3.58817 | -42.56092 | 2025-11-05 11:57:00 | TERRA_M-M | MADEIRO | PIAUÍ | Brasil | 2205854 | 22 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 89fefe9b-1efb-3f2c-9496-4ff9a8bd205b | -5.17042 | -37.92807 | 2025-11-05 11:57:00 | TERRA_M-M | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 40.7 |
| a0ad8976-4161-3343-aeb9-f139ba0ab647 | -4.58335 | -43.34293 | 2025-11-05 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 835299be-6a71-3292-9936-eab58676e6b0 | -6.16405 | -42.6209 | 2025-11-05 11:57:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 44d46179-e2b0-3eed-8ee8-7b8eef24169c | -3.70804 | -40.37614 | 2025-11-05 11:57:00 | TERRA_M-M | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 1c4fa779-ad37-32bd-8473-9d3600020df4 | -3.80241 | -39.64609 | 2025-11-05 11:57:00 | TERRA_M-M | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 13.6 |
| e52c9c6c-9d61-3f1e-b609-8ad4f1610545 | -2.59144 | -44.66634 | 2025-11-05 11:57:00 | TERRA_M-M | ALCÂNTARA | MARANHÃO | Brasil | 2100204 | 21 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 3839a59b-3a36-3724-930a-6dac951a1909 | -2.58188 | -44.66499 | 2025-11-05 11:57:00 | TERRA_M-M | ALCÂNTARA | MARANHÃO | Brasil | 2100204 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 25d5cfcd-797d-332f-8932-f5ecb490f5c6 | -6.97611 | -38.07742 | 2025-11-05 11:57:00 | TERRA_M-M | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 28.6 |
| 0cb2f8df-94b4-3963-ad32-4e624b682f8f | -3.3837 | -42.69902 | 2025-11-05 11:57:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3ad68f4c-3944-3605-9c04-24c251f2a5a6 | -3.51598 | -43.00035 | 2025-11-05 11:57:00 | TERRA_M-M | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 695c0602-e2ee-3744-bd9e-9d18eaec2065 | -6.10995 | -41.64587 | 2025-11-05 11:57:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 22.1 |
| da983018-4f9f-302b-a323-f6ae979fa0d5 | -3.47974 | -43.63735 | 2025-11-05 11:57:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a79c24c4-9e88-369c-974a-b89fff7dbf2c | -2.95573 | -42.34009 | 2025-11-05 11:57:00 | TERRA_M-M | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 95bddf75-d9f6-34e1-a6f0-0bebbca99761 | -3.51726 | -42.99148 | 2025-11-05 11:57:00 | TERRA_M-M | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| c9af50a9-4611-370c-8707-cec0b0b7bc7a | -3.58946 | -42.4271 | 2025-11-05 11:57:00 | TERRA_M-M | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 938d51c4-5bf6-3a39-9660-f76ab56360b4 | -3.50983 | -42.15131 | 2025-11-05 11:57:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| c212b88a-4c65-318c-9f88-583ee3f3f28e | -3.72499 | -44.98323 | 2025-11-05 11:57:00 | TERRA_M-M | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 804bf34a-cf28-3316-b306-a76f793fe95a | -6.27538 | -42.56807 | 2025-11-05 11:57:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 2cb10b1f-d9f7-3e36-8221-44c6c14bd92f | -3.52746 | -43.62525 | 2025-11-05 11:57:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| fafbf355-f7d6-39d5-9bf8-f41ebf165c59 | -2.95699 | -42.33134 | 2025-11-05 11:57:00 | TERRA_M-M | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6a5dca40-9d76-393e-b54c-bf27a42eaacd | -5.90509 | -43.27842 | 2025-11-05 11:57:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a3efcd9e-9972-3454-96c8-1a6497f89097 | -3.41781 | -44.43386 | 2025-11-05 11:57:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 86ccb168-bfaf-36fa-8e30-89001c4bf3e5 | -2.90252 | -44.17253 | 2025-11-05 11:57:00 | TERRA_M-M | ROSÁRIO | MARANHÃO | Brasil | 2109601 | 21 | 33 | nan | nan | nan | Amazônia | 17.5 |
| d3542668-a3f6-34d5-a728-3c8d3879076c | -4.33085 | -40.13139 | 2025-11-05 11:57:00 | TERRA_M-M | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| dfe0301a-6860-3f48-ae71-0c97cedd7ae6 | -5.24184 | -38.93554 | 2025-11-05 11:57:00 | TERRA_M-M | BANABUIÚ | CEARÁ | Brasil | 2301851 | 23 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 36fa3897-2a0e-3164-a54d-2614af1f4be1 | -3.33003 | -44.35821 | 2025-11-05 11:57:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| fe7ebd83-df3c-391c-9b8e-e2f529403c6a | -2.601 | -44.66768 | 2025-11-05 11:57:00 | TERRA_M-M | ALCÂNTARA | MARANHÃO | Brasil | 2100204 | 21 | 33 | nan | nan | nan | Amazônia | 33.1 |
| ce65551c-8c08-3e84-ae3a-9a47a28a21cf | -3.52613 | -43.63449 | 2025-11-05 11:57:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| c250a43e-53f4-3edb-adb0-69a228d53d67 | -5.73746 | -43.02015 | 2025-11-05 11:57:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 782cd097-6a27-38d7-a02d-fcb7ba0b1aed | -4.57447 | -43.34169 | 2025-11-05 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ba8e5d75-eced-3f97-87a1-effefe89d07a | -3.128 | -44.48028 | 2025-11-05 11:57:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 14.1 |
| b9a640e5-c078-31a6-a327-654206d5a232 | -3.5882 | -42.43585 | 2025-11-05 11:57:00 | TERRA_M-M | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 38.6 |
| d52742d8-2f96-39ba-b1b4-7972e18f1b41 | -3.33703 | -44.35574 | 2025-11-05 11:57:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| fc6e0866-b550-3f90-a515-164739530d98 | -3.40738 | -41.38753 | 2025-11-05 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| c4002a0a-2bc2-3af5-979a-600c0ab19b9f | -4.57576 | -43.33277 | 2025-11-05 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e76ad070-82c7-3701-8401-081218acfded | -1.19154 | -49.19093 | 2025-11-05 11:57:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 36a3d1c7-c101-3dfa-8a78-deac7f11bdbd | -5.17064 | -37.93451 | 2025-11-05 11:57:00 | TERRA_M-M | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 935daa69-3ddf-376c-98de-e08ca3f9ef2d | -3.13432 | -44.47734 | 2025-11-05 11:57:00 | TERRA_M-M | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 96520c1a-bf66-3cf8-ae63-922fcec86c87 | -6.46931 | -39.16655 | 2025-11-05 11:57:00 | TERRA_M-M | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 40.3 |
| 4a69c0f8-d9ca-3698-8b9e-9d69a1c6236b | -3.4933 | -41.6228 | 2025-11-05 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 20.0 |
| f7dcf32f-2217-34c5-bf2c-ef45403506b8 | -3.80391 | -39.63552 | 2025-11-05 11:57:00 | TERRA_M-M | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| b791b2f5-9edb-37fa-8c5d-83e3c830bc5a | -3.58943 | -42.55216 | 2025-11-05 11:57:00 | TERRA_M-M | MADEIRO | PIAUÍ | Brasil | 2205854 | 22 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 0a37b471-6e46-3cff-977f-1c19a128db91 | -3.96612 | -43.78395 | 2025-11-05 11:57:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3cd20b75-988f-3898-89b2-d48a202710a8 | -4.61835 | -39.30917 | 2025-11-05 11:57:00 | TERRA_M-M | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| ccb93b9e-c916-3cd2-95e8-89e0d6f23546 | -3.41089 | -44.43699 | 2025-11-05 11:57:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| e7a290bb-a756-3b0f-883c-bb6e74f868b8 | -5.51565 | -41.15397 | 2025-11-05 11:57:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| c8bd880c-f2fb-3786-b0f8-0e9a7e778866 | -3.06304 | -42.36102 | 2025-11-05 11:57:00 | TERRA_M-M | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| cb303dc2-49b2-31a4-8f7f-e6df6496c541 | -3.66011 | -44.79754 | 2025-11-05 11:57:00 | TERRA_M-M | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 18.3 |
| f388d8cc-737a-33f5-a1e6-e718191b4720 | -3.40864 | -41.37871 | 2025-11-05 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 85790535-3c19-3ec4-afea-ce90e5ea6b10 | -6.84166 | -38.57549 | 2025-11-05 11:57:00 | TERRA_M-M | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 02ca1bda-65c2-3612-a1cc-dffce01f4fdf | -4.47106 | -43.23016 | 2025-11-05 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 77c8aeee-3601-36ac-864d-8d42fb0595b5 | -6.97473 | -38.08368 | 2025-11-05 11:57:00 | TERRA_M-M | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 28.0 |
| b1ca63cb-627b-31f9-ab9d-df65fc94580f | -4.58463 | -43.33401 | 2025-11-05 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 9d48c1ad-3a57-3fea-b66e-fc736b393f24 | -4.30376 | -42.92336 | 2025-11-05 11:57:00 | TERRA_M-M | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 78be3637-ff7d-370d-ade2-4569d7ec1f6a | -3.38009 | -42.16251 | 2025-11-05 11:57:00 | TERRA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 23.5 |
| b9584818-724d-3658-95b4-48b9c399b328 | -3.68903 | -42.50098 | 2025-11-05 11:57:00 | TERRA_M-M | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| dd91ac9e-20f2-3498-a2d1-09558b281ca7 | -3.52295 | -39.31424 | 2025-11-05 11:57:00 | TERRA_M-M | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 16.1 |
| e4e3684f-0cce-3ee8-a39e-1809c1163e08 | -7.17386 | -42.738 | 2025-11-05 11:59:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 22.4 |
| 50159f4e-831f-38b9-9302-5c2714f5a906 | -11.41386 | -42.54945 | 2025-11-05 11:59:00 | TERRA_M-M | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| dc2a8f5f-c6d8-38c5-ace0-db2cd1cea5ea | -15.57701 | -43.42494 | 2025-11-05 11:59:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 587b0896-d187-3143-aed4-6bcaafe5a742 | -11.84867 | -43.72386 | 2025-11-05 11:59:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 2ef68a21-514e-35d1-8f25-0ea0b88b27a5 | -11.85837 | -44.60893 | 2025-11-05 11:59:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| cf630b03-5a5d-3808-bcfb-3ac1b4e8d30f | -8.04839 | -46.64936 | 2025-11-05 11:59:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| bac57a0a-d9b6-3941-8e04-ac83f8847480 | -15.57832 | -43.41535 | 2025-11-05 11:59:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| dca45036-0aa7-3983-9c81-0b3697e1a64b | -12.52783 | -42.95659 | 2025-11-05 11:59:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 20.5 |


[Clique aqui para ver as próximas entradas](README40.md)
