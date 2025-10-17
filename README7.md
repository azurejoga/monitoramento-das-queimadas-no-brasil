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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae7df371-4b9e-324f-a636-0a5c449b4ed1 | -5.36595 | -43.15543 | 2025-10-17 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 70af1701-c3aa-3691-b0b6-c40d344dd066 | -4.87913 | -45.94681 | 2025-10-17 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 86241f2a-64c1-3270-9f67-ccca9bf9e6e6 | -5.87541 | -44.75848 | 2025-10-17 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ac29c95a-91ea-3151-83c2-65a512ebe05e | -5.3444 | -45.37309 | 2025-10-17 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e4888667-b1da-3051-88fe-b2eb97375720 | -10.27463 | -44.04752 | 2025-10-17 00:13:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 61eb3f0d-beb8-30b8-9ee9-9b2e51ce0a57 | -10.95115 | -49.77532 | 2025-10-17 00:13:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 3aa25c9e-19ae-38fa-b19d-af7c4ff078a5 | -6.2242 | -44.14624 | 2025-10-17 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dc3826af-5a9f-36d0-ad4c-e7cf74221cda | -8.0761 | -45.41554 | 2025-10-17 00:13:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 48f54681-fd1d-3925-8f97-b3da89d1246b | -10.1052 | -44.62905 | 2025-10-17 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 7aa69dcf-7520-3e6e-b808-77f6dad3a243 | -8.67674 | -40.89577 | 2025-10-17 00:13:00 | TERRA_M-M | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 21.7 |
| effa0659-7df1-30aa-8ce0-5ed9a1a227ee | -11.09214 | -45.86953 | 2025-10-17 00:13:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 310ebed9-1a36-3bc1-b27e-e41ded5dda8b | -9.948 | -45.7099 | 2025-10-17 00:13:00 | TERRA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 8a0202c2-e0a0-3589-9bba-97d9a6e1be84 | -9.44085 | -47.90454 | 2025-10-17 00:13:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 92fed843-800b-3223-86cb-a4ab577294ec | -7.17693 | -46.93312 | 2025-10-17 00:13:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 9d0e08a4-8d67-3e10-98d7-b61cd4cf805b | -8.25422 | -43.43865 | 2025-10-17 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8520c8e4-b294-3649-a8ff-a105c8b9eb20 | -10.13167 | -44.54521 | 2025-10-17 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 4c4a4cc2-e90d-31ae-9b7a-7b33f57449e0 | -5.34792 | -45.74093 | 2025-10-17 00:13:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bee7b383-4ecc-3afc-b16d-57fe1776b108 | -4.4211 | -40.17658 | 2025-10-17 00:13:00 | TERRA_M-M | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 15.1 |
| bb8c6597-1c02-3595-8be7-321245f95c2f | -8.83243 | -47.3112 | 2025-10-17 00:13:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 687c4975-f880-3e4f-9da0-4d30521be5d1 | -9.34066 | -46.90147 | 2025-10-17 00:13:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 235193f8-5822-3a57-a607-c9bc3ea10564 | -10.13931 | -44.53497 | 2025-10-17 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 48dfa1a0-84d4-3717-9bb1-564b176ea439 | -7.59508 | -46.07773 | 2025-10-17 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2f0c8cd7-d9bd-3a63-a605-bf21defcb395 | -6.37557 | -41.4736 | 2025-10-17 00:13:00 | TERRA_M-M | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| e31c57c7-f56d-391f-9f3e-d30b27101859 | -10.26458 | -44.03987 | 2025-10-17 00:13:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 61.7 |
| aa80f5d9-b631-3cb9-a857-ce5c49ae7d6c | -11.75676 | -51.16127 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 9348f318-49a9-3eb1-bf4a-4c4973d021a9 | -7.40537 | -44.75236 | 2025-10-17 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a0e188db-c8a9-323f-9b60-a7963f10f614 | -9.9493 | -45.71957 | 2025-10-17 00:13:00 | TERRA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 28fe7fe6-9891-34e7-af5c-cb3bba6f81d9 | -6.38559 | -41.47233 | 2025-10-17 00:13:00 | TERRA_M-M | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 247f9f25-6456-333d-af65-33e128adb6c0 | -7.85341 | -43.80211 | 2025-10-17 00:13:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 8dcdcf78-9c6e-3001-8a1b-7ddcc5838bfd | -8.24363 | -44.02137 | 2025-10-17 00:13:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 21.3 |
| d835ae03-4f3f-3352-98db-9d57d0fb658f | -5.27268 | -43.21428 | 2025-10-17 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 041892c7-33d1-3d3d-931b-63941aeba9f0 | -10.51287 | -43.43346 | 2025-10-17 00:13:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c350d5c9-4206-39a3-8c89-92399837f9ef | -8.12054 | -45.54018 | 2025-10-17 00:13:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2bddfcb2-03a5-3f61-82ab-ccee51a5c624 | -4.31349 | -43.21643 | 2025-10-17 00:13:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c5288c1f-e237-322d-a29f-59126635fe62 | -10.13782 | -44.59039 | 2025-10-17 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 379fd102-571e-317e-8230-27db93886523 | -6.48974 | -47.22388 | 2025-10-17 00:13:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ad304281-c5ef-3870-99f7-b36b92820b6a | -4.94766 | -44.44056 | 2025-10-17 00:13:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| e1e7a2d2-d291-3517-9250-107f49a390de | -9.23913 | -44.36027 | 2025-10-17 00:13:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 08da14a7-c493-3104-9e09-5d84908f72c9 | -5.96859 | -44.03714 | 2025-10-17 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 900fc6b4-a526-3ad9-8e34-782a8b8bf52c | -4.59099 | -46.33516 | 2025-10-17 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2115a134-774b-33a7-8376-607abd7daf33 | -7.95349 | -44.11768 | 2025-10-17 00:13:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 3a68592c-77cb-3088-8f3f-72fd0d3d3f68 | -5.3554 | -43.14713 | 2025-10-17 00:13:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 1832ed73-993c-3d62-9ced-016b3f2da5d0 | -6.09564 | -40.9003 | 2025-10-17 00:13:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 761da602-ca60-3db6-8be0-6d88f254271f | -5.70508 | -44.51887 | 2025-10-17 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| da32191e-6b1d-30f7-8aa8-763449431cab | -4.86597 | -45.78427 | 2025-10-17 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ac195211-a938-3225-9c01-291d3a06d450 | -11.13306 | -47.4436 | 2025-10-17 00:13:00 | TERRA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| fd0b795a-8f9c-3a54-8d3b-f94b65c0f498 | -8.3966 | -46.28218 | 2025-10-17 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 56715c55-7c0a-346a-bc2e-1a8390f17512 | -6.0867 | -42.38832 | 2025-10-17 00:13:00 | TERRA_M-M | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| bf39f562-c566-3f80-a7de-bd1207fb136b | -5.35821 | -42.71973 | 2025-10-17 00:13:00 | TERRA_M-M | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| db85b1d9-c19a-3c46-9a28-81dddf19ee46 | -6.02167 | -41.93314 | 2025-10-17 00:13:00 | TERRA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 6f1e966f-8f0d-380d-b2ba-d907ba4b611e | -7.48331 | -42.7493 | 2025-10-17 00:13:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| e56f52aa-2ffa-36ae-85e0-4a6bbbfcbb66 | -7.1664 | -42.53609 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 67ad3c98-3c1b-39cc-8e86-b8609fe4b137 | -11.52485 | -49.14128 | 2025-10-17 00:13:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| d077f277-a646-3ec7-b3cd-4bf252af5035 | -10.14939 | -44.54269 | 2025-10-17 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 0498011a-d574-3ce3-88b8-8753d929dec6 | -5.86797 | -43.91089 | 2025-10-17 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 6fa2d0f4-1a9c-3d93-9209-b097c3d9baa4 | -8.56159 | -44.58134 | 2025-10-17 00:13:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e20d554e-0222-3027-bc1d-9dde3225fe96 | -11.76198 | -51.15545 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 73ae8700-5fdd-3da4-8120-817bc1015c56 | -8.39394 | -46.26257 | 2025-10-17 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 55b04040-2263-3438-a916-201b3d37e2c1 | -6.3167 | -40.93236 | 2025-10-17 00:13:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| dfa826b0-7e6c-3aa5-996f-40e2784d20d3 | -8.11661 | -45.57835 | 2025-10-17 00:13:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 51c36b9d-74c2-3e0c-b91a-093d8f2f5898 | -6.57996 | -47.06874 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c371e29e-6186-3b49-bd3d-e930ca02236a | -6.43979 | -43.3852 | 2025-10-17 00:13:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 65803faa-72f0-3d81-9300-040e7c877c0a | -10.50662 | -43.38882 | 2025-10-17 00:13:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8f4e72df-032b-3be0-8491-75f660cc6ed5 | -4.92886 | -45.9124 | 2025-10-17 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 46dd0344-e432-358a-b76c-e4725db25410 | -7.17427 | -42.52495 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| e5f4370e-8136-370f-8b9f-358657483f17 | -5.883 | -44.74843 | 2025-10-17 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f2762320-b622-3614-a18a-60d071a5c495 | -6.90721 | -46.16357 | 2025-10-17 00:13:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6dc9e244-9bf4-3ed5-993b-d87c205c48ad | -7.20287 | -45.49131 | 2025-10-17 00:13:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| c0f30ec2-7d2a-37c7-8166-583591cd5c32 | -7.61496 | -47.84193 | 2025-10-17 00:13:00 | TERRA_M-M | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ecfe7cce-8caa-3591-8a48-4a4265fa073f | -6.32739 | -43.63256 | 2025-10-17 00:13:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fdb3433a-31f1-32b1-a60b-fda01968920d | -7.16229 | -44.99519 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 86d7ee4f-c8f0-3df6-9c4b-588cd629d954 | -7.05196 | -44.26257 | 2025-10-17 00:13:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| fd0a5912-bfc3-3e0f-b0ac-5bbcb84ddde6 | -10.9539 | -49.76841 | 2025-10-17 00:13:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| b81229a8-4444-34a5-ab7b-c3b1555e5383 | -7.46939 | -42.14941 | 2025-10-17 00:13:00 | TERRA_M-M | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 55011a45-53b6-3c3d-91a2-c9301ee3c24f | -8.40586 | -46.28087 | 2025-10-17 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 6f3bcb65-fe31-3012-9f41-0cfb7ee1a640 | -6.32205 | -44.31643 | 2025-10-17 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 438546b0-ce85-3369-b552-5d2a0b7bad5a | -8.23481 | -44.02264 | 2025-10-17 00:13:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f4e8d06a-0fc7-38cc-9802-87dc3968aa2d | -10.27094 | -44.0208 | 2025-10-17 00:13:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| f9ce4aa3-0016-327d-846a-a5861c68dce1 | -7.09978 | -35.09934 | 2025-10-17 00:13:00 | TERRA_M-M | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 36.7 |
| 6e8127ec-cb09-3288-a32f-9cccdf6c27bc | -9.23413 | -48.59777 | 2025-10-17 00:13:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| af51aee9-8a88-3f24-b9f6-8294a6407102 | -6.93331 | -43.68422 | 2025-10-17 00:13:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 69139efe-ff3e-3b4d-ae29-ec9e4bfa6de0 | -5.69665 | -44.3938 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 55fb2e70-a032-3a97-b1c7-3754a8c8efba | -10.53197 | -49.54227 | 2025-10-17 00:13:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 31.5 |
| ac7f91a1-8a1d-3d15-afb2-8e78eef9162b | -6.21581 | -44.42494 | 2025-10-17 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 8f73bd42-49d4-3daf-8b30-13416b986fbc | -6.5857 | -47.07222 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 8ee6ca56-10c6-3d1b-beb3-6bdf5c9a7e2f | -5.84636 | -43.88626 | 2025-10-17 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| c9d25a12-4075-39b0-bd52-37a2acf9f32a | -4.48391 | -44.29162 | 2025-10-17 00:13:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9ecd66d2-02c3-34ad-93f7-89b6da028f21 | -10.14816 | -44.53372 | 2025-10-17 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 182b5018-dff8-322c-8bc6-d4f635565e47 | -5.89509 | -43.90102 | 2025-10-17 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2d93a152-f062-33af-90b8-f76423ba834e | -6.29098 | -42.97994 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 88cb62a0-4be3-33c7-9033-b66c98e8ac7b | -7.28094 | -42.94353 | 2025-10-17 00:13:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 3a9c1857-425a-3805-998d-07cf0bbad6b9 | -5.45717 | -42.94806 | 2025-10-17 00:13:00 | TERRA_M-M | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 981d2695-c924-33f5-9161-9a9ddbdc7e19 | -8.07733 | -45.42455 | 2025-10-17 00:13:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f8d2b454-ad43-36c3-bb66-b06b4ec54692 | -5.27806 | -43.25243 | 2025-10-17 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 3178e616-7d5d-354c-9c5c-1ce2837129f1 | -5.0341 | -49.21745 | 2025-10-17 00:13:00 | TERRA_M-M | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| fe429e75-7db7-3998-9252-b7faf7b48017 | -9.35319 | -46.92189 | 2025-10-17 00:13:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 6e8d2e88-8da5-3fc1-a5aa-e4fc06b064c3 | -6.18254 | -44.10678 | 2025-10-17 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| a0c111fc-1fbc-3ee0-848c-afdae0f64c46 | -6.76997 | -42.85362 | 2025-10-17 00:13:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| eeb9feab-8e0f-30a8-8408-5475f170a33a | -6.33076 | -46.32847 | 2025-10-17 00:13:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bcf01b71-32df-3794-86f5-232fad6534ee | -5.29205 | -43.54809 | 2025-10-17 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |


[Clique aqui para ver as próximas entradas](README8.md)
