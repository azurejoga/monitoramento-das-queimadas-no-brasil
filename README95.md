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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ffb539fb-27b0-3fe8-9fa2-d30849c486cc | -5.5472 | -41.3128 | 2025-10-16 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 137.1 |
| 73e32f59-2e97-3e99-8c04-3b466a6097fc | -5.4558 | -41.0297 | 2025-10-16 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 193.7 |
| 81f16b70-6751-3433-9427-d96d745253c7 | -13.055 | -46.9746 | 2025-10-16 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| c64177df-7dbb-3e6f-8473-6a494388019e | -5.739 | -44.9945 | 2025-10-16 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 145.6 |
| 999be7aa-c825-3ae2-8976-7d07574804d7 | -13.4412 | -47.9483 | 2025-10-16 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 53.6 |
| c32630a0-ceea-3e71-a7bb-8568d66e2211 | -6.5903 | -44.1039 | 2025-10-16 14:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |
| da3c2a38-fc5d-3990-9b6f-3cc52ba28b6a | -12.2652 | -47.1346 | 2025-10-16 14:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 5cec7efd-869b-3f7b-b1ae-81bedb393c25 | -14.1749 | -47.9477 | 2025-10-16 14:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 0454927f-fefd-3053-947f-60c0acfe5d89 | -6.4255 | -41.8865 | 2025-10-16 14:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 111.0 |
| 0d280387-e7ca-3939-b642-519f1686af1c | -10.133 | -44.5777 | 2025-10-16 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 317.3 |
| 2a272579-2066-3705-a9ae-f3928a6d964d | -12.2655 | -47.1121 | 2025-10-16 14:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 4ecdc5f1-7817-35cf-ba86-42267ee77a97 | -6.3733 | -41.4828 | 2025-10-16 14:30:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 205.7 |
| 86993e9a-8de5-3ade-badf-ad1be9feee4e | -6.314 | -45.5174 | 2025-10-16 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 5d727d5e-e634-3abd-a063-236fb39b828f | -12.3032 | -47.1517 | 2025-10-16 14:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 467a48a6-ae1e-3694-9b28-f762092ea239 | -11.5255 | -43.4922 | 2025-10-16 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 89195eb2-e67f-3c7e-8847-1a0a5fad9989 | -9.3596 | -46.9813 | 2025-10-16 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 64a1050d-8af8-3f67-89a2-76ca3c0a8d5f | -7.4717 | -42.6658 | 2025-10-16 14:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 145.4 |
| a216da89-26c5-33b6-9f38-0dcc96adcc49 | -13.4605 | -47.9454 | 2025-10-16 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 6e701de0-8ea2-34d7-9d34-db7e6a1dab0c | -10.6539 | -45.3151 | 2025-10-16 14:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 2c3de9e4-9bf0-3386-93a5-5c8292b36d09 | -11.3603 | -45.2646 | 2025-10-16 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 881c881f-d3ae-3cdd-8863-d1c62960ea2c | -13.4609 | -47.923 | 2025-10-16 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 63ab23ac-07cb-362e-a0d9-259aaa80cb37 | 1.8402 | -55.7034 | 2025-10-16 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 118.9 |
| e0a624c7-7482-3548-9f10-07f86c3d3843 | -6.1385 | -44.2792 | 2025-10-16 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 0d4fb3b0-51f6-3ea8-8fa3-55f16441d872 | -12.941 | -47.9545 | 2025-10-16 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| b1217e98-e352-3c33-ac1b-17c23f8605e8 | -13.2535 | -43.752 | 2025-10-16 14:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| cd4c4926-2332-3a3b-85ac-7dd9de69ead5 | -6.8502 | -44.3807 | 2025-10-16 14:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| b870dfbf-470c-3828-90d4-3ff50b62c84c | -5.1585 | -45.1698 | 2025-10-16 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| ed746967-f17b-36c3-a5a9-04034a894db9 | -6.3328 | -45.516 | 2025-10-16 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 212.4 |
| d3650178-f528-35ee-b350-172d6f0c018a | -10.1524 | -44.552 | 2025-10-16 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 90.1 |
| ad858ab4-fb46-39a1-8f0d-ffffe1d938e2 | 1.8034 | -55.7434 | 2025-10-16 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| f8a632e1-47dd-38b3-a5a6-07034b2bcf2d | -10.5144 | -43.3579 | 2025-10-16 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 336.4 |
| ec164628-d4bf-38b9-9ee5-e72ba370a274 | -9.2694 | -45.2799 | 2025-10-16 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 124.4 |
| f3af8518-ebda-3080-a3c9-c79a5cc99327 | -12.9179 | -47.1078 | 2025-10-16 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| b6549b11-f704-3f8b-9592-268a855599ef | -9.7162 | -44.5149 | 2025-10-16 14:30:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 5c367526-a548-3cce-88ae-0c34f2b41f05 | -3.0386 | -44.4612 | 2025-10-16 14:30:00 | GOES-19 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 74.6 |
| ef3ebebd-1728-32a8-9831-5cca5c0ba21a | -10.1143 | -44.557 | 2025-10-16 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 247.4 |
| 14923790-fb45-32c8-99aa-d02e8ba8ee13 | -10.514 | -43.3815 | 2025-10-16 14:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 223.5 |
| f50a5699-c7c2-354b-8457-b0c1226d6312 | -5.8799 | -43.8844 | 2025-10-16 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| aeb8f1eb-3d0e-3811-a0bc-0b4cfb20c7c6 | -10.673 | -45.3125 | 2025-10-16 14:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 3140bea1-a355-3fc2-a16b-5adc09d5b9e6 | -11.438 | -44.0938 | 2025-10-16 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 153.1 |
| b88d599e-aefa-38fb-8220-c4d6648738ae | -6.4476 | -43.3736 | 2025-10-16 14:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 55da9ae6-1e43-3a54-9f95-4c81ae411b3f | -9.2508 | -45.2592 | 2025-10-16 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 6e99e616-420d-3707-9d29-ff81dcf94e31 | -4.3874 | -43.3827 | 2025-10-16 14:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 314.9 |
| d6796148-112b-36b9-8aa0-27302076a754 | -6.4129 | -43.0958 | 2025-10-16 14:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| cb0587ee-9cb3-34ae-8bbe-2978b45a2c59 | -6.6746 | -45.0357 | 2025-10-16 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| a1dbb698-a7a6-35b6-9297-03a23ffa19cd | 1.8401 | -55.7232 | 2025-10-16 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 125.1 |
| 3d7670fa-f4c2-3bc6-bb3a-bf92bd25431d | -10.5331 | -43.3788 | 2025-10-16 14:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| aad3e2c1-6222-30e6-8d6d-320e41fe1196 | -4.1525 | -42.1989 | 2025-10-16 14:30:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 119.9 |
| 23935887-2354-3f55-ac2b-22c590a56aa6 | -11.4376 | -44.1172 | 2025-10-16 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 216.8 |
| 463e014e-c635-3943-b708-0d6de164b8af | -9.3788 | -46.957 | 2025-10-16 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 119.4 |
| feb55ad7-33fa-3375-9c06-a4f24568c56b | -13.0743 | -46.9717 | 2025-10-16 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 2691ffd9-cd34-3ef8-bf1a-741423a348af | -11.5921 | -44.0472 | 2025-10-16 14:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 134.4 |
| ad0a9c48-b7a1-3b4a-b73b-3c73d345cd0c | -13.1129 | -46.9658 | 2025-10-16 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 3c1168bb-3447-3758-a9cb-3365670f9927 | -12.1547 | -50.3735 | 2025-10-16 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| c52e3807-a534-37ea-ac40-92497d521235 | -4.3687 | -43.3838 | 2025-10-16 14:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 167.1 |
| 3d104ce7-c3fe-349b-aba1-5953ab0215b6 | -11.4197 | -44.0496 | 2025-10-16 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 163.1 |
| 358e3149-8759-359b-b2db-e65442b4c204 | -9.3599 | -46.959 | 2025-10-16 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| d4f8735c-21ae-397f-a2f4-bf7be6132e85 | -4.9429 | -41.7191 | 2025-10-16 14:30:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 108.1 |
| 11de6999-be63-33a8-8f5c-577180a4e3c0 | -5.476 | -42.9602 | 2025-10-16 14:30:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 112.0 |
| 9c2d7596-f0da-34cf-a9c0-2037bad76d6b | -4.3872 | -43.406 | 2025-10-16 14:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 473.4 |
| ac7a23db-d8cf-3dc6-9749-7b7bced8a8c8 | 1.7851 | -55.7436 | 2025-10-16 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 87929640-6103-39ef-a4f8-5a0f23deb655 | -12.284 | -47.1544 | 2025-10-16 14:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| f4b0b4a1-34d9-3bb4-a8e6-3502df745a45 | -6.5646 | -42.9651 | 2025-10-16 14:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 57d7f4c4-7e50-3d27-a36f-2e1fec37ae8a | -8.1717 | -44.0217 | 2025-10-16 14:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 00ddef5b-d8e1-3b0c-b680-0fa6aa1bc74c | -4.3687 | -43.3838 | 2025-10-16 14:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 7185fae3-4ee5-3593-8245-7e771c656a4e | -13.4609 | -47.923 | 2025-10-16 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 04512c34-280f-3a80-af3c-368ce7231424 | -1.3932 | -49.0174 | 2025-10-16 14:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 95adc684-e26f-3bab-894f-51b6d2e1d052 | -6.5903 | -44.1039 | 2025-10-16 14:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| a8c05ae0-7ad7-3260-807d-d0ba1a4b5703 | -10.6543 | -45.2921 | 2025-10-16 14:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 2b983259-6516-3c3b-b735-6e287c4b44f3 | -12.941 | -47.9545 | 2025-10-16 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 5d61b46d-4683-3c77-98d2-82ed461366f7 | -3.7441 | -41.6977 | 2025-10-16 14:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 92.5 |
| b2152021-92bf-3fe0-8a7f-435d00291edd | 1.7851 | -55.7436 | 2025-10-16 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 9d254dc7-50c1-378d-a7f6-78879bbcab2f | -12.2652 | -47.1346 | 2025-10-16 14:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 140.8 |
| ce96bcd0-4198-3567-b6e9-e7a016b29acc | -10.1143 | -44.557 | 2025-10-16 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 178.9 |
| 7a986a6a-7ada-33dc-b857-2f778f84f564 | -7.4837 | -44.8501 | 2025-10-16 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 7b6c0e67-1c38-3171-ac4a-71dadaad30f7 | -6.8502 | -44.3807 | 2025-10-16 14:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| cd44f387-cc95-331e-9516-c966931f4e0f | -13.1133 | -46.9432 | 2025-10-16 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 78.3 |
| e414cb30-ed63-3c63-a488-939236c890ad | -8.2371 | -43.3382 | 2025-10-16 14:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 136.1 |
| d4cbe7ad-0d9b-3be3-8f03-c997b4c9f036 | -8.4714 | -44.1978 | 2025-10-16 14:40:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 99.7 |
| e16a44fb-0bd2-3e5c-b7e9-92fae0dfc2ae | -8.0788 | -45.4298 | 2025-10-16 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 45692bda-b69b-3e9a-a44a-59861b96fb2b | -13.055 | -46.9746 | 2025-10-16 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 1f6919cc-eeff-3def-aeba-0b36565435ef | -4.3871 | -43.4292 | 2025-10-16 14:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 043ec461-10bc-36e8-9f35-975a3df1d01e | -8.2373 | -44.7984 | 2025-10-16 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 336.4 |
| 9bf0e9cf-534e-3a27-baf7-5970c5ef9769 | -13.4605 | -47.9454 | 2025-10-16 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 76e6c46c-b0d8-3b86-9f2c-b814ec3c24e7 | -14.1749 | -47.9477 | 2025-10-16 14:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 4818a1ec-fb34-3a1e-90c1-eb38620beadf | -10.5834 | -47.42 | 2025-10-16 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 0093fecb-6208-351b-a747-b46f49c8b43d | -4.1149 | -42.2248 | 2025-10-16 14:40:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 144.2 |
| ffce6b71-23ee-3660-9331-bccb2bdd48f0 | -12.284 | -47.1544 | 2025-10-16 14:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 6e08383c-586a-3557-a495-237a1862ff85 | -6.4637 | -41.8351 | 2025-10-16 14:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 106.3 |
| a4ce86c5-e449-317f-a4dc-9d1d4c5a25ad | -13.1129 | -46.9658 | 2025-10-16 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 8a785dce-2b9f-37a4-aa59-2b7bd87bb46f | -8.2455 | -44.1528 | 2025-10-16 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 188.3 |
| 36c46275-1694-37c5-a5b3-d9b9808e0d79 | -10.1528 | -44.5289 | 2025-10-16 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 79791721-6bc5-3e45-ad57-71455b309b36 | -8.2558 | -43.3596 | 2025-10-16 14:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 122.1 |
| b5f9e88f-6dfb-3a50-96fe-bfab6a651768 | -6.892 | -43.9851 | 2025-10-16 14:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 244cebdd-e4b3-3a16-9b2c-9118645de0ce | -9.7162 | -44.5149 | 2025-10-16 14:40:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 144.8 |
| 6b875856-a9b5-3a1b-87c9-6c5915d3d5b5 | -10.1333 | -44.5545 | 2025-10-16 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 173.5 |
| 02707216-db3b-3e89-9d89-639284917955 | -12.9716 | -47.3245 | 2025-10-16 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 6a3873ee-1762-3997-bbdf-667e4e3827ea | -5.0597 | -45.8957 | 2025-10-16 14:40:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 72.3 |
| ab4138e4-bc6d-3b63-9871-8d3faa4eb060 | -5.476 | -42.9602 | 2025-10-16 14:40:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 128.6 |
| 2570930e-64b9-3350-ad16-bee79711522c | -13.0743 | -46.9717 | 2025-10-16 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |


[Clique aqui para ver as próximas entradas](README96.md)
