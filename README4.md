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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 647a988a-b3be-37cc-8fe1-4008c9705bb4 | -7.7632 | -45.210602 | 2025-08-03 00:18:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 62117dfc-1eb2-3dba-a9d1-325fe049f299 | -12.6194 | -44.493301 | 2025-08-03 00:18:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ab284643-ed8e-37b3-936b-a3e8fc2fe3a7 | -19.9786 | -45.783401 | 2025-08-03 00:18:00 | METOP-B | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8a5552d1-134e-372b-8396-bd34b3f59a6c | -7.5416 | -46.293701 | 2025-08-03 00:18:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9142a51c-527b-3ca2-8ccc-5004917a5751 | -12.6314 | -44.5 | 2025-08-03 00:18:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 46ea3bbc-4c96-35c8-b7ad-02b42894d958 | -10.4381 | -50.274101 | 2025-08-03 00:18:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 048e0514-4cbc-3ed3-a53c-3b663a503750 | -7.9852 | -43.195999 | 2025-08-03 00:18:00 | METOP-B | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 225037d4-9075-3e5b-89b5-46474d9d1a67 | -14.3601 | -50.3269 | 2025-08-03 00:18:00 | METOP-B | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a03cac7f-9342-3a35-b040-746ec184ce92 | -18.7617 | -47.469799 | 2025-08-03 00:18:00 | METOP-B | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 05a04abe-cd78-3c30-995e-c935dc54bc13 | -8.0053 | -43.1511 | 2025-08-03 00:18:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 49653fb1-1a1b-3e80-bbcb-3a42effb25c2 | -14.1408 | -45.430099 | 2025-08-03 00:18:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e024d275-1848-3589-82ad-33f391c703e3 | -7.8665 | -45.5196 | 2025-08-03 00:18:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 39a3bc7f-b40e-3fb8-b6b5-49d000681243 | -12.6509 | -44.495201 | 2025-08-03 00:18:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ecf412b6-b22b-3302-b557-59d2825ca7cc | -12.6635 | -48.0952 | 2025-08-03 00:18:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c63f2dd6-f227-363d-a7b7-f9f3dd27a4d1 | -18.912201 | -46.787498 | 2025-08-03 00:18:00 | METOP-B | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b138c1e5-6e7a-39b1-9501-419a3a88c9d6 | -6.3372 | -46.1675 | 2025-08-03 00:18:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1462377f-2d0b-3159-92d5-7816333494d4 | -21.6936 | -47.693501 | 2025-08-03 00:18:00 | METOP-B | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9ec4b7bf-e5e6-31a5-8c9c-882b5ec4b255 | -5.9027 | -50.004299 | 2025-08-03 00:18:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27a7068a-0a03-33d0-a980-7dd9493e354d | -7.0078 | -59.822701 | 2025-08-03 00:18:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6bb4e12f-389b-37f4-b526-8f04459a4186 | -9.441 | -57.8246 | 2025-08-03 00:18:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 169fd185-92e6-3c86-9340-aa53cb0302ac | -7.9956 | -43.1534 | 2025-08-03 00:18:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4b4003ce-8e34-343d-be1b-2b7a083c20ca | -7.9822 | -43.183399 | 2025-08-03 00:18:00 | METOP-B | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 030cca99-01c8-3fa0-a983-e2eea0bb0fa3 | -7.1039 | -44.077202 | 2025-08-03 00:18:00 | METOP-B | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c457894c-112b-3ad7-a1db-f0dd98740c13 | -2.2682 | -47.872299 | 2025-08-03 00:18:00 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18aa1acf-6c11-3965-a335-b8b620758f70 | -16.1096 | -46.873402 | 2025-08-03 00:18:00 | METOP-B | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7ba12d1d-542e-36fc-af8a-b599844533d1 | -8.1013 | -49.7533 | 2025-08-03 00:18:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61ff085c-6244-3b53-a14c-f752c39b51c9 | -12.6412 | -44.497601 | 2025-08-03 00:18:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 69c14939-11f2-3559-bd38-9d5fa0405d02 | -13.6675 | -41.373501 | 2025-08-03 00:18:00 | METOP-B | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 737d2813-ae53-3d0f-bd3e-b069ce1aaafe | -7.9474 | -45.116901 | 2025-08-03 00:18:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9c1c078d-16fe-3998-945a-ce00554eabfb | -9.4373 | -57.805901 | 2025-08-03 00:18:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4a0f7395-3383-3a66-bb23-3412ad553608 | -6.6299 | -59.068001 | 2025-08-03 00:18:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1bfa87a2-60c3-3bfe-889f-96fd438e6483 | -12.6097 | -44.495701 | 2025-08-03 00:18:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0c26c7dd-c03f-3b39-a2ef-3efa50c83cd0 | -22.0068 | -47.5718 | 2025-08-03 00:18:00 | METOP-B | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| adcb5b57-f518-3962-aa98-94569271f94c | -12.6357 | -44.518101 | 2025-08-03 00:18:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8ecadfb0-e2c4-39ac-87dc-0d907bf7b6ec | -8.0059 | -43.1106 | 2025-08-03 00:18:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 30757b0c-4a4b-3cc4-81b7-cd2ddc4b24d1 | -12.5999 | -44.4981 | 2025-08-03 00:18:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9530c546-2622-3de1-8858-0e30b21a7d92 | -8.9146 | -46.7463 | 2025-08-03 00:18:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e323822a-2535-3ba0-b88a-adaafac815cb | -16.8097 | -42.866699 | 2025-08-03 00:18:00 | METOP-B | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ce1e1fb7-eeda-3881-bb73-51d8eba22992 | -7.9925 | -43.1408 | 2025-08-03 00:18:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e34e18cb-225b-3c61-9be4-ea2fd4ce12ee | -10.4479 | -50.271999 | 2025-08-03 00:18:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 105c3b95-3a22-39ce-a0cc-82913f89303b | -21.691999 | -47.685799 | 2025-08-03 00:18:00 | METOP-B | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a78c4192-c664-3e2a-9663-6cb20dfd4068 | -7.9376 | -45.119202 | 2025-08-03 00:18:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 505fa4fa-ddb6-362c-84d2-00d8f3b9cd7d | -8.0089 | -43.123402 | 2025-08-03 00:18:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a49b9457-db3e-3cca-9345-8e21dfa19772 | -18.816401 | -46.444901 | 2025-08-03 00:18:00 | METOP-B | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a6bd9206-b63f-39bd-a1d7-f1a232a6bd7b | -18.818001 | -46.452202 | 2025-08-03 00:18:00 | METOP-B | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| df65f169-68f0-37e7-aa95-b941ec16d933 | -12.6455 | -44.515701 | 2025-08-03 00:18:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0dbb257d-f189-3c83-8638-d798dfc61b97 | -11.7917 | -44.923 | 2025-08-03 00:18:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b5354e12-27ec-3b36-b0c7-5d517670e55b | -8.5655 | -49.526402 | 2025-08-03 00:18:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a46b4120-f4cf-3489-85ed-32d924ff196c | -15.5868 | -46.518799 | 2025-08-03 00:18:00 | METOP-B | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cd744b28-fe00-3b88-b77b-0c8099d74699 | -5.7013 | -44.503601 | 2025-08-03 00:18:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3f9b72be-0269-3711-b838-7cad075961e8 | -7.4935 | -49.751301 | 2025-08-03 00:18:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57d8f065-5b60-3ec6-89bd-4816a7bc00d6 | -12.0191 | -44.0107 | 2025-08-03 00:18:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9a0e16f8-9d7f-3efc-8190-21906ce28269 | -14.1291 | -45.424599 | 2025-08-03 00:18:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 273f6306-cadf-317a-85aa-533443fd98cd | -12.6292 | -44.490898 | 2025-08-03 00:18:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8c34331e-afea-3da0-a142-2323be76ddff | -7.9725 | -43.185799 | 2025-08-03 00:18:00 | METOP-B | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d5460aaf-53fb-3ccb-9d10-d3b21561eb47 | -8.0915 | -49.755501 | 2025-08-03 00:18:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 190425ec-877a-3379-a592-af3c14320396 | -6.6741 | -59.1746 | 2025-08-03 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| d877d4c7-afa7-3fa0-9e9b-0937fe07e347 | -13.6935 | -41.3685 | 2025-08-03 00:20:00 | GOES-19 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 52.2 |
| 27cad741-a192-3b2c-aa85-d520ab682ef8 | -22.029 | -47.5843 | 2025-08-03 00:20:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 99.7 |
| fa92e3b8-e92d-3506-92d8-0d643bfe5d49 | -4.3197 | -48.0908 | 2025-08-03 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 36623cde-c0b1-369e-9566-cb51cde49a87 | -8.0324 | -43.1022 | 2025-08-03 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.6 |
| 565c2b0d-5e8b-3192-9a26-58070ac495f8 | -12.6789 | -44.4851 | 2025-08-03 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 3bc03dd0-abdb-3aa8-b080-e5e17e55c9c3 | -22.0297 | -47.5605 | 2025-08-03 00:20:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Cerrado | 81.5 |
| ada76d0e-b213-3ddb-af28-4f8a680441bd | -12.6595 | -44.4882 | 2025-08-03 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 192.8 |
| 2e52da69-c746-317c-89dd-dd8fc7124608 | -12.6398 | -44.5148 | 2025-08-03 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 3ee545ad-7d69-38e9-98d0-3c38acabc0d4 | -12.6402 | -44.4913 | 2025-08-03 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| cfc3c9bd-f44b-3af7-aacb-2902c9345ef0 | -12.6591 | -44.5117 | 2025-08-03 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 60547415-8e0d-3e0b-9a9e-144005024585 | -4.3196 | -48.1125 | 2025-08-03 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| a124e45f-2e23-35de-8770-231da4ef3d88 | -4.5684 | -44.2036 | 2025-08-03 00:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| f95c152b-18ab-3445-bcea-f78c28476ff1 | -18.8407 | -46.4417 | 2025-08-03 00:20:00 | GOES-19 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 98.1 |
| ab48c8fa-dd81-3b19-93bb-51c41013b961 | -6.6559 | -59.1174 | 2025-08-03 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 4af36359-973f-33b3-af4f-e41596c4240d | -6.656 | -59.0981 | 2025-08-03 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| d4a7fa22-1d09-3f37-b825-7a963eb68ad4 | -12.66 | -44.4647 | 2025-08-03 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 3293f2d8-a519-3af7-a727-e18610303855 | -12.6595 | -44.4882 | 2025-08-03 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 52b4e4d4-5eb6-3a7f-962e-7143f2a755f4 | -12.6591 | -44.5117 | 2025-08-03 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 61282faa-5718-3e69-8eba-0c7bd337e3a5 | -6.656 | -59.0981 | 2025-08-03 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 142.5 |
| 62dc32a9-1cd4-383e-85d9-5e56a9807632 | -22.029 | -47.5843 | 2025-08-03 00:30:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 1476939c-165d-39d0-beab-3aada436d3df | -7.0208 | -59.8346 | 2025-08-03 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 75fb5980-0ee6-3d25-9554-0c9c2a72c908 | -6.6742 | -59.1553 | 2025-08-03 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 642175c3-94fa-35e9-83e4-723e3edf9886 | -4.5497 | -44.2047 | 2025-08-03 00:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 05ebba08-fe96-33a5-a456-710aa251dfc2 | -6.6741 | -59.1746 | 2025-08-03 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| e7b5ee11-8700-3541-aaa1-4f1e4bd83bd3 | -7.0391 | -59.8531 | 2025-08-03 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| a888925c-f664-3a0f-a4c1-adc63f720057 | -12.6789 | -44.4851 | 2025-08-03 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.4 |
| b612f637-074b-3d56-8cd4-d7fc52fc71f9 | -18.8407 | -46.4417 | 2025-08-03 00:30:00 | GOES-19 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 5500e405-8272-3a70-a6f1-9185bd758899 | -6.6559 | -59.1174 | 2025-08-03 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 145.1 |
| dc3d024b-8a70-35f9-af8d-d1704dc0f3aa | -6.6376 | -59.0988 | 2025-08-03 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 64c5affc-d413-3f79-936f-e35228e7720a | -12.6402 | -44.4913 | 2025-08-03 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 14902508-c11f-390d-abc2-1c8d02399753 | -22.0297 | -47.5605 | 2025-08-03 00:30:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 9e57258c-b508-341a-b119-bcefff487c2f | -4.5684 | -44.2036 | 2025-08-03 00:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| fc4dca6f-660a-37e1-94c0-dd2dec16b3fc | -13.6935 | -41.3685 | 2025-08-03 00:30:00 | GOES-19 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 58.9 |
| 6c3ea192-a01d-34b4-94b3-f5b298a5671b | -6.6375 | -59.1181 | 2025-08-03 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 335ce07b-468b-37f3-8118-3dfaa0fec0b7 | -12.6398 | -44.5148 | 2025-08-03 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 38.1 |
| a439fe79-d818-3169-b7f9-91abe3ce07ab | -12.6402 | -44.4913 | 2025-08-03 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 95cad4ab-5482-3ec2-b924-1df61dffb7c1 | -4.5684 | -44.2036 | 2025-08-03 00:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 91e694a0-ad35-3979-ab78-664ea1b8e0c4 | -6.6375 | -59.1181 | 2025-08-03 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| b58427c7-8e84-3fff-b3bf-a4ae897e9075 | -12.6209 | -44.4945 | 2025-08-03 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| abfc66f7-16b4-3e3d-b220-bf010854aa2b | -12.6595 | -44.4882 | 2025-08-03 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 117.5 |
| ba9c1c11-8e4b-3039-9554-b4ba5b6b7368 | -6.6742 | -59.1553 | 2025-08-03 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| fb5414bf-bd55-3e0d-9516-9ca8482825cb | -12.6591 | -44.5117 | 2025-08-03 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| df06bd5b-df08-3392-8158-7a3079ddb60c | -12.6398 | -44.5148 | 2025-08-03 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |


[Clique aqui para ver as próximas entradas](README5.md)
