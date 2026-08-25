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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2080e828-6d77-3eb0-98ee-c4e5e57eca0e | -10.07579 | -46.37496 | 2026-08-25 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee42dea6-f62b-3876-8d59-4fb4a4234ed2 | -7.19537 | -42.76493 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 24c1054a-e380-36e5-b7b5-0bc291654de8 | -4.47371 | -54.80919 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bf167840-9bcb-31d9-a848-e443793aeff8 | -7.74248 | -46.15648 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b95a3adf-50d3-3c37-a645-2e6ede403c09 | -7.14273 | -42.76075 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 22838ef9-743b-3b72-9837-4ba075284c96 | -6.60441 | -58.38787 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 091b2d12-2ec0-3767-90db-a85ac38d75bd | -6.17705 | -55.43968 | 2026-08-25 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4266ed41-4caf-3c2f-8d6f-d260696f2150 | -9.20625 | -50.10275 | 2026-08-25 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84b3cdff-dd3a-3d92-ba43-aaa2528c2d96 | -6.53764 | -55.09287 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d68d3ca-9b4a-3f10-bc69-5c24ef2dfc6e | -5.94391 | -57.73232 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ca724e5-a69c-3d61-b33a-6a4a8cd5b2cd | -6.33266 | -54.75526 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 919c5944-3e6a-3b8e-b4c3-fe025e5c0199 | -6.32911 | -54.76518 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05d37c69-2d98-3dd8-86e5-f9228447a624 | -5.86019 | -50.14278 | 2026-08-25 04:25:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8cfa8c4-bba4-357f-b46b-537aad6266bf | -5.95501 | -53.60381 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5674a1f6-f25f-3c65-a12b-0a8b8ec051b8 | -5.52706 | -46.60679 | 2026-08-25 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a92e5e8-eb4f-33a8-b28d-4d07f93d1a1a | -9.60737 | -35.9018 | 2026-08-25 04:25:00 | NOAA-20 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 82421b54-283f-3435-b2f6-e0be5f33ef21 | -7.24672 | -45.8566 | 2026-08-25 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb990a10-84e6-305c-8f57-563f6ab4bb1b | -5.92627 | -49.67788 | 2026-08-25 04:25:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29a10b5c-d226-33ce-9b36-e6b393625d49 | -6.29569 | -43.79456 | 2026-08-25 04:25:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8e9f0ca-b601-3666-a853-d73dd1b54ac9 | -5.29528 | -42.70924 | 2026-08-25 04:25:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3de5cd24-aba1-3020-9e8d-d3a6e18dedfc | -8.61698 | -47.15158 | 2026-08-25 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d9444fd7-9409-362f-89f0-bee8fc18548a | -7.38275 | -55.1829 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0854d17b-f062-3fc6-b06f-cbffbace83ed | -6.83153 | -52.51124 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a6d83728-2c25-37ba-a589-4cba30b9dd05 | -7.43144 | -43.11711 | 2026-08-25 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4e9d1734-2a15-373b-b0a1-c8c534466805 | -6.33895 | -54.77446 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48410995-464d-3194-8287-afe8e15c1218 | -11.14068 | -44.47704 | 2026-08-25 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 32.8 |
| ca2d0605-9310-302e-a3bb-32e9398e9dd1 | -11.13392 | -44.47598 | 2026-08-25 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 45d12b0e-7422-3fd6-8d08-0bc3ad277edf | -7.44116 | -43.12244 | 2026-08-25 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ce4539e3-2919-39f6-95b4-6a3e52ad4cec | -10.57188 | -46.31155 | 2026-08-25 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83e3584b-f2b0-3b84-b034-e341c76e3214 | -6.84272 | -52.50298 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d3238e20-a77b-3411-ada1-9fc0520319e3 | -7.27912 | -44.08137 | 2026-08-25 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7206a780-aaf6-3c0c-93c7-fd0cfcb4f067 | -7.06106 | -42.93143 | 2026-08-25 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 873a457b-bc65-394c-b150-d833ef8abfd7 | -7.15716 | -42.78257 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 902d1c87-7b75-3736-bd74-082984cf4753 | -5.92683 | -49.67459 | 2026-08-25 04:25:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ec24037-b52c-31e5-864f-636b544a4384 | -6.81907 | -58.65172 | 2026-08-25 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 699ffd3e-0d6a-377b-9fb4-29adb40fcb28 | -9.57404 | -49.23212 | 2026-08-25 04:25:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e29b428d-242e-3324-85bb-14369923f905 | -11.13786 | -44.47286 | 2026-08-25 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 18a4236c-91c0-3238-a811-ce6ec4f6890d | -5.83792 | -50.08241 | 2026-08-25 04:25:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce4eb0fc-c48f-385a-ae33-864b77617961 | -6.32978 | -54.76152 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a8d5aec-e712-30e7-9399-606922fb5a71 | -7.26225 | -45.84473 | 2026-08-25 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 49976a42-bfe4-3c12-a84d-af088aa13a79 | -6.70201 | -56.3514 | 2026-08-25 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e029b8a6-ebe6-3f24-bc07-9e6f2b6c5ce7 | -7.25781 | -45.85121 | 2026-08-25 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1a3114cc-8c4d-3828-86a5-e5006cadb0df | -6.18694 | -53.4803 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33b2d55a-3653-32ec-a63a-ef55cc6c0d81 | -9.05186 | -50.79647 | 2026-08-25 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f7745921-70ea-305d-bbd6-64b7145e8da3 | -5.51666 | -46.62791 | 2026-08-25 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 75ce5417-8d45-347e-af20-872aae902588 | -7.38086 | -45.99306 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e340211f-b97c-34fb-a956-e1b735c3f50c | -6.55682 | -56.55305 | 2026-08-25 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad77963f-ec20-3482-ad43-00cc937d7d97 | -5.78745 | -57.6106 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 54bb9638-5feb-3765-a9b8-a8182f5b7473 | -6.33566 | -54.77106 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8b10dd9-c89f-387a-a861-fdade965cc21 | -8.1148 | -47.47921 | 2026-08-25 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3140217f-6019-35dd-a699-86469fedc1b5 | -7.89922 | -46.38501 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df5c9027-4500-3f48-b6de-026e140e2e92 | -9.97051 | -48.32668 | 2026-08-25 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e67d6d4a-7d8f-31dc-9fbd-9ec7f4b535a7 | -6.18297 | -53.53368 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b5622c9-25fe-33fc-b3b7-bacb1db03fb8 | -5.39412 | -43.60763 | 2026-08-25 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 609bc849-ad2d-3a36-bb52-4847a2c42c45 | -7.2639 | -45.85579 | 2026-08-25 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3f16d2db-9dd6-363f-b0f2-49fa6aaeb5ac | -7.29322 | -43.0164 | 2026-08-25 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f09a6b8e-d31e-3a6b-b11b-38299ea74013 | -6.7016 | -56.35068 | 2026-08-25 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7ae5273-9518-3ba5-8851-019018947722 | -5.67166 | -44.41508 | 2026-08-25 04:25:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2567d5dc-8db7-36b2-a282-4b576bfd048d | -6.91108 | -44.654 | 2026-08-25 04:25:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7149e5c-5084-3ea7-8acf-9caaf02c424f | -7.28022 | -44.07431 | 2026-08-25 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5540da0e-420e-3a37-82f0-fd65e3f08838 | -6.17133 | -43.76437 | 2026-08-25 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05c6dc38-855c-3fb4-b50f-2487a2113403 | -6.44081 | -54.96816 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 261aaf84-d732-3167-82ff-0151d60bdd5f | -6.18534 | -53.48949 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d6a536d-b666-3d18-85b7-176659764f86 | -8.6172 | -49.99236 | 2026-08-25 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9aa6a528-1b5f-34fe-b72e-cbdd1043d09a | -6.33113 | -54.75407 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25abece3-3139-3ce2-941f-5d2034d087c9 | -8.59626 | -54.73204 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35caac04-10b4-3294-a1f8-f1c43ee32040 | -10.71388 | -47.75949 | 2026-08-25 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea1b767c-a129-3c5c-9b5e-92856dc41188 | -5.78885 | -57.61733 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 78edcba0-43b4-3cb0-91cf-c482747b2054 | -7.48008 | -44.46915 | 2026-08-25 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d41b3624-37a3-3216-b353-819a8ef26351 | -8.09318 | -47.5032 | 2026-08-25 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e881a59d-b9fe-35cd-9264-0f99a8b6c58b | -7.7052 | -46.15419 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d74f0661-6037-31dd-b585-8ab32007e720 | -4.9516 | -42.98407 | 2026-08-25 04:25:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 427793a2-b50c-33fb-8011-fa07af496d4e | -9.94609 | -48.34304 | 2026-08-25 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8db7804a-3987-3d0d-90d8-70e9d8b51590 | -6.33952 | -54.74884 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71d375f0-742b-3e2d-ae4f-80d315f852b6 | -6.93899 | -52.79805 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20ebaf98-61e5-3f90-823b-3a55c4776a4e | -8.15792 | -46.69538 | 2026-08-25 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2eca2a4-23f3-398c-9e01-d8105f6fdd70 | -7.15143 | -42.75022 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 34a232d4-6ab6-3b6b-9914-5a0ccdc976cc | -3.53057 | -48.17803 | 2026-08-25 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| e3bc6ae9-2be8-32cb-98c2-64ad38f5d2b3 | -4.12325 | -49.45072 | 2026-08-25 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8552f218-8f17-351a-b768-61a43746c86f | -8.11717 | -47.47929 | 2026-08-25 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06dbad20-3824-34f5-ad1f-4c6ab1334db9 | -6.34385 | -54.7792 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2d6906b-5f75-36b7-8d92-bc8f8d0ce11f | -9.59789 | -49.11469 | 2026-08-25 04:25:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3cf8b71-5c17-3517-82d1-9b9435832756 | -6.12702 | -57.82127 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b17d0d48-bfd5-39a0-a7c9-34e0a722fb41 | -6.63881 | -58.50497 | 2026-08-25 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| ad92b612-2b4d-316b-89b1-71c8499e7424 | -7.26916 | -49.91724 | 2026-08-25 04:25:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e7733d27-bdc7-30d3-aa58-96e107287328 | -7.96974 | -43.91886 | 2026-08-25 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 016282d8-8891-31f9-9d0a-a7079feb31f8 | -7.2521 | -45.37537 | 2026-08-25 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e7837791-17ad-3c9c-a88a-6e501bdd3c99 | -7.28136 | -45.3623 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28ce2e5a-c47a-36fa-993c-da1c1d8f2740 | -3.54261 | -48.17521 | 2026-08-25 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| cd3839e1-0232-3975-8870-d12f5544f228 | -7.35403 | -55.66786 | 2026-08-25 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 09a9ba03-0344-3714-a90b-7c50c6d38135 | -7.28797 | -45.36335 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9eb21a37-c914-3896-b3fa-f3cbe7789119 | -7.28191 | -45.35883 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 8e61ef41-f3dc-31bd-8725-6dd42419e05c | -8.171 | -54.96791 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b6fc8a59-3ba7-3ebb-9f11-4594cf412836 | -7.45203 | -43.12033 | 2026-08-25 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 30ce28c2-0f19-3be7-9e2f-701e66eebc0e | -8.06941 | -44.65169 | 2026-08-25 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5ac95e3a-e67d-36da-8ee7-51c3326b5fc1 | -8.57038 | -54.86005 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23806fac-afcd-3414-ac4b-10dac9f15e79 | -8.21303 | -54.98661 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06584260-35e3-3639-8fc0-1e7428bd3236 | -7.89713 | -46.35537 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f04ce3e9-a1a3-3692-8afc-3e017424932c | -7.1462 | -42.76127 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9a952dbc-243f-3328-ac69-fafa08a586d7 | -6.34017 | -54.74513 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README30.md)
