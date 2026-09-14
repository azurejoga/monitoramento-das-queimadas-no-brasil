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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c54cb7c-cffe-3bc1-a3ec-47aba8218a42 | -10.5788 | -51.33997 | 2026-09-14 11:30:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 6d24ba60-4179-303a-bc3d-d3ffa54af2f1 | -17.60154 | -44.60778 | 2026-09-14 11:30:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4bac16b3-079c-325b-acf5-4f3edeed07d2 | -13.62668 | -47.91499 | 2026-09-14 11:30:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3c26a3c6-e639-3241-882e-27d31441191b | -13.80785 | -44.96926 | 2026-09-14 11:30:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d7f7ac8d-4bed-3bce-9530-c9cb0621cf24 | -14.1023 | -46.34817 | 2026-09-14 11:30:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 84dfc46d-23d8-3c5e-bcc2-43d203ed9758 | -14.28264 | -43.77076 | 2026-09-14 11:30:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b9640365-9645-3d17-8da1-22699bd7ce2a | -13.62864 | -47.90269 | 2026-09-14 11:30:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 6cb62227-d008-3a7c-8b0b-9ff8e7712aee | -14.82092 | -48.15221 | 2026-09-14 11:30:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 5ee3099e-1eb8-3937-9c81-f173e00eeeca | -11.78624 | -46.40748 | 2026-09-14 11:30:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 674338cf-7300-3cd2-967d-5d3bc9e460b9 | -10.43966 | -48.65179 | 2026-09-14 11:30:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| a1a8b575-385f-3b4d-9756-c682589d69ff | -18.38696 | -43.92216 | 2026-09-14 11:30:00 | TERRA_M-M | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7797070b-c2c9-32dc-b4cd-ea98e8315386 | -12.77699 | -43.92648 | 2026-09-14 11:30:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 29a74235-4881-39e1-a8a3-48942eb05186 | -10.80264 | -46.26316 | 2026-09-14 11:30:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| a1144ace-9710-3b12-a6d0-0b0d2e016ede | -13.58011 | -47.88818 | 2026-09-14 11:30:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 34cf10ca-c4e4-3a72-8997-d3934203a1da | -13.27686 | -43.45599 | 2026-09-14 11:30:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e46da2b5-a23b-32e0-be32-4f6172ad10d3 | -12.4036 | -44.41307 | 2026-09-14 11:30:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b9c1319c-4e72-3305-a17a-8d7ec92658ef | -13.59213 | -47.87777 | 2026-09-14 11:30:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9ea93380-3ea1-3929-9d94-3a98b922c1b9 | -8.7405 | -46.41694 | 2026-09-14 11:30:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 208.1 |
| ae23a6dd-d779-3f8e-924c-c8f572895a54 | -11.83307 | -46.38789 | 2026-09-14 11:30:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 82ff0d6e-d221-3e9f-9933-6ea10295d8bc | -9.09415 | -45.89935 | 2026-09-14 11:30:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 21025b4d-11d0-3c05-8f3d-d577a41369f3 | -11.77832 | -46.39557 | 2026-09-14 11:30:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| fa6b82cb-812e-3e12-87c1-c4a685359e66 | -13.6306 | -47.89038 | 2026-09-14 11:30:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 2d58a1d7-ce1c-3fcb-83e5-dbdcfaf62171 | -10.80576 | -46.33529 | 2026-09-14 11:30:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| bebd4004-52b2-3bdc-bf90-9eb80e55b73b | -11.18336 | -42.80658 | 2026-09-14 11:30:00 | TERRA_M-M | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 38f2d262-a478-3c1e-b09a-959ef6b0772e | -17.59267 | -44.6065 | 2026-09-14 11:30:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e01d08f1-3a01-30ec-9f42-6ebb1b1d71d5 | -11.22208 | -46.41208 | 2026-09-14 11:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 59b907d9-b3d0-3b40-8227-ca856f5dd2fb | -14.10379 | -46.33818 | 2026-09-14 11:30:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| fd845f0c-44c4-3f6d-a46d-58fe962805aa | -11.78467 | -46.41793 | 2026-09-14 11:30:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 32f9030b-1036-32f7-8873-5cc0e184c053 | -10.42827 | -48.65023 | 2026-09-14 11:30:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 5ddae5b4-e5e5-3360-bc57-6fc903532fec | -8.60502 | -44.45761 | 2026-09-14 11:30:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 26.6 |
| b97d3c19-02d2-3e46-a886-241d39bc9ef3 | -11.84131 | -39.24069 | 2026-09-14 11:30:00 | TERRA_M-M | CANDEAL | BAHIA | Brasil | 2906402 | 29 | 33 | nan | nan | nan | Caatinga | 13.4 |
| cdfd9f63-33b9-34b1-8cab-51da6260883f | -10.80741 | -46.32461 | 2026-09-14 11:30:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 156.8 |
| 3b2096c0-b1ec-396a-9214-817bfa77c348 | -13.43775 | -43.8167 | 2026-09-14 11:30:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 3e810c06-5026-30e2-90db-2b2ec717ac6e | -14.17473 | -47.43219 | 2026-09-14 11:30:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| d11c1783-898b-37fa-80e3-5ebfcf66e16d | -10.75177 | -46.27718 | 2026-09-14 11:30:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 9afc3aa2-4296-3835-9fa7-efd80f11af8d | -13.59404 | -47.86542 | 2026-09-14 11:30:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 364dcafd-2877-3deb-8caa-d6fd72c93236 | -10.76927 | -46.29061 | 2026-09-14 11:30:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 40.0 |
| c104d266-88ed-3375-a5e8-06b4831c20a3 | -14.61987 | -46.94417 | 2026-09-14 11:30:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7a371935-0cb7-3a99-9428-96393a915610 | -8.7504 | -46.41837 | 2026-09-14 11:30:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| bacd91fd-0eec-3706-b383-4adc5b965ce6 | -11.22846 | -46.4347 | 2026-09-14 11:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 345a712b-f089-382a-aadb-f135423f4a09 | -15.57017 | -48.80119 | 2026-09-14 11:30:00 | TERRA_M-M | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 0fd43ec3-17b5-35f1-93c6-4ff0b4de8ac0 | -14.16588 | -42.33266 | 2026-09-14 11:30:00 | TERRA_M-M | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| e7ea7f45-3d7e-3fba-966c-28a2f38106d1 | -14.16724 | -42.32238 | 2026-09-14 11:30:00 | TERRA_M-M | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 7cc91c9c-4b9b-35d0-8492-86e2b0e64677 | -10.8059 | -46.30685 | 2026-09-14 11:30:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 80fd214c-ac06-3dfa-83dc-904122681153 | -8.7388 | -46.42831 | 2026-09-14 11:30:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 27ca1f00-3078-3991-81fb-692a5a0dd367 | -18.30999 | -44.14974 | 2026-09-14 11:30:00 | TERRA_M-M | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 95207422-2544-3ec4-80db-c8e3602152d9 | -18.47627 | -51.72033 | 2026-09-14 11:32:00 | TERRA_M-M | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 45c4f645-1666-34ac-a0c2-e1a35a5f4f3b | -13.5769 | -47.9056 | 2026-09-14 11:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 84.1 |
| f326ac02-d5c3-34c5-bb61-1c6c09c13e69 | -10.6641 | -54.1491 | 2026-09-14 11:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 9f03534f-3145-3f64-a5fd-8cf26ed467fc | -10.6829 | -54.1475 | 2026-09-14 11:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 138.1 |
| dbe80487-b543-331f-9f95-9b7f1ad87f4c | -10.6827 | -54.1679 | 2026-09-14 11:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 140.6 |
| a57e6543-22e5-3874-8803-ee594b3f4634 | -13.2867 | -51.3046 | 2026-09-14 11:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 98acca0e-4560-3038-a73e-dc0e9b241672 | -13.6349 | -47.8969 | 2026-09-14 11:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 4d94ea26-610d-3942-940d-3d2bf26c9697 | -13.3059 | -51.3022 | 2026-09-14 11:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 0e5e50f0-b7c2-3842-b010-54089a16dccb | -10.6829 | -54.1475 | 2026-09-14 11:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 137.9 |
| 4f17d152-926b-3985-9ab7-12e4de160c61 | -10.6827 | -54.1679 | 2026-09-14 11:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 134.2 |
| 0bcb5eb8-b431-3603-b95b-499155915fe7 | -8.7445 | -46.4213 | 2026-09-14 11:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| d1660f13-f453-3b6a-88fc-ddf497884aeb | -13.2867 | -51.3046 | 2026-09-14 11:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| dd8efbe7-8ce3-3dc9-9751-31ef689f3643 | -13.5769 | -47.9056 | 2026-09-14 11:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 113.2 |
| b2765cb7-b40b-32e6-8910-f4528dba345e | -5.1255 | -55.955 | 2026-09-14 11:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| d6bc0399-bcc7-3fb8-b13f-26557e30c9c8 | -10.6638 | -54.1696 | 2026-09-14 11:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| f15072d8-bc23-3407-9ee3-b339c066cc88 | -8.8081 | -45.8753 | 2026-09-14 11:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| f3211a24-e35e-3c09-9433-f7433fbd2e2b | -10.6641 | -54.1491 | 2026-09-14 11:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 76b95691-5013-3a40-b4fb-e2f101f7c931 | -13.5963 | -47.9027 | 2026-09-14 11:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 98.7 |
| cf10f235-d3d7-31d3-aab6-fd03587512c4 | -14.205 | -47.4039 | 2026-09-14 12:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 0b67b021-385f-3269-938c-6858f72162fb | -8.7445 | -46.4213 | 2026-09-14 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| d4e226a3-7253-3e9b-96ca-c9e7b609e79d | -10.6829 | -54.1475 | 2026-09-14 12:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 109.6 |
| ccd526c8-b284-3fe7-9898-1e6ce69d0ca9 | -13.6349 | -47.8969 | 2026-09-14 12:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 72.7 |
| a7c76273-e9c2-3322-9f64-913122b9e49b | -5.1255 | -55.955 | 2026-09-14 12:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 9c9106ae-02b5-3c31-a61b-67d46f9e0620 | -10.6638 | -54.1696 | 2026-09-14 12:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 070174b1-4580-3ef2-b043-5595319efafc | -8.6194 | -44.4357 | 2026-09-14 12:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 6796ec30-7353-3594-b2c1-4317125435f4 | -10.6827 | -54.1679 | 2026-09-14 12:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 428bad5f-5c96-3046-8299-16e14be61a2d | -13.5963 | -47.9027 | 2026-09-14 12:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 6078ff5c-12af-36cb-9b56-1551e3aecd1e | -10.6641 | -54.1491 | 2026-09-14 12:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 119.7 |
| c31d59fe-4e14-34d9-b8db-b5a9eee4e0b8 | -6.6767 | -58.7105 | 2026-09-14 12:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 6451416c-35b1-3d2a-8ae1-59126c3a6fbd | -8.8081 | -45.8753 | 2026-09-14 12:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 7403cc50-e85b-3166-9fd9-5b6bf8a4df8a | -10.81 | -46.2726 | 2026-09-14 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| b84c79a2-8d76-3301-8db3-e041039343ba | -13.2867 | -51.3046 | 2026-09-14 12:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| c1a254e0-ff3c-37b9-b0c9-b9181f44c9bc | -15.5572 | -48.7953 | 2026-09-14 12:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 01d41aaf-d94e-3857-b3cb-b7cd3edaac9c | -8.7445 | -46.4213 | 2026-09-14 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 198.5 |
| 0f2dadd3-c9b2-39e6-9dbd-b83b1386efe9 | -14.1861 | -47.3844 | 2026-09-14 12:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 8e83ef94-2c80-3be8-bc32-e343afbfe540 | -10.6827 | -54.1679 | 2026-09-14 12:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 116.6 |
| eb68c307-ce53-326e-a731-c972ce2d5158 | -5.1255 | -55.955 | 2026-09-14 12:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| df7ee99a-3574-3911-b0ab-34593a544d7c | -8.7634 | -46.4194 | 2026-09-14 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 149.0 |
| 3a747a1b-cd34-3a0f-a7c3-09e9c2f34194 | -8.6194 | -44.4357 | 2026-09-14 12:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 3fa64416-b3f1-35d2-b2e7-e56f613e638e | -6.6767 | -58.7105 | 2026-09-14 12:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 59e66a9b-9ab5-336f-be41-cbcf98272cb5 | -13.3059 | -51.3022 | 2026-09-14 12:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| cfabe06c-f512-3304-9c79-d5fbd5af35bb | -10.6641 | -54.1491 | 2026-09-14 12:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.2 |
| a9c4df6b-79d6-3e21-9024-1a6743fde08a | -13.6349 | -47.8969 | 2026-09-14 12:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 7d839cac-5208-3eec-8777-fdb541fdbfbe | -9.442 | -47.8788 | 2026-09-14 12:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 628e4a6e-58d1-3f28-b4dc-18c08d799782 | -9.4325 | -50.1299 | 2026-09-14 12:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 06dccb8b-7d65-31da-ba0c-9587364a5c7f | -8.8081 | -45.8753 | 2026-09-14 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 256.2 |
| 74bbe857-badf-3c51-9c63-7105b1016d67 | -9.4328 | -50.1086 | 2026-09-14 12:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 1adf59c0-832d-3340-854a-cea05da8d7b3 | -14.205 | -47.4039 | 2026-09-14 12:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 270.8 |
| 6a42852d-24ad-3dc0-8ce6-47485a2671b6 | -13.2867 | -51.3046 | 2026-09-14 12:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 81269fe8-236a-3664-9602-cae12784edf5 | -10.6829 | -54.1475 | 2026-09-14 12:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 134.3 |
| faf392a0-f8e8-3a56-9b68-a02553f37323 | -14.1856 | -47.407 | 2026-09-14 12:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 59c9d775-8d49-3bdd-9273-324001d8bc79 | -15.5572 | -48.7953 | 2026-09-14 12:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 100.8 |
| dee91646-f547-3a04-93e7-9068ce18e657 | -10.81 | -46.33 | 2026-09-14 12:15:00 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 96061eee-b53c-37d4-95ce-222d697b7385 | -9.4328 | -50.1086 | 2026-09-14 12:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |


[Clique aqui para ver as próximas entradas](README67.md)
