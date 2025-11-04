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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4bb85c54-bd18-337a-bd45-14d9deb06afc | -2.6416 | -54.58181 | 2025-11-04 04:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5b77f5f-2474-31ba-9d49-b3e17ab43f87 | 0.98291 | -51.21602 | 2025-11-04 04:10:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 133b9f1e-1a96-3ce4-91c3-635d1f8b00f5 | -2.94772 | -51.57877 | 2025-11-04 04:10:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54c09ecc-286c-3bf6-a609-98708eefc0ac | -5.93267 | -41.2961 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9bc45870-727f-32a8-8115-73e1215cb354 | -5.03341 | -43.61902 | 2025-11-04 04:10:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e2792aa1-8bd0-332d-8f44-cdcb446c76cf | -3.92405 | -47.70091 | 2025-11-04 04:10:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d0e06af9-56b5-330b-a9bf-2e6d01fd7e36 | -4.58383 | -38.29695 | 2025-11-04 04:10:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d10c9992-062d-3bfa-8983-631bdcae428a | -5.36498 | -44.73629 | 2025-11-04 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1715b9e-98b4-3026-8057-2c8eebd0e929 | -5.52868 | -41.13296 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0fc5894d-e27d-38f0-b736-183bfae1958e | -3.49214 | -50.46665 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8acced21-f784-37a6-b3fb-701cdebe6bf9 | -3.4395 | -50.24379 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0c6399d2-4383-39ce-b186-fea06ee04d80 | -3.75477 | -45.08799 | 2025-11-04 04:10:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc7464b2-9948-3b8e-9ffc-80c6fe70ebaf | -3.34332 | -45.378 | 2025-11-04 04:10:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0889fc5-29f7-31bf-9b8a-d85dcecce14b | -2.87165 | -45.29805 | 2025-11-04 04:10:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 57605379-9354-3a06-af21-9157e9497d5a | -5.51149 | -41.11253 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a3ec95c2-ecb7-3b8b-917b-04a81a349e06 | -4.43049 | -45.55743 | 2025-11-04 04:10:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a18ccbf3-56d2-326a-b669-d54d0f433e9a | -5.92935 | -41.29558 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b578e67c-b35f-31ef-8228-ddecf3e6d5f3 | -5.14765 | -41.20733 | 2025-11-04 04:10:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2989878b-c5fe-3042-b63b-e536afa1ce86 | -3.76941 | -52.32076 | 2025-11-04 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a989d13e-f6b6-3e1b-9e4e-ae6f731817a9 | -2.32099 | -48.58889 | 2025-11-04 04:10:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 29234e4e-1f12-3b70-8b7b-1be9aa925bd9 | -6.42256 | -43.07007 | 2025-11-04 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8279e33d-8795-3c0c-826a-21f92f60cc6f | -5.52645 | -41.12552 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7a8e7a96-a6b0-3b46-be56-7ba84c2da38e | -6.41636 | -43.06537 | 2025-11-04 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a38a0d8c-5206-3820-83df-58109fadd451 | -5.78248 | -40.8098 | 2025-11-04 04:10:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d97281bc-668a-3a51-9b4e-2ab918e3de17 | -6.42375 | -43.06685 | 2025-11-04 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6dad971-a95b-3927-9b81-d0f7df9df922 | -3.23926 | -50.79453 | 2025-11-04 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f1c1ba2-f38e-38c0-a194-9f894211d439 | -4.80733 | -46.72369 | 2025-11-04 04:10:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1e84c9c-c86e-3917-b696-b5e68183cc57 | -3.03905 | -50.34601 | 2025-11-04 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 460d338b-d1d1-371c-8963-29f891730607 | -2.83817 | -49.83271 | 2025-11-04 04:10:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 78f11dd8-a42e-3dd0-ba66-a7d7e56767b4 | -2.31418 | -48.59936 | 2025-11-04 04:10:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 25c3e208-243a-3460-8892-00c025bdffed | -3.77399 | -52.32364 | 2025-11-04 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4835f8ba-ffca-348c-b364-f65c6b7ab515 | -3.77559 | -52.32185 | 2025-11-04 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18fe41d7-d6e1-3df9-8a82-9d5dd0a96004 | -4.00554 | -46.50379 | 2025-11-04 04:10:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bc5ec0b4-cfd2-3d72-ac5e-476588974176 | -3.0696 | -47.77187 | 2025-11-04 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3c65d65f-735d-360c-aeea-01ea4bb45e49 | -6.24423 | -42.0854 | 2025-11-04 04:10:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 536bf859-3775-31a6-9808-ef223e011b73 | -4.74618 | -46.5676 | 2025-11-04 04:10:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7964a38e-4978-3488-a848-5cc1ad062a55 | -2.6233 | -49.23096 | 2025-11-04 04:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8cfacf05-d106-3ea2-a246-fd04f96724e1 | -5.40855 | -43.66156 | 2025-11-04 04:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06c58a9a-a91c-34bd-b1fb-1f38a23283cf | -5.85589 | -43.99764 | 2025-11-04 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b7836bb-e1eb-36d5-a10d-cc9f89396e7a | -5.19197 | -45.274 | 2025-11-04 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93daf33c-930b-39de-8c04-54cb6202ccda | -5.41344 | -45.29406 | 2025-11-04 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28344a15-fc13-3899-abfd-7702e1174637 | -3.36107 | -42.12048 | 2025-11-04 04:10:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ef4b828b-064c-3823-9488-2c326c93a844 | -2.84351 | -49.83361 | 2025-11-04 04:10:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b18f5103-6930-36f6-8226-e352ca8e22f2 | -5.61495 | -45.97986 | 2025-11-04 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 509d484b-a1bf-36a8-9806-112088f1ef38 | -7.31868 | -39.21075 | 2025-11-04 04:10:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fe09627b-d7ac-3d89-83e6-24ec4ad06ac2 | -5.3606 | -44.74003 | 2025-11-04 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29eb374c-318b-313f-936d-5835062eabc7 | -7.08253 | -38.82579 | 2025-11-04 04:10:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f56b0a3c-6199-3e7c-a32a-fdc03e64f2c3 | -5.52368 | -41.12154 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9f404fbf-594a-3b5b-9ff6-8ec3b4ceb4aa | -3.39628 | -40.8359 | 2025-11-04 04:10:00 | NPP-375D | URUOCA | CEARÁ | Brasil | 2313906 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 616d2dcd-c1f9-3573-8cfb-c985411b3d31 | -4.58961 | -44.61265 | 2025-11-04 04:10:00 | NPP-375D | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2797e1c3-6b8a-3536-b446-a700eecb0c7e | -5.23349 | -44.21048 | 2025-11-04 04:10:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 99b4182c-ee86-3ef6-89e8-f4f8503bdb31 | -4.78589 | -43.18703 | 2025-11-04 04:10:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b31917a5-3ee7-3e46-9cb4-6de701480413 | -6.41578 | -43.069 | 2025-11-04 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b0129371-ab45-37b5-a916-49a3d212783b | -3.98398 | -47.07993 | 2025-11-04 04:10:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33e05d65-e3f7-3bdb-93b0-a30777d33703 | -3.06882 | -47.77673 | 2025-11-04 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ec4aaa2-f72b-3660-8dc6-6406b9260915 | -4.3791 | -46.27358 | 2025-11-04 04:10:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 90bbc786-1a05-34cd-b0de-97bbd8016fdb | -6.10439 | -41.70324 | 2025-11-04 04:10:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b6c75b11-9a59-395d-844f-972c103a440f | -5.5159 | -41.10613 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f346908f-a5dd-32e2-90b0-b470695b45b0 | -5.82965 | -44.0909 | 2025-11-04 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 979dfa82-dfac-34da-87e1-5e4809240a61 | -5.98589 | -41.91899 | 2025-11-04 04:10:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 16b3d610-28ba-3f3e-8acf-a05046c1fec2 | -6.70895 | -43.56869 | 2025-11-04 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84e0f226-a714-3eaf-91f3-c9c7c192bbd3 | -3.98833 | -47.08061 | 2025-11-04 04:10:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff9131de-bb24-397c-81ed-20d3ed5443a9 | -2.86772 | -45.29741 | 2025-11-04 04:10:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f659df83-4438-308d-b6ad-f584ef4a4de9 | -5.36767 | -45.07721 | 2025-11-04 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 174c573d-b734-3d97-919f-eeb20cb4a330 | -4.87295 | -49.00329 | 2025-11-04 04:10:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a34db67-b8d2-3389-9efe-bd737cf562c1 | -2.98667 | -44.96128 | 2025-11-04 04:10:00 | NPP-375D | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45906342-9822-368b-9895-143887d3b5b2 | -6.06412 | -47.28986 | 2025-11-04 04:10:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a60323cb-02c0-325d-a340-63ab608bf9f3 | -7.1751 | -41.95158 | 2025-11-04 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f1fa3924-a222-3b09-82b8-40c2b059d930 | -2.29338 | -47.86626 | 2025-11-04 04:10:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0395e00e-9ceb-3562-af48-77cd7cc7ea5b | -2.36911 | -47.72788 | 2025-11-04 04:10:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| de0978b1-3304-31e2-8733-93370494c76b | -4.00794 | -45.29891 | 2025-11-04 04:10:00 | NPP-375D | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cefd38c1-ade2-39b8-9f45-1b9b10a5990b | -5.89554 | -42.91628 | 2025-11-04 04:10:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 63906e5f-033c-3b69-9630-ffeae20f8598 | -2.87245 | -45.29311 | 2025-11-04 04:10:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 86460729-a2c8-34d1-8ca0-08bfe4be489c | -5.57564 | -43.78999 | 2025-11-04 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 745eda06-0335-3449-8a8a-99b4495eef4f | -4.31037 | -41.45114 | 2025-11-04 04:10:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ef965e68-7f4f-3a45-8f0c-ffe57c58dc4d | -3.98329 | -47.0841 | 2025-11-04 04:10:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9dcac7c6-6a98-3e3f-a847-fcb83397e664 | -5.78748 | -40.82136 | 2025-11-04 04:10:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 40ab1289-4e2c-3a54-bdb4-21c94d956b5e | -5.03691 | -43.61957 | 2025-11-04 04:10:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8a2beb18-ac52-3fe8-b7b2-28ce87c4ba5f | -3.0447 | -50.27775 | 2025-11-04 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d0151c3b-adfc-3296-bb4b-6cf63a52730c | -3.6993 | -49.5648 | 2025-11-04 04:10:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7805941b-92db-30d0-ae1f-6f6ebc4e4498 | -3.44067 | -50.23689 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2485d596-0de6-304c-ae2f-c4ceb910ee8d | -5.51547 | -46.23705 | 2025-11-04 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b11c716b-ce24-3326-8290-83d10d7ebaf4 | -3.49701 | -50.47133 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4574cd8d-e192-3123-8096-472d6c33068c | -2.84407 | -49.8303 | 2025-11-04 04:10:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 96f80ac6-2386-3e7d-8a27-35a016eae174 | -4.6745 | -40.4722 | 2025-11-04 04:10:00 | NPP-375D | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bfef68c8-f132-3b2d-867b-277f9a6c2119 | -4.95198 | -44.90258 | 2025-11-04 04:10:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb048e54-79de-397f-8ed5-b1eb630d31e8 | 0.97746 | -51.2218 | 2025-11-04 04:10:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2fd20e9b-4169-31f8-b283-d0ef7b227d5b | -5.61576 | -45.97486 | 2025-11-04 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8661d464-ac69-3e7a-86b4-422ba5130e68 | -2.19601 | -48.35904 | 2025-11-04 04:10:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00ed8c25-33e7-3b90-8387-0a167a89abcf | -5.65325 | -44.06771 | 2025-11-04 04:10:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82e828dd-5872-3f69-b8ae-7a99c5bb7b96 | -3.03965 | -50.34241 | 2025-11-04 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b92a063e-c89f-3519-8f80-ed4942de1c21 | -3.24491 | -50.79553 | 2025-11-04 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5f72069-d9ac-3ac5-a154-3783df6a2645 | -4.58863 | -40.97763 | 2025-11-04 04:10:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 46aa1f0f-1345-3a98-9a27-2ce02351906c | -5.29996 | -44.81019 | 2025-11-04 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 524efb84-6535-3da6-987f-60f36193a1b4 | -4.59424 | -45.58559 | 2025-11-04 04:10:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 95bf308d-68ae-380a-b6e2-d8b7352c4369 | -4.62247 | -46.40737 | 2025-11-04 04:10:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77f8ad20-db94-36a7-ba2b-22fddf3bfbf1 | -6.43054 | -43.06792 | 2025-11-04 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84bb4406-3810-36a7-95a0-10bb36827c5a | -5.25906 | -44.81423 | 2025-11-04 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5329ce59-e364-3313-931a-ce742fa2598e | -6.45197 | -38.17586 | 2025-11-04 04:10:00 | NPP-375D | TENENTE ANANIAS | RIO GRANDE DO NORTE | Brasil | 2414100 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1a2fedbe-5024-3095-93a9-2c055eb88e29 | -5.75195 | -43.39539 | 2025-11-04 04:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README13.md)
