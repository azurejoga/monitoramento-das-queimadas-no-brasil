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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0143ec1c-1f04-34db-9df1-06807706b9a9 | -4.87363 | -48.88199 | 2025-09-30 05:06:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e34b9895-843b-3674-a0de-f2699dc628d8 | -5.52897 | -46.38346 | 2025-09-30 05:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51cc76af-2bab-33d6-ae3a-c1de8ef19419 | -4.51494 | -50.4516 | 2025-09-30 05:06:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 41a923a6-3b18-32ab-a5b4-1f16a2811b0f | -5.62713 | -42.83535 | 2025-09-30 05:06:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 86f4962c-6683-3e93-bd64-a9d2a3f488c3 | -5.8166 | -42.78434 | 2025-09-30 05:06:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f53cf6bd-243b-30c5-9c74-e6ae46b8c4ad | -6.29177 | -43.91942 | 2025-09-30 05:06:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 303a46b9-ef92-39f5-ba08-6bbf1e96f815 | -3.50491 | -53.4529 | 2025-09-30 05:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6b29454d-e0a5-3e41-b16e-67300a3be816 | -4.39085 | -44.40187 | 2025-09-30 05:06:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03bbdbc9-577b-357e-917a-963cf171c0b9 | -6.20433 | -44.21489 | 2025-09-30 05:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d08bf61c-f2d1-3a3b-9c4c-545aa5c44fd2 | -5.52657 | -46.38545 | 2025-09-30 05:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 36cbc1ca-c12f-3c1d-9fdf-346716ab73eb | -4.64233 | -50.67449 | 2025-09-30 05:06:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b0bd324-058f-3146-87b7-0d4e07b5e849 | -4.58281 | -50.69166 | 2025-09-30 05:06:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 25abcc64-a144-3603-9e93-6fee3502bd85 | -5.7474 | -42.66796 | 2025-09-30 05:06:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8dcdc213-f8d0-3c9d-99a0-34d14914a62f | -6.56312 | -43.4216 | 2025-09-30 05:06:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 22ca0fa6-4cd0-30c2-80f9-f5d25fecd71c | -1.29105 | -54.18694 | 2025-09-30 05:06:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 03159d95-2feb-3151-a625-e0f934265bb4 | -5.82189 | -42.78588 | 2025-09-30 05:06:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 288b7aa7-65b9-3259-a82c-bc106812a7ad | -2.25433 | -47.88939 | 2025-09-30 05:06:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d051a900-3db4-373d-b855-bf4c28d670a7 | -4.90104 | -43.46907 | 2025-09-30 05:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e38264da-45a1-3720-959d-ed45d6118242 | -6.46733 | -44.21287 | 2025-09-30 05:06:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 453271cb-c317-3b8c-955f-25406e93c927 | -3.09182 | -47.00984 | 2025-09-30 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 1f131afa-ec64-304f-b120-7deedde71ef7 | -3.45173 | -53.83399 | 2025-09-30 05:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bce2402-bdf2-3f1c-8285-46a6b31882f5 | -5.57502 | -44.85203 | 2025-09-30 05:06:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dc8725a2-97f2-3c9a-bd83-a2181dce41d8 | -4.86799 | -45.05745 | 2025-09-30 05:06:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6cf65fb1-5cac-3414-9325-d88888c54d3c | -5.24517 | -43.74312 | 2025-09-30 05:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81bb47f9-89dd-33b4-957c-d52df4cd6017 | -4.90138 | -43.4702 | 2025-09-30 05:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 5814dea3-c16f-3c34-954e-de39ace2eb5a | -5.23173 | -43.6996 | 2025-09-30 05:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1db3870-3e24-357e-a6fa-f40c9e4e6e03 | -6.43373 | -43.07903 | 2025-09-30 05:06:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7cf1b1e0-462a-33b3-b8b5-6086ee09aeaa | -5.05013 | -45.31658 | 2025-09-30 05:06:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8de4f35a-c989-3218-ac40-03ba966ca0d3 | -3.10204 | -47.00891 | 2025-09-30 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ea366148-bbd3-38a7-b27a-4de3eb211fdc | -5.22159 | -45.22742 | 2025-09-30 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b8f18bf5-cb72-3045-854e-94c3f0a7e985 | -5.03934 | -43.61174 | 2025-09-30 05:06:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6dd2f26a-66ed-3509-b956-dfbd62ca45c7 | -4.80734 | -50.73922 | 2025-09-30 05:06:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 973742b1-cc29-304f-a145-650fe22e4224 | -1.28882 | -54.17946 | 2025-09-30 05:06:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33e8730f-89e5-35d6-b63e-6185794a1d31 | -5.31383 | -44.79153 | 2025-09-30 05:06:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9fbfdbf-b5e4-304f-aa4b-59c517186abe | -5.03293 | -43.61073 | 2025-09-30 05:06:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6235bbdd-547c-3215-8fb9-ad30f8e3d5ef | -4.3982 | -44.39383 | 2025-09-30 05:06:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d542c58-cd36-3bfb-a6b9-060e7d694b3b | -3.85452 | -48.97256 | 2025-09-30 05:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| c7099877-e69b-3ba7-8b9b-9f6efd0b59e0 | -2.69129 | -54.76684 | 2025-09-30 05:06:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd7e8fea-fe82-36b8-bd9e-09d8eb7d3e55 | -5.47984 | -48.66128 | 2025-09-30 05:06:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e15e611d-8993-334c-a1d8-981e96e20aeb | -5.9114 | -43.70485 | 2025-09-30 05:06:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45cc1228-e19c-3799-bf78-ff30499e8462 | -3.50013 | -52.47132 | 2025-09-30 05:06:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 57bcd7d7-7d54-3b60-b6a8-8f0ee493a96f | -6.27426 | -43.65166 | 2025-09-30 05:06:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| efb42dde-73cb-34de-a7c0-47d9dd268169 | -4.2595 | -48.55512 | 2025-09-30 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 174a4350-7693-3aa9-9260-40cb93b0f80f | -3.09531 | -47.01945 | 2025-09-30 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8c037b02-a2f6-3ffa-9b87-1e8d9cd1cea6 | -4.89494 | -43.46909 | 2025-09-30 05:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 01bad0f2-fd43-3f99-b85d-fcb924edaa82 | -4.86846 | -45.0594 | 2025-09-30 05:06:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6269b5e8-4e02-3390-bed4-de3f7c9464eb | -6.21236 | -44.20304 | 2025-09-30 05:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ccbe37b0-f3c2-3c6e-b46f-ed962e9aa198 | -2.73935 | -48.67115 | 2025-09-30 05:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea474399-5e82-39e0-b2a8-c554a1df74a8 | -3.74534 | -51.38235 | 2025-09-30 05:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0249082f-1149-3fcb-8e61-c00b07c5cfb5 | -3.10677 | -47.01231 | 2025-09-30 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 914b5452-bd46-3da6-83a6-b87db65a60eb | -5.62492 | -42.83725 | 2025-09-30 05:06:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 80bba2d7-52aa-3337-8cf2-0d0c067c658f | -4.89421 | -43.47435 | 2025-09-30 05:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 0ffd8890-4367-3a38-96f0-fbed2c716609 | -3.54131 | -52.20506 | 2025-09-30 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50726f8e-ee5f-3823-bb49-59a4c7cad7ec | -6.21124 | -44.21126 | 2025-09-30 05:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 10af3145-7213-3b7f-b710-7686c89bb543 | -6.42908 | -43.0807 | 2025-09-30 05:06:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 27859b58-93f2-35e1-878a-0a03d1c9c839 | -4.39928 | -44.08717 | 2025-09-30 05:06:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 258e257e-fc18-3cf9-b01f-b9d55a009d54 | -2.93372 | -51.94277 | 2025-09-30 05:06:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9191c65e-94fd-3f0d-8712-1f83453a4aac | -5.2788 | -43.17063 | 2025-09-30 05:06:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8b814f81-0f48-3448-a95f-57f2562441b1 | -5.22099 | -45.23163 | 2025-09-30 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 29324761-30f9-3d49-8e17-8acf36513e72 | -4.25938 | -48.55334 | 2025-09-30 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 868c2b74-496f-3527-b149-0ba2baa74c70 | -0.90657 | -47.54617 | 2025-09-30 05:06:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 747263d1-a603-3006-83d3-4cd33a76cbaa | -6.09963 | -42.65783 | 2025-09-30 05:06:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 082dda71-a092-3191-9ebc-9d957b921a26 | -5.74623 | -42.88239 | 2025-09-30 05:06:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 54adba5c-9d08-3b51-86c0-2782be1795c4 | -3.25323 | -49.12828 | 2025-09-30 05:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3b4717ae-4904-3205-a612-93ef7611f93d | -4.88847 | -43.46812 | 2025-09-30 05:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7220dd28-b77d-3443-8e7c-c635b3015c07 | -3.10616 | -47.01532 | 2025-09-30 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 5835a305-70ac-36a3-8131-f8fb69505a8f | -4.07533 | -48.03894 | 2025-09-30 05:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83593b3e-eb71-300b-8c3d-2e98da945b5f | -5.91069 | -43.71017 | 2025-09-30 05:06:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4fd79d8b-18e9-3aae-ae6c-df148224238f | -4.39148 | -44.39748 | 2025-09-30 05:06:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ff9bf2e-0ace-3c60-b77f-c22ce37ffa2e | -0.09801 | -51.27438 | 2025-09-30 05:06:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 15bb5581-bfac-3f97-b5b4-84a4e3bfd024 | -3.55128 | -50.32608 | 2025-09-30 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2526057c-ca50-34a9-856c-6d600ebc0eea | -3.55179 | -50.32845 | 2025-09-30 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cc8a8949-e195-30f3-ad49-b028085ea873 | -5.23878 | -43.74218 | 2025-09-30 05:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01b192de-76a9-34dc-a397-dfc3001029c4 | -4.39756 | -44.39829 | 2025-09-30 05:06:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37a6bf05-4218-3861-a249-0a6fb0b32d1d | -3.09679 | -47.01075 | 2025-09-30 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 32141dbc-832e-32c2-a375-4493368cece1 | -3.09596 | -47.01642 | 2025-09-30 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 47bf82d8-c85b-3086-ac84-5883e7a8bc51 | -5.66561 | -45.30177 | 2025-09-30 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2ab0211-5111-3efe-9ce0-51221c3cede5 | -3.50136 | -52.46331 | 2025-09-30 05:06:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9cf5855c-e4ab-3cfd-82c7-1403955f4418 | -6.29879 | -43.81065 | 2025-09-30 05:06:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 45dee0de-dfa7-3695-bc44-e9ef3fc535ba | -4.86855 | -45.05342 | 2025-09-30 05:06:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 33accabc-1895-3d74-9fe4-20dba5d2baaa | -4.4007 | -44.07761 | 2025-09-30 05:06:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4d36c85-b2c2-3c4e-8c9c-7eca95821969 | -4.29257 | -48.27639 | 2025-09-30 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a04d3504-bf24-3e44-9d4a-a64175f7427f | -2.74049 | -48.67365 | 2025-09-30 05:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6bf0e07e-38a8-3d9b-a7d5-ed6d8ac7a550 | -12.85038 | -47.00816 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5fd57603-ef2a-34eb-b67a-bed0e088f30b | -8.87431 | -46.64176 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ba9382ad-807c-3cbe-abf3-09f3862a1833 | -11.71794 | -44.44222 | 2025-09-30 05:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fbe6d1e1-4352-38f7-9424-9af564edd63f | -11.28079 | -57.8709 | 2025-09-30 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6d77fad7-4aae-34e7-aba9-9092ca095033 | -11.17746 | -47.23351 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1739a46-1ef4-3a81-9eeb-94a4461099d3 | -13.39573 | -48.07441 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8f450a83-0cc9-33f4-a6b9-1635d6206817 | -6.74717 | -45.62601 | 2025-09-30 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8241bf92-0b39-3979-90c5-593dc3abfc8a | -9.51128 | -47.68937 | 2025-09-30 05:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcc4da81-fc58-3d98-b328-6810258133c5 | -13.38657 | -48.05991 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a276742-d296-3831-9d1d-8ca9dff2c873 | -10.40074 | -49.04408 | 2025-09-30 05:08:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec744a4d-293c-305d-88d8-b2e3c537623f | -12.22906 | -47.80129 | 2025-09-30 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| beb88ed4-5031-3c36-9c3a-454728b2b8b6 | -7.84399 | -47.25832 | 2025-09-30 05:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb03cef7-1efa-3e49-b182-4601c00ab75e | -13.36838 | -47.31409 | 2025-09-30 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b4cbbbeb-ee0c-3f57-bd49-05163b033a1f | -6.56081 | -43.42197 | 2025-09-30 05:08:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 5.3 |
| ce5c9e6a-b8da-39f2-8867-2c946e755604 | -12.83839 | -47.011 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e16d1d56-5c45-35cb-a24d-fcace2fca85a | -12.79432 | -46.88789 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00c35b9e-cab9-3ed6-b8f8-3162f58915c2 | -11.19581 | -47.2216 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |


[Clique aqui para ver as próximas entradas](README84.md)
