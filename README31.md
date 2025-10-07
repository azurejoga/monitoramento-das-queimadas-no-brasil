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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59c782da-5c38-309d-b354-5f3ad85e3f51 | -8.61618 | -44.92289 | 2025-10-07 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 839a5786-d0ae-3474-a65d-60d8431b4cf3 | -11.03283 | -50.90678 | 2025-10-07 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2bc95efd-fadd-37bf-a6ec-fefc2af413cd | -11.93992 | -46.42177 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b917e86-989e-3eb9-a38c-600694e83b1b | -8.48113 | -46.29939 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 453942b8-e479-366d-b3bd-3c8788e44371 | -10.55463 | -54.86889 | 2025-10-07 04:08:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4905d3f1-ca30-3fb2-bd21-bb61674eb545 | -11.05024 | -44.78613 | 2025-10-07 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be0b1cc4-73a5-3e47-b3c7-1336e39cd876 | -11.77514 | -45.12599 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15fe0470-ead8-3e03-a1c9-d5c6b6ffeae6 | -10.09268 | -48.17421 | 2025-10-07 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f2d6c93-d589-39db-8b19-8824ebaac937 | -8.5607 | -50.08578 | 2025-10-07 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c4111414-bae6-3ef3-bcf1-883b83d89bfd | -8.55422 | -46.25672 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e8f7760a-c591-3e14-a5bf-3a46f88086db | -7.98589 | -49.95716 | 2025-10-07 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| acaf4c97-86d7-36b5-9b74-a38c84a4d49e | -10.73902 | -50.49101 | 2025-10-07 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 591d227a-b556-3120-8bd0-11a6d9cdb17a | -5.65656 | -43.18656 | 2025-10-07 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 11.3 |
| e7713cde-8098-3185-bafc-09fc7edcb6c0 | -7.88793 | -47.81334 | 2025-10-07 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8acc8caa-f689-33f0-8a12-9b9e20a3c765 | -11.04717 | -50.91243 | 2025-10-07 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bac71641-5983-31ff-bbbf-363ea3fe21d6 | -12.48514 | -45.55762 | 2025-10-07 04:08:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af7afa1b-7b70-356f-924f-10819f6fc6cc | -6.46274 | -43.44225 | 2025-10-07 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 70f2466f-9552-3474-b5b0-9b13261fd0fd | -6.33004 | -42.99538 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06b9d016-db10-3913-afe4-f6b4df74818d | -9.78609 | -48.28347 | 2025-10-07 04:08:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4d9622b7-c7d3-3013-97fc-5dfee2096484 | -9.97979 | -48.0179 | 2025-10-07 04:08:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 73c99844-809c-3392-b42e-461a2b187532 | -11.85075 | -44.92078 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 59e631b1-1569-39e1-bb6f-f99ecf739c91 | -6.71391 | -42.85145 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 442e4725-be36-3ca1-bd29-5faefa5d9b8d | -6.97146 | -41.99761 | 2025-10-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| de7285f8-d661-3c77-9c94-2e113cac2f21 | -11.49167 | -44.96898 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed78658b-b6b2-3f2a-a402-1c1a19a9aef6 | -8.61839 | -44.93155 | 2025-10-07 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f8fe11c8-4749-3876-be1c-7c195a6d9f77 | -4.58149 | -48.12307 | 2025-10-07 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 53538ee0-3703-3e38-941d-46981641a1d1 | -11.94794 | -46.4412 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8269ba24-0f47-3170-b2a0-94c6e6980952 | -6.07102 | -42.56766 | 2025-10-07 04:08:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1222c25a-3c2c-386b-909a-cac2f100ddde | -7.88724 | -47.81736 | 2025-10-07 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9429b530-13b0-33c9-93ec-a016e1662c06 | -7.03022 | -42.29427 | 2025-10-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e3b745d2-e3b7-34f5-b14d-ac4ef0c5a513 | -8.48969 | -46.27189 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e4f59e9-e44c-3f47-b6fd-3c1b46711ae7 | -11.81313 | -45.04084 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 165b2f05-1aca-33ff-a843-42f5c6fc9fcd | -10.9221 | -47.0761 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cda24912-79b3-3cb8-a83e-ef520f32355d | -10.26962 | -44.37613 | 2025-10-07 04:08:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5db45ac9-5fdf-32e7-9549-4b6cf7399d4d | -5.54532 | -42.6806 | 2025-10-07 04:08:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| edd596d5-bdb7-303c-beb5-8be2d913eebb | -10.90008 | -51.06358 | 2025-10-07 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e136101-828e-355f-b434-4a67e85f00c7 | -6.71595 | -42.85593 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 83fda0f8-e62d-3d7d-90be-e9f9a510980a | -4.55263 | -46.67817 | 2025-10-07 04:08:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55477f8e-bb5e-3832-8b45-ccdc99d94dee | -11.80965 | -45.04483 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| defdcb7b-020b-326f-a023-73f17f0237b5 | -7.67835 | -50.20828 | 2025-10-07 04:08:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3741db59-df07-305a-bf31-b976efa88a62 | -10.57997 | -51.46981 | 2025-10-07 04:08:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c61d3ef9-406d-3311-9718-955833c177e5 | -6.20582 | -44.09482 | 2025-10-07 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eaf61091-0d47-33c5-b96f-e753e6c029d8 | -8.85001 | -46.09559 | 2025-10-07 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2a7ceb93-841b-3b0f-abfa-d9d1b20b262a | -6.72119 | -42.80531 | 2025-10-07 04:08:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9f4d63eb-f051-348e-9479-2342eaeb8e0f | -8.65736 | -46.29054 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 54abe5f0-2bcd-385d-b250-3188461998f3 | -6.24726 | -43.25361 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9a85870-4c34-328a-a206-9a97cff6fac6 | -8.65254 | -46.27736 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de5f76ba-6e76-38f5-87f1-5fe93d1eeabc | -7.67924 | -42.5803 | 2025-10-07 04:08:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4948354c-39da-3536-9986-ebb52fff5523 | -7.02115 | -42.78065 | 2025-10-07 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 445ce84b-f624-39e9-9de2-2de6a4254154 | -8.54701 | -46.2571 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1453be39-04e5-33a3-a06f-b6da3e100fd2 | -9.70049 | -45.93167 | 2025-10-07 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 288a4e52-0e0a-3dc6-b3dc-808a9674f819 | -11.67613 | -46.33882 | 2025-10-07 04:08:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44e814e2-882a-34d3-83d0-4383cef0c384 | -11.22624 | -47.77815 | 2025-10-07 04:08:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3851f12-94e1-3a33-9a6b-3d4fc3a6adc8 | -7.47606 | -42.61609 | 2025-10-07 04:08:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c2f8fd0c-5111-3d22-8d22-f93b37941c54 | -5.61735 | -43.93641 | 2025-10-07 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 32cdd552-9dd1-3076-91af-fea82373ecf8 | -8.80194 | -47.86037 | 2025-10-07 04:08:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8fe37e16-5faf-3b82-9440-a3381075b3bd | -6.31989 | -41.61488 | 2025-10-07 04:08:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 51af1f7d-2627-3c40-a670-39734a0834e6 | -9.96884 | -43.78374 | 2025-10-07 04:08:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 331950db-2088-365c-bf74-f4930d3b2d96 | -9.18855 | -47.84161 | 2025-10-07 04:08:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7fb931f6-b0b8-3adb-b6c1-8156ccd378be | -7.00325 | -42.85036 | 2025-10-07 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6fe4ad8c-3ab8-3e69-a723-bddd8c933460 | -6.45733 | -42.79286 | 2025-10-07 04:08:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3ba3969a-1783-3c4d-a6ac-32a3740a8bbf | -11.39207 | -43.48884 | 2025-10-07 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d55caab-0275-33f8-a7e4-9b415cf936d7 | -11.15253 | -47.74996 | 2025-10-07 04:08:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9e2c0505-8bf1-3efb-b5c5-8599e0fa5eff | -5.95839 | -44.34203 | 2025-10-07 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 722ed488-8231-34ad-a4a5-57f7990c2696 | -11.79812 | -45.09392 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ed3fd98-a356-3c68-a4ff-4da1dc42ae45 | -6.23455 | -44.65189 | 2025-10-07 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1e85290-76ae-3b64-adb2-b1bd6363a972 | -11.43817 | -43.47799 | 2025-10-07 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e805542-dfeb-3ab5-8331-bd2048cb171e | -7.57323 | -43.96675 | 2025-10-07 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 450d42b9-9bce-3560-b8ba-5dc96cd452dd | -8.18349 | -50.29861 | 2025-10-07 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d20426e-0ea3-33c1-af85-9aa59b8526df | -7.59901 | -37.80751 | 2025-10-07 04:08:00 | NOAA-21 | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2f2b4ae5-3645-331a-8718-622a3a0fd5b3 | -11.71865 | -44.31302 | 2025-10-07 04:08:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8fcf925-b901-3316-be0c-1094ae58b598 | -4.91493 | -48.01933 | 2025-10-07 04:08:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44fa987e-a912-3c55-9ba8-318f076d0092 | -11.85917 | -44.93383 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e27577ba-e432-33d8-bb7d-a27d02176d08 | -9.09517 | -44.39909 | 2025-10-07 04:08:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19d04931-bc28-37a9-a70d-9358ac4c529d | -8.64413 | -46.28088 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b2c2dfdd-b0f5-3ce3-86b7-2b0ba424e02a | -8.1869 | -50.30822 | 2025-10-07 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c581cac5-f2ca-316a-bad5-b78c625b304e | -11.2956 | -48.26861 | 2025-10-07 04:08:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c82d0a01-5e9e-3212-9586-0e87eb1f21cb | -8.59913 | -44.91596 | 2025-10-07 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a0902fa3-fa9c-34c2-aa6b-3d4d278d7fe5 | -11.7425 | -43.29676 | 2025-10-07 04:08:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 09c566b2-581b-33f0-a139-f16df2603794 | -8.43634 | -48.70019 | 2025-10-07 04:08:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9d5977b-d829-3062-b0fd-d47e67b87a3a | -6.64895 | -39.30001 | 2025-10-07 04:08:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b3e366ca-1589-31d1-b79f-ec7b9c3bb1ac | -11.71647 | -45.4398 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc8cf627-f2ca-3ddb-9301-e4e44181d6f5 | -7.01645 | -42.29209 | 2025-10-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 77f13773-200d-3ccf-a862-8a773ce894d9 | -11.5692 | -44.66551 | 2025-10-07 04:08:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d4bcca1-7434-3fa4-a2bc-518b5d59ebf7 | -11.95236 | -45.49 | 2025-10-07 04:08:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 18f301cf-50a9-3f44-a218-a2bf2fcd218f | -8.91235 | -50.60702 | 2025-10-07 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c1beab40-4b22-367a-b622-0060ac7bc425 | -8.55542 | -46.25354 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 020072ff-0240-3e26-bc2e-c574e07fd87e | -5.44979 | -44.64593 | 2025-10-07 04:08:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11ef6f96-bae2-3190-b9e8-e69bc2d964b8 | -11.46357 | -43.48937 | 2025-10-07 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 69409658-2f9c-3940-8eef-105ab30c7a8f | -5.51371 | -41.00431 | 2025-10-07 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 93cc6ea2-038b-3c5c-bd62-248087af17ef | -9.19124 | -47.82618 | 2025-10-07 04:08:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ed424da4-2579-3f27-bbac-461017a46470 | -8.61972 | -44.92348 | 2025-10-07 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d8af307-b8b0-3cee-bd67-d8d8d1b10a2f | -5.46012 | -42.89894 | 2025-10-07 04:08:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ab3b29ac-c044-34fc-b4ed-e752b7d1a2be | -8.58916 | -44.33392 | 2025-10-07 04:08:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3abcc138-902f-3f7b-b397-d1d80e5c10a3 | -6.65115 | -41.97833 | 2025-10-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f34d5839-224c-33aa-9d6c-8d6d23d3b848 | -6.36848 | -41.6331 | 2025-10-07 04:08:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5ca3fbbb-c316-367c-8d59-e9ce2cfa3f6c | -5.2954 | -42.54256 | 2025-10-07 04:08:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5512ad72-6928-3665-a826-93a6c5cccb9f | -5.49458 | -43.0827 | 2025-10-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 3351a54a-92b9-30c3-a7a7-74126878b966 | -11.74361 | -43.28973 | 2025-10-07 04:08:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9c82f76a-a670-334f-8bc6-e2b00f115afd | -10.67676 | -44.14522 | 2025-10-07 04:08:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README32.md)
