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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a6c00c4-bfdd-3316-a7b5-6ee6ead8f32e | -10.52024 | -50.7725 | 2026-08-22 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d4eb951-1f13-3017-95b7-7e7b4ccefec0 | -7.72396 | -46.14866 | 2026-08-22 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 093b3d30-4e6d-3041-9fe7-5621c6d7a66d | -9.17711 | -59.45189 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 20935d0a-5035-3fa8-a628-8eb97db00293 | -8.61499 | -54.73557 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7445a1f-7189-3492-9cdd-ffa3f96f91e5 | -9.44222 | -51.6454 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa40bda2-bedb-3c20-a9c1-31d09fdb61ee | -6.77286 | -58.65736 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3bd6fdc-73ed-39f2-8b8c-7d302e9359a4 | -12.81685 | -48.42035 | 2026-08-22 05:04:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ba3846a0-6f31-304e-85c5-b20eb986b88c | -9.1277 | -61.59414 | 2026-08-22 05:04:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 70e58908-2ebb-3500-b6b2-70e2a16039c9 | -5.98206 | -51.9461 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 021fff82-1bc5-3cc6-9b9d-154805cff96e | -6.00997 | -57.79517 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e01de60-9d81-341c-96d1-c5b9f54cb5c9 | -6.85753 | -59.46545 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| a2c58d01-9f64-3a05-aace-25de6b4cf3c3 | -8.57818 | -54.74811 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 232dd442-ca51-3cbf-9ae3-1f54b2423092 | -6.81364 | -59.39808 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1007dbe7-1856-3496-a8c3-3a9fa1d6834c | -7.50278 | -60.07348 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 99b1ea35-6079-31cc-a043-73e6c434e3d2 | -8.55969 | -54.7976 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd1e5d00-770e-3efd-83d3-5db39a23d76a | -8.52675 | -54.80723 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| aefc2d0e-be9a-33f4-a6fb-41080ac27ca8 | -6.17479 | -53.50498 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2fa2e3c8-d883-3214-be88-e78cbd8ab0a1 | -6.85925 | -59.02848 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6721b9fd-e7e9-33ce-86f9-e5b47868f35d | -7.10413 | -59.78017 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81473e1b-918f-3de6-bfa5-89b5ab4b9d19 | -8.63256 | -54.69701 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 426729bf-b8fa-3e42-bb6b-ae2f1fc5b78f | -6.74177 | -58.58254 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87e1140d-f342-3d16-973c-cac5f6554280 | -6.42124 | -52.72447 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b359404-8959-3831-80d6-ee09d4b72308 | -10.4392 | -50.47211 | 2026-08-22 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 799486af-8968-387f-bf99-406d10585e5d | -7.6926 | -46.17192 | 2026-08-22 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5de20c2-56c8-3685-9084-8c1c9816554b | -6.90194 | -58.98854 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5ee2fea-1fd8-3d0e-95ea-363e940d833e | -9.4461 | -51.59676 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 807e9f2f-1f1d-3212-9ab9-1cf047185c5f | -7.35064 | -55.67603 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82386cfa-9560-3517-8511-e5fed1ef06d2 | -7.60311 | -60.82637 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d43d796-183b-3017-bdc0-5adae68441bc | -9.43315 | -51.61749 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8943f845-d94a-342d-8fa1-0930ec711209 | -10.95279 | -49.5937 | 2026-08-22 05:04:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e50484b-a38b-32b9-b501-205848b80eb1 | -7.34842 | -55.66736 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 609e2ab2-3c66-3995-b499-251866a5f49c | -6.81466 | -59.66266 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 72b1c055-5563-3830-9b99-1512f1377790 | -6.4135 | -52.73035 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 42831dcd-3fe9-3fe7-abe2-72e2aa81cca6 | -9.17856 | -59.44366 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 75e05089-0472-380b-b843-b1749f6a8980 | -6.76529 | -58.67641 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f304f461-a977-38d6-9b17-fc474e9c0b1e | -6.78771 | -58.63773 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 755ccf08-660c-30fc-9bca-13b30de17e4e | -9.05011 | -57.07045 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9f5b692-ee85-321b-85c6-45b27d2f1711 | -6.20341 | -53.09089 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23247e73-3b4c-3531-8c67-2c668a634756 | -10.3059 | -48.22776 | 2026-08-22 05:04:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8cb53e6-6b78-3c44-8350-54ea5dc28a6a | -9.05386 | -57.071 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ff7a2edd-9284-3529-9e85-ab3a6f1df0c7 | -6.77901 | -59.43812 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ee1ed5f-6bc9-37a3-bb30-f60112c90ae7 | -9.118 | -60.34092 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80abbb1a-d5b7-3af7-9a6d-27001ba458c2 | -9.16052 | -59.47017 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 31d339e0-6b14-3bc0-ae75-07e7b5a018de | -6.86687 | -59.44622 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be4af122-69ec-316b-b4da-d9eb8b2084b5 | -9.15912 | -59.45295 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 024b8b50-c754-326d-8b89-65731da9c539 | -6.9671 | -59.05412 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 0bf48c3c-c5b1-34ce-8735-dd6f36cf35ac | -8.02751 | -54.02572 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 034027c2-e340-3658-9404-1f99a68162d4 | -9.1728 | -59.45111 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e34a9736-5e82-353c-96f5-b706ae5d4a1b | -12.76289 | -48.40461 | 2026-08-22 05:04:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f7994836-2922-3759-901d-f0118de884de | -6.00288 | -57.81244 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d2f148a9-c4c1-3d2e-8475-de449ac40391 | -7.59982 | -60.82962 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ac0ee84-7299-3d17-aa98-7acc6cec80d0 | -8.62717 | -54.68153 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b2ca2c6-81bf-3798-b188-3eaa58f095f0 | -9.44564 | -51.64597 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 27e493e3-e3bd-3ad7-8b18-cf558c543c9e | -6.81966 | -59.38988 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 250a8425-47fe-3d95-bee8-1b1e47795800 | -10.28076 | -50.38657 | 2026-08-22 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83cc7d88-4206-336b-acae-1f9f8773d7a1 | -8.52864 | -55.32715 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbc4851e-2f48-337f-bad9-398c4cd5d79b | -8.52356 | -55.32306 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de67abf1-a9ce-3792-a3f3-f4c0fcb95090 | -7.08321 | -44.99822 | 2026-08-22 05:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 202fdd29-2bf1-3e1e-a673-ff64d4f10c76 | -8.68419 | -54.74276 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5f2b4e69-a9b0-390e-8919-458b484b6694 | -11.82147 | -56.59533 | 2026-08-22 05:04:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a35769d5-9008-354f-8ac9-00d4a26ad4a4 | -10.3069 | -48.22061 | 2026-08-22 05:04:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae7a24a6-33b7-3ca5-a916-01864c55dcd1 | -6.55199 | -56.26113 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ed872e5-08a7-3531-b661-eda7e7247ee7 | -9.19509 | -59.45081 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 26861105-847d-368e-9abe-b1235f7c6f87 | -12.82784 | -48.46447 | 2026-08-22 05:04:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c6e551c6-b547-3bd7-8c96-e9a3a7e5b0cd | -6.79032 | -58.63138 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d95619ef-149e-3e2c-9324-4bc6f36d6153 | -6.75317 | -58.67024 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a4b5230d-eb11-35eb-ad0f-700f69d9a3cc | -6.77154 | -58.66528 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4602450d-111d-39cd-bd0a-e6e09b0e67e0 | -11.63315 | -46.52439 | 2026-08-22 05:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e2b9df3-a7cf-3f12-8765-cded7885b030 | -5.74815 | -53.59213 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8d7033c-b729-355e-b42b-af34bd500dd1 | -8.58555 | -54.74556 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f40beb9-4cd2-369a-b452-3849726683da | -6.80456 | -59.42399 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 83acdc9a-5d7d-3cea-9e7d-1645bbbb4548 | -6.08554 | -57.9124 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 843fc2dc-12d4-3d37-a199-3df2c5aa3ee5 | -10.27844 | -50.37571 | 2026-08-22 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8930a73-5904-3803-ad63-c444ee39f672 | -6.75676 | -58.67496 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d15b3fa2-0b8c-3140-9085-f1eedd6fb066 | -11.65429 | -48.35301 | 2026-08-22 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3fa3a329-edae-3d12-b7d6-bf87d48ece1b | -6.7489 | -58.66954 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d5ce165b-e653-3620-9d1e-2eb3beff0872 | -9.42571 | -51.64292 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e314ce41-96b3-3803-b591-2bd14f016468 | -6.88419 | -59.4264 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7134a89e-b4a6-3b1f-b793-735cee694bb4 | -11.33298 | -45.02597 | 2026-08-22 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7e4778a-bd7f-3981-8fae-5ac89b1863ab | -6.54831 | -56.26051 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f1aba6b-7ced-334e-9d3a-eccf34adc008 | -6.23323 | -55.425 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de6e6750-1cc4-36c8-b72f-ec568f96b011 | -12.83246 | -48.46212 | 2026-08-22 05:04:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e7aa5aa4-e73a-3958-9545-a778bdb00aaa | -6.86796 | -59.03001 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4fe75581-7e94-3881-b222-f129d6e560b0 | -8.80332 | -48.54799 | 2026-08-22 05:04:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dd9f1029-51d5-3282-acce-f36676b8fdc9 | -10.79338 | -50.56445 | 2026-08-22 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efd8bafc-a6a4-389c-900b-836b3592e290 | -10.27413 | -50.38123 | 2026-08-22 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6273d563-64e5-3a04-b8ae-a9a198ba4f8a | -9.00416 | -50.75067 | 2026-08-22 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 3fbc8c2d-d506-328c-a5a7-7cc19110ab29 | -8.53837 | -55.33267 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 076fef3b-265a-306b-9d36-cc52a7a2e2cc | -8.53146 | -55.33152 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aab95a92-3b8c-31d9-b522-5e226228f302 | -8.57904 | -54.78576 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67feb9e1-b51e-3242-ac0f-5c24c6574e7f | -5.79371 | -57.54819 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75c4a035-96fa-3149-b37e-fbddc6b15671 | -6.25916 | -55.41565 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72f816e4-289e-3aac-a817-d853fbc3458f | -8.53083 | -55.33533 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39df756c-8722-3bef-840c-c1edb7702c22 | -6.95766 | -59.05677 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3b7df39f-fa03-3908-9379-a4b8305e7190 | -6.00375 | -57.85731 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1b8fb80d-5ed9-3dfd-b28d-bfea2eba22cb | -6.8144 | -59.39365 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9b9ed39d-0647-3405-9b37-9013b2f9f860 | -9.43712 | -51.61444 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e98556f-efc8-3c4f-b192-acd414994a3e | -6.85057 | -58.97518 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02a0801f-7e9b-3d46-a46d-e4a52c0bceb8 | -6.11839 | -57.69304 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5281c44a-7915-3f01-bd83-1bcee9832051 | -8.38966 | -62.68851 | 2026-08-22 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 27.5 |


[Clique aqui para ver as próximas entradas](README47.md)
