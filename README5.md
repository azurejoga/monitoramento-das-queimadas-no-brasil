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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d0f93bc-a4f4-3c54-b843-0d79f7a8fab2 | -17.5826 | -47.51499 | 2026-07-21 03:45:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d6875af6-0a20-3f98-83b0-f519d5064783 | -17.58637 | -47.50402 | 2026-07-21 03:45:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a6b551a0-0436-385e-80fd-38e64f0df215 | -17.45749 | -47.15114 | 2026-07-21 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4a204a9-4ef6-36a1-af34-63daba3ebd58 | -17.58555 | -47.50169 | 2026-07-21 03:45:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ceb1dc1d-5b75-3da9-a31f-6aca0e047c0d | -17.86569 | -50.51131 | 2026-07-21 03:45:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 29.1 |
| f671dd0d-1302-3e93-95ae-d0ea93b7e673 | -17.58542 | -47.5084 | 2026-07-21 03:45:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f10cf952-abc2-343e-a0c1-ef65e525a31b | -20.35273 | -46.67554 | 2026-07-21 03:45:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9174034-5e67-341a-9e28-83ac92a65c02 | -17.86403 | -50.51819 | 2026-07-21 03:45:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 201ca14d-c461-3f42-9285-b7842646d25c | -20.35639 | -46.60746 | 2026-07-21 03:45:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f3c44fd-9e4d-3223-9e4d-0c1a8369627b | -20.43425 | -46.47466 | 2026-07-21 03:45:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7ada204-180c-3d94-a048-f1bed65a2cbb | -19.6082 | -47.64766 | 2026-07-21 03:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 35f60e01-1aed-3421-bc36-5804d55439ec | -20.3813 | -46.59341 | 2026-07-21 03:45:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7405a6da-94bb-3abd-89ac-a74cef1ba773 | -20.43376 | -46.47451 | 2026-07-21 03:45:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37b670ed-c9dd-315b-a022-2455b0d95ba2 | -16.02031 | -43.04013 | 2026-07-21 03:45:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a99cf475-bb6e-3f99-9590-9548f3c7c268 | -17.58446 | -47.51289 | 2026-07-21 03:45:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9083d091-a141-3a13-9024-c2a3cec66da5 | -17.46288 | -47.1501 | 2026-07-21 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9daff768-7b36-3b74-98c0-a2ac2e63960a | -17.45725 | -47.14844 | 2026-07-21 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 426d3438-ebbe-36c6-85e2-26090f9c55bb | -20.38041 | -46.59757 | 2026-07-21 03:45:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca24175b-7036-320b-a6fe-ab45b710e76a | -19.1817 | -47.36506 | 2026-07-21 03:45:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 8ec40cbd-4cc2-386d-be77-2404e66193c3 | -20.05418 | -43.24065 | 2026-07-21 03:45:00 | NOAA-20 | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7928e2f0-8078-342d-a225-c71e14f3ed74 | -17.57968 | -47.50677 | 2026-07-21 03:45:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5765e2ba-5aad-39fe-b6c5-c00f56993a44 | -17.86322 | -50.52312 | 2026-07-21 03:45:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 7f158545-08d0-3374-899d-809fe754fbd5 | -20.42986 | -46.46989 | 2026-07-21 03:45:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 26d3b643-adab-3695-b2bf-382d8124aa38 | -19.60909 | -47.64359 | 2026-07-21 03:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 133d8a09-b9c7-3552-a44c-653de3adebf5 | -19.18726 | -47.36648 | 2026-07-21 03:45:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65c8f82c-d40c-3e44-8d92-c47ae92814d4 | -19.60998 | -47.63954 | 2026-07-21 03:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5a71841a-224e-37b1-8c6a-50ce064ed2f5 | -17.45656 | -47.15537 | 2026-07-21 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60a6674a-02b5-3085-8402-8df56918213b | -20.42866 | -46.47297 | 2026-07-21 03:45:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7779f9e9-4eb2-3ec9-b6d4-335f71b92efe | -20.42799 | -46.47617 | 2026-07-21 03:45:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf11302e-a7fb-343a-bca3-99ad01a0f641 | -20.42916 | -46.47308 | 2026-07-21 03:45:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7f998da-48c0-3449-a50b-f6ec827d7a47 | -19.18255 | -47.36118 | 2026-07-21 03:45:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 119d194a-306d-3f1e-935b-8d5b43c29438 | -20.3623 | -46.60542 | 2026-07-21 03:45:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8de9216-1737-33c0-b789-84323bdd77f3 | -21.67952 | -41.1517 | 2026-07-21 03:45:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4113d445-cbea-37a7-9861-1febe8aa6531 | -17.45635 | -47.15268 | 2026-07-21 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 976bc4b1-5fb4-3abc-be61-8b15add2b5e5 | -20.42731 | -46.47939 | 2026-07-21 03:45:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a420fb4e-897b-3c25-b271-eb0c0c63d6c2 | -17.85809 | -50.5141 | 2026-07-21 03:45:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 5e7c16d9-da44-3e39-8855-8dd4b01f2ad3 | -20.42776 | -46.47948 | 2026-07-21 03:45:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16fd1ae9-897e-3c78-ad18-5b246986c6c9 | -22.73501 | -46.81737 | 2026-07-21 03:47:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 03c5a874-7d39-3ec6-95f1-4cf6986d781d | -23.13648 | -48.67448 | 2026-07-21 03:47:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5ab96935-83fe-3c19-8723-5859f69d5f1a | -23.77835 | -49.04342 | 2026-07-21 03:47:00 | NOAA-20 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 635a4068-2938-377e-a43a-53475bf601c7 | -23.29253 | -46.16288 | 2026-07-21 03:47:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| fb28c0a6-b68f-3c6b-9b53-e273778531a5 | -22.79704 | -49.34404 | 2026-07-21 03:47:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02eded17-b262-38c1-b795-ef4c68b2b042 | -23.28776 | -46.16164 | 2026-07-21 03:47:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f4b2226e-80dd-3555-9fd7-23d7ef410bad | -22.23621 | -42.53832 | 2026-07-21 03:47:00 | NOAA-20 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| aa0f5b57-7273-3f40-a575-cd40b576c3b0 | -22.73707 | -43.77633 | 2026-07-21 03:47:00 | NOAA-20 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2c43665e-d316-3b31-a09c-65f19dcdfc88 | -21.21145 | -48.98815 | 2026-07-21 03:47:00 | NOAA-20 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| be5ad959-5cc3-3c31-8bfe-4e75d23ca2d2 | -22.3439 | -41.78453 | 2026-07-21 03:47:00 | NOAA-20 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6c0899f5-8e4a-3542-b0aa-a7fa08b368ce | -22.79126 | -49.34229 | 2026-07-21 03:47:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bd2b1066-9a54-3ef3-846a-581bf865c34b | -22.23522 | -42.54348 | 2026-07-21 03:47:00 | NOAA-20 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| fd5ae44b-d918-39f7-92c2-b614972f18e3 | -22.79595 | -49.34868 | 2026-07-21 03:47:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5b2e685-1a0f-39b9-ad7d-c6badcc0809c | -23.28896 | -46.15602 | 2026-07-21 03:47:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 89517d23-fd44-3e0e-bf0f-c2b10fa73082 | -23.29375 | -46.15714 | 2026-07-21 03:47:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 39f48a03-0516-389e-a454-86217c1c88a5 | -22.90146 | -43.42418 | 2026-07-21 03:47:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 04abbe63-55b4-3a6c-8b25-cceaab72daeb | -22.44312 | -47.1545 | 2026-07-21 03:47:00 | NOAA-20 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7ff2de2-533c-31b4-9bb6-79bcb6fd0f30 | -22.71174 | -43.74963 | 2026-07-21 03:47:00 | NOAA-20 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| bce806cb-e412-3ed0-86b3-01047bf672a4 | -22.71256 | -43.74545 | 2026-07-21 03:47:00 | NOAA-20 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b82f2484-0dab-3154-b5e0-9d36b75057cd | -21.20555 | -48.98665 | 2026-07-21 03:47:00 | NOAA-20 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3a2cb07d-da1f-306e-ac74-4e74fc90a6c8 | -23.77934 | -49.03914 | 2026-07-21 03:47:00 | NOAA-20 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c060b602-4dd6-3e91-805f-a0947a1799c5 | -23.78062 | -49.04213 | 2026-07-21 03:47:00 | NOAA-20 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81a6ff5b-ba4f-396f-8af6-0b4690919f22 | -13.3023 | -45.1511 | 2026-07-21 03:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| a5c12031-80c8-31f6-a64e-6907b7cc6a96 | -18.5675 | -56.8109 | 2026-07-21 03:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.4 |
| 510cf1eb-2387-318a-915e-95c12cff2afb | -13.3217 | -45.1479 | 2026-07-21 03:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 5029e89d-e6db-305a-9223-4524e2226f15 | -13.3221 | -45.1246 | 2026-07-21 03:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 276.1 |
| cb84c957-648f-3bfb-b932-11754a4e6b05 | -13.3028 | -45.1278 | 2026-07-21 03:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 307.8 |
| 18180e78-2981-3a54-ba38-add7507e134a | -18.5472 | -56.8343 | 2026-07-21 03:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.0 |
| 6cfd6e12-3483-3a65-8a4d-e03687b849da | -13.3032 | -45.1045 | 2026-07-21 03:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 56.6 |
| e3fcee7e-8b01-3422-9717-ff3d9ed4e9a8 | -18.5671 | -56.8317 | 2026-07-21 03:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.8 |
| 67e0a91e-264c-372f-ad80-2e0e92f36080 | -13.3226 | -45.1013 | 2026-07-21 03:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 45764850-d09b-3263-a942-864381355239 | -18.5476 | -56.8135 | 2026-07-21 03:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 188.3 |
| 6c268684-9561-3c04-8d64-4143b3498eba | -18.5476 | -56.8135 | 2026-07-21 04:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 165.3 |
| 2fa253f0-067c-3f92-b480-db77f54ad0df | -13.3023 | -45.1511 | 2026-07-21 04:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 939afd3a-d106-3cc8-b9c1-1f50a8904a10 | -18.5675 | -56.8109 | 2026-07-21 04:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.0 |
| 171468ab-6a5b-305a-9254-8f962105fb7b | -18.5671 | -56.8317 | 2026-07-21 04:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.3 |
| 2e576f04-f45c-3141-8f42-d287f34de4a8 | -18.5472 | -56.8343 | 2026-07-21 04:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.3 |
| aa7bde4e-ce1b-342e-9308-deb21d485ff5 | -13.3028 | -45.1278 | 2026-07-21 04:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 217.3 |
| c4f6c537-e5f8-376e-bfdf-a290d4f3a4e4 | -13.3221 | -45.1246 | 2026-07-21 04:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 237.3 |
| fa4b1657-532d-30b6-befb-0cb95c68b78d | -13.3032 | -45.1045 | 2026-07-21 04:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 4fe737fb-2604-3bea-99f4-0d14ebf13182 | -13.3217 | -45.1479 | 2026-07-21 04:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 30dedf18-5dd8-3baa-b003-bf3adbc40e02 | -13.3226 | -45.1013 | 2026-07-21 04:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 1996c976-3ea6-3b2a-b1fa-a859759d533c | -18.5472 | -56.8343 | 2026-07-21 04:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 141.0 |
| 0aa8ca5e-826e-3d7b-b7fb-7e2f8ceed2bf | -13.3023 | -45.1511 | 2026-07-21 04:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 8737fa5c-cddd-3df9-97c6-61a7862aec51 | -18.5476 | -56.8135 | 2026-07-21 04:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 186.8 |
| 6681cd43-b53a-39d4-a148-0819cb384f71 | -13.3028 | -45.1278 | 2026-07-21 04:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 253.6 |
| ddd342fb-2327-34aa-a866-4c432115d470 | -13.3032 | -45.1045 | 2026-07-21 04:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 52.5 |
| fedcb0aa-8361-3f95-97a0-af3cbaa2c987 | -13.3221 | -45.1246 | 2026-07-21 04:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 4ce614c1-1812-33f9-95db-366704516acc | -13.3217 | -45.1479 | 2026-07-21 04:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 46fd815e-b0a7-3760-b727-2eca6b4b499b | -13.3 | -45.14 | 2026-07-21 04:15:00 | MSG-03 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f6f79c76-0b3d-3e00-917f-d2107a0f51e9 | -13.3221 | -45.1246 | 2026-07-21 04:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 639e3038-debc-3dac-83bc-611a74e4c04a | -18.5675 | -56.8109 | 2026-07-21 04:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.4 |
| 587ecf95-f384-3218-8e9f-cbfe5b724e0b | -18.5472 | -56.8343 | 2026-07-21 04:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.9 |
| f394b746-adda-3378-86e0-2ce3276ef2a9 | -18.5476 | -56.8135 | 2026-07-21 04:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 197.0 |
| 5948c7f1-332c-3b4f-ac20-3ee71b751b4d | -13.3023 | -45.1511 | 2026-07-21 04:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 54.2 |
| da407cc1-40e1-3703-acfe-a5a19cf22622 | -13.3028 | -45.1278 | 2026-07-21 04:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 213.6 |
| f1dc64a5-70ff-3552-b3f8-5cc9844258b6 | -13.3217 | -45.1479 | 2026-07-21 04:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 9af58b06-c7d5-39b9-909f-eb720bfe979b | -7.08422 | -46.53579 | 2026-07-21 04:25:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8c1aa6c-58dc-3591-8db8-67de25b6a44c | -3.79588 | -42.94765 | 2026-07-21 04:25:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b1584af-a098-34c4-9b27-fb5e72b8b5b6 | -5.7051 | -45.84502 | 2026-07-21 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 430c0bed-73c3-3c17-b7f6-c86a4018dcb8 | -3.52544 | -42.7007 | 2026-07-21 04:25:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b79fad73-e354-3c14-8504-aaded6ab2c67 | -3.23944 | -47.92432 | 2026-07-21 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a7a142d-0982-33f2-b12d-bc9e818e997d | -3.57806 | -43.46438 | 2026-07-21 04:25:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README6.md)
