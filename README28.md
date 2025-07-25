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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae44f37b-adc1-3cdd-bd5a-6cf336fcf220 | -9.03889 | -61.23135 | 2025-07-25 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 465d5120-bde7-3394-9f0a-0588bb12982a | -9.20102 | -59.68006 | 2025-07-25 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d1d09ad-90e1-327d-8c12-c145f59fa8d2 | -9.13279 | -63.92304 | 2025-07-25 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b92e361b-f11a-33af-9f8f-181846d8cca1 | -7.6703 | -69.93163 | 2025-07-25 06:03:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 09919e79-f2b5-3c97-afa8-a13c7154378a | -8.65187 | -68.68107 | 2025-07-25 06:03:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65cff891-7204-3fa2-8d05-a5b19aef336f | -9.7624 | -65.09379 | 2025-07-25 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9011d4f6-fcef-3956-a4e0-8e366f41c56d | -11.94285 | -58.75999 | 2025-07-25 06:03:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2ba5660-2781-3209-86c7-fd35e1c6171d | -8.45484 | -70.08449 | 2025-07-25 06:03:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7061903-aa90-3137-ab1b-40bb31dab3c7 | -10.3633 | -57.50502 | 2025-07-25 06:03:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 36aa1afa-bfbc-30fa-a7cb-f603d6e47a12 | -7.97972 | -70.99457 | 2025-07-25 06:03:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| fe23acef-d44a-3f4d-8c20-77fedd75122f | -9.03935 | -61.22784 | 2025-07-25 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed523d2b-f594-32c4-8885-c5debc7033d3 | -9.73989 | -65.10388 | 2025-07-25 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5079423-13a6-3929-9224-8729f2062b2a | -9.74299 | -65.1123 | 2025-07-25 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5296e2ce-c8c9-37f6-ac0d-490bc12f4703 | -11.67972 | -58.49395 | 2025-07-25 06:03:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ebc08d8c-c37f-3ffa-a971-5720faccedeb | -11.94223 | -58.76534 | 2025-07-25 06:03:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d7d0115-b1f7-3b7e-915f-8cea5c7e9084 | -10.04219 | -59.10081 | 2025-07-25 06:03:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5aabf23a-882d-3b42-bc38-3ade779bed54 | -11.67568 | -58.49313 | 2025-07-25 06:03:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d396be32-d908-377c-823f-3947d5574d9f | -10.36407 | -57.49843 | 2025-07-25 06:03:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e089c07a-fe5f-39dc-881c-baf432fa319e | -7.78202 | -72.78363 | 2025-07-25 06:03:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74d2528e-4a56-344b-b379-49f9c01422c9 | -10.0479 | -59.10674 | 2025-07-25 06:03:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 40526d35-407f-3a47-be0d-a7c6b8d2bdeb | -9.57727 | -64.22253 | 2025-07-25 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e8bf760-e5ad-3666-a1d8-64de6f6e0e92 | -11.94881 | -58.76628 | 2025-07-25 06:03:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4666732e-173e-3545-a003-004b4c746f11 | -11.94943 | -58.76103 | 2025-07-25 06:03:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5709d67b-d4e5-38aa-8af8-752bcf5eedfe | -9.74355 | -65.10841 | 2025-07-25 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e97c376-1c71-371a-a07f-9dfbe35cf5f7 | -9.20609 | -59.67985 | 2025-07-25 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0219e1a5-e22b-3073-952a-aff186ef8303 | -7.03628 | -71.69465 | 2025-07-25 06:03:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7d19275-347a-36f5-9a9e-942010fec1fe | -7.67362 | -69.93216 | 2025-07-25 06:03:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d2d2221-97c8-31b2-90fb-1d6a5907aaca | -11.94778 | -58.76081 | 2025-07-25 06:03:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 56cdffb8-247e-329c-97c2-098aa47ace26 | -11.4584 | -45.1126 | 2025-07-25 06:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| f9047841-457a-377b-bbe8-65b8160af968 | -7.67255 | -69.93146 | 2025-07-25 06:25:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 539942d9-164b-3a42-8cb4-f172f0e59e32 | -9.96782 | -64.95224 | 2025-07-25 06:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5fdcbdd5-d15c-327c-805e-9f2c765e2d12 | -9.74393 | -65.11063 | 2025-07-25 06:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32032a30-9f05-323e-834c-2456d4a01563 | -7.66716 | -69.93266 | 2025-07-25 06:25:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 694901d5-529b-3c4e-b029-64e48b5094cd | -8.65429 | -68.67904 | 2025-07-25 06:25:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8103bfcf-f105-37e7-af13-bd107a2334ca | -8.65388 | -68.68201 | 2025-07-25 06:25:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7b39c87-a8a1-318a-8fd9-763bfdf38206 | -7.67173 | -69.93327 | 2025-07-25 06:25:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 875c3819-8876-323f-8e0d-bca48de3b8d5 | -7.66798 | -69.93082 | 2025-07-25 06:25:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e03fa98b-dc6f-3ac2-9988-96f3d22c72a3 | -8.95623 | -72.8396 | 2025-07-25 06:25:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ce87820-463a-3e42-b58d-5994303fd4ea | -9.73748 | -65.10957 | 2025-07-25 06:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc16ef5c-4ab3-3159-8bae-01d7e96c215c | -11.4584 | -45.1126 | 2025-07-25 06:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 0e25a2c0-c404-3c8b-9e5f-81229eceae1b | -11.4584 | -45.1126 | 2025-07-25 06:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 905efda9-cde0-325f-8e35-c6b4b96ee8a5 | -15.7954 | -41.9591 | 2025-07-25 06:50:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 69.4 |
| 0f987b36-44be-3d86-a35c-b8edd8c3c780 | -15.7954 | -41.9591 | 2025-07-25 07:00:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 66.9 |
| d88eca8d-e814-3959-97ea-525bc72ecf57 | -15.7954 | -41.9591 | 2025-07-25 07:10:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 62.6 |
| c06cd52f-2c53-3dc9-be4b-ef0cd7389955 | -15.7954 | -41.9591 | 2025-07-25 07:20:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 62.0 |
| 8c9c1f58-a2fc-38bc-a93a-c7581eb54eb7 | -15.7954 | -41.9591 | 2025-07-25 08:10:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 74.7 |
| 9e908442-2436-33bd-8c9a-28febd334e79 | -22.1161 | -52.5776 | 2025-07-25 08:50:00 | GOES-19 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 177.1 |
| 927236f9-2171-3c29-a3e0-c7704ff463a0 | -22.1155 | -52.6 | 2025-07-25 08:50:00 | GOES-19 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 71.7 |
| 7893ca31-bc4f-3c19-b7fe-214b9c1263b1 | -22.0953 | -52.5818 | 2025-07-25 09:00:00 | GOES-19 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 88.7 |
| aa2b8803-0772-33dd-ad9e-b65659b0f1a9 | -22.1161 | -52.5776 | 2025-07-25 09:00:00 | GOES-19 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 140.9 |
| 2ffabe8e-0b8c-3a64-ae9f-0b999e4f8bfc | -15.7954 | -41.9591 | 2025-07-25 10:00:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 126.8 |
| ad0fe0f5-bd87-3c4c-bf86-3c993ad66a8d | -14.9523 | -46.9616 | 2025-07-25 10:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 101.1 |
| c38dae7e-5766-3c4f-a021-9b04317f7f46 | -6.48762 | -37.76702 | 2025-07-25 11:32:00 | TERRA_M-M | JERICÓ | PARAÍBA | Brasil | 2507408 | 25 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 4532e271-20db-3c07-982f-3fb8147f94f2 | -6.78916 | -37.67136 | 2025-07-25 11:32:00 | TERRA_M-M | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 8c5b1af2-85d2-3c03-9c94-2c5180752b82 | -6.77854 | -39.17924 | 2025-07-25 11:32:00 | TERRA_M-M | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 671144ae-8d2e-3fa0-8fd7-51f88e85e90f | -7.92076 | -44.09758 | 2025-07-25 11:32:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 40.8 |
| df5c899b-f894-37f7-b192-e0fd216aafc4 | -6.77772 | -39.1887 | 2025-07-25 11:32:00 | TERRA_M-M | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 25.0 |
| 3cd570ae-90ee-361a-a847-993c13a4edd7 | -4.39258 | -39.26467 | 2025-07-25 11:32:00 | TERRA_M-M | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 5866fa73-cb4c-3adb-b239-dc0507ac446b | -14.14943 | -45.25132 | 2025-07-25 11:34:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 24.4 |
| ca34fb57-0a20-3435-a03c-e1066be9b619 | -12.99088 | -44.90513 | 2025-07-25 11:34:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 8eb70a44-8bbf-3ad9-b4c0-0c7649887282 | -19.12762 | -40.46842 | 2025-07-25 11:34:00 | TERRA_M-M | GOVERNADOR LINDENBERG | ESPÍRITO SANTO | Brasil | 3202256 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| b22b807d-c2ef-30a5-a685-5efc8e737a05 | -14.13526 | -45.2756 | 2025-07-25 11:34:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| fa17015d-5bb7-3fe3-a9cd-64e47b4660de | -14.14319 | -45.28457 | 2025-07-25 11:34:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 2c35ed15-7a52-346b-b59d-3f87dafd7678 | -8.3297 | -44.949 | 2025-07-25 11:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 4bcb3c3f-4da8-3e6b-9437-f929e32d3eeb | -8.3485 | -44.947 | 2025-07-25 12:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 5a73e429-157f-3196-85e6-b3c37998ee62 | -8.3297 | -44.949 | 2025-07-25 12:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 2af028f4-0ca8-3f85-8394-876bdac12c2d | -7.7694 | -44.5476 | 2025-07-25 12:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 6668fd7d-f27f-311d-b17f-05c8f46457be | -8.3485 | -44.947 | 2025-07-25 12:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 5eea3ab3-5c33-3962-970d-b9fc8323db44 | -8.3485 | -44.947 | 2025-07-25 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 89cf63b7-fa74-31b6-a4c1-23c370af2f54 | -8.3485 | -44.947 | 2025-07-25 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 7ff7aa78-ebab-3886-b6c6-b1d07e3001fc | -8.3485 | -44.947 | 2025-07-25 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 84.2 |
| fb314112-8f47-31b6-bfe8-c4a3bc9fd575 | -8.3297 | -44.949 | 2025-07-25 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 103.0 |
| d5502273-6f99-37e2-84d6-ba1c44277499 | -8.3485 | -44.947 | 2025-07-25 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 963b7ab2-9b1f-368c-8f1a-7fc2fc441bc0 | -8.3297 | -44.949 | 2025-07-25 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 02ce9600-3bfc-35c4-a329-0873bed1d187 | -8.3485 | -44.947 | 2025-07-25 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 102.1 |
| af10bd94-6a63-37d8-ac56-ec2fa1278d4a | -8.3297 | -44.949 | 2025-07-25 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 101.3 |
| a7e34edf-c384-38e9-9beb-296fa1b9077d | -8.3485 | -44.947 | 2025-07-25 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 106.5 |
| ad54ba33-9479-33f9-b630-01cf5a0f4c3f | -8.3297 | -44.949 | 2025-07-25 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 94.4 |
| edf91fb1-179a-3fcf-8844-f4b681291d52 | -8.3485 | -44.947 | 2025-07-25 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 153.1 |
| dfff32ee-59d6-3a68-9d21-1f25a69e9358 | -4.9682 | -43.2299 | 2025-07-25 13:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 77d80c2c-4f81-31df-ba87-b4d1c10f4507 | -8.3297 | -44.949 | 2025-07-25 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 94.6 |
| ffbdd1a4-ff80-35eb-a772-a6257b2ba205 | -11.6791 | -51.6623 | 2025-07-25 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 66bb331e-ad12-3fcd-811e-7321f8cf8109 | -8.4869 | -47.4682 | 2025-07-25 13:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| edecfe9c-88bd-3b37-a157-429492ce4845 | -8.3297 | -44.949 | 2025-07-25 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 6f23e786-b3d1-3720-9dcd-e332ba57faaf | -8.3485 | -44.947 | 2025-07-25 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 0b10762d-1c72-3c70-9ac9-282044dc11cd | -4.9682 | -43.2299 | 2025-07-25 13:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| bb22346f-89a9-3743-805e-509c5074e64f | -8.3485 | -44.947 | 2025-07-25 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 161.4 |
| fa5309e7-bc03-3fc3-8774-0667c7e55b1e | -7.2399 | -44.8041 | 2025-07-25 13:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| d5b67cb9-046a-3ed2-8dbb-c8630006b03e | -8.3297 | -44.949 | 2025-07-25 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 4165fd37-bcce-3e2c-9947-614e4241c70a | -9.023 | -45.3305 | 2025-07-25 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 74.8 |
| a2a5dc3e-45df-3d23-bd1f-4ad026f887fb | -7.2399 | -44.8041 | 2025-07-25 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 349559f6-528e-3be7-a8d6-4b4b1908864d | -4.9682 | -43.2299 | 2025-07-25 13:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| caf8b208-0ec3-34cf-b363-46c35e1119e5 | -8.3485 | -44.947 | 2025-07-25 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 163.8 |
| a4d86b40-5b52-3158-930e-25ca46733af0 | -7.4445 | -44.9907 | 2025-07-25 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| f09ed9d3-aa11-373f-9582-779c9d1915ef | -7.2402 | -44.7812 | 2025-07-25 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 4d84af0c-c092-3776-b541-a5097ba79a28 | -8.3485 | -44.947 | 2025-07-25 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 76747888-0e2b-3506-8ca2-ded26da06606 | -9.023 | -45.3305 | 2025-07-25 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 704eef7e-9542-37c4-bf42-7c21a5f690df | -14.1327 | -45.2644 | 2025-07-25 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 6b252b1f-75f2-372f-b155-f34e509d353b | -4.9682 | -43.2299 | 2025-07-25 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 4c7c1ae8-f06d-3cd9-bf67-85031f233c12 | -6.5626 | -56.25 | 2025-07-25 14:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |


[Clique aqui para ver as próximas entradas](README29.md)
