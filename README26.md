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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb9d8488-c2a3-3fee-b745-d8408856cea1 | -11.6584 | -44.6207 | 2025-06-18 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| ce1312e2-1d02-31dd-aae5-36616a95af4c | -4.8377 | -43.1685 | 2025-06-18 13:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 483b003e-0ba6-3ae5-a648-b4365732028e | -5.9216 | -43.4403 | 2025-06-18 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 9a2a3b08-086d-31fa-ae8f-252e03debc85 | -19.0711 | -53.4599 | 2025-06-18 13:50:00 | GOES-19 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 74.1 |
| b1d8957a-6070-3f9e-90b6-e98e61f775c8 | -11.658 | -44.644 | 2025-06-18 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 2c37556e-8526-3d70-b31d-c661450a37e2 | -6.6938 | -43.1882 | 2025-06-18 13:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 93.8 |
| 030d2744-be0d-32c4-954f-e191031dd808 | -6.675 | -43.1899 | 2025-06-18 13:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 89.4 |
| eb7a7a74-b89a-3595-b5af-6c4d030526a8 | -6.675 | -43.1899 | 2025-06-18 14:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 86.8 |
| 0df97486-a11d-341f-a5ef-903efe1d5ca0 | -10.8571 | -53.7631 | 2025-06-18 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 101.8 |
| ea5d9116-d0ac-38d0-8263-bbaa0510c635 | -5.9216 | -43.4403 | 2025-06-18 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| de8049ec-2e2c-341e-bf54-091a53127acc | -9.4994 | -56.0788 | 2025-06-18 14:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 334ab4be-84ea-3b08-ba17-38a2bcd070e6 | -5.7713 | -43.4752 | 2025-06-18 14:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| a4a3dde9-85eb-33af-9342-ed73aa81e98a | -11.1382 | -53.9223 | 2025-06-18 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 3d65218b-1e80-316f-9b95-a356fe012d04 | -6.6938 | -43.1882 | 2025-06-18 14:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 90.5 |
| 68a195de-dc9e-3ed3-af3c-5d7b92365c67 | -11.658 | -44.644 | 2025-06-18 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 126.4 |
| e37db779-bf4c-3062-881e-27396e90561b | -19.0711 | -53.4599 | 2025-06-18 14:00:00 | GOES-19 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 462d1682-4d87-3aaf-84c1-ca608c1d3a17 | -11.6458 | -54.1418 | 2025-06-18 14:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 0639fb48-b691-30cf-943a-0559fb9df476 | -11.1379 | -53.9429 | 2025-06-18 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 76a6582d-2668-39f1-9f1f-88852418c06c | -11.6584 | -44.6207 | 2025-06-18 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 58703987-142e-369e-b212-fcfc0fba4b5c | -9.4993 | -56.0988 | 2025-06-18 14:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 8458c8d3-4d13-327a-b50d-2fd07d65836f | -11.658 | -44.644 | 2025-06-18 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 904bf9ec-264d-3fb2-93c1-febca9f2fc01 | -6.675 | -43.1899 | 2025-06-18 14:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 82.7 |
| d27175ae-318d-3d39-a1de-72ded4f38e07 | -11.1382 | -53.9223 | 2025-06-18 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| e3c8227c-0e6f-36fb-9c57-8b9762b7a300 | -6.6938 | -43.1882 | 2025-06-18 14:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 94.7 |
| a917b21b-2a04-3133-bfb9-7c1b1a66fb65 | -9.4994 | -56.0788 | 2025-06-18 14:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 0fe2b17b-54f1-321c-9ddd-4902c1a9c060 | -10.8571 | -53.7631 | 2025-06-18 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| c020300a-3886-3395-8dd6-0d6aecf34d04 | -19.0711 | -53.4599 | 2025-06-18 14:10:00 | GOES-19 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 66.8 |
| a2ac6e80-1592-3012-a36e-f36009eab417 | -11.1379 | -53.9429 | 2025-06-18 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 4521bcd4-0ff5-3c68-bfee-099774e8be12 | -11.6584 | -44.6207 | 2025-06-18 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| ca05ad00-7299-37d0-801b-7c77cafefb4c | -9.4993 | -56.0988 | 2025-06-18 14:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 510c9b84-8ed5-3ea0-b94a-e3670904816f | -5.9026 | -43.4651 | 2025-06-18 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 9c8fbfff-d130-35aa-96d6-5a346ccfe478 | -11.6458 | -54.1418 | 2025-06-18 14:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 7f548ffa-d22e-3a04-8f6f-51f564c0aa51 | -9.4806 | -56.1001 | 2025-06-18 14:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| a15fddda-a7c8-3d17-9a4d-e8b9f8cd57ca | -11.658 | -44.644 | 2025-06-18 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 5ceb5815-4daa-3c3a-8f21-c0db32bf7558 | -9.4993 | -56.0988 | 2025-06-18 14:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 108.8 |
| b2c94df1-4758-3788-a757-c334dc9f98a0 | -10.8571 | -53.7631 | 2025-06-18 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 37e16d2a-ac5c-30b6-84a6-a4a4ccd680d9 | -21.5262 | -47.8271 | 2025-06-18 14:20:00 | GOES-19 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 239.7 |
| a57085c2-5e32-3a13-b362-4df70bb3e0ef | -9.4994 | -56.0788 | 2025-06-18 14:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 477346a3-5632-39c0-bb03-c48628e6f4b1 | -11.6584 | -44.6207 | 2025-06-18 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 106.9 |
| dc0af4aa-5058-33ba-bc0c-1f58571ff5b7 | -21.5269 | -47.8034 | 2025-06-18 14:20:00 | GOES-19 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 125.3 |
| bac4313d-9f81-359b-a3a4-54d8dbf31a15 | -11.6458 | -54.1418 | 2025-06-18 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 94.0 |
| fcbd23d1-527e-3b60-b2cf-0dee5e6c3385 | -11.1379 | -53.9429 | 2025-06-18 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 496ae2d1-be72-33b7-b6da-7c13e78518fb | -10.8571 | -53.7631 | 2025-06-18 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 395ca159-ae2f-38d7-9afd-9975c773eb0c | -11.6584 | -44.6207 | 2025-06-18 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| fa265b53-43f8-3034-b52c-ffc766341e60 | -21.5269 | -47.8034 | 2025-06-18 14:30:00 | GOES-19 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 44eaa166-7779-3e65-a573-f08255ad129c | -9.4994 | -56.0788 | 2025-06-18 14:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 104946b6-b519-3f5d-81f3-ce3cfa313d29 | -9.4806 | -56.1001 | 2025-06-18 14:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 0e159e71-a8c6-37a8-ad74-ef7a1db4d29e | -9.4807 | -56.0801 | 2025-06-18 14:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| dd54c4ed-5a62-3e3f-a7c1-f7ffecf8a987 | -9.4993 | -56.0988 | 2025-06-18 14:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 28b21d95-9d37-3360-ad2e-1c8fc2f723c8 | -21.5262 | -47.8271 | 2025-06-18 14:30:00 | GOES-19 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 144.6 |
| ff2cae14-c8c1-3d64-a219-939791061610 | -11.658 | -44.644 | 2025-06-18 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| cd0f38f6-9b8b-3d6b-a047-bfc39bb00eb7 | -9.4993 | -56.0988 | 2025-06-18 14:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 144.0 |
| 163cb172-f75a-35e6-a701-71173495909f | -9.4994 | -56.0788 | 2025-06-18 14:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 118.1 |
| ab1bfdeb-3292-3c19-af74-942f9216ce1c | -10.8571 | -53.7631 | 2025-06-18 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 539d8826-b2c7-3b48-a95a-aaac20ed1094 | -14.0328 | -55.13 | 2025-06-18 14:40:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 13feaee0-af99-3438-a23d-c00effd6222a | -21.5262 | -47.8271 | 2025-06-18 14:40:00 | GOES-19 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 95.9 |


