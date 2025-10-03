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

## Dados Diários - Página 137

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e6f77cf-9fb6-3bb4-8feb-0e2db76c6a50 | -10.06524 | -48.18577 | 2025-10-03 05:23:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f81aebe4-bd48-371d-af23-dd8dc0b7eb8c | -11.31088 | -47.84193 | 2025-10-03 05:23:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5e650f9c-f451-3218-b9ff-03146716fec3 | -10.01003 | -50.22081 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 21e0ffc2-a792-395d-8c0a-e71189e01d0e | -7.24974 | -48.4793 | 2025-10-03 05:23:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4578b4f-33eb-3e0b-86f6-cfccc1ddc611 | -6.99657 | -47.20443 | 2025-10-03 05:23:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d4c8eca7-c93e-3d06-bf91-4f684b21d60b | -11.08343 | -47.86863 | 2025-10-03 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 61e2d78f-f88c-3d79-b6fd-c78e7528e453 | -3.16891 | -48.61174 | 2025-10-03 05:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d26203b5-f0bd-34c6-b6a2-73b5c4c51ea7 | -10.00836 | -50.23474 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 574c5391-2572-3255-bec5-d6a8c1fb1581 | -10.6562 | -48.48258 | 2025-10-03 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7b7b6d72-d0e7-3b0e-b9aa-8c6e085b520c | -4.89588 | -49.96276 | 2025-10-03 05:23:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36a442af-ad8f-34b7-9637-3cf0bd809de6 | -10.41305 | -54.40651 | 2025-10-03 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1dd999d8-6d0e-3cfe-9dca-82b96d0471da | -10.00229 | -50.2339 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 57f7f5c8-004d-30a6-88e6-d3f78a67dfdc | -4.89533 | -49.96682 | 2025-10-03 05:23:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 191afb28-d012-394a-b4cb-a35db8808291 | -10.60518 | -48.71953 | 2025-10-03 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e86150fa-d109-34ff-a0a7-5104796936b4 | -9.99588 | -50.22344 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 7880d3fc-da2a-3eb6-b6ff-670aa2e3160c | -4.51187 | -55.45711 | 2025-10-03 05:23:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0bc091f-8693-3c49-86e3-a2d817affdc1 | -7.00355 | -47.20562 | 2025-10-03 05:23:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e9d10224-fa53-3e07-be72-ec01a0dfd590 | -11.3341 | -56.20551 | 2025-10-03 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56f0a444-2f19-3ebd-b46b-251893f504f0 | -9.93503 | -59.80362 | 2025-10-03 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76b2b891-9000-3313-94bd-312364054b91 | -10.89819 | -56.20253 | 2025-10-03 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 75f5676a-1103-37c3-b200-abc2b146e6eb | -11.12029 | -47.86038 | 2025-10-03 05:23:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d9169904-5588-325f-a6f7-ca97f4c71c35 | -10.28638 | -50.30374 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00b3283f-8930-3efa-bb1b-54506cb768a6 | -10.60851 | -48.72149 | 2025-10-03 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ff56d24a-ddff-31bf-95c2-e46dc0ed63fb | -2.92445 | -48.30487 | 2025-10-03 05:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 66640ce5-49a2-3c75-ae9b-69b46af3d05f | -7.25525 | -49.41216 | 2025-10-03 05:25:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d7fc7492-1a38-3166-9739-16e33b1af6c1 | -14.97997 | -49.97156 | 2025-10-03 05:25:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9c905b3e-6f4e-3c4c-acb1-958e49a77960 | -16.68474 | -53.01788 | 2025-10-03 05:25:00 | NOAA-21 | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 044c40d8-2626-3db6-a5c5-cecb89448eb4 | -8.52088 | -50.03551 | 2025-10-03 05:25:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9566f6c-6a9d-3877-a953-4b5eebdad392 | -11.78816 | -61.87863 | 2025-10-03 05:25:00 | NOAA-21 | ROLIM DE MOURA | RONDÔNIA | Brasil | 1100288 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf287602-87a8-3856-bfb3-92554bc4b758 | -8.75903 | -49.91943 | 2025-10-03 05:25:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f656ed32-b985-3842-8778-45d864a4a767 | -14.57833 | -52.47114 | 2025-10-03 05:25:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 95cc2e59-bd76-3c13-8d70-ff299726f019 | -7.24971 | -49.40648 | 2025-10-03 05:25:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8701baa-3e58-3099-a046-b9b13fd57b74 | -15.25459 | -50.12553 | 2025-10-03 05:25:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| aa6bab7b-0130-37da-8587-20d97817f1a3 | -18.19459 | -53.29063 | 2025-10-03 05:25:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 962326a1-2fdc-398d-8ebd-e636864030f6 | -18.16763 | -53.33544 | 2025-10-03 05:25:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12acfd62-22e5-3887-afb2-434d42fa6d6f | -7.24846 | -49.41613 | 2025-10-03 05:25:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b937a27-8a7e-3ab0-88a0-081f20ede80a | -18.16674 | -53.34428 | 2025-10-03 05:25:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1b488045-9ca0-3034-b32a-faabfc64fcd6 | -8.61684 | -54.97871 | 2025-10-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a27090a7-9b5d-3ce2-a1f3-b53a2bf93812 | -14.85996 | -49.31795 | 2025-10-03 05:25:00 | NOAA-21 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7f7e2ea2-6a3f-351f-b51b-b8861b77ed12 | -16.0546 | -51.04329 | 2025-10-03 05:25:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca3b484e-ea7a-34bc-aa90-df59470e2348 | -14.58008 | -52.45574 | 2025-10-03 05:25:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 28c83fad-f6a9-349f-acdc-81791c76d1b1 | -16.17823 | -57.59637 | 2025-10-03 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c926a7b8-b71b-3c6f-8149-cc7f23b1e21f | -15.02647 | -56.03959 | 2025-10-03 05:25:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3ab91ae4-87c7-3584-8552-c31f3f991822 | -14.57964 | -52.45966 | 2025-10-03 05:25:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 57b837fe-a488-3b12-a69c-2df1455b3855 | -16.93078 | -54.14953 | 2025-10-03 05:25:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47b498ff-1a9b-35fb-9961-719493a8b04e | -16.17061 | -57.59156 | 2025-10-03 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 63b08e09-bd8c-321c-90d8-40ab866b9a43 | -16.68508 | -53.01537 | 2025-10-03 05:25:00 | NOAA-21 | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7ee74631-1065-33cc-a84f-daf2856cfb51 | -6.94077 | -59.53305 | 2025-10-03 05:25:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f87dcb8-9ab1-3c6c-87f1-28978eb26e28 | -13.68192 | -48.63975 | 2025-10-03 05:25:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bdbc8672-0b35-315d-9478-b4aaea951673 | -18.20444 | -53.357 | 2025-10-03 05:25:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4315731-003f-3ee3-a1a1-db6ab7b07736 | -16.05601 | -51.03938 | 2025-10-03 05:25:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e2d89a3-24d7-3900-bb1f-7cb618ceeaa8 | -8.61099 | -54.97165 | 2025-10-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f92c2449-f940-3925-9358-2bb5f366e63e | -14.98747 | -49.96257 | 2025-10-03 05:25:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 30a74567-4962-3411-be89-0daaf8bd6757 | -15.01825 | -56.03369 | 2025-10-03 05:25:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef029b6f-6e45-3195-a5ff-3bebc8acc495 | -15.22893 | -56.83383 | 2025-10-03 05:25:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cb68a963-6a44-3b70-8b9e-ffd1f03f279f | -14.38049 | -48.47794 | 2025-10-03 05:25:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d19d3080-05c0-345c-a722-9bcd88178885 | -8.61475 | -54.97645 | 2025-10-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad42ba93-8571-3df8-a5fb-eea575965857 | -8.61965 | -54.97284 | 2025-10-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d316d63-9838-3ad9-9c7a-1007b1979e18 | -13.68314 | -48.62827 | 2025-10-03 05:25:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d07556c7-f2c7-395b-a994-40136cb5a027 | -8.02334 | -55.41674 | 2025-10-03 05:25:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88f24e43-5061-3813-a265-b791615c44dd | -11.78761 | -61.88213 | 2025-10-03 05:25:00 | NOAA-21 | ROLIM DE MOURA | RONDÔNIA | Brasil | 1100288 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 884d6177-bc41-386c-b069-85305ea041d2 | -14.37591 | -48.47744 | 2025-10-03 05:25:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ada12aa3-6f27-3b3f-b01d-85f33a3eed3e | -12.23048 | -60.84311 | 2025-10-03 05:25:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 748e13a0-8108-310c-bbc4-7ed93774ce70 | -8.6234 | -54.97763 | 2025-10-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f7325ed-914f-3d89-9e0b-cdc8d89c5043 | -8.61588 | -54.96811 | 2025-10-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8bcdbe39-a2d7-38e6-b992-03aaf0bed152 | -15.24135 | -50.12645 | 2025-10-03 05:25:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a4ee27c-ee95-3c5b-9577-a74244646359 | -14.85853 | -49.31298 | 2025-10-03 05:25:00 | NOAA-21 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e664068c-86d1-3775-9e98-721e5e3d63f5 | -18.23259 | -53.35593 | 2025-10-03 05:25:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5e7fe4e-3c04-3636-8fe5-f450c0729f01 | -8.61804 | -54.97036 | 2025-10-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f4ab836-9987-3652-8651-c55aeed7e792 | -8.61532 | -54.97227 | 2025-10-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 657d2cc8-7ba7-3de0-9c21-80c42404fdd5 | -8.75918 | -49.92693 | 2025-10-03 05:25:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e571c67b-2d3e-3707-9540-27ecffbd7c7c | -8.6266 | -54.98655 | 2025-10-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e6ab7a5-24e4-3a43-ad75-1a052ed6566c | -8.52032 | -50.04003 | 2025-10-03 05:25:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5da49255-229a-31c6-8199-8219292da792 | -18.19895 | -53.35622 | 2025-10-03 05:25:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 59789eae-9a46-3eba-ad46-64ef67950ace | -16.40172 | -52.15475 | 2025-10-03 05:25:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e143361f-1d86-3afb-b20a-feaf8a4e7843 | -16.9363 | -54.1468 | 2025-10-03 05:25:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0508480-be1d-3e87-bf09-d918c26064e4 | -8.62226 | -54.98599 | 2025-10-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 718bb083-57b4-3665-b28b-781cd7c50c19 | -15.23491 | -50.12508 | 2025-10-03 05:25:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0de8138a-cbec-3677-90a9-db07e8736420 | -8.75842 | -49.92408 | 2025-10-03 05:25:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0c0fde02-da47-36af-84b4-58451c2a647c | -16.93112 | -54.14644 | 2025-10-03 05:25:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e305a73-4005-3d0f-8d87-945cc3b6350f | -14.86014 | -48.36104 | 2025-10-03 05:25:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ee323f72-252c-3d1e-b94d-06468680dacd | -9.16581 | -50.84163 | 2025-10-03 05:25:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9bbd85ac-bb79-3849-8293-ba2b2e2701a6 | -16.63355 | -49.41353 | 2025-10-03 05:25:00 | NOAA-21 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a56ee8d2-0036-351f-b2e2-f1a5f671a9a0 | -14.85787 | -49.31945 | 2025-10-03 05:25:00 | NOAA-21 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b929dce5-47b7-3ee9-89cf-14c98781072d | -14.57876 | -52.46733 | 2025-10-03 05:25:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a6fe9886-7955-375d-aa24-1ac44e116862 | -18.16631 | -53.34857 | 2025-10-03 05:25:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 57c4cc7a-264c-3551-bdef-1c78e2763bcc | -8.55192 | -48.64791 | 2025-10-03 05:25:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 89b96f08-9ba9-3ce9-aa0a-504d83290f45 | -18.20407 | -53.3606 | 2025-10-03 05:25:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63f31add-daa8-3ed4-a2e4-de32451568f9 | -13.80808 | -51.30571 | 2025-10-03 05:25:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30208987-8c3f-3ca9-9e2a-42d964cea281 | -16.18545 | -57.60418 | 2025-10-03 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e5a6a727-bb00-3c2e-9a7f-a31b9bdb9a4d | -14.98699 | -49.96749 | 2025-10-03 05:25:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 42fef66c-92d8-3f54-a252-4cf0c503a8c4 | -16.05553 | -51.04391 | 2025-10-03 05:25:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb07abae-5d1b-3084-b463-aae0618acdf4 | -14.45872 | -48.4104 | 2025-10-03 05:25:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5df6904d-14fe-30db-8877-d6084c75c05d | -8.6143 | -54.96565 | 2025-10-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 370a78ca-0481-34a1-8871-6eb2722ccf05 | -16.05504 | -51.03879 | 2025-10-03 05:25:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3005ce22-f0f8-3572-a155-8e2f42a72abf | -13.68099 | -48.63813 | 2025-10-03 05:25:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d2cc58a8-5410-3adc-a910-3c0293722b6c | -18.34013 | -52.01123 | 2025-10-03 05:25:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 96e6d401-9d2d-3e1b-8f72-8824b8dd0256 | -18.23296 | -53.35218 | 2025-10-03 05:25:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a708fef-d109-3242-b9c1-6aad59d225a5 | -16.06082 | -51.04387 | 2025-10-03 05:25:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3cdd137d-6617-34d2-b310-57a00e05dd90 | -8.10946 | -55.07765 | 2025-10-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README138.md)
