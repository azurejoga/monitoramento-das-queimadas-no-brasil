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
| a7d13728-011d-31bb-a784-b3a9b3bf0cf2 | -13.4463 | -48.11788 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb35a538-7ed6-37c8-82ec-f0c5c5b1758e | -11.59533 | -44.05943 | 2025-10-18 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cc25b638-b3e4-39c7-8937-5bac81634696 | -9.96834 | -43.96692 | 2025-10-18 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a4a200b-95e5-34a3-95e5-c2f7fc375261 | -11.49052 | -44.16615 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bd5a1f0c-ab1b-34f2-b835-3cc97b4202bf | -10.48929 | -43.43728 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 9f6d13aa-5408-3f5f-b30d-c1112b17a701 | -10.82464 | -43.93011 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c5925c7-4181-3f1a-8b2b-13e6fc60ff7c | -8.09762 | -45.43178 | 2025-10-18 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b595af2-52bd-3b5e-8cf3-286d0862a843 | -8.19952 | -43.3098 | 2025-10-18 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 47e042ae-7630-354e-b2ee-4e8ef83c26a7 | -11.48846 | -44.02531 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 381672fc-66a4-3338-b1f5-ecc2dff5a06d | -8.26183 | -44.01768 | 2025-10-18 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4f2fde11-d492-3fb9-a38e-8226e091b691 | -13.77739 | -48.24381 | 2025-10-18 04:02:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| dd723b8a-929e-3d3b-9451-28a0432b6b06 | -10.25255 | -44.03692 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97bc790b-090c-3733-8a15-7f8a2aece9ef | -8.36358 | -46.21362 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5cb8b71c-a33e-37de-aa04-5b58c0b0ad41 | -7.45961 | -42.16816 | 2025-10-18 04:02:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0c3300ea-a7d4-3e8e-a3eb-278192aa51cd | -12.49315 | -45.50679 | 2025-10-18 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1fd62ac0-09a7-3c57-861d-acebde3b8f57 | -7.34622 | -43.85864 | 2025-10-18 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 9820e9c2-07cb-3df1-bd10-cd662d6f92f8 | -10.50123 | -43.36551 | 2025-10-18 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2f74bd81-8142-3ece-b81e-18639f1875c7 | -13.7683 | -48.23985 | 2025-10-18 04:02:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d3fcd848-dfd5-3ccb-a498-9e5cbba0ec76 | -7.88975 | -41.30996 | 2025-10-18 04:02:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| eb4cb348-71c7-300b-a618-033b1afbc215 | -11.36371 | -45.26289 | 2025-10-18 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eef4734e-8403-3bd0-af9b-9b7073bcb5a4 | -10.80552 | -44.02122 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aaa043a1-8f42-3ec1-be8f-44313978dc74 | -10.97822 | -47.93001 | 2025-10-18 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7eba4680-1e0b-3c67-80d2-ab060b763d11 | -12.17838 | -45.07492 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a2335396-df1a-3590-bc10-27a5ffc24c76 | -8.27138 | -48.00487 | 2025-10-18 04:02:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 255af333-3f5d-3d02-af52-905335b9fe3c | -8.04805 | -41.10767 | 2025-10-18 04:02:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 79fd995b-0a09-3ab1-ab2a-d12f97903e55 | -13.96146 | -41.72266 | 2025-10-18 04:02:00 | NOAA-21 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4234b992-934d-3866-827b-86a22c6bc877 | -13.44608 | -47.92015 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8afa485d-a97f-3f28-ab57-6541a5d85c89 | -14.49083 | -44.60873 | 2025-10-18 04:02:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 116305bc-9280-3ac9-aadb-9ddbc180153a | -6.9323 | -43.69578 | 2025-10-18 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 87ffa477-96f3-30fb-9e32-212d6f304d86 | -13.72872 | -48.11136 | 2025-10-18 04:02:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0572cfcc-55e6-328d-9c33-5d76003294b2 | -11.38762 | -44.26217 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f2e14fa-fdb4-3b5c-8ce0-efc00844c834 | -8.16001 | -49.29809 | 2025-10-18 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a02b415-4537-39d6-a525-b96c5bc4ff1c | -7.16185 | -46.21726 | 2025-10-18 04:02:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d54ddfe0-50bd-3ec7-9528-c17c02315514 | -7.44157 | -43.75534 | 2025-10-18 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3bc2fca4-3c4d-3d31-9c8a-7be13204b91d | -11.35545 | -42.5691 | 2025-10-18 04:02:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f5ee5a39-7909-3e7d-b845-068c9f83aa6f | -9.15548 | -37.29921 | 2025-10-18 04:02:00 | NOAA-21 | OURO BRANCO | ALAGOAS | Brasil | 2706109 | 27 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7c8b56a8-4147-3e60-98be-34198e32cb04 | -11.57244 | -44.66325 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2098fdd0-42e5-36a5-95b3-2d2baeac84bf | -7.44368 | -44.74849 | 2025-10-18 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6605f049-069f-320f-b9ae-c6471dd1991f | -11.61541 | -44.09255 | 2025-10-18 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| ca38f325-ff2f-332c-82e0-27ce788ae5c4 | -10.48229 | -43.43611 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ffb3b7c3-5ebf-39df-9516-17cbd28909c7 | -13.70611 | -47.71403 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53af9d83-f258-3c1a-b9c3-25d1be7a7e87 | -9.12449 | -46.61965 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd64ae0e-3368-3ea1-b6dc-fe0d58bd2fd7 | -9.67999 | -44.5427 | 2025-10-18 04:02:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5a5c6ea3-ab47-3c73-8ff7-cc56e8d72c46 | -11.40922 | -44.26587 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f1831bd-2b71-3e8f-b8f4-413cd8ded7e9 | -9.26558 | -43.73978 | 2025-10-18 04:02:00 | NOAA-21 | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d0005548-fad5-34c0-b409-132e424749c8 | -13.67638 | -44.65102 | 2025-10-18 04:02:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9261ac41-c3f8-348c-a46a-83bf22772aa9 | -13.197 | -46.43353 | 2025-10-18 04:02:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1b15db2d-8c3e-3fc2-ad1a-90f106f341f4 | -10.53675 | -43.36739 | 2025-10-18 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75f1409b-835d-3289-a3bc-9cb83497d48c | -13.33028 | -40.46181 | 2025-10-18 04:02:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9a2e246e-94b5-34b4-93fc-e79d5bd49e81 | -7.59645 | -44.96938 | 2025-10-18 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c659b8b7-b580-3080-9377-9c1ee6b46214 | -12.15826 | -45.08047 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4913df6d-76ef-3774-a47c-97ad66e20c46 | -10.55625 | -43.81998 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 367ad385-e355-332e-b0e8-54d76aad6b4c | -10.48428 | -43.42415 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d3b3e273-f1be-30a5-af55-bc1fbea80aed | -7.59002 | -44.98375 | 2025-10-18 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c8e4cf55-046b-3987-9dd3-3d04b628851d | -7.45214 | -46.52516 | 2025-10-18 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59c1c70d-bd1a-3a73-874c-53b8cdbaa8a1 | -13.77024 | -48.2328 | 2025-10-18 04:02:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ec2e9e3-549c-3f7a-b52c-e757044e2168 | -8.10571 | -45.4331 | 2025-10-18 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2f6a47f9-79ae-3ac2-9826-94f501725b4a | -11.95965 | -45.34953 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c230de5-5d14-3d53-b300-5b3912217b98 | -12.90794 | -41.84508 | 2025-10-18 04:02:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| befb1c6e-c5e9-3d61-934e-d4f7199e51d0 | -13.44522 | -47.92487 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8242185d-82c8-3445-bdc8-7bd09aa68be6 | -7.5871 | -44.99549 | 2025-10-18 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ff499b6-3ebb-3bb3-8431-920fd70fe34e | -10.49213 | -43.44184 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 9d06bc55-4f4e-3577-823a-cf73650077cc | -11.36608 | -44.28022 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73c7bc65-9db0-36f5-bc39-658a5d1eb77e | -14.04792 | -44.64909 | 2025-10-18 04:02:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1b9b9be-33e4-3e7e-aae4-1e82beff0970 | -7.76657 | -42.48864 | 2025-10-18 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c0fa5342-c4d8-37ba-ae9a-84639e09d6b5 | -8.58715 | -45.42916 | 2025-10-18 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6287e8c1-23f7-301f-a434-7aa381c03105 | -8.82573 | -49.688 | 2025-10-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37b9268c-f696-3c32-95fb-893522f7a582 | -10.80744 | -44.01858 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e1dec52-65a4-3d4d-9a33-9779060eb585 | -11.00093 | -47.91392 | 2025-10-18 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da1d7de1-5b38-3d75-a975-f0c0c902a0ca | -12.61147 | -42.39885 | 2025-10-18 04:02:00 | NOAA-21 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 172fb7d3-8ddb-3d9e-8c65-684872ab6c8a | -10.6383 | -42.30704 | 2025-10-18 04:02:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c5646f9c-87e0-35d9-913f-efb2ca809472 | -9.98079 | -48.24251 | 2025-10-18 04:02:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7fe5e6f3-a5fb-3bf8-9630-b7f7901c5d76 | -8.77822 | -47.92567 | 2025-10-18 04:02:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a1c09746-e619-32d5-a1ea-ae75d2e87f48 | -7.93219 | -44.12899 | 2025-10-18 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 36f87bcb-fb35-3c6e-b102-5c0896d2bbee | -7.42907 | -46.8954 | 2025-10-18 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 810cc2e3-e0a0-3924-ad5b-6f78f42db435 | -8.88402 | -37.23308 | 2025-10-18 04:02:00 | NOAA-21 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e61a9b47-8401-3b2f-a112-5759a1d437aa | -6.74622 | -47.37175 | 2025-10-18 04:02:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3ebc0b2-ae21-3cd9-94f9-daea03059a60 | -10.23748 | -44.06091 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e967e9ea-aab8-3ae1-bed3-41ed3ca1f367 | -8.04529 | -41.10365 | 2025-10-18 04:02:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a11f5119-38a1-3c1a-8566-4120752c7894 | -12.20618 | -43.56052 | 2025-10-18 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c81579a5-26c3-3a6b-87cd-6797f82276da | -11.48204 | -44.02 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fcfb557-5c66-3b1b-abbd-a25c17fcdb10 | -12.1703 | -45.05518 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d36970c-5006-3c89-b998-7e75c0907dec | -10.10969 | -44.55634 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 064380a0-b95a-394a-bfb5-928ef5fff2eb | -8.56652 | -45.42923 | 2025-10-18 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61c77d88-c2f1-3578-bc5c-bd4b093226ea | -10.25117 | -44.04535 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b10bf42-a052-369c-8070-e39ed32f4f6d | -10.12833 | -44.53637 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87e3cc82-48b6-3b68-8669-d1492240e336 | -9.0054 | -47.8419 | 2025-10-18 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a91d7103-8cf6-3fd4-95e8-1008ad6b48a5 | -9.58872 | -42.32707 | 2025-10-18 04:02:00 | NOAA-21 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 45fcc645-eac2-35a8-ae74-ccb14bbbdd46 | -9.88181 | -49.11781 | 2025-10-18 04:02:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d0668d5-9a19-37e1-9ce5-aae4e55ad427 | -11.3761 | -45.27737 | 2025-10-18 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9369f76b-de06-3b66-97e3-a8f651d43545 | -8.82604 | -49.67813 | 2025-10-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64a2fdd8-1c3b-311f-823a-846350d23206 | -11.09927 | -44.7066 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4fe86527-b3b1-32ed-9691-a6b05e5f0ccf | -10.6324 | -45.23437 | 2025-10-18 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2c812a52-956c-361f-a354-7b356fc45055 | -11.84521 | -38.19908 | 2025-10-18 04:02:00 | NOAA-21 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 53a1ce27-9ff8-348c-8fb2-ff57c35c61e0 | -9.38208 | -46.91092 | 2025-10-18 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 19f6eef9-fb89-322d-b6f9-bbcda82b2399 | -14.1313 | -44.71418 | 2025-10-18 04:02:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42b4abab-92f1-3a8a-96d9-11d4d23d8931 | -10.49563 | -43.44242 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 34.8 |
| af651641-d10a-3d4e-b4da-dcc1472bbf93 | -12.15706 | -45.07697 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9c6a247-6e90-34ca-8627-aa4b87d279bb | -11.13508 | -45.07258 | 2025-10-18 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 86a15b1d-b1b9-32b0-ae3c-01bc6d1be2cf | -10.48702 | -43.40779 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README24.md)
