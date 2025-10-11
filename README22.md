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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3249810a-27b4-308c-9931-78e31208aae4 | -5.3255 | -43.0893 | 2025-10-11 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7c2ce8db-af0d-3dd3-84ff-36529f2c5d41 | -1.40524 | -46.70597 | 2025-10-11 04:32:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| caaa6c57-fd11-3f45-bdaf-cd5cf8457138 | -4.41039 | -43.47042 | 2025-10-11 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b862ef49-7046-3088-a3d9-1387a2c1fb19 | -6.75719 | -42.8246 | 2025-10-11 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 5f1c0932-f134-30b8-9165-dddbf7e47820 | -5.63147 | -42.69603 | 2025-10-11 04:32:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a70c3cf9-e06d-389a-b046-be5b622795bc | -6.10541 | -42.55666 | 2025-10-11 04:32:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 328b41cc-903f-339a-bbc5-32e10480caa5 | -6.43875 | -45.82084 | 2025-10-11 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29b20b6a-2b1d-3c25-a1ca-0de15fda9808 | -4.40979 | -43.46838 | 2025-10-11 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 60a7b0f7-ca24-345c-bcd1-49f386b388c4 | -3.52039 | -49.70371 | 2025-10-11 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 658fa72b-fba2-3bc0-a5ca-a3bc67236062 | -7.35081 | -44.79334 | 2025-10-11 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ade3013-54b3-3839-87a8-4684deb7f336 | -8.20976 | -43.33981 | 2025-10-11 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| dcce0138-8a77-3dc4-b9e9-e5c74ba97b1d | -7.40288 | -45.91706 | 2025-10-11 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c933ebe4-f945-3026-91d0-e6c666a150cd | -8.20729 | -43.32885 | 2025-10-11 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 969965f4-c704-31d5-b378-cbc79568934e | -4.14223 | -47.65615 | 2025-10-11 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb369c15-9bd4-3fca-aa24-6f58ffed860b | -6.89869 | -46.73562 | 2025-10-11 04:32:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 12edd76f-93d3-3f57-9ced-2d92a5b42362 | -7.40922 | -45.91796 | 2025-10-11 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ba706b57-4427-3a9a-ab5c-a61370c1c836 | -5.25494 | -50.90592 | 2025-10-11 04:32:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ba001193-3d44-3ded-bbc7-c43c65a8419d | -8.40379 | -45.08826 | 2025-10-11 04:32:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4901560b-6d28-3b70-bb5b-275253bd1c9b | -5.25856 | -50.90651 | 2025-10-11 04:32:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69bf3e60-91b7-3696-b7c4-965a935f88c5 | -7.80513 | -42.40855 | 2025-10-11 04:32:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2913eeb3-667d-334e-96cc-e1cbe8adcee2 | -8.21515 | -43.3586 | 2025-10-11 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0193187c-f5be-3344-b49b-887b37baf561 | -7.86484 | -44.4743 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ce24ea76-275e-305a-bd91-d213bb4e2fea | -6.43802 | -45.82479 | 2025-10-11 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2aa92d6c-d83b-3c50-9cd5-7c4b08fe9844 | -5.28635 | -44.88058 | 2025-10-11 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e50f1ca-ee3b-3550-a44b-a7aee914fb60 | -2.73771 | -47.14676 | 2025-10-11 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fa597e19-086c-3c71-9860-a4ce7f61bf1f | -6.16389 | -42.55397 | 2025-10-11 04:32:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 91def5e2-ffee-387e-9fea-d6141ae32b35 | -7.3858 | -45.17523 | 2025-10-11 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1ae99d45-af3b-3732-8094-31849520794c | -4.53834 | -38.46502 | 2025-10-11 04:32:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2716544c-ecc0-38fa-8460-2aa357bbe998 | -3.7801 | -44.10789 | 2025-10-11 04:32:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 032eb175-c1c8-3d5f-a3ca-1068df550948 | -7.77804 | -42.26329 | 2025-10-11 04:32:00 | NOAA-21 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 457aebcd-255a-343b-9e6d-962d37aea625 | -7.77378 | -42.26265 | 2025-10-11 04:32:00 | NOAA-21 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| aa1baaaa-8701-363b-a131-88d27579db5c | -7.81867 | -44.12573 | 2025-10-11 04:32:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83f82798-10a5-3635-8553-92ccaf1433c3 | -7.80569 | -42.40454 | 2025-10-11 04:32:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dc73ca78-8dbc-39b8-8c5c-f92563da83c4 | -4.83325 | -49.94454 | 2025-10-11 04:32:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03c974e9-6ed6-3b6b-95ad-c8c942567f76 | -7.34952 | -44.79494 | 2025-10-11 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9b4c6765-2a31-35bd-bba7-61bee87548fb | -4.07492 | -48.04125 | 2025-10-11 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c6643530-d096-32a5-8cab-40580774df8f | -5.96322 | -42.27934 | 2025-10-11 04:32:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6aed8b58-287a-3999-b900-bede91bfda5a | -8.40316 | -45.09256 | 2025-10-11 04:32:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50b69647-3039-3218-a07a-2598348c2007 | -3.84968 | -50.49983 | 2025-10-11 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cfb4fb41-0247-3e04-993d-7db89a1631c2 | -5.23986 | -42.98577 | 2025-10-11 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4e5ee55d-551a-3d30-8f3b-7b8c15b68870 | -7.46489 | -46.85924 | 2025-10-11 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 7b4c9f2d-8cdb-373b-9f30-45b4a90dd3a0 | -7.8592 | -44.48703 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e3117c1c-4b14-39ff-a048-663ac82ce74f | -7.12759 | -45.08447 | 2025-10-11 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9d7e8609-6b24-37d4-b2b4-f20eeeab6f01 | -5.7924 | -47.09164 | 2025-10-11 04:32:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88dbc17a-5c2d-30ea-add4-de6215a2a1fa | -6.94549 | -45.59996 | 2025-10-11 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4cf405ab-1595-339a-99f8-876807e489b9 | -7.80404 | -42.41648 | 2025-10-11 04:32:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1614eb1c-5d57-3f93-8014-93b39e620213 | -8.83316 | -44.41812 | 2025-10-11 04:32:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| faed870b-9176-3744-acaf-eb6a787425e7 | -7.54194 | -43.84662 | 2025-10-11 04:32:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6c90614f-c3c4-36d7-91ae-80c921527218 | -6.43002 | -45.83121 | 2025-10-11 04:32:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88df6f4c-3430-37d1-a89d-56d41551ecd2 | -6.94838 | -45.60436 | 2025-10-11 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ef6766d-1c9f-32af-8065-7a9e36475e91 | -5.28155 | -45.26686 | 2025-10-11 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4e8664d6-1df4-3456-b627-da6132244274 | -8.01367 | -44.45824 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 39a0b3d9-24bc-3a8b-a1b9-5d7d65317a32 | -5.8676 | -42.84123 | 2025-10-11 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b4fb7cb7-91cd-34d9-ade7-17dc67ee3ff2 | -8.49792 | -40.7552 | 2025-10-11 04:32:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7fff563e-2deb-31bd-a181-11ac863dfb08 | -7.38642 | -45.17115 | 2025-10-11 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f41a6a6-956e-39f2-89c7-16aa9cdebea8 | -5.48071 | -51.40881 | 2025-10-11 04:32:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59ac0bfc-b7cf-3635-9126-ed595cc63917 | -4.14499 | -47.66009 | 2025-10-11 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ae035bd-576d-35ef-923e-6d8944a7b2ad | -3.07128 | -49.2112 | 2025-10-11 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 116b7fbe-d202-3be8-8b62-64621eb5dd16 | -7.79784 | -42.39698 | 2025-10-11 04:32:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 84e83d06-def3-3272-a4cb-b33874f6ad52 | -7.5009 | -43.09994 | 2025-10-11 04:32:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a22f028e-62d2-31c4-8d3a-34621ccb355a | -7.49689 | -43.09931 | 2025-10-11 04:32:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cb97a777-e777-3c1a-a73c-ccf73112b57a | -8.16385 | -43.31886 | 2025-10-11 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 9e3f1d45-9f72-3046-9207-f598bd8cc892 | -8.19183 | -43.3229 | 2025-10-11 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 773531e1-3ea4-3a0f-bdb5-cc6e05d2821e | -6.04591 | -42.50809 | 2025-10-11 04:32:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2fdfb76f-0870-3d15-96b4-0733160ec731 | -4.15596 | -46.78589 | 2025-10-11 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d5618c0c-e46c-34ba-be4c-f67c45426f30 | -7.74848 | -46.66775 | 2025-10-11 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d494c5a7-187d-3eae-a4b5-fff0d0628401 | -3.40901 | -52.66117 | 2025-10-11 04:32:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 08f60b50-9a3b-394e-b3ec-572e0526a648 | -2.55259 | -48.39525 | 2025-10-11 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e25e4cd5-4a73-3462-ace0-5ee0484fc806 | -5.37432 | -44.99416 | 2025-10-11 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9dfaab20-6262-3bf4-99dc-1473a5be06d6 | -1.75601 | -47.17813 | 2025-10-11 04:32:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| addac07e-d4e3-393f-95c2-24f192a14670 | -5.97014 | -42.2612 | 2025-10-11 04:32:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c9bdcf5e-1c18-3fdd-87c6-f6d11aad3d59 | -7.78804 | -46.01268 | 2025-10-11 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4db81636-633a-31b8-8b2c-97ea58705df3 | -7.85507 | -44.46323 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 61c13779-5059-3a63-a47d-34f97ea874cc | -5.22216 | -45.6545 | 2025-10-11 04:32:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67309027-e44f-3738-adf4-557afcf29b71 | -6.43762 | -45.82839 | 2025-10-11 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| cfb21a13-a7b8-3ff3-94c1-75b9d1f8f1e9 | -6.04998 | -42.50877 | 2025-10-11 04:32:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 56354ef9-babd-32aa-828f-13cdb865859b | -5.41361 | -40.98396 | 2025-10-11 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| fe6c4824-8833-32b4-af37-57a239471a7e | -5.5879 | -42.99465 | 2025-10-11 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c72dea1e-179e-3c29-904c-e2da1b335fa5 | -7.79148 | -46.01321 | 2025-10-11 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7c9f068b-e85b-3ced-bf48-b978050df094 | -2.5537 | -48.38812 | 2025-10-11 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6d3ff68-0bf3-3cd0-982b-242e5eb07a7b | -7.67865 | -42.38475 | 2025-10-11 04:32:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 159d03b7-7ccd-3501-b3f9-273fc8943a27 | -5.85809 | -42.85043 | 2025-10-11 04:32:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 10a64b12-fb60-3e16-b1f3-5160d7a858fc | -7.87231 | -45.13866 | 2025-10-11 04:32:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6810e436-d062-303c-b0bd-478490fa5f9c | -5.68655 | -47.90437 | 2025-10-11 04:32:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b57a060b-de68-33f1-937c-c12d7f2b0e60 | -6.92219 | -43.58372 | 2025-10-11 04:32:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 277198d8-801a-3e14-a7d3-2191bdd7621c | -6.04128 | -42.5111 | 2025-10-11 04:32:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f18fcda0-7bf2-349d-801b-43c7057cccaa | -6.32531 | -41.59739 | 2025-10-11 04:32:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8e32dec9-1efd-391f-83ab-9990bf15e438 | -5.33757 | -45.56511 | 2025-10-11 04:32:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72dba9bd-6dc7-3f2a-8f6c-145ab7efc793 | -8.56978 | -44.61127 | 2025-10-11 04:32:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d285a470-ec21-3244-8910-260b320f7edf | -7.53535 | -44.60529 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f68b7418-7ce3-3653-a67f-e90374ece658 | -5.93779 | -42.27952 | 2025-10-11 04:32:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 61000ec2-1c44-3eef-8452-4e92554b2134 | -7.73902 | -42.41656 | 2025-10-11 04:32:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 79670140-c349-3a47-9dbd-3825d9a14df2 | -6.7379 | -42.16093 | 2025-10-11 04:32:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| aa96a859-1b65-3793-ab13-8a651771d06f | -5.42655 | -41.36764 | 2025-10-11 04:32:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 59bae209-6c18-3d2b-8ea0-869018ff5263 | -8.15034 | -43.32775 | 2025-10-11 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3bc3c801-3bfb-3476-b729-4024ee0b4ef2 | -13.25596 | -48.02255 | 2025-10-11 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c791896e-cce6-300d-a4bd-6aad1e2acf99 | -14.92454 | -46.77432 | 2025-10-11 04:34:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f5f618df-70b6-3457-81d1-75e44a2b0730 | -13.41407 | -47.27087 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8251ae62-f9f8-3441-bf47-80d33ac01326 | -11.24635 | -58.032 | 2025-10-11 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e7a0a76-7946-3d00-9b8b-af609147c714 | -8.58893 | -48.75012 | 2025-10-11 04:34:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README23.md)
