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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ff561cb-b0bc-3a34-9ec0-d92df91798e2 | -8.5096 | -43.310299 | 2025-07-10 00:11:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 60cdfd61-0b6c-3cc6-92ab-4fddf3ac67e2 | -3.749 | -47.107399 | 2025-07-10 00:11:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b696baa1-1be1-3817-8573-16386a93113f | -10.5827 | -49.1199 | 2025-07-10 00:11:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f02353e5-e1ef-396f-915c-23c26d488a6c | -8.5025 | -43.280399 | 2025-07-10 00:11:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b26bc7f9-2280-361e-9632-a87523c414f5 | -5.0618 | -43.723598 | 2025-07-10 00:11:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ca0fb238-43b3-38f2-8f33-1f684c952bf9 | -7.4654 | -49.391499 | 2025-07-10 00:11:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09a1fffb-c160-3aac-a9c0-33deb9938712 | -19.4559 | -48.527401 | 2025-07-10 00:11:00 | METOP-B | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6e423dd0-2cbd-3cc5-9318-305310d3b2eb | -14.8645 | -45.119701 | 2025-07-10 00:11:00 | METOP-B | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 35f03ec0-01ba-3cf0-bf4b-84bcecbead2d | -23.114799 | -47.195999 | 2025-07-10 00:11:00 | METOP-B | INDAIATUBA | SÃO PAULO | Brasil | 3520509 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a8a76dc1-11d3-378d-9fca-29db0ff58a38 | -11.4568 | -45.1049 | 2025-07-10 00:11:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3e35ad57-002c-31e8-b9ac-8677dbe77b8f | -7.1997 | -45.341202 | 2025-07-10 00:11:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 50e0676b-54d0-339c-9814-2a7b2243ac7c | -6.0918 | -47.304501 | 2025-07-10 00:11:00 | METOP-B | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 083fb37f-cf3a-3ebe-a49b-48c80a3d0e2c | -8.7375 | -47.155701 | 2025-07-10 00:11:00 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3dc9198a-a74a-370b-8d18-0196ba8c3285 | -10.6189 | -45.229599 | 2025-07-10 00:11:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a75da1c7-4111-3776-89a2-a4c3ef2919e9 | -13.3403 | -52.8885 | 2025-07-10 00:11:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 851a284c-abc9-3795-961c-0ec793249ef2 | -5.4178 | -46.0653 | 2025-07-10 00:11:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6f0e28a6-853c-328a-aa52-6c7853649cf8 | -11.4649 | -45.095001 | 2025-07-10 00:11:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d343723c-d182-393d-925e-a935578bbd8f | -10.6305 | -45.234901 | 2025-07-10 00:11:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b65aa71a-a10e-370a-9c12-5036f675c94a | -8.3612 | -43.950298 | 2025-07-10 00:11:00 | METOP-B | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c3f00804-2bf7-3ee0-8266-fa09229b345d | -10.6205 | -48.071899 | 2025-07-10 00:11:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9443557f-853e-3010-9de0-9d103a0cfea9 | -12.5618 | -52.2034 | 2025-07-10 00:11:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9c971fda-ece9-3ebd-88fd-6ead80ab6c87 | -6.6755 | -46.291 | 2025-07-10 00:11:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 254a3412-793a-3e76-bb0f-aa10a4622f78 | -12.4219 | -43.705502 | 2025-07-10 00:11:00 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 75d4583f-c25a-3990-bf85-ffb2c58a0eeb | -12.4357 | -43.7201 | 2025-07-10 00:11:00 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a9c5194e-3b2a-37fb-9795-46a9330755f6 | -8.5049 | -43.290401 | 2025-07-10 00:11:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c2f838cf-a191-3c6d-a786-f3e7535f62f8 | -11.8824 | -46.7542 | 2025-07-10 00:11:00 | METOP-B | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3414930f-661a-3866-9501-9e70a3f03905 | -13.2885 | -49.147999 | 2025-07-10 00:11:00 | METOP-B | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 89c912d1-90d1-3488-82a8-de4ffc666a31 | -9.214 | -48.598499 | 2025-07-10 00:11:00 | METOP-B | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 63cf6a99-0571-39ce-8c56-65028e8a9583 | -6.8529 | -42.8004 | 2025-07-10 00:11:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b542bdf1-905f-3328-bf6e-ea3ad831371d | -7.9531 | -49.6446 | 2025-07-10 00:11:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c3e290f-04fe-335d-8f4a-c4e634c8f027 | -6.9899 | -43.5116 | 2025-07-10 00:11:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fd0ab757-1ef2-3034-a149-3feb32e7b6cb | -12.4239 | -43.714001 | 2025-07-10 00:11:00 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 97393024-04d2-3e07-a15f-dfeaf921c36a | -5.4876 | -45.337502 | 2025-07-10 00:11:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 473b3346-7205-375c-88b1-be45e97b4270 | -6.5504 | -43.614799 | 2025-07-10 00:11:00 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ef5d5dd-2bc9-32dc-a089-c57fcbc4ae12 | -6.9925 | -43.478802 | 2025-07-10 00:11:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a5e142a8-20ed-37cd-9f77-f702530a3fe0 | -4.2234 | -47.199902 | 2025-07-10 00:11:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 62dc3c6a-30b3-3e3a-a335-1a9d58eddef8 | -8.9583 | -47.266499 | 2025-07-10 00:11:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a0ab7589-05e3-3b0e-acd2-4375b190f706 | -18.6472 | -55.681301 | 2025-07-10 00:11:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 981265ba-4b9f-3f26-a2d9-c195d0db6c0d | -6.0903 | -47.297501 | 2025-07-10 00:11:00 | METOP-B | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a699e8d-8051-3675-8894-3faafcfbee09 | -7.7104 | -45.7682 | 2025-07-10 00:11:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e0a5c37f-e932-381c-bd6f-6574ca3b0ec6 | -10.8818 | -46.748199 | 2025-07-10 00:11:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 721027da-8769-3dc9-bccf-9cbc53f49872 | -13.333 | -52.902802 | 2025-07-10 00:11:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1f8553ab-f8e3-3e55-969b-2a092586f09b | -8.512 | -43.320301 | 2025-07-10 00:11:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4ce49026-15f0-360a-a151-377d527c57e6 | -8.488 | -43.262699 | 2025-07-10 00:11:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d421cfae-c093-39bb-b19e-9500031e645c | -10.5663 | -49.138901 | 2025-07-10 00:11:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 78b97a2f-e879-3228-8cb1-c7596d70e4bd | -5.6208 | -44.000401 | 2025-07-10 00:11:00 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bdecba34-0b4e-3695-b4af-66abe4caf482 | -17.784901 | -52.426498 | 2025-07-10 00:11:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 28d9a6c2-6e38-366c-b4cc-9ba0ca6ef2b1 | -16.0662 | -51.549702 | 2025-07-10 00:11:00 | METOP-B | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 24e29b08-925c-305a-86b7-ca813523d849 | -6.9851 | -43.491299 | 2025-07-10 00:11:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7761e561-5e09-33c5-87c6-c6c20eeebae5 | -11.8315 | -48.200401 | 2025-07-10 00:11:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7fe77438-7216-3a71-a955-c229168c4654 | -8.5045 | -43.3325 | 2025-07-10 00:11:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ba901798-f414-3fd5-a1ee-63326988c1e1 | -8.8892 | -47.325901 | 2025-07-10 00:11:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ad8c14b6-f0a4-36df-91fe-4cb43d590d4d | -7.2236 | -43.060501 | 2025-07-10 00:11:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a4c2a73a-899c-321b-9726-e3dae0f36ee4 | -8.4904 | -43.272701 | 2025-07-10 00:11:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ca486054-95bf-3091-baf1-13750ca420e1 | -13.355 | -52.911301 | 2025-07-10 00:11:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4858cfb4-31dc-356e-9d01-fe92187f5eca | -4.2267 | -47.214401 | 2025-07-10 00:11:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 62d57986-bfcf-3188-abfc-61653c589b53 | -11.3752 | -48.7006 | 2025-07-10 00:11:00 | METOP-B | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e07283f8-6e33-3d17-b557-58172f85f3b4 | -13.4613 | -43.1194 | 2025-07-10 00:11:00 | METOP-B | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f32ea324-8ec7-35cc-a70b-335765f07853 | -10.6632 | -49.443901 | 2025-07-10 00:11:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1782ced2-46dd-3f74-863d-9d00320c0f79 | -5.623 | -44.010201 | 2025-07-10 00:11:00 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fc09707f-bab6-3a16-922c-8bb6593fe049 | -4.225 | -47.2071 | 2025-07-10 00:11:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d192b09d-6363-3f1e-b569-b0fe8bcde0f2 | -8.9987 | -47.4468 | 2025-07-10 00:11:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cfc83d60-edf2-34a4-afe2-2204afca26f3 | -8.9599 | -47.273499 | 2025-07-10 00:11:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d114268b-ec91-32c2-8e3d-85cc28e743fe | -9.0919 | -47.955299 | 2025-07-10 00:11:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3fb933fc-8a78-3990-b00e-efef12f912ee | -7.007 | -43.496799 | 2025-07-10 00:11:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4844e92b-6fd2-3207-9202-302cb676653b | -6.8476 | -42.777802 | 2025-07-10 00:11:00 | METOP-B | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b110dee9-6bbe-3b3b-a6b1-cba861a90723 | -9.2904 | -44.838001 | 2025-07-10 00:11:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 85f58e4a-e8fa-3d4c-bf59-4b7310e14c1d | -5.8906 | -45.565601 | 2025-07-10 00:11:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f944ec92-9391-37fd-83f8-ee8166ca8ccb | -5.5561 | -43.900002 | 2025-07-10 00:11:00 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6756b4b3-1e5f-3d7d-8403-e96add9e6bff | -12.4724 | -46.905602 | 2025-07-10 00:11:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9e4be79a-d9e5-372a-b543-9764f96cfff8 | -10.6566 | -49.461102 | 2025-07-10 00:11:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 00609033-2112-33a4-bf30-a4e72e536523 | -8.736 | -47.1488 | 2025-07-10 00:11:00 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1ef9e225-8aa4-32a6-bd32-392851661015 | -10.619 | -48.064899 | 2025-07-10 00:11:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 52104d03-1a82-3429-b90f-43be54933ba9 | -7.4803 | -43.932098 | 2025-07-10 00:11:00 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dd3cd70e-09b0-3882-b8c0-b206099ca16f | -16.580999 | -43.6455 | 2025-07-10 00:11:00 | METOP-B | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5526b855-f4af-339a-83ba-22395af82374 | -7.2016 | -45.349201 | 2025-07-10 00:11:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cc82eac1-0879-3ec6-adbb-acb502eca0d2 | -13.3501 | -52.886501 | 2025-07-10 00:11:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 07d03d05-26d7-3a75-9a9f-9c84c3c17b22 | -10.5843 | -49.1273 | 2025-07-10 00:11:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 01ee40e9-6ca6-3adf-a3c7-c490f79209e3 | -12.4316 | -43.703098 | 2025-07-10 00:11:00 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e237573a-3041-3703-8b9d-4fbc66943b8b | -11.3623 | -48.688301 | 2025-07-10 00:11:00 | METOP-B | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 72fe1308-ec88-3a14-b0f0-a0ba83060419 | -13.0012 | -46.274899 | 2025-07-10 00:11:00 | METOP-B | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ac9a18fb-3d7a-3cf7-9cdc-d4d549713e04 | -11.8346 | -48.2146 | 2025-07-10 00:11:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 697937a5-0e1e-3cf2-b898-d0bc22d85a29 | -10.6534 | -49.445999 | 2025-07-10 00:11:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6f502831-53e1-3318-a688-72b0d5fb3c51 | -12.5716 | -52.201302 | 2025-07-10 00:11:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cc142d03-51c1-340a-97bb-df2a405e02bc | -6.1257 | -42.948502 | 2025-07-10 00:11:00 | METOP-B | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d0c4247a-79d8-3173-a8ac-47edcfa57f00 | -3.7523 | -47.122002 | 2025-07-10 00:11:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fce1e1d1-7e42-36a8-84e3-e2a1882600f7 | -9.2109 | -48.584499 | 2025-07-10 00:11:00 | METOP-B | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3643e137-32c3-33ad-9940-8adf21cc0a29 | -12.5735 | -48.874901 | 2025-07-10 00:11:00 | METOP-B | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5972b83b-15a1-35dc-b6c1-935e47ff541f | -11.0626 | -45.861301 | 2025-07-10 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a092ec44-a662-351a-9506-cc638e46845c | -6.6789 | -46.305901 | 2025-07-10 00:11:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d1db4586-85b0-3a5a-ae09-7e7e265f5377 | -5.5762 | -46.532799 | 2025-07-10 00:11:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 24e81750-b049-3306-bf9b-9ba2951f3c90 | -9.2238 | -48.596401 | 2025-07-10 00:11:00 | METOP-B | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 59a4158f-380b-3c32-b81b-ec85a1abaf89 | -7.2286 | -43.081902 | 2025-07-10 00:11:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 874eba6f-9f46-3ecb-87e1-301f84b83e54 | -7.7129 | -43.736698 | 2025-07-10 00:11:00 | METOP-B | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3f66bcf1-0237-3547-9f28-9aef58fc2971 | -9.2983 | -44.827599 | 2025-07-10 00:11:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 986001d5-9fc5-305b-8df5-e0379d3e1ed6 | -19.4576 | -48.535999 | 2025-07-10 00:11:00 | METOP-B | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4e273f39-d8dd-3734-bae8-032e58881742 | -6.8626 | -42.7981 | 2025-07-10 00:11:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7e947dbd-c88e-39aa-855d-37a9d8ae7bdd | -5.544 | -43.8922 | 2025-07-10 00:11:00 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0e83b8a0-59f5-3e67-9341-37b4ddde5c21 | -6.1284 | -42.959702 | 2025-07-10 00:11:00 | METOP-B | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ba24640a-4ec5-3108-8a8e-633d3530ff44 | -11.9573 | -46.3531 | 2025-07-10 00:11:00 | METOP-B | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
