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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dcbc9d2b-1776-326b-a67b-0dd567dea562 | -12.71694 | -48.07681 | 2025-08-06 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a081db1-a514-38ce-bb37-ce64f3a1ff25 | -16.7707 | -49.29061 | 2025-08-06 04:21:00 | NOAA-20 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c66e7561-7784-3721-88ad-5b43c2d186be | -13.3733 | -43.75405 | 2025-08-06 04:21:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eff0e6bd-2681-3d52-a8a1-607a9e6c94f2 | -12.7067 | -48.07518 | 2025-08-06 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4cecda26-dfa9-3e86-a5ce-b53607183cc4 | -12.72035 | -48.07737 | 2025-08-06 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 210382d5-b507-316d-8a71-683dd8f401fd | -15.65895 | -53.60932 | 2025-08-06 04:21:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e1592958-3147-3f55-8bcf-306e76e34730 | -12.66053 | -48.12135 | 2025-08-06 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b56cc5b1-bfd6-3bb8-8a94-6ba5ccc56a72 | -12.7366 | -46.39328 | 2025-08-06 04:21:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d277aac5-2119-38c7-9e82-453a1018c24c | -16.7137 | -49.46133 | 2025-08-06 04:21:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2723460e-2d44-33b8-821e-47c6ef9f541e | -17.82731 | -55.103 | 2025-08-06 04:21:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 26c26512-45ce-30a8-bd36-6ec90f320a58 | -15.69429 | -48.96482 | 2025-08-06 04:21:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ace6e23-59fd-3d72-8497-19dac797f371 | -10.22185 | -59.41266 | 2025-08-06 04:21:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00ed0750-026b-3e83-a171-93df817e6f06 | -15.64287 | -46.96006 | 2025-08-06 04:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc1b959d-c2ec-3434-ae3f-9dcbfe5ad0c1 | -12.96727 | -44.88169 | 2025-08-06 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 825afb7d-3d79-37c6-91c8-73509665c963 | -21.07558 | -49.98809 | 2025-08-06 04:23:00 | NOAA-20 | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 2a953760-07e2-3ae0-a277-b53e620f8eda | -20.77376 | -49.8612 | 2025-08-06 04:23:00 | NOAA-20 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a692daa4-e5fc-3f1b-8884-ccca126ede06 | -21.50201 | -49.74495 | 2025-08-06 04:23:00 | NOAA-20 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 636eb803-e5dd-334c-9bed-e5c3b0008cb2 | -21.02 | -50.0466 | 2025-08-06 04:23:00 | NOAA-20 | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f152fabc-9cae-3604-963b-efbfa0a93231 | -21.07089 | -49.99516 | 2025-08-06 04:23:00 | NOAA-20 | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| a1f43517-699f-3f86-aa31-013cbe890dbc | -24.50584 | -50.73593 | 2025-08-06 04:23:00 | NOAA-20 | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 626500c3-4034-3a86-8dde-2438826d87a8 | -21.01255 | -50.04925 | 2025-08-06 04:23:00 | NOAA-20 | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5a4e5377-f059-337d-9937-9ee6e2dc1c12 | -21.02065 | -50.04269 | 2025-08-06 04:23:00 | NOAA-20 | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| af1021e3-bf3f-3a19-be05-47e752e6a378 | -19.84361 | -51.19809 | 2025-08-06 04:23:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cded2229-5ff9-3e53-b15d-46175388a82c | -19.84451 | -51.20136 | 2025-08-06 04:23:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6ec0280b-609c-3ace-866e-5153900be3b6 | -21.00915 | -50.04862 | 2025-08-06 04:23:00 | NOAA-20 | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| fa8a8452-f53e-3663-93e4-1f023446522e | -21.07428 | -49.99582 | 2025-08-06 04:23:00 | NOAA-20 | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 49c920c9-0bec-38f9-b9d2-2aad48349040 | -24.50651 | -50.73197 | 2025-08-06 04:23:00 | NOAA-20 | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 04e79e5a-2c55-3a8f-98d2-128eb38215f5 | -24.50488 | -50.73638 | 2025-08-06 04:23:00 | NOAA-20 | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 469e7eb4-17a2-3463-afd7-70f6645a7792 | -21.07493 | -49.99195 | 2025-08-06 04:23:00 | NOAA-20 | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 5f1ebcb2-5733-3cbd-b5c6-1d1ae4e6cb90 | -21.4045 | -47.67289 | 2025-08-06 04:23:00 | NOAA-20 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c98e5f70-9787-3364-b722-1bce51d4d8a6 | -24.50921 | -50.7366 | 2025-08-06 04:23:00 | NOAA-20 | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1135097e-998a-3cac-8da1-621fb2851de3 | -23.3098 | -47.48929 | 2025-08-06 04:23:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ce088b2c-65b1-3c7b-87cb-04924d1e8c55 | -19.84285 | -51.20245 | 2025-08-06 04:23:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3695cc75-891b-3b15-b794-2f72451173ae | -24.28872 | -50.83372 | 2025-08-06 04:23:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f60129db-3802-3d8a-b4f1-9c883a8b630d | -24.50555 | -50.73241 | 2025-08-06 04:23:00 | NOAA-20 | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 205e95ae-19f4-3355-b18d-b82d5e14791e | -20.47545 | -53.67525 | 2025-08-06 04:23:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1a9d383-9948-3b19-8d9d-f4172615728c | -21.94582 | -50.51347 | 2025-08-06 04:23:00 | NOAA-20 | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4d06de1a-d9a7-3537-b5f8-9498fca4c137 | -21.07154 | -49.9913 | 2025-08-06 04:23:00 | NOAA-20 | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| c34740f8-ca6c-3595-8dbf-d308672013ac | -21.02405 | -50.04334 | 2025-08-06 04:23:00 | NOAA-20 | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0cc63601-3693-33b3-bec5-014432353868 | -22.66066 | -47.31794 | 2025-08-06 04:23:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 486c120a-b110-3a9f-b71b-5300225189b1 | -23.31373 | -47.48603 | 2025-08-06 04:23:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1481ac83-a300-377d-a46b-923b31337968 | -21.07219 | -49.98743 | 2025-08-06 04:23:00 | NOAA-20 | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| cf009816-a729-35f7-bb11-49bc0717f1a1 | -19.84644 | -51.20319 | 2025-08-06 04:23:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c73a6b7f-d03b-332b-a8f8-272509e9bf7d | -21.07623 | -49.98422 | 2025-08-06 04:23:00 | NOAA-20 | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| de6f4b52-2e51-3292-adc1-ed8fafe2d2f2 | -23.45722 | -51.88871 | 2025-08-06 04:23:00 | NOAA-20 | SARANDI | PARANÁ | Brasil | 4126256 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1f981d9a-6a9f-3cf1-978b-66db43976f41 | -29.90376 | -54.66829 | 2025-08-06 04:25:00 | NOAA-20 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 2bc86319-a55d-3581-b7a7-27d5ba911ddd | -13.0731 | -56.8527 | 2025-08-06 04:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| c74fd218-7c87-3215-9cb3-b47537744ee2 | -11.4389 | -45.1385 | 2025-08-06 04:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| b28c8101-0e11-3cf3-9241-511e21ebcc01 | -8.9215 | -60.7297 | 2025-08-06 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| e44eeec6-74ab-378e-a41e-17ab6cab6c85 | -8.9213 | -60.7489 | 2025-08-06 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 65ebca7b-262d-351f-a71c-1089a942a5f9 | -13.0728 | -56.8729 | 2025-08-06 04:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 39.8 |
| f4d04452-9048-3910-af64-903f5e7d965b | -21.0754 | -49.9855 | 2025-08-06 04:40:00 | GOES-19 | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 136.5 |
| 9dabc786-3287-340d-8c86-c07b6419185a | -8.9213 | -60.7489 | 2025-08-06 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.6 |
| e284b0f3-1015-3d86-986b-5dd99de0095e | -11.4389 | -45.1385 | 2025-08-06 04:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 8f3d267c-c5d9-373e-92ed-005a8e239b6b | -13.0731 | -56.8527 | 2025-08-06 04:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 41.1 |
| b7dd925a-7091-3673-9444-06d9f7ef3136 | -8.9215 | -60.7297 | 2025-08-06 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 2e2b5a94-03fd-3ed6-858c-1cc00d5c3415 | -8.9215 | -60.7297 | 2025-08-06 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 3fbf0fd1-8ceb-3eab-937d-7b41994cea12 | -11.4389 | -45.1385 | 2025-08-06 04:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 2b06be18-a0fc-3851-bfe9-e9f4ba2a35f8 | -13.0731 | -56.8527 | 2025-08-06 04:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 678d8f1d-034a-30ed-966d-6eea22914837 | -8.9213 | -60.7489 | 2025-08-06 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 9d6f66f3-d991-364b-a239-6090555679b2 | -13.0728 | -56.8729 | 2025-08-06 04:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 9a21fc2e-156b-3fef-ae84-94bb8962bc1f | -8.9213 | -60.7489 | 2025-08-06 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 5f23060c-9632-39b6-a3c0-46a398464e3c | -8.9215 | -60.7297 | 2025-08-06 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 4214f203-b998-31d1-a2c5-a8a0a65f56ff | -6.91444 | -43.67826 | 2025-08-06 05:08:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 61d4e6b7-b779-36b6-ab2a-0cf79d20ebdd | -8.01232 | -43.17792 | 2025-08-06 05:08:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 36.7 |
| 5b8129d3-3cf1-30b6-94cb-99d429c70965 | -8.9213 | -60.7489 | 2025-08-06 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.0 |
| a98f6423-949d-35bc-be81-a6300d4c7c60 | -8.9215 | -60.7297 | 2025-08-06 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| a37d19ac-c364-31cd-9b29-5f78697f66b1 | -6.41258 | -53.37128 | 2025-08-06 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0758505-4ed4-3067-bc50-8d2101eb6ed7 | -7.9123 | -45.53196 | 2025-08-06 05:10:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 704c8584-283d-3728-8752-12ea26280165 | -4.82226 | -47.31804 | 2025-08-06 05:10:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a35bf8f8-5d0a-31ef-bd69-f20197f3dddb | -4.02605 | -48.06107 | 2025-08-06 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d2f747a-b9a0-3ee7-a279-9eb583bf8149 | -5.80458 | -59.22787 | 2025-08-06 05:10:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8545731c-8c3f-3e12-b721-fcdecda68d12 | -3.768 | -59.33512 | 2025-08-06 05:10:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 48027197-6050-3068-8ad4-fab30524be29 | -2.95456 | -51.65719 | 2025-08-06 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97463750-93e8-3449-91ce-2f5ffa2f693f | -7.51484 | -44.85958 | 2025-08-06 05:10:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7d3b8bd1-8652-374d-bf52-55ed7ec0ce1c | -3.05328 | -47.37889 | 2025-08-06 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80a0f2bf-d8e6-3d91-ba13-cff64e2deb50 | -7.18518 | -45.47737 | 2025-08-06 05:10:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 01061a6e-f1f7-3d51-902a-35417f52f213 | 1.69118 | -61.07888 | 2025-08-06 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0c67b692-5699-3bd3-8891-7a835ecc53a2 | -6.68007 | -49.78374 | 2025-08-06 05:10:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62aa68e3-0864-3f30-8e86-e43702037c70 | -6.41528 | -53.37355 | 2025-08-06 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c0ced149-2f11-3392-86f0-94b92c143bb0 | -7.11214 | -44.37073 | 2025-08-06 05:10:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 949c72dc-7480-3d35-9582-1690c1ae548e | -5.67943 | -50.26314 | 2025-08-06 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e254715e-2a43-38a0-93fc-1b80d355bc69 | -5.23666 | -56.06327 | 2025-08-06 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 96402a76-1242-345f-bf5e-bb78fb1139aa | -6.28788 | -45.74281 | 2025-08-06 05:10:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d836c52-247d-3784-8460-b01ae7c1584a | -3.71441 | -53.37414 | 2025-08-06 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3c3919f-18e4-3451-89b0-f82165436f16 | -6.95343 | -50.45798 | 2025-08-06 05:10:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e05ea0a-6d52-39b9-8d8e-4170e8f43542 | -3.05872 | -47.37975 | 2025-08-06 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2ec669a-6195-3adf-8a49-c0dfa49a5ae7 | -3.04079 | -49.43245 | 2025-08-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0fa710a-9036-331e-8d7f-1935d25fb687 | -7.06856 | -44.38562 | 2025-08-06 05:10:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e3e6efff-9cef-3a52-b382-ab1c647f7cfe | -7.63385 | -44.58227 | 2025-08-06 05:10:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d1368bac-d313-33a0-86fb-ca194f52413d | -3.20241 | -49.16814 | 2025-08-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43026e89-d66b-3a64-a0fc-be9d936f579d | -6.94701 | -51.63426 | 2025-08-06 05:10:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51d3338b-829f-3a87-8bf3-074a41559675 | -7.63431 | -44.58071 | 2025-08-06 05:10:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e0fc4326-7435-31aa-8b88-4ef806fb8e7f | -6.41329 | -53.36659 | 2025-08-06 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51fde73f-14c9-3727-aed9-7082f44b545f | -7.57869 | -44.8994 | 2025-08-06 05:10:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1d2aa2ce-a863-394a-8117-80513975410b | -3.23805 | -60.19603 | 2025-08-06 05:10:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e7c0757-36f5-3f7e-ac95-62102f32fd85 | -6.26885 | -53.63121 | 2025-08-06 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5bf1c6c1-ab1c-30aa-864b-62334cc5367f | -6.4236 | -53.36998 | 2025-08-06 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7eea0284-99be-3ae8-a222-1c86a9c80ae3 | 1.68649 | -61.07581 | 2025-08-06 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f04c07e-5f76-33b9-a36c-d88106a7e0c4 | -2.95402 | -51.66076 | 2025-08-06 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README22.md)
