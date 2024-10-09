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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b00bfa90-b48c-3477-97db-461f7bc6bb94 | -17.007401 | -42.002602 | 2024-10-09 00:38:15 | METOP-C | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 953c347b-a4f1-3ac3-9000-6616d53933a5 | -17.598101 | -44.500999 | 2024-10-09 00:38:15 | METOP-C | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f601d206-83d4-3aa6-bb67-56a6b0c7d18e | -18.1784 | -48.124599 | 2024-10-09 00:38:18 | METOP-C | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 38d29c3a-78c0-358e-ba84-576e88eb3792 | -18.180401 | -48.134201 | 2024-10-09 00:38:18 | METOP-C | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 376aea81-9125-3c70-a850-91639f0ac046 | -18.1882 | -48.122601 | 2024-10-09 00:38:18 | METOP-C | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8bb8e56b-cba9-3d4d-8561-ff7df7ffbab4 | -16.653999 | -42.214699 | 2024-10-09 00:38:22 | METOP-C | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 617feff9-c338-3376-81e7-cb686baf795b | -16.655899 | -42.222401 | 2024-10-09 00:38:22 | METOP-C | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 01d734a6-c754-3d5d-a291-aace0c160141 | -17.101101 | -44.580799 | 2024-10-09 00:38:23 | METOP-C | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e21893f2-6217-3900-9756-14f17de18b9e | -16.485001 | -43.8097 | 2024-10-09 00:38:31 | METOP-C | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 14c246a7-106b-389f-a3c5-b08408b324db | -16.5334 | -45.273102 | 2024-10-09 00:38:35 | METOP-C | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| af762149-5936-396d-890f-6ac52da69986 | -16.534901 | -45.2803 | 2024-10-09 00:38:35 | METOP-C | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 904d8ac5-ce46-3431-83b6-4636b4eae0a0 | -16.536501 | -45.287498 | 2024-10-09 00:38:35 | METOP-C | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 48b72ee7-61c6-36c2-adf8-8e4c89b9f3d6 | -16.523701 | -45.275398 | 2024-10-09 00:38:35 | METOP-C | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e3a98cac-781e-338b-85b2-276080482607 | -16.5252 | -45.2826 | 2024-10-09 00:38:35 | METOP-C | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e72fe6c0-66a6-31bb-9c18-ce39fd931cc3 | -16.5268 | -45.289799 | 2024-10-09 00:38:35 | METOP-C | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3fac1dbd-15d0-39d1-b9a6-db13fa2f60be | -16.5154 | -45.284801 | 2024-10-09 00:38:35 | METOP-C | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 24ff6dde-2d61-3593-8b88-0c9326e9f5b7 | -16.517 | -45.292 | 2024-10-09 00:38:35 | METOP-C | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c79a950b-dbf3-3a67-8c0f-ae4e31d010e5 | -15.613 | -42.3587 | 2024-10-09 00:38:39 | METOP-C | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8b3117c5-7752-3ce2-9bdd-81f5bf914982 | -15.6148 | -42.366402 | 2024-10-09 00:38:39 | METOP-C | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7ea8cb65-4632-3722-a432-1044904de3d7 | -15.6032 | -42.361099 | 2024-10-09 00:38:39 | METOP-C | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2bcc3d7c-3405-36d2-9cfd-1df88d5f8634 | -15.274 | -41.626701 | 2024-10-09 00:38:42 | METOP-C | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1c88cbd4-1485-37f3-9694-8ee432bf1862 | -15.276 | -41.634998 | 2024-10-09 00:38:42 | METOP-C | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1ea6ca87-0e97-343b-8309-f791bc284ad8 | -15.2643 | -41.629101 | 2024-10-09 00:38:42 | METOP-C | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 54129b75-be2d-3809-8594-87d92879a200 | -15.2663 | -41.637501 | 2024-10-09 00:38:42 | METOP-C | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 695935f4-2e38-3338-9f7c-29b5b4424c4a | -17.322399 | -54.9874 | 2024-10-09 00:38:53 | METOP-C | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1b83e34f-3338-38ca-9cad-33dbe8e60f42 | -17.3083 | -54.963501 | 2024-10-09 00:38:53 | METOP-C | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f4cc9d47-627d-3f46-8aa0-fce925c36e68 | -17.3127 | -54.989101 | 2024-10-09 00:38:53 | METOP-C | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 42649eb5-8c64-3ff8-9415-9cceadc24e59 | -14.7833 | -42.830399 | 2024-10-09 00:38:54 | METOP-C | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 54de26ff-425b-373e-8852-cc8a960cb7dd | -14.785 | -42.837898 | 2024-10-09 00:38:54 | METOP-C | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 65d5da02-e9e9-3d02-85b9-693803a83c09 | -16.4918 | -52.852402 | 2024-10-09 00:39:01 | METOP-C | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9fe86d17-d905-302a-bd84-4b309a8e5add | -16.4951 | -52.8703 | 2024-10-09 00:39:01 | METOP-C | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ebe360f5-bb96-33db-9e47-b4c0acc0ce61 | -17.081699 | -56.8111 | 2024-10-09 00:39:02 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 80cd76eb-4de3-3035-893a-3af10860a5b4 | -15.7561 | -49.462898 | 2024-10-09 00:39:02 | METOP-C | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 024b9905-a7cc-3b72-b218-1697492b3a8c | -15.7582 | -49.4734 | 2024-10-09 00:39:02 | METOP-C | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 26d408e9-97f5-38d0-87ba-7b3f78ef70bd | -16.8962 | -55.7589 | 2024-10-09 00:39:03 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 59eda352-04a0-37fa-b799-1d7f91ffda09 | -17.0721 | -56.812698 | 2024-10-09 00:39:03 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4d6de3b2-f145-3c4c-96d5-900cdf0e592c | -16.8818 | -55.732201 | 2024-10-09 00:39:03 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 33b5dddd-d45c-38e1-a9d3-01062a2fc48c | -16.8866 | -55.760601 | 2024-10-09 00:39:03 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 295f0169-c51c-3802-9304-8aa63b2ab061 | -16.891399 | -55.7892 | 2024-10-09 00:39:03 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 613e84d5-3577-3ff4-b994-c9b89f2cce1e | -17.062401 | -56.8144 | 2024-10-09 00:39:03 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1ce5fdc7-c152-3179-9874-b2dd05e480fc | -16.8769 | -55.762299 | 2024-10-09 00:39:03 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c25d9575-e03f-35f7-a141-6463b767ae99 | -14.5122 | -43.8438 | 2024-10-09 00:39:03 | METOP-C | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3d5cd031-6faa-313a-8304-93d639e45ac9 | -14.5139 | -43.851002 | 2024-10-09 00:39:03 | METOP-C | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 80ac5240-f02b-323d-b3d2-ae09bc604d56 | -16.940001 | -56.731899 | 2024-10-09 00:39:05 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f6752ee4-2b1b-33f5-89a6-c2d071b31450 | -16.945499 | -56.765202 | 2024-10-09 00:39:05 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dbb198a4-8ae1-3dd9-a34e-089841386ac0 | -16.930401 | -56.733501 | 2024-10-09 00:39:05 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 07bbcfdc-6ded-34be-a439-1881ed5798e8 | -16.8713 | -56.675701 | 2024-10-09 00:39:06 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 842bd571-3d83-3ff4-a604-6a1672410f61 | -16.8617 | -56.677299 | 2024-10-09 00:39:06 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 577b6f52-4c09-38a8-b5c8-09b8b8ae6adf | -16.867201 | -56.710201 | 2024-10-09 00:39:06 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c2188669-610a-3933-beb7-d7efe687f944 | -14.1591 | -43.298302 | 2024-10-09 00:39:06 | METOP-C | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 110a9ac1-3c26-365f-ba3b-5ec9cdcb2cec | -14.1608 | -43.305698 | 2024-10-09 00:39:06 | METOP-C | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 51cc47d4-49ba-3dfd-a2c1-434744a06a1d | -14.8532 | -46.950001 | 2024-10-09 00:39:08 | METOP-C | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 26faac2f-7096-362b-8036-bbf974ae4536 | -14.8549 | -46.957802 | 2024-10-09 00:39:08 | METOP-C | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6890481c-630a-308f-b87c-4aa4c20adfce | -14.8565 | -46.9655 | 2024-10-09 00:39:08 | METOP-C | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a3e5aadf-4b62-327f-97f4-317b7fb1292d | -14.0342 | -43.5611 | 2024-10-09 00:39:09 | METOP-C | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2c02662c-6e86-3426-ab4e-a8acf991edc4 | -13.7774 | -42.420399 | 2024-10-09 00:39:09 | METOP-C | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ef000df1-e458-33c0-9d2c-d86369c2a6f1 | -13.9232 | -43.0396 | 2024-10-09 00:39:09 | METOP-C | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ee2feb35-7931-3d70-b489-78698985d298 | -14.2264 | -44.489201 | 2024-10-09 00:39:10 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9ab097e3-dc1e-3010-952a-994d74af043f | -14.228 | -44.4963 | 2024-10-09 00:39:10 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6cfad143-dd73-3a04-a386-16c17e8785c8 | -14.2296 | -44.5033 | 2024-10-09 00:39:10 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 89e89dbd-c5a9-38f5-b6a6-ed1e64358d26 | -14.0836 | -44.089298 | 2024-10-09 00:39:10 | METOP-C | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bb75d41e-9699-3b32-b752-067c5088084e | -16.403799 | -55.904301 | 2024-10-09 00:39:11 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2ca4f1d6-c15d-3623-b29b-1d176d262067 | -14.0852 | -44.141499 | 2024-10-09 00:39:11 | METOP-C | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e3974fd5-2d12-30a8-8b48-aa6356bfe46a | -14.0869 | -44.148602 | 2024-10-09 00:39:11 | METOP-C | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c2f983f5-cb06-34b7-a910-5afa489a6fe6 | -14.0885 | -44.1558 | 2024-10-09 00:39:11 | METOP-C | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0b80eeea-4485-3bfd-9838-9c7ad0401e10 | -14.0684 | -44.4743 | 2024-10-09 00:39:12 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3f2aded7-0e87-3961-bbae-f741cf4e3f31 | -13.892 | -43.794399 | 2024-10-09 00:39:12 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d6cb3607-bb63-3917-a5a7-f04c1e54682a | -13.8936 | -43.801601 | 2024-10-09 00:39:12 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5431d61f-e9d3-3db0-a7e3-a500c85b31e3 | -14.0668 | -44.4673 | 2024-10-09 00:39:12 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fe740084-0350-380e-a6f2-d67f6e1be47f | -14.0554 | -44.462502 | 2024-10-09 00:39:12 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 46491b4d-ef00-38b3-afb7-304ac22f62db | -14.0652 | -44.460201 | 2024-10-09 00:39:12 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| da9f9be2-6f51-35fb-8159-681386b01631 | -14.057 | -44.469601 | 2024-10-09 00:39:12 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5bac3c4a-698e-3cc7-8053-08d2781011e7 | -14.154 | -44.943802 | 2024-10-09 00:39:12 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c5f110e0-3622-3aab-9a62-9f992ce38b74 | -14.1556 | -44.950901 | 2024-10-09 00:39:12 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3a0310a1-a555-3b48-9c10-07569079fdd5 | -14.1395 | -44.924999 | 2024-10-09 00:39:13 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f12c5853-eeb2-3b34-af39-3a7ed0121d3b | -14.1411 | -44.932098 | 2024-10-09 00:39:13 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d1a3efb2-01e0-3613-9c16-2b5ec7f76b12 | -14.1426 | -44.939098 | 2024-10-09 00:39:13 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6b133396-28b6-3314-b790-8a8d354c2cba | -14.1442 | -44.946098 | 2024-10-09 00:39:13 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 85cbd9be-4a83-394a-b3d7-33e6b6f37e01 | -14.1458 | -44.953201 | 2024-10-09 00:39:13 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 172af906-6d63-32ea-acab-c9f94798ff48 | -14.1474 | -44.960201 | 2024-10-09 00:39:13 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4216ee4e-fad8-3aa2-9e33-31dde8df3c18 | -14.1345 | -44.948399 | 2024-10-09 00:39:13 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 594fed27-0270-3c5e-a8fd-2c35da88f31f | -14.1361 | -44.955502 | 2024-10-09 00:39:13 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8d5a0658-05aa-3307-b1f1-3f2188dc1929 | -14.1247 | -44.950699 | 2024-10-09 00:39:13 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 13d231b3-4354-396f-a2fc-e9a31cc9becb | -14.1263 | -44.957699 | 2024-10-09 00:39:13 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 15c8e5b5-c1cf-3deb-ac46-cb3745cf640e | -14.1279 | -44.964802 | 2024-10-09 00:39:13 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bf885246-0007-38c6-a5e6-e585ae4b2b5e | -14.1295 | -44.971802 | 2024-10-09 00:39:13 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0f82de4c-b979-3bac-9ff3-15f7c706fff6 | -14.1165 | -44.959999 | 2024-10-09 00:39:13 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d0faca2f-7f7a-315d-9db2-02fd61f7d81e | -14.1181 | -44.966999 | 2024-10-09 00:39:13 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4aab1293-d26e-395f-aebe-49587ae1af48 | -14.1197 | -44.973999 | 2024-10-09 00:39:13 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a6f4603e-a7ea-3f77-b1a5-601fef998f4e | -14.1213 | -44.981098 | 2024-10-09 00:39:13 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9a80508c-37ec-3200-8c02-ba135f03350a | -14.1067 | -44.962299 | 2024-10-09 00:39:13 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 53d968f3-64a9-359f-8f77-8025a9231474 | -14.1083 | -44.969299 | 2024-10-09 00:39:13 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7b88f83e-7c9e-3524-b16a-8c593141147e | -14.1099 | -44.976299 | 2024-10-09 00:39:13 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7f37ad82-aaec-3b1b-aa65-69d23f845876 | -14.1115 | -44.983398 | 2024-10-09 00:39:13 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f758ea8e-0843-3605-a067-dfb50b6c5912 | -14.2154 | -45.493401 | 2024-10-09 00:39:13 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f151b14c-c642-3196-845d-eda2d99449a7 | -14.217 | -45.5005 | 2024-10-09 00:39:13 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9e27092b-e01b-36e7-a634-598627fad301 | -13.8139 | -43.590801 | 2024-10-09 00:39:13 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bd962310-2927-3032-b13d-861c217858f0 | -13.8156 | -43.598099 | 2024-10-09 00:39:13 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0ddf59ae-f33f-3530-8d41-87adb234eb62 | -13.8173 | -43.6054 | 2024-10-09 00:39:13 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 093b9a1f-2dfd-3bc1-86d5-3cfecdf99388 | -13.8042 | -43.593102 | 2024-10-09 00:39:13 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README12.md)
