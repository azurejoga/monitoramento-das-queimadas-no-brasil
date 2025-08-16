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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 777eedf4-1692-3dd8-837c-13ebce9663ec | -6.92808 | -59.53478 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9aa4aa44-d5ba-3d80-a22d-83941f43699e | -9.21529 | -59.65472 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 07254e82-f455-32fd-8e53-b45d551e3515 | -8.1107 | -61.20357 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 751d4044-94a3-3c04-aa1f-6fc545057b34 | -9.21036 | -59.63672 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f07cf78-3c60-342c-9b15-288e026257d2 | -6.93353 | -59.53043 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6793615f-4f31-349c-bd7b-785fc06b7f3e | -8.56839 | -63.91531 | 2025-08-16 05:50:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 185047a3-0dfa-3621-ad67-44805ce32260 | -9.20323 | -59.65224 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b758537-b81b-35f2-b4bd-8ceb5d2bbde4 | -8.99474 | -60.53788 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c5468966-5613-3767-85c7-b745909b2fcf | -8.99866 | -60.54316 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 03b7ffc0-6def-37f2-a530-83cc45929b3a | -7.12952 | -59.65841 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 36d40022-3461-3425-aa78-a699925cb8c8 | -9.20136 | -59.63014 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c814886-bd97-3857-aeaf-539001364e33 | -8.92599 | -60.72476 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a4fa312-1b2c-3f89-978d-43009ca801a0 | -8.97886 | -61.70795 | 2025-08-16 05:50:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 363b1c8a-73dd-3709-858b-6d9f936f43b5 | -9.20473 | -59.64153 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7fa1a304-8b8c-3636-a3ff-e7f086d1a23a | -7.50236 | -63.82613 | 2025-08-16 05:50:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fa6c87e7-c599-39cc-92af-36ca9dec33d4 | -7.53265 | -61.33276 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2495c11-73d9-333e-8c32-58d00097081c | -8.66006 | -62.45839 | 2025-08-16 05:50:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ff3d640-7915-3d84-878d-19105a47228c | -8.55121 | -63.9302 | 2025-08-16 05:50:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cd29da4-5bc6-3671-ac05-f55a6aaa4745 | -6.14022 | -57.93247 | 2025-08-16 05:50:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd738c71-297a-3e28-be01-adcf539c5a33 | -8.9927 | -60.51865 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2dc51dde-6eb9-3519-b958-48c0a2c4aa5d | -8.11736 | -61.18795 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c9dcb00-af71-3f76-a9da-e14726dcf9f3 | -9.50013 | -60.55424 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 98fbb50c-c5eb-379c-b7f3-0cf0e32377c9 | -13.12498 | -57.13236 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ef2ea9dc-69df-300e-afb8-3c33a3d34df3 | -9.84216 | -67.77477 | 2025-08-16 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03016094-3df6-383d-9624-15c7064fba47 | -13.44088 | -56.68934 | 2025-08-16 05:53:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 250689ef-d09a-3963-bdaa-d1bb601c0600 | -14.94789 | -54.7315 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 331c1882-6db8-3c4c-9ea8-5de7d5ae0a1d | -10.17039 | -68.19871 | 2025-08-16 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64a1cf40-f3ec-301e-b3bc-74e1f5b7ef74 | -13.12447 | -57.13696 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 89254fc6-781f-3b9b-aaa4-a0d82daec159 | -14.94592 | -54.75264 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 285df58a-e9ff-3980-bda9-aaaf1103e772 | -14.94431 | -54.73189 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e2f2f9fb-2c3e-368f-8607-de5a0e655bbd | -14.94803 | -54.69446 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bcfd2d92-d4bc-3333-b9a7-9c036378d176 | -9.74084 | -65.32803 | 2025-08-16 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8664be1-91b0-3285-b251-48849020c59e | -13.11201 | -57.13401 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 48e7b074-9695-30c7-9522-3468f28729fe | -8.96968 | -69.2737 | 2025-08-16 05:53:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0e225cd1-3d45-34fb-8f4e-d29d580e8440 | -13.11805 | -57.13496 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e88f6244-4d40-3c2a-9a9d-54a63bf98ad9 | -9.54231 | -67.16416 | 2025-08-16 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a2e8198-b9f2-3ccb-92cb-3a7ab49e4048 | -13.12101 | -57.16824 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4de2b5c3-8928-37c9-8cb3-605d310ce333 | -9.0511 | -67.42602 | 2025-08-16 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c5e16b5-61bc-3c8d-a4f8-92d996d5ada6 | -9.37446 | -66.57494 | 2025-08-16 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95a9190e-b93f-302c-8697-66a35db00635 | -9.63173 | -63.09808 | 2025-08-16 05:53:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae099144-e1f1-3ed3-8713-51159b22322b | -9.03781 | -67.42389 | 2025-08-16 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa5f4367-1bef-3ec0-af85-a127b45fab1e | -10.47698 | -61.31853 | 2025-08-16 05:53:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1116fc28-36ca-3203-a600-e4433e3a9c5e | -13.11841 | -57.13618 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 92258629-ff1a-3e95-9940-71295d86dc7f | -14.94044 | -54.69815 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 3b641a41-b58d-33b2-bf6a-612d3884577b | -14.9507 | -54.74007 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 180f4e5a-0ea6-3e34-8490-a8ba71442ef7 | -10.40022 | -64.50533 | 2025-08-16 05:53:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b577eca2-e110-3001-af5b-dda4b2e264ab | -14.93618 | -54.7022 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8f388f05-87f3-313d-9f5a-4c0810ba4fdf | -14.94152 | -54.75983 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e9ca6636-f1c6-3499-afe0-39e36b5b70d4 | -9.41549 | -68.55364 | 2025-08-16 05:53:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6287dac5-0d77-3ffa-8674-03cd4965cd68 | -9.04501 | -67.42146 | 2025-08-16 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2603a3da-5268-3053-b8a3-cfd35e7871d8 | -9.8525 | -62.21886 | 2025-08-16 05:53:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7af26ea-410d-3dbb-aae0-59c4f97b13d3 | -14.94266 | -54.71021 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5a3231f8-97e8-38dd-a67b-8d9f71a7dba8 | -9.8192 | -63.01711 | 2025-08-16 05:53:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04286981-5fd9-3157-a04c-955751aaac1d | -10.39359 | -64.50007 | 2025-08-16 05:53:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94c2749b-eed8-3b15-a655-50abcaeb6ee6 | -9.04113 | -67.42442 | 2025-08-16 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3c54d45-4dbd-3549-97c9-d821e77d62a3 | -13.43573 | -56.67857 | 2025-08-16 05:53:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8064927e-3b28-3416-b8cc-f46c8d6961a2 | -13.11891 | -57.13165 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 88356fec-7181-3f20-b488-7a97ac946852 | -10.01526 | -59.22145 | 2025-08-16 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 428f2c9d-8ce4-377e-a0e3-7a5feff25cdc | -14.94931 | -54.75395 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7a7a2a1a-36a6-35c6-b7b6-7123ddb6b0a4 | -13.0116 | -56.87263 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b58d4336-daa6-3161-b3fb-abd283b42ebb | -9.30756 | -63.74044 | 2025-08-16 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 74bdd192-3626-3bf7-8002-e55fd4ce10d4 | -14.93985 | -54.70411 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 6a9569c2-9a09-3fae-bcbb-2365ec0116dd | -9.03393 | -67.43042 | 2025-08-16 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7bb05e23-4f73-365a-860a-31dc1f330490 | -10.40084 | -64.50113 | 2025-08-16 05:53:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15a068f1-a7c0-3026-8a54-8134c32959ba | -9.92458 | -60.48188 | 2025-08-16 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e03a3573-a311-332e-a3d7-7cf289cc2a8a | -8.81439 | -68.61555 | 2025-08-16 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9bb06688-f455-3e29-b38a-10f18c92b912 | -12.02886 | -63.32988 | 2025-08-16 05:53:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 21b2b5d5-a7b1-3d61-9e88-e39c630cc377 | -13.13361 | -57.16528 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c2fc759-fbbc-3cb4-8da9-5e0f3448e83f | -8.79226 | -71.02586 | 2025-08-16 05:53:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 763c3112-aff6-3578-8c13-b62e3125cbe0 | -9.53431 | -63.71562 | 2025-08-16 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9506a97-155a-3eb8-9f6e-758537ba09a6 | -10.04711 | -64.89661 | 2025-08-16 05:53:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6899a0cc-7c40-3c35-b617-c6bfc6d597cb | -14.86847 | -60.09047 | 2025-08-16 05:53:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e6638b2e-d6ab-3f1b-977e-9647f44eb848 | -8.57507 | -69.6939 | 2025-08-16 05:53:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24263e46-df4d-31c6-924f-4fd4feb54423 | -10.51017 | -68.08439 | 2025-08-16 05:53:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.2 |
| b61f862b-6e08-32e7-a29f-2e8734294505 | -13.13306 | -57.16398 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e59602f7-9cf6-36fe-9c39-e5ddd6d86ab0 | -14.97525 | -54.71133 | 2025-08-16 05:53:00 | NPP-375D | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d8f08c2-8333-36a2-94bd-948a354e3733 | -9.03448 | -67.42693 | 2025-08-16 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b29680a9-a879-3915-b843-ac493bd05108 | -9.04723 | -67.42897 | 2025-08-16 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cb424f13-2d03-3c76-b86c-fec78624bb3a | -9.04169 | -67.42094 | 2025-08-16 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9f55a42b-4576-3b06-b0c8-3ec41629a3aa | -11.9479 | -62.8368 | 2025-08-16 05:53:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12e0d2e6-5355-3eb5-95e3-ba6ae0f21072 | -9.92391 | -60.48675 | 2025-08-16 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 730ab3a0-1dcd-3c82-9764-9256c80e528e | -10.0106 | -59.21781 | 2025-08-16 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f3748f3-f2e9-3fb0-a522-abcb8c3eb012 | -10.2488 | -68.2583 | 2025-08-16 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b90fcce-77c4-3165-bda1-040fd788c283 | -9.04778 | -67.42548 | 2025-08-16 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6e4f4020-9091-3638-9095-c13bb53375eb | -10.16674 | -69.00479 | 2025-08-16 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8a090e1-e48e-3566-99be-80a13a662d20 | -13.11858 | -57.13042 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 772ba1bf-bc1f-348f-81e6-34488725669c | -13.13311 | -57.16978 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0b014c3-d0c6-32e4-bb32-dbae61f2ad5d | -14.93922 | -54.71044 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6843286e-e5a8-3313-84ca-cf3769bb846e | -14.95497 | -54.73304 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9a57f2f2-43aa-3e21-974c-a8a36c231aaa | -14.9514 | -54.69405 | 2025-08-16 05:53:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5bf3ff27-c650-3c4a-8f23-05d0c02058fb | -13.132 | -57.17296 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1483864-f90b-377f-ab42-5b451a332f52 | -14.94725 | -54.73839 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 66a3c1ac-1c42-3721-866c-5680c5176daa | -13.44143 | -56.68442 | 2025-08-16 05:53:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8345d33f-3f09-3b8e-9a1f-145d0a7e42d6 | -14.9487 | -54.68778 | 2025-08-16 05:53:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8b3bfd7c-81f4-3921-8f4b-d704d77eba95 | -13.44254 | -56.67441 | 2025-08-16 05:53:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f33706ba-17ad-346c-9ac5-334b06b3b3d8 | -9.34592 | -62.58739 | 2025-08-16 05:53:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 15c7c947-b2b9-3f7e-a57e-19fcd3f85c0c | -9.81525 | -63.01316 | 2025-08-16 05:53:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a8c91bd-7e8e-3d9d-b07d-388081bea514 | -13.13911 | -57.16471 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08ed34ae-f294-3cd5-b352-55bd437ef034 | -13.11334 | -57.17517 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77932ac1-8049-34bb-834d-d67d905f8151 | -9.9207 | -67.83453 | 2025-08-16 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README70.md)
