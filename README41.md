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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18f2e092-4bb6-31b7-83cd-6cdc1d05b6af | -3.17154 | -49.47789 | 2025-08-26 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 20c26718-c3a0-38f4-a499-40751abd8d44 | -6.06576 | -43.9993 | 2025-08-26 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b608608d-0fdf-38c9-9f7a-f1cd5e37d4e3 | -6.56681 | -44.217 | 2025-08-26 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3867d1a2-6e5e-33dd-af57-4acab8557eb5 | -9.26899 | -49.62205 | 2025-08-26 04:21:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a355a39f-bc0e-340d-8775-3b77643ce76b | -11.28856 | -44.99032 | 2025-08-26 04:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0886ac7-6d54-399f-8615-c9aae66f15c9 | -11.08787 | -44.77966 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee1fb261-710c-31ed-8ab6-03a0e597996c | -6.52048 | -44.57253 | 2025-08-26 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| eed31c8b-4dc8-376a-b3c3-aa9b3d47528a | -3.84529 | -47.80729 | 2025-08-26 04:21:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23671a7b-2cd5-3c62-9062-b1e3a2d2843f | -6.94537 | -44.1728 | 2025-08-26 04:21:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d694461-b083-3166-8d61-ef96e6c1db4f | -5.46409 | -42.5897 | 2025-08-26 04:21:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 61c0ae9a-663f-3def-a666-920060a1b80c | -7.58933 | -47.51577 | 2025-08-26 04:21:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd38cb2e-b50b-3c69-bde0-1789672940ef | -6.2884 | -43.85891 | 2025-08-26 04:21:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 953ee793-c646-3131-ac12-60b1c64b4bb6 | -6.74876 | -43.03506 | 2025-08-26 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4ccddba7-cd9b-34d6-82a7-6ee5ef965ec8 | -6.6095 | -47.3317 | 2025-08-26 04:21:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3c078060-be9a-3409-966c-2a2cc6065400 | -11.15965 | -44.76947 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 44bfa1f4-3bee-31cf-aacb-b223d6d82801 | -4.89385 | -55.80962 | 2025-08-26 04:21:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4a25bc1-d592-3ecc-998a-29665e702f4a | -6.75978 | -42.98764 | 2025-08-26 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 86fb60f0-88b4-39ad-9ea1-6146dbe98788 | -7.08251 | -46.05839 | 2025-08-26 04:21:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b51124a3-bb41-31f4-9997-b60d3ed7ff63 | -4.6275 | -41.3992 | 2025-08-26 04:21:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| da419934-787b-33b6-87e5-dc72d206083d | -6.31371 | -41.89135 | 2025-08-26 04:21:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 33abac09-4da5-3741-85d9-a23e750f160b | -9.84827 | -44.70101 | 2025-08-26 04:21:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3acd13cb-0d70-3dfc-9229-32cab971b41b | -7.75219 | -43.92424 | 2025-08-26 04:21:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 085da664-31b8-3b87-b1ec-28b9c3f886e0 | -11.13858 | -44.69624 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9c1f8ea-e9c9-39e4-a761-4948d61b8b7f | -7.30513 | -43.6621 | 2025-08-26 04:21:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 381ebc1b-0708-30ae-a660-4c6c4c1c67ea | -4.78714 | -47.2778 | 2025-08-26 04:21:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f427a437-618b-3e39-826d-c64460e23c2e | -5.79099 | -46.13823 | 2025-08-26 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71cdffcc-db45-3569-9adb-794dac6d0c34 | -6.89277 | -45.65517 | 2025-08-26 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e38ccc21-71d2-30bf-9400-177dcb6e6f67 | -8.28339 | -47.2272 | 2025-08-26 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5902feb9-983a-3e81-a2aa-ca39ec698641 | -6.41114 | -41.76696 | 2025-08-26 04:21:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f3b70f74-c196-37f2-a1c3-e41ea1e4d251 | -4.70154 | -56.06913 | 2025-08-26 04:21:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 35f3d9c1-890a-31be-9a72-8e627f0874cf | -7.30343 | -43.66207 | 2025-08-26 04:21:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 97267a7b-1faa-3bee-9bb7-00e2ceba862e | -6.53736 | -44.42233 | 2025-08-26 04:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 439a69db-8758-3a0e-8c6b-30a2e986fdb4 | -8.15912 | -45.06024 | 2025-08-26 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a379bb05-a8af-391e-b048-43b50e2a27af | -8.07081 | -49.66374 | 2025-08-26 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4a0962f5-5219-3cab-8a8b-5ae24aabb5e1 | -11.08732 | -44.78321 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df39acec-c8ca-3d82-9a08-752dc23b02db | -6.89548 | -44.42546 | 2025-08-26 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1a3dc0c-d3f7-3d0c-9a8f-8f6ce594b878 | -6.03031 | -43.9933 | 2025-08-26 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbb9d02f-3304-3941-b226-8abafbb1e365 | -4.69435 | -43.09994 | 2025-08-26 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6fddbcca-9cb1-3d8a-a795-72181b2114d1 | -11.14796 | -44.7786 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| becce13b-41f4-3395-aeff-8fc03fea4a3b | -8.48932 | -48.23553 | 2025-08-26 04:21:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ea3c902-823a-389a-83d4-1e201a80ac5b | -11.15237 | -44.75 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 976d03df-0e97-3de6-a013-4ef177601cdf | -6.88943 | -45.65457 | 2025-08-26 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3585cec3-6ab4-3b43-984d-e02643cda80d | -5.7493 | -45.3575 | 2025-08-26 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f06dd59a-97b8-3f6f-936d-aa9929f927e3 | -4.93229 | -47.55377 | 2025-08-26 04:21:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 194816d7-bf14-3f77-a430-8c8d0fcc2882 | -3.97788 | -51.06543 | 2025-08-26 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 07a86dc3-3a77-369d-b095-40b669325726 | -7.22302 | -44.40914 | 2025-08-26 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb30d56e-b08a-3f06-af03-c7c2234fca74 | -7.67209 | -42.67265 | 2025-08-26 04:21:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6fbc4dcd-0472-3db9-9d53-1c4118df781e | -6.06909 | -43.99982 | 2025-08-26 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c7c89bb-f2a1-31b2-bbc4-62ec5966cafa | -8.32723 | -50.57529 | 2025-08-26 04:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d27692d9-155b-3b3c-b3c6-50afaaa1accc | -8.12383 | -47.29377 | 2025-08-26 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf5b1611-0843-3b46-8446-07141cfe4290 | -7.58491 | -47.49855 | 2025-08-26 04:21:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05ca6265-dbda-3c87-95ad-22dc71b467ae | -8.47188 | -43.66892 | 2025-08-26 04:21:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34d8a6bc-e21e-34aa-b3a0-3320a013c373 | -5.13185 | -43.22487 | 2025-08-26 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aa2921d6-37d7-37b6-a967-72f1f0937a18 | -10.81568 | -46.37438 | 2025-08-26 04:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3c8b753c-180c-363a-a187-31ba533a3756 | -5.57343 | -42.62872 | 2025-08-26 04:21:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 750c3620-fca4-3c38-a94f-6849056c4f20 | -11.10848 | -44.75738 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f6da33a-e03c-34d8-a1c2-0a4e53a761c7 | -11.28015 | -44.93442 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| efde45bf-2aa3-3152-a6ec-bf533ff3e2c2 | -11.15448 | -44.69171 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9001580-78ef-3e52-89d1-51290a93e406 | -5.46808 | -42.58654 | 2025-08-26 04:21:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6d20f3b7-145f-3621-9f70-379c60867c72 | -9.74747 | -37.91708 | 2025-08-26 04:21:00 | NPP-375D | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 66f83061-4831-3cc8-b634-e7c5c650d02c | -7.5785 | -47.49331 | 2025-08-26 04:21:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ccc10942-fc49-3440-9efa-4ed8f21320cf | -6.5238 | -44.57305 | 2025-08-26 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5f741ff8-3ca8-3828-b56f-6b8bf75f3d72 | -6.27081 | -43.68735 | 2025-08-26 04:21:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16bcfcf2-ee2c-3810-88d0-1522b227420f | -11.22833 | -45.46205 | 2025-08-26 04:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 063030ed-d221-3f7b-86df-b2f8b2ce44ab | -11.14965 | -44.78982 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0a39870-81c2-342f-a052-8f4009a919ee | -4.79142 | -47.27431 | 2025-08-26 04:21:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ab2722e-fe96-3bc1-b87b-cee92abab0cb | -6.80883 | -44.99548 | 2025-08-26 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c7cf347-d374-3e4d-8a15-0267141dbc87 | -7.5891 | -47.49518 | 2025-08-26 04:21:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18230c4a-7260-384a-9f33-ecaed760f172 | -8.33205 | -50.57218 | 2025-08-26 04:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 97af7434-eb81-3e79-bd02-74051ea015c0 | -6.02589 | -43.99974 | 2025-08-26 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c761fd6-64ea-3bb3-a1e5-6345bab6f880 | -6.4341 | -44.58374 | 2025-08-26 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0f76d22-2876-38b7-8f38-b27cd01026ef | -3.25323 | -46.90722 | 2025-08-26 04:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 558719a4-a0b0-397f-945b-fb226c391bbc | -11.1558 | -44.79445 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c791722-2231-3744-974a-e472f979dfbb | -6.90208 | -44.40516 | 2025-08-26 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 529fd18a-66e7-3c93-bb02-66f8823b97d0 | -6.80606 | -44.99147 | 2025-08-26 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2203671f-0c4e-32af-8f34-84d7377f15f2 | -5.90195 | -46.05762 | 2025-08-26 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4404f72-0401-3708-b2b6-4a728d31d227 | -8.47301 | -43.66167 | 2025-08-26 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b72beb2-6d66-3e17-be78-ad76e70c39fc | -4.96534 | -55.82494 | 2025-08-26 04:21:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 35a372f2-f110-3444-b1d9-ed05d4ef5910 | -6.97968 | -44.12813 | 2025-08-26 04:21:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1cefcf60-ef68-3f56-ae1a-bc21be698bbf | -8.07711 | -44.99726 | 2025-08-26 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ffaecd7-b209-36a4-beb5-39d1c27dbc57 | -6.44411 | -44.60665 | 2025-08-26 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9dc4c9d-a635-32de-8243-8cccfca4113d | -4.4813 | -47.66806 | 2025-08-26 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e69ce28-bf4b-3069-8632-aa3ca6d43b6c | -11.30452 | -43.28947 | 2025-08-26 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ebc5b582-74fa-39b9-9c23-6d0141d7b72b | -6.24091 | -43.74731 | 2025-08-26 04:21:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9411d8bf-cabd-3c55-96d7-c504a9195b82 | -4.82506 | -47.31801 | 2025-08-26 04:21:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56f5db58-e074-3c88-abf8-6f71dd08815b | -5.41027 | -49.20082 | 2025-08-26 04:21:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac722652-2241-32cd-8f6f-e33d9469ed18 | -3.98333 | -51.06136 | 2025-08-26 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2b5ba7b8-af25-3272-8cd7-c9ec2b71f15c | -3.25257 | -46.91135 | 2025-08-26 04:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f838608d-ccb7-3b7a-b580-4308001e5c39 | -7.46965 | -45.01131 | 2025-08-26 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5acbdaca-7895-3db1-8e7a-336f35a22948 | -6.14652 | -44.39254 | 2025-08-26 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac0ba561-a7ef-3620-8d1a-9a18049836cb | -7.67033 | -42.67261 | 2025-08-26 04:21:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b6bc8ee2-f804-3e6f-9ebf-0acb1fedbcb8 | -8.3289 | -47.25456 | 2025-08-26 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3994bd96-445c-34f1-872a-1ea29bab8711 | -11.25573 | -44.98145 | 2025-08-26 04:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b45dfa77-8697-34f3-b22a-9132fc4fdec2 | -9.26666 | -56.90389 | 2025-08-26 04:21:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 775104cd-73b1-3453-9a6a-503ee06405fb | -11.15627 | -44.74694 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af71f291-09a0-3244-b1bc-d75fb3405f6c | -10.51486 | -46.7673 | 2025-08-26 04:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 24329cd2-7bff-3849-ba40-ecc69e89001a | -8.24277 | -45.08789 | 2025-08-26 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e967dfd9-d71a-3085-a54d-c24de10c0ceb | -4.70252 | -56.06369 | 2025-08-26 04:21:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ce21f67-8b11-3428-90fd-0e8bc8a6593a | -4.63105 | -41.39978 | 2025-08-26 04:21:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d37dd73e-dac6-3357-ac4b-bb207b0ea29b | -3.97871 | -51.06046 | 2025-08-26 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README42.md)
