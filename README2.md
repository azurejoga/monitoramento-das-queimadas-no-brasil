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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8f026ea-d98c-3e55-826c-bc5a83409c3f | -20.04185 | -43.19055 | 2025-08-23 00:07:00 | TERRA_M-M | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.2 |
| ad133d9d-4a7f-3556-90e8-79753a3322c7 | -17.59322 | -46.57086 | 2025-08-23 00:07:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 135.5 |
| f41deb02-5fb1-3974-9047-241da15af3d6 | -18.06415 | -47.88202 | 2025-08-23 00:07:00 | TERRA_M-M | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 22.9 |
| a667679f-88ad-372e-a0b0-f621c42c344f | -20.39352 | -45.62541 | 2025-08-23 00:07:00 | TERRA_M-M | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 078573f9-cb82-368d-85a2-7b67e377a055 | -17.27603 | -46.76951 | 2025-08-23 00:07:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 173.4 |
| a81417cf-e718-3737-9684-09456799514f | -18.9694 | -46.92297 | 2025-08-23 00:07:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 04e71612-f5cb-3f7f-afd6-97c6c8ccc170 | -17.34678 | -42.65823 | 2025-08-23 00:07:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 14.6 |
| d646b9fa-b32f-312e-8ffe-61af40ed717b | -22.16608 | -43.2742 | 2025-08-23 00:07:00 | TERRA_M-M | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 2a8c3586-1e40-3730-8192-c339106e4664 | -22.17805 | -43.28625 | 2025-08-23 00:07:00 | TERRA_M-M | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 17.7 |
| c914ff7d-6600-334b-a1be-5bbdd0892082 | -22.02949 | -44.0989 | 2025-08-23 00:07:00 | TERRA_M-M | SANTA RITA DE JACUTINGA | MINAS GERAIS | Brasil | 3159308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 178d4bcf-0c1b-313a-9797-74d68bc91607 | -18.27371 | -45.58423 | 2025-08-23 00:07:00 | TERRA_M-M | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 74887766-8fd0-32a3-b5a1-4fd0f3a96884 | -23.49368 | -46.00294 | 2025-08-23 00:07:00 | TERRA_M-M | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.1 |
| 7b77ccf4-e7e9-380a-9e1c-974fff0e684c | -20.86998 | -42.54274 | 2025-08-23 00:07:00 | TERRA_M-M | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 57.5 |
| e36aafc8-1ee5-33bf-a2c2-16843a2e3a09 | -18.30114 | -45.5419 | 2025-08-23 00:07:00 | TERRA_M-M | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 878a9ddb-8b5b-3ff6-9584-882a9d7938d9 | -21.96227 | -45.60406 | 2025-08-23 00:07:00 | TERRA_M-M | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| cda99b97-d540-3808-b8f5-c8f6dffa37d9 | -20.87967 | -42.54082 | 2025-08-23 00:07:00 | TERRA_M-M | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.5 |
| 8144464f-0fbb-3d7e-b4fb-248f8fb0283f | -6.79018 | -45.00053 | 2025-08-23 00:09:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 9ea87715-8da9-3514-931c-deb7d7255534 | -6.61101 | -44.56315 | 2025-08-23 00:09:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 692870d5-abfc-36ac-a23c-86add60a6827 | -7.02753 | -44.64142 | 2025-08-23 00:09:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 70d6a30e-4419-388d-87ba-a03a23ce0c6b | -12.54105 | -45.6202 | 2025-08-23 00:09:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 49315d40-01ee-3887-b2e2-4d8db92f1fc1 | -15.07073 | -48.49367 | 2025-08-23 00:09:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 41.8 |
| e3b594a6-04d4-37d3-8268-f1ba4e608ac7 | -6.58612 | -44.57238 | 2025-08-23 00:09:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| c80df1e9-3717-3a9a-9602-882808aa464b | -14.96555 | -48.67325 | 2025-08-23 00:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 40.8 |
| c13a45f0-8f5b-3b4c-b6bc-1790885919d3 | -7.03276 | -42.12439 | 2025-08-23 00:09:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 1513f0a8-ddce-3052-9baf-b4990ffca3e6 | -12.92794 | -46.17384 | 2025-08-23 00:09:00 | TERRA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 2d0b9419-cc01-31ae-ad25-d8673319519c | -6.50553 | -42.97272 | 2025-08-23 00:09:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0d82e265-f7c4-3bb1-a156-4b7f7c356605 | -15.26943 | -49.85528 | 2025-08-23 00:09:00 | TERRA_M-M | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 54ab4930-82d5-3e8b-b81e-25abd321e1b0 | -10.88101 | -44.17165 | 2025-08-23 00:09:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8852b822-89ae-3388-82b6-99dd13eaee06 | -6.42375 | -41.20434 | 2025-08-23 00:09:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| dfbdf5f9-f513-3402-afdc-be00d58ebcd6 | -9.87491 | -47.81049 | 2025-08-23 00:09:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 7eca283a-5c3d-328c-b33b-441f493772c1 | -6.78881 | -44.99024 | 2025-08-23 00:09:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 87005d54-5b07-36a1-8710-8818420c5b52 | -7.64518 | -46.28033 | 2025-08-23 00:09:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 5dc5644c-82f5-3f62-948b-84b551475486 | -7.02887 | -44.65133 | 2025-08-23 00:09:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| b3164fc3-381c-32fa-8167-98dd65242283 | -13.37773 | -47.5135 | 2025-08-23 00:09:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| f57f3c3e-de29-3366-912e-485acd5ec299 | -15.55853 | -42.69035 | 2025-08-23 00:09:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 2f980273-601a-3411-a387-4cc2c31be2f8 | -6.4355 | -41.22175 | 2025-08-23 00:09:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 15668f30-349c-3929-bd07-5117bb320937 | -9.64196 | -44.6076 | 2025-08-23 00:09:00 | TERRA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| a9e61cd9-1d03-30ab-a1db-84d9b5f40d56 | -6.57345 | -42.99327 | 2025-08-23 00:09:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3865751e-9108-3009-91e7-a8c6e303cdd3 | -11.98226 | -44.89151 | 2025-08-23 00:09:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 39396351-7e60-3557-a412-0ca08a4eebb9 | -14.96946 | -48.66758 | 2025-08-23 00:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 31596228-46f2-313a-8a53-04e3f6e6c886 | -12.96006 | -46.24831 | 2025-08-23 00:09:00 | TERRA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 5f1b53b2-e887-3d7c-9654-1eb3e04bc555 | -13.4656 | -47.04366 | 2025-08-23 00:09:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 5abce4ce-02f4-3d6d-b2b7-da8297f98d51 | -11.12988 | -44.77141 | 2025-08-23 00:09:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| eb5ea3e7-133d-3900-90e7-e6985ead8011 | -14.91243 | -47.99229 | 2025-08-23 00:09:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 28.1 |
| c6f012b3-5469-3a0e-ae06-dd1cdc7c3f9e | -7.07906 | -44.06828 | 2025-08-23 00:09:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7de5668f-8d47-332e-bd2f-e9a5b7107a31 | -14.9179 | -47.33096 | 2025-08-23 00:09:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 19.4 |
| ffabfd51-7bdc-32eb-8a8b-68a3f0615505 | -13.53195 | -51.50839 | 2025-08-23 00:09:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 37.8 |
| dff8c4e4-658f-3bfc-8c6c-3aef80d6bf40 | -11.43736 | -47.34385 | 2025-08-23 00:09:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 7a90d5fa-3da5-3f2e-bf14-1a4cb1a2f63d | -13.37429 | -47.49849 | 2025-08-23 00:09:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 21.8 |
| da545d1d-c973-3742-a730-ef0e728c10e7 | -6.60306 | -44.57418 | 2025-08-23 00:09:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 4bea8953-52c0-3a92-9fa6-d842b8e2bf3f | -6.41735 | -41.22441 | 2025-08-23 00:09:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| fba2b6f0-fd9d-3780-9cfa-618e2a38c8a6 | -14.91572 | -47.31217 | 2025-08-23 00:09:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 31.3 |
| c756c01e-6deb-3017-9550-3aa44066bd92 | -7.20997 | -45.31557 | 2025-08-23 00:09:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| fc032fe5-9e5a-355a-97fc-4aafe540da05 | -9.43831 | -47.64193 | 2025-08-23 00:09:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 9c3d4d21-a7c2-3ef0-ae39-77dc2e5b35d7 | -13.41837 | -46.26324 | 2025-08-23 00:09:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 00e896ea-e8ea-38d0-a810-526f0e261e5c | -11.44056 | -47.32021 | 2025-08-23 00:09:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| d5925a0d-c352-3eb9-85fa-6de65ee85506 | -15.52787 | -41.68631 | 2025-08-23 00:09:00 | TERRA_M-M | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 918536ac-001f-34f8-aa56-81fcb8599228 | -6.41602 | -41.21507 | 2025-08-23 00:09:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 86.4 |
| 4393d6ba-296c-32e5-8fbe-cf23c73c76de | -13.00494 | -45.23402 | 2025-08-23 00:09:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 5a49ad8b-de1c-35aa-86e3-d78982e5e682 | -7.00657 | -35.15972 | 2025-08-23 00:09:00 | TERRA_M-M | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 25.3 |
| c154ed31-0841-3a8d-9211-62336b2ce7c8 | -15.18917 | -48.232 | 2025-08-23 00:09:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 763f3091-d1e4-374a-8a2a-1c9f6c9d0245 | -13.17984 | -44.04337 | 2025-08-23 00:09:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 1b74951a-e96a-3372-8c37-460fd4788098 | -6.39973 | -44.29215 | 2025-08-23 00:09:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 95581d86-321e-37ce-b9af-f1e4a6067d6b | -15.70766 | -41.93241 | 2025-08-23 00:09:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 24e86382-94cb-3ffc-9ea1-9ddba7cb1c09 | -7.60512 | -46.29861 | 2025-08-23 00:09:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 34534241-fc91-3f88-a71d-82b736914c30 | -8.30372 | -47.27015 | 2025-08-23 00:09:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 1ca2f756-5731-3dfb-9109-6435ac14f46c | -9.45243 | -47.65749 | 2025-08-23 00:09:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 166.1 |
| d5a8b5cb-c036-3522-a008-455a44891a8b | -15.55722 | -42.68012 | 2025-08-23 00:09:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| f159728b-35f3-30e6-ae2e-2f8694ee2003 | -15.19824 | -48.24799 | 2025-08-23 00:09:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 82140140-d5ba-340e-a803-1bd3f3ae7a11 | -11.13066 | -44.76498 | 2025-08-23 00:09:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 608e41c3-3791-3d00-b06e-e20cc42132db | -6.98311 | -44.0402 | 2025-08-23 00:09:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a35cf988-bdb6-3bc1-9f13-772a2d65a3f3 | -15.06911 | -47.1567 | 2025-08-23 00:09:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 21.4 |
| de62cd8e-cc66-35d1-bec0-2175f0a1981e | -7.65284 | -46.28612 | 2025-08-23 00:09:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 0b1715de-a0a2-32c0-9abc-765fda48610b | -11.43529 | -47.32708 | 2025-08-23 00:09:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 393807d9-ad72-3537-8992-94510e2c41b1 | -6.60176 | -44.56443 | 2025-08-23 00:09:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 7377521c-6445-357e-a029-8aed813bbba7 | -15.70639 | -41.92294 | 2025-08-23 00:09:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 66e70555-0992-3e55-9fe4-b8d6c6a1e97c | -8.54488 | -48.85118 | 2025-08-23 00:09:00 | TERRA_M-M | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 14.7 |
| eaf70375-8c40-31af-86ca-c7dc9e00e316 | -13.22566 | -42.08461 | 2025-08-23 00:09:00 | TERRA_M-M | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 36d411af-ebb8-3550-805f-3c791af39cf9 | -7.46988 | -44.90695 | 2025-08-23 00:09:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4194b8ef-bc66-38f0-a637-497dd390f563 | -13.03809 | -46.32499 | 2025-08-23 00:09:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 6600cb2b-b1df-3b25-91e5-30473162f9a5 | -6.71122 | -43.19381 | 2025-08-23 00:09:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 6.5 |
| dd4f2674-ef2f-3d57-ac8e-1f2f6f0d6ac0 | -10.88235 | -44.18204 | 2025-08-23 00:09:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b1a48a45-d11c-3cdc-81a9-622a6d10889c | -15.904 | -42.3046 | 2025-08-23 00:09:00 | TERRA_M-M | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 427f0843-bb1d-3a09-8d24-8522a11f709b | -15.06279 | -48.47677 | 2025-08-23 00:09:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 45bbe049-930a-319f-a96d-2ee116729a67 | -11.97194 | -46.77511 | 2025-08-23 00:09:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 8c02b3eb-180d-3d39-ab6a-d430bff7a488 | -6.59537 | -44.57118 | 2025-08-23 00:09:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 08d4d236-0377-33ca-8090-9a4f24187c98 | -6.43417 | -41.21241 | 2025-08-23 00:09:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 9b93854e-d5ca-3844-8633-8c2996e1616c | -11.1321 | -44.77636 | 2025-08-23 00:09:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 9fb57ae8-70dc-385a-97dc-bd7281215b16 | -11.05891 | -44.61064 | 2025-08-23 00:09:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| c43be00e-1a28-31bd-8137-227306aa37fc | -15.19582 | -48.2247 | 2025-08-23 00:09:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 0b7a6c83-8386-32b0-a002-f188b3d5f45a | -6.43054 | -45.5314 | 2025-08-23 00:09:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c9265f58-e28c-3e41-8a75-fa8115b864d2 | -14.91826 | -47.32503 | 2025-08-23 00:09:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 650593ca-9f38-317c-8aa4-7b0606943d8f | -12.5427 | -45.63371 | 2025-08-23 00:09:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| f3043c65-264e-3d5e-b1b0-cef16904ff10 | -15.07329 | -48.51786 | 2025-08-23 00:09:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 30.2 |
| c7c49861-2454-31ca-bcae-a58444f405be | -7.21968 | -45.31431 | 2025-08-23 00:09:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 23b4f794-4ac7-3680-819f-3c274ebbc7c9 | -9.44046 | -47.65911 | 2025-08-23 00:09:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 870d3ea8-1f97-34c9-a66f-f1c88d315a1b | -13.0033 | -45.22112 | 2025-08-23 00:09:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 82bd2917-3d4b-3fc6-8b44-cf304b3fd2db | -12.78888 | -48.72209 | 2025-08-23 00:09:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 35.8 |
| bbc37dbc-4b1a-3e52-af20-57ab76b378b1 | -7.43726 | -45.41669 | 2025-08-23 00:09:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 67438f50-a844-330e-9d20-05344fb7a6af | -15.06801 | -47.16336 | 2025-08-23 00:09:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |


[Clique aqui para ver as próximas entradas](README3.md)
