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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be558aa1-cc99-3e1d-9ed9-c477f880924f | -6.1544 | -53.6874 | 2026-08-24 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 135.2 |
| c428f226-80e6-34d2-a9a7-819204270c3b | -9.6774 | -55.1022 | 2026-08-24 14:40:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 0abff53f-4f26-3f47-9d5d-daefa467dbe7 | -6.8491 | -52.505 | 2026-08-24 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| f3bc3c1f-7e80-3196-bb52-9585154e467d | -6.3692 | -54.7455 | 2026-08-24 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| d6befc41-c6ff-3246-bd53-7bd0b9a4793c | -12.0753 | -50.5759 | 2026-08-24 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 4b863555-da16-3e55-848e-8df8dd4e8975 | -14.7787 | -48.7882 | 2026-08-24 14:40:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 60.7 |
| a399630d-998e-3f69-9be7-33198c74e658 | -9.0627 | -45.1893 | 2026-08-24 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.9 |
| b620677c-a87e-34be-90b9-5a253858809d | -11.4201 | -45.1181 | 2026-08-24 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 95bcf830-9744-31a5-96d6-a27b835cc71a | -13.8954 | -54.0508 | 2026-08-24 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 73085524-5944-3150-99de-a67e4904254b | -10.7985 | -50.9518 | 2026-08-24 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 151.5 |
| e30015b0-d87f-3773-b128-31f4e4eb95bd | -10.785 | -50.5493 | 2026-08-24 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 107.9 |
| c3d39499-080d-3e97-a6da-3c76b89e5c3a | -15.2648 | -52.8747 | 2026-08-24 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 3799bf13-cb6b-33b5-aa5d-718f386beec6 | -10.8174 | -50.9498 | 2026-08-24 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 27736247-c995-332d-8f61-687098667948 | -14.2402 | -51.7576 | 2026-08-24 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| f1b3c0fb-5fc2-343e-95ce-2e0e97842c0f | -6.1542 | -53.7077 | 2026-08-24 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 166.9 |
| 93f146e4-89a0-386b-9269-5849385d593c | -7.2979 | -43.0137 | 2026-08-24 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 140.1 |
| d5de24e1-199c-3b07-aec9-3002bedd45a8 | -9.0311 | -50.7183 | 2026-08-24 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 173.0 |
| 98383806-996b-3d32-8774-ec4a6c00d5a1 | -6.1727 | -53.7067 | 2026-08-24 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| cec965c7-22c7-3506-a7fb-b5e17864bd6a | -9.7317 | -46.0433 | 2026-08-24 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 9c5f1c94-e618-3dac-8cc3-140bced7924a | -14.2595 | -51.7551 | 2026-08-24 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 5e382127-38b1-3425-8dbd-3678411e1c46 | -14.3558 | -52.9083 | 2026-08-24 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 86.2 |
| df4d123c-aff2-3096-bd0d-1319a6d4bfb2 | -10.804 | -50.5473 | 2026-08-24 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| a20c97c8-341f-3d92-a067-8568001d1d6e | -9.7131 | -46.0229 | 2026-08-24 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 38b44357-a564-3c03-93f6-584eb4c72dc3 | -6.6048 | -58.3838 | 2026-08-24 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 2352f81f-94ae-3867-ac1e-21b77bb06d2e | -6.8202 | -59.4194 | 2026-08-24 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| dffe7673-f78b-3ee6-9c8b-0819c2a22e95 | -7.2193 | -60.6316 | 2026-08-24 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| e1e64ca1-3817-30b5-9540-0cb7b5e874a4 | -7.2713 | -45.37 | 2026-08-24 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 3685fbea-04ab-3a5b-9066-cf8df36002a7 | -13.1512 | -51.3854 | 2026-08-24 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 104.7 |
| fdd6f0a4-8afa-3b0d-a858-ecb3dc973b66 | -9.6776 | -55.082 | 2026-08-24 14:40:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| a4d5ee72-b7a8-343d-b3de-948b5cd75117 | -7.2901 | -45.3683 | 2026-08-24 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 237.1 |
| ef8b55d9-f96d-3c83-b5d1-7224c0daed18 | -14.2591 | -51.7764 | 2026-08-24 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 105.9 |
| dfcff6ef-2754-3c11-bfd8-bec49a3c8b33 | -10.4463 | -50.4353 | 2026-08-24 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| beb89ed7-e854-32f4-9999-967360740b14 | -12.1132 | -50.5929 | 2026-08-24 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 128.7 |
| a77ad27d-95a7-38f0-9f4b-786a851049d8 | -14.3933 | -52.9667 | 2026-08-24 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| e2982792-c8f0-33d8-b174-5d39058e0845 | -15.4972 | -52.9069 | 2026-08-24 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| f86b5393-dcd9-3cff-a94f-193a992ff898 | -6.3507 | -54.7464 | 2026-08-24 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 422.8 |
| f69c8103-a91e-3ddf-bc83-4f8941ac77af | -12.1128 | -50.6143 | 2026-08-24 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| a28259c8-ccfb-3a3b-a3bb-ece43c0897c2 | -10.7988 | -50.9305 | 2026-08-24 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 108.5 |
| a64e3fa5-a3d9-3e24-9ddc-692d85c152fb | -6.8305 | -52.5061 | 2026-08-24 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 125.9 |
| a326c39f-a35e-3059-9ecb-5eafe3bb60a9 | -6.7832 | -59.4401 | 2026-08-24 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| c8d6a404-b086-3505-a67a-4d720049e62d | -6.5596 | -45.2947 | 2026-08-24 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| f593bd9f-805d-3467-81a4-6e9f670a5356 | -15.2854 | -52.8084 | 2026-08-24 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 64086d60-246b-3763-a535-101a1b0efc20 | -14.3937 | -52.9456 | 2026-08-24 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 677d7b50-91ba-3bdf-8d31-a8b414b7a440 | -15.5522 | -53.09 | 2026-08-24 14:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 534017ff-adb7-35c0-b183-06072fd8fdab | -8.3247 | -46.8866 | 2026-08-24 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| c0ae38a9-80ad-34d1-a4af-067c40b8b28f | -12.1319 | -50.6121 | 2026-08-24 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 7fb98c50-063c-3352-ab34-3ec6077d2b74 | -6.332 | -54.7674 | 2026-08-24 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 245.6 |
| 4d18f994-48f6-3ad0-a6b4-990ed2781de8 | -4.9535 | -45.1374 | 2026-08-24 14:40:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 3888edea-e319-3ac2-8794-f8f80ff79b50 | -7.7706 | -61.1061 | 2026-08-24 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| d92e0f02-3136-356a-b954-0cefa9d07e03 | -14.2781 | -51.7953 | 2026-08-24 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 8e15d338-382e-313a-b216-f93ecbd4fda9 | -14.393 | -52.9878 | 2026-08-24 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 979f9605-933f-3182-8b4a-dfecb7dcedda | -13.8957 | -54.03 | 2026-08-24 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 0c097ba1-d887-3ac7-a507-b1fa4ce9fd96 | -6.3322 | -54.7473 | 2026-08-24 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 156.4 |
| fe9a6d94-b3da-351c-82e7-f1037e30b6cb | -14.2785 | -51.7739 | 2026-08-24 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 156.0 |
| 406cf4b3-c528-3619-b169-d1cedd846ffd | -13.1879 | -51.4874 | 2026-08-24 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |


