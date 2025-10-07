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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac2e382b-2718-3918-a8ac-1a831f696e29 | -12.36438 | -54.16808 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5db006bb-d83c-32ef-8e0c-0c840a54f02c | -10.19433 | -46.02668 | 2025-10-07 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61b0d9f6-fffd-3e9e-a710-319c13e7b5f5 | -15.36175 | -47.30675 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6e20658-b4bd-339c-b190-1a7d2f5a42db | -8.56331 | -50.08551 | 2025-10-07 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4d18f8e6-eec9-3b91-bf1a-027f85b874f1 | -14.76824 | -46.06921 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3382002a-4562-3e31-99cf-a75ba5407f2b | -12.94671 | -54.72769 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5372563b-f067-3187-8595-f37628f791cd | -11.47726 | -43.49904 | 2025-10-07 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d9503b0-8c4d-3ee9-8bff-730abd9ac53e | -14.51222 | -46.92253 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ef7d6bb3-cd43-3842-8153-089ab9d4db87 | -14.91998 | -46.81298 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9389e7a-617b-3a86-ab20-e56a018894f9 | -10.43151 | -50.288 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5125889b-eb4e-3cc1-98b7-1d040c93f9e7 | -10.39325 | -50.30308 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| c10a4e42-a557-3a4c-9d4a-57421f29d0a9 | -10.26349 | -44.36375 | 2025-10-07 04:57:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bdd97bdb-1388-3f8e-8720-5fe57bd9c617 | -12.238 | -47.02348 | 2025-10-07 04:57:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec002e09-c1ad-3f70-80fa-0804127e78a8 | -14.54002 | -46.6394 | 2025-10-07 04:57:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a7bba9d-e53c-31bb-b642-fc129f6b8a46 | -11.12058 | -47.2205 | 2025-10-07 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8da0d054-52f9-3334-b723-345270906a47 | -10.80683 | -48.59434 | 2025-10-07 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e697b93c-3c95-3a8a-a41f-6f24d3292010 | -14.77041 | -46.0506 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 39b0c10f-9473-3500-8d6f-10cb63d0b743 | -13.01802 | -51.0319 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6fb83668-b307-37f5-81b6-dca4725596be | -9.66237 | -64.72488 | 2025-10-07 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8989a4dd-7e4b-338a-98e0-07a662a88ada | -12.42824 | -54.50249 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65a35321-62c4-30f1-9f78-380479df0aa8 | -15.27373 | -46.33983 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d2ef77f-81ac-3c63-8e44-a87fedcd39a3 | -11.94464 | -51.47824 | 2025-10-07 04:57:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b72debd7-0abd-3053-8a7f-26009c98df1b | -10.80856 | -48.81206 | 2025-10-07 04:57:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dbea1736-7574-3263-bc6c-d3d931ca0b84 | -12.54388 | -48.14452 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aa272225-b016-37ff-b0df-e44dae81bf30 | -7.49253 | -63.67582 | 2025-10-07 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9cd96021-a49d-34a3-a045-423a30054239 | -11.94657 | -46.44065 | 2025-10-07 04:57:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f382a68f-c909-3b97-8a63-5fd409b07445 | -10.36038 | -44.98071 | 2025-10-07 04:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9182426a-7642-38b8-8445-c5d0cb6ce5d5 | -8.8524 | -46.10664 | 2025-10-07 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ad8d05d-ed13-3d15-92f6-7d7fa4d08613 | -9.06127 | -54.51931 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e034ae6b-de3c-3348-bfd8-46ce473de9c1 | -14.76236 | -46.02291 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2dda3c7b-a129-34ae-8aae-3758e566e929 | -12.9234 | -54.72396 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5344589b-802f-3025-aaf9-e5a6e18c47bc | -15.19724 | -56.823 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80916b32-387f-3b9c-8043-1e0bd1377fbb | -17.3489 | -46.83511 | 2025-10-07 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93943fd2-d27f-37e6-80f3-5e9186fdcb83 | -17.16892 | -43.46038 | 2025-10-07 04:59:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c204cb2-31a3-3906-8547-aceac648868f | -21.43299 | -46.67994 | 2025-10-07 04:59:00 | NOAA-20 | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2309bce9-7cad-3b14-9071-577d5a5a58e7 | -18.11153 | -53.34427 | 2025-10-07 04:59:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 85d317c0-8e7f-3fd3-801d-f940426e04b1 | -15.58712 | -52.55553 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fe56aaa5-1eeb-3266-848f-3f8098e38d5f | -20.58187 | -46.30983 | 2025-10-07 04:59:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf3d4b8c-843c-3da4-8656-b91dad3ce56f | -15.60858 | -52.56342 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e9876dee-23b8-329e-a5e8-36989b657727 | -15.1822 | -56.83154 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 62b0771f-382d-3c6e-84ee-62208a581393 | -20.20459 | -43.93045 | 2025-10-07 04:59:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| f9db090e-1cc9-385a-986e-e41aba91a679 | -19.01432 | -49.75457 | 2025-10-07 04:59:00 | NOAA-20 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5af5ea1-db06-382a-a18e-0bb5c87e04e3 | -21.7688 | -47.78569 | 2025-10-07 04:59:00 | NOAA-20 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d372f1bc-6f66-3d06-bc68-76a8cecf2e7a | -15.61165 | -52.56838 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d61c1133-af4e-3d4e-ba44-fff3b95faae4 | -21.18592 | -45.61676 | 2025-10-07 04:59:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f89c3782-84ae-36f0-bfa0-29b37aa3a81b | -15.5908 | -52.5561 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 614f5928-2a49-3d26-ba2c-f19b36c7103b | -21.61146 | -44.0037 | 2025-10-07 04:59:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0ae00560-3fe2-3298-a965-d23cacee6862 | -21.43264 | -46.68377 | 2025-10-07 04:59:00 | NOAA-20 | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ce59a682-7414-3213-9363-b1653a34b3e4 | -18.2864 | -45.41372 | 2025-10-07 04:59:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fec05f51-30e5-3b88-ab9e-44c83dbb2b0a | -16.06151 | -50.9986 | 2025-10-07 04:59:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d77b5a0d-32ab-3a37-84e8-ddd1cac5a580 | -15.57855 | -52.56305 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4d85a938-d517-3b98-96db-c7531eb379d3 | -16.00018 | -50.961 | 2025-10-07 04:59:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a1467cc-f92a-3f37-aba7-79c1f9d9d24a | -15.20779 | -56.82115 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40c196d0-743c-35e4-9f1c-80a4f6b810df | -15.61224 | -52.56413 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 04c84f54-ba55-3b93-9559-a3de4659a39a | -16.3916 | -53.32486 | 2025-10-07 04:59:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 511f286c-f00b-3c9a-bd6e-ff74d55d1dd0 | -15.35069 | -56.92339 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a4643313-2e2d-356b-ae42-8a934c3ca5f9 | -17.71816 | -56.73684 | 2025-10-07 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| dcd8369c-d8ab-3923-b378-e5bdc88bb398 | -17.08802 | -43.3886 | 2025-10-07 04:59:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 81259353-9202-3693-b1e7-ae1a21e0d5b3 | -15.22253 | -56.77189 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d7328e0-e198-355e-acfc-421ab6a65321 | -15.59019 | -52.56046 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ee56fa39-cbea-34b7-afe7-01c0a352d625 | -18.28686 | -45.40898 | 2025-10-07 04:59:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71cecb81-45e5-3496-8783-5d71d30c2d49 | -15.99387 | -59.54029 | 2025-10-07 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8335ce68-41d2-337a-a000-b101e8fc5be1 | -21.18605 | -45.62043 | 2025-10-07 04:59:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7f64c4c3-c7c2-36eb-887b-5af337334ccc | -18.51281 | -43.91407 | 2025-10-07 04:59:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 988ceb6d-3e5e-328c-a774-f1a903d47717 | -20.28293 | -48.51259 | 2025-10-07 04:59:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c1e0e0c-6665-3409-b8a5-961b753f1e6e | -18.51801 | -43.91046 | 2025-10-07 04:59:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8cc92d58-8d41-37c3-b264-467ef7cff3f1 | -21.99945 | -49.7263 | 2025-10-07 04:59:00 | NOAA-20 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 25827169-b83b-325d-9c11-ad4453e04969 | -15.61656 | -52.56016 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 667295cb-ab13-37be-861d-0446c1c599e9 | -19.6399 | -55.73979 | 2025-10-07 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1737a077-c775-3cde-b9f9-34c93bd9ce71 | -18.27528 | -45.46545 | 2025-10-07 04:59:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 63f0707c-3a8f-3a3e-bac3-495ddcae13f7 | -15.98535 | -59.53997 | 2025-10-07 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0b59379-54d5-3bb2-80a3-73ebb9147550 | -18.11515 | -53.34501 | 2025-10-07 04:59:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| cc45fb31-1445-3de8-ab7b-4127c7b3ba32 | -15.99456 | -50.94122 | 2025-10-07 04:59:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6754a50b-8a6b-39eb-849e-0c9729d3139f | -15.61593 | -52.56463 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2107ecd6-e5d7-3f62-b15b-3639e0c59d1d | -18.51137 | -43.91002 | 2025-10-07 04:59:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ffa6a65-42f0-3db0-96ab-ee48c08d420e | -22.00363 | -49.73253 | 2025-10-07 04:59:00 | NOAA-20 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| c9fc0c4b-e310-35ad-b179-17b5c98042d2 | -18.28215 | -45.45737 | 2025-10-07 04:59:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| eb6c0345-58e3-3f3e-98f6-9fd03c89aea0 | -15.58039 | -52.54979 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6cd63b3b-59c5-3f92-9898-f49c9f70d05f | -15.58468 | -52.57308 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 05d9c675-5925-39d6-b30a-6dd95d37595e | -19.63933 | -55.74357 | 2025-10-07 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| bf8613e2-d134-3f47-a7f2-4bf4706ae2a0 | -16.05474 | -50.98719 | 2025-10-07 04:59:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b795974b-3410-3720-bedb-5df05693272f | -18.16124 | -53.36092 | 2025-10-07 04:59:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8df098fd-0776-3699-95be-b9d467c430c2 | -15.9817 | -50.85079 | 2025-10-07 04:59:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 83737657-d24a-319f-9a0f-1196af8079b4 | -16.02317 | -50.97523 | 2025-10-07 04:59:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9030ad4-0043-3ce7-a109-e8832a02f892 | -22.00007 | -49.72063 | 2025-10-07 04:59:00 | NOAA-20 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 3a01aa6e-5c05-3e34-aabd-1638f789954e | -15.20229 | -56.81287 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9e0d58f1-c157-3652-bacf-869110630301 | -17.25361 | -46.93409 | 2025-10-07 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 14aa6f92-23e7-347d-a8b2-8cca5e3a91e6 | -17.54729 | -46.76168 | 2025-10-07 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0812739-da86-3ef2-a067-860b75215c60 | -17.24815 | -46.93391 | 2025-10-07 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1cd1bf5e-487f-3f12-ba1f-74ae968a53af | -15.59634 | -52.57031 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| ef59d6d3-b6ad-3bc7-9597-2952d17d57b1 | -15.2348 | -56.75925 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc876d81-7acd-32e1-a444-e53617f724a7 | -22.00904 | -49.72744 | 2025-10-07 04:59:00 | NOAA-20 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| b1873a37-7917-364d-9e34-f8481b1a0ebd | -21.52163 | -45.59845 | 2025-10-07 04:59:00 | NOAA-20 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 39713ac7-22ee-384b-a5b1-b31e81c05a99 | -16.02126 | -51.05307 | 2025-10-07 04:59:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3057721-d75f-3d4b-8b32-1dc8956a394c | -16.06101 | -51.00237 | 2025-10-07 04:59:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4dc614f9-e9d2-3023-a8e9-9d29fd2c5585 | -16.00576 | -50.82716 | 2025-10-07 04:59:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 50d01415-18f3-3a54-8477-dac2c199a64a | -18.2878 | -45.46176 | 2025-10-07 04:59:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a3ec25f7-c953-398e-9c67-828582ca5db7 | -15.22412 | -56.78323 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d026ac1-5e50-3d6f-8b18-0e130f5c41bf | -15.61103 | -52.57277 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 416cbe14-8fac-3d66-9702-a364dadcfd91 | -20.07777 | -49.6003 | 2025-10-07 04:59:00 | NOAA-20 | RIOLÂNDIA | SÃO PAULO | Brasil | 3544202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |


[Clique aqui para ver as próximas entradas](README101.md)
