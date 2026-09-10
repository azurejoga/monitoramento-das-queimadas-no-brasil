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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b4d128b-9490-3e21-acd1-c27047c81fdd | -6.4958 | -47.6213 | 2026-09-10 00:05:00 | METOP-B | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 55064cf8-e9a4-3b18-bf36-353e0a2fd516 | -5.7614 | -45.099499 | 2026-09-10 00:05:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bc1b44da-78aa-3ede-a75f-2464eff99946 | -2.7069 | -49.500599 | 2026-09-10 00:05:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14b1e7fe-26de-3222-862e-dda78ccb8b27 | -1.7027 | -53.684101 | 2026-09-10 00:05:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06161393-e7e0-36f0-bdbb-247b753e6ca6 | -4.8611 | -47.413101 | 2026-09-10 00:05:00 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c8eab6be-cfa9-33f5-bc2a-bb8409a36ebc | -3.2473 | -47.251202 | 2026-09-10 00:05:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8589db02-4e0c-30b8-b8fa-e523e959ecb4 | -7.5024 | -45.270199 | 2026-09-10 00:05:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 29d05171-e496-3ea8-a577-0385315bfe0e | -13.4301 | -43.828499 | 2026-09-10 00:05:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 21d78e03-fa37-3dc3-bc7a-567a671bc2e2 | -2.9358 | -50.470402 | 2026-09-10 00:05:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4636d974-a2b2-35dc-b9f4-6dd99871dcf6 | -4.367 | -47.777599 | 2026-09-10 00:05:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fda035d5-0241-3675-ae6f-9870cbbd5d9d | -2.7264 | -57.587799 | 2026-09-10 00:05:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 736e23ce-9235-38dd-80b6-54e2c441854c | -6.1579 | -44.633801 | 2026-09-10 00:05:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 07799860-5e07-3393-a253-edfe3996adb0 | -4.8595 | -47.405899 | 2026-09-10 00:05:00 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c98f71ca-8347-39f1-97ac-a03f7e67dbac | -13.5336 | -43.305099 | 2026-09-10 00:05:00 | METOP-B | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 88d356ad-ea9e-33bb-8934-b2a5db35a5fb | -7.4926 | -45.272499 | 2026-09-10 00:05:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| efcbda99-8275-3b7e-91b7-e18a330b8ca8 | -6.1677 | -44.6315 | 2026-09-10 00:05:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 62e0ecd0-a0b0-3cb8-b145-73b4f9229dd4 | -11.8568 | -44.871799 | 2026-09-10 00:05:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4e4b822d-2dce-3aec-af91-93547458d95f | -2.4783 | -49.401001 | 2026-09-10 00:05:00 | METOP-B | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8485b955-03e2-3c35-9020-b47334c1d911 | -12.6404 | -47.091301 | 2026-09-10 00:05:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7a81b6d9-7055-3600-88a4-30a68724847f | -10.0845 | -45.4618 | 2026-09-10 00:05:00 | METOP-B | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 091a936b-63b6-3262-a8ba-46f92957e255 | 1.0093 | -51.110199 | 2026-09-10 00:05:00 | METOP-B | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 68c0c5de-fc22-3815-890e-8538108e5a81 | -10.0667 | -45.473999 | 2026-09-10 00:05:00 | METOP-B | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fc931d1c-4975-3976-8cbf-2b5a3349b4e8 | -5.116 | -46.007301 | 2026-09-10 00:05:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 18f1a07a-4875-3268-8293-60027c40c825 | -6.2715 | -46.369301 | 2026-09-10 00:05:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 83093b24-ad5d-3f89-8e46-552b4f69a0a6 | -12.4182 | -49.8438 | 2026-09-10 00:05:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c23020d9-2761-3a49-bfc3-11a04d50311f | -5.6448 | -44.290401 | 2026-09-10 00:05:00 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8c0fcfc-92c2-396d-b868-16e3aaf69175 | -7.1006 | -42.132099 | 2026-09-10 00:05:00 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fe5c9e7b-323a-34aa-900f-ca70a58582de | -9.6826 | -43.4841 | 2026-09-10 00:05:00 | METOP-B | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| dc46a813-b4c9-3a35-a545-35f7d938d414 | -2.9441 | -50.461201 | 2026-09-10 00:05:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f15101f9-adec-3d4d-87cb-f059730a5827 | -6.1024 | -44.132401 | 2026-09-10 00:05:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3341a6c2-673e-3a61-80f2-1319adee9f35 | -2.9472 | -50.475201 | 2026-09-10 00:05:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb853736-00cc-33d5-adff-85763a5a673d | -4.8579 | -47.3988 | 2026-09-10 00:05:00 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3a98bf6b-7c90-3fa9-9ea5-6b33cf8029f3 | 0.262 | -51.452301 | 2026-09-10 00:05:00 | METOP-B | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| b6e12902-6318-3097-98ae-28f244ab7d2f | -7.0451 | -42.717499 | 2026-09-10 00:05:00 | METOP-B | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 71f9d07d-66ca-343c-893b-74e8f2752703 | -5.7631 | -45.0625 | 2026-09-10 00:05:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 41af6cd5-136a-3c1d-be82-f0ffb5d93e70 | -6.0904 | -44.125 | 2026-09-10 00:05:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7136f932-48a3-3e06-a952-51a539bb5591 | -12.8463 | -44.333698 | 2026-09-10 00:05:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 824de9c0-6c57-3fec-bef6-78a1eb426893 | -2.5637 | -54.734798 | 2026-09-10 00:05:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a13ed10-5054-3e3a-82ae-984f19efae94 | -7.9515 | -43.797901 | 2026-09-10 00:05:00 | METOP-B | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| df84cd58-2fcc-34fb-bcfa-e9cf2e01cb2f | -5.7569 | -45.084 | 2026-09-10 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 554.1 |
| 6f660829-4504-3b6c-8dc6-90337bd3b416 | -20.5381 | -57.459 | 2026-09-10 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.9 |
| 6a2530f0-983f-347c-8be7-46d8fac2fc56 | -2.7331 | -57.6271 | 2026-09-10 00:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 6fd56cd7-25ee-3ba1-96e2-64f84d86269f | -6.5453 | -62.8914 | 2026-09-10 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 002b884f-5790-3cfa-b866-8545b620565b | -5.7754 | -45.1053 | 2026-09-10 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 81d7069e-1f7f-3de8-b33b-67600ab5a752 | -5.7571 | -45.0613 | 2026-09-10 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 0631b4ca-a21d-3c20-9d97-777728768d65 | -8.744 | -62.379 | 2026-09-10 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 9c0a6c52-17cd-3847-9730-c2c8cbbc2bec | -6.1726 | -44.6432 | 2026-09-10 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 76b5eb3f-a28a-34c7-9f0f-170bd973fb0d | -5.7756 | -45.0826 | 2026-09-10 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 613.4 |
| c6f4b8ab-1889-3caf-a230-fdebf7d5f0c1 | -13.4453 | -43.8366 | 2026-09-10 00:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 0a7fcf9e-e0f0-358f-ab5d-9320b66130cc | -4.3587 | -47.7853 | 2026-09-10 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 31558137-d7f9-3987-ba56-cb50b3ff1008 | -7.4976 | -45.2814 | 2026-09-10 00:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 0036c5fd-f0a6-3c9f-b8d3-8bd7771949fb | -5.7567 | -45.1067 | 2026-09-10 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 62a8cfb4-48a2-3df3-a71e-488cb36088be | -5.7758 | -45.0599 | 2026-09-10 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 181e655e-6f83-3aaa-9e86-ca25e4b3f02f | -7.4979 | -45.2587 | 2026-09-10 00:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 2b22edef-988a-3074-b46c-a6226fbb568a | -5.1148 | -46.0041 | 2026-09-10 00:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 59.5 |
| ed4d0504-df8e-3ae1-be45-8b42cc1c14d4 | -12.86 | -44.45 | 2026-09-10 00:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 28d669fb-436e-36a5-95d5-7398999e95c6 | -12.89 | -44.32 | 2026-09-10 00:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 78a665f9-fc7d-3351-ae10-b9789f9591b5 | -12.87 | -44.5 | 2026-09-10 00:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 296cf1d9-4609-3388-b30f-a1d8e08d9b9b | -5.76 | -45.09 | 2026-09-10 00:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4839fcd3-458a-3c63-bc0e-6879e6c29938 | -5.79 | -45.05 | 2026-09-10 00:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 33afbbaa-e7d2-3c10-88d4-cb5f4646d624 | -5.79 | -45.1 | 2026-09-10 00:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 830ece97-d065-3dca-8af1-b5d231a35a04 | -12.83 | -44.35 | 2026-09-10 00:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ec9ff79a-0889-3908-b243-5fcd4ceaa855 | -12.83 | -44.44 | 2026-09-10 00:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b5c0914f-90f7-3489-9b77-abeb3bf041da | -12.86 | -44.36 | 2026-09-10 00:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 03d1477e-1a0b-3629-a3fd-2e29c726f0cb | -12.89 | -44.37 | 2026-09-10 00:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1cb17a09-6926-37c7-929c-3e2084d2cc8d | -12.86 | -44.31 | 2026-09-10 00:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ed78f94f-4162-3edc-a647-316a8502ebab | -12.83 | -44.3 | 2026-09-10 00:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fa014f14-4b35-3f05-93b9-3fb32e15087d | -12.83 | -44.4 | 2026-09-10 00:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0b766b43-1036-300c-bf41-ab42d2777bce | -5.76 | -45.05 | 2026-09-10 00:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a4368660-62af-3bf8-8d9f-d9ac4395a6f2 | -12.86 | -44.41 | 2026-09-10 00:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 587f0d8a-0b96-3a88-8871-9adf8fc900ab | -6.5637 | -62.8908 | 2026-09-10 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 0ba2a432-afe0-3300-ba9e-e4e1024365b0 | -4.3587 | -47.7853 | 2026-09-10 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 76c1537e-647a-3a1e-bfe9-336f1974994c | -2.7331 | -57.6271 | 2026-09-10 00:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 506d6e03-5b20-3e6d-b0e7-df0ad3dd2546 | -5.7569 | -45.084 | 2026-09-10 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 437.0 |
| 3676c630-a3a6-37da-a523-c3cb8901736c | -5.7567 | -45.1067 | 2026-09-10 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 147.3 |
| acddc730-8c40-3c30-980c-ad322b4f696e | -6.1726 | -44.6432 | 2026-09-10 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 72c5e627-296b-3ebe-baf4-89e3f1fbe68d | -5.7754 | -45.1053 | 2026-09-10 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 193.2 |
| ea97c9ab-dc3e-3658-901a-05bec9eecb05 | -13.4453 | -43.8366 | 2026-09-10 00:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 11277d52-3c40-3a91-9e3a-6801d186cc42 | -6.5453 | -62.8914 | 2026-09-10 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 212.9 |
| 847d8556-1f10-39e5-93e0-95defb6abb1f | -6.5636 | -62.9096 | 2026-09-10 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 7e4f7d63-db51-3c83-9418-2d64e2919bb6 | -5.7571 | -45.0613 | 2026-09-10 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| e8425c40-f393-3868-9e39-9a94c373cc25 | -5.7756 | -45.0826 | 2026-09-10 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 630.6 |
| 2f912a57-0a7b-305f-ac67-18eebfaa46ff | -6.5452 | -62.9102 | 2026-09-10 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 8cf1818a-86e1-3d2d-a763-456b26dbafb6 | -7.4979 | -45.2587 | 2026-09-10 00:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 6a9397ab-4254-3332-a6eb-cd4eae393665 | -4.3772 | -47.7844 | 2026-09-10 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 230e8ee6-7954-3197-bc61-0c6c80b2e807 | -2.9391 | -50.4832 | 2026-09-10 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 87e5ab55-04f7-3412-9372-98c615ece1d6 | -10.7582 | -45.9397 | 2026-09-10 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 8ed47f99-ed9a-367d-99a7-b6f4cc0f1a06 | -7.4976 | -45.2814 | 2026-09-10 00:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 2ccb7a75-bb26-37f7-9a95-5c119f9b0ed0 | -5.7758 | -45.0599 | 2026-09-10 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 06584268-81d0-386e-afb1-9cc9683107aa | -2.9111 | -54.1022 | 2026-09-10 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57762a05-6749-3b3e-b654-f98f0b0a8eaf | -10.6677 | -46.090801 | 2026-09-10 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a0ac5409-025f-32a2-bd41-ce7c21b6b9aa | -14.9039 | -44.680698 | 2026-09-10 00:28:00 | METOP-C | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0435a101-6611-36b1-ad48-a86f7e37fcf7 | -10.0755 | -45.470699 | 2026-09-10 00:28:00 | METOP-C | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5a3736f2-bd1d-34e6-9f1d-ca8fb276ad62 | -14.117 | -44.015701 | 2026-09-10 00:28:00 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 30eb0d12-fcbd-3f2b-b2a3-0be92d44bef5 | -5.1143 | -46.002899 | 2026-09-10 00:28:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f300f426-9dce-30ec-bc6c-6cb3641b2b6b | -6.1778 | -43.019501 | 2026-09-10 00:28:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a2e98daa-d8b7-37e1-aeb0-5819e04aaedf | -10.5952 | -47.111198 | 2026-09-10 00:28:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca679c12-a06b-3332-9c94-b656d2d067f2 | -10.7438 | -45.924198 | 2026-09-10 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3206e933-5a69-3e3b-a9c3-46d8bb78fd9e | -11.8547 | -44.861401 | 2026-09-10 00:28:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6863e743-6c19-345c-984d-34867cb44a80 | -9.6971 | -43.457401 | 2026-09-10 00:28:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README5.md)
