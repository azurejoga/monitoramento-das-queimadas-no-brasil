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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 277ec999-9aff-35cf-990a-db870a4efa51 | -5.4565 | -43.0554 | 2025-09-27 03:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 3da370b1-d051-3227-a388-78304576713f | -5.5056 | -43.866 | 2025-09-27 03:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 52f8f65c-0e7c-31d0-8984-6345fceaf3da | -22.6009 | -48.5698 | 2025-09-27 03:30:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 55.4 |
| 4323a407-50fd-3a04-9c7a-eec265aacd58 | -15.2325 | -49.4243 | 2025-09-27 03:30:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 7361d5f6-a474-3809-97a1-6da849b8bdd1 | -12.3157 | -44.3564 | 2025-09-27 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 4b14d4df-625e-3d26-b074-fb6129ac0f7e | -15.2329 | -49.4021 | 2025-09-27 03:30:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 848bb737-f84c-375f-9b2f-e76baa5c41fb | -5.4562 | -43.0788 | 2025-09-27 03:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 32050df1-0dad-379c-85f2-f54c4df5251a | -5.494 | -43.0526 | 2025-09-27 03:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| eba6e12c-5ce4-3847-acf6-6b9b878db6ac | -5.4752 | -43.054 | 2025-09-27 03:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 5640124a-ad6a-3680-805d-7a86038edde3 | -15.213 | -49.4273 | 2025-09-27 03:30:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 0e7c8201-ae36-3a74-b396-9f2b47481657 | -5.475 | -43.0774 | 2025-09-27 03:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 389.5 |
| 75bbd129-76c4-3d8a-8c3d-f8d469668942 | -5.5241 | -43.8878 | 2025-09-27 03:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 7c11f49d-3144-3d88-88ac-f194615cfdb6 | -5.4937 | -43.0761 | 2025-09-27 03:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 181.9 |
| abd04830-c70b-33b5-bb44-c4a09a40ec1e | -12.3157 | -44.3564 | 2025-09-27 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 9af57ef8-13ae-37f7-9ee0-8f9f29384421 | -22.6009 | -48.5698 | 2025-09-27 03:40:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 58.7 |
| 6ff45139-52b8-331c-92c0-afd2f42c229d | -5.4562 | -43.0788 | 2025-09-27 03:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| d04c859c-977a-371f-bc4a-c60224acd7ac | -5.5241 | -43.8878 | 2025-09-27 03:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| d532c937-6881-332d-8dd6-e5b64c1ad91a | -5.475 | -43.0774 | 2025-09-27 03:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 293.9 |
| 2dae1c0d-1d48-358b-ae61-a13c334d04c3 | -5.5243 | -43.8647 | 2025-09-27 03:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 24190399-d9a3-3d0c-9108-6e4e41246f22 | -5.4748 | -43.1009 | 2025-09-27 03:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 5622b990-41de-3df1-b2d6-f317d3e3870e | -5.4935 | -43.0995 | 2025-09-27 03:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| af031eb5-870c-3a4a-97a7-ba63223486d9 | -5.494 | -43.0526 | 2025-09-27 03:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 2bc39514-cfb2-371d-b544-eb42d035b2eb | -22.5792 | -48.5986 | 2025-09-27 03:40:00 | GOES-19 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.7 |
| de0f832d-1c7a-3a15-9118-2e6f1d989b84 | -22.6001 | -48.5934 | 2025-09-27 03:40:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 64.9 |
| 12457933-cec1-3af5-8cff-18e6d33c9404 | -5.4752 | -43.054 | 2025-09-27 03:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| e07c7ef3-0538-3894-97cd-84d36eb45387 | -22.6009 | -48.5698 | 2025-09-27 03:50:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 53.9 |
| 4694c856-5392-3f6d-8b9e-258f07979e17 | -22.6001 | -48.5934 | 2025-09-27 03:50:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 57.5 |
| ad80bec1-1dcc-30a5-a728-931387be7f66 | -5.0862 | -44.857 | 2025-09-27 03:50:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| c1b0db39-1b6a-36c4-b721-5596829e6765 | -9.9328 | -59.9247 | 2025-09-27 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 13b1aa7e-d074-34d3-85b2-0c2c334d4c50 | -22.5792 | -48.5986 | 2025-09-27 03:50:00 | GOES-19 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 79.5 |
| c8745267-4ccf-3d64-8a03-4ee6d20c9e1b | -2.96153 | -48.59496 | 2025-09-27 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b41d7752-0cf1-3391-b685-0abaaa54b2e0 | -6.33756 | -43.35857 | 2025-09-27 03:53:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8b3f198-975a-3f6e-b1b0-066176ad8600 | -6.49148 | -39.46848 | 2025-09-27 03:53:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| da956476-0626-3e3d-aa5e-aa4032ed4439 | -6.26977 | -42.49221 | 2025-09-27 03:53:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 76988b6b-ccaa-3938-872f-c7b8c0e753b8 | -5.07812 | -44.85616 | 2025-09-27 03:53:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| a42e85e7-fb99-3cd4-9c52-bf4b21613406 | -5.51866 | -43.87302 | 2025-09-27 03:53:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| aa1b025c-34b2-372a-b123-bdc64e9c3f5b | -5.46513 | -43.06259 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15c7be7d-1b8b-39f8-a792-2b32a57fe13b | -4.57308 | -44.07781 | 2025-09-27 03:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2de52ca4-aada-3e14-89be-3df500f21e57 | -5.47544 | -36.66685 | 2025-09-27 03:53:00 | NOAA-21 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| eea13a8b-5ee8-3847-b7ff-41d809468a8a | -4.58233 | -44.07522 | 2025-09-27 03:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9ece4c9-7b50-33fc-a62c-f84499a52177 | -5.45891 | -43.07561 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b015e346-832e-3608-85d5-0a77811e67cb | -4.14144 | -39.99807 | 2025-09-27 03:53:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a298710e-b197-3312-985e-33184b3d19eb | -6.31893 | -43.45952 | 2025-09-27 03:53:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e2d0fac-d68a-3a11-85c3-cfa0482d2613 | -5.7974 | -42.83184 | 2025-09-27 03:53:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5f91fe69-aa0e-3910-bead-4848c74d4ef4 | -3.80258 | -41.57307 | 2025-09-27 03:53:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 6a841aff-9fb0-3d23-8b67-e1e8ed5e8f1f | -5.72627 | -42.29802 | 2025-09-27 03:53:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8efbac11-ce69-3e46-a7f9-e4b1e82d782f | -4.62247 | -47.41491 | 2025-09-27 03:53:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb747b99-77a7-3001-8b1f-9206699a31a8 | -3.9652 | -38.28386 | 2025-09-27 03:53:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f7c879a0-2916-393d-93a9-6b54e8196029 | -5.47703 | -43.06456 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 8f895776-8531-3bba-9ae6-7d93c5691f54 | -5.51736 | -43.88072 | 2025-09-27 03:53:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 09df6a3c-be80-3fb3-a40e-8c8ab9e76fcc | -4.80692 | -46.81008 | 2025-09-27 03:53:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5835ac6e-b69a-33b9-990b-9e0a7bfc3a9e | -5.48276 | -43.0794 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 56e98da9-8c7c-3979-9752-a12da02af4de | -4.68983 | -37.63448 | 2025-09-27 03:53:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6fb36ee8-ede4-34e8-9216-ca54ded2ec04 | -3.87989 | -40.44247 | 2025-09-27 03:53:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5a270cf3-7c1e-3b9a-97ef-d7f99894f284 | -3.81448 | -40.37294 | 2025-09-27 03:53:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d0e206b9-e525-374c-bab9-f3bb5b3e99e2 | -4.57468 | -48.01807 | 2025-09-27 03:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 379c1eaa-64b8-3072-a0e8-7742a3d1f7d4 | -5.51801 | -43.87688 | 2025-09-27 03:53:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 958f9e66-8046-3862-9d9a-f3e953237ab6 | -4.53591 | -48.64977 | 2025-09-27 03:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c5af8311-422a-3be6-8782-e0dc4765c734 | -3.54068 | -39.8211 | 2025-09-27 03:53:00 | NOAA-21 | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d6f72486-0f7d-3585-8ff4-c5fc41970b2c | -4.00324 | -46.96554 | 2025-09-27 03:53:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3d106c98-65d6-3ff2-9fdf-cb5d3a91a7e7 | -4.16649 | -44.27261 | 2025-09-27 03:53:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 008efbcd-18a7-377c-89a3-251ce7e6043b | -5.8215 | -41.2971 | 2025-09-27 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4ad74e3a-5c0b-39ee-9093-4396b0f33761 | -4.77547 | -41.05462 | 2025-09-27 03:53:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 82309d09-fd07-367c-abf7-e8040cc0e89f | -5.50963 | -43.87561 | 2025-09-27 03:53:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1c5c0817-e081-307d-8b33-dee6ca2f7d76 | -6.32227 | -43.38843 | 2025-09-27 03:53:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f5cd0fd8-d888-3316-971b-5f1f56a1c537 | -2.549 | -48.4054 | 2025-09-27 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 497bf9df-163a-38dc-a0c2-71c96c4c7dd2 | -3.40348 | -46.90388 | 2025-09-27 03:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec06779b-e2b8-31d2-ad96-ca1643cca4dc | -5.22437 | -44.49098 | 2025-09-27 03:53:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a34240b6-7188-393a-80af-f73acfbd302a | -5.48673 | -43.08007 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 62baa32c-f3d6-3d6b-a316-4f6ab9aed3f8 | -5.0736 | -44.85548 | 2025-09-27 03:53:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 9b1125d0-ae13-358d-88bd-7a600f95b1d0 | -5.97532 | -44.12915 | 2025-09-27 03:53:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a96a0cfb-6cfb-344d-bb92-ef335f9357b7 | -5.77801 | -43.64834 | 2025-09-27 03:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1b882c8-50b5-3d36-b15a-315b79198942 | -5.49069 | -43.08076 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 32.7 |
| a9d9b7de-987e-3d28-8c10-911f8a8d4630 | -3.53726 | -39.82057 | 2025-09-27 03:53:00 | NOAA-21 | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0c7a20bf-b15e-353a-bf7d-dde9d1918be6 | -6.4264 | -43.07154 | 2025-09-27 03:53:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d5304e4e-15d0-3c0b-b6be-a54c5710d546 | -5.51382 | -43.87625 | 2025-09-27 03:53:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| eb03928e-48b6-3da0-9bbb-a2e6b65d1b01 | -4.61589 | -40.21684 | 2025-09-27 03:53:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ce27ffbf-7161-36fe-a632-0f48d0faa731 | -3.83463 | -40.33633 | 2025-09-27 03:53:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 65880551-acaf-3e84-a313-3600fedce564 | -6.36505 | -43.34137 | 2025-09-27 03:53:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4a6c445-fc3e-3e56-be68-e2ec47789dc0 | -6.227 | -44.18437 | 2025-09-27 03:53:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2b0b818-224a-3e59-87ab-4dc35e21f75d | -4.79892 | -45.11937 | 2025-09-27 03:53:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d39fc4ad-e613-397f-95cf-8a7e30fb648e | -5.48331 | -43.07599 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 7692670a-a9bd-33e6-bfb8-c3f6c5b93c89 | -4.32939 | -48.39169 | 2025-09-27 03:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2f7fa7d-5c43-31fe-9b02-23d721b6500d | -5.78742 | -41.75597 | 2025-09-27 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 972c17f8-2b6b-3337-bf50-6b47bf15860d | -3.99738 | -46.96806 | 2025-09-27 03:53:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5a77bee-1cbd-3cb2-9ff8-71444957aa82 | -5.36729 | -42.2838 | 2025-09-27 03:53:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 30281c61-15ef-3008-90ef-e1b13efd1393 | -5.76579 | -42.79912 | 2025-09-27 03:53:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 60e18ab6-1ce8-390a-b130-3601f826b1e2 | -6.06195 | -44.07929 | 2025-09-27 03:53:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1124a106-5b00-3bcf-93f5-ab91f2139b9c | -4.58059 | -44.07397 | 2025-09-27 03:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 803681e9-1371-3563-aaff-02ae47d6c01d | -5.73476 | -42.64867 | 2025-09-27 03:53:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 0446174f-941a-3ed9-b032-d61d81be6846 | -4.57738 | -44.07853 | 2025-09-27 03:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7664ff69-4df9-3d3e-a8af-f02a18fffea0 | -5.46574 | -43.08372 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f3332f9c-df0b-3b60-8b81-3ed03e5ea518 | -5.94599 | -44.88189 | 2025-09-27 03:53:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b90cc7ed-d02f-3a93-999e-cf0e28fb97f7 | -5.48728 | -43.07664 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 04586db4-a524-3db4-bcf0-7543bd24cacd | -5.08109 | -44.86618 | 2025-09-27 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8d37b482-e753-3d8d-8f9f-91484287ff95 | -6.07172 | -44.07246 | 2025-09-27 03:53:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc2656e2-950e-327e-91ef-56e9837e88dd | -3.31712 | -44.1893 | 2025-09-27 03:53:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a3f88cf-399c-3e7a-b453-b289126f5d85 | -6.49425 | -39.47252 | 2025-09-27 03:53:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| f44f9c60-61d4-38a2-801a-07bfd1e8efcf | -4.57374 | -44.07375 | 2025-09-27 03:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9ca2a42-4282-3088-835a-16af63802184 | -4.1716 | -44.26898 | 2025-09-27 03:53:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README12.md)
