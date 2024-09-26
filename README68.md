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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd623be6-9160-36ce-80e1-5582e1e586a1 | -18.36285 | -42.53663 | 2024-09-26 04:08:00 | NOAA-20 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a74f0dfb-788b-373c-a309-458bfee63c7f | -18.32633 | -42.61301 | 2024-09-26 04:08:00 | NOAA-20 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e929cd13-7970-3488-9c08-f5785f3c6053 | -18.32186 | -42.59671 | 2024-09-26 04:08:00 | NOAA-20 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6cdad410-bb1a-3e3b-932e-8ec2c4c27ea1 | -18.27176 | -42.67754 | 2024-09-26 04:08:00 | NOAA-20 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dbdcb99f-7954-3573-9ddb-1a4b5bc7d73e | -18.2712 | -42.6813 | 2024-09-26 04:08:00 | NOAA-20 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 142094c7-638d-31af-aeb0-ac1408785f76 | -18.27065 | -42.685 | 2024-09-26 04:08:00 | NOAA-20 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 05424d18-4004-30ff-a3b8-daf92ab6c7f1 | -18.26896 | -42.67318 | 2024-09-26 04:08:00 | NOAA-20 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 75dd5a7f-fcca-3a42-9500-e22db40818de | -18.26838 | -42.67701 | 2024-09-26 04:08:00 | NOAA-20 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e92da48e-d554-38c7-a8ab-c17e77b6fac9 | -18.26782 | -42.68078 | 2024-09-26 04:08:00 | NOAA-20 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3b507a67-ba0f-31b1-b136-dd4529bbf489 | -18.26727 | -42.68448 | 2024-09-26 04:08:00 | NOAA-20 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7c501726-7c62-3d81-ad3e-15c4c6b631c9 | -18.16014 | -42.60552 | 2024-09-26 04:08:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| da52579c-5f1e-34d3-9d9a-17e4debf7ce9 | -18.15959 | -42.60927 | 2024-09-26 04:08:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7c8b4a35-1fb1-3aab-88f1-687cb7d00982 | -18.15233 | -42.77358 | 2024-09-26 04:08:00 | NOAA-20 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| bea5b194-be52-38e4-a0ee-a2aa1c8093b1 | -19.39966 | -42.99579 | 2024-09-26 04:08:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e44ba0ad-d704-3875-b1ee-cf98f29aff44 | -19.26676 | -42.73336 | 2024-09-26 04:08:00 | NOAA-20 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b9643128-ec2c-39d3-9c18-c1831fa44983 | -19.26452 | -42.72507 | 2024-09-26 04:08:00 | NOAA-20 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d9695741-db77-308e-a8ac-aa514eccebe6 | -19.26394 | -42.72899 | 2024-09-26 04:08:00 | NOAA-20 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 826fcf05-0fcc-3bfb-b211-099ee775df50 | -19.26337 | -42.73278 | 2024-09-26 04:08:00 | NOAA-20 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7f8690f9-f526-3cfe-b916-ebbaec9478ba | -19.26114 | -42.72446 | 2024-09-26 04:08:00 | NOAA-20 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| bce62fd3-d3be-3da1-9117-2526970a5f8c | -19.26056 | -42.72837 | 2024-09-26 04:08:00 | NOAA-20 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 02925916-41aa-3a5c-9f03-34eeb18f3771 | -19.24516 | -42.97086 | 2024-09-26 04:08:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c387f175-c231-34e4-9dcb-d33f31dfa5ba | -19.24459 | -42.97467 | 2024-09-26 04:08:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 11c9c53a-3307-301b-bd6c-727e30fe7c09 | -19.18815 | -42.57994 | 2024-09-26 04:08:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 604ed7ec-4b0d-3c94-a78c-c6f0e990f740 | -19.04811 | -42.72247 | 2024-09-26 04:08:00 | NOAA-20 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e58c18b1-b3bf-36c2-8d35-fb72fe7407ba | -19.04753 | -42.72637 | 2024-09-26 04:08:00 | NOAA-20 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| fd2d54d2-14ec-365f-b285-b4028df0a93a | -19.04695 | -42.73026 | 2024-09-26 04:08:00 | NOAA-20 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 123fb7fb-48d9-3013-8e0f-64ca81ef366b | -19.04415 | -42.72579 | 2024-09-26 04:08:00 | NOAA-20 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 363eefad-1e8d-3f48-bb7a-8e3d76ebd1b6 | -19.00445 | -42.59484 | 2024-09-26 04:08:00 | NOAA-20 | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bbf3a0be-7675-3732-9af6-895a3acc7a53 | -19.00389 | -42.59871 | 2024-09-26 04:08:00 | NOAA-20 | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 79847c52-57da-3367-83db-1ddfce03f41a | -19.0038 | -42.59549 | 2024-09-26 04:08:00 | NOAA-20 | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f08cd3f0-fd1b-37be-901e-1dc03af06c70 | -19.00322 | -42.59935 | 2024-09-26 04:08:00 | NOAA-20 | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 601b5b09-095b-357c-b3c7-e60c2f9892b4 | -20.21128 | -43.43925 | 2024-09-26 04:08:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| fc2d982c-38ad-3fae-ab37-8273a9bdea44 | -20.20792 | -43.43871 | 2024-09-26 04:08:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 2189df9b-d3df-311f-bbdf-60937263202b | -20.14202 | -43.4755 | 2024-09-26 04:08:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 21bed385-3f0a-3df5-b057-4b66ff09b620 | -20.13865 | -43.47511 | 2024-09-26 04:08:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9ac675ca-4533-3e33-942f-391c2b3f92df | -20.13754 | -43.48245 | 2024-09-26 04:08:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5176ba50-a356-34e1-96b0-ad1e8b4341bb | -20.13419 | -43.48195 | 2024-09-26 04:08:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5e4091dc-119e-395d-848e-bd3dc5926792 | -20.12304 | -43.44222 | 2024-09-26 04:08:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| d202608d-145d-3028-83f9-a3a0da1069bb | -20.12246 | -43.44605 | 2024-09-26 04:08:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 6537e1ab-2d41-3393-af9e-e523c45ed578 | -20.11968 | -43.44173 | 2024-09-26 04:08:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 727aa10d-00e3-3b33-9ada-636a8185e7b8 | -20.11911 | -43.44554 | 2024-09-26 04:08:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 0ade7280-2cd1-3171-8189-9d05f84b2f06 | -20.00784 | -43.44075 | 2024-09-26 04:08:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4832d1bf-b258-3226-b3f3-5901367886d9 | -19.99163 | -42.29489 | 2024-09-26 04:08:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 647df2ea-ed3c-3007-84d0-f5d7f986c468 | -19.98761 | -42.3469 | 2024-09-26 04:08:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ae380805-ea4e-35de-866a-b0da5d23e380 | -19.98475 | -42.34235 | 2024-09-26 04:08:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3ab779eb-a409-3663-b7ee-f187940c7b73 | -19.98416 | -42.34638 | 2024-09-26 04:08:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3fec701c-8766-3a2e-8870-eb288798556c | -19.81516 | -41.94305 | 2024-09-26 04:08:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a53ab817-3cb2-36cf-807c-f86a3e357d1a | -19.70522 | -42.38813 | 2024-09-26 04:08:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 127025b8-8810-35b8-918a-4a309646668d | -19.68638 | -42.42136 | 2024-09-26 04:08:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| af670aa9-b8a5-3e1e-9ab1-5521834ed722 | -19.68295 | -42.42081 | 2024-09-26 04:08:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 850fcda0-ffb2-345b-8f17-91e8a04eb020 | -19.68069 | -42.43656 | 2024-09-26 04:08:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b6662ed3-8393-390e-914b-c67e4b7d6596 | -19.68012 | -42.44048 | 2024-09-26 04:08:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5371c01d-7f71-34ca-8d24-d9da17c2ada5 | -19.68002 | -42.42133 | 2024-09-26 04:08:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 161fb238-42c3-3688-9dbc-d71c182fe9d3 | -19.67895 | -42.4242 | 2024-09-26 04:08:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7582cdb2-f911-3698-9eef-b8e2b868885e | -19.6777 | -42.43705 | 2024-09-26 04:08:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| bc44a3e3-fb04-35e7-a9a9-025a50bc38eb | -19.67726 | -42.436 | 2024-09-26 04:08:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4d89971d-fc48-32fc-a960-24dc5e4362c1 | -19.67427 | -42.43649 | 2024-09-26 04:08:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| d2a69624-7585-37e7-a6a5-fa8f15d86e58 | -19.67369 | -42.44042 | 2024-09-26 04:08:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| dd453625-cf4f-3b34-9504-df5a60173fbf | -19.67084 | -42.43594 | 2024-09-26 04:08:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2b562ef6-e346-34af-b5a8-4be5b55424ee | -19.66159 | -42.87792 | 2024-09-26 04:08:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 48360906-dafe-3cb8-ba56-822c22bf2422 | -19.65313 | -42.86478 | 2024-09-26 04:08:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 346fd484-d314-33c0-bbf6-a9e59b2662ad | -19.64409 | -42.83197 | 2024-09-26 04:08:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6bf18830-ceeb-33b1-af4d-b6ea42eb934e | -19.64352 | -42.83584 | 2024-09-26 04:08:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| aed2410e-9513-3fb3-897d-89871ac54dcf | -19.62936 | -42.93203 | 2024-09-26 04:08:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7570e337-a137-36b7-be26-2e6ee8c77eb1 | -19.62147 | -42.93861 | 2024-09-26 04:08:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 580cb5d0-e5b3-3ee0-b2e4-cbca193bc157 | -19.61809 | -42.93807 | 2024-09-26 04:08:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 57e2a775-ce47-3f85-8486-2e23eb64d778 | -19.61679 | -42.80065 | 2024-09-26 04:08:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 3b93eb13-0eee-37a0-950d-e3812c0f2870 | -19.61399 | -42.79616 | 2024-09-26 04:08:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| 694bbc90-08a9-3e74-bc5d-e44854f613f2 | -19.6134 | -42.80015 | 2024-09-26 04:08:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 7e078ea0-87ed-366a-adb3-6c10e53552ae | -19.6128 | -42.80414 | 2024-09-26 04:08:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 6783485c-6372-34de-bda1-7a4d62cac75b | -19.58686 | -42.62656 | 2024-09-26 04:08:00 | NOAA-20 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| c469317e-b67a-38c1-b225-43cb53c9e47b | -19.58347 | -42.62593 | 2024-09-26 04:08:00 | NOAA-20 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 174ef01c-81e3-3b50-9514-09e32e2084c4 | -19.58291 | -42.62971 | 2024-09-26 04:08:00 | NOAA-20 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 648dff44-020d-38a8-bb0d-aff6ee7f8b60 | -19.57952 | -42.62906 | 2024-09-26 04:08:00 | NOAA-20 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ca699d26-c34b-3b2e-ad8d-924bdcf028db | -19.5733 | -42.6 | 2024-09-26 04:08:00 | NOAA-20 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9865dca2-b670-37ae-b5ce-24858390fb17 | -19.56989 | -42.59947 | 2024-09-26 04:08:00 | NOAA-20 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 080dcb35-23a9-30b4-bb30-fd0996170b3f | -19.56822 | -42.6348 | 2024-09-26 04:08:00 | NOAA-20 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 204fe999-7c02-3613-8fb5-986938d2ddf3 | -19.53765 | -42.7011 | 2024-09-26 04:08:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 064a5447-a3c6-3f61-8a09-70b71922ca9d | -19.53708 | -42.70502 | 2024-09-26 04:08:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 753908f3-76e3-3241-9775-d48f9ea656e8 | -20.33573 | -42.61814 | 2024-09-26 04:08:00 | NOAA-20 | SANTO ANTÔNIO DO GRAMA | MINAS GERAIS | Brasil | 3160108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2dda3093-8169-3acb-9b12-7fe13dfb358d | -20.33286 | -42.61375 | 2024-09-26 04:08:00 | NOAA-20 | SANTO ANTÔNIO DO GRAMA | MINAS GERAIS | Brasil | 3160108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7eafad80-5a23-3a08-b019-310d0722d1f4 | -14.56196 | -45.67666 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3439565f-9ad2-348e-9fb2-a754e60a2671 | -13.56396 | -43.45525 | 2024-09-26 04:08:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a68f1b1-1618-3618-b37a-0c6339deb3da | -13.5347 | -42.56128 | 2024-09-26 04:08:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| df94222e-8a39-31c5-bc3b-bbc635e21863 | -13.53138 | -42.56074 | 2024-09-26 04:08:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ab738b0a-a5c3-37d8-9f6a-2d3d57124a00 | -14.44584 | -43.31293 | 2024-09-26 04:08:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 10e82102-1a7c-3fc9-bf50-30c0a6ba2a1f | -14.35922 | -42.34251 | 2024-09-26 04:08:00 | NOAA-20 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| c0ee752b-b888-39e5-be2d-d85c78106790 | -13.79324 | -43.14351 | 2024-09-26 04:08:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a0014208-8afa-3b88-947c-982e3db5c682 | -16.23713 | -43.81912 | 2024-09-26 04:08:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37d8f0e5-24b7-3c48-a2d6-e36617c8c5cc | -16.08215 | -43.66074 | 2024-09-26 04:08:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a7f0f60-dbde-325e-9b82-d614cbbeb6cd | -16.03811 | -43.61666 | 2024-09-26 04:08:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3b9f602-09eb-3b9d-9576-0bc38368179b | -16.03755 | -43.62024 | 2024-09-26 04:08:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9924e41-199c-3ee3-a877-5fe2ef95efbd | -15.779 | -43.55944 | 2024-09-26 04:08:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46e76ea4-d0e7-3129-8c38-25515c4e7ff1 | -17.96835 | -43.5168 | 2024-09-26 04:08:00 | NOAA-20 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60cd835d-8e9a-3620-9fe5-2d3a225ab35a | -17.96779 | -43.52042 | 2024-09-26 04:08:00 | NOAA-20 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0690c9fd-26ad-3744-ab38-30ac6ca4f17b | -17.92848 | -44.27033 | 2024-09-26 04:08:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab877db9-73ff-3d67-ae7f-1834e64b062a | -17.92517 | -44.26976 | 2024-09-26 04:08:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59f899a3-e8af-3e9d-a768-4f12eb922ac9 | -17.9246 | -44.27337 | 2024-09-26 04:08:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f199f905-1e6e-32e2-b9a0-72589008b8a1 | -17.90622 | -44.19609 | 2024-09-26 04:08:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc8715cf-4bca-3c01-9036-166a927dbb83 | -17.90565 | -44.1997 | 2024-09-26 04:08:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README69.md)
