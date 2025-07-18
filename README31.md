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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| feaa3ad7-1910-3d75-8253-1a4bb127c3fd | -12.0076 | -43.3688 | 2025-07-18 13:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 7772dff7-6a3c-32df-bff6-e59314a4cc75 | -6.1444 | -47.7688 | 2025-07-18 13:20:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 1a975b62-5b39-3fba-83e7-371a5f255918 | -14.7011 | -45.0685 | 2025-07-18 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 36f7880b-546a-3080-ae16-460336191b59 | -14.7207 | -45.0649 | 2025-07-18 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 151.5 |
| 3963f615-bc46-399c-a281-107b246f31de | -5.6565 | -43.7393 | 2025-07-18 13:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 94877638-67c5-35a3-a2bf-e87e3fd40507 | -6.9613 | -42.8108 | 2025-07-18 13:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 102.2 |
| 4eea4954-2e59-39ca-8a4f-b648cb92efa5 | -5.6569 | -43.6929 | 2025-07-18 13:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 6ad7a0e4-1313-3003-b08e-13ac815a0470 | -6.9801 | -42.809 | 2025-07-18 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 106.7 |
| 5f8bbf7c-4a3c-35ca-b240-055ed0771027 | -14.7011 | -45.0685 | 2025-07-18 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 141.1 |
| f17fd600-f589-30e7-b64b-4e1d48e07bc3 | -5.6379 | -43.7175 | 2025-07-18 13:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| f08ddf7e-19cf-3bf7-84a6-f755f83e0872 | -5.6565 | -43.7393 | 2025-07-18 13:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| c93cefb7-35f6-350a-980d-6cb088366426 | -5.6567 | -43.7161 | 2025-07-18 13:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 288.9 |
| 3b5d2bdb-89e4-3ccf-9765-8cc650a3e7fe | -14.7207 | -45.0649 | 2025-07-18 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 0772d75f-7928-3a6a-b384-9dc0d10f54c3 | -6.1444 | -47.7688 | 2025-07-18 13:30:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 193.8 |
| d0da2cf7-4270-34c4-aaa4-63784996feb1 | -6.1444 | -47.7688 | 2025-07-18 13:40:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 170.1 |
| 3677689f-cd8b-37ee-ab8b-ea682a82da9e | -6.4873 | -45.0283 | 2025-07-18 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 1b624e24-3997-3b83-bc05-54ebebb9a2e7 | -14.7011 | -45.0685 | 2025-07-18 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 52ae7373-d711-344d-9260-88c456b9ff3e | -5.6565 | -43.7393 | 2025-07-18 13:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| ba995884-8d6f-3353-9ebb-6dc65ae6a3c7 | -5.6567 | -43.7161 | 2025-07-18 13:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 324.7 |
| da235ff3-cf97-3e94-b4d5-d1e566206af4 | -5.6754 | -43.7147 | 2025-07-18 13:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 95dd00e7-5226-3b63-b781-d5cce6ad75e7 | -14.7207 | -45.0649 | 2025-07-18 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 207.1 |
| d23773ed-cbd3-3497-95c9-784507bd5561 | -3.3958 | -47.4785 | 2025-07-18 13:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| f42c810f-1175-3f02-b2bb-b7f8d46c21f6 | -5.6379 | -43.7175 | 2025-07-18 13:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 145.8 |
| bc37e3cb-33b2-3264-93d4-eb528e3d64f8 | -12.0076 | -43.3688 | 2025-07-18 13:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| c8ba14e4-5612-3227-a524-e769a9baf9e5 | -6.9801 | -42.809 | 2025-07-18 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 104.4 |
| 20bccc46-ce18-3e48-9d14-1576b16495d6 | -6.1444 | -47.7688 | 2025-07-18 13:50:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 124.2 |
| c253e836-506f-3e3c-a50d-b05f731e6e26 | -5.6754 | -43.7147 | 2025-07-18 13:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 6319e23c-7dd6-3870-ba22-d5d5b10cc5e5 | -7.1917 | -44.0732 | 2025-07-18 13:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 114.7 |
| ea0cc559-d575-320b-b8e5-9b93b37579b2 | -5.6567 | -43.7161 | 2025-07-18 13:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 421.5 |
| d1b5bce0-4d48-328a-951e-768113563271 | -14.7011 | -45.0685 | 2025-07-18 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 176.7 |
| 5d1eb46f-5a2b-3661-aa2b-80d323b96905 | -5.6379 | -43.7175 | 2025-07-18 13:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 05553d98-a6d7-3292-a4e3-2f3073fb25c7 | -5.6565 | -43.7393 | 2025-07-18 13:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 124.1 |
| c691c28e-5ad4-3ede-90fd-c4c98418d310 | -6.9801 | -42.809 | 2025-07-18 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 106.9 |
| 301256f3-23e0-3349-bb77-3d59be090ed5 | -6.4873 | -45.0283 | 2025-07-18 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 231.4 |
| aa4515df-9f4e-34c4-9565-f1c1492b1b53 | -11.9343 | -46.3472 | 2025-07-18 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 403a73e9-bb3f-3882-9941-86fd396370fd | -14.7207 | -45.0649 | 2025-07-18 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 48f18108-1c29-37c0-b931-5b5340e7a299 | -5.6379 | -43.7175 | 2025-07-18 14:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 145.6 |
| fe026e29-db30-3c4e-921e-bdea7f003cd9 | -14.7207 | -45.0649 | 2025-07-18 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 165.0 |
| 235314e2-4c5f-386f-8e99-01183566e153 | -5.6569 | -43.6929 | 2025-07-18 14:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| d08210c0-031d-3da6-86f8-72011f370497 | -5.6565 | -43.7393 | 2025-07-18 14:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 47adc574-7238-3361-8fa2-0b2ba0002534 | -6.4873 | -45.0283 | 2025-07-18 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 206.3 |
| 386a8582-5072-3bf5-83da-aa6e2e8f03d6 | -11.9343 | -46.3472 | 2025-07-18 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 71af57eb-5cea-38f0-94b0-54ccc36b104c | -6.9801 | -42.809 | 2025-07-18 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 98.9 |
| 2b38dba6-9693-3ed2-ac3e-cef4d3a79076 | -5.6754 | -43.7147 | 2025-07-18 14:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| a4507b2e-540f-310a-a550-d0dbb2123f4e | -14.7011 | -45.0685 | 2025-07-18 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 52ab86f0-739d-3546-822e-87e134795e0d | -6.4685 | -45.0299 | 2025-07-18 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 94977b80-894c-33e0-977b-66b0df767d55 | -5.6567 | -43.7161 | 2025-07-18 14:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 343.7 |
| 7e555708-f0b5-3abe-af46-649aa2904d39 | -5.6565 | -43.7393 | 2025-07-18 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 131.2 |
| a698a7e4-1b37-3001-8033-a0546a83efb6 | -11.9343 | -46.3472 | 2025-07-18 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 16fcb766-cbef-3f4c-9708-2e07c0a1bda7 | -3.9219 | -43.1525 | 2025-07-18 14:10:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| dd1c10a3-abcd-3f43-817b-ddf98d15ede1 | -5.6379 | -43.7175 | 2025-07-18 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 177.0 |
| d9af91b7-cb8c-37dd-8850-dd201d6acd0d | -7.1917 | -44.0732 | 2025-07-18 14:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| acb5c0d6-f076-36f1-bfea-b2e6a06d6202 | -14.7011 | -45.0685 | 2025-07-18 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| ca2f65d0-8ace-379e-9ce0-3c279423428d | -6.4685 | -45.0299 | 2025-07-18 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| dfe944b8-bba2-363c-8eae-132c727782b0 | -14.7207 | -45.0649 | 2025-07-18 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 270d8647-57a4-3a1f-b65d-374d5058e187 | -5.6754 | -43.7147 | 2025-07-18 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 135.9 |
| a9a9c587-4c0a-37f1-a8d6-95b97db32a71 | -6.4873 | -45.0283 | 2025-07-18 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 223.7 |
| 027e3b8a-29c5-368a-9a1e-69e370edd762 | -3.2906 | -42.5271 | 2025-07-18 14:20:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 9848396a-8dac-39aa-b36b-72c5f8ff63ac | -14.7207 | -45.0649 | 2025-07-18 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 331ba5be-ffb7-3bbe-b7a9-f7b297a03548 | -5.6379 | -43.7175 | 2025-07-18 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 15fba681-e037-3e0f-9798-ad54e3a0df61 | -2.9109 | -48.2325 | 2025-07-18 14:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 39f5cbe3-89a5-3619-94a4-350d67cb9ed4 | -6.4873 | -45.0283 | 2025-07-18 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 8a6855f2-2024-3514-902f-ffbfbb9e09b9 | -5.6565 | -43.7393 | 2025-07-18 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| d10e96bf-da1e-39e0-b85f-d1191bf3acad | -14.7011 | -45.0685 | 2025-07-18 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 161.6 |
| 55244923-7f74-3fe7-86fb-3d3ea378f4c7 | -3.9219 | -43.1525 | 2025-07-18 14:20:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 40143bcd-8e7f-37bd-9a06-69cc859f12f6 | -5.6569 | -43.6929 | 2025-07-18 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 3cb1854c-1831-39bf-a4e6-9fb867a08bf5 | -7.1917 | -44.0732 | 2025-07-18 14:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |
| c2242ae5-c07b-3587-976a-5219fc69882b | -14.7011 | -45.0685 | 2025-07-18 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 118.9 |
| b8802745-9d7c-3733-a90f-f51e32e97be9 | -3.2906 | -42.5271 | 2025-07-18 14:30:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| fe244955-7e63-3462-bcd2-de74a91a756b | -5.6754 | -43.7147 | 2025-07-18 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| aba0c29e-248b-3af7-bc79-f5450e1315a0 | -5.6565 | -43.7393 | 2025-07-18 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 3cc66d5c-76c9-386d-ae40-85905588b6e2 | -11.9343 | -46.3472 | 2025-07-18 14:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 68977210-12b5-3e2a-83c0-965b2a9a4aa7 | -3.3958 | -47.4785 | 2025-07-18 14:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| df7f77c0-6961-321a-8d49-ed846e138a51 | -5.6569 | -43.6929 | 2025-07-18 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| b6fde5d9-727f-385b-80e9-88cc5f43637c | -3.9219 | -43.1525 | 2025-07-18 14:30:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 05c1a0cc-ea70-3743-a99f-9fab5d5fd7c4 | -5.6379 | -43.7175 | 2025-07-18 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 157.4 |
| f9006a3d-9380-3f65-8666-e4dd98f1f2f9 | -14.7207 | -45.0649 | 2025-07-18 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 137.3 |
| b25398ef-6bda-345e-acf3-cbee1f609ded | -2.9109 | -48.2325 | 2025-07-18 14:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| a570f10b-bb34-343e-84f8-451bb778b531 | -7.1917 | -44.0732 | 2025-07-18 14:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 544d9020-8c5f-30dc-8b5b-43d162d6bb8f | -5.6565 | -43.7393 | 2025-07-18 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 5b66d328-fa29-30c6-90ce-714ddf18e00f | -5.6569 | -43.6929 | 2025-07-18 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 0077a699-459e-391f-849b-71ef036746f0 | -14.7207 | -45.0649 | 2025-07-18 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 57de32ce-b16c-3965-9d3a-bf78b0c95991 | -3.3958 | -47.4785 | 2025-07-18 14:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 877ef76c-2233-36f9-8fe0-97354543c34d | -6.1444 | -47.7688 | 2025-07-18 14:40:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| c25d1053-789d-3935-bf4a-7313abd67e0e | -3.9219 | -43.1525 | 2025-07-18 14:40:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| f9735bc6-4d02-3116-b4cd-03b31d1872e5 | -2.9109 | -48.2325 | 2025-07-18 14:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| cdf792f9-9d26-3387-89f6-d49d68e623eb | -6.4888 | -44.8689 | 2025-07-18 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| ab1339e8-3c74-3566-97e7-ace402d14f9b | -14.7011 | -45.0685 | 2025-07-18 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 176.4 |
| 44f37696-0fd7-3c41-a5f9-501beb4558c4 | -3.2906 | -42.5271 | 2025-07-18 14:40:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |


