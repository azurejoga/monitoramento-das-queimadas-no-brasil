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
| 97d00bdb-df6b-3f58-8d31-85b9303f9663 | -22.80013 | -49.33236 | 2026-05-28 12:38:00 | TERRA_M-T | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 38.3 |
| f76e485c-33b6-3c6f-9f49-08159546e8fb | -22.79807 | -49.32712 | 2026-05-28 12:38:00 | TERRA_M-T | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 34.5 |
| a46797c3-f0ef-3506-940e-6064d128b451 | -12.7272 | -54.1988 | 2026-05-28 12:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 17101033-b296-3372-b641-5fa041558a96 | -8.854 | -46.7005 | 2026-05-28 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 9595253c-054e-3dc2-a9bb-84fca3247101 | -8.854 | -46.7005 | 2026-05-28 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 203.6 |
| b4b7b17e-931d-39f4-907f-32c43adc9e45 | -8.854 | -46.7005 | 2026-05-28 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 160.1 |
| b784090f-5f03-3e1a-9342-83c2e37851ae | -8.854 | -46.7005 | 2026-05-28 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 155.3 |
| abe16e92-47df-3c63-bba6-ca4f036133a3 | -8.854 | -46.7005 | 2026-05-28 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 156.1 |
| 04c5ac04-7485-3c95-8f93-0bf960a3f131 | -6.9982 | -42.878 | 2026-05-28 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.2 |
| dae78305-49da-3323-a072-150b92f0ed83 | -8.854 | -46.7005 | 2026-05-28 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 156.2 |
| 2f3f2973-7945-356d-b101-4d1ce586ef93 | -11.4724 | -52.9193 | 2026-05-28 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 4c0121e2-a818-3f08-a867-0a1a82fb6524 | -11.2754 | -46.9323 | 2026-05-28 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| d5ca4fcf-4556-38c9-acd6-a413e2248e00 | -8.854 | -46.7005 | 2026-05-28 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 173.2 |
| 5c0337ab-2ee2-3b61-b10a-c37b7dc2ed4f | -7.0125 | -45.0069 | 2026-05-28 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 0f0ec31b-d01e-3d41-aff5-d1026b93ff31 | -6.9982 | -42.878 | 2026-05-28 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.3 |
| 2d71680a-35a4-3ec8-963f-bd411c86e3f4 | -7.0125 | -45.0069 | 2026-05-28 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 57f94a78-5e51-3014-8c2d-d47c7ff2a92f | -11.4724 | -52.9193 | 2026-05-28 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 105.6 |
| d6d4d839-2d1d-3640-b393-d9f19c1f923a | -6.9982 | -42.878 | 2026-05-28 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.5 |
| fb7b6933-1f30-3618-8376-d6733e9347fe | -8.854 | -46.7005 | 2026-05-28 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 200.3 |
| 31dbc6b5-a46f-3310-90ce-c5a90e42b7f9 | -8.8543 | -46.6781 | 2026-05-28 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 9a63348f-6aa2-389d-bb3f-cdddc6db1c26 | -7.0125 | -45.0069 | 2026-05-28 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| e1fb59fe-c41e-332a-90a9-75656e57b64e | -7.0127 | -44.9841 | 2026-05-28 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 8bdf2be1-0d22-31ba-9ec5-7e515debb131 | -8.8543 | -46.6781 | 2026-05-28 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 8f39ef24-f3de-389e-b883-b61bc685eba7 | -6.9982 | -42.878 | 2026-05-28 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.2 |
| 70bc1afc-fb54-34d7-8a84-77ba6426fe20 | -8.854 | -46.7005 | 2026-05-28 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 258.8 |
| 84df4705-3078-357f-a8dc-378337f6b5e4 | -12.7272 | -54.1988 | 2026-05-28 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 109.4 |
| cf710d1f-3eef-39f2-bc03-86065721bbb9 | -11.4724 | -52.9193 | 2026-05-28 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 132.3 |
| 1c283bf1-8968-3de7-83eb-28053bf5de86 | -8.8543 | -46.6781 | 2026-05-28 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 742984cb-36df-3d11-82e8-c987542c7f87 | -7.0125 | -45.0069 | 2026-05-28 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| da5ee5ec-4eec-3bd9-85fb-15b2ae12441f | -8.854 | -46.7005 | 2026-05-28 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 215.4 |
| 09e90faa-2fe1-3baa-8838-8629060f47e5 | -6.9982 | -42.878 | 2026-05-28 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| 72710607-467e-3534-8c62-188448e10001 | -7.0127 | -44.9841 | 2026-05-28 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 2d92daa5-5bf0-30cf-8ffd-9a90e151bcbd | -12.7272 | -54.1988 | 2026-05-28 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 123.3 |
| ebd1aea8-c0cd-3674-85c3-d2bcae13c6ff | -12.7272 | -54.1988 | 2026-05-28 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 209.2 |
| 0cc72a4b-8a96-3ef9-a47c-267a1bc57b50 | -7.0127 | -44.9841 | 2026-05-28 14:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| b765f979-2694-35e2-935f-c7909f51305d | -7.0125 | -45.0069 | 2026-05-28 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| e93640e2-e3d4-35c8-840d-47843218d075 | -12.7275 | -54.1782 | 2026-05-28 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 561179f3-7cde-36f0-9249-36606f93e42f | -8.8543 | -46.6781 | 2026-05-28 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 5858e366-f987-30f1-8fb5-6ab57546a8a0 | -10.4862 | -48.9028 | 2026-05-28 14:20:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 2ca9cacd-6628-3be5-8f89-04c6322db479 | -11.4724 | -52.9193 | 2026-05-28 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 155.5 |
| fa7ef18b-0038-34d7-aa13-46b649c74848 | -10.737 | -49.9126 | 2026-05-28 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 86f3bd9c-f595-304b-8b5e-8c387ee971d0 | -11.4724 | -52.9193 | 2026-05-28 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 128.5 |
| b6b5c9ec-2a7f-339f-9b65-21f1df06a0c0 | -7.0125 | -45.0069 | 2026-05-28 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 8fe91b6b-b647-3c3b-becc-625a23695c21 | -7.0127 | -44.9841 | 2026-05-28 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 053ec720-5e29-3c93-b897-21862daa7f9e | -12.7275 | -54.1782 | 2026-05-28 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.2 |
| cb541d7f-0d90-395a-9b78-50111d21281b | -7.0125 | -45.0069 | 2026-05-28 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 173b7d2d-0a4f-3db4-8db8-d7069935ad1e | -7.0127 | -44.9841 | 2026-05-28 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| dcf129ba-c368-318b-b401-0539e43e75f0 | -12.7275 | -54.1782 | 2026-05-28 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 379e942e-837f-327e-99bd-d04931f1712e | -12.7272 | -54.1988 | 2026-05-28 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 177.7 |
| 18505e28-66b5-3581-8d37-18caa30fc9d6 | -11.3068 | -54.0299 | 2026-05-28 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 6ecc96c4-53f3-34b9-90e1-e8d8cb27b6a9 | -11.4724 | -52.9193 | 2026-05-28 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 127.9 |
| 40d95e93-9262-3ea5-a7b6-4fb65fcc8896 | -7.0127 | -44.9841 | 2026-05-28 14:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 03ddfab2-9cd0-31cd-b90a-b3438c6f8a9c | -6.9937 | -45.0085 | 2026-05-28 14:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 2a1e82dc-c07a-32b9-aab4-aca58287dedc | -11.3068 | -54.0299 | 2026-05-28 14:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 113.6 |
| f17e79c7-46b6-330a-a656-9e1d48aa99e3 | -7.0125 | -45.0069 | 2026-05-28 14:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| bedf89cd-6093-3194-9843-23dc234db90d | -11.4724 | -52.9193 | 2026-05-28 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 134.2 |
| a6be71f3-4024-3a5b-a7e5-0894b6557a12 | -10.4862 | -48.9028 | 2026-05-28 15:00:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 1431fd00-7147-31cf-be1f-7e7c1c11d2af | -11.3068 | -54.0299 | 2026-05-28 15:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 072935b7-c9fe-357c-92e6-d9a53988684a | -7.0127 | -44.9841 | 2026-05-28 15:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| cfdacfb2-b341-37f1-af50-35df06c9ec98 | -7.0125 | -45.0069 | 2026-05-28 15:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 0e91422b-9767-30fb-b532-407222e0d603 | -11.4724 | -52.9193 | 2026-05-28 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 138.3 |
| 5b8c2076-850e-3a42-89ba-2119beba732d | -11.4724 | -52.9193 | 2026-05-28 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 7d40680c-da52-390c-b338-b53f9b78444c | -11.3068 | -54.0299 | 2026-05-28 15:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 3daf30f8-4b2a-3d33-ba49-449a46d553f1 | -7.0125 | -45.0069 | 2026-05-28 15:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 9ee08323-48e2-3104-9652-a7de6a6e5a2e | -7.0127 | -44.9841 | 2026-05-28 15:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| b11fcffb-6657-34bf-a559-b2a0142aef8d | -10.6292 | -46.9021 | 2026-05-28 15:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 742b5584-693d-3411-9267-a2d924d8c256 | -11.3457 | -53.9442 | 2026-05-28 15:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 21011d38-4c9d-3f47-a0ae-ac2d59090436 | -11.3068 | -54.0299 | 2026-05-28 15:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 108.8 |
| c2855b84-5453-30c5-aa4c-c4a5ee44e61b | -7.0125 | -45.0069 | 2026-05-28 15:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 7a49b90a-71f2-3423-aeec-19d46568ff1d | -7.0127 | -44.9841 | 2026-05-28 15:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 9f72f2c3-daf7-35a7-9737-6f8db7883133 | -11.4724 | -52.9193 | 2026-05-28 15:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 125.4 |
| df225246-da04-31ab-979b-6a4cd3a20b97 | -7.0127 | -44.9841 | 2026-05-28 15:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 995598c6-12af-3130-b68a-ba404b716132 | -11.3268 | -53.9459 | 2026-05-28 15:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 96.5 |
| a9298564-76ea-32e7-95c3-31f5e8645763 | -7.0125 | -45.0069 | 2026-05-28 15:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 5b8c30cf-55f2-3b31-907a-38c3ad79d73a | -11.4724 | -52.9193 | 2026-05-28 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 6244fae4-cfac-34b5-b219-644150809355 | -11.4724 | -52.9193 | 2026-05-28 15:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 105.1 |
| f315a663-f222-3b19-8fb9-8ae21f191848 | -7.0127 | -44.9841 | 2026-05-28 15:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 9823bdf8-beb5-3362-b5f9-3da33c1cf4e6 | -11.3068 | -54.0299 | 2026-05-28 15:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 100.0 |
| b14d3977-95d2-3f94-b9ff-b2609edbb306 | -7.0125 | -45.0069 | 2026-05-28 15:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 9b5ab1cd-edea-3d52-b28b-26ee2e60d959 | -11.3457 | -53.9442 | 2026-05-28 15:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 107.4 |
| f6017d55-ccb9-3d0d-bf81-27ef2dbe5ed8 | -11.3268 | -53.9459 | 2026-05-28 15:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 98.2 |
| fa72bad2-995e-36cd-81c6-89f8bcf1de87 | -11.3068 | -54.0299 | 2026-05-28 15:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 16b1db1d-fd6c-3cfb-a9c5-268330765e87 | -7.0125 | -45.0069 | 2026-05-28 15:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 185d0078-4889-3e51-8656-860fe5e22715 | -11.4724 | -52.9193 | 2026-05-28 15:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 76279439-5f99-3a40-9496-c7b55d9aeddb | -11.4724 | -52.9193 | 2026-05-28 16:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 117.3 |
| ec4d00ed-c82c-33cd-9ee8-d5de855fca09 | -7.0125 | -45.0069 | 2026-05-28 16:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| b00f3035-5ad9-31dc-83d8-73506afa86a4 | -11.3068 | -54.0299 | 2026-05-28 16:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 107.2 |
| d2f62111-7ed9-3c5e-9264-adb9dd4c1a0f | -11.3268 | -53.9459 | 2026-05-28 16:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 118.1 |
| c1a6b8c3-024a-39c0-9373-4cc4d0c1c475 | -11.3457 | -53.9442 | 2026-05-28 16:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 111.9 |
| caeccaee-e294-366a-87bb-22e1f9d2c359 | -7.0125 | -45.0069 | 2026-05-28 16:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| d0195f78-bd1c-3200-a357-34f33812dc33 | -11.4724 | -52.9193 | 2026-05-28 16:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 9175c590-1a81-3ed1-be70-f11f00969078 | -11.3268 | -53.9459 | 2026-05-28 16:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 147.4 |
| 98a6f246-8562-3bd2-b02f-0a03fea82aa6 | -11.163 | -46.8124 | 2026-05-28 16:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 9a24c496-a637-3be1-b829-e977af0f2e7c | -11.4724 | -52.9193 | 2026-05-28 16:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 101.5 |
| c983317f-2b27-39b0-ac72-f24ac72d869a | -11.3457 | -53.9442 | 2026-05-28 16:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 109.9 |
| e9b46e0d-4b08-39bf-9134-04eca9085f3f | -11.3268 | -53.9459 | 2026-05-28 16:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 101.1 |
| dc2d4f2b-0fc0-3986-926d-73a36b9d7d90 | -11.3268 | -53.9459 | 2026-05-28 16:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 139.8 |
| 2db9d66d-cbac-36f0-914e-00f713dc60aa | -11.4724 | -52.9193 | 2026-05-28 16:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 117.0 |
| f3377cb6-062c-3ddf-af7a-9b2a9d9c2b91 | -11.3268 | -53.9459 | 2026-05-28 16:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 9e8b026c-814d-3dab-b7e8-3cc862f2d4de | -8.8729 | -46.6985 | 2026-05-28 16:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |


[Clique aqui para ver as próximas entradas](README17.md)
