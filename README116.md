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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c2984e7-0812-3188-8b04-ebb4913c782a | -9.6924 | -65.09006 | 2026-08-28 17:28:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.6 |
| e32ade2b-1573-349b-bb0b-9be14d33c29a | -8.44483 | -70.71133 | 2026-08-28 17:28:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 3ef73033-76d8-3952-8312-4f3df51fb273 | -8.21902 | -70.50737 | 2026-08-28 17:28:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 3f79bdc8-db79-3e7f-b6a7-90d6c536916d | -6.21666 | -52.97134 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 4a3e8251-34ce-3688-acf0-238fa5f2debf | -6.15203 | -56.1119 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 287ee7be-64a6-34fa-bbac-ab70a7d420dc | -6.31935 | -54.7466 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 57ed9a60-7a08-3a6c-a04b-82289946ce93 | -6.26079 | -55.42237 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bbe41e8b-7ded-3037-92fc-7637514f8368 | -7.1002 | -55.47762 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 4bd9ea63-84f9-3009-a866-209dcc76066e | -7.50238 | -55.28786 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| c172839a-ffea-3587-9d07-bf3fbf1dd535 | -6.32512 | -54.73786 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| c967099b-0f83-3477-a31e-17bbbe4fdb1a | -8.82761 | -49.6008 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0b3c67bd-c3ed-3d97-9d00-af0a0930c667 | -4.52368 | -55.94167 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0e9afa2d-f85f-30fa-86c2-5790d9a485ba | -7.01487 | -59.64046 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 882dde1d-629e-32e0-b333-97283bd8d2e3 | -6.37205 | -54.95678 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 12a19708-2124-3b4e-ab39-9cda56beafc8 | -2.81068 | -43.82757 | 2026-08-28 17:28:00 | NPP-375 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 2cb11515-898c-36fd-964d-43a625f0a99a | -4.05658 | -60.63965 | 2026-08-28 17:28:00 | NPP-375 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| df3c7b2a-0971-343c-84ab-b7dee0cf8894 | -6.59654 | -55.45081 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 6d26485b-18dd-3e99-a83d-a09b96f8ed5a | -6.83496 | -56.13267 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bb8cee12-2edb-3405-8cca-b6e1258becc7 | -6.75538 | -59.46582 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c1f8e387-f202-385b-bcac-04601d5814a9 | -3.7075 | -57.22595 | 2026-08-28 17:28:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 7ee3c3d1-2892-3137-bd81-012a838e5d8d | -6.77071 | -59.44734 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 9e8f0e53-04ce-389a-832c-8549a9705ac7 | -6.30511 | -56.27116 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9395a060-147b-3d50-8376-ada71cf8bc58 | -7.35117 | -55.16611 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1a7d5560-0388-3ef8-b3cd-3dd23c5c332a | -6.4694 | -55.86835 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 038e0b41-7e62-3dd2-a71c-018970723dea | -8.58162 | -54.82215 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 9734d52e-20b3-3951-bcee-ee3a773a5f7d | -5.91582 | -61.30286 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8fbac812-7b02-3691-ab2e-ade283109163 | -2.71474 | -47.03665 | 2026-08-28 17:28:00 | NPP-375 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 595f62eb-c667-30b4-9fde-167ddad37303 | -7.59791 | -61.35357 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 55eee263-9f6f-3d01-a082-5126c6929fbd | -6.16669 | -57.79946 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 221a33f3-e180-32df-9cd9-efb5907b40e7 | -7.36479 | -55.18644 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2fd86bda-eaed-3884-a6fa-56ea5ce31573 | -6.18342 | -55.44207 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 19d156d6-39cc-3c26-ac44-6e55939230b7 | -8.03642 | -51.81502 | 2026-08-28 17:28:00 | NPP-375 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1620d5ce-6e82-32a3-8bd7-d27e327f5781 | -6.19079 | -55.44465 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 156f439b-e7f4-3ca5-b77b-5ac03a77f2ad | -10.25372 | -55.88436 | 2026-08-28 17:28:00 | NPP-375 | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| d453e4e0-23dc-311e-a7db-2c59a4bb305d | -8.8793 | -66.90191 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 37e04424-08f9-360b-ac89-284d5d3aed30 | -10.57362 | -57.49498 | 2026-08-28 17:28:00 | NPP-375 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| c302ed9c-2622-36e6-b897-8df00ff82400 | -6.08068 | -57.38407 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d02da2f0-614a-3bba-93e4-fc7de662f905 | -7.11897 | -43.16776 | 2026-08-28 17:28:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 59e57844-5dc0-3a79-9d3f-d47e53707e9f | -7.48506 | -61.40329 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| c38d2935-1b1f-3671-957e-4ad06b7d258a | -6.84469 | -59.46104 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.2 |
| d5a02176-9290-3d36-9896-4ec9795cde47 | -8.95627 | -45.73595 | 2026-08-28 17:28:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6502edd1-67f7-3e0f-89de-037a6bacd5ad | -10.08128 | -68.56506 | 2026-08-28 17:28:00 | NPP-375 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 11.2 |
| a818c285-7e69-3255-9573-0942c4a8b39c | -6.77009 | -59.46762 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 6d732b0f-6a2f-3701-99da-af72aa4d20fd | -9.93345 | -60.43592 | 2026-08-28 17:28:00 | NPP-375 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 117.4 |
| c01089b3-eae1-3d68-acbe-128aa29d0a89 | -6.73842 | -59.03684 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| edf8355d-6bbd-386d-b7e1-92c6a2be9810 | -6.95528 | -59.48124 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 6970b948-7122-3819-80ba-5c8ab0dc1762 | -10.51058 | -59.62818 | 2026-08-28 17:28:00 | NPP-375 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 66d78c32-d49e-3a88-9a89-dd329d40ea03 | -6.2139 | -53.48309 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 1e404cfb-76d5-37a0-b3dc-b3fd7b0821e7 | -6.02309 | -57.73643 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 0fd3472e-859b-3acd-820c-e051e8441cba | -8.21816 | -70.50018 | 2026-08-28 17:28:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 5d916c2d-f6bd-3c3b-910d-5b122eb1d9fe | -5.80908 | -51.66488 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bf5091d1-82a5-39fa-aca8-dfd027fa29f3 | -4.39268 | -55.46206 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f4016ca7-d696-3d3d-b9fe-a23074a6987e | -9.04145 | -70.5907 | 2026-08-28 17:28:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 25.7 |
| cb195fa8-9add-3f4c-86e7-a7d587542fc4 | -7.48902 | -61.40274 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| c90d7b61-8a7b-3203-bf0c-b17680820cd7 | -6.2562 | -55.39312 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5fb76700-e6dd-3063-aee2-ff425e64e717 | -7.28406 | -49.95306 | 2026-08-28 17:28:00 | NPP-375 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 87c6ee0a-dc42-3958-9389-a1fbe5c73357 | -6.01718 | -57.78753 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cffe1c89-c648-3c6b-9c4c-1cb5d985ad0a | -9.61793 | -55.11619 | 2026-08-28 17:28:00 | NPP-375 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3e2ad018-26ff-3f61-87ac-241d0d3fa070 | -6.31816 | -54.73897 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 65c586ba-8cdf-3979-9686-f722779470d5 | -7.58171 | -61.32494 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| beef3868-07da-3091-a8af-c9d1878b4a2c | -6.96287 | -59.04623 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f3312f15-88be-3f96-9f07-02c292666315 | -7.13412 | -48.07246 | 2026-08-28 17:28:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 76d3ec6d-c07a-3530-be75-81706fd6df24 | -6.56807 | -56.52995 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 386a1ddd-1950-32dc-bfa6-f2dc4af29dda | -6.80368 | -59.40224 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 622bd9ef-f1c7-3c49-a286-86f2fca63a8b | -6.14022 | -53.70098 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 69558d63-2fca-3ce3-9278-8af6532b34ba | -6.90088 | -43.65566 | 2026-08-28 17:28:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 7ac2a88e-085a-3d3b-b20d-c744f2acc22c | -7.62086 | -44.81893 | 2026-08-28 17:28:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5362f3b9-4565-35e0-80a3-ebe4ec1bd68a | -8.79463 | -62.47747 | 2026-08-28 17:28:00 | NPP-375 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 38adec6f-8e45-3500-880b-46f1b73ad471 | -5.99788 | -57.68298 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a1385d66-e337-3293-8974-c983cb977996 | -6.59598 | -55.44717 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 0ce9b4d0-8862-3e0c-a546-c49994057b96 | -7.59428 | -61.32825 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f9b3a27e-9248-30e1-8fcf-7f75e258adf9 | -10.58013 | -63.55909 | 2026-08-28 17:28:00 | NPP-375 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c51233b6-cbc1-3a0d-95be-dc7ee9623445 | -6.26362 | -55.41819 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4bcf78fe-abe5-3a7e-a960-1d9a805c81ce | -6.02029 | -57.74044 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ae1d78ec-b0bf-30cf-835b-4b1190910798 | -6.14745 | -53.81715 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fb66fff9-664c-3daf-b775-9382a9f1ff5f | -7.59323 | -61.34907 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 5a0b8272-0d99-3226-bd8b-906c3b52e066 | -10.06249 | -69.10809 | 2026-08-28 17:28:00 | NPP-375 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 20c63ab2-5b6a-3b43-a54b-cccfbacb8012 | -6.53319 | -55.24743 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| fcc064bc-5efd-3606-8050-24628071e3d5 | -6.77594 | -55.68452 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| eb6c4a14-f4f6-3130-b9ce-9c03132d33d2 | -7.7227 | -57.49521 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 851425e1-1e70-3aa3-aac4-4673321a54d6 | -6.54401 | -55.2495 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| ce295038-d4cf-3c73-89f4-dfd0bce3db72 | -6.75955 | -59.44501 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 769909ba-e16e-3924-b5e3-756b3065eb06 | -3.69739 | -50.05938 | 2026-08-28 17:28:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 764997ad-4afe-3b21-a227-d3b12e18674b | -8.24531 | -54.99305 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 960dae63-cad1-3f6e-a7c0-f0fa8d57203f | -10.50707 | -64.51883 | 2026-08-28 17:28:00 | NPP-375 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 15.6 |
| ff722fa4-7874-3ec2-bb94-fdf4c6c0d6df | -7.34833 | -55.17024 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 68306442-7948-3c20-b022-9fd1211aa5fa | -9.25358 | -57.08154 | 2026-08-28 17:28:00 | NPP-375 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7c09646c-92d9-362e-8e36-9f1991c2c81d | -10.50474 | -64.50081 | 2026-08-28 17:28:00 | NPP-375 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9d523414-2b02-3e09-9f63-e5241848459e | -6.75802 | -58.72633 | 2026-08-28 17:28:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 6c55843b-6ca9-32ea-ae96-6779519d8767 | -10.41145 | -61.19637 | 2026-08-28 17:28:00 | NPP-375 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| adce9cef-fa3e-3af5-a65c-0319ebf097ce | -9.88187 | -60.26314 | 2026-08-28 17:28:00 | NPP-375 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 7a251cf4-5d06-3761-9aa3-67b344b586e1 | -6.6022 | -55.4425 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bb6fe6a2-30c5-3e53-9439-0b618eb98ca3 | -7.3506 | -55.16245 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9b1d12c7-281e-31d5-842b-84497c72933e | -9.69075 | -65.07717 | 2026-08-28 17:28:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 57f217e5-8198-32c4-8a33-55d052ba5294 | -5.99014 | -57.67699 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 8715b841-1ce2-33ed-8dd8-f774b2d16267 | -7.02882 | -45.76873 | 2026-08-28 17:28:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 9686a0e1-c963-3fc3-beee-82da03b12251 | -5.84326 | -55.7184 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d19855c7-e486-38af-a0a4-deabaacbe048 | -6.17849 | -57.7869 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c044038-1c68-3c23-97ca-bfeba971f140 | -6.27877 | -53.14066 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| df15bbca-a248-3797-8627-7ce2f0f37e5b | -4.97197 | -44.89628 | 2026-08-28 17:28:00 | NPP-375 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |


[Clique aqui para ver as próximas entradas](README117.md)
