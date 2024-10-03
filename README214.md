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

## Dados Diários - Página 214

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48acb73d-0495-3cc9-9520-188d616c3e8b | -9.6012 | -50.1779 | 2024-10-03 13:36:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| ed60d496-ac44-39ae-938d-cc01c4da9ec3 | -10.0418 | -48.2097 | 2024-10-03 13:36:03 | GOES-16 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 2e83507d-a806-3512-a16b-28107c532538 | -10.0229 | -48.2117 | 2024-10-03 13:36:03 | GOES-16 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 45.1 |
| ec36ef3e-deb7-30a5-acae-10245d2e077d | -10.2381 | -47.7038 | 2024-10-03 13:36:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 57c66c67-9f15-33be-a501-ca2a3468d766 | -10.2195 | -47.6839 | 2024-10-03 13:36:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| c84184ef-8718-3a80-a9a2-173e72b7bd7c | -10.7161 | -46.1942 | 2024-10-03 13:36:06 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 905ec31d-ada9-39a5-8cdb-ba93b3ad4fc4 | -10.6794 | -46.1085 | 2024-10-03 13:36:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| bec135ba-fffd-3aa5-9595-ce58deb0c313 | -10.6791 | -46.1311 | 2024-10-03 13:36:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 52323521-6ad9-3a43-ba2b-63426d620e28 | -10.5736 | -48.0839 | 2024-10-03 13:36:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| f6170fe2-f0fd-3fd2-8eac-695c4b202b98 | -10.7168 | -46.1489 | 2024-10-03 13:36:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 4d98bb3c-6a76-3441-b3b7-d4e2ba367cfc | -10.7158 | -46.2169 | 2024-10-03 13:36:06 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 35726ee5-e539-3fdf-9909-3454f2d00566 | -10.6978 | -46.1514 | 2024-10-03 13:36:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 199.7 |
| a28bbd4b-f1d0-3009-a7ff-82cb2b6e4d02 | -10.7502 | -47.6882 | 2024-10-03 13:36:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 90d35ec0-9572-3770-bad0-0103dcfec271 | -10.7456 | -47.9978 | 2024-10-03 13:36:07 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| edb07048-813a-34b6-ba6f-f095a0980aaf | -10.7122 | -47.6927 | 2024-10-03 13:36:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 136.5 |
| ad6464a9-8bb4-35c1-b382-1ce28ccbf7cc | -10.7309 | -47.7126 | 2024-10-03 13:36:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 2d905367-e93a-314b-b723-276c47fe8ab1 | -10.6317 | -53.7011 | 2024-10-03 13:36:07 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| b1bb4fa7-000c-364d-bac5-94a089303dce | -10.7118 | -47.7149 | 2024-10-03 13:36:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 1ee54eb8-547b-3681-b607-6db1231f6df6 | -10.7348 | -46.2145 | 2024-10-03 13:36:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 667a967c-112a-35d0-8749-fa89e6930e01 | -10.7352 | -46.1918 | 2024-10-03 13:36:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 163.1 |
| 1b715a5f-ee31-34b7-b8f9-7bcbed361f99 | -10.7312 | -47.6904 | 2024-10-03 13:36:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 230.3 |
| 1505a72a-9605-3f81-8826-4d149f88d121 | -10.7834 | -45.5495 | 2024-10-03 13:36:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 177.1 |
| 3f22fe12-acb4-3d8b-8427-b835f8c6e415 | -10.7831 | -45.5724 | 2024-10-03 13:36:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 193.5 |
| 8f8363ea-e8e2-367e-9bf2-21432b8887e0 | -10.7459 | -47.9757 | 2024-10-03 13:36:07 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 17eb5296-7e97-3234-a1d8-f8b0472424aa | -11.0345 | -46.5143 | 2024-10-03 13:36:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 87ddf8bd-d45a-385d-ae9e-b87b0810e180 | -10.876 | -48.1584 | 2024-10-03 13:36:08 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 94ea1ef2-a898-3238-a187-aaa9bac0a691 | -11.2783 | -43.388 | 2024-10-03 13:36:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.9 |
| d55dd021-ff98-3dc1-a7f1-ed2ce895e716 | -11.2779 | -43.4118 | 2024-10-03 13:36:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| e9e53a8b-305b-35e9-8f86-315458c5fc79 | -11.1575 | -45.9779 | 2024-10-03 13:36:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| cd95f168-0bc4-3495-9459-f9d18a5e732b | -11.1579 | -45.9551 | 2024-10-03 13:36:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 222.7 |
| 3d99e517-400c-3b9c-b85a-739372586466 | -11.2758 | -46.9098 | 2024-10-03 13:36:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 8ee91947-19ef-3d22-85b9-769db6c48a0c | -11.551 | -63.7712 | 2024-10-03 13:36:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 72.0 |
| b298e1a3-4480-3412-b371-cb8ed4e1445b | -11.6243 | -64.0339 | 2024-10-03 13:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 41f649bd-a0bc-3a1b-936b-3b1b7dbe0940 | -12.0128 | -47.3486 | 2024-10-03 13:36:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 142.0 |
| a2f56654-32e7-33a4-b6b0-36dd4f2ee12b | -11.9671 | -50.181 | 2024-10-03 13:36:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| d8cd2f99-c4fa-3722-a324-6519705ab199 | -11.9737 | -47.3986 | 2024-10-03 13:36:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 3fd2d59a-465d-3c85-888c-6d98b6e5baf0 | -12.1406 | -50.0524 | 2024-10-03 13:36:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| b8b88d45-a874-3a44-a2cb-7cd2e78ee5ce | -12.3628 | -50.4772 | 2024-10-03 13:36:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| d9aff428-2abf-39e8-883c-e110942441ef | -12.762 | -50.5997 | 2024-10-03 13:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 7aec7d3d-aa25-3815-b1e4-c8804e924496 | -12.7812 | -50.5973 | 2024-10-03 13:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 80956d9c-fde8-3f0a-94ed-8b639a5276db | -12.9831 | -51.129 | 2024-10-03 13:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 00b5d7de-dad9-3828-9bce-fc08872a7ad6 | -13.1976 | -48.6489 | 2024-10-03 13:36:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 93.1 |
| c10ecfa4-b883-385b-957c-3de231cf3b40 | -13.198 | -48.6267 | 2024-10-03 13:36:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 261345f0-d398-346f-bec5-9f763591f0e6 | -13.0402 | -51.1432 | 2024-10-03 13:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 178.3 |
| 46f73f38-6e4e-34fc-9a92-62cad8dc0d93 | -13.0591 | -51.1623 | 2024-10-03 13:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| fb9fcbdc-95ff-334e-9968-a90074aaa622 | -13.0406 | -51.1218 | 2024-10-03 13:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 128.4 |
| ed88613a-9461-3d2f-b535-f5608b9701e1 | -13.5198 | -51.1252 | 2024-10-03 13:36:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| efde9f68-4391-315a-8631-61327892be76 | -13.5387 | -51.1442 | 2024-10-03 13:36:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 6a309e7c-b897-3340-b25f-0afbff8d45dd | -13.5195 | -51.1467 | 2024-10-03 13:36:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 118.6 |
| b8576a28-9cec-358f-bf74-5729ca7a8f0c | -14.0392 | -45.0947 | 2024-10-03 13:36:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 256.3 |
| d8bc2755-4b53-37b9-9fea-8b4c88facb5b | -14.6277 | -40.6982 | 2024-10-03 13:36:27 | GOES-16 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 98.4 |
| 79bdadcc-b373-36f0-b530-0ae625324034 | -14.8181 | -48.7598 | 2024-10-03 13:36:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 75.6 |
| fceca74d-3e03-308e-8656-8dd9dd53add5 | -16.1286 | -53.5189 | 2024-10-03 13:36:37 | GOES-16 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| d7b805d2-b021-3d58-8985-20eab32dc51e | -18.3079 | -43.2326 | 2024-10-03 13:36:47 | GOES-16 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 93.7 |
| f7927006-cb8a-3925-8f24-9d9b2a5a0878 | -18.8406 | -42.9235 | 2024-10-03 13:36:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 111.8 |
| 25935f28-bed3-3318-800e-56fb80f37a6c | -19.0344 | -43.1944 | 2024-10-03 13:36:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 208.4 |
| 0e1267df-7340-3d28-a763-a36d88696836 | -19.0141 | -43.1998 | 2024-10-03 13:36:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 141.9 |
| 4cea9521-c888-3b7d-914a-40e6a82ba108 | -19.0148 | -43.1749 | 2024-10-03 13:36:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 94.1 |
| 715f166a-ec2b-3fb6-ac47-eee1d8c49b26 | -19.0932 | -48.2876 | 2024-10-03 13:36:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 253.0 |
| eb95a503-4e85-39d6-b8e4-3543eca3dda3 | -19.2962 | -42.5779 | 2024-10-03 13:36:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 136.5 |
| 1467cfab-4421-373c-9726-fd95e68d57ff | -6.1325 | -44.9199 | 2024-10-03 13:45:41 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 45ab344c-a4f7-3185-8cdb-18611846642e | -6.3008 | -43.0351 | 2024-10-03 13:45:42 | GOES-16 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| c87c24d1-9143-3fa6-9420-dff5b3559af0 | -6.2968 | -43.4331 | 2024-10-03 13:45:42 | GOES-16 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 0f3d0c30-9974-3326-ae85-e8bd7a2bb48a | -6.4275 | -47.399 | 2024-10-03 13:45:43 | GOES-16 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| d7bd896b-760d-34c3-a656-ecda15b8d12d | -6.8885 | -44.3083 | 2024-10-03 13:45:45 | GOES-16 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 527ac507-1a6e-3165-a8e4-ac779fa627d3 | -6.8887 | -44.2853 | 2024-10-03 13:45:45 | GOES-16 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 258.5 |
| 9762d686-35fd-3f1c-a3f4-46db81097fc5 | -6.9075 | -44.2836 | 2024-10-03 13:45:45 | GOES-16 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 175.5 |
| e1496e94-ffd8-3bee-8bda-025276e348fe | -7.0752 | -48.028 | 2024-10-03 13:45:46 | GOES-16 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 6d349621-284c-302d-8006-c604e951f681 | -7.0364 | -42.8272 | 2024-10-03 13:45:46 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 73.9 |
| cf52edde-4c63-384b-a8c2-419366c40d54 | -7.0367 | -42.8036 | 2024-10-03 13:45:46 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 80.0 |
| f1a43717-0e4a-3f1d-93c4-656f495ae185 | -7.0175 | -42.829 | 2024-10-03 13:45:46 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 73.7 |
| f0a0115e-6a8d-3394-976d-234494aec19e | -7.2001 | -43.3283 | 2024-10-03 13:45:47 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.7 |
| 2e594fba-b51d-3af5-bb9b-cc9b8d079b37 | -7.6267 | -45.496 | 2024-10-03 13:45:49 | GOES-16 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 3d3b3915-5c01-3a70-99d8-af453124c3f9 | -7.6255 | -42.4362 | 2024-10-03 13:45:49 | GOES-16 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 65.7 |
| 2f21a736-a777-373b-bac3-7ba94e8614d5 | -7.6444 | -42.4342 | 2024-10-03 13:45:49 | GOES-16 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 86.7 |
| dc3645bd-9cc3-3366-ac5c-9a9a7a726113 | -7.6441 | -42.458 | 2024-10-03 13:45:49 | GOES-16 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 89.7 |
| c56285b4-29d6-3327-a6ac-f77f29705c4d | -7.8626 | -43.0969 | 2024-10-03 13:45:50 | GOES-16 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 140.6 |
| 1cd29475-a512-3f6a-b286-80b366b152d6 | -7.8629 | -43.0733 | 2024-10-03 13:45:50 | GOES-16 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 124.4 |
| e47c9614-2528-3739-bc13-8b13167438c0 | -7.796 | -45.48 | 2024-10-03 13:45:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| bcd44b9a-6b7e-3f87-966f-1939bec3910b | -7.8149 | -45.4782 | 2024-10-03 13:45:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 163.0 |
| 13f10431-c7f4-3a4c-8523-9a5f4e1eec78 | -7.7321 | -46.1393 | 2024-10-03 13:45:50 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 48.6 |
| c2cceaf1-9a73-35d1-8e90-434afbfdbcf1 | -7.8245 | -61.3709 | 2024-10-03 13:45:51 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 4dc7a107-734a-3623-a476-ed154dbab9e9 | -8.1756 | -43.719 | 2024-10-03 13:45:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 98.7 |
| ac3342aa-2d01-33d3-ab1d-10f03ccd0ab5 | -8.157 | -43.6977 | 2024-10-03 13:45:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 162.8 |
| 7a847b0a-5915-3bce-a13a-8f062b14cd20 | -8.1859 | -44.3901 | 2024-10-03 13:45:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 15878dd1-ba18-3c3c-bf6a-a4073f0aabb8 | -8.1937 | -46.8324 | 2024-10-03 13:45:52 | GOES-16 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 50.8 |
| b747908c-293c-3b97-829b-8cf152dc537a | -8.1567 | -43.7211 | 2024-10-03 13:45:52 | GOES-16 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 168.2 |
| 471077d4-0abd-3ce7-8ba5-227bd21a8ce6 | -8.1759 | -43.6957 | 2024-10-03 13:45:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 113.9 |
| ca6026a2-f9eb-3f88-a84f-84ea4e6d7dae | -8.4535 | -47.1181 | 2024-10-03 13:45:54 | GOES-16 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 0a33c6d9-1248-3f11-b444-9a7d7dd7a268 | -8.4347 | -47.1199 | 2024-10-03 13:45:54 | GOES-16 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| d4ea6fe4-0dcb-3f3c-8025-38e918f48520 | -8.4344 | -47.1421 | 2024-10-03 13:45:54 | GOES-16 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| b08ade79-8afc-3f64-a248-6033b8dac9e2 | -8.4259 | -46.2968 | 2024-10-03 13:45:54 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| b8027b0e-3ec5-388c-b0b0-20fa2ef786b3 | -8.4944 | -46.8479 | 2024-10-03 13:45:54 | GOES-16 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| daeb40e8-70b9-377a-8f77-5775a36336ed | -8.4256 | -46.3193 | 2024-10-03 13:45:54 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 44b8101b-02ad-3b53-a9de-57296c6eca24 | -8.6113 | -46.5243 | 2024-10-03 13:45:55 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 3000f786-b141-3e8e-ad7c-61658abc73eb | -8.4645 | -62.6745 | 2024-10-03 13:45:55 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.0 |
| bdb0a47c-ebaf-3cd5-921b-d1a5ad9ba672 | -8.7036 | -45.2061 | 2024-10-03 13:45:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| de455b60-cef0-301b-a04f-fb5d434e713c | -8.4646 | -62.6556 | 2024-10-03 13:45:55 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 8f2e14b7-5708-3982-8b49-c3528633a991 | -8.7225 | -45.204 | 2024-10-03 13:45:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.3 |
| ed901639-9948-3bf8-a94f-f795e0a7de69 | -8.8362 | -45.1688 | 2024-10-03 13:45:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 125.4 |


[Clique aqui para ver as próximas entradas](README215.md)
