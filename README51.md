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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 775b1132-9dd8-3ff1-a8f0-53c1020602da | -23.21935 | -49.35983 | 2025-09-14 04:44:00 | NOAA-21 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| fb0513d5-7962-3e4a-8661-aa6c2b14e0f3 | -23.45622 | -51.83885 | 2025-09-14 04:44:00 | NOAA-21 | MARIALVA | PARANÁ | Brasil | 4114807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d568e462-9661-3844-b017-ff4a691db840 | -20.08861 | -46.90103 | 2025-09-14 04:44:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84b18591-3eb9-3780-96c4-969755143e28 | -21.58918 | -46.79887 | 2025-09-14 04:44:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 00642bf4-289b-32d9-9a96-1acc3ef559ce | -23.16991 | -47.5667 | 2025-09-14 04:44:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 69ef9c9e-93a1-3fad-a1ed-3312d85d4e60 | -23.47951 | -50.84813 | 2025-09-14 04:44:00 | NOAA-21 | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 8828998a-18a3-306b-8760-66446b7dc4b8 | -21.9223 | -46.5545 | 2025-09-14 04:44:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| b39540e7-00f9-3ff2-96c2-1ce588647e11 | -22.19533 | -49.60532 | 2025-09-14 04:44:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2f20fa30-c029-3bb5-9ea0-0302419707b6 | -26.63086 | -51.81246 | 2025-09-14 04:44:00 | NOAA-21 | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| afde9aed-7089-3f24-b170-91fa974f6d0a | -21.07909 | -47.11009 | 2025-09-14 04:44:00 | NOAA-21 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 30fffa29-3f56-38be-b4fb-146f0e866a0f | -21.12473 | -45.95253 | 2025-09-14 04:44:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 67fbec4f-2fb1-3ef5-b021-8cc448483bfe | -24.76593 | -51.75348 | 2025-09-14 04:44:00 | NOAA-21 | PITANGA | PARANÁ | Brasil | 4119608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 34065c4c-27c3-337a-b4f9-b86b08682aba | -23.5559 | -51.55794 | 2025-09-14 04:44:00 | NOAA-21 | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9be11601-62a9-34d6-b716-c02a8bb0913d | -20.44631 | -45.23978 | 2025-09-14 04:44:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f7a6a95d-2676-3da8-a68b-518c734a553d | -22.72785 | -49.88947 | 2025-09-14 04:44:00 | NOAA-21 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3b806d2c-d0ad-3ec8-8608-3cc1ba675dbb | -23.74438 | -54.53081 | 2025-09-14 04:44:00 | NOAA-21 | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 22b8b085-78b2-37be-8f06-10597e813a4d | -22.39799 | -47.59114 | 2025-09-14 04:44:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6600b96f-ab86-329e-966f-a6d139571ff8 | -22.29639 | -47.95455 | 2025-09-14 04:44:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce41c9e5-e43d-3681-949e-4fddf511112c | -22.73453 | -49.89518 | 2025-09-14 04:44:00 | NOAA-21 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f906614-d2cb-30aa-b9af-cba4ec162584 | -23.16108 | -47.56962 | 2025-09-14 04:44:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6a6beaab-174c-35b4-a76e-cb0788049eda | -22.03179 | -55.87624 | 2025-09-14 04:44:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5c0b3436-78b8-3087-b271-9ef98cdec639 | -23.27741 | -51.02816 | 2025-09-14 04:44:00 | NOAA-21 | IBIPORÃ | PARANÁ | Brasil | 4109807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| cdef95db-52d3-3fe6-81a1-3812efdd6c7c | -20.72549 | -56.74256 | 2025-09-14 04:44:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77fd45c1-daa5-3492-92d8-c8956f86f82f | -21.59246 | -46.80793 | 2025-09-14 04:44:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2044f444-e02a-3f04-bcb9-3ff0f16fbcf1 | -20.09473 | -46.88613 | 2025-09-14 04:44:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a844d1e-16ee-3091-9ed9-23ee3ab7284a | -22.73512 | -49.89062 | 2025-09-14 04:44:00 | NOAA-21 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5130e5af-d139-3678-b22a-c1134c272607 | -22.73443 | -49.89307 | 2025-09-14 04:44:00 | NOAA-21 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 501b1592-d0b4-3f44-9ba5-26afddacf5c1 | -23.48244 | -50.85303 | 2025-09-14 04:44:00 | NOAA-21 | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| edbcaef3-0b9a-3a97-b208-a73bfe57dbc9 | -22.73816 | -49.89577 | 2025-09-14 04:44:00 | NOAA-21 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fccf0d95-2888-39f1-ac8d-35d9fc1fef59 | -20.64593 | -48.6932 | 2025-09-14 04:44:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbc66ab3-a116-32ca-b3e5-40ca9d535d97 | -21.6519 | -50.20288 | 2025-09-14 04:44:00 | NOAA-21 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ed7f0ead-29e6-37d7-8c49-e814dee40546 | -25.10378 | -50.11892 | 2025-09-14 04:44:00 | NOAA-21 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 79e3aea7-0b34-3afa-acff-f50fe363d38f | -22.02975 | -55.87471 | 2025-09-14 04:44:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49078a0a-7cad-3134-b8ce-376e56a0cf56 | -21.59336 | -50.97149 | 2025-09-14 04:44:00 | NOAA-21 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| de97ee96-737d-3136-9166-9f94569a63f7 | -21.76967 | -45.45909 | 2025-09-14 04:44:00 | NOAA-21 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 1dd725a1-d33a-3a81-a97c-79c33554ba7f | -23.476 | -50.84753 | 2025-09-14 04:44:00 | NOAA-21 | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 55836559-1721-3297-9c0b-b06a72981799 | -22.20704 | -48.34929 | 2025-09-14 04:44:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 276e7ee8-8498-3bd2-9896-a87765d22d4a | -21.91792 | -46.55397 | 2025-09-14 04:44:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 7dbb043d-8301-370a-9cc3-2032b8533bd2 | -22.19106 | -49.60922 | 2025-09-14 04:44:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 02651621-fbef-3000-aa7e-ddcf4b276a29 | -22.7308 | -49.89248 | 2025-09-14 04:44:00 | NOAA-21 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2b449ee4-d08a-36ab-b734-481996d64fbe | -23.13855 | -49.65696 | 2025-09-14 04:44:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0a1833ff-4361-3393-b272-f6287d8c4158 | -20.09145 | -46.88768 | 2025-09-14 04:44:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5707382b-bdd8-36a1-ace6-a04e9a90f75e | -21.6252 | -46.81212 | 2025-09-14 04:44:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5845725d-66be-321b-9599-5bdd608282f4 | -20.45101 | -45.2402 | 2025-09-14 04:44:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 52152f39-bbaf-3a78-b23c-a6f6069f3230 | -25.00946 | -50.07238 | 2025-09-14 04:44:00 | NOAA-21 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 65905c54-b70a-3dbb-a8d1-2a61134d8a3a | -25.08587 | -50.91625 | 2025-09-14 04:44:00 | NOAA-21 | GUAMIRANGA | PARANÁ | Brasil | 4108957 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 542ff9e8-22d0-3d69-b34f-f2ca3a73f2af | -21.42083 | -46.60721 | 2025-09-14 04:44:00 | NOAA-21 | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f6a7dd86-4f6d-3074-9e6b-8058becca89b | -23.23569 | -51.04671 | 2025-09-14 04:44:00 | NOAA-21 | IBIPORÃ | PARANÁ | Brasil | 4109807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6347979a-0fd7-34cd-ba74-01aa4496ec35 | -21.76822 | -45.45267 | 2025-09-14 04:44:00 | NOAA-21 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2b34791e-3ec1-3819-b1b6-43ee11fae99f | -21.66073 | -50.11211 | 2025-09-14 04:44:00 | NOAA-21 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 397fb0de-8eba-391f-97ec-400904a0ef4f | -22.6592 | -53.10829 | 2025-09-14 04:44:00 | NOAA-21 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8f836f9b-011d-3a53-9cc9-e2804f90e89c | -20.08445 | -46.90028 | 2025-09-14 04:44:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ab30a08-422b-3a8b-ac36-38ef974504f2 | -20.84558 | -56.89515 | 2025-09-14 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1f516c4d-d42b-332f-96ea-12c199987945 | -21.77023 | -45.45374 | 2025-09-14 04:44:00 | NOAA-21 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 29c1bb0f-d26f-33fe-8da5-3e17e77514eb | -22.29683 | -47.95094 | 2025-09-14 04:44:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 77f0c94b-967c-3a26-8b70-ea690f20a01f | -22.28786 | -46.37039 | 2025-09-14 04:44:00 | NOAA-21 | OURO FINO | MINAS GERAIS | Brasil | 3146008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 17c798d9-e6d2-3b64-a115-a841314ce798 | -22.17888 | -49.61639 | 2025-09-14 04:44:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| 670d465c-963f-3e6c-ac42-485129c3cdb1 | -22.49536 | -47.41251 | 2025-09-14 04:44:00 | NOAA-21 | CORDEIRÓPOLIS | SÃO PAULO | Brasil | 3512407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2249cfe0-d72b-356a-84b4-ae10b7ae13cd | -22.61692 | -47.66412 | 2025-09-14 04:44:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9de950cc-721c-302a-99f9-d1380552e8a5 | -22.17522 | -49.61581 | 2025-09-14 04:44:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| df8e3b70-6e10-3f03-a2aa-e6a1e5b713ad | -20.25308 | -47.7961 | 2025-09-14 04:44:00 | NOAA-21 | BURITIZAL | SÃO PAULO | Brasil | 3508207 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 40354561-68ae-3149-add6-441153f024c9 | -22.52066 | -52.99221 | 2025-09-14 04:44:00 | NOAA-21 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2873182c-16c5-3091-b149-41815e2c043f | -23.17456 | -47.56318 | 2025-09-14 04:44:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5c622eb4-ec7d-3f71-b838-eb556e44593e | -22.17949 | -49.61184 | 2025-09-14 04:44:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6317282c-8921-38f2-8ba3-839838e182b1 | -24.07997 | -51.0704 | 2025-09-14 04:44:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| df5e640d-744b-37bf-9c27-b3469738fee2 | -22.6674 | -53.12126 | 2025-09-14 04:44:00 | NOAA-21 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 440b3849-ca15-3b80-9901-45fdeafa44a6 | -20.7632 | -56.94772 | 2025-09-14 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5c4ce8e8-1818-333b-b6e3-814f95497b5f | -21.64481 | -50.20176 | 2025-09-14 04:44:00 | NOAA-21 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e0dd52e5-4437-328c-afcd-3c651c32c057 | -21.3033 | -48.55431 | 2025-09-14 04:44:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f17ec5a5-702b-39bf-9d30-c179805d1698 | -20.84188 | -56.89443 | 2025-09-14 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a9b9aeb6-c8cb-3b74-b748-cbd087fd22d8 | -21.86512 | -47.3239 | 2025-09-14 04:44:00 | NOAA-21 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ab7e0fde-ba9a-3c43-ba09-f905e48342ae | -22.66136 | -53.11634 | 2025-09-14 04:44:00 | NOAA-21 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0876c237-6dff-3a61-92a7-ecb011adb285 | -21.66014 | -50.11646 | 2025-09-14 04:44:00 | NOAA-21 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f77bdbd9-fdbc-3b9d-bdaf-ebb2bd9ba694 | -22.78801 | -46.7966 | 2025-09-14 04:44:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1798dafe-fa68-30e2-a726-c4e11bbf78e3 | -23.14746 | -50.3998 | 2025-09-14 04:44:00 | NOAA-21 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0b3fd76b-362d-3ef8-880a-995fbc35f3d4 | -23.16014 | -47.57773 | 2025-09-14 04:44:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3dca9b97-f7e9-3cf2-9d03-132d03eb48c4 | -20.78748 | -56.96226 | 2025-09-14 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1481e12a-299a-38c1-814e-eb40e2ace24a | -22.22579 | -48.61005 | 2025-09-14 04:44:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 3391e9c3-4bb2-3aca-8d27-9c99b501c100 | -20.7218 | -56.74191 | 2025-09-14 04:44:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f87e1286-27f7-34b7-b761-ad86e84abd2c | -22.73149 | -49.89004 | 2025-09-14 04:44:00 | NOAA-21 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 103f4f2d-3b27-32d1-8d6f-f25570752314 | -22.04868 | -47.40894 | 2025-09-14 04:44:00 | NOAA-21 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 71b304f8-473d-308b-a701-d7f791b0c493 | -21.06396 | -47.84744 | 2025-09-14 04:44:00 | NOAA-21 | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95358218-3f4a-332e-b16f-49c8385ac19f | -22.20312 | -48.34862 | 2025-09-14 04:44:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e2dbf2c4-1d89-3b2b-8c63-ff9d30e9bb07 | -21.60841 | -46.82025 | 2025-09-14 04:44:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a6dd1ce0-2539-371f-a316-949010e8f7d1 | -22.54255 | -55.68392 | 2025-09-14 04:44:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ca38b9a-c2cd-3f4f-a191-0d4fb308ada6 | -21.65421 | -50.10665 | 2025-09-14 04:44:00 | NOAA-21 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0b63ea65-e7ba-3070-b858-4e98d3f44d03 | -20.12679 | -46.87674 | 2025-09-14 04:44:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5fc20017-09b2-3905-971f-b5e61e16bb77 | -20.25375 | -47.79079 | 2025-09-14 04:44:00 | NOAA-21 | BURITIZAL | SÃO PAULO | Brasil | 3508207 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 19b50330-bfd0-3378-9592-9f2d5e846e50 | -21.65539 | -50.12459 | 2025-09-14 04:44:00 | NOAA-21 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| fa9b6d21-b701-315f-b1a2-a8417fdb85d1 | -21.65598 | -50.12025 | 2025-09-14 04:44:00 | NOAA-21 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 3c1badb1-bfd5-3e51-b835-8c9775b429d1 | -22.34962 | -49.11165 | 2025-09-14 04:44:00 | NOAA-21 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17f744ef-e195-38f7-ba83-0a8516b1eab5 | -20.09424 | -46.89007 | 2025-09-14 04:44:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54dfd381-56b8-3cd3-a965-515badb56014 | -22.20243 | -48.35423 | 2025-09-14 04:44:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e95ffd95-bc25-39b2-aca4-4c5ff389ce50 | -20.08911 | -46.89703 | 2025-09-14 04:44:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a41b00dc-0a3e-3c7a-83f9-e012b4631587 | -22.72667 | -49.89852 | 2025-09-14 04:44:00 | NOAA-21 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 49b63cef-b49e-3844-87f1-0623fcc5c1c7 | -20.45042 | -45.24544 | 2025-09-14 04:44:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a13d5fb4-e327-35dc-97ab-e76f39a39eac | -22.52283 | -53.00025 | 2025-09-14 04:44:00 | NOAA-21 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 23c80ebb-5e4d-3494-8935-a525aa29a1ac | -21.41956 | -46.60506 | 2025-09-14 04:44:00 | NOAA-21 | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7caa79e3-39a3-3814-97b1-1a03765e0807 | -22.80261 | -47.8055 | 2025-09-14 04:44:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1ae2022c-1588-354f-b314-a5fb052d7591 | -22.67013 | -53.12558 | 2025-09-14 04:44:00 | NOAA-21 | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |


[Clique aqui para ver as próximas entradas](README52.md)
