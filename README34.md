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
| f4e6de62-1327-3329-ae71-01aad3631e08 | -5.61895 | -45.24075 | 2026-09-19 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 78cee46f-2ad9-321d-85dc-f522c46ddf34 | -7.00106 | -42.17281 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ca41ecd9-13f0-35e6-acc2-790165e5fb1c | -6.02543 | -51.76391 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7936ed19-7c5d-34ef-ba83-60193d865f0e | -3.35987 | -50.44691 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3490f76f-f698-3fd6-91fd-d908543dc919 | -8.60955 | -54.59449 | 2026-09-19 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c6780295-453e-301f-9b6f-35a8a55c9ac2 | -10.58889 | -46.60755 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7f3d51cd-21a5-328f-aad7-4364679ac029 | -7.883 | -46.43296 | 2026-09-19 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| c5205656-7d59-34a2-9656-3ddc61e68c7e | -2.81937 | -50.48016 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 03c4c171-afa9-3784-a8a9-79739b46bb9f | -10.55028 | -46.58497 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f073e798-d599-30ba-938e-864a7127cf24 | -9.60874 | -35.91578 | 2026-09-19 04:02:00 | NOAA-21 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 741593a6-535e-328e-b885-c26e384007f7 | -7.76336 | -46.75732 | 2026-09-19 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 244272c5-4faa-3d9b-903c-5a1d578673fe | -5.14127 | -45.77151 | 2026-09-19 04:02:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e4af56b8-b4e9-3dab-bac1-a2b3ce585fc9 | -6.62004 | -43.36328 | 2026-09-19 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 16f3679c-bb8b-33ba-863d-133b40121d86 | -7.05242 | -42.07421 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 84597117-6449-3474-9b1f-23ede81950fb | -8.3763 | -45.6514 | 2026-09-19 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eda04108-48e9-32b1-937c-48a079884e68 | -9.98093 | -50.27781 | 2026-09-19 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4e4c941-1e1f-3907-9734-2d0e8e9b66b2 | -3.33235 | -50.1134 | 2026-09-19 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b8277b5f-9816-33bd-aa15-80a0635b0d21 | -8.77975 | -48.68277 | 2026-09-19 04:02:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 6c6e0ed7-4ae0-3fbc-b7d1-a66d532e5bb9 | -8.39491 | -45.63911 | 2026-09-19 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 932d809e-71da-3c43-8574-8082d89c2d57 | -9.24561 | -45.93007 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c859952e-dd48-37ed-97ac-564dab36621c | -9.24073 | -46.20087 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 65fa0405-a477-3518-83b2-05241f459dc3 | -3.35915 | -50.45127 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9745f710-822f-3817-b369-c1d67f9048ee | -3.45897 | -50.61345 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 15de4245-aedc-374e-b917-0da5987a19a0 | -8.24486 | -45.61447 | 2026-09-19 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4e67ac8-4383-38f5-bb8a-b694094791a2 | -5.24811 | -44.92797 | 2026-09-19 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e97d58a1-6dfb-36a7-a8dc-c14c78ff6968 | -5.99646 | -51.79525 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 622fd7ee-d7e5-312c-afe7-110a56d7c73e | -10.61246 | -46.10576 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| cf3566f0-d0f6-3fa8-88e8-a37e5f94e38d | -9.04181 | -48.71193 | 2026-09-19 04:02:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 64680c66-9600-360c-b9ea-60d49dfd0308 | -7.39594 | -44.49421 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 124e158f-b7f9-3aae-b628-0c2dbe84ffb0 | -9.89493 | -46.54809 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 11603713-d686-3431-b5b8-d316e8bc91d9 | -9.89421 | -45.82567 | 2026-09-19 04:02:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5f3e40cd-2f12-31fc-b0eb-bde0205c40ea | -6.02783 | -51.76452 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6659be75-dd6f-3443-8c84-69595b7e60b9 | -7.36475 | -50.32942 | 2026-09-19 04:02:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0409a740-bfb3-341d-ac63-06bfbf609f57 | -10.76381 | -42.11118 | 2026-09-19 04:02:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cb020211-13d7-3203-b5e3-c36fdbb572ca | -7.81963 | -46.63596 | 2026-09-19 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a787f32b-5da8-38c1-b205-37b876e5dd33 | -9.89074 | -46.54753 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c06fd33f-1c63-3e99-a65b-5f5ce64669a6 | -10.00356 | -50.27491 | 2026-09-19 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e621944a-522a-3937-99dd-4f4a1be23d20 | -9.74487 | -46.09123 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 29695153-7ca1-3f49-935d-b743526601a4 | -9.70319 | -48.3248 | 2026-09-19 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6b42048e-91c5-377d-8e11-60eefb4dbc28 | -8.88004 | -45.93782 | 2026-09-19 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5eedd44-52ad-3aeb-9179-10ad334d9e54 | -9.56582 | -45.4785 | 2026-09-19 04:02:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 14b0f219-f159-3fdb-993e-ab2719d6135d | -8.77938 | -45.86505 | 2026-09-19 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b72309d-2e96-34db-a66f-8853859112c5 | -10.17974 | -48.52315 | 2026-09-19 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ea1d772c-44cc-35fe-8149-e816906c0d45 | -4.55388 | -42.97842 | 2026-09-19 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b7bfadd-0424-341b-98a5-82d2c7c14831 | -4.25934 | -48.53881 | 2026-09-19 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 52bce651-0018-3612-a3ee-5a58f4a2f94d | -6.2699 | -41.67289 | 2026-09-19 04:02:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 172491f5-b4e8-3903-8eec-33b0d95f6bbe | -8.29486 | -46.85122 | 2026-09-19 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4db92072-6dea-33b1-a339-2fac156361bf | -7.69516 | -46.10983 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a8e0f583-f035-319f-a6c6-b2b849daf3eb | -4.9519 | -43.00256 | 2026-09-19 04:02:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 88ac9da9-85d4-36ea-9379-ff9515de5bfb | -9.04859 | -48.73064 | 2026-09-19 04:02:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5816e769-2e78-3915-9b11-b8b4cb4192fc | -6.62196 | -43.36501 | 2026-09-19 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 949eaf9d-e489-322e-a8ec-f5e99be57c75 | -8.77057 | -44.22868 | 2026-09-19 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ee36e3a1-4c31-320e-bb2f-f74a9eef3f1e | -5.83492 | -47.7861 | 2026-09-19 04:02:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5861edae-507a-318d-8a75-715117ad7db7 | -2.82795 | -50.45989 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 5044edb6-337c-30e0-87fa-8f231f08753e | -8.22996 | -45.60474 | 2026-09-19 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b784c3bf-7fc1-34a6-96f8-c8f0d2b5bce4 | -6.98901 | -42.18244 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| e6dfd258-6c21-3681-b1d3-2f826b64f82a | -3.36888 | -50.44204 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 21d8b680-a29b-364f-b6cc-e0e8cb4cfed4 | -3.23851 | -46.96017 | 2026-09-19 04:02:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| d5ba1e07-87bf-35f0-b18c-588a7b4ef15a | -8.44033 | -45.74428 | 2026-09-19 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6139a6d-6e3c-3aca-80a1-ea2c8145a42b | -6.29916 | -45.57205 | 2026-09-19 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1bb29c0c-c630-3552-a290-a42899692776 | -6.94892 | -46.97236 | 2026-09-19 04:02:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4521f160-24be-392a-a862-a1e6238960f1 | -8.39022 | -45.64244 | 2026-09-19 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| afbdeea3-6464-3e9d-ba27-9adde3bda271 | -8.87939 | -44.91791 | 2026-09-19 04:02:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 58d560a1-1258-3b33-8c96-faa6c182734a | -4.0175 | -41.28273 | 2026-09-19 04:02:00 | NOAA-21 | SÃO JOÃO DA FRONTEIRA | PIAUÍ | Brasil | 2209872 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f9fdbe7d-ca89-3a7d-9565-950cd233e399 | -7.4433 | -44.70013 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ce5a4f98-5d06-394f-b68a-692bf6de2c62 | -8.61441 | -54.58753 | 2026-09-19 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f40e5d96-7986-303b-bdd7-a476a58b2bd1 | -3.54249 | -48.18389 | 2026-09-19 04:02:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ad17248-643d-351e-b94c-c1be197183dd | -7.88439 | -46.42492 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 4330fc83-789f-3e3b-99a0-692be540465d | -6.90704 | -41.71025 | 2026-09-19 04:02:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 58917a6a-8674-3950-9695-b311ba1cb061 | -3.37043 | -50.45783 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ce9b1f32-c99f-3d32-b622-7509d6ea7f57 | -2.73672 | -49.45972 | 2026-09-19 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 89058619-ef66-3cc2-a28e-149482121f9a | -7.60663 | -45.43137 | 2026-09-19 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f66b3ea6-218b-3bdc-9c3a-c29ad04ac673 | -11.28462 | -43.51033 | 2026-09-19 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a8549de4-72ed-3771-805a-219bd8c4ed7c | -8.92469 | -49.99793 | 2026-09-19 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ec0a4fbe-b6aa-3edd-b912-284cbfc9348b | -8.83688 | -46.93475 | 2026-09-19 04:02:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d47dcdc2-ed90-3507-b2a5-f09f7a1c6c65 | -9.17717 | -46.74681 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a5a69bfe-a389-3685-983b-6024bf0ec9f5 | -10.09794 | -45.64421 | 2026-09-19 04:02:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ec38aa5e-bbcc-3414-a558-817f95bf4b42 | -9.64224 | -45.90738 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 229bed7a-5abf-31b1-9dd5-2698911fa770 | -9.00957 | -44.9083 | 2026-09-19 04:02:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2cdfd8e6-7d00-3a69-a622-4a401c9e9c3f | -6.30331 | -45.57264 | 2026-09-19 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e7222c68-613b-3b82-adfd-4ba8a037fd8a | -7.36409 | -50.33309 | 2026-09-19 04:02:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 860398fa-a2e7-320d-8d38-13fa3690b4ca | -9.57067 | -46.55968 | 2026-09-19 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a694e30c-de1d-3f20-901c-8b4527383537 | -4.59415 | -42.95903 | 2026-09-19 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ae29c849-79e3-3a7f-8558-158aff434b48 | -9.02698 | -48.73851 | 2026-09-19 04:02:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 12ed2d38-9d4b-387c-9e69-d928062414f7 | -3.36209 | -50.44547 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f4dfe12a-1cb1-3d74-ac1a-2fa0b96a4f43 | -6.26315 | -41.67177 | 2026-09-19 04:02:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 814f1a87-3a9d-30a7-b6ba-9288e79fc3d4 | -9.94004 | -45.31639 | 2026-09-19 04:02:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1fae5003-15e8-3df2-9c90-78e50b824199 | -7.78249 | -44.83831 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 638a1c31-6cdb-30eb-a54e-8d4378850d03 | -7.08869 | -42.08748 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f3071ce9-efb0-3b95-90ca-bf107e94c0bb | -6.29148 | -41.777 | 2026-09-19 04:02:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b03a6d8f-cbca-3f34-ad1a-97629d4d8f0b | -9.97624 | -50.27341 | 2026-09-19 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fde48b28-b5b6-3462-a813-de9e2fc6e1a7 | -9.24432 | -45.93748 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| de5a2e54-43e1-3aab-aa87-f93e0aec4bd9 | -9.20781 | -46.76514 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d7a0606d-343e-372f-8286-7efdc686aae3 | -9.60009 | -45.37159 | 2026-09-19 04:02:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ac142a1d-4180-3f48-8a8e-7a81de18116b | -4.5575 | -42.97901 | 2026-09-19 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0ff42b98-5d10-3154-abdb-aab76983fb4e | -5.62119 | -45.25269 | 2026-09-19 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e21b105-76b1-3dce-833e-4cbbd61a70c1 | -9.94281 | -45.27674 | 2026-09-19 04:02:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dfa3e1b5-5236-3cef-8272-866551ac419f | -9.65487 | -45.90591 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b80a5e4c-b18f-33d7-8f9d-d97c9bc451dc | -11.1202 | -45.28388 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8437d8bc-1550-3e36-bb16-681f6e6b1046 | -14.92589 | -49.92089 | 2026-09-19 04:04:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |


[Clique aqui para ver as próximas entradas](README35.md)
