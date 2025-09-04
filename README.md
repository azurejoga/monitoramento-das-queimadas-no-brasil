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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e428fecd-89eb-3594-b83d-e9cc056276da | -2.962 | -49.3437 | 2025-09-04 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| c40f2bed-c6f5-3d0e-8cf7-d3e5ecc059e5 | -6.7649 | -63.1292 | 2025-09-04 00:00:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 619a7333-b0b4-3b86-b140-a4a2394f75e1 | -15.7475 | -49.9806 | 2025-09-04 00:00:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 234b4cf1-5156-37fe-9895-adbba28992a2 | -2.9434 | -49.3655 | 2025-09-04 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| f1edeb4c-bab1-3cad-aeb2-ad16bb393948 | -16.3133 | -45.6927 | 2025-09-04 00:00:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 4f008fb0-97af-37a0-b2d0-b8d7ea45213f | -6.7465 | -63.1297 | 2025-09-04 00:00:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 3c172e61-5008-3a6e-87d8-7d05098dffbf | -7.6492 | -63.1008 | 2025-09-04 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 715b4508-c46a-3b4f-8e0c-8416429986b3 | -7.6306 | -63.1203 | 2025-09-04 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| f19b70b9-421a-37dc-a788-ea4572bd5f96 | -11.6409 | -54.5315 | 2025-09-04 00:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 07a2745e-f4d0-357c-89ce-cdc89ed04008 | -6.7782 | -44.0876 | 2025-09-04 00:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 1e824f61-6dc1-38cc-ae21-14f9e86caefb | -8.6603 | -68.7657 | 2025-09-04 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 7dbcec4c-41a1-36a2-b997-28bbaecde21f | -11.6599 | -54.5297 | 2025-09-04 00:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 135.1 |
| 656e4cb0-9b08-38b9-bd68-29e23fb72b57 | -11.5779 | -52.115 | 2025-09-04 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 41f2c353-10b9-3050-98ad-dde674a7346e | -23.3053 | -46.1614 | 2025-09-04 00:00:00 | GOES-19 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.7 |
| cad2bbdf-666b-3d68-942f-56abb20053e0 | -18.151 | -51.7719 | 2025-09-04 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 420.2 |
| e1515a02-e071-3a8e-af95-d6c38ef72c35 | -6.7832 | -63.1474 | 2025-09-04 00:00:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 723094ad-f5f5-37f2-852f-1c42d9354f67 | -10.4475 | -50.3499 | 2025-09-04 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| ec761f1a-8fd1-3263-9427-1b2b4e1d364e | -9.4833 | -47.6104 | 2025-09-04 00:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| d1821e0a-1511-3646-9055-13f911c29347 | -11.8708 | -51.5357 | 2025-09-04 00:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 51.7 |
| db50c709-3128-3e1e-a9b4-543a3cc32795 | -12.9859 | -54.7891 | 2025-09-04 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 104.6 |
| c6d13545-4367-3c24-a8d3-22fc88c261a0 | -6.7833 | -63.1286 | 2025-09-04 00:00:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| aa290dec-526d-3187-b0f7-a403642c86a2 | -10.4661 | -50.3693 | 2025-09-04 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 5056f8f9-9def-3548-a03f-a62db3830635 | -13.75 | -46.9346 | 2025-09-04 00:00:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 101.8 |
| e42d512e-22dc-3978-839c-eb74162b1819 | -7.6851 | -48.7386 | 2025-09-04 00:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 52a5cb41-0dcd-3c11-b678-6711eaa1c7e8 | -7.6491 | -63.1197 | 2025-09-04 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| afad4dca-c7e9-3f37-b7ab-0e42ee8653e2 | -10.5316 | -57.7747 | 2025-09-04 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 3a6f7d90-87b9-31bb-ba47-68d88c57db9e | -7.6307 | -63.1015 | 2025-09-04 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| f0f058a2-b371-3c7e-8ab1-9886cb334318 | -4.9951 | -56.256 | 2025-09-04 00:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 286c877e-377a-3f3e-85b4-a8ce30db84e1 | -11.8899 | -51.5336 | 2025-09-04 00:00:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| b6264a82-a801-378d-9974-8adaa1cb9970 | -18.1305 | -51.7971 | 2025-09-04 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 251.2 |
| 15e39039-4d83-3a46-b306-1d7d9bbd70f8 | -17.1688 | -46.2651 | 2025-09-04 00:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 03bb3285-5392-36cd-86d3-fad1c6a560af | -10.4664 | -50.3479 | 2025-09-04 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 1be59475-9079-3334-9695-896fb679655e | -12.6341 | -56.9926 | 2025-09-04 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 44.7 |
| c51bb004-2b55-3bae-b00f-d8aa17611d9a | -5.6081 | -45.0038 | 2025-09-04 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 34730575-ed27-3f42-b217-38e027e1ebbc | -12.9668 | -54.791 | 2025-09-04 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 886fb232-65a5-3d14-aa43-53f7e913ea56 | -11.2005 | -55.0195 | 2025-09-04 00:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| e99b2992-3a9f-32cb-b275-24d72abc1f4e | -6.7933 | -44.4316 | 2025-09-04 00:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| c2a79ccf-e7ba-33ef-9dc0-1f9378eb3ee6 | -11.2318 | -44.9604 | 2025-09-04 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| ca6d0ce3-9125-3dc7-b7fb-9ac5bd8cf050 | -22.7299 | -50.5522 | 2025-09-04 00:00:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.2 |
| db809647-8b57-3186-9301-b54905246954 | -10.4472 | -50.3713 | 2025-09-04 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 205.3 |
| 713cb826-68c7-315c-855f-3fc854211ca4 | -13.7495 | -46.9573 | 2025-09-04 00:00:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 5568d2ca-f32f-3de3-8c48-181a284b7fc6 | -10.4469 | -50.3926 | 2025-09-04 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| e88dd130-0dfa-39be-87a8-b85a766b23b3 | -18.1505 | -51.7937 | 2025-09-04 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 339.3 |
| 51789ba5-2cbe-30ab-81f3-4f98f17576cc | -12.9861 | -54.7685 | 2025-09-04 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| f7bd0caf-0cc1-3ba3-a515-a64099763621 | -2.9619 | -49.365 | 2025-09-04 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 69e894d2-30ad-3c3a-9908-876fa81af208 | -8.6604 | -68.7473 | 2025-09-04 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 91890688-a69d-38c3-a381-00d8e1dd48b9 | -17.1888 | -46.261 | 2025-09-04 00:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 82.2 |
| c987dcc2-7fc4-30bb-8b20-3fb86d1b97a5 | -5.6079 | -45.0265 | 2025-09-04 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 214.9 |
| 34850beb-50e3-349e-9dd5-c34a010f197b | -12.967 | -54.7705 | 2025-09-04 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| e61cfabe-4ef6-3da6-8dfa-6cb1d03190d2 | -6.7931 | -44.4546 | 2025-09-04 00:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| f8bda8f1-1060-35e4-890e-b95770485d66 | -7.7066 | -50.3188 | 2025-09-04 00:00:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| b7259a92-edec-380b-a246-ad47d65dd75a | -5.6266 | -45.0252 | 2025-09-04 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 7ad20acf-a673-3a2b-803f-dfbfedf898cb | -18.131 | -51.7752 | 2025-09-04 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 306.7 |
| afa60bde-1057-36b9-b640-6cab3784a5b4 | -8.0917 | -42.429798 | 2025-09-04 00:04:00 | METOP-C | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 126389a4-5ef3-347e-9359-32552de0ade8 | -6.7633 | -44.0877 | 2025-09-04 00:04:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2dccb512-1694-3d75-b37f-c23938e39eef | -8.7305 | -47.074699 | 2025-09-04 00:04:00 | METOP-C | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 638bdbb0-ff06-3dd2-8f13-d7c1f84b75ce | -13.4395 | -46.937901 | 2025-09-04 00:04:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ad731c0e-ffc7-39c4-904a-b9dc3b169eef | -7.6882 | -48.738098 | 2025-09-04 00:04:00 | METOP-C | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| daf00b81-0f2c-3530-93d9-b80065692fed | -9.0582 | -46.990501 | 2025-09-04 00:04:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ccb5c5a4-ce7c-370f-acf6-d6578ed9cec1 | -13.7519 | -46.936699 | 2025-09-04 00:04:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| df9f1505-8ce1-3025-8127-e84eadf8b269 | -5.9844 | -43.8125 | 2025-09-04 00:04:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 966221a6-3d26-30c4-af2f-c80c9fcd11c3 | -6.2031 | -41.798698 | 2025-09-04 00:04:00 | METOP-C | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d3ad8333-e182-3127-a290-29194c95f09c | -2.9517 | -49.320599 | 2025-09-04 00:04:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 497c3a41-c85c-3f3c-8f0e-f72b55ff9817 | -11.2319 | -44.9636 | 2025-09-04 00:04:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 02aacdb5-d11f-392f-8ae4-2cc2e109edb7 | -2.9559 | -49.3396 | 2025-09-04 00:04:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9a1345c-5d05-3475-b8bf-3dbec3e2e21e | -7.496 | -44.817101 | 2025-09-04 00:04:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b9e8d89d-9ae8-3421-a16b-d8415537e2e8 | -5.4743 | -45.215698 | 2025-09-04 00:04:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5b255ec4-d487-3ae6-bba1-e552c1c8566b | -5.9721 | -44.127701 | 2025-09-04 00:04:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0e539b0d-ef45-3bd1-941b-ba228b96dc83 | -3.8012 | -44.1092 | 2025-09-04 00:04:00 | METOP-C | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 82c37bf7-5cb0-3aef-a654-4f55b9266a16 | -5.6968 | -45.1563 | 2025-09-04 00:04:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 941d798c-3def-346f-b02c-553e8a7686bc | -11.3754 | -43.545799 | 2025-09-04 00:04:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 61c15e47-491f-3628-b3f0-40ad4fd56fef | -3.811 | -44.106998 | 2025-09-04 00:04:00 | METOP-C | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 30f85f83-9a10-3f37-bec6-260eb27f73f4 | -11.0446 | -45.388302 | 2025-09-04 00:04:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 07558d00-29d6-3e67-99e3-6526acc3f714 | -6.7312 | -42.273499 | 2025-09-04 00:04:00 | METOP-C | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6d19e2fe-70ea-3c6d-9f1a-c4f4eed19ac0 | -6.7675 | -44.107101 | 2025-09-04 00:04:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 56fd99bf-b056-3b19-818a-59b0b8fd9242 | -6.7927 | -44.081299 | 2025-09-04 00:04:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b65f50d9-d795-384e-b027-f234914fd75f | -10.9059 | -50.906799 | 2025-09-04 00:04:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 56e5496b-3e77-3177-92b9-73969099d5d6 | -6.7907 | -44.4464 | 2025-09-04 00:04:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 63877b6b-e969-3e4d-b9a9-fba2d0974507 | -11.0571 | -45.400002 | 2025-09-04 00:04:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cf555d53-37a3-3993-b15e-d81f5b96c914 | -13.4457 | -46.917099 | 2025-09-04 00:04:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4f5cf5c4-0301-3eeb-ba28-405557c3df8a | -7.4473 | -42.026402 | 2025-09-04 00:04:00 | METOP-C | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cba02ca9-ee03-39cf-b413-b7fedffa3598 | -6.2145 | -41.804001 | 2025-09-04 00:04:00 | METOP-C | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6b0a0c1c-9a5e-3184-9245-85b3b656835b | -4.5107 | -41.964401 | 2025-09-04 00:04:00 | METOP-C | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 089d22a9-d666-3a85-a48d-f5bc44d80031 | -8.0706 | -45.3493 | 2025-09-04 00:04:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| eba585a2-befa-3f12-b684-54879dfc3bf6 | -12.5041 | -48.047401 | 2025-09-04 00:04:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c9f8537b-f00c-3c79-a8b6-3896de432ba2 | -5.5312 | -43.759399 | 2025-09-04 00:04:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 87ea744c-9812-3cff-b89e-9770da7f85ed | -6.7752 | -44.0952 | 2025-09-04 00:04:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a23e20e0-14ed-308b-aa20-02c163fd8d42 | -6.2129 | -41.796501 | 2025-09-04 00:04:00 | METOP-C | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0e350866-c235-3c00-8d20-664584b934b9 | -7.6839 | -48.717499 | 2025-09-04 00:04:00 | METOP-C | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 81c61b84-dcdb-352e-b6d3-61fa49cff5b4 | -5.7812 | -43.222099 | 2025-09-04 00:04:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4472467d-41a9-388d-a836-fd1710134a7e | -12.5067 | -44.728199 | 2025-09-04 00:04:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d781ab4a-363c-3be0-a468-7b96659e42bc | -12.4847 | -48.051201 | 2025-09-04 00:04:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1fff10f3-a534-3f8c-834d-f7c85326b4b0 | -12.4986 | -48.071201 | 2025-09-04 00:04:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a7208823-0177-3d27-ac0c-5fc25eacf3eb | -10.4536 | -50.321602 | 2025-09-04 00:04:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ac8b5cbe-a6af-359b-839d-70b33601cfa3 | -11.0466 | -45.150902 | 2025-09-04 00:04:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 60fd832a-0522-36fc-8051-c18dd2f3d0c4 | -11.0474 | -45.402 | 2025-09-04 00:04:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4c78bb38-72f1-3b5e-87b2-1f3bb874e522 | -8.0899 | -42.4216 | 2025-09-04 00:04:00 | METOP-C | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| dc1ef262-cdb4-36b6-8be1-878f5566ab82 | -11.0439 | -45.137798 | 2025-09-04 00:04:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 151ead22-83f6-3dc0-a029-4a84ade34a07 | -6.5427 | -42.9501 | 2025-09-04 00:04:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9a9d7fe7-a271-320d-b64f-35319f679632 | -6.7731 | -44.085499 | 2025-09-04 00:04:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
