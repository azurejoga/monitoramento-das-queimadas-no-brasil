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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29aa88e5-41e0-3827-82db-5101e5f42037 | -13.42627 | -46.84682 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| af8d5b22-2df7-361d-9980-f007fdb81321 | -7.942 | -42.65369 | 2025-08-28 04:08:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b971381a-3f4b-36f4-8802-2b7e73281187 | -10.48936 | -51.58677 | 2025-08-28 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c446047-27e4-3ffd-8749-4f15bbaefde9 | -13.39484 | -46.86162 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6074f9cc-70f4-393f-b424-e0f204388487 | -14.14219 | -45.41061 | 2025-08-28 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a27fec36-2ee8-35f6-9f8f-0ce1f30272fc | -9.60161 | -49.02202 | 2025-08-28 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eab52918-0879-3de0-86d7-2d3bcc30bb96 | -7.73364 | -50.278 | 2025-08-28 04:08:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df89ac30-e2ba-37bf-a3ac-da1cbb615f81 | -9.6643 | -48.31554 | 2025-08-28 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd8a6d7d-5c10-3253-b88f-b47ade82cbcb | -8.29482 | -45.16322 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a16e4518-f6d8-3282-a29a-23f917c67aea | -9.19418 | -44.43451 | 2025-08-28 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f162c3ca-4525-3c9d-8608-57d54d4e5fb8 | -8.43774 | -41.44859 | 2025-08-28 04:08:00 | NOAA-20 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 57.1 |
| a523bd78-f54d-373f-9701-d195d0d94996 | -12.85888 | -48.10836 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e70dd3d2-9120-3532-899f-0add8670c6dd | -10.54011 | -46.68102 | 2025-08-28 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0bb78a32-af95-317b-a48f-2f534daefa7c | -12.67875 | -48.16192 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59b8457e-2d96-3356-8f16-a8efbabf8d60 | -12.92547 | -46.33122 | 2025-08-28 04:08:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9fe00290-089a-3e36-8d40-4cab91fed3dd | -13.5044 | -46.85638 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 732ff136-514a-359b-8386-aa18aba632f2 | -12.71785 | -48.17584 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c77c8f47-cb6e-327d-bede-3bcdfb3eb05f | -11.31958 | -43.5451 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3250f198-10b0-3afe-bce7-81735ea6ff55 | -13.54878 | -46.90018 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5cf66e02-da81-3f9b-9f8c-31b93564fde8 | -11.32738 | -43.5391 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23b44412-8023-312f-a3ab-a9fa0178abc2 | -7.94315 | -42.62508 | 2025-08-28 04:08:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5af20cb0-16e8-3d1e-9fd6-1603e5b6d2f7 | -14.54583 | -48.17813 | 2025-08-28 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f22504c7-857d-3960-a08c-2b7f53b4bbbe | -9.13501 | -40.55941 | 2025-08-28 04:08:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| be4786d1-42c0-3584-b323-b31fa9a5f440 | -8.44688 | -43.65811 | 2025-08-28 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1839476e-fed1-3367-b121-6d1edbefc6b1 | -12.67938 | -48.15835 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c71a5ada-4af0-33f5-92c3-8d6ca34cc871 | -12.93485 | -46.34181 | 2025-08-28 04:08:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8356119c-7ee0-391c-a124-54f418d94ba6 | -13.45953 | -46.85221 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9870bde-0ce9-36bd-9ea6-96c66394f75c | -10.53907 | -46.70997 | 2025-08-28 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea0aae7f-8719-3860-84f9-01c12cde6eea | -11.24456 | -44.97756 | 2025-08-28 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff3e4a93-cd65-32aa-9f8f-fd21804dc4c8 | -8.2804 | -45.1608 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 42.3 |
| a947899a-bb20-324d-ac4d-375758f444d9 | -11.93279 | -47.1383 | 2025-08-28 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db57d122-ffd8-32bd-9f90-79427e44c433 | -13.43407 | -46.97778 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c267888c-cd46-3111-8701-7db6abcadc4a | -13.17904 | -45.29288 | 2025-08-28 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4db6f563-f3b0-3745-93ec-612ee25a5a2a | -13.07731 | -46.34642 | 2025-08-28 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c6f17e28-daf7-332c-9b12-1d0b7c213e14 | -11.31625 | -43.54456 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c72d3d3-8c6e-32a7-9472-0581e402a80d | -11.79525 | -46.79256 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b38173e0-17aa-3639-9ecf-8ec2b112a004 | -9.19073 | -44.43392 | 2025-08-28 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| daff0fa3-ce9d-3caf-83e5-4244f25682c8 | -13.06138 | -46.35249 | 2025-08-28 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a8de625-69c2-31d9-bcb2-72ec93fd822e | -9.50927 | -46.70711 | 2025-08-28 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70cdc294-c889-34af-a3cf-2184b21fd41f | -13.52272 | -46.91868 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8bb1fad9-0be6-3315-b36f-eccc4c268f68 | -12.93197 | -46.33679 | 2025-08-28 04:08:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 322ab126-b310-3cb1-8517-a4b13beaee94 | -10.32686 | -46.77148 | 2025-08-28 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| beca90bc-2ba8-3d34-84ab-493f397d7587 | -9.4524 | -51.9464 | 2025-08-28 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a5b9d3d3-8553-3013-9198-a4f65715ddad | -11.56541 | -46.38741 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 40994ea9-b4f3-375a-ace5-8d3f9f83f336 | -11.22138 | -55.07279 | 2025-08-28 04:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2892a717-4b14-3f9d-9f27-a0e24a66ed95 | -13.42181 | -46.85061 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ad5e5898-dd74-3a80-b7c3-0b9da113ede6 | -12.5751 | -43.78801 | 2025-08-28 04:08:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc798eeb-49b1-38da-95d3-1f42be1a75ab | -13.07804 | -46.34216 | 2025-08-28 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c9208a9d-0dcb-3d6b-a840-c3b5bb0ef9c2 | -13.5352 | -46.93458 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87ecf179-00e1-3cbd-87f3-91370aa4a2c4 | -13.37599 | -51.77108 | 2025-08-28 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed3b841e-db58-3bad-ae6e-13574557913a | -12.81976 | -48.14317 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 408b6c4b-ce7a-3762-b9d2-434d6ff03c42 | -13.41861 | -47.02288 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0028ab7a-cb19-32dd-83c7-36a6a6776e81 | -10.71145 | -47.01902 | 2025-08-28 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ac3e3609-4803-366f-b8f8-d091ea18ec3d | -11.33298 | -43.52544 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0554478-6567-33ab-890c-d3abfba1dcd2 | -12.81704 | -48.11149 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6a32a532-f833-3730-8c52-7780f5bc66b3 | -13.45287 | -46.84679 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 96445769-6933-3901-8987-4d19f0d2a5ff | -12.92185 | -46.33062 | 2025-08-28 04:08:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a9a77bf6-41a4-3e35-afa5-2c7d29fbd2b8 | -8.29469 | -45.14169 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f5991285-ef24-3589-964e-b0ca0c3c799e | -12.79187 | -48.16033 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07a1ac57-439a-307c-a75e-26a4d0b012bd | -12.68774 | -48.18155 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9d2f39fe-af34-3415-9431-43b8c5d6b2f4 | -7.71607 | -43.96771 | 2025-08-28 04:08:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93373b3d-03cd-3a79-bd34-ee52aaa45884 | -14.13102 | -45.39288 | 2025-08-28 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 941e3da4-9f17-37e4-ab1e-c4aa7c5242f2 | -10.59849 | -55.40448 | 2025-08-28 04:08:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9ceaa25-03da-3911-be01-9854336efaf4 | -12.81913 | -48.14674 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e88433b-7979-3101-a26f-9be154271a0f | -9.66287 | -48.30782 | 2025-08-28 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7bca6008-6661-3b30-9bd5-49f28ee615f7 | -8.27542 | -45.16846 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 141.5 |
| ae0b8e29-e107-314f-a405-efff2fbbec00 | -8.28761 | -45.16199 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 775ca12d-436c-3bcb-b66e-9097c292a52c | -11.33631 | -43.52599 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cfe2398-d1b7-37d7-9b0f-0ec5827e6dda | -14.24219 | -48.02675 | 2025-08-28 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1cf4b88f-abaf-3158-aec2-f942de113064 | -13.37301 | -51.76683 | 2025-08-28 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 101dd695-3645-3b02-9604-6851e206d0b2 | -13.42419 | -46.99069 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ff460111-6c77-398e-ade3-1b76e15f6861 | -12.77399 | -48.16751 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 09d9e172-95fd-37cd-9cae-1e50643e8ec6 | -10.52845 | -46.70334 | 2025-08-28 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8dd43388-15e4-36d3-8abc-4aa3ddac9784 | -13.45346 | -46.97624 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 727d1ce8-ecd6-3d0e-ade4-ac36dd4e1742 | -11.55896 | -46.33651 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| b20a43dc-60cf-3a0c-bb1f-5e9ad2776f2d | -8.27819 | -45.15189 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c2d7f6bf-fe76-3677-a209-a86440107a87 | -13.54296 | -46.88981 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fb21523f-dc28-3381-aed2-3b891f4bbe8c | -12.40306 | -46.49093 | 2025-08-28 04:08:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c32f076-3cad-3aa8-9672-6c1df8e04617 | -9.4572 | -51.95107 | 2025-08-28 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 58ecfe67-f1be-3081-aa2c-3cd65d454542 | -13.63498 | -48.24395 | 2025-08-28 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a5f32dd-48f5-350f-84ba-6457e4ffe007 | -13.08025 | -46.3293 | 2025-08-28 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b5d9dbac-5d07-32ea-9852-fc7e67d93626 | -12.6775 | -48.16894 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 41643590-425f-3289-b1b7-24c79b9a3722 | -6.8774 | -43.5919 | 2025-08-28 04:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 69.3 |
| fc5bca0d-99fe-37a9-af73-90897a032c34 | -6.4355 | -44.5764 | 2025-08-28 04:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 31a34f0c-db24-3972-b4d4-e2fc56e4dfa7 | -9.406 | -60.5711 | 2025-08-28 04:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| e2772e31-489a-3daa-911f-9468fede6994 | -8.9479 | -65.9616 | 2025-08-28 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 756e9ac8-26c5-377f-b3de-7754e49d8b30 | -8.2705 | -45.1605 | 2025-08-28 04:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 4c30113e-129e-3fd3-b4ed-cf7aa8ad6a7a | -9.1339 | -65.788 | 2025-08-28 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 150.8 |
| 35aa6d6c-686f-378f-a80e-670f28b18ee2 | -10.4736 | -57.9563 | 2025-08-28 04:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 71fa5f26-749a-3cad-b3c0-3d5f1414973c | -8.289 | -45.1814 | 2025-08-28 04:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 3a8cb63c-1bbe-317e-b856-c3aae4595ceb | -9.134 | -65.7694 | 2025-08-28 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 57e00b6c-b683-3bc8-9b99-e9b4d3a758be | -10.5375 | -46.6894 | 2025-08-28 04:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 218.5 |
| abc1bc5d-5f31-3678-89e0-0661ec1e5156 | -10.5371 | -46.7119 | 2025-08-28 04:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 34e61f2b-63b9-3470-b4fb-8cd22d6a02fa | -9.1154 | -65.7886 | 2025-08-28 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 210.1 |
| bc43fe55-4419-3019-82f2-343bd3db1820 | -8.2896 | -45.1357 | 2025-08-28 04:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 103.2 |
| acf53d1d-5a9a-379d-8dbb-6349a5b54775 | -7.3955 | -39.6845 | 2025-08-28 04:10:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 47.6 |
| 69aa17f4-1419-3aa2-ab4b-d3060440f35d | -8.3082 | -45.1566 | 2025-08-28 04:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 8e985df1-13e3-31c6-87c2-c7fee361d968 | -6.8772 | -43.6152 | 2025-08-28 04:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 4aa9e5d5-9a6c-3160-ad72-a651be356a1d | -10.5184 | -46.6917 | 2025-08-28 04:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 176.2 |
| 489ed9d2-c87b-33db-9d33-9ce670c82643 | -10.5188 | -46.6693 | 2025-08-28 04:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |


[Clique aqui para ver as próximas entradas](README44.md)
