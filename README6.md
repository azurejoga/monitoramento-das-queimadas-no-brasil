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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd15cd4a-5091-3350-b280-7474cd6ebd60 | -11.8045 | -47.562401 | 2024-10-03 00:10:17 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e73d06a2-47d0-30d0-a18e-e54e96d4f453 | -12.1683 | -50.033501 | 2024-10-03 00:10:19 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d1f7d2cb-a000-3221-8248-b36161915f37 | -12.1548 | -50.0159 | 2024-10-03 00:10:20 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 19dc7bbb-3814-3477-827c-30d18a4c6297 | -11.6862 | -47.682098 | 2024-10-03 00:10:20 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5193e4e5-b3f8-3502-92da-6dc67c4ef415 | -11.6889 | -47.695301 | 2024-10-03 00:10:20 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0cea7dff-20b4-3462-92a5-97d6b28bb8c6 | -11.9425 | -50.117699 | 2024-10-03 00:10:23 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8fb873c2-3e26-319c-9224-330d3f11e8cf | -11.9463 | -50.137299 | 2024-10-03 00:10:23 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2a265754-af0d-3a8e-ade8-a1e8bcd4a7ef | -10.9136 | -45.168999 | 2024-10-03 00:10:24 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0919e6a9-da4e-37f1-9502-71249ff9ee63 | -10.2293 | -42.380402 | 2024-10-03 00:10:25 | METOP-B | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| df78827c-9f33-3422-84cd-a3768b86a34b | -10.6654 | -44.4827 | 2024-10-03 00:10:26 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 203fd787-541f-30f8-ab21-09924e2eae96 | -10.6672 | -44.491001 | 2024-10-03 00:10:26 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dcde5c45-2fba-3232-a9f8-e235f5971999 | -10.6556 | -44.484798 | 2024-10-03 00:10:26 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ae9f4242-2bef-3e3b-8cd0-ea864e791217 | -10.6592 | -44.5014 | 2024-10-03 00:10:26 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e77830c1-655f-3412-8b96-f592777d211c | -10.6574 | -44.493099 | 2024-10-03 00:10:26 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 734473fc-a806-35b9-bffe-33b346c280a3 | -11.0303 | -46.511902 | 2024-10-03 00:10:27 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 06d240d2-1d50-30c5-bb90-cb39f0cec31b | -10.9836 | -46.532902 | 2024-10-03 00:10:27 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 392d04e1-61fa-37d9-920b-3ba0feed0270 | -10.9859 | -46.5438 | 2024-10-03 00:10:27 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d24bb32b-c095-3c49-b1b1-5b15c9bf1d1b | -10.9155 | -46.302399 | 2024-10-03 00:10:28 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e12fe844-c742-31f1-be2a-5bd381ab626f | -10.9177 | -46.312901 | 2024-10-03 00:10:28 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 45dc5a7f-4be8-36b9-a8b9-a9032b79e798 | -10.9058 | -46.304501 | 2024-10-03 00:10:28 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6614c94a-be6c-3650-983b-518ee12340d4 | -10.9079 | -46.314999 | 2024-10-03 00:10:28 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 35733086-6fd0-38a7-8d24-adb6d7f2964c | -10.949 | -46.562801 | 2024-10-03 00:10:28 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 20debd26-cc05-3719-bfaa-30060bc0ee51 | -10.9513 | -46.5737 | 2024-10-03 00:10:28 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6cec740f-7ed0-3963-848c-b8bd9d6fdc55 | -10.7224 | -46.1595 | 2024-10-03 00:10:30 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 76a20e5d-d3ae-304f-8371-7d375a51b0bf | -10.7245 | -46.169701 | 2024-10-03 00:10:30 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 84df8056-ff81-36d4-9b8d-6b9f49cfdb78 | -10.7267 | -46.179901 | 2024-10-03 00:10:30 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4630139a-3eac-3e58-996c-ff6adbae4128 | -10.7169 | -46.181999 | 2024-10-03 00:10:31 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a69b65fe-400c-37d3-898f-8ae9dcc13aca | -10.719 | -46.1922 | 2024-10-03 00:10:31 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6f4b28d0-a35b-3e3a-a4da-9f3337edc6a0 | -10.6923 | -46.112701 | 2024-10-03 00:10:31 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 36b83143-55db-3894-9956-e609d799f208 | -10.6944 | -46.122898 | 2024-10-03 00:10:31 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c4115dea-6470-35f0-be14-a9e215ab7243 | -10.6965 | -46.132999 | 2024-10-03 00:10:31 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5de8ddb0-0aa5-3176-b1ab-171644c0ee80 | -10.6986 | -46.1432 | 2024-10-03 00:10:31 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 98cf44d5-65ef-3833-8817-17dff3e94a19 | -10.7386 | -47.6731 | 2024-10-03 00:10:35 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fd822b78-ac89-3fd5-80e8-614c24b698de | -10.7412 | -47.685902 | 2024-10-03 00:10:35 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 55948623-da9d-3dc1-a3a3-085229e668c1 | -10.7165 | -47.664398 | 2024-10-03 00:10:36 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d2c50709-2bee-36f0-aa53-167bbba762cf | -10.7191 | -47.677101 | 2024-10-03 00:10:36 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 54615098-a650-3042-830c-5c1e205ac670 | -10.7217 | -47.689899 | 2024-10-03 00:10:36 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8f145874-85c3-3784-b62e-a4ae4da70498 | -11.0864 | -49.559299 | 2024-10-03 00:10:36 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7b25fe4a-506e-311a-94cf-88d1fb0e4bc6 | -11.0899 | -49.576698 | 2024-10-03 00:10:36 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 647aacb8-3aa2-377e-8ad1-1f91bd7a2f87 | -11.0801 | -49.578602 | 2024-10-03 00:10:36 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4e6dc034-4252-3bed-b9a3-96f1e639976a | -10.7455 | -47.956799 | 2024-10-03 00:10:36 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0593e7ac-010c-3813-b73a-91e97747c2ca | -10.7482 | -47.9702 | 2024-10-03 00:10:36 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4473d1d3-aaf0-3cd4-84af-be8bc17a682e | -9.0093 | -40.252899 | 2024-10-03 00:10:37 | METOP-B | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| d114a4df-8f55-3a6b-9099-ace45b7efa66 | -9.011 | -40.260101 | 2024-10-03 00:10:37 | METOP-B | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 9f72c27f-4f49-3f5e-abdf-c2fec7f66c99 | -10.6001 | -48.042301 | 2024-10-03 00:10:39 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 952e73ce-bd14-3ee0-a4d3-78b06b70d6db | -10.5931 | -48.057701 | 2024-10-03 00:10:39 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 325e98ed-44db-30dd-91d5-af62dae5bdf7 | -10.5959 | -48.071201 | 2024-10-03 00:10:39 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f1501e86-1e56-3fe3-9ffa-d17bc5f867b2 | -10.5986 | -48.084702 | 2024-10-03 00:10:39 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f923bea0-e92f-34fb-bf4d-9fa9c4f79ada | -10.5697 | -47.992802 | 2024-10-03 00:10:39 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d33aad4-acda-3c89-9934-1948187b6e32 | -10.5725 | -48.0061 | 2024-10-03 00:10:39 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 42489a0d-af19-3b2b-be1a-c7e6cf78abfe | -10.5599 | -47.994801 | 2024-10-03 00:10:39 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| daa52df6-f7e2-3701-91a3-aa0e3482d478 | -10.5627 | -48.008099 | 2024-10-03 00:10:39 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c6549fa3-b3e8-3ced-a0c1-82b925cfca20 | -10.5708 | -48.048302 | 2024-10-03 00:10:39 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ecf4f78-2c5c-3eb3-b4f0-1db130c40989 | -10.5736 | -48.061699 | 2024-10-03 00:10:39 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ee099fab-96f0-3028-8d9b-6373a0982442 | -10.5611 | -48.050301 | 2024-10-03 00:10:39 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f5cf3dc8-131c-3d3d-adaf-278bb872954b | -10.5639 | -48.063702 | 2024-10-03 00:10:39 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f7f8105c-775f-3e27-907b-d55637ec650c | -10.5666 | -48.077202 | 2024-10-03 00:10:39 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7fb9a81a-e49a-3106-8d18-be073dd0a8eb | -9.4965 | -43.162998 | 2024-10-03 00:10:40 | METOP-B | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 3021a142-0f79-3659-9e22-0e4ba43cb866 | -10.473 | -48.166901 | 2024-10-03 00:10:41 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d12d8caa-9733-3f68-b330-c5e9229d9da7 | -10.4604 | -48.1553 | 2024-10-03 00:10:41 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 773c1583-6550-308b-bff7-cd2b6950ad71 | -10.4632 | -48.1689 | 2024-10-03 00:10:41 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 54d001e0-ad02-3bc2-8575-886c3408981d | -10.2465 | -47.655998 | 2024-10-03 00:10:43 | METOP-B | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4a8f4b6b-6896-399d-9514-a00d21979f85 | -10.2367 | -47.658001 | 2024-10-03 00:10:43 | METOP-B | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d13d3d87-8e5f-3b26-9d32-8e1fe5461c76 | -8.4804 | -39.880001 | 2024-10-03 00:10:44 | METOP-B | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| c44aee91-7ec0-3df8-bc09-73bfd7d7c558 | -9.2484 | -43.484798 | 2024-10-03 00:10:45 | METOP-B | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9231164e-d7be-34ef-9c61-727b56c1dcda | -8.4706 | -40.512901 | 2024-10-03 00:10:47 | METOP-B | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| b3ff417c-01a3-36f7-b536-2048cee02050 | -9.8974 | -47.7411 | 2024-10-03 00:10:49 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7ae6ada5-70ad-3ec6-b752-d443496a596e | -9.8876 | -47.743099 | 2024-10-03 00:10:49 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f4e470ac-8d65-30d0-84fd-fea887cca7ff | -8.4291 | -41.924 | 2024-10-03 00:10:53 | METOP-B | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 53322449-d67d-37f4-9390-31d12e2957b1 | -8.4306 | -41.930901 | 2024-10-03 00:10:53 | METOP-B | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 16a86be5-2381-3292-9307-0e7d386ed9d8 | -8.4322 | -41.937801 | 2024-10-03 00:10:53 | METOP-B | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 53ae0b05-bbb7-3511-8315-e6a55b17ee29 | -8.4208 | -41.933102 | 2024-10-03 00:10:53 | METOP-B | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b2535157-defd-3455-ada0-a6a099768e93 | -8.2067 | -41.394001 | 2024-10-03 00:10:54 | METOP-B | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 17c47719-1b9a-33b2-be14-b9524e2e39c5 | -8.2083 | -41.400902 | 2024-10-03 00:10:54 | METOP-B | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f56a9585-4450-3dd1-900a-535e5e88bbe5 | -10.644 | -53.630699 | 2024-10-03 00:10:56 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 02d39afa-5c10-3a5c-9879-677104245e07 | -10.6344 | -53.6325 | 2024-10-03 00:10:56 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cdf666e7-87ac-30e8-9bfa-bb7aae61ef1d | -8.3188 | -42.813801 | 2024-10-03 00:10:58 | METOP-B | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8f7353d7-5dbf-3a89-94af-89a18c2931fe | -8.3203 | -42.820702 | 2024-10-03 00:10:58 | METOP-B | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 621bf9ea-4a0f-3fa3-a3a5-db48642e5272 | -8.309 | -42.815899 | 2024-10-03 00:10:58 | METOP-B | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 274d64b0-2dbe-3cfa-b999-b4f51203620e | -8.3105 | -42.8228 | 2024-10-03 00:10:58 | METOP-B | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3164e6f4-0917-37bc-b50e-8d31afad3db7 | -8.9309 | -45.621101 | 2024-10-03 00:10:58 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0f49832d-15d9-326c-9819-582d621ea9cf | -8.9328 | -45.630001 | 2024-10-03 00:10:58 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4a30d070-6a0f-3ca5-b6be-5017a8890d97 | -8.9211 | -45.623199 | 2024-10-03 00:10:58 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a68fc5fb-f75d-31b8-9ee9-2499122db628 | -8.923 | -45.632099 | 2024-10-03 00:10:58 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 20cc18cb-0807-3566-88e3-0dbb0f107d10 | -9.4227 | -48.897598 | 2024-10-03 00:11:01 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| feb2497c-78e0-3d67-9a1a-d1e9c41c7073 | -8.0751 | -42.875198 | 2024-10-03 00:11:02 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3b328c8d-16e2-3fc7-aab0-72495c2894a0 | -8.0767 | -42.882198 | 2024-10-03 00:11:02 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d124f018-0425-35af-86ff-607a88aed733 | -7.8723 | -42.657398 | 2024-10-03 00:11:04 | METOP-B | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0dd9ac25-359d-3452-b947-6464dd4dcb39 | -7.4134 | -40.443401 | 2024-10-03 00:11:04 | METOP-B | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 62a8c3bd-03b6-3254-ad04-0bd9f23ee0c1 | -8.1852 | -44.3545 | 2024-10-03 00:11:05 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b41e519e-c358-3fa3-a1bb-52cdcad50e1a | -8.1869 | -44.362202 | 2024-10-03 00:11:05 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c25de6f5-0b3a-3788-a71e-8a70ee464a2a | -8.1886 | -44.3699 | 2024-10-03 00:11:05 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fff36716-26d7-3809-9f24-672e60d8fc6f | -7.8512 | -43.071899 | 2024-10-03 00:11:06 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2165a937-47b8-37ee-bb63-44eee827e4d6 | -7.8528 | -43.078999 | 2024-10-03 00:11:06 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 464a8041-72ec-337e-8a93-3fb0c77a25dd | -7.8544 | -43.085999 | 2024-10-03 00:11:06 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ef685bde-6ece-3c65-9e52-c6a92a877857 | -7.8559 | -43.092999 | 2024-10-03 00:11:06 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 24731348-4bcf-32df-ac06-6e626d3dddb3 | -8.335 | -45.327999 | 2024-10-03 00:11:06 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a7a9bebe-74d2-3d39-92be-395e1296237d | -8.3369 | -45.336601 | 2024-10-03 00:11:06 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b8d622cc-b4fb-346d-bbb6-88d967203a87 | -8.3387 | -45.3451 | 2024-10-03 00:11:06 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 21065c95-7eb6-3342-8a2c-2daa62d153aa | -8.1787 | -44.372101 | 2024-10-03 00:11:06 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README7.md)
