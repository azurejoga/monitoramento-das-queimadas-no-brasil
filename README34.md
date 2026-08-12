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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84747086-2ade-3115-bba5-30406aa2de00 | -6.89069 | -41.93324 | 2026-08-12 06:14:00 | AQUA_M-M | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 0d2c8bd7-48cf-3af4-bad7-49c7e3b549b0 | -6.33651 | -44.05787 | 2026-08-12 06:14:00 | AQUA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 5f21d7b4-739b-321c-95d4-186f1f8cf39c | -6.55188 | -43.11757 | 2026-08-12 06:14:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 353f15d8-fb0d-3a6e-a308-dc15388a0520 | -7.01811 | -42.13126 | 2026-08-12 06:14:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 46b2e426-9e99-3607-b068-45827537b0f0 | -6.54105 | -43.12615 | 2026-08-12 06:14:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| b32fb2de-31fa-3920-8e7e-a51c2502c8ae | -7.027 | -42.1326 | 2026-08-12 06:14:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 2fe90221-6cd8-325f-b592-562ca2f05003 | -6.54258 | -43.11615 | 2026-08-12 06:14:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 36.1 |
| e9489002-1cfd-3c14-959b-d38804d52691 | -7.02561 | -42.14165 | 2026-08-12 06:14:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 938d646d-8053-3188-80c5-1124bb8288bc | -10.21908 | -45.92534 | 2026-08-12 06:16:00 | AQUA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| b6691f8b-09e0-3bcf-b313-cdbc180f8df3 | -11.98678 | -46.35998 | 2026-08-12 06:16:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 66deda30-9981-3244-9f47-3ea92e512b83 | -14.98141 | -46.59507 | 2026-08-12 06:16:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 90194c83-4dcb-32e3-b0b6-57aed5b8fe9f | -11.94114 | -46.33482 | 2026-08-12 06:16:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 76086bf9-8ce1-3e16-8d47-2a44bd9be43f | -11.94513 | -46.37696 | 2026-08-12 06:16:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 1a94a671-f884-3920-86ef-a0fa591e719c | -11.94293 | -46.39043 | 2026-08-12 06:16:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 0d4b6ecf-1062-3a6e-a8e5-143999855f6a | -11.98191 | -46.38897 | 2026-08-12 06:16:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 6a5004bf-0b24-382b-813d-eae5d7fb3cc4 | -11.46865 | -44.55606 | 2026-08-12 06:16:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e106e11a-4432-3f8b-a8f9-f0d920da291f | -13.54358 | -46.26969 | 2026-08-12 06:16:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 960e8eee-5133-3853-92c3-ab331aec1fa9 | -11.94351 | -46.32031 | 2026-08-12 06:16:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 35fba8fb-43d1-36b6-b862-c2bcd7af55cb | -8.35021 | -45.9739 | 2026-08-12 06:16:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 658235f3-ea56-3e5d-9e51-50ad29694985 | -9.13652 | -46.38511 | 2026-08-12 06:16:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| fff0130f-6cb0-3e7e-8e82-7591173cb6ba | -13.54548 | -46.27613 | 2026-08-12 06:16:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0a0c8b5a-9f39-3456-a1ae-a017a3adf57d | -11.98427 | -46.37493 | 2026-08-12 06:16:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| f3eee7ac-36ff-3d4a-9d37-7c4c1a1e87c9 | -11.97964 | -46.4025 | 2026-08-12 06:16:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 020456b4-e906-3abd-96a7-38a2adc9a2e8 | -11.95189 | -46.33552 | 2026-08-12 06:16:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 22f6d0e2-03c8-3321-88b6-e95f860087d8 | -11.95004 | -46.38372 | 2026-08-12 06:16:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 88f5a199-5df8-33ed-ab32-c563d2d2cfc1 | -11.47644 | -44.56808 | 2026-08-12 06:16:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 856d1396-21ba-3126-b4b8-a41aee2ff8b4 | -8.96 | -60.5358 | 2026-08-12 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 1fc56398-6ef7-3d7a-8692-444015a746dd | 4.84563 | -60.19035 | 2026-08-12 06:29:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0f35695-479c-3ae3-a090-e37ce1adaebd | 4.83896 | -60.19049 | 2026-08-12 06:29:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9b35c06-13d5-3de2-adce-e89f1cb5ef58 | 4.83986 | -60.19548 | 2026-08-12 06:29:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0de26b63-cd4c-3002-98e5-82736ef095f4 | -15.3023 | -48.8595 | 2026-08-12 06:30:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 90a6a0c5-dcae-3cb0-a299-56e77adbdbd8 | -15.3019 | -48.8818 | 2026-08-12 06:30:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| bbe25a8d-c73e-357b-8984-39a04c4eeb48 | -11.164 | -50.5299 | 2026-08-12 06:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 88a09cd7-0db5-3e29-83f1-a2355a1f9d8d | -11.164 | -50.5299 | 2026-08-12 07:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| b1ffd3e9-7ea9-3e6c-a202-11d7e0bdd897 | -11.164 | -50.5299 | 2026-08-12 07:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| acb01dff-1d9e-3b66-a152-a50d06039eba | -8.96 | -60.5358 | 2026-08-12 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 0988e9fb-eb1f-3771-8690-763f3371d5e5 | -15.3023 | -48.8595 | 2026-08-12 07:40:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 525acc43-3f34-3910-90e1-f059d27c86b7 | -15.3019 | -48.8818 | 2026-08-12 07:40:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 48.0 |
| b4fe503f-df8e-3093-aebf-ba9a968fb92c | -13.8797 | -53.824 | 2026-08-12 07:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| a1d20ead-376e-33f2-bb54-9f83b2f299da | -13.8989 | -53.8217 | 2026-08-12 07:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| cec355ab-59c7-332d-8005-fc1177168463 | -8.95388 | -60.54176 | 2026-08-12 07:54:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 3c732e47-398d-3653-98a4-4d1b3a2281d2 | -8.95161 | -60.55875 | 2026-08-12 07:54:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| ef31abf3-a772-3bff-b0b4-bbfff13a768e | -8.95614 | -60.52487 | 2026-08-12 07:54:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 453cf06f-2362-3680-a919-7185c96215b6 | -7.41294 | -59.99562 | 2026-08-12 07:54:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 7f55155b-9e7e-329d-94b3-565d19fda2c1 | -13.8797 | -53.824 | 2026-08-12 08:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 4b72ab08-efda-3f0e-9a02-a4ec43042c9a | -11.9911 | -46.3844 | 2026-08-12 08:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| c2327111-882e-3649-9414-1e63ecc872ef | -11.9911 | -46.3844 | 2026-08-12 08:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 88cc79cb-8726-3339-8ed6-f98ff3cb2934 | -11.8285 | -51.8359 | 2026-08-12 09:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 4e12a403-76e7-3a8b-8857-aebd7402685e | -11.9911 | -46.3844 | 2026-08-12 10:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| be3c0230-ae39-346e-bb9f-6ed5a12a70f0 | -6.5443 | -43.1078 | 2026-08-12 11:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 08890a34-7e29-3f42-8875-21b2230437a2 | -6.544 | -43.1313 | 2026-08-12 11:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| e2a8b5d3-b795-3a96-8dde-b4c3c2429d91 | -6.544 | -43.1313 | 2026-08-12 11:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 1a10e7bd-376e-3650-819b-6cf8a0dfa17a | -6.5443 | -43.1078 | 2026-08-12 11:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 104.9 |
| ea132b71-db30-3e12-833b-e6bbdd5c1bb6 | -2.94466 | -40.49273 | 2026-08-12 11:15:00 | TERRA_M-M | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| eaaf8e64-0c7a-3765-a447-1520a76dc51b | -5.77846 | -45.06493 | 2026-08-12 11:17:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| ef57a66a-44bd-32fe-98cf-4b24cc50ccb1 | -6.54819 | -43.11121 | 2026-08-12 11:17:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 8e2b6c53-0322-3ac5-bf4c-0dd25f001209 | -10.10297 | -46.21599 | 2026-08-12 11:17:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| ba6d06ab-58af-38cc-b2be-0eb3974de832 | -10.21689 | -45.92216 | 2026-08-12 11:17:00 | TERRA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 1437658f-1cc5-3709-8196-932b5cbaefc2 | -11.00549 | -39.26808 | 2026-08-12 11:17:00 | TERRA_M-M | ARACI | BAHIA | Brasil | 2902104 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| b2a45fbd-b39f-31d2-a9f2-f13ca231d854 | -7.03053 | -42.1317 | 2026-08-12 11:17:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| f1e0b372-e44a-3fdb-9a3b-e7f4142cc8f1 | -6.54634 | -43.12382 | 2026-08-12 11:17:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 183.4 |
| bd953af3-336b-369d-aad6-1523cc3a45f2 | -10.21979 | -45.90406 | 2026-08-12 11:17:00 | TERRA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| a8bdc530-2b77-3126-953e-ff7de78a6490 | -7.31547 | -35.13569 | 2026-08-12 11:17:00 | TERRA_M-M | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 27734723-038f-391d-90f0-18319b98c8d4 | -6.28238 | -38.24803 | 2026-08-12 11:17:00 | TERRA_M-M | MARCELINO VIEIRA | RIO GRANDE DO NORTE | Brasil | 2407302 | 24 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 45ee9ad9-3c9c-321c-8bd5-3c901b4de482 | -6.55435 | -43.11832 | 2026-08-12 11:17:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 290.3 |
| 4a397d86-6494-347b-a115-06b894c5c376 | -6.89298 | -41.94655 | 2026-08-12 11:17:00 | TERRA_M-M | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| c5fea8ea-7178-396c-9e1c-c3c2ead41874 | -9.3378 | -47.49382 | 2026-08-12 11:17:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 46bf2b0a-5417-35e8-b2a4-53985438a242 | -6.99755 | -42.63218 | 2026-08-12 11:17:00 | TERRA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 1c4151de-e721-3ad4-9aef-3e2cf93310ab | -9.3692 | -47.44233 | 2026-08-12 11:17:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| e7c51369-939f-3064-bc55-e78100fbb9b6 | -7.31362 | -35.14921 | 2026-08-12 11:17:00 | TERRA_M-M | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 3b7a5e95-b7ed-3bb4-b5ba-41e46f677869 | -9.34335 | -47.51368 | 2026-08-12 11:17:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| e07ce9a0-605f-3d78-bc91-24f1d4bc7800 | -10.36657 | -46.37654 | 2026-08-12 11:17:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 578744c6-4d74-3d8a-8cfd-8138500b4e44 | -7.92664 | -45.10964 | 2026-08-12 11:17:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 1aaa66d4-ffc8-3855-95a3-99b05c03b4f5 | -9.34732 | -47.48911 | 2026-08-12 11:17:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 38.3 |
| ab39e1b6-064f-3164-8262-a3691007f661 | -6.55242 | -43.13091 | 2026-08-12 11:17:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| d20e9865-8aa8-30af-bd51-e46273a49986 | -11.95208 | -46.3547 | 2026-08-12 11:19:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 2810c5a2-e682-39c8-b1c0-873abcb707fb | -11.88979 | -45.83438 | 2026-08-12 11:19:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 59e5d0c0-cc91-370a-b0d2-25046e4568fc | -15.79383 | -43.78797 | 2026-08-12 11:19:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 0ca63f25-a703-3090-9e04-5f781def4853 | -20.90306 | -44.90764 | 2026-08-12 11:19:00 | TERRA_M-M | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| b45f71ce-192e-3fa1-b718-d8b47177fc1e | -11.94854 | -46.34795 | 2026-08-12 11:19:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| a98bde06-0c72-334c-ab0b-b7416919110c | -11.943 | -46.33424 | 2026-08-12 11:19:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 97c2b6fb-4539-3368-b0fc-fcd912a9b49d | -14.29798 | -45.27128 | 2026-08-12 11:19:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| ccd10747-d737-396f-acac-ae1f0652756f | -12.48236 | -44.49874 | 2026-08-12 11:19:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 585f5659-edaf-35fc-b57a-31bf8162fdfe | -15.29684 | -48.87138 | 2026-08-12 11:19:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 2bdada33-c5ce-3bd5-9a9b-1f7ad7e6626f | -13.54707 | -46.26871 | 2026-08-12 11:19:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 19.3 |
| fc01e648-3ab2-30e2-bd5e-5c6ad1055c8f | -11.98271 | -46.39685 | 2026-08-12 11:19:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 376dcaf1-225b-3b99-bb8b-a3bd3a8b96d0 | -11.95547 | -46.33439 | 2026-08-12 11:19:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 63641781-f37f-3fa3-be3c-52f361b7b5c8 | -11.95175 | -46.32769 | 2026-08-12 11:19:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 2fd10fb0-1f01-357d-b3f4-05631e3dd8fa | -14.29577 | -45.28512 | 2026-08-12 11:19:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 8d6e87ef-0ea1-3591-ab9d-344d3941bad7 | -20.91252 | -44.90926 | 2026-08-12 11:19:00 | TERRA_M-M | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 8bf76c37-19ab-362a-bbe2-5f08b6daa553 | -15.79217 | -43.79866 | 2026-08-12 11:19:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 5.7 |
| ce272b7f-90be-3697-8b10-bed72bd64a63 | -11.98581 | -46.37784 | 2026-08-12 11:19:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 05281467-37be-34d0-8ec3-34cafab57cd2 | -6.5443 | -43.1078 | 2026-08-12 11:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 157.2 |
| e67e5fab-6126-3b91-bfcd-dd5b81b6a6e1 | -6.544 | -43.1313 | 2026-08-12 11:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 2b1ea14f-08df-32ba-a33b-207460b00a0e | -11.8859 | -45.831 | 2026-08-12 11:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 9897b66f-0074-37f3-8240-39db8de8c47a | -6.544 | -43.1313 | 2026-08-12 11:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| d25f2922-eb3d-37a5-a14a-683755959ac3 | -6.5443 | -43.1078 | 2026-08-12 11:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 956baad2-ace8-3051-b3c6-2b1b5e2c0f94 | -11.9535 | -46.3444 | 2026-08-12 11:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| a90829f5-6da5-3f7f-8b69-8406f096bfd0 | -11.9911 | -46.3844 | 2026-08-12 11:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 84fdeadf-35f9-3641-8815-f0fd1735b162 | -11.8859 | -45.831 | 2026-08-12 11:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 199.2 |


[Clique aqui para ver as próximas entradas](README35.md)
