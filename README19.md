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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a9588b0-19bd-3d68-b27c-a31ebf2dd2f0 | -10.6128 | -44.3284 | 2025-09-06 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 282.5 |
| a0739a70-f431-310c-aa45-b8a2f19b04b5 | -10.5937 | -44.331 | 2025-09-06 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 136.2 |
| e4620c66-0d48-3a72-a316-d9043e92b019 | -12.9665 | -54.8116 | 2025-09-06 03:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| b1de6fdf-1d3d-3e03-8efd-77da523710e5 | -9.7041 | -49.4825 | 2025-09-06 03:10:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 569aae71-e1aa-3ad7-95ff-2a662de856e1 | -10.6131 | -44.3051 | 2025-09-06 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 8488b360-740e-3667-a61f-ba24f209225d | -14.9214 | -49.4289 | 2025-09-06 03:10:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 49.9 |
| a30eb949-2a95-3a61-a14b-7d7a2ca54c79 | -14.9209 | -49.451 | 2025-09-06 03:10:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 2f9c4f36-954c-3448-a9a3-621cb6809bb9 | -13.0235 | -54.8262 | 2025-09-06 03:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| bae6244a-b351-385f-8855-9a4d3cb746c8 | -10.594 | -44.3077 | 2025-09-06 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 60fbcd5a-af9c-3217-959f-b6bd6c0aa383 | -13.0044 | -54.8282 | 2025-09-06 03:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| aa7c3e8f-e5a3-3cc1-9588-4ca64a31a634 | -14.9019 | -49.4319 | 2025-09-06 03:10:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 84.7 |
| a7ab4100-259e-396f-94f7-2970fc938e22 | -14.9015 | -49.454 | 2025-09-06 03:10:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 141.4 |
| bef2c265-704a-3f34-88f7-c1e3d85c1791 | -22.2424 | -48.7513 | 2025-09-06 03:10:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 78.3 |
| 51aad23d-7ddf-35dc-8901-0e34703d195e | -15.5747 | -52.9175 | 2025-09-06 03:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| e5a7d795-b08e-3bd0-a470-61692b5bfc7d | -15.5747 | -52.9175 | 2025-09-06 03:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 36e6fbc2-bf9a-3737-9997-1576087de204 | -4.5031 | -42.8854 | 2025-09-06 03:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| ea37648d-c9fd-3fa9-b5f7-0c9b4573afdf | -14.9019 | -49.4319 | 2025-09-06 03:20:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 138.9 |
| ae59c6f6-f68c-38e3-b67f-6700655c9c3a | -14.9214 | -49.4289 | 2025-09-06 03:20:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 8fef4dec-9a0c-3e1b-a917-28a3488565a7 | -13.0044 | -54.8282 | 2025-09-06 03:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 2722fa43-4641-33d7-bf2f-363941d1d1d2 | -14.9015 | -49.454 | 2025-09-06 03:20:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 228.0 |
| dedfc650-dd86-349e-a84e-7c01f687281c | -13.0235 | -54.8262 | 2025-09-06 03:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| b341e0c0-768e-3c7c-a9f8-b8a467527adc | -10.5937 | -44.331 | 2025-09-06 03:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 1f76180f-ca0c-3afa-82f0-02f9411adbb9 | -12.0992 | -45.6856 | 2025-09-06 03:20:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 68e89b61-0f24-33be-be4c-76af444eb994 | -10.6131 | -44.3051 | 2025-09-06 03:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 86e03642-31ca-3e29-bb6d-1b0f7767e161 | -10.6124 | -44.3517 | 2025-09-06 03:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| c74db787-bf40-3c7d-9e87-8d998a4788e3 | -12.9665 | -54.8116 | 2025-09-06 03:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 105608cb-ab10-3b18-b442-9a76adef686e | -10.6128 | -44.3284 | 2025-09-06 03:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 296.9 |
| 6e8d3c17-fe73-3c96-b6a1-26339110c352 | -14.9209 | -49.451 | 2025-09-06 03:20:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 13fb548c-3ea6-3ea8-8ce4-f2066e1d5ebe | -14.9015 | -49.454 | 2025-09-06 03:30:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 1ffa9ee4-64cf-32a1-a929-0a3c5c3ee34a | -19.9051 | -57.9213 | 2025-09-06 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.3 |
| 2c0d9626-d560-3d26-b693-0e5d687604cb | -12.9665 | -54.8116 | 2025-09-06 03:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 8ca94550-2579-3efc-a1b6-9aa2d1bda149 | -9.7041 | -49.4825 | 2025-09-06 03:30:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| a6f42eeb-76da-3554-bbbc-090c61bfdaef | -13.0044 | -54.8282 | 2025-09-06 03:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 3c1060a8-c29f-3a93-b6f3-3905988de77b | -4.5031 | -42.8854 | 2025-09-06 03:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| a0065808-9694-392d-95a0-3d6d5d96c470 | -19.9047 | -57.9421 | 2025-09-06 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.9 |
| 176f8522-5342-386b-9014-313059ef115d | -15.5747 | -52.9175 | 2025-09-06 03:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 89f0b793-1ee3-3be3-9213-7fc83e55dd83 | -13.0235 | -54.8262 | 2025-09-06 03:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| e7d5d21a-d53f-3977-bed9-5bcb7f2e26e6 | -13.0044 | -54.8282 | 2025-09-06 03:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| cff3e041-d322-379f-b07f-aa47e9552da3 | -14.882 | -49.457 | 2025-09-06 03:40:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 8f65c020-fece-380e-b986-cce6706a486b | -12.9665 | -54.8116 | 2025-09-06 03:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 56173d58-8e53-3ded-b3b3-6aaf147333a4 | -14.9019 | -49.4319 | 2025-09-06 03:40:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 5fb36d69-8e7f-34fc-8a63-d058a0eb299d | -22.2424 | -48.7513 | 2025-09-06 03:40:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.9 |
| 1d115e5c-123f-304e-ae01-a0e2530b454f | -19.9047 | -57.9421 | 2025-09-06 03:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.6 |
| b3362204-7d3b-33a8-a8db-2e6b5d5cc030 | -14.9209 | -49.451 | 2025-09-06 03:40:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 55.8 |
| d4324ad2-8df5-3de6-9e7f-0e57b4f44660 | -14.9015 | -49.454 | 2025-09-06 03:40:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 214.5 |
| 8bd4a0bb-9c96-36ce-94a2-9deba3267d82 | -22.2633 | -48.7463 | 2025-09-06 03:40:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 82.6 |
| faa4225b-4477-3165-9a7c-8fbac9720190 | -4.63511 | -42.52945 | 2025-09-06 03:47:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7c6e028f-2a7f-3e3f-b252-807f5d4d94e7 | -5.87472 | -46.04981 | 2025-09-06 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3114e8e-7a62-39b6-a184-5cb8bb858375 | -2.47172 | -47.77682 | 2025-09-06 03:47:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| acda3c9d-3237-3a34-8c63-5bf14930cbd5 | -5.87236 | -46.05011 | 2025-09-06 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0bf1c5eb-9a42-3c11-a9e7-f393bd6831a8 | -6.38713 | -43.00742 | 2025-09-06 03:47:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0938da8a-a161-3c83-a4d2-c01dd47de4fd | -6.24563 | -43.30212 | 2025-09-06 03:47:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 566b86a7-4065-3c83-ba8c-a5ae7d76abe5 | -5.72811 | -46.44455 | 2025-09-06 03:47:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d673a70-42c7-3cdd-8db5-6c7bf270fa93 | -6.21749 | -43.36393 | 2025-09-06 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0921ad22-61c5-3e62-9247-95ecc5d1b905 | -5.54856 | -43.06549 | 2025-09-06 03:47:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56865fac-7acc-3afb-af9e-c799d2029452 | -5.95739 | -44.74261 | 2025-09-06 03:47:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 41083937-73d8-3af8-a45b-6cac357954e3 | -5.54058 | -43.08601 | 2025-09-06 03:47:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03fed4f1-cd37-3ef8-b205-57de43802586 | -3.16445 | -49.47517 | 2025-09-06 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e13dde19-cc47-3283-ae70-4378ee293366 | -5.63056 | -44.99916 | 2025-09-06 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c5e1e08-7561-35c7-9c3f-60444c79c21b | -5.95759 | -43.02972 | 2025-09-06 03:47:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0cf9c82e-b5df-3433-8915-91d1667829ed | -5.73073 | -43.90858 | 2025-09-06 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f3d9f948-f330-3455-9b11-f461e7b1a96b | -4.80132 | -47.26273 | 2025-09-06 03:47:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 518a128e-6ab7-3b48-9e43-1531d0d4b367 | -5.74667 | -43.70534 | 2025-09-06 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e5845af-2e32-3ffe-a22c-1d101e4dc52c | -5.87053 | -46.04213 | 2025-09-06 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c73d508-8764-349f-8c86-134be184de64 | -5.3365 | -42.78712 | 2025-09-06 03:47:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| baaea307-2497-35a7-b772-fcf82dd342a4 | -3.59207 | -40.00702 | 2025-09-06 03:47:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 66503894-1148-388f-a5f8-40d1fbee57c7 | -6.38572 | -43.01557 | 2025-09-06 03:47:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 600b9fab-3495-3609-9f3a-03917d1bce79 | -6.21763 | -43.35897 | 2025-09-06 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6749897d-501d-322c-a494-927232ecb67b | -5.65877 | -43.61213 | 2025-09-06 03:47:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52295fd8-dbeb-3e07-8245-eb813eb3559e | -6.20889 | -42.62793 | 2025-09-06 03:47:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a314a89a-90c3-3c7b-840d-7643a3d8e839 | -6.21661 | -43.57762 | 2025-09-06 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a832425-71ee-30fc-8ba4-0e78eb13debe | -3.11364 | -40.83597 | 2025-09-06 03:47:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 631a7a82-1d6b-3a33-b6e3-60efb28ba622 | -5.86466 | -46.03153 | 2025-09-06 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b2f00c0-6a44-3cf9-9502-862d69fa2bab | -5.72106 | -43.93718 | 2025-09-06 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 252adcc5-423b-3b9d-9a26-c3ab648caaa5 | -6.24352 | -43.28888 | 2025-09-06 03:47:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 913405ec-52ec-3b7c-a584-57e93582603f | -6.17306 | -43.27677 | 2025-09-06 03:47:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| af6ad1bc-70e9-3198-ad90-8ddacc35db5c | -5.54129 | -43.08182 | 2025-09-06 03:47:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 268acae2-18f0-3d09-aaf1-180914ba5e9d | -5.95831 | -43.02552 | 2025-09-06 03:47:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2e5c75e7-0ed6-332e-9a35-919a667eda5b | -5.92765 | -43.7201 | 2025-09-06 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 093d33d1-11e6-3519-9338-05615d903dc2 | -6.55137 | -42.94139 | 2025-09-06 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea5a1fc2-9044-3b4a-b897-f2b5cd2a8fce | -5.34083 | -42.78781 | 2025-09-06 03:47:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 929e494f-e2ec-3e00-84fc-426a7bd07349 | -4.54901 | -37.78836 | 2025-09-06 03:47:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 73ee1185-14d1-32d9-b011-072b5c3ec021 | -4.45443 | -44.14232 | 2025-09-06 03:47:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 468ec478-78bb-3ef2-b3b7-c54d55d78594 | -5.55887 | -46.53773 | 2025-09-06 03:47:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 760cf24a-2f23-397d-bcb0-8de6f307736c | -6.39288 | -43.81471 | 2025-09-06 03:47:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32aaa359-255e-31d5-99cb-83ad060fd3fd | -6.20343 | -43.36634 | 2025-09-06 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1fe1a2e5-9b4a-3095-8c37-f1b35c932f8b | -5.75569 | -43.12433 | 2025-09-06 03:47:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bc023145-c4fb-3c85-b742-dd4734859023 | -5.73314 | -45.36241 | 2025-09-06 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64f4263a-e863-3cf9-8afb-aa86fd6a3208 | -3.96728 | -43.24091 | 2025-09-06 03:47:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0efc3101-787e-31a1-a8f3-1d57222a232c | -3.98201 | -47.88457 | 2025-09-06 03:47:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c463087c-cec6-3e45-a749-f2bdb08f089b | -5.55739 | -46.54094 | 2025-09-06 03:47:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 86690f55-d0c2-3f14-9d6c-5813b3b5d87c | -5.85096 | -45.30536 | 2025-09-06 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8dc5dcb-473c-3618-8f1d-574c07763efe | -3.16186 | -48.60223 | 2025-09-06 03:47:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 155f45d9-e86a-3dd9-9593-7472523aabcd | -5.98281 | -44.72791 | 2025-09-06 03:47:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 40d66079-a861-301c-93d9-f0e1828e0a72 | -5.44796 | -42.80819 | 2025-09-06 03:47:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| abad9109-be3b-32c5-afc2-0038b17bd819 | -5.73156 | -43.90374 | 2025-09-06 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cac8fe44-cf8b-3b67-bd13-55e60467c50d | -4.61221 | -41.54239 | 2025-09-06 03:47:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 660eb39d-aa68-3b56-a1b1-62175c1a6f7e | -5.8711 | -46.03877 | 2025-09-06 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 038a3199-ba4c-3753-a315-7d046f7133e0 | -5.94944 | -42.96382 | 2025-09-06 03:47:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f41603f5-9da8-3abe-a65f-8ae89e4b9b26 | -5.71641 | -43.93639 | 2025-09-06 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README20.md)
