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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efa019fa-fe08-31ad-96d2-320b97f29ae0 | -8.78815 | -44.84016 | 2026-05-07 12:00:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 63.3 |
| c1a9556a-0b69-3492-ae57-1e484883da28 | -11.77659 | -47.09066 | 2026-05-07 12:00:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 5706acd1-d501-3d7c-96fa-f3521ccfc56f | -12.14872 | -46.66002 | 2026-05-07 12:00:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 1e4365b6-726a-3d58-8d44-bcf98b505680 | -10.56712 | -47.04536 | 2026-05-07 12:00:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 7abbc0e0-f03f-35aa-81f4-1fbc57bfd1fa | -6.12041 | -44.69949 | 2026-05-07 12:00:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 3d0cf0a2-6c00-390d-973f-6555eeb5a89c | -8.77977 | -44.82794 | 2026-05-07 12:00:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7ee9e3f9-4407-371b-99fd-ee7f14537ba2 | -13.96012 | -47.5467 | 2026-05-07 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0dcf1706-30b4-3d9d-b3fa-d8cbfb9807aa | -9.46848 | -46.13781 | 2026-05-07 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 5badd357-9846-34db-9078-adf8513c6a62 | -8.67928 | -49.09128 | 2026-05-07 12:00:00 | TERRA_M-T | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| a00d3937-d11d-3e8e-90c1-db09e2b0b5d9 | -6.90595 | -42.83684 | 2026-05-07 12:00:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 32.7 |
| 719f7534-92bb-3002-8908-d697d3bbf73c | -14.13857 | -45.35116 | 2026-05-07 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 46.7 |
| dd10914b-4dfb-392e-8267-1d60f7ae4244 | -11.54713 | -42.17067 | 2026-05-07 12:00:00 | TERRA_M-T | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 41.4 |
| a236b162-a489-35fe-a7a3-5625615cf721 | -12.14737 | -46.66989 | 2026-05-07 12:00:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| cf3d503d-ea87-3c52-b677-40dda395bc5b | -11.7753 | -47.10007 | 2026-05-07 12:00:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 18f9d419-b629-3310-bd2e-3433772552a6 | -13.60287 | -47.86866 | 2026-05-07 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 24.4 |
| c92f5e42-bdea-3c15-b500-2cde75e3c89d | -12.38223 | -47.17337 | 2026-05-07 12:00:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 79707b1a-7a7e-3a5e-bdaf-24d256a3c77a | -10.5782 | -47.03438 | 2026-05-07 12:00:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c2303dbc-3f7b-3eb6-818d-453cf891e21f | -12.79129 | -44.82214 | 2026-05-07 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 011f1d39-9ecb-3dec-97cd-e350ea6ef91b | -6.90403 | -42.85094 | 2026-05-07 12:00:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 96099181-6a4f-3332-b670-a076079496b3 | -14.14881 | -45.35251 | 2026-05-07 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2b03c391-2e26-3824-8fa4-88b1c11fe68c | -14.15038 | -45.34014 | 2026-05-07 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c789905e-c8c7-3c8f-b74f-e9d860c44f04 | -10.56842 | -47.03609 | 2026-05-07 12:00:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 33.1 |
| d901aaa3-128b-3116-aec3-ae8793e13acc | -8.63258 | -49.53801 | 2026-05-07 12:00:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 533386f6-8ff2-37e7-8d8d-866c31ac1182 | -8.17097 | -43.16719 | 2026-05-07 12:00:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| dac3ff89-3027-3096-9b75-54e364f1bf6a | -9.55427 | -48.6587 | 2026-05-07 12:00:00 | TERRA_M-T | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 07a9942d-ef10-3f3c-8579-690b369d6184 | -8.68063 | -49.08201 | 2026-05-07 12:00:00 | TERRA_M-T | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f2310bb0-9bb7-31bd-8390-3aa33b309d44 | -8.53042 | -44.32526 | 2026-05-07 12:00:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 33009e83-e64e-3fc0-bb66-48a39dfea0a8 | -8.63118 | -49.54762 | 2026-05-07 12:00:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 5b0967f6-5d62-36fe-a797-dd5503dc9f21 | -6.11899 | -44.70993 | 2026-05-07 12:00:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3cd033b3-5309-3955-9c1f-8fcfa8080343 | -9.45925 | -46.13662 | 2026-05-07 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| a2361e19-d878-368f-b670-6d7cdb0aae51 | -6.90675 | -42.84307 | 2026-05-07 12:00:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 41.4 |
| 119ab1ec-d9fb-3a6e-afdb-be6d335fa756 | -14.14014 | -45.33881 | 2026-05-07 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 28b0d909-4642-363f-8b07-7e670d9d95af | -8.78962 | -44.82922 | 2026-05-07 12:00:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 48.4 |
| bf140bf2-1e12-3852-8380-14b943cd0c67 | -13.60415 | -47.85939 | 2026-05-07 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 462def40-ce25-373b-a665-b3d2fbb953f2 | -18.78306 | -51.93636 | 2026-05-07 12:02:00 | TERRA_M-T | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2e8c1cbc-bae9-3b6b-9ad8-c3ea9a676e3a | -18.7846 | -51.92623 | 2026-05-07 12:02:00 | TERRA_M-T | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 5b163bb4-9741-37ec-9290-b31bc2609604 | -14.68764 | -46.15934 | 2026-05-07 12:02:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e778cf7d-0fe6-3287-bf74-751cc1c4f374 | -20.49081 | -50.43027 | 2026-05-07 12:02:00 | TERRA_M-T | SÃO JOÃO DE IRACEMA | SÃO PAULO | Brasil | 3549250 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| dc9843f8-134d-3546-8c4f-d12652d891f7 | -17.59383 | -44.5969 | 2026-05-07 12:02:00 | TERRA_M-T | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b2bcf5d6-beda-3ee0-9f9b-38283b9e4446 | -20.48946 | -50.43966 | 2026-05-07 12:02:00 | TERRA_M-T | SÃO JOÃO DE IRACEMA | SÃO PAULO | Brasil | 3549250 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 2bd2dba8-93fe-3bda-ae0e-65746fcb20ca | -26.7046 | -50.90352 | 2026-05-07 12:04:00 | TERRA_M-T | CAÇADOR | SANTA CATARINA | Brasil | 4203006 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 7edbc7e9-5e1d-3b5b-914c-a344c9ce5183 | -22.91955 | -48.67809 | 2026-05-07 12:04:00 | TERRA_M-T | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 33.0 |
| d5e1ff82-6c2c-3f88-9ea0-39ce3d7b08db | -22.98499 | -51.54158 | 2026-05-07 12:04:00 | TERRA_M-T | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 4c5208c8-8c05-3696-a59a-76cf3f6ac447 | -22.91817 | -48.68879 | 2026-05-07 12:04:00 | TERRA_M-T | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 4dc87682-e038-3e6c-a402-acc6804bd55f | -12.1586 | -46.6546 | 2026-05-07 12:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 20d96a89-6081-3075-a6a6-38834d847d1d | -12.1394 | -46.6573 | 2026-05-07 12:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 94fd2693-9a8a-3a2c-9dec-7a780a40407c | -12.1582 | -46.6772 | 2026-05-07 12:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| dfb59f4f-405a-3b7f-844f-ef5a60680783 | -8.7841 | -44.8315 | 2026-05-07 12:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 99.0 |
| e147ae19-c3b8-3f8d-81dd-a070103de388 | -12.1586 | -46.6546 | 2026-05-07 12:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 01656a87-32ae-33f2-bc7a-7056fb958552 | -8.7841 | -44.8315 | 2026-05-07 12:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |
| a513ebce-aec2-348e-8acb-76d5bdf63f86 | -12.1582 | -46.6772 | 2026-05-07 12:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| c6f8e457-72c8-3d2e-af48-1de455431d29 | -8.7841 | -44.8315 | 2026-05-07 12:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 45180cb3-5097-3a0d-ae12-f427920802d3 | -12.1586 | -46.6546 | 2026-05-07 12:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 79921c95-db9b-36f4-81c3-05dadf24a64e | -12.1582 | -46.6772 | 2026-05-07 12:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 7a338a01-5746-3699-bb0b-81d30f058ee5 | -12.1586 | -46.6546 | 2026-05-07 12:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 3dd727e8-444e-372c-86ad-e339d1c66af6 | -8.7841 | -44.8315 | 2026-05-07 12:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 78.3 |
| a2a2dd8e-9092-3623-90cc-5ed88d58217f | -8.7841 | -44.8315 | 2026-05-07 12:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 9e80c5cd-fcbc-345b-a27f-1fb6d20786f4 | -12.1586 | -46.6546 | 2026-05-07 12:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 838c93c1-5619-3f14-b2f0-ce2b0ae55ba3 | -10.5701 | -47.0433 | 2026-05-07 12:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 9a43a938-d9b3-395a-8168-25b73a0bd891 | -12.3508 | -50.0266 | 2026-05-07 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 8849c496-e09b-3c59-b39f-7c1e9e3ba2cf | -8.7841 | -44.8315 | 2026-05-07 13:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| bad1f4bb-e6e7-3888-bf12-5ffc4955191a | -10.5701 | -47.0433 | 2026-05-07 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 4e2ddec1-1f44-321a-8eff-41f8086ab9a2 | -12.3508 | -50.0266 | 2026-05-07 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 123.5 |
| d5f1aa7d-55e5-376a-b9c6-b00ae57298b8 | -12.3512 | -50.005 | 2026-05-07 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 9da20a87-2535-389b-80aa-8b859ecf675c | -8.7841 | -44.8315 | 2026-05-07 13:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 74.5 |
| d1f92fed-2542-30f1-8e2a-c652b4ef798b | -14.1507 | -45.331 | 2026-05-07 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 33d41eb1-6d66-3a6d-a245-1d6b317a857a | -12.1586 | -46.6546 | 2026-05-07 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 92027650-2402-3268-a715-431b947ddb3a | -12.3508 | -50.0266 | 2026-05-07 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| d3dea191-1cf9-3702-90cd-afe4027d078d | -14.1312 | -45.3344 | 2026-05-07 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 72b1094e-6321-3921-b5ed-0f54befc6459 | -12.3512 | -50.005 | 2026-05-07 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 0814d96e-d19f-3e3b-b707-3f6adc34bff6 | -12.3512 | -50.005 | 2026-05-07 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 01093389-42b7-3689-b083-00917936edad | -12.3508 | -50.0266 | 2026-05-07 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| fb34f4fb-7079-3ed3-bd3a-1ad6ae426f14 | -14.1312 | -45.3344 | 2026-05-07 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| d43450dd-de69-3a2e-b665-192778785518 | -10.9273 | -49.8488 | 2026-05-07 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| ad471ab6-435d-32bb-b2a3-66459a42a450 | -10.5701 | -47.0433 | 2026-05-07 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| dd91e7d4-da56-39d4-9bd7-516e46425425 | -14.1507 | -45.331 | 2026-05-07 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 79.8 |
| d9ea9356-206b-3eda-802d-005d441cbf5b | -12.1586 | -46.6546 | 2026-05-07 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 196dca3e-8378-3f9b-b039-d7ef838f8c30 | -12.3512 | -50.005 | 2026-05-07 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| b59000a3-2415-34fe-b654-adda7c9cad86 | -14.1307 | -45.3577 | 2026-05-07 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 354e1a20-eb05-3977-889a-fefa74044d47 | -12.3508 | -50.0266 | 2026-05-07 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 762d184b-ac8a-3b9b-85d9-0c01f5b3adca | -14.1507 | -45.331 | 2026-05-07 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 2b655fe0-68aa-3ade-b77b-934e4e490121 | -10.5701 | -47.0433 | 2026-05-07 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 7da08927-e233-304f-9769-ec59796ba000 | -10.9273 | -49.8488 | 2026-05-07 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 787f582c-f699-3128-bc98-500615124784 | -8.7841 | -44.8315 | 2026-05-07 13:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 0a18fe36-bc02-3c7d-b030-228e9b718e0a | -14.1312 | -45.3344 | 2026-05-07 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 939fe800-2426-3285-996a-7d6de1c651b0 | -10.5701 | -47.0433 | 2026-05-07 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 121.7 |
| aaadee2e-eb47-3301-9980-386596f6b2ec | -14.1307 | -45.3577 | 2026-05-07 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 446bc91b-2078-3fc6-a355-7259383bff0f | -14.1312 | -45.3344 | 2026-05-07 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 00430dc1-3804-3325-ba55-4af996e3c06e | -12.3508 | -50.0266 | 2026-05-07 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 123.9 |
| b0300abe-3407-340f-b96f-80924de14ff1 | -8.7841 | -44.8315 | 2026-05-07 13:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 4a5ddb2a-d61d-39a9-85a6-55f1234c4e4c | -14.1507 | -45.331 | 2026-05-07 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| c21421bc-d1d2-3f9d-bfd1-72f46b144c16 | -12.3512 | -50.005 | 2026-05-07 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 6c330a88-2f75-3320-b72a-64449ca35edc | -10.5697 | -47.0657 | 2026-05-07 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 8017b37b-86e9-39b7-b149-3f7ad9d19877 | -12.3512 | -50.005 | 2026-05-07 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 2a831810-cb61-378b-922d-cdac1ab3a56a | -10.7774 | -49.7362 | 2026-05-07 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| b63282dd-e68a-3b00-b060-914c9a14aa10 | -14.1307 | -45.3577 | 2026-05-07 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 32c8c688-0b6b-3260-9a4a-23db91191756 | -12.3508 | -50.0266 | 2026-05-07 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 322ef3e2-9c2c-3806-b707-37cd5f8e8a32 | -9.4655 | -46.1415 | 2026-05-07 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 0c21fa12-dc96-34cb-9cc8-0d8fb356a5df | -8.7841 | -44.8315 | 2026-05-07 13:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 10c42d3f-6f69-3a1e-a057-9a0d3b38f284 | -14.1312 | -45.3344 | 2026-05-07 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |


[Clique aqui para ver as próximas entradas](README10.md)
