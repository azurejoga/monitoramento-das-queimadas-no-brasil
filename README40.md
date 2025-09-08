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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cfc45d8b-7a77-350f-8450-6c7ef715f0fd | -15.29622 | -46.97876 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a43f53d-9787-3be6-aa32-9a624b7bcf86 | -12.00096 | -47.76713 | 2025-09-08 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 183dd06c-ee5e-3f54-89cb-55f93b2d00b8 | -15.13235 | -48.06219 | 2025-09-08 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3a40e11-b07b-3a6c-ab09-cb24847ccba1 | -9.96137 | -51.20515 | 2025-09-08 04:02:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e009cb68-0e04-3801-a61b-074c06c7498e | -10.28315 | -48.80357 | 2025-09-08 04:02:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7100c00c-600d-3fdd-a492-9139d8866cb8 | -9.18042 | -46.06961 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2cdf065e-1672-385a-b439-c6cb2babeb79 | -14.51959 | -48.75985 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 69aee008-a718-381f-a8bc-65bf2607a9ad | -15.18111 | -47.9647 | 2025-09-08 04:02:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ddc83314-66f7-36de-bd15-d5d7582271f5 | -9.19886 | -46.06146 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1a96f8c-2fde-305d-b568-cf3dd58ba1ef | -11.2783 | -46.45095 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8e506499-91fb-3525-926a-d1596e26741e | -9.39686 | -40.30752 | 2025-09-08 04:02:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| cdba9e31-2be0-3cb2-a358-683abd2ec2d7 | -15.29496 | -43.38282 | 2025-09-08 04:02:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 2e6770bf-b2ae-36fe-b286-cbe942d46113 | -15.13506 | -48.07135 | 2025-09-08 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 699cb7e4-3f67-38d2-924a-4f03d875fbdd | -14.71723 | -45.13906 | 2025-09-08 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9af1daa0-df64-3e87-a84b-63c509e0a9fa | -11.18855 | -55.01072 | 2025-09-08 04:02:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8328fbe7-7fe7-3903-8ff5-d878427711df | -15.1393 | -48.0723 | 2025-09-08 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b0fcd03-9ba7-3620-a074-e18d6d6d6e81 | -11.62368 | -47.14705 | 2025-09-08 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4bd79d6-aedf-3788-809b-a0574e092b8c | -13.90453 | -53.97334 | 2025-09-08 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3bdbe471-6c8a-31a6-ba0a-f6b1b1c42588 | -11.19563 | -55.01191 | 2025-09-08 04:02:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 5618eecf-7d54-3d09-8348-7a6e83dd10c6 | -12.82532 | -52.89443 | 2025-09-08 04:02:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fa660bce-4be9-3da2-84a2-943e929caea8 | -14.09197 | -46.60463 | 2025-09-08 04:02:00 | NOAA-20 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2fc4c187-65c3-3ac9-ba9c-f0a04542a952 | -10.82409 | -47.74176 | 2025-09-08 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 461f2016-4a07-369e-9cb3-75c97c5eca8d | -12.9479 | -54.7741 | 2025-09-08 04:02:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c4ef1507-f964-3259-8d7f-18ffabe07028 | -9.84927 | -48.85137 | 2025-09-08 04:02:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3c0c5036-2c51-3006-aacd-1ee3c5465b67 | -11.14253 | -45.25386 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96e03e30-0901-3658-8d15-f0845f562fca | -12.87578 | -47.98629 | 2025-09-08 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b7b701d6-75de-3e9f-9e2c-9cd8d06f79bd | -13.35273 | -44.43225 | 2025-09-08 04:02:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0fcfdc7d-70a0-33b7-b05c-407cc201ceb2 | -12.82949 | -52.90499 | 2025-09-08 04:02:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c4002929-2b0f-3fd0-844e-faa5a51af54a | -9.14882 | -46.06845 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 849615a5-4002-3f2b-be1f-c16cd8b94a31 | -9.85405 | -48.85309 | 2025-09-08 04:02:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0185edaf-e5be-3acd-8905-187840df4051 | -9.2091 | -46.0514 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c9daeab-7ef5-3abb-82a6-ddb300726a85 | -11.01717 | -45.93155 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e48c4079-9479-35ba-9d4d-5e6e50a40195 | -8.74245 | -46.68649 | 2025-09-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9abac69d-840f-32dd-915b-63087194c637 | -10.80032 | -47.73566 | 2025-09-08 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2273d6d8-ca92-3424-ac7e-e27106fce854 | -12.46416 | -48.03699 | 2025-09-08 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9864fec7-67dd-3f90-b5f6-3c098aaa2ec1 | -9.2028 | -46.03867 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 12a35a00-33a7-3c08-b28d-deedb5ece8a3 | -13.81981 | -46.25474 | 2025-09-08 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e9db23ef-d1ef-3fde-a913-eff328234ec9 | -15.53459 | -49.24014 | 2025-09-08 04:02:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 89da1d2d-8c74-31b3-b146-18b1502d222c | -12.16635 | -43.94032 | 2025-09-08 04:02:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dac5468a-7af6-3dda-bd77-ad269dab3f63 | -11.28043 | -46.46274 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d2bad594-fb98-3316-9557-0c7e06c43dfe | -11.82868 | -46.77362 | 2025-09-08 04:02:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf5431bd-ca70-3136-ba22-6376b201bcbc | -13.82545 | -43.8647 | 2025-09-08 04:02:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5d5ddde2-55d5-3e77-8990-6ecbd6691956 | -11.40702 | -50.36472 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8578159f-da9c-34f7-9838-85a645e3b096 | -14.51877 | -48.75735 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c468d55a-ccef-31c7-b398-9fa8557c916e | -14.99809 | -48.00986 | 2025-09-08 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c42bb11e-4fc8-3bdd-b438-6ef44c048b2c | -10.9612 | -46.81592 | 2025-09-08 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cedbb957-eaf8-39d8-9b53-212eed877f6a | -12.82893 | -52.93916 | 2025-09-08 04:02:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 09a384fe-b188-3f0d-9f03-95fefb17c121 | -11.66147 | -46.88571 | 2025-09-08 04:02:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a1371648-6d1a-3a36-9a19-8ce14803aaa2 | -14.65318 | -46.84233 | 2025-09-08 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 654b98f4-3baa-3621-9c3f-3b5a8e2bfb12 | -15.34768 | -49.12833 | 2025-09-08 04:02:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a874f08-aabc-38c8-9811-5a32fa8bd552 | -9.32586 | -46.52998 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 527d171f-08ad-3286-b15a-dfc67f3b61ee | -10.14384 | -46.20056 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1a318bdb-a4b3-3f25-9e13-63f707901310 | -11.31848 | -47.33323 | 2025-09-08 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ebd7de4-1c24-3ad4-b255-0d5507d73406 | -7.73751 | -50.31219 | 2025-09-08 04:02:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a8c0508-4515-3a4a-9ecc-aaa127b1a2bb | -15.17687 | -47.96399 | 2025-09-08 04:02:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ad84461-2464-3810-822d-2578b67e3f44 | -11.40263 | -50.38827 | 2025-09-08 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1e370a45-388f-3ee6-be7e-95886fc4b35f | -15.13583 | -48.06721 | 2025-09-08 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c3a27ac7-3a54-3031-96ce-eede51c5427e | -14.32581 | -44.9245 | 2025-09-08 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f83db2d-012e-3a54-935e-cd62cc4f2b00 | -15.19028 | -47.96242 | 2025-09-08 04:02:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 42bb7be4-43ba-3064-a2ce-f15d7323b74b | -11.76482 | -47.75017 | 2025-09-08 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6e66b0af-d3e9-314f-8194-7db57e7eee4b | -15.53371 | -49.24487 | 2025-09-08 04:02:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4ef0177-992e-3c39-bd94-1e89cca3fcbc | -10.7959 | -47.73439 | 2025-09-08 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 42141e7b-073d-3a96-b513-99f503cc5f48 | -12.81398 | -47.99972 | 2025-09-08 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f032989-31b1-36b6-86c8-2bbc07bc23ad | -9.8265 | -47.77769 | 2025-09-08 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4303b60c-c85d-3852-9711-b05125c72f59 | -13.81124 | -46.28035 | 2025-09-08 04:02:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa7560ab-d3fe-3f41-838c-b39cb6d4f154 | -12.19409 | -53.91365 | 2025-09-08 04:02:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 39f48d84-70e5-3047-9896-36f360be2ea5 | -14.51499 | -48.78378 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| edd20fc5-1213-3dc7-af0a-e5223b72933b | -9.07992 | -46.97868 | 2025-09-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c9f91b0b-8dc9-3077-bfda-36ef882424f9 | -15.53395 | -49.24205 | 2025-09-08 04:02:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5002de2d-5603-3e61-9182-13c9eccc1d48 | -11.38775 | -43.54089 | 2025-09-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31163c21-7ad2-3282-9741-ecf6b078dfb0 | -13.73312 | -46.90179 | 2025-09-08 04:02:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57321e97-cbf5-3f00-9a15-59d70a27dc6c | -14.51948 | -48.78473 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27e624d7-2073-36f0-9b7e-48bb20d37ef8 | -9.96051 | -51.2098 | 2025-09-08 04:02:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| deafa528-6ac3-34ce-b6be-ab06832e4052 | -9.85277 | -48.84045 | 2025-09-08 04:02:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2b6f8432-365f-3b81-8bab-549fd2fe4913 | -13.03204 | -47.12515 | 2025-09-08 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a24468a-4c36-381d-a6ad-0463341c97a2 | -13.70506 | -46.87186 | 2025-09-08 04:02:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 5760cf7e-8d8f-3c1c-a8f8-cd3903b5b231 | -11.02362 | -45.93048 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86d4a700-3fbf-3749-a70b-0c4f30f8cb63 | -13.54671 | -48.10688 | 2025-09-08 04:02:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e57f572a-2459-3ca9-846c-e81628fe975e | -12.82966 | -47.99321 | 2025-09-08 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dfba70c7-dacd-3922-bacb-a948b2ec6259 | -15.09132 | -48.13967 | 2025-09-08 04:02:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0592ae17-0cc5-30f0-a444-0c585a1f96bb | -10.33013 | -46.35338 | 2025-09-08 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87a4a668-3d13-3c51-bbf0-c1788b17edeb | -14.81194 | -48.17373 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b63f36c-4890-37be-b39b-4ac5d5bada8a | -14.49994 | -48.80863 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bb5aab99-42f5-3246-b5b8-58cc51d05b00 | -10.15768 | -46.21832 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c515e427-799c-31a6-a158-ddea9c395932 | -12.49258 | -48.09642 | 2025-09-08 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df11019a-73e7-3810-bff4-dbb02298cedf | -14.51884 | -48.78231 | 2025-09-08 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06054d11-9fc5-3dd8-815b-0ca1d1146e8c | -11.83084 | -46.76123 | 2025-09-08 04:02:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c9825a9-d2a2-38e7-9293-fd0e7e9f6b69 | -10.28623 | -48.81408 | 2025-09-08 04:02:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 794d1a25-7ef5-3089-abad-d599d332ccf8 | -11.76403 | -47.75459 | 2025-09-08 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 938c855c-d04a-3241-aaff-c7bad8916732 | -9.85054 | -48.85246 | 2025-09-08 04:02:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 638fd90b-3e10-385d-a8ae-2a47e796af0a | -11.15102 | -45.25022 | 2025-09-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fff43969-2916-310e-9759-e632ba100edb | -9.83302 | -47.79387 | 2025-09-08 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 508029cf-b72d-356d-b5f9-195f66726a97 | -15.18606 | -47.96156 | 2025-09-08 04:02:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f9a179e0-a3a9-3022-9352-8e6dd8415923 | -10.1167 | -46.02066 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61e1ea7c-acaa-3304-a2de-9f27675cbe18 | -11.4249 | -43.64802 | 2025-09-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| f3859736-9749-3618-b445-494795b4e294 | -10.13909 | -46.20355 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0c5f942e-f525-3234-90f3-c0d433a53240 | -9.14259 | -46.06662 | 2025-09-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a0801f11-a5b0-32e2-b1ea-43206fcd68e9 | -13.81812 | -46.28688 | 2025-09-08 04:02:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dd5d455c-a67b-3370-bbfa-5b5954d143ce | -10.81957 | -47.74108 | 2025-09-08 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41377ccf-1920-3ea1-81b7-900670daf668 | -8.69845 | -45.32319 | 2025-09-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README41.md)
