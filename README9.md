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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74e44c0f-edfa-3b98-a6df-4e9e6ba6b00c | -13.89003 | -47.33806 | 2025-10-31 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 844743e9-d13e-3245-b0ba-d939aae37452 | -5.80204 | -35.5835 | 2025-10-31 03:47:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a7b27324-7c4f-36dc-b4bb-6c8b2fa7ed88 | -9.86028 | -44.84794 | 2025-10-31 03:47:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4c59f4f4-c95a-3fde-933c-5362b0691593 | -7.81866 | -46.40048 | 2025-10-31 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49a2581d-a3e0-3799-a3e2-79e020faa5fe | -5.42095 | -44.58599 | 2025-10-31 03:47:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd2d9b9d-948e-31de-a0fa-dc1f344c948d | -9.86312 | -44.86174 | 2025-10-31 03:47:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e83a9918-c32a-3632-a520-8050b506d55d | -13.90533 | -47.35004 | 2025-10-31 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d0587d38-2fef-35c5-8028-6c1ec6968419 | -5.11706 | -43.29848 | 2025-10-31 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e518207-22d3-3046-a151-43664ed2e686 | -4.83587 | -45.33105 | 2025-10-31 03:47:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3c13d229-76b9-3faf-8273-543d31358834 | -6.25596 | -42.55489 | 2025-10-31 03:47:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| b60ecc20-4577-33a7-86b4-d4dc27a94c8e | -10.84172 | -44.92767 | 2025-10-31 03:47:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 866e8e2e-4619-39ca-a1c2-f1cc18d08068 | -5.02092 | -45.56755 | 2025-10-31 03:47:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ab17b58-5bd8-3771-8eb6-4d8baa241a30 | -7.43297 | -41.85646 | 2025-10-31 03:47:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f5a8fe22-e5f3-3ab7-a068-c95272ce431a | -7.04464 | -41.47219 | 2025-10-31 03:47:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7f1da61c-fa0a-3228-9a9c-4754ef9505fe | -10.74993 | -44.72796 | 2025-10-31 03:47:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0215dd6-78d0-330d-b400-7c6c43b270d2 | -7.04027 | -41.47165 | 2025-10-31 03:47:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4a36515b-ae48-3a6b-a043-c421012a7318 | -5.11398 | -43.297 | 2025-10-31 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f4025c1c-fb7c-3035-abf8-d3fe353803bb | -14.1302 | -44.187 | 2025-10-31 03:47:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26f37e87-1581-31fa-8acb-e7b63362823b | -5.78905 | -40.81451 | 2025-10-31 03:47:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f1052b07-70a7-37e7-9918-2ea86923e8b8 | -5.25657 | -45.51162 | 2025-10-31 03:47:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2287a9d6-e947-3763-8119-69e97996d7f8 | -5.01492 | -45.56704 | 2025-10-31 03:47:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02243f5a-7e1e-30e5-8a50-549134f02d08 | -7.36378 | -44.63182 | 2025-10-31 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f91090f-5d14-33f4-a85d-efe6daba31ab | -6.92275 | -42.24982 | 2025-10-31 03:47:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| afea0802-a712-3caa-883a-91fdaaef8409 | -10.74915 | -44.64733 | 2025-10-31 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3eb3d8e-2f5a-3ed7-bef4-a786e2bdd73a | -7.92085 | -46.79795 | 2025-10-31 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c3fb010-97fc-3be4-9a91-179ea3e25b2d | -8.10109 | -45.17848 | 2025-10-31 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 505b5e03-7298-3783-b561-5b88e68fc384 | -10.92761 | -44.76355 | 2025-10-31 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e99aca30-7cfe-3bd8-b72a-a69f1d0aca48 | -7.35723 | -44.6375 | 2025-10-31 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f48a6071-f182-3c67-ba7c-f18c3c743dcc | -7.34606 | -45.00734 | 2025-10-31 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 661b5f73-e29c-3b03-9d4c-b23c55528aca | -10.92615 | -44.16263 | 2025-10-31 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e2a15193-a872-3d46-bd81-de336af70425 | -4.67084 | -46.42834 | 2025-10-31 03:47:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 620544b9-fbbd-3f89-b424-568853291377 | -8.1072 | -45.17607 | 2025-10-31 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01a7caee-7552-3bf1-b1e6-75cce7aaf1c5 | -8.09168 | -45.13747 | 2025-10-31 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e9fa650-1ebd-3688-a8b3-29fa06c5415b | -4.76569 | -45.98821 | 2025-10-31 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d97f9a1f-7f1b-3c4b-b3e8-db9b491de6cc | -15.04277 | -41.94456 | 2025-10-31 03:47:00 | NPP-375D | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9a72eaa2-8d28-3314-b8db-9354e5dc7f30 | -5.92598 | -44.57288 | 2025-10-31 03:47:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db3f4e03-5481-3b11-8135-3681c9567c28 | -5.80441 | -44.43213 | 2025-10-31 03:47:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47c32d29-e5e7-3507-aba1-a9b9e48f9e27 | -4.6634 | -45.09054 | 2025-10-31 03:47:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bb3455df-fb70-386b-9263-c32baf130aaf | -13.68502 | -44.73034 | 2025-10-31 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 5f1468f6-7843-39e5-8860-5ed5a5bf1dd1 | -13.39151 | -47.34191 | 2025-10-31 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5252e273-06b1-3012-a19c-1177b02dd123 | -8.15487 | -45.46671 | 2025-10-31 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 052ccd3b-9395-3d36-a593-9534d459c140 | -3.52849 | -47.55375 | 2025-10-31 03:47:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fcbc5336-8a0b-3ad1-be6c-b3bd0642423b | -16.36591 | -45.24651 | 2025-10-31 03:47:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c26c9fbd-fca0-34e9-8323-cb65a0aa46d0 | -4.8688 | -44.6511 | 2025-10-31 03:47:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00b44124-e118-3d90-86b8-8c95fd15e7b1 | -3.48195 | -46.01794 | 2025-10-31 03:47:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9bdd832-86ed-3ed0-861f-9b9e94432005 | -5.47455 | -44.31732 | 2025-10-31 03:47:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d65646f9-cc2a-3c83-8688-b1507f62e8de | -10.85882 | -44.9043 | 2025-10-31 03:47:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 906917b4-b49a-30dd-a316-c8988defe2c7 | -5.7925 | -43.73797 | 2025-10-31 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f2a9a2ca-29d9-30e1-985b-7d507292f7ff | -4.05341 | -47.50687 | 2025-10-31 03:47:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 790af28d-103b-39ed-912f-0fa82c95d10f | -9.72839 | -48.03519 | 2025-10-31 03:47:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 16dc3736-019f-3e9b-b6dd-4595215a8f89 | -9.92095 | -44.92677 | 2025-10-31 03:47:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3b778c03-5957-3c4b-a885-6b1c011f92cb | -9.5137 | -47.26911 | 2025-10-31 03:47:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27b89c20-899b-3500-bc50-2d7321278011 | -8.0849 | -45.14379 | 2025-10-31 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 01164d28-37b9-3d8a-a2e4-1f0a6e9fb4a0 | -6.68818 | -38.19658 | 2025-10-31 03:47:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 4ffb4d22-45da-3fd4-8a73-8bc740c39f37 | -6.81096 | -44.45575 | 2025-10-31 03:47:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2972a894-7d76-39c8-9b5e-e0d4c0e038c8 | -7.37999 | -46.22372 | 2025-10-31 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2689061-dc51-32e8-b84d-4f9a9224afcd | -5.95407 | -45.56231 | 2025-10-31 03:47:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4198cea7-a3ea-3433-8250-197f31d058e1 | -10.85084 | -44.90689 | 2025-10-31 03:47:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ff725f33-8d78-3ffe-a0c6-36c067da3ab1 | -4.45988 | -45.75686 | 2025-10-31 03:47:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c35e1299-e452-3639-a272-09bc287f840f | -7.92689 | -46.79707 | 2025-10-31 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5185a674-073c-397c-b32e-c115c266dc58 | -8.09233 | -45.13384 | 2025-10-31 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 180195c5-a396-31c7-ac94-75a3ded8c191 | -4.9209 | -45.31807 | 2025-10-31 03:47:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fcbc3fa7-7baf-3c79-b6ce-8f597791f60f | -4.4808 | -46.56926 | 2025-10-31 03:47:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2b4b692a-c445-39c4-8e98-49615dcd7989 | -4.9545 | -45.8787 | 2025-10-31 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 695be3dc-02db-32e5-a56f-2dbd0d881e3e | -14.12561 | -44.18605 | 2025-10-31 03:47:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 51dea000-70d2-34b2-a568-dcf6e9cf9814 | -5.77633 | -39.21062 | 2025-10-31 03:47:00 | NPP-375D | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 72c7c839-dcbd-3068-9c7e-4cf234ac634c | -7.34747 | -39.33652 | 2025-10-31 03:47:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b65a528b-6ef6-315b-83e5-2019b23e3aed | -5.28412 | -45.42175 | 2025-10-31 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c80bdb00-4882-3a0f-a4e2-c21eecd240ed | -7.77132 | -46.47619 | 2025-10-31 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d87bdccf-d073-3cd8-bc0f-26d6fdebc442 | -8.16436 | -45.50832 | 2025-10-31 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b18010e2-346e-325e-aa7d-cbb099b6d1e3 | -10.53535 | -45.0431 | 2025-10-31 03:47:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09ef696e-5830-3be3-9bbc-aade7c5b1cd8 | -4.78995 | -44.32093 | 2025-10-31 03:47:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fac1ad9b-cd33-397c-8d32-57134da3495d | -8.18242 | -45.69258 | 2025-10-31 03:47:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 797af2b6-8c62-3583-aac4-2dd3878042f5 | -6.55426 | -44.02197 | 2025-10-31 03:47:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc9a3ac9-87a7-31d9-a8d6-f2ebbcf1ed4f | -16.30154 | -45.09674 | 2025-10-31 03:47:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c2070a40-dd0a-3c4c-9a8c-01ef6a920267 | -9.8843 | -44.86397 | 2025-10-31 03:47:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cdef7630-858d-31eb-a258-bd72f2850003 | -7.61585 | -46.4717 | 2025-10-31 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8bf397f-4e6a-38ae-83f6-f2e93b72a373 | -10.53008 | -44.92524 | 2025-10-31 03:47:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc4ac690-35a7-3917-ae97-f606e267c6ee | -10.49451 | -43.32251 | 2025-10-31 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4a689f0-55a9-3c32-917c-81709d8a634f | -7.48469 | -41.74132 | 2025-10-31 03:47:00 | NPP-375D | FLORESTA DO PIAUÍ | PIAUÍ | Brasil | 2203859 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e994f290-3c27-3536-a946-3d46d1a827d7 | -10.93586 | -44.16453 | 2025-10-31 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f35c07d6-9ba7-3b93-994a-bfaef1dc9354 | -10.84326 | -44.93015 | 2025-10-31 03:47:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 540de93d-0e11-36ce-8f57-cbc6334f61c4 | -5.41018 | -41.24332 | 2025-10-31 03:47:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 38d5f59e-a10f-38c1-b2d9-953e19542d10 | -5.88602 | -39.7627 | 2025-10-31 03:47:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 37ce7ee1-0f21-383f-a969-38a195f9b7df | -3.99232 | -43.42689 | 2025-10-31 03:47:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8488fc54-2173-3bdc-a928-26bb115ce6ea | -10.94208 | -44.63062 | 2025-10-31 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04a80b80-3540-31bc-921c-d1f858c3bf5d | -3.54048 | -46.42943 | 2025-10-31 03:47:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f43b3a2-9dcc-36ac-af44-74c43bce0093 | -9.87752 | -44.87118 | 2025-10-31 03:47:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ae759c2-6783-3cdc-956a-98152f4e8c91 | -9.8837 | -44.86712 | 2025-10-31 03:47:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a2bf95c-8ac4-3b70-a6be-0cd98ca7c0fc | -13.62952 | -47.58866 | 2025-10-31 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04174b3d-be60-307c-9f1a-94f651b3af41 | -6.53223 | -43.71233 | 2025-10-31 03:47:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b01579b8-f68e-32d8-b11b-ceb4c13912af | -8.9016 | -37.96969 | 2025-10-31 03:47:00 | NPP-375D | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8cb10f9a-9176-3545-9282-23979dbd5291 | -6.51746 | -40.80083 | 2025-10-31 03:47:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 981041ec-06b9-3f2a-bde0-97354e00abf5 | -13.68602 | -44.725 | 2025-10-31 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 080b1164-6a9a-3f4d-90f5-f4286a4ab29b | -10.53089 | -44.92517 | 2025-10-31 03:47:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| afaefe91-8c25-35f2-8399-a220f281d318 | -6.52763 | -43.70852 | 2025-10-31 03:47:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 688835e3-92bd-3030-82da-615b7e5aca04 | -5.36753 | -45.52139 | 2025-10-31 03:47:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ab7445f-38d3-3ea2-98d1-1138ec9c5afc | -7.08361 | -44.92678 | 2025-10-31 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a25ab6a1-f7a3-3f95-86c0-f68f7b03f01b | -6.86119 | -39.56198 | 2025-10-31 03:47:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5f956cdc-7586-3a70-90d2-71e3ff217b03 | -13.88858 | -47.34522 | 2025-10-31 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |


[Clique aqui para ver as próximas entradas](README10.md)
