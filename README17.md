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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 454a3a4f-d1e2-30d5-a312-a8740788bcb7 | -6.6318 | -51.252602 | 2026-09-19 00:41:00 | METOP-C | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9be1bf2d-07da-3a77-8a32-0ee924667653 | -5.488 | -45.804798 | 2026-09-19 00:41:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b23434de-9c3a-3310-adf3-8186b7f10fc2 | -9.0307 | -48.742001 | 2026-09-19 00:41:00 | METOP-C | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| edee73f1-23ba-3fcc-977b-6ad976c4ba0c | -5.9077 | -46.315102 | 2026-09-19 00:41:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4681dc96-8361-3dfb-a512-f07396aedf35 | -11.3067 | -51.720501 | 2026-09-19 00:41:00 | METOP-C | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 394ed695-6ebf-34d6-8447-c67bd1679a19 | -13.6217 | -48.308201 | 2026-09-19 00:41:00 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 453dfc1e-25c0-3f36-9e4b-6125920fb502 | -5.3311 | -48.980999 | 2026-09-19 00:41:00 | METOP-C | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d6f3756-01da-3008-8544-8527c8f940d8 | -10.1854 | -48.515099 | 2026-09-19 00:41:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4133f8e6-f9a1-395b-b8a7-6db7a6324829 | -13.7408 | -48.798302 | 2026-09-19 00:41:00 | METOP-C | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| be3ec34b-bb9c-36db-ac4b-a248128b5131 | 1.2607 | -50.954399 | 2026-09-19 00:41:00 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 08a8c391-f9db-3e89-a90a-35879953faee | -10.4683 | -51.260399 | 2026-09-19 00:41:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a832e5ce-8edf-315d-9e06-bc2326a28641 | -8.3751 | -45.658798 | 2026-09-19 00:41:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 273327ea-6352-338f-a08d-44281240ad9e | -11.0776 | -48.2672 | 2026-09-19 00:41:00 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 89455d1c-3225-3a7d-bbb7-743963b29564 | -11.8613 | -47.588402 | 2026-09-19 00:41:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9da92819-0d74-3fb9-a895-a2a53c2632b9 | -9.0276 | -48.728199 | 2026-09-19 00:41:00 | METOP-C | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 4453212c-68e1-3e9b-9d21-9ee942a89aab | -10.6982 | -50.25 | 2026-09-19 00:41:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d8f2817-2f9b-3a4c-8dda-3707acaf5b28 | 1.256 | -50.9748 | 2026-09-19 00:41:00 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| a46a66e5-348a-3ccc-ab89-e954cfb4066c | -3.8161 | -50.7393 | 2026-09-19 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6548f64-cc78-3263-9266-35f75cad9d1f | -12.9951 | -44.833698 | 2026-09-19 00:41:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0b4bc9f8-c781-33fd-aea9-3e797fa71d68 | -3.3567 | -50.444401 | 2026-09-19 00:41:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5659275-741f-3e3a-8704-323b6757b10b | -11.0462 | -48.310902 | 2026-09-19 00:41:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e395b00e-eb95-313f-809e-555f99f0dceb | -12.1253 | -46.9856 | 2026-09-19 00:41:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 107fa629-b35d-3696-940b-a0cf62ce0205 | -10.2045 | -46.584202 | 2026-09-19 00:41:00 | METOP-C | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 30301c0a-384a-3126-80c7-88f921b80364 | -12.6021 | -50.879002 | 2026-09-19 00:41:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8092057f-27e1-3a72-8c26-0cef97aa7abb | -5.8701 | -53.548698 | 2026-09-19 00:41:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 601e2eeb-6332-3bdd-a9c6-5cf3d86fee52 | -1.702 | -54.882198 | 2026-09-19 00:41:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f183b90-c31f-3c5d-bea6-e3d1e5fa56b8 | -4.0517 | -56.2505 | 2026-09-19 00:41:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 560b3ff7-d147-3c40-84f3-bd735703b409 | -14.1487 | -45.207298 | 2026-09-19 00:41:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ff9d8cb1-1a81-369c-9ab2-75d9e857ca17 | -7.0203 | -44.653999 | 2026-09-19 00:41:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5d04f9c6-1ade-36f6-9066-e5b9795c8fc4 | -4.2117 | -56.325901 | 2026-09-19 00:41:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7b0db24-70d6-34a8-9b93-a91149d211a8 | -10.932 | -47.855099 | 2026-09-19 00:41:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 16db590d-4ff0-3a6a-8633-12259de926a8 | -5.2287 | -47.558701 | 2026-09-19 00:41:00 | METOP-C | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2183dbb2-ef03-3921-beb2-6cc94a92756b | -13.0049 | -46.9505 | 2026-09-19 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| de4e7c64-bb7f-3401-ae55-bb328f57e9d5 | -10.1344 | -49.1544 | 2026-09-19 00:41:00 | METOP-C | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 65ca22d0-ebfe-37cc-b05e-d14da334fa67 | -10.8687 | -54.091099 | 2026-09-19 00:41:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2aee91e8-673c-34fd-bada-7f2dc14bac3b | -5.3244 | -48.996899 | 2026-09-19 00:41:00 | METOP-C | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99334533-60c3-31ee-9543-faeea3c4a135 | -9.9728 | -50.2714 | 2026-09-19 00:41:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6f9bbdc5-c33e-3ed5-be89-d277457a6e5f | -2.2925 | -47.887901 | 2026-09-19 00:41:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 581eb6e1-4ae1-3c86-9ee9-f914b966a742 | -3.2066 | -53.948002 | 2026-09-19 00:41:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8cdd7b38-596a-3e26-b37b-4be39a6b7736 | -12.1384 | -46.997501 | 2026-09-19 00:41:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 12195af6-e3a9-343d-9f51-dab711edf306 | -13.3857 | -48.036701 | 2026-09-19 00:41:00 | METOP-C | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a61dad11-8932-304e-ba32-2900f1e23c56 | -5.1847 | -49.3311 | 2026-09-19 00:41:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1e4c287-8b27-39ab-8f5f-2e9bb5667c91 | -12.2791 | -49.1674 | 2026-09-19 00:41:00 | METOP-C | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c05ad446-6710-3285-bbb3-94e49c4c2232 | -9.7284 | -48.1395 | 2026-09-19 00:41:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4921885b-4c59-30c2-9d59-2f6b630facca | -12.7422 | -47.019901 | 2026-09-19 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cf8eba6a-3d53-3015-9f0c-9e235116136a | -2.3886 | -48.525799 | 2026-09-19 00:41:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9383ed5c-6dbc-3e1b-9997-67c1131eaf11 | -9.994 | -50.2743 | 2026-09-19 00:41:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 38216a56-3f54-3204-811e-afe990903b52 | -3.2311 | -46.956501 | 2026-09-19 00:41:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b0d00b0-e43e-3d88-83e9-e185407ed2bf | -16.3022 | -53.861301 | 2026-09-19 00:41:00 | METOP-C | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d21ef95a-8856-30d1-b6d3-b3585c9c6a15 | -9.2362 | -46.198898 | 2026-09-19 00:41:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 53867172-7179-3ed2-ad87-35af13f39ce7 | -8.6399 | -47.535801 | 2026-09-19 00:41:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 11f4a1f9-2edd-3284-915a-d36d224463b5 | -11.3491 | -44.138 | 2026-09-19 00:41:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 137177f7-3aba-330c-8650-10a7b033b6cb | -7.2224 | -49.6287 | 2026-09-19 00:41:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6fb38bc-a2ce-3497-8491-908bd7e21686 | -7.5591 | -57.669498 | 2026-09-19 00:41:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4154708c-9752-306e-a2b5-4d9d2ef8c6d9 | -5.2443 | -49.411098 | 2026-09-19 00:41:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 778504e8-6a6d-3fbc-ab28-5d5bf4965b98 | -8.4593 | -45.708801 | 2026-09-19 00:41:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 86cb7efb-1b0f-380b-afc6-1f84d09a934a | -8.983 | -50.171101 | 2026-09-19 00:41:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccda2da1-0b05-3f00-bc90-78389f42504e | -4.5767 | -42.938099 | 2026-09-19 00:41:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 648af563-70d7-3785-830a-a7a3c43ab21e | -3.0325 | -48.410702 | 2026-09-19 00:41:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b05ae75-00b0-35bf-8d41-785049f62694 | -10.6999 | -50.2575 | 2026-09-19 00:41:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f40ade16-f9e0-3cac-b516-0a41b966eee3 | -3.5572 | -50.284599 | 2026-09-19 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7dd8ce3e-5897-31fc-a592-433931f70a17 | -7.1851 | -50.829201 | 2026-09-19 00:41:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0df0b36-c3b0-3087-b008-f1616fda03cf | -13.6103 | -48.303398 | 2026-09-19 00:41:00 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 54b5c31d-b60c-3b9f-8369-78ba187ff869 | -11.0823 | -48.287998 | 2026-09-19 00:41:00 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 726a46cc-0d5e-3e52-b3a9-b093879b33b0 | -3.7335 | -54.644402 | 2026-09-19 00:41:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7461836e-f254-3b9c-90ff-71988d2e665f | -2.8164 | -50.471802 | 2026-09-19 00:41:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37b534ad-e2a5-33d6-ab3d-e093a3af6cf9 | -8.8675 | -49.7491 | 2026-09-19 00:41:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca71b0be-4d0e-32f8-bc56-591170f45c53 | -2.023 | -48.773899 | 2026-09-19 00:41:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55597182-bd71-39f5-a3de-2665e969b716 | -11.8629 | -47.595402 | 2026-09-19 00:41:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5b1d0dbc-fb5f-37b9-98c9-0c69f0c99c61 | -10.6078 | -46.1012 | 2026-09-19 00:41:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8668807c-e385-315e-b296-66ccce92731d | -13.6119 | -48.310501 | 2026-09-19 00:41:00 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ae76777f-ef0a-3f61-8511-cfcfbc178dd8 | -6.9772 | -42.183201 | 2026-09-19 00:41:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ac2944ed-07c9-35d9-afa2-570f28cc0b17 | -10.3753 | -50.4632 | 2026-09-19 00:41:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d8efb7d2-8e49-3c15-b3d0-04d2c5e72048 | -7.67 | -46.126598 | 2026-09-19 00:41:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 580e503c-6d19-3afa-961c-9fe648e4c680 | -12.5829 | -49.098801 | 2026-09-19 00:41:00 | METOP-C | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 375d6d7f-9b17-3ea6-970b-d322b167e2dd | -8.4515 | -45.719299 | 2026-09-19 00:41:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bbff6de6-13f3-339b-9f9f-e8cbde4bc013 | -6.3138 | -47.5648 | 2026-09-19 00:41:00 | METOP-C | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4973bc2b-dd82-3e93-9d74-910d61d922d4 | -4.1455 | -48.2267 | 2026-09-19 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ef55158-729c-3de0-b29b-d8d0e4db7f33 | -4.6885 | -46.3964 | 2026-09-19 00:41:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e23a7587-7ad7-39f3-83fc-4f96bbbe35ff | -7.6466 | -46.115002 | 2026-09-19 00:41:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6d4215eb-fdd8-349f-8bf3-5cee3e775816 | -3.1417 | -53.9338 | 2026-09-19 00:41:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46773653-7b52-3cf0-a933-2f3c663e2aad | -13.6329 | -46.944 | 2026-09-19 00:41:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 70a1b150-eba9-3d43-a4a7-c38c54d2b639 | -12.8553 | -44.379398 | 2026-09-19 00:41:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ffbdc86f-a4bf-364e-a111-7ae9d2d4b909 | -4.5833 | -42.965302 | 2026-09-19 00:41:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d7be8655-d990-3f74-961f-f8290a1afc21 | -13.6881 | -48.606701 | 2026-09-19 00:41:00 | METOP-C | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d5b8b2fd-e3e0-3317-8d0c-da7ee2d4586e | -9.7814 | -45.055698 | 2026-09-19 00:41:00 | METOP-C | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6dac1a86-ae31-3039-98f8-5bd90abfa8df | -4.2816 | -48.591099 | 2026-09-19 00:41:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd60d5c2-2bc9-3a02-bf71-e1a7c0717588 | -7.361 | -50.330601 | 2026-09-19 00:41:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f41013d-1a58-397f-8fe4-1234a7591bdf | -14.6835 | -46.6651 | 2026-09-19 00:41:00 | METOP-C | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 373dccdb-75f3-34db-87dd-4064d416ca9f | -11.9433 | -50.1152 | 2026-09-19 00:41:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4fd7a213-acf7-3893-b244-a36a1c46bbb7 | -6.5883 | -44.1441 | 2026-09-19 00:41:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94c500fb-d6c5-38cf-b973-d97c24be1656 | -13.0114 | -46.933998 | 2026-09-19 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 15429275-c245-38d3-8b56-422f145268ab | -11.13 | -49.047001 | 2026-09-19 00:41:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 56f8a8f7-911d-31b7-b234-53144e0c01b3 | -9.7451 | -46.078701 | 2026-09-19 00:41:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 48430e48-8bd4-3dc7-8bd9-dd31b54264dc | -9.3506 | -50.111801 | 2026-09-19 00:41:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a778f68-622c-3b7d-8065-940919fd1c68 | -8.4945 | -57.634399 | 2026-09-19 00:41:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b18f577e-8b86-3c99-bf7e-59d9d7bb5d49 | -17.9636 | -45.122398 | 2026-09-19 00:41:00 | METOP-C | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 706e2f87-82fe-3de6-95e3-dabeb3128aa7 | -8.4866 | -57.596401 | 2026-09-19 00:41:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad89db14-659d-3426-bdf6-44fd516108d6 | -8.3786 | -47.210999 | 2026-09-19 00:41:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a40d72db-ba24-3482-bebd-912c1c6d1060 | -10.6149 | -50.245098 | 2026-09-19 00:41:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README18.md)
