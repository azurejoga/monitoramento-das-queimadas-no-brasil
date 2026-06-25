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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8173b9b7-e297-3bed-af41-7c1a10840ac5 | -14.2647 | -52.04452 | 2026-06-25 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a465bfae-db4f-315c-9bc2-ed2d7ce09ec8 | -11.90714 | -56.86555 | 2026-06-25 04:17:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a6243197-bcd2-37b9-9932-9396117810c1 | -11.24692 | -43.33091 | 2026-06-25 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5b194625-18e8-324b-83c5-0357e830d9cf | -11.54531 | -52.77878 | 2026-06-25 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a103ff9e-42a3-3932-bc23-dca5ae0b5aed | -11.89242 | -51.74642 | 2026-06-25 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 28.1 |
| f2f8cc52-5776-35c7-8a5a-b3d4bd5b9ddb | -12.16507 | -46.68196 | 2026-06-25 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 59cbb564-ead9-3c4d-934f-a24c9dd46c17 | -12.22158 | -55.50179 | 2026-06-25 04:17:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dc1ba7df-58a2-3353-a3c1-71ff677b68c8 | -10.77744 | -54.1111 | 2026-06-25 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ad7200d-e1af-3e80-a049-b16b6e7dc75c | -11.9133 | -46.62741 | 2026-06-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cefb023d-a11e-382a-a6f2-277a3571ce7f | -11.25078 | -43.32793 | 2026-06-25 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 5d06db01-9425-3a20-ba4c-86c5ee1ca44a | -12.74955 | -44.45393 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a25b9a24-d58d-31c0-8850-2d2bde946c85 | -11.20219 | -49.41897 | 2026-06-25 04:17:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6fa54733-d318-3aaa-82ec-fe2075533571 | -10.3663 | -47.33941 | 2026-06-25 04:17:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 720c38a2-01c3-3339-9a09-be613de5ff02 | -12.45451 | -46.52233 | 2026-06-25 04:17:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 09ac85cd-33a1-3b91-9775-743051e7b551 | -11.64378 | -52.86182 | 2026-06-25 04:17:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 893968fe-7bc7-3dfc-bf61-d724644ffc6d | -13.20013 | -48.31981 | 2026-06-25 04:17:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 448e07ea-d2a0-34ea-9a20-9ed6fb4060af | -11.91977 | -44.16864 | 2026-06-25 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f701e5b1-8a32-375a-885f-e03015281052 | -14.89934 | -47.74563 | 2026-06-25 04:17:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9a1bb4c-c086-35c6-b8dc-e69e35f28d73 | -12.83311 | -44.35621 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bb4c21ae-6985-304a-9563-55416c97e7df | -11.90963 | -43.39917 | 2026-06-25 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 051d1c81-2a36-36bc-966d-d5421514ffaf | -16.08201 | -45.89636 | 2026-06-25 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 407876c1-6cbc-36f7-865b-bca619bc704c | -13.20384 | -48.3204 | 2026-06-25 04:17:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d42c915-8870-3901-a935-fac3c0a28525 | -12.74625 | -44.4534 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 68216fa5-c2a8-3eec-9f38-72d771e13642 | -12.73245 | -44.36834 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96d325e0-0a58-3055-9223-c7150a09f6eb | -13.03454 | -49.93688 | 2026-06-25 04:17:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf6513c5-e5ad-33bd-ac4e-89f828211777 | -12.738 | -44.46287 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 92ccad86-1730-3dad-baf1-cdb7dbd8034c | -11.90831 | -56.85984 | 2026-06-25 04:17:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1a69257-d868-34de-8aeb-72aa47f75d6c | -13.20755 | -48.32101 | 2026-06-25 04:17:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0664296-d670-3aaa-8290-717b56b3f670 | -12.84631 | -44.35834 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a50dbdf-55ea-3d39-8ada-dec3779431cf | -12.74405 | -44.46745 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fabf4a80-5906-3d36-8ca1-4b40f6f945f1 | -12.78036 | -44.43414 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0c49d43-5a7e-37c7-841c-a8aeb7e08a16 | -11.30891 | -54.7131 | 2026-06-25 04:17:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9404c3e4-90e8-3ea0-a09a-2465a4bbf53d | -10.53014 | -48.16022 | 2026-06-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e2d784b-f649-3d7e-be7e-40d64d65be9b | -10.36994 | -47.34003 | 2026-06-25 04:17:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a95a41f6-15ce-3554-b842-e110f1f23c28 | -17.34573 | -42.62817 | 2026-06-25 04:17:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7ffc68e9-ce5e-3838-9d17-1e94808d18d9 | -11.92367 | -46.62938 | 2026-06-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8dc5b6e0-0200-3d61-8bf8-6e8d71fbdbf6 | -13.87001 | -47.14676 | 2026-06-25 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31afaa8c-c255-3d04-9546-815d5b965912 | -12.22081 | -55.4917 | 2026-06-25 04:17:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 627917a5-82ba-3785-8213-e157e529f806 | -12.84686 | -44.35483 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1c4ec7c-8baa-3a14-a13f-e1cb205da2f6 | -9.88347 | -52.43935 | 2026-06-25 04:17:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13ffaa61-a7a1-3a7f-ae7e-9ace275dae9c | -12.84851 | -44.36591 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec0c7740-8f2c-3150-8333-76402cf77971 | -11.75324 | -48.83282 | 2026-06-25 04:17:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad03b652-c2b2-37a7-b066-33b8bd2ea869 | -11.92303 | -46.63327 | 2026-06-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c1cb306b-c4f9-3689-91e8-713843b61be2 | -11.09966 | -49.45437 | 2026-06-25 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a420c2a-47ba-310d-8afa-55f2a7ff33b4 | -13.83195 | -47.01984 | 2026-06-25 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 294b1a1e-23e1-3402-bf73-970f8fcce6ba | -12.21559 | -55.50076 | 2026-06-25 04:17:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 52a98494-2047-3582-8461-2b588a61a87e | -17.34632 | -42.62399 | 2026-06-25 04:17:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| c6e1ce9a-4be0-3024-ba4d-d4f4b864e659 | -17.34985 | -42.62455 | 2026-06-25 04:17:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9c3b9888-0116-3116-aeee-f63cc8e5dd0b | -11.79353 | -56.99475 | 2026-06-25 04:17:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec05a7fa-ccea-33ab-a6af-01c908798a39 | -12.83861 | -44.36431 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 65c617f0-6baa-325b-b061-9b698e5b3333 | -13.07312 | -53.35494 | 2026-06-25 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9254ed81-c867-3011-b73d-893652d9f06f | -12.22498 | -55.50203 | 2026-06-25 04:17:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 54a5cde7-2102-310a-a8ce-d29423cea43e | -11.89712 | -51.7473 | 2026-06-25 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 112988e0-f98f-3383-b4fc-8d48f99eeb7d | -12.31666 | -46.73836 | 2026-06-25 04:17:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 70685d7a-f440-3e26-ac7e-9b12cc01961b | -12.16224 | -46.67745 | 2026-06-25 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a1bd4c4-91f5-3d5c-8944-5b263ada1daa | -11.92021 | -46.62872 | 2026-06-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70b23b12-2169-32ce-8cf0-920c91a3e774 | -11.0453 | -47.03856 | 2026-06-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4271c793-2402-32b9-a64b-d8007d7cad38 | -12.07924 | -54.61103 | 2026-06-25 04:17:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 13a579d8-a8bb-3e50-ad27-1e66ac896a86 | -12.7413 | -44.46341 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| becbc496-913b-3672-a4db-628302bd61b7 | -12.55414 | -54.5927 | 2026-06-25 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ebe3b762-d119-35b1-8e9a-28e514d7a6e3 | -10.7767 | -54.11495 | 2026-06-25 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 857de85c-126a-3f66-a11c-dad2a19301c4 | -12.73525 | -44.45882 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 96dfd828-d41c-32cb-9665-3d9696a85bec | -14.7531 | -47.55453 | 2026-06-25 04:17:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bdbe3f6d-2c72-3571-9c26-83d33f6d62cd | -16.71085 | -41.18522 | 2026-06-25 04:17:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| dcb331a0-8433-3897-8b94-b8136bb881a5 | -12.22408 | -55.50661 | 2026-06-25 04:17:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5e4f31b8-4bbf-3d9b-bf73-2be0894bb8c9 | -11.91922 | -44.17214 | 2026-06-25 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff43d02f-d9df-3dcd-82a1-35b4f080913f | -12.22344 | -55.49262 | 2026-06-25 04:17:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5b41296-79f0-3240-b281-c5c2cd94f3ca | -10.73623 | -47.26119 | 2026-06-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a5e7a08e-c383-3f28-bf95-bd33f6c84dd1 | -11.88011 | -51.76032 | 2026-06-25 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 103.9 |
| cb19feb5-0ca8-3007-a4bf-4e6354fe8f24 | -15.37288 | -47.35404 | 2026-06-25 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14ca0797-1957-316a-9ecf-f519dcd5516f | -11.91592 | -44.17161 | 2026-06-25 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7aba108b-545b-3df3-b4b2-23ba8957eb21 | -12.74295 | -44.45287 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3f44750b-b0a6-36ae-b02c-7d68cb15ad3a | -11.91393 | -46.6236 | 2026-06-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85eb9cdd-153f-3193-a74c-27b7a1e4af97 | -12.75175 | -44.46149 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ab9e4369-a58e-3305-b7bd-559a40b67768 | -12.84356 | -44.35429 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a1fc0ca7-2907-338f-a556-50feb3326c97 | -11.48952 | -46.74887 | 2026-06-25 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23a300b3-0835-3ed2-a799-bad8ab0daadc | -11.22211 | -43.33772 | 2026-06-25 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c0b1aead-a714-3ea7-b8b7-278e0c859e40 | -10.61694 | -47.12378 | 2026-06-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 30e797f8-1111-3ca3-b550-2b0678702dd1 | -11.37831 | -47.82251 | 2026-06-25 04:17:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d857f36-9583-3922-bb03-99ae4fd6a518 | -11.63815 | -52.86383 | 2026-06-25 04:17:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cb9e755c-0db5-3a16-8d42-ec63d108b351 | -12.22849 | -55.4983 | 2026-06-25 04:17:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5d2081bd-fe86-38b4-8cec-199736e41f3e | -12.21262 | -38.98371 | 2026-06-25 04:17:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cfcf36b4-7512-3e68-bae7-70a599abb90a | -12.13934 | -48.26834 | 2026-06-25 04:17:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 24fde7b5-c3ca-35f1-970f-83073f248d02 | -9.88621 | -52.44067 | 2026-06-25 04:17:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1f61ffca-9cd7-368f-a859-fcfca78dd02d | -11.88772 | -51.74554 | 2026-06-25 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 36d5e7e6-0ea1-3f21-a37d-51a5d9b19a8a | -11.20285 | -49.41526 | 2026-06-25 04:17:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5a9f8344-8cc0-37c9-81e6-afe88a277201 | -15.89459 | -42.69384 | 2026-06-25 04:17:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e606a16-632f-3587-94a0-7488d7a60994 | -12.06519 | -48.42562 | 2026-06-25 04:17:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c29a2a6-9eb2-3522-af67-a4de89b6acbd | -14.85496 | -42.79193 | 2026-06-25 04:17:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6cd68643-208f-3bb6-8577-57c0f57009ce | -12.7512 | -44.46501 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8478b0a6-47cb-3372-b5f5-c270bec76dd5 | -12.219 | -55.50092 | 2026-06-25 04:17:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cfd3cc2e-215f-354a-8070-11e012a482e0 | -11.28144 | -53.95203 | 2026-06-25 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a8cb36e-fdb7-3e66-91f1-c44a7c8e4c10 | -10.38378 | -47.30232 | 2026-06-25 04:17:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01556de4-a0ff-3f44-bdbe-44f15d0856a9 | -12.21991 | -55.49631 | 2026-06-25 04:17:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 79c61d51-3b2d-384c-9c58-fb444b245f46 | -10.17432 | -51.66107 | 2026-06-25 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d95af2a0-9b51-37d6-96b8-60959258c405 | -12.7391 | -44.45585 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 03ff4ab4-f55f-3a60-b5ef-03f06b693e4f | -13.86165 | -47.1423 | 2026-06-25 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff309c3f-d78c-31e0-90ff-3eca60e79e9f | -13.86438 | -47.13773 | 2026-06-25 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b1e8587-2383-3819-b8a0-3f9ea0d9401e | -10.73695 | -47.2569 | 2026-06-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 628f1d0e-84ab-3048-8b98-99c55b9d9324 | -11.3215 | -43.3322 | 2026-06-25 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README11.md)
