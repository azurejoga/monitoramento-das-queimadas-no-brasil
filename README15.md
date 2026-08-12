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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84092935-c5b6-3d52-bb71-64ad3fedf1f6 | -11.82041 | -51.83312 | 2026-08-12 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 121ff567-4a53-355b-982f-a93e4110ae0a | -12.03656 | -47.80012 | 2026-08-12 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60d91b93-6800-3494-8df2-9e6791e9030d | -11.98743 | -46.36337 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a9cdeb58-1f5d-301d-b64d-4f33b84dcfb4 | -16.10135 | -49.89036 | 2026-08-12 04:17:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 99cf9c85-ea45-3abc-b9ef-5058491dc392 | -14.29224 | -51.98707 | 2026-08-12 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a909317d-f22c-3a9e-8d36-178910ff232f | -9.34288 | -47.51253 | 2026-08-12 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 50c350e8-6d5e-37b2-a528-910ab6d96b0f | -10.70775 | -47.90485 | 2026-08-12 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a29c0b33-5a73-3ef3-b0c6-70edb313c44b | -12.1404 | -48.26831 | 2026-08-12 04:17:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ec4b99ed-3d69-31d9-aa7e-f1b2e9f4cf4a | -11.97836 | -46.39757 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 91284423-6ecb-366b-8a69-a08f13d8afec | -14.5069 | -49.2756 | 2026-08-12 04:17:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb04354f-0d7a-3031-82e2-9e0f7bc16ba2 | -12.10794 | -47.18158 | 2026-08-12 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 577a1d28-e641-3ccc-93be-07d054a583d1 | -11.78776 | -51.85303 | 2026-08-12 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4218a0a1-ad87-304a-88e3-445f5ebef670 | -13.56752 | -47.63958 | 2026-08-12 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac8a7ba4-2a8d-32f3-9751-e4e595ca9872 | -10.82102 | -45.53638 | 2026-08-12 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c96f0500-72bd-345b-bdc5-cea3d4d15d43 | -14.29677 | -51.98793 | 2026-08-12 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f0fc3a7-eaae-3224-9631-688b876fa478 | -14.3602 | -53.23427 | 2026-08-12 04:17:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 86fbd322-bddb-3195-9354-83c489e4cf90 | -14.98392 | -46.60408 | 2026-08-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb8c6e56-ae18-3ef6-a464-caa11793f260 | -11.46836 | -46.67918 | 2026-08-12 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec135f2e-ec14-3375-9321-5338fd7dba6d | -18.22924 | -46.11757 | 2026-08-12 04:19:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b2b0fbb-ff90-314e-8ce1-4202ce6713cf | -17.50785 | -42.36997 | 2026-08-12 04:19:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa561cc9-92a7-3fcc-b9a5-882e6ddfee64 | -23.06087 | -51.07668 | 2026-08-12 04:19:00 | NOAA-21 | SERTANÓPOLIS | PARANÁ | Brasil | 4126504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f4a1adb6-2577-315f-9787-dd8555a1c84e | -17.14431 | -44.80394 | 2026-08-12 04:19:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 62e726da-4f7c-3da5-8175-ba7ccb30f113 | -18.90375 | -48.3432 | 2026-08-12 04:19:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ab1bc6b-9c37-378b-a3b0-167d2c5d2873 | -19.00033 | -45.72657 | 2026-08-12 04:19:00 | NOAA-21 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc84c69e-8446-3b9e-bb84-7954fc3338d0 | -18.91973 | -47.03611 | 2026-08-12 04:19:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b4f5cd1-dda5-3812-87d8-54fb57b0f758 | -17.44521 | -48.85651 | 2026-08-12 04:19:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7dd976e1-83d1-3f76-8075-00024ca7d352 | -17.81478 | -44.38247 | 2026-08-12 04:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02a00cf5-5344-3744-9a82-6040f4e512d8 | -18.87146 | -48.33014 | 2026-08-12 04:19:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 48318c82-36fd-31ab-90d6-55c3dde7e8f3 | -18.99218 | -46.90489 | 2026-08-12 04:19:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee87ef68-b700-3410-9b8f-22820151e5b6 | -18.91913 | -47.0398 | 2026-08-12 04:19:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40433b3d-f937-331b-b7cf-55bc296b58ba | -18.7689 | -46.5761 | 2026-08-12 04:19:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| bde34d7c-83b6-3419-b50d-25713d2fd71c | -16.70914 | -49.15558 | 2026-08-12 04:19:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6e44f34-1c20-36a1-98ac-bcce20ad3b7c | -18.70004 | -44.54874 | 2026-08-12 04:19:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7e3999a-cccb-3ac2-a6de-106261dc7879 | -16.8127 | -49.33962 | 2026-08-12 04:19:00 | NOAA-21 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 474734ed-6014-393b-942e-8939a6a4cb33 | -16.73803 | -49.36091 | 2026-08-12 04:19:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b8eb280-1642-3c7a-9d2a-c97498039136 | -17.46296 | -48.90379 | 2026-08-12 04:19:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b694d344-343a-351e-b240-ffa115f09d5b | -16.54722 | -49.41298 | 2026-08-12 04:19:00 | NOAA-21 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e630a37d-ac5d-3549-bb17-3a3e4033421e | -18.93244 | -46.8299 | 2026-08-12 04:19:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8cfa9efb-fa95-32d5-8028-58a258841c71 | -17.98655 | -44.37486 | 2026-08-12 04:19:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23dc90e7-6662-3225-a32b-cd4ee6171313 | -17.81141 | -44.38194 | 2026-08-12 04:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ece12dd4-0876-320a-8b2c-8393af0e064e | -15.58084 | -53.93469 | 2026-08-12 04:19:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0107270d-5743-3d86-bd4b-4780be8a5091 | -18.67152 | -47.202 | 2026-08-12 04:19:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d1589ef-d114-31e7-8742-ee93d7634943 | -17.10855 | -47.19042 | 2026-08-12 04:19:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 734164a3-797b-3a15-af8c-4ff4dcae56a3 | -18.72172 | -47.06205 | 2026-08-12 04:19:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c92a1c0-2021-345d-b306-9873833d783f | -11.9719 | -46.3871 | 2026-08-12 04:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 2d8b3111-5852-39c6-ac13-7f72e9b25cbe | -11.4869 | -44.5763 | 2026-08-12 04:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 04cf8d45-cadd-3bcd-ad26-d9ba253dcf54 | -11.9911 | -46.3844 | 2026-08-12 04:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 2cd5dac7-9b48-3a59-a50e-b10f0dbfa6cb | -6.6013 | -59.0037 | 2026-08-12 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 61dd9b93-cae7-3baf-bf2b-af775e2e63d5 | -11.9911 | -46.3844 | 2026-08-12 04:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 28f3afc5-f46f-3540-b97e-45c69fa9691c | -8.96 | -60.5358 | 2026-08-12 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 4367f4de-a6c6-3da0-957e-b358908c9cfe | -11.9719 | -46.3871 | 2026-08-12 04:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 264ed1cc-ee65-3939-940a-5849762c89d9 | -11.9539 | -46.3217 | 2026-08-12 04:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 75231242-cd5f-3549-a88c-f0169158d118 | -15.3023 | -48.8595 | 2026-08-12 04:40:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 66.7 |
| b3a0edc5-3d09-3dee-9c91-bc04ef5d5ee0 | -11.9719 | -46.3871 | 2026-08-12 04:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 52483fd4-25eb-3918-b54d-ab067fe6e409 | -15.3019 | -48.8818 | 2026-08-12 04:40:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 3db70a93-9dd2-3d59-aeba-f657065e7b10 | -8.96 | -60.5358 | 2026-08-12 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 5cb81f7b-0af5-3382-bcc8-306f27eddaf2 | -11.9535 | -46.3444 | 2026-08-12 04:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 94214c23-579d-3073-b2e1-f99ae660b91c | 0.01202 | -51.07538 | 2026-08-12 04:46:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8ef09fea-9407-38b1-b1c8-6060a01bbc11 | -2.84772 | -49.54006 | 2026-08-12 04:49:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da894564-d7b5-3f10-b791-ad32a4c13424 | -3.43518 | -49.48295 | 2026-08-12 04:49:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ddef6bc9-8dce-3d6f-ba3e-ee94b8faee7d | -8.42047 | -49.48701 | 2026-08-12 04:49:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 889bc7bf-7ca8-33b9-9154-cd3269d2381a | -3.23598 | -49.45893 | 2026-08-12 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c4ce4e9-2085-38f3-8915-fb4657b18748 | -6.88775 | -41.9445 | 2026-08-12 04:49:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8801bdfb-69fc-3605-b984-c37a9237ce5d | -7.72088 | -46.22215 | 2026-08-12 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa5e71d3-d5f8-3e80-a350-aef89c0d041b | -6.55216 | -43.10951 | 2026-08-12 04:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf595c70-c438-3e80-8eeb-c47e9a71ea60 | -6.89344 | -41.93942 | 2026-08-12 04:49:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a733b72a-2d97-3e5a-8d97-f02e8c9cbcf0 | -6.34103 | -44.06734 | 2026-08-12 04:49:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b52b09d8-585e-3ec4-bdde-a6337f2bdc6d | -8.76432 | -47.35308 | 2026-08-12 04:49:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d2eea35-aa8b-3574-9408-53947d592852 | -8.36635 | -47.74687 | 2026-08-12 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21e66c16-1e77-383d-9d4b-96dd602eb97b | -8.60022 | -45.39107 | 2026-08-12 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83587504-22d8-3169-86c3-dcac2a1e363e | -6.60137 | -59.00626 | 2026-08-12 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d53908a8-643e-331a-8914-3b888d48120b | -2.80535 | -48.59122 | 2026-08-12 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a8e2165-f299-3794-a782-a9a5186d1093 | -7.19163 | -44.36854 | 2026-08-12 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d56a9c4-2285-3a1f-ab84-bd0508642e90 | -5.73573 | -44.5006 | 2026-08-12 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 253b8694-861f-322c-a73d-e1f9d595c2b8 | -7.91475 | -45.11488 | 2026-08-12 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26392769-e573-3aa3-b05a-ff0c0615f71c | -9.03148 | -47.49455 | 2026-08-12 04:49:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e88dfcfc-120e-31cc-9ee5-f64261f27b87 | -8.11351 | -47.18359 | 2026-08-12 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64d52d2f-e767-3614-8584-7d34326edb83 | -6.58772 | -59.01126 | 2026-08-12 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6d16e791-e840-3c64-9ad9-adcf564e261c | -6.54191 | -43.11708 | 2026-08-12 04:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26fa07fa-79de-327a-bbcd-9281aca3b51f | -8.35898 | -45.97789 | 2026-08-12 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 3a46dde9-e6a4-374c-9887-24e0f8689b3a | -3.11605 | -47.9115 | 2026-08-12 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7237ac5-d6b3-3437-b973-c54c379c9573 | -6.61345 | -59.00119 | 2026-08-12 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fdf421e6-07a8-33ca-b3bf-2401e1729d83 | -6.04752 | -43.86891 | 2026-08-12 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1407156f-bdab-33e0-8dc0-84a644aeffac | -8.6013 | -45.41179 | 2026-08-12 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1ec3e415-86ce-38c1-8eac-760a1c43bd9f | -6.88705 | -41.94942 | 2026-08-12 04:49:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7dca19ae-04bc-376d-9f1c-4f15576b867b | -2.77129 | -49.46681 | 2026-08-12 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 375983a6-c45a-3d11-b8ea-0d85056f8a08 | -3.96588 | -43.11398 | 2026-08-12 04:49:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fa24552-26e1-3602-b14f-27d991712000 | -6.85211 | -46.00601 | 2026-08-12 04:49:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5dbafe6a-147f-315f-a825-7e9655ae4267 | -8.64188 | -45.87754 | 2026-08-12 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 782a9cc2-a1ae-30cd-98dc-66e03a5c017d | -6.60518 | -59.00713 | 2026-08-12 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0015bf4d-c1e4-39e8-a0a7-c1fcc6f8c083 | -3.42909 | -49.48195 | 2026-08-12 04:49:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5a3c1965-8801-3d5a-a2bf-e0345ca121e8 | 0.18652 | -60.49093 | 2026-08-12 04:49:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 57bc9867-bebd-3691-8523-755b9227685d | -6.99986 | -44.83036 | 2026-08-12 04:49:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9bf5e08a-d657-37ca-88a2-8bf5e5cd4e7d | -8.78258 | -45.78725 | 2026-08-12 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d6a8ef8-5eec-3628-ba79-801c64e6bc88 | -8.6377 | -45.85197 | 2026-08-12 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 096e2e00-2f61-3247-9b01-dae7f7f928ec | -4.4553 | -55.66552 | 2026-08-12 04:49:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1cee229b-14f3-353d-95ec-833439f1fe9b | -6.60579 | -59.00363 | 2026-08-12 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5ac3f68-6b78-3db2-8830-365bf5dd665f | -3.23931 | -49.45945 | 2026-08-12 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42ba0625-630e-3d18-b0db-68ec4d350ba7 | -2.11409 | -48.99768 | 2026-08-12 04:49:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e39968c7-3731-3f50-ab17-929fbe5698ea | -2.68985 | -48.20518 | 2026-08-12 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README16.md)
