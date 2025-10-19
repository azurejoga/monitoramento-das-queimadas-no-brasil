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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 510ed95e-6f38-3de3-a3e2-32be66ccedec | -2.65562 | -49.52346 | 2025-10-19 04:10:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2ae5c1c-84e4-3f15-af5f-4ea4d14e2327 | -5.71566 | -46.46129 | 2025-10-19 04:10:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fec0a0ba-149d-346c-b26b-f83ba2a771a1 | -5.81763 | -42.51761 | 2025-10-19 04:10:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b9bbb326-738e-33c1-a048-3a711850bbb2 | -4.41946 | -40.16821 | 2025-10-19 04:10:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 398d25b8-c8bb-3977-83e4-6f45c03185ce | -8.08204 | -41.0727 | 2025-10-19 04:10:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 152fb50f-dd48-34ee-8626-f2071ce9cc5d | -4.98744 | -43.84631 | 2025-10-19 04:10:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2f80d45-6323-3745-bc02-b87ecfd96270 | -5.47758 | -43.02865 | 2025-10-19 04:10:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0149423b-101f-35d1-b90d-b56ffbf68a38 | -4.22951 | -44.68565 | 2025-10-19 04:10:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca4fcced-e69c-3a00-89de-4bb963f26270 | -4.14083 | -47.65779 | 2025-10-19 04:10:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0f5f216f-1b82-3c75-804b-2a3454baf10b | -4.85561 | -44.59962 | 2025-10-19 04:10:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a51912c8-9fda-3440-8994-7ee4f47148a4 | -4.24883 | -40.34645 | 2025-10-19 04:10:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 45e97641-bfa0-334c-8201-e2fb1f6caddc | -5.86421 | -42.35457 | 2025-10-19 04:10:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 22501465-f667-3341-b59f-48834da72c67 | -5.9916 | -44.15471 | 2025-10-19 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5fcad49e-7e20-394c-a2c1-38de1fcfe242 | -5.30814 | -44.8478 | 2025-10-19 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ec8b4e19-7469-3239-b70e-87ac4be8b78b | -7.46928 | -42.74356 | 2025-10-19 04:10:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0fce257c-a608-3001-bdb3-ab5088b58839 | -4.24492 | -48.56826 | 2025-10-19 04:10:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94b0fab0-15f0-353d-98d8-43ede682119b | -5.89623 | -44.76748 | 2025-10-19 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 839670ea-bd7c-3802-9859-13ee77af8d94 | -3.12451 | -50.21557 | 2025-10-19 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e06d9487-b212-37aa-9a12-d4feecb399a4 | -3.84688 | -41.77958 | 2025-10-19 04:10:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0badc6bf-adc1-3b13-811f-62b45e14b63e | -4.24137 | -44.68308 | 2025-10-19 04:10:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 912ca4af-6ef8-36a9-a68e-9cc3e2cab9f4 | -5.28201 | -42.52425 | 2025-10-19 04:10:00 | NPP-375D | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9dc06c57-2d37-3a21-82e6-e30c1e2ab562 | -7.12341 | -46.15606 | 2025-10-19 04:10:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ff7a3e81-f72b-385f-92c8-4d737bcec3b1 | -2.69802 | -49.56003 | 2025-10-19 04:10:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ebcb111-9f60-35d6-9176-c7692f4da19b | -3.03424 | -47.80938 | 2025-10-19 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b834e7ee-c762-372c-8059-3ad3e8333b7e | -4.96458 | -45.91165 | 2025-10-19 04:10:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| f6626933-d981-35e7-8199-8abeb7af9b44 | -4.96145 | -45.9146 | 2025-10-19 04:10:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9634c5bf-d7a1-3913-9850-e834401f27b4 | -5.77336 | -42.72996 | 2025-10-19 04:10:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| abf051d7-d371-3c1c-8656-0f13e9ac1f3d | -5.21403 | -43.7415 | 2025-10-19 04:10:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90574592-c0e8-3c31-8cee-a2a1a7ce5f65 | -8.02709 | -40.86458 | 2025-10-19 04:10:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d955202a-0c99-328e-b2df-02ce25efb36e | -2.6933 | -49.55592 | 2025-10-19 04:10:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 72517321-6fa2-3cf5-b1e1-e465f4b2a33b | -2.25484 | -51.91975 | 2025-10-19 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fc278bba-2618-358c-8fe2-d9eb7842ac2f | -7.30987 | -42.47263 | 2025-10-19 04:10:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| fca7ec2f-cd8e-3597-8288-3e94e1da11c7 | -6.31226 | -43.97757 | 2025-10-19 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 71cc2cd3-2ed7-319c-bddd-ecba482a25a0 | -7.08799 | -46.87772 | 2025-10-19 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fe66cd2-ea78-34e5-b6ff-09276c5d4d8a | -4.77597 | -45.8925 | 2025-10-19 04:10:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8c1497e4-e80b-373c-80fc-4759719b729f | -6.9608 | -39.63577 | 2025-10-19 04:10:00 | NPP-375D | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bc5470eb-4b01-34d6-89c3-119d38a4ea26 | -7.01359 | -41.99179 | 2025-10-19 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a89e7fe1-461e-362e-a9fe-df1d61966767 | -2.69961 | -49.5504 | 2025-10-19 04:10:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45136725-7a31-3898-af7f-afb69fe7f886 | -6.59232 | -45.87825 | 2025-10-19 04:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca3a44f6-78b7-38fe-899f-5ffbebeb157a | -5.86086 | -42.35405 | 2025-10-19 04:10:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 54efc436-7c82-3c20-aaa3-e99dc7a021f0 | -7.33357 | -43.86634 | 2025-10-19 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 12b63dd9-1c3b-3d4d-bad1-fd5707df5877 | -2.70014 | -49.5472 | 2025-10-19 04:10:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3fa2420b-bff8-3629-8ae8-3fdcddebc261 | -7.18159 | -42.21859 | 2025-10-19 04:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 47b1ee6f-a66f-3ca4-903a-a8fbdadf3ff7 | -7.35392 | -43.85011 | 2025-10-19 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 06e95c60-a3c7-39af-8609-0948f8f3cc6e | -4.85702 | -44.59114 | 2025-10-19 04:10:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0d80488e-88b5-353f-a8bf-d988f4087ee1 | -5.86249 | -42.76202 | 2025-10-19 04:10:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e51773d2-2343-353b-89d2-124ad7c195c7 | -5.89276 | -42.81112 | 2025-10-19 04:10:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 183f73be-2ed8-396a-875d-416c3b6a27d2 | -4.23994 | -44.69185 | 2025-10-19 04:10:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c86f69d-7ad6-32a2-919c-4e9ceb3b6543 | -3.05589 | -40.81643 | 2025-10-19 04:10:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9a8d78ff-f707-3eb5-983a-95c07ff043a2 | -4.24065 | -44.68747 | 2025-10-19 04:10:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34a77cb7-b9d8-3193-8f3a-ba5221f22e0d | -7.15881 | -42.38353 | 2025-10-19 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f6023af8-740e-3456-b31b-9b30cc10cb96 | -4.22725 | -50.63055 | 2025-10-19 04:10:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f3b15f7-986c-3e4f-8766-0a608032355d | -8.47045 | -39.51003 | 2025-10-19 04:10:00 | NPP-375D | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7c085c5a-f55a-3705-ad17-46fe90fd18e7 | -7.2009 | -42.19692 | 2025-10-19 04:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 0da0dbe9-8320-3cc5-8576-f24147fb3948 | -5.34007 | -42.90645 | 2025-10-19 04:10:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8d413afa-350d-38d8-91f7-daa7e6b28642 | -6.25342 | -43.5875 | 2025-10-19 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 208517d4-4d48-396c-b7ca-be3f74bd98f2 | -3.51461 | -49.93573 | 2025-10-19 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f4daaf71-f803-38c9-a060-37e777d05def | -4.53031 | -48.41187 | 2025-10-19 04:10:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9091aa6a-2e15-3ace-bd65-7286a151b705 | -3.39888 | -54.06508 | 2025-10-19 04:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58b430ed-3c98-3644-8612-fd0a83b6dd56 | -5.10218 | -47.79711 | 2025-10-19 04:10:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 423c92ff-a4d3-39a2-9935-08d79b4a3a92 | -6.08573 | -46.46087 | 2025-10-19 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e5c0bb5-e9ef-3814-9771-2b527994fe13 | -6.44051 | -43.92217 | 2025-10-19 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1f26d760-3b0c-319b-91dc-30f91aeedde4 | -4.85362 | -42.8899 | 2025-10-19 04:10:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50fc0feb-1628-3948-9425-63da9f165ac2 | -5.87991 | -48.18058 | 2025-10-19 04:10:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec843164-697f-399d-92dc-400c5260ef8a | -6.23247 | -44.1383 | 2025-10-19 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 94c920ef-21ea-30f3-ae67-65214120a6d1 | -6.06089 | -44.51649 | 2025-10-19 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70a3b0c8-04e0-304a-bf5a-395fef3d2523 | -5.36266 | -47.21151 | 2025-10-19 04:10:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0c1ed7c1-803e-3f28-8e14-6bdc5ae74bbb | -4.41204 | -49.76699 | 2025-10-19 04:10:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5819d35-e1bc-3db8-b4ec-d6d3645e5f9f | -5.30444 | -44.84722 | 2025-10-19 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e20f55ce-de96-3b19-a3a6-f7ed526a32e7 | -4.30088 | -49.66218 | 2025-10-19 04:10:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 372fb022-8736-3475-9137-f150acafd12a | -4.23394 | -44.68188 | 2025-10-19 04:10:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3401c43-0a49-3cfe-8308-32ff3007e016 | -6.68016 | -46.19463 | 2025-10-19 04:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba16ffef-9330-32c9-b0bf-f218485a6478 | -7.22747 | -41.17667 | 2025-10-19 04:10:00 | NPP-375D | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1bcc146a-15d6-306b-b4e5-b545435c8c43 | -5.69426 | -42.67651 | 2025-10-19 04:10:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d0893768-d86c-3343-a8d9-93d0d30632f2 | -4.00702 | -46.23964 | 2025-10-19 04:10:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38cecbbb-aeb1-32c2-9982-60861ad9fbe9 | -3.35156 | -45.45185 | 2025-10-19 04:10:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbbcf143-0ab5-3ec9-9863-093194f2baab | -2.98103 | -50.30021 | 2025-10-19 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35292595-b9b4-3102-9b9c-94135771bf12 | -5.60365 | -42.68048 | 2025-10-19 04:10:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 53f71157-dc23-348d-8923-13e64b131263 | -5.63949 | -44.80775 | 2025-10-19 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 21117cf5-d529-3df7-86b7-a978febd6314 | -7.16605 | -42.35952 | 2025-10-19 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f86b626b-425c-3ac3-a7ce-bbe7fd2987cf | -2.25565 | -51.91501 | 2025-10-19 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 047198a2-600b-384e-8e99-91a817889d49 | -7.15827 | -42.36544 | 2025-10-19 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 19e8ef01-3f08-3da6-bcf0-8edc41e59182 | -5.23769 | -50.95238 | 2025-10-19 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1849432-8ffc-3a0c-952d-a5d23c8af412 | -6.33364 | -43.28745 | 2025-10-19 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be51fe79-2590-362a-854c-3710960f85c2 | -3.161 | -49.16852 | 2025-10-19 04:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fcc8aab-f30e-3b30-a42f-aa97dc511e29 | -2.68442 | -49.54451 | 2025-10-19 04:10:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 55226ffd-22d2-3345-b247-95c24e0e6d3e | -3.11606 | -49.10428 | 2025-10-19 04:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 093a0242-30aa-3953-a2be-cd58d2a06817 | -5.31225 | -43.71244 | 2025-10-19 04:10:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2b45333-56c5-3d7a-9220-7d1b961e6d5f | -5.26737 | -44.8189 | 2025-10-19 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31a5e10e-d494-3179-8d08-ba53b1531ffb | -3.39781 | -54.07141 | 2025-10-19 04:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb515ed6-a0ec-32e8-a09b-faff990e8451 | -4.26948 | -48.88321 | 2025-10-19 04:10:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bd0028b-afad-3292-827b-fbab4878e567 | -2.91301 | -52.72936 | 2025-10-19 04:10:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 62edd91e-b8ed-3178-a82d-11e685608bc1 | -2.70235 | -49.86648 | 2025-10-19 04:10:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b6bf00ab-911b-3deb-be5b-0303570e7be2 | -5.41919 | -40.89006 | 2025-10-19 04:10:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fdc10ef9-6c4f-3136-8f46-0ddd66bc58b3 | -7.12725 | -45.7443 | 2025-10-19 04:10:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1529eb0-76a7-31c9-8f32-0a185b8a5a02 | -5.60529 | -43.64325 | 2025-10-19 04:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52566222-2306-3446-a354-1a250069509d | -2.25653 | -51.91563 | 2025-10-19 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2311af98-e68e-30b5-8bd4-20960c60efc7 | -5.33672 | -46.06326 | 2025-10-19 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecb1e8fd-0324-3ee9-82f8-f868efdd01bc | -6.17939 | -46.31921 | 2025-10-19 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 17addfd7-bdc4-32ad-9200-5b8a86f2966b | -2.91472 | -52.7193 | 2025-10-19 04:10:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |


[Clique aqui para ver as próximas entradas](README24.md)
