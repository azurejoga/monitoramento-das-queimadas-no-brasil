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
| 3e172133-b24e-33fb-ac35-d5b21bb4a146 | -7.13563 | -44.28941 | 2025-07-14 04:27:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce73d615-f19b-3bef-a0fb-076c6515608a | -6.38353 | -43.28905 | 2025-07-14 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4a331240-de25-3e31-a7fe-00a4835dc4d6 | -7.00584 | -44.40952 | 2025-07-14 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a19dee8-39b8-3c5c-a509-d248ab13d2f0 | -6.83506 | -44.83676 | 2025-07-14 04:27:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 475b9232-6864-3ba8-86b9-cdbe6ecfb007 | -7.58478 | -44.72787 | 2025-07-14 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b8e6601-134e-357b-9ad0-74b021345520 | -6.28637 | -43.41259 | 2025-07-14 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79c525c2-c17e-390c-b34f-1c5f2c893f30 | -8.51754 | -43.30901 | 2025-07-14 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 4af0776c-fe9a-3625-888a-1413dbcbc751 | -7.4191 | -43.89642 | 2025-07-14 04:27:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae96c3fd-ffa2-3da1-9bf0-1644c871a0e4 | -5.73605 | -39.54467 | 2025-07-14 04:27:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4e352640-fbe8-339f-9d73-e95ea15fa537 | -6.23964 | -43.34441 | 2025-07-14 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0894b1a-fb45-3470-8f4e-686c7e814eef | -4.24913 | -46.62946 | 2025-07-14 04:27:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6da3e34a-85ad-39a4-9601-28dc1533c58f | -7.2728 | -45.30465 | 2025-07-14 04:27:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76abbd58-4431-3a8b-a766-468c20021a7a | -7.19124 | -42.96536 | 2025-07-14 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f3ece65a-43c2-3170-975d-c3dd9775be41 | -6.46843 | -45.37266 | 2025-07-14 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7079586-3895-3a5f-9ad6-ef3607e2ef79 | -6.16486 | -45.88331 | 2025-07-14 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3aecadf8-1f94-37d8-9b7d-9378db7d90ea | -7.06025 | -43.96034 | 2025-07-14 04:27:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 749d49eb-67a4-374f-b97b-44ab49678009 | -10.27985 | -47.61406 | 2025-07-14 04:27:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 59d862fc-6c04-314e-8e5d-ea54669bbfb2 | -8.04436 | -50.09166 | 2025-07-14 04:27:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| e9529648-fa65-357e-acbf-8149da8410f1 | -7.80583 | -44.78789 | 2025-07-14 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a88a7fd-afde-3dc1-a939-baebdd135cd5 | -7.22693 | -43.99721 | 2025-07-14 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 055154f3-e978-3072-b424-855f49887b34 | -6.16208 | -45.87932 | 2025-07-14 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 73eaa113-382a-3afd-aed4-033ffa83d4f3 | -5.62434 | -44.36198 | 2025-07-14 04:27:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c829987-d1f5-307e-8ac0-6c48f7259cd9 | -8.24459 | -41.93182 | 2025-07-14 04:27:00 | NPP-375D | NOVA SANTA RITA | PIAUÍ | Brasil | 2207959 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d15e6968-4e90-3546-b12e-0cd338626e6f | -4.24579 | -46.62894 | 2025-07-14 04:27:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 58930201-4a3b-3433-8d54-d9a36aaf4618 | -4.57036 | -43.08984 | 2025-07-14 04:27:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2f74fd08-4875-32d6-9738-38c7acf1ca27 | -7.26745 | -43.49646 | 2025-07-14 04:27:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d7cabba3-f1b6-340c-b61c-252d0d2dd410 | -7.0415 | -44.36115 | 2025-07-14 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ac77b68-cdfe-38aa-8b23-d69fcd0e7be6 | -5.62491 | -44.35831 | 2025-07-14 04:27:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30f45555-b7c1-390d-9f98-5fae1da87b5c | -7.58421 | -44.73156 | 2025-07-14 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e6185d3-7027-33d1-ba84-b0956e10d6b4 | -6.40521 | -42.44702 | 2025-07-14 04:27:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f94d3f30-81f6-3906-a139-9f70586eeaa8 | -3.98282 | -48.42031 | 2025-07-14 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63d9f96c-abc4-320f-8345-52a08906c588 | -5.1561 | -37.68575 | 2025-07-14 04:27:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.5 |
| abc55c1e-3986-37c3-bc26-be0cc4a91018 | -4.11197 | -47.92719 | 2025-07-14 04:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51dac534-9cab-36a7-9ac9-936b56065356 | -3.98346 | -48.41632 | 2025-07-14 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 613e8814-9be4-3595-9c4a-6380a2bdd355 | -5.24697 | -39.48116 | 2025-07-14 04:27:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 42720357-81c2-3c9f-974d-05cc67b18856 | -8.87524 | -46.91098 | 2025-07-14 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a3d2d4f-badb-3d56-b027-9c3ab77e34db | -6.71016 | -43.89314 | 2025-07-14 04:27:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa635df0-4c49-30e6-b2ed-9d0d6bff589e | -3.58374 | -47.51101 | 2025-07-14 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b29355d7-5998-3c58-8973-521f1a3027a0 | -8.51789 | -43.29811 | 2025-07-14 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 27.6 |
| dba3ed35-907d-3386-9c3b-823f0c6a25da | -6.75874 | -47.366 | 2025-07-14 04:27:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff4d0849-446e-380b-aa96-4d3c508e372d | -4.30833 | -48.10499 | 2025-07-14 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4e3ba17b-6b85-366d-afe0-af562329cb54 | -7.02198 | -44.37335 | 2025-07-14 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45349308-e914-3bf6-a4a0-af635a670d7d | -7.33328 | -45.31408 | 2025-07-14 04:27:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01647ded-6626-36d6-b753-afbd31d887fc | -7.59789 | -44.73371 | 2025-07-14 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7e5e3bc-197c-366c-9d8f-e230cf4475c9 | -4.86611 | -45.31633 | 2025-07-14 04:27:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e691910-244c-3303-aaeb-c9917b22522d | -6.28281 | -43.41201 | 2025-07-14 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e499bfe5-acdf-31b0-a85c-2509c7ca878c | -7.26443 | -45.31429 | 2025-07-14 04:27:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 79c609df-1d53-37c6-8f58-0dba3355d212 | -8.87579 | -46.90749 | 2025-07-14 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c535ecd2-af66-380a-aab0-306a4ceb50cc | -6.40208 | -42.44226 | 2025-07-14 04:27:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ad961bfa-fc6b-3e3c-8e05-918ee8e4143c | -6.28576 | -43.41663 | 2025-07-14 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b292e752-c5da-3b69-ae14-a408040b9f58 | -4.30739 | -48.10524 | 2025-07-14 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 80d1d75c-faef-32f9-8a78-88965bfc4b68 | -6.43496 | -45.34579 | 2025-07-14 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f7569e1-2594-339c-81a5-f469ef336b21 | -5.15971 | -37.68714 | 2025-07-14 04:27:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 93227188-6b57-34a5-86c6-e8f2814fcb50 | -7.05139 | -44.32006 | 2025-07-14 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56c06c94-ad67-3747-90ed-12694accedbb | -7.54546 | -45.05191 | 2025-07-14 04:27:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 793df903-e32b-3a8a-ade1-055f3026ef8a | -5.26785 | -45.12805 | 2025-07-14 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b91e589a-9594-34b8-9737-a817447850b8 | -3.97992 | -48.41574 | 2025-07-14 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a1bc50a-2fa0-31b0-9eda-001187596e85 | -7.58877 | -44.72467 | 2025-07-14 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cca91bff-6de1-3874-be08-82d27b9ca46a | -8.51453 | -43.30413 | 2025-07-14 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 25.6 |
| a8d78bdb-e111-3bf1-96b8-7deaaca78fe0 | -9.50196 | -47.56749 | 2025-07-14 04:27:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d001f915-2d2a-3359-ab56-0e7b5f211f2c | -6.44778 | -45.35146 | 2025-07-14 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aab25800-1af0-316a-8c69-e9507c7d1333 | -6.25804 | -43.35855 | 2025-07-14 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd951695-43ce-30f9-9d28-4cec6a223ff0 | -7.05265 | -43.96315 | 2025-07-14 04:27:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d239b6a-df82-3653-9f2d-5fb482d5ede8 | -6.81852 | -43.72499 | 2025-07-14 04:27:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae086d27-0769-3800-a7ab-983f2f087a3b | -7.06083 | -43.95647 | 2025-07-14 04:27:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77c4bfd4-ff45-3cfb-ba4a-12a13b060349 | -7.02081 | -44.38093 | 2025-07-14 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8149185a-917e-37e5-8e8f-81ccbc7f00ec | -6.84134 | -42.77265 | 2025-07-14 04:27:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 12a9f014-923e-3259-9b7e-ec5b7ddbea51 | -9.49253 | -47.56236 | 2025-07-14 04:27:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b370992-b7f0-3752-982b-ff9b845df664 | -9.51195 | -47.5691 | 2025-07-14 04:27:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf71fc5a-2897-3754-bd70-11c0d07f6d07 | -7.96939 | -45.93742 | 2025-07-14 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c0628d49-452e-30a5-95c3-598b7209d7c8 | -5.27002 | -49.29836 | 2025-07-14 04:27:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0665a624-3928-3011-9fc7-652e554c9261 | -10.2865 | -47.61514 | 2025-07-14 04:27:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 616c2ca7-18d9-3e24-bdd5-78f5c7da9173 | -6.24322 | -43.34491 | 2025-07-14 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b19335d-58c4-3239-9b64-476d7bdbb0bf | -10.28318 | -47.61461 | 2025-07-14 04:27:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| abca92e5-2e70-383b-9956-d0bd4abed9e8 | -6.9915 | -44.48001 | 2025-07-14 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41c8b677-462f-31d5-92e3-9b33b40f494a | -9.48879 | -40.38974 | 2025-07-14 04:27:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 76095c5d-9228-3ac5-8285-02e3286685fd | -6.94372 | -42.73203 | 2025-07-14 04:27:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6a3ae7b5-5fd8-39a2-8101-9a80b6a1b884 | -7.03917 | -44.37624 | 2025-07-14 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d28279f2-14ef-3479-90c3-cd0685686cbb | -6.06081 | -44.58867 | 2025-07-14 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a535b8a-2260-3e17-9a07-241ae6cddf08 | -3.62018 | -47.54726 | 2025-07-14 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd381434-47c0-3ab2-b831-6daff8785caf | -6.43272 | -45.33819 | 2025-07-14 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 99df20e6-2239-338b-8668-da2a9b51f69a | -6.46564 | -45.36861 | 2025-07-14 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f87de72-5ec3-3c5b-a688-b047e9a85a9e | -4.86283 | -43.22538 | 2025-07-14 04:27:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4be6baee-75e9-36c6-ad4d-a27b9b914c8a | -8.51519 | -43.29979 | 2025-07-14 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 25.6 |
| 2424c849-94b7-35ac-825c-e90f74621690 | -6.62572 | -56.28595 | 2025-07-14 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b30b59b2-5db0-30f9-9c98-9b94cddccbe1 | -4.86348 | -43.22674 | 2025-07-14 04:27:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 757b0b0b-dfa4-3584-bdf1-bbf42171e54c | -8.8647 | -46.86997 | 2025-07-14 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8afab515-0eb4-3ca0-a69e-4fb5dbfe7ceb | -4.01027 | -49.46945 | 2025-07-14 04:27:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 247c3886-5609-3f5d-afbe-9bf51985161d | -7.29639 | -44.53693 | 2025-07-14 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cebd60c5-9b7e-3d6b-964e-4f544f358c2a | -7.26723 | -45.31839 | 2025-07-14 04:27:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| ae7ccefb-84b9-3247-a56e-66f09aeab260 | -14.49562 | -58.59688 | 2025-07-14 04:29:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c67c64f-3453-30d6-b359-8f4f66874eae | -13.0332 | -47.81268 | 2025-07-14 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5202dfc9-4dc2-3ec9-b51a-8874824d7085 | -13.03652 | -47.81322 | 2025-07-14 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5ccd003-1e1d-3add-a243-b25331baeec5 | -16.30647 | -44.20462 | 2025-07-14 04:29:00 | NPP-375D | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 69041fbc-bfb2-3af1-8bdf-27305f7e9a29 | -13.10371 | -47.29763 | 2025-07-14 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 735834c4-33bc-3142-917c-a9af11269623 | -13.02655 | -47.81159 | 2025-07-14 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a86d2f16-2e13-32b4-838b-68edc8d531ca | -13.10099 | -47.30051 | 2025-07-14 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5db2cda1-48db-3ddb-ac7a-eabb6144ffb0 | -13.10043 | -47.30407 | 2025-07-14 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa6706ed-a3bf-3295-88bf-a20369ecff8b | -17.09559 | -43.80445 | 2025-07-14 04:29:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf42be39-393d-381c-8b69-70f8b2242ae2 | -13.01978 | -47.81741 | 2025-07-14 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README10.md)
