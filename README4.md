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
| 2b9f0faf-1501-3bb5-90a3-6e246a3cc877 | -11.12812 | -45.11899 | 2026-05-15 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c32bbb01-fcdc-3ab9-b2b2-344c93c46557 | -19.92678 | -54.74634 | 2026-05-15 04:19:00 | NPP-375D | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 491dad81-b467-3142-8d9d-f8f204dd8a0b | -11.12464 | -45.11838 | 2026-05-15 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9c2c87ae-f6f6-38b7-9abd-84f52dbce38b | -10.64963 | -42.31602 | 2026-05-15 04:19:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fb50c95d-4978-3ee6-a99f-83bbf211b6cf | -15.64363 | -47.93796 | 2026-05-15 04:19:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2cc8c45-ec3c-3862-8cd9-156fb504701b | -9.81587 | -48.52293 | 2026-05-15 04:19:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a01988be-b65f-3b15-b56c-0a67cf1ee80a | -11.75395 | -47.06831 | 2026-05-15 04:19:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94ec631a-4245-37b5-b6cc-1e928ccb6487 | -12.05137 | -45.27805 | 2026-05-15 04:19:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a541fc5-96b8-3e75-a36b-650d8200e7ce | -11.75648 | -40.14413 | 2026-05-15 04:19:00 | NPP-375D | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f6f5ed46-f595-30dd-b6a8-db5a8a36d0cb | -10.40668 | -44.93837 | 2026-05-15 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 47d965ae-db72-381a-a3de-683d58c85ccc | -17.07353 | -43.69376 | 2026-05-15 04:19:00 | NPP-375D | GUARACIAMA | MINAS GERAIS | Brasil | 3128253 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3db7a144-4dfd-34ed-a38a-db4073395fae | -11.03113 | -42.83554 | 2026-05-15 04:19:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 45b385d1-b7ac-3247-a758-cd8dd3c7aebb | -10.64731 | -42.31571 | 2026-05-15 04:19:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 42e5ff02-1bc9-35cb-af98-f9e44ecefbef | -10.64786 | -42.31219 | 2026-05-15 04:19:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2ad4aa32-1acd-3d02-9b60-7b0c102fe2ab | -10.56022 | -42.43509 | 2026-05-15 04:19:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1ef501d1-82b9-3b06-8988-189a666ab408 | -10.64675 | -42.31923 | 2026-05-15 04:19:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c09cb75c-39f3-3762-b1ae-f223d7d5ae23 | -11.12748 | -45.12286 | 2026-05-15 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 037457d6-c70f-3ebd-9a77-2442c9f92aba | -11.75708 | -40.14 | 2026-05-15 04:19:00 | NPP-375D | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c91f4cbf-d659-3c19-99ce-44054c2dffed | -15.64824 | -47.93394 | 2026-05-15 04:19:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee6c43ec-da4f-357d-b18a-436b92744a66 | -10.61568 | -39.43023 | 2026-05-15 04:19:00 | NPP-375D | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 520c0e13-cd2c-3bf8-b192-3aa15d23f455 | -19.93216 | -54.74746 | 2026-05-15 04:19:00 | NPP-375D | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 330cc3ce-6af7-3e29-b087-72945dba8d1d | -11.75776 | -47.06898 | 2026-05-15 04:19:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 024da5f1-d56b-3ef4-918b-dc09d642b65a | -12.05072 | -45.28193 | 2026-05-15 04:19:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9c0252f-fa18-36fa-8642-54cfad94d532 | -10.6707 | -49.69801 | 2026-05-15 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9976af60-869d-3212-8cd7-7fee7a5cb1d8 | -11.44967 | -39.28891 | 2026-05-15 04:19:00 | NPP-375D | CONCEIÇÃO DO COITÉ | BAHIA | Brasil | 2908408 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f0338e4e-dc53-3ec8-8b62-d9eafdb178bd | -11.03695 | -43.83727 | 2026-05-15 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1d9dd7c7-a1df-3c23-b8cc-f86513b3e3a6 | -15.63986 | -47.93717 | 2026-05-15 04:19:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf34e5af-f0bf-33f6-a4d2-9870a2250315 | -10.92639 | -44.17659 | 2026-05-15 04:19:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5fe46d9-1096-35d5-a00f-ec8c0ba0d0d7 | -10.9206 | -44.19066 | 2026-05-15 04:19:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17542f2f-c435-3ace-8cdf-5028d2c59ac0 | -9.14466 | -49.8377 | 2026-05-15 04:19:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 444dc056-3613-3b86-bcb6-71c954748eac | -11.63287 | -47.8794 | 2026-05-15 04:19:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0133e131-4ce9-3061-a4b8-40ed959d5ec0 | -10.55301 | -42.43754 | 2026-05-15 04:19:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| b894f5ab-d945-3e43-a083-76695e2529c6 | -9.45774 | -47.82154 | 2026-05-15 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 590d9d99-4366-3f65-a499-7782b4bb6b8c | -15.64278 | -47.94279 | 2026-05-15 04:19:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07852f43-4d25-3e2c-984a-6b4f337c756c | -10.65296 | -42.31656 | 2026-05-15 04:19:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| eb5dccab-fdc9-3658-8a13-0c2fbfc52b43 | -16.64946 | -43.67933 | 2026-05-15 04:19:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1f4cf619-540d-316f-8457-7a6600f4cc81 | -10.64908 | -42.31954 | 2026-05-15 04:19:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ab108bea-1550-380c-bac3-9272cd5dfedb | -10.67156 | -49.69325 | 2026-05-15 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 603808fc-2b2d-39af-b2ee-de28792c7db3 | -11.12904 | -45.1351 | 2026-05-15 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f120bd78-c1ce-35a3-98d0-93ddba5fc4c9 | -11.03637 | -43.84088 | 2026-05-15 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 026aa9e4-843f-3101-9319-7ce06356b957 | -10.66355 | -49.71143 | 2026-05-15 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2068ea0b-69c8-346c-8aa4-72d1788de75a | -11.86472 | -43.86249 | 2026-05-15 04:19:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f11aef84-79d8-3652-91a2-bbaa87c097a6 | -10.65074 | -42.30898 | 2026-05-15 04:19:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 558825bb-e6b6-3d83-8b11-1defdec3d1cf | -17.66536 | -44.76152 | 2026-05-15 04:19:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| faf11e74-a924-33e4-860d-6f77b72688ad | -11.86414 | -43.86607 | 2026-05-15 04:19:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ec96201-1127-3450-9b99-6e94af35fbfc | -10.66697 | -49.69239 | 2026-05-15 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22d0c771-788d-34fb-b493-90ec4ba9f162 | -15.64909 | -47.92909 | 2026-05-15 04:19:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3bc3765-2d6d-3200-b9dd-370966b580b6 | -10.65019 | -42.3125 | 2026-05-15 04:19:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0e0ea890-152d-388d-9804-e5520cbcbbcd | -10.55689 | -42.43456 | 2026-05-15 04:19:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fd63addc-75d3-3cdc-8cd4-f9e43195fab7 | -12.05484 | -45.27865 | 2026-05-15 04:19:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41b2ccad-906e-35f6-8b53-86ede3b869a5 | -11.63689 | -47.8801 | 2026-05-15 04:19:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23334784-5537-3d4d-b327-ef6774312d3d | -15.6474 | -47.93877 | 2026-05-15 04:19:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f890348c-0b43-3109-94bf-9a352f4393b4 | -11.76157 | -47.06965 | 2026-05-15 04:19:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 857ad7db-b601-3b9a-aa8f-23ca723457de | -10.55634 | -42.43807 | 2026-05-15 04:19:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 067046cd-2845-38e0-888b-e569f04df82d | -9.4578 | -40.3392 | 2026-05-15 04:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 71.9 |
| 8c70eda8-2dbf-3750-85b8-b320b4808165 | -9.4769 | -40.3365 | 2026-05-15 04:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 106.9 |
| 46ea2d41-a57c-3856-8c49-6cafb39d3fa7 | -31.55498 | -52.74734 | 2026-05-15 04:23:00 | NPP-375D | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 020be479-b9f6-3727-a649-6d7760e89cdb | -9.4578 | -40.3392 | 2026-05-15 04:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 66.1 |
| eb44090d-efce-3ab5-8e2d-f4e5402977e1 | -9.4769 | -40.3365 | 2026-05-15 04:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 71.5 |
| 3aa6cdeb-b903-36fb-99e4-1bcec1554e78 | -6.95499 | -44.53795 | 2026-05-15 04:34:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25fb5c23-fc6f-37bd-908f-143cd08ded31 | -7.13278 | -44.06009 | 2026-05-15 04:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 123d970d-6b1c-300f-a947-b6b7d5851ce0 | -6.95118 | -44.53937 | 2026-05-15 04:34:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71a92d51-a73f-363b-a021-648d5d37801d | -6.95182 | -44.53507 | 2026-05-15 04:34:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b025d2e-3482-3891-9d73-1c1b36dd8486 | -6.38881 | -44.1791 | 2026-05-15 04:34:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 484cd359-14a3-3373-944a-91fb1d69d29c | -6.95546 | -44.53565 | 2026-05-15 04:34:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 97eeea5b-fc92-3dae-a665-e698cb192c8f | -6.95135 | -44.53736 | 2026-05-15 04:34:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00baf616-6355-3a7b-a7ca-f3abc3a73906 | -6.93812 | -44.27876 | 2026-05-15 04:34:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dfa0c0f1-661a-3d21-b6e7-5f54ef4f9653 | -6.64079 | -44.4896 | 2026-05-15 04:34:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0bba4b1-f92b-3cb6-a3b1-c29a2fe3d119 | -6.38946 | -44.17474 | 2026-05-15 04:34:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff559dba-ffdf-3ef9-8cbe-5eca1065f7b7 | -6.64139 | -44.48854 | 2026-05-15 04:34:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 994fa979-9021-3cf6-8568-28b21ab06354 | -6.63775 | -44.48795 | 2026-05-15 04:34:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b2f7d69-3c6d-3880-b2be-51397aa9a557 | -6.63715 | -44.48903 | 2026-05-15 04:34:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79ce66fe-6f6a-321d-8644-b2db956d5fac | -7.13401 | -44.0585 | 2026-05-15 04:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d31ce70-331a-344d-b6aa-9cce868466ae | -10.40486 | -44.9386 | 2026-05-15 04:36:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 67465760-720d-399b-9d37-eed86fcc34fd | -11.73828 | -44.52047 | 2026-05-15 04:36:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 67bb57b4-2e2c-35e6-bdf7-36423790b826 | -12.8557 | -43.75777 | 2026-05-15 04:36:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 56a29262-f979-3739-9606-cb763848ce5e | -11.30811 | -54.03245 | 2026-05-15 04:36:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32e49ea2-2156-3964-a233-0a368e4c7984 | -11.75558 | -47.07066 | 2026-05-15 04:36:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 615bbd1e-eccb-3555-9510-8e49f688fdbe | -11.31149 | -54.03682 | 2026-05-15 04:36:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 82440bb8-c0db-3aed-9b68-147395e3726e | -11.93936 | -47.8811 | 2026-05-15 04:36:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0034939d-c47b-3252-bc11-dfd4a2839094 | -10.66224 | -49.71082 | 2026-05-15 04:36:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c3ac354-95e2-3839-81c1-1f1d82594d5a | -12.59957 | -44.50646 | 2026-05-15 04:36:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2cf7c902-f771-3743-b365-850bac6fe535 | -10.64958 | -42.31453 | 2026-05-15 04:36:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dcdf3903-c7fb-3254-9e5d-3ea7dbf7a5fe | -11.12451 | -45.11909 | 2026-05-15 04:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eab28983-7a1a-36c3-a439-8ba56ba33229 | -10.64576 | -42.30957 | 2026-05-15 04:36:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 03dd2cbb-8a60-37d0-9ecf-e03b1af809f9 | -10.40302 | -49.44256 | 2026-05-15 04:36:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9575c683-af14-37b7-96c3-c141b04649f2 | -11.12757 | -45.12416 | 2026-05-15 04:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e4569cac-240d-3e34-9f7e-98e1fb9fd067 | -11.06353 | -52.45229 | 2026-05-15 04:36:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 819d08c1-9ead-363c-b282-226f5e43adc2 | -11.12823 | -45.11961 | 2026-05-15 04:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f1d3b3e9-21ef-36f2-beba-5caf03c1fef4 | -10.66903 | -49.68998 | 2026-05-15 04:36:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8b10b7c-d0be-3588-bb52-6ab5eed3bcbc | -10.55621 | -42.43876 | 2026-05-15 04:36:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 57f766fc-8052-3104-a1af-30e56c926ca8 | -12.04405 | -45.27985 | 2026-05-15 04:36:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff459f4f-a61a-34e1-8d4d-75a60515b406 | -10.5568 | -42.43447 | 2026-05-15 04:36:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7f66169a-f199-3591-a0da-9dc50f6045a5 | -11.759 | -47.0712 | 2026-05-15 04:36:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f73642d6-d3ca-34f1-b71f-c26508f1e149 | -12.60349 | -44.50705 | 2026-05-15 04:36:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1d57ecb6-8f48-3685-be36-193114ab6688 | -12.6042 | -44.50196 | 2026-05-15 04:36:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f44d0f1d-24dd-3252-8ad3-1dbad5420399 | -12.47685 | -45.43702 | 2026-05-15 04:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6aa3f962-72d9-36b9-ae04-f3b6c54c35a3 | -10.64459 | -42.31825 | 2026-05-15 04:36:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b6ee6aef-0c68-31c9-8268-fa48180f30cd | -11.20806 | -46.873 | 2026-05-15 04:36:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b7f3273-3527-3273-88e9-6684f409e7ef | -10.66501 | -49.71494 | 2026-05-15 04:36:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README5.md)
