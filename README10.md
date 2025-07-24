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
| 6b08e9cd-e443-3dfd-924d-8cdb31da6df5 | -3.36018 | -47.16252 | 2025-07-24 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 492cc35a-bd93-3aa5-96cf-0f2b46701593 | -5.68007 | -43.67214 | 2025-07-24 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdeb6292-5f96-3756-9a26-48697bc1237d | -6.64394 | -43.05669 | 2025-07-24 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbe3f0e5-6708-31df-ba50-f906431aea06 | -9.59791 | -43.87017 | 2025-07-24 04:14:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| abc7956f-c037-335b-85d8-a5346cfbef91 | -5.14259 | -45.17131 | 2025-07-24 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b499a80f-0d70-36b1-ad15-0fe0d0602d3e | -6.89216 | -44.20429 | 2025-07-24 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 64db09e3-3590-3618-bc7b-9b96a0041409 | -7.11132 | -43.32854 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d9aaa3b0-a8ea-3f08-b46e-29413b53f2bd | -4.10362 | -48.20465 | 2025-07-24 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f2f0a30-fcb9-3684-8bef-040d6c5d127c | -3.0429 | -47.38203 | 2025-07-24 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 44d6fa18-9151-3006-bb7d-4a134622281c | -2.65943 | -47.39814 | 2025-07-24 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1e5761ea-e618-3f1b-9a78-39f2907f19c7 | -5.48577 | -42.14907 | 2025-07-24 04:14:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 30938944-24c3-36e4-86f9-f3149996dc05 | -5.13975 | -45.16695 | 2025-07-24 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 606f92e0-749e-3390-a507-42f6e0edaacf | -7.10802 | -43.32803 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 05637c6c-277d-301c-83ce-e651254aea60 | -7.24519 | -43.08072 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| bf0837de-1c20-3639-8fcf-456ea5df17a3 | -7.46035 | -49.40508 | 2025-07-24 04:14:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 930f72f5-5a1f-3432-8dae-03d176fd206c | -8.48322 | -49.55011 | 2025-07-24 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7949183b-9536-3703-8891-02d124c8130d | -4.05215 | -42.51105 | 2025-07-24 04:14:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 75159c54-0b75-3d1f-98f9-297f02fb2f61 | -6.53768 | -44.65912 | 2025-07-24 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24bb4278-5fda-32af-9db5-33d7abe41a50 | -7.24958 | -43.0743 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 796e4382-de99-32ac-9d83-e4a07df9d71f | -8.52173 | -44.67808 | 2025-07-24 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d3b54c2a-3ff4-338e-ad12-287ba2f473d9 | -4.06099 | -42.51947 | 2025-07-24 04:14:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 98ebdb75-21d4-371c-98ac-509fbbd103c5 | -7.5458 | -44.45989 | 2025-07-24 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc7df073-b2cb-3e51-bd12-297a5c9cb6d7 | -2.58484 | -51.92452 | 2025-07-24 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91fc1155-93bc-3165-a6ea-58b0008bcfda | -7.9202 | -43.09101 | 2025-07-24 04:14:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 95f2cbb7-159e-3e3c-9a9b-cac9c2ab4a75 | -3.64981 | -48.32468 | 2025-07-24 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8082de30-1f74-33eb-a006-1d0a07e15e8f | -9.48733 | -40.38365 | 2025-07-24 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4b5f27fc-fb83-3e8b-9859-a38a6d72704f | -5.31855 | -45.23306 | 2025-07-24 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea10dc58-182b-3083-bf90-a1e55419c68b | -6.63471 | -43.09421 | 2025-07-24 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d70f5f3f-a585-3b91-ba86-9439e463e4e6 | -6.49837 | -43.50793 | 2025-07-24 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 255e2676-a4bc-339a-b8b2-5f3adc47b7c1 | -3.47475 | -42.85307 | 2025-07-24 04:14:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0432aee8-4bb5-3938-af0a-c5a21059572a | -8.3012 | -44.97067 | 2025-07-24 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d6c73a8d-8593-3132-b841-b84696da7cca | -7.73344 | -43.939 | 2025-07-24 04:14:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34e78976-56fd-344d-b947-317b261aeeee | -6.82995 | -43.06088 | 2025-07-24 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fea79784-3e34-353f-afae-aa13e1565787 | -4.04777 | -42.51742 | 2025-07-24 04:14:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a8487308-6cc6-3089-b789-0727371276a9 | -6.96753 | -44.37161 | 2025-07-24 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32c28d3e-d051-3082-82ac-27fb674d6ba7 | -6.26143 | -45.26829 | 2025-07-24 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc4dd658-15d7-32e4-8149-f790dae300cc | -5.9353 | -44.71939 | 2025-07-24 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d574f503-5679-33ba-96ef-0d5e203cdcdc | -8.03449 | -47.65303 | 2025-07-24 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2c56d44-e95c-3438-a621-e21a3842a9b4 | -6.93981 | -44.31262 | 2025-07-24 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 213c5e34-1200-340f-bacb-f2bfdc478805 | -4.17982 | -48.74025 | 2025-07-24 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c861717-8ec9-3397-bd70-f3142891911f | -10.62764 | -49.4538 | 2025-07-24 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a9f95b6-bf07-34ef-b8c0-64655750df72 | -13.70809 | -45.67558 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f97f52c-da6d-3e3c-8cd7-8b408572752e | -14.09712 | -46.34512 | 2025-07-24 04:17:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13761a9e-7ace-3ca2-944b-6a9ba30f7c3c | -11.99434 | -45.15556 | 2025-07-24 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82a0eb97-6491-3d94-9e37-d3f4adc635e7 | -13.70307 | -45.68573 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4dcd2b24-8945-3c41-b7fe-2ab660e39d74 | -10.71506 | -48.85613 | 2025-07-24 04:17:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c81be846-d181-37b7-9e7c-bc355346bc88 | -11.13047 | -48.63945 | 2025-07-24 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73b5cb0b-383f-3bd1-abb6-91b2bc70dbde | -15.28302 | -47.13054 | 2025-07-24 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eef67d8d-c83f-3280-9f02-990e6e90bfcb | -22.25704 | -49.57728 | 2025-07-24 04:17:00 | NOAA-21 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d3908612-4ee8-3b17-b58d-92e50e5afc58 | -14.16874 | -45.34388 | 2025-07-24 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5af44861-ad50-3879-941b-5400ce7db727 | -21.31421 | -48.56596 | 2025-07-24 04:17:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e86d83db-db78-3162-9202-7c1524f958bd | -20.40325 | -54.63214 | 2025-07-24 04:17:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd0da768-f284-3f24-b7bc-c7ac16de0c61 | -23.02614 | -46.72638 | 2025-07-24 04:17:00 | NOAA-21 | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 94099681-f971-3196-ab22-a6d60b174501 | -12.11064 | -43.75563 | 2025-07-24 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e5df82e-a84a-392c-9d8c-7aa3b337ac7b | -21.76727 | -52.75672 | 2025-07-24 04:17:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0bb92ff-e8be-3b94-abf6-64be090d28ec | -15.28703 | -47.12744 | 2025-07-24 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| caeb1ef8-9182-30fa-abd6-3dbdc4a21262 | -20.04466 | -45.65253 | 2025-07-24 04:17:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8da230e4-a5fc-3f5d-9452-0bb785db385d | -10.66884 | -47.78749 | 2025-07-24 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f467bc5f-8faf-3902-8f8f-ef01b35ebb71 | -23.48294 | -47.02718 | 2025-07-24 04:17:00 | NOAA-21 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ebe87e7c-23e1-3363-bd13-25e30508c1ec | -13.21725 | -51.08219 | 2025-07-24 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 927ba593-b2e1-395f-ba32-1cfa9d40359b | -12.42717 | -45.38655 | 2025-07-24 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7199453f-9116-33e5-af87-6690593f4714 | -11.73594 | -48.18768 | 2025-07-24 04:17:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fe349d33-659c-3a17-ba43-7328795a144c | -14.18085 | -45.35316 | 2025-07-24 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38d4548a-91cf-37f8-b3b4-4d32af3a53cf | -11.46151 | -48.16161 | 2025-07-24 04:17:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b34d4d89-b6b6-3212-b57d-c2e2fd9a874f | -10.66021 | -47.25856 | 2025-07-24 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 464e0e24-c8a4-3e82-9861-61dd9da2b025 | -10.3624 | -48.237 | 2025-07-24 04:17:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0f80804-4575-32fb-b83d-f6d3cde7967e | -22.81429 | -47.17364 | 2025-07-24 04:17:00 | NOAA-21 | SUMARÉ | SÃO PAULO | Brasil | 3552403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 87f40efc-d9d0-34d6-876a-15169eac52eb | -20.96051 | -43.9691 | 2025-07-24 04:17:00 | NOAA-21 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5f63f0be-ef1b-3372-8a36-bc71b3e14815 | -12.71042 | -47.79505 | 2025-07-24 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7239ec8-8fa3-3047-949c-88f7b703af1d | -12.25725 | -44.78341 | 2025-07-24 04:17:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2b7ca9b0-9b41-30c2-8f3b-cdaddcff1ffa | -15.75969 | -43.3727 | 2025-07-24 04:17:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e4711d1-91ae-3bab-9055-5346fd4b1f3a | -17.84465 | -42.64063 | 2025-07-24 04:17:00 | NOAA-21 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9f53ca5e-c39c-3070-af23-48177127bebf | -15.82466 | -45.77736 | 2025-07-24 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| caa331af-aa1d-37f1-8488-1315a9e6c108 | -14.10107 | -46.34202 | 2025-07-24 04:17:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d2d4d9f-31a6-3408-9726-006bc31910ef | -14.74286 | -46.30794 | 2025-07-24 04:17:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 82df6898-dde7-36a5-b3ff-2a091fa6f31c | -10.42655 | -44.18171 | 2025-07-24 04:17:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50a5420c-d32a-3388-8259-9323890bc8b7 | -10.62401 | -45.23704 | 2025-07-24 04:17:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 740319c6-28d1-3ac4-a446-be7d0fc8095a | -13.70582 | -45.68986 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c9690915-ee0d-3758-a865-e138355aa64d | -14.37373 | -50.32648 | 2025-07-24 04:17:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 07ab601d-31e6-372b-8098-bfcb3688122c | -23.36804 | -47.17602 | 2025-07-24 04:17:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 80ae30db-7f0d-301e-9668-6928dd05e155 | -23.00837 | -47.38854 | 2025-07-24 04:17:00 | NOAA-21 | ELIAS FAUSTO | SÃO PAULO | Brasil | 3514908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cd198abe-da39-36e7-adb3-6fe2aa8f105a | -19.36716 | -52.03917 | 2025-07-24 04:17:00 | NOAA-21 | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b40d68f9-1c7c-3b4e-b76a-7be11c200c6b | -20.2949 | -54.07991 | 2025-07-24 04:17:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 52eea6fc-4cb3-32eb-bb1b-4e4d7b093824 | -13.70088 | -45.67804 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4548a46c-d238-3850-9a47-10646b215069 | -10.96667 | -49.57418 | 2025-07-24 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef066643-4855-3cb9-b468-70dd382ddb0b | -10.05024 | -48.66235 | 2025-07-24 04:17:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3facff17-1f4a-323c-81ea-86bdbaa327b1 | -10.62458 | -45.23348 | 2025-07-24 04:17:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a3a118b4-45e2-37b4-8471-be8bbeb6f5f9 | -23.06989 | -49.68994 | 2025-07-24 04:17:00 | NOAA-21 | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d871752a-4f68-3e59-95d2-d6ea27421c37 | -13.6464 | -45.72035 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5e54a6a-3aa5-31b2-9fbc-10dd60fc6523 | -9.34569 | -49.91741 | 2025-07-24 04:17:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb8c9754-252e-3321-857a-8ad7db406dbc | -13.70639 | -45.68628 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 72ca267e-8b39-3107-a667-aab94825d768 | -13.68557 | -47.73763 | 2025-07-24 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8ee7dab-c118-3e17-ae0d-9cd16ea3c66c | -14.21036 | -43.95058 | 2025-07-24 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b51bfe5-3380-3e73-ace9-cc7cfc366bb3 | -12.42497 | -45.3789 | 2025-07-24 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2831c147-415f-3b36-bd93-0dcc6cffe77e | -10.63181 | -45.23101 | 2025-07-24 04:17:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0ac29f33-0ce0-3115-947e-1c0c57efe15e | -11.81334 | -44.27218 | 2025-07-24 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b35b8a0-8963-3e30-8102-2fc70191e0f2 | -13.09522 | -52.14534 | 2025-07-24 04:17:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5473c707-f3b1-38b4-8146-1d0d91cffd42 | -13.64915 | -45.72448 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f649ba7b-e45b-3d39-ac72-4dbadf0b2cea | -13.71028 | -45.68326 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bce4500-e7c0-3ee8-8fa0-4805e1bb70c0 | -10.17983 | -50.22205 | 2025-07-24 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README11.md)
