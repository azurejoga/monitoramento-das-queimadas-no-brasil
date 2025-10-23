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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42a4910f-8e3b-3bc1-989c-f46f7f2fd210 | -3.35236 | -40.42459 | 2025-10-23 03:15:00 | NOAA-20 | SENADOR SÁ | CEARÁ | Brasil | 2312809 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0f7225c2-75ec-3b2b-92c0-f7408cc565e2 | -6.30719 | -41.8852 | 2025-10-23 03:15:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0dc8064a-318f-3418-8dc5-d0264135cce8 | -3.34482 | -40.42913 | 2025-10-23 03:15:00 | NOAA-20 | SENADOR SÁ | CEARÁ | Brasil | 2312809 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 80b8fc7d-8f63-3bea-aa54-7ec4d37f893a | -4.71046 | -40.58985 | 2025-10-23 03:15:00 | NOAA-20 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4d123bd4-00fe-3967-86c8-a81c6893bd42 | -6.99241 | -38.05416 | 2025-10-23 03:15:00 | NOAA-20 | COREMAS | PARAÍBA | Brasil | 2504801 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f2327699-fa17-3515-8f85-93fcf4be58dc | -7.62876 | -42.20473 | 2025-10-23 03:15:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 47cf635a-b977-35b7-8cce-c11b978fbb27 | -6.30083 | -41.88389 | 2025-10-23 03:15:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 0c45681f-f1d7-3e54-8530-6822c6905d2d | -5.79243 | -35.59983 | 2025-10-23 03:15:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7d563d9d-70d5-3984-be15-5dadd9ee55d6 | -3.35054 | -40.42515 | 2025-10-23 03:15:00 | NOAA-20 | SENADOR SÁ | CEARÁ | Brasil | 2312809 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1436ef7a-e2a8-3971-9c7b-5e2d8b827de4 | -6.99183 | -38.05752 | 2025-10-23 03:15:00 | NOAA-20 | COREMAS | PARAÍBA | Brasil | 2504801 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6887c2da-4972-300a-9cc7-6f53f70209cc | -3.35139 | -40.43032 | 2025-10-23 03:15:00 | NOAA-20 | SENADOR SÁ | CEARÁ | Brasil | 2312809 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 631d482d-dab6-3741-86cf-27a373d70350 | -3.34953 | -40.43085 | 2025-10-23 03:15:00 | NOAA-20 | SENADOR SÁ | CEARÁ | Brasil | 2312809 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ab8fcfb9-6340-3f99-8c92-8db76a465219 | -6.30763 | -41.88535 | 2025-10-23 03:15:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2d5e3464-f96c-3ead-9bf0-6320e27b36c8 | -7.62997 | -42.19858 | 2025-10-23 03:15:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d29c2ae8-e3d4-3c29-a505-b815a8284465 | -6.30039 | -41.8837 | 2025-10-23 03:15:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 94efec9d-03e6-3ab9-9cdf-fe12fee92cd4 | -9.4517 | -40.39533 | 2025-10-23 03:15:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| abf60c72-73b3-3583-bf4a-dd593a55bf96 | -6.29926 | -41.88984 | 2025-10-23 03:15:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 08c58b9e-8f25-336f-b53b-b3cb06be5bc0 | -6.99183 | -38.05751 | 2025-10-23 03:15:00 | NOAA-20 | COREMAS | PARAÍBA | Brasil | 2504801 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 14964446-a5d7-3bab-bde7-584d24ce6c20 | -6.30039 | -41.88369 | 2025-10-23 03:15:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 74670b78-f349-3b94-a832-7caa5dd1737a | -3.34482 | -40.42912 | 2025-10-23 03:15:00 | NOAA-20 | SENADOR SÁ | CEARÁ | Brasil | 2312809 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 80454487-9bda-3b19-92c4-f1dcb548e463 | -6.30719 | -41.88519 | 2025-10-23 03:15:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 117ac41e-5a98-35ba-a9f4-68064409827e | -9.4517 | -40.39532 | 2025-10-23 03:15:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d9be4336-8150-3bc5-8c40-605f2708b819 | -3.35236 | -40.42458 | 2025-10-23 03:15:00 | NOAA-20 | SENADOR SÁ | CEARÁ | Brasil | 2312809 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 19868018-9cf7-3779-8a80-adda0d69275d | -6.30083 | -41.88388 | 2025-10-23 03:15:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 7aa4d13e-cfc3-370c-874d-5d214a74be8a | -14.21068 | -44.52535 | 2025-10-23 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 591e784a-dabf-3937-a6f0-597ecff18dff | -14.20385 | -44.52322 | 2025-10-23 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be18ce29-d3b2-3300-bdc7-d952c42fbf24 | -14.20857 | -44.5265 | 2025-10-23 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f72c7efe-43a4-31c7-9eea-91faa9c49b55 | -19.95639 | -45.60258 | 2025-10-23 03:19:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4301f12-62d7-3a03-a921-9671b88ceeb1 | -19.95497 | -45.60845 | 2025-10-23 03:19:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10d7d846-faa4-3bca-84e4-97f32e8e7117 | -20.12906 | -41.80362 | 2025-10-23 03:19:00 | NOAA-20 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 41c5ffd7-6cab-37d8-8e47-ef2d36f11822 | -19.77213 | -41.30272 | 2025-10-23 03:19:00 | NOAA-20 | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 396630e5-e28b-362c-9405-df0a39dd0eeb | -20.97693 | -47.36587 | 2025-10-23 03:19:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 53232a03-dcd7-33ab-948c-3f98eee60902 | -21.95067 | -42.92396 | 2025-10-23 03:19:00 | NOAA-20 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c8022ab4-4b75-3f1d-8b4c-62407de7971d | -21.955 | -42.9306 | 2025-10-23 03:19:00 | NOAA-20 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 5bbb7e11-3944-3e0a-affd-d02df986d1f0 | -19.7676 | -41.29834 | 2025-10-23 03:19:00 | NOAA-20 | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| f2ce21b0-3526-3255-bfe5-0d2c0fd80e6d | -20.12906 | -41.80363 | 2025-10-23 03:19:00 | NOAA-20 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 042024fd-c619-3b02-b3fb-6adf0d1fbc2e | -20.97481 | -47.3667 | 2025-10-23 03:19:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3d4733a4-f848-3f3f-89f5-ea107e70b067 | -21.9542 | -42.93038 | 2025-10-23 03:19:00 | NOAA-20 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 898c6c85-f184-3ac4-ba70-f9019235bdd2 | -20.12981 | -41.80012 | 2025-10-23 03:19:00 | NOAA-20 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| a8d7b755-cd49-36d0-840a-490c4759c3f6 | -21.73347 | -45.65261 | 2025-10-23 03:19:00 | NOAA-20 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 3cda1f3c-a30c-3c88-acc0-dbc76453bf71 | -19.3364 | -44.23201 | 2025-10-23 03:19:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 818909b4-e154-38ac-a7ad-006ea49d4953 | -21.95598 | -42.92615 | 2025-10-23 03:19:00 | NOAA-20 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 226fdc12-6fb0-36b0-a6ed-705f38f529f3 | -19.99865 | -42.19707 | 2025-10-23 03:19:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ea207f33-3c93-3b18-86e1-8d2114a044ff | -20.76456 | -43.21786 | 2025-10-23 03:19:00 | NOAA-20 | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1017c91e-73f6-3950-a6fe-e9a3c8b9f5fc | -18.13602 | -44.46605 | 2025-10-23 03:19:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1243962-a759-3342-802e-47f2942baeaf | -18.13584 | -44.46947 | 2025-10-23 03:19:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11902b70-017c-3d42-8d34-ba635082c459 | -19.76833 | -41.29493 | 2025-10-23 03:19:00 | NOAA-20 | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d52c4ccf-2c23-3349-966e-2bf370e1d03c | -21.95067 | -42.92397 | 2025-10-23 03:19:00 | NOAA-20 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 7c2a218c-bee1-3b0d-999a-d7296e82cfa0 | -21.9542 | -42.93037 | 2025-10-23 03:19:00 | NOAA-20 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 490e2987-5ab8-3176-81f5-6f104fff2d07 | -20.13165 | -41.80375 | 2025-10-23 03:19:00 | NOAA-20 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| dc169cdb-adee-37dd-989d-22c920cc77a6 | -19.99782 | -42.20085 | 2025-10-23 03:19:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 5ec13f43-dcf6-3c3f-86f6-b454bd759f1f | -21.95523 | -42.92588 | 2025-10-23 03:19:00 | NOAA-20 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| f34897b7-3c9f-316f-8f8a-0e9be7f13443 | -19.76687 | -41.3018 | 2025-10-23 03:19:00 | NOAA-20 | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 61823eb8-7046-3e6e-ac1d-4d03a5159a56 | -21.9496 | -42.9288 | 2025-10-23 03:19:00 | NOAA-20 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 85c56948-738d-3f82-8c1b-fc7acf9d581e | -21.73488 | -45.64677 | 2025-10-23 03:19:00 | NOAA-20 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 300a26c3-3f2d-36a4-974e-717d7944f21f | -19.95497 | -45.60846 | 2025-10-23 03:19:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bf1565c-1b6f-3902-b799-92116e2a53ac | -20.13242 | -41.80029 | 2025-10-23 03:19:00 | NOAA-20 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 594e3392-7b51-3a27-bd13-9c30b636ff8d | -21.95598 | -42.92614 | 2025-10-23 03:19:00 | NOAA-20 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d74b5c4a-08ca-3a14-b69b-c89472b1fb57 | -19.9564 | -45.60258 | 2025-10-23 03:19:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54c8d04c-5408-3d5f-9f1b-34ce183b26f1 | -20.13165 | -41.80376 | 2025-10-23 03:19:00 | NOAA-20 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ffe53ebe-99db-3c86-86c3-45eb00023a04 | -18.13468 | -44.4718 | 2025-10-23 03:19:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ccfa1490-c331-3aab-a9e9-a21d9baeead0 | -21.9496 | -42.92881 | 2025-10-23 03:19:00 | NOAA-20 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| caecbaed-b4ab-3a44-9d79-3321520ad7e1 | -20.13242 | -41.80028 | 2025-10-23 03:19:00 | NOAA-20 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| c4897de1-1fcc-3d4f-8f3d-72cf81438c5e | -20.75875 | -43.21685 | 2025-10-23 03:19:00 | NOAA-20 | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 49c9bfac-d699-321a-bb30-1f1a65165b8a | -20.76456 | -43.21785 | 2025-10-23 03:19:00 | NOAA-20 | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d0f59bf9-32ad-3398-b545-8e23f8c014f6 | -19.7676 | -41.29835 | 2025-10-23 03:19:00 | NOAA-20 | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 3fafbae0-ffc3-3464-9757-e10f342e1b71 | -20.12981 | -41.80011 | 2025-10-23 03:19:00 | NOAA-20 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| df5f3bd7-e690-3966-a5a5-8a1f2d619c11 | -19.3364 | -44.23202 | 2025-10-23 03:19:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9523892a-2e2d-30dc-b2fb-6305c8ca2a80 | -19.33759 | -44.22683 | 2025-10-23 03:19:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b058872-2750-3d34-84b4-8beedb68408c | -11.3643 | -49.7995 | 2025-10-23 03:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| bd6b58ef-902d-368e-b310-a2cff6fc59fd | -3.0353 | -49.4901 | 2025-10-23 03:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| db7d1a98-cbbd-3359-bcb3-89dcf2c1e4fd | -17.6167 | -46.614 | 2025-10-23 03:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 57.5 |
| e0165e72-3c43-3e71-bfb5-5cccef5778e8 | -3.0169 | -49.4694 | 2025-10-23 03:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 0eb77f02-c58c-3cec-9ad2-01389db91ad4 | -3.0168 | -49.4906 | 2025-10-23 03:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 125.7 |
| 015a72f3-1505-38c4-b2e4-d1a387421ff8 | -3.0168 | -49.4906 | 2025-10-23 03:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| f750e831-d2d2-36b8-9e0d-1e4cbe5f4a58 | -17.6173 | -46.5906 | 2025-10-23 03:30:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 4ae1ba92-bff3-341c-a735-fdda442482af | -12.0036 | -46.7667 | 2025-10-23 03:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 8222f1db-638f-31b4-8668-12336065e65e | -3.0353 | -49.4901 | 2025-10-23 03:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 5b60610c-2ec2-3ed5-9c33-23d7a6e0157d | -3.0169 | -49.4694 | 2025-10-23 03:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| bfff9c10-b94c-3780-bf4c-4894aba74a4b | -17.6161 | -46.6373 | 2025-10-23 03:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 686ac327-49b1-3431-922f-e72cd5698ddb | -11.3643 | -49.7995 | 2025-10-23 03:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| ba590c7b-5fca-3aba-a2e0-bfe26cd81cd1 | -17.6167 | -46.614 | 2025-10-23 03:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 279.1 |
| 1ed3d281-ae41-334b-a694-3fd603ecf6bd | -17.5967 | -46.6182 | 2025-10-23 03:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 462ff402-f472-3208-ac43-fcd5aa58e426 | -17.6167 | -46.614 | 2025-10-23 03:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 350.1 |
| c30e6b23-207a-329d-ba46-6b1a455828b5 | -17.6173 | -46.5906 | 2025-10-23 03:40:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 2dd227f5-7d91-3058-8cba-0e258efccc8c | -3.0169 | -49.4694 | 2025-10-23 03:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 61a0cbc6-1fa5-3f02-bc2d-bce239ecfb03 | -17.6161 | -46.6373 | 2025-10-23 03:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 117.7 |
| b02e1443-34fe-3b83-9aa2-977046d64442 | -17.5967 | -46.6182 | 2025-10-23 03:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 55a1106e-db1e-384b-8b77-6d94da8d4fd5 | -3.0168 | -49.4906 | 2025-10-23 03:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 1e33ff0f-c5f4-34e8-8543-73ef8361b41a | -12.0032 | -46.7892 | 2025-10-23 03:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| cdeaf2d1-c247-364d-93d8-b50bd0f6fddf | -3.0353 | -49.4901 | 2025-10-23 03:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| d8fc16b7-3058-3aa4-be00-2c0c44b5a0e7 | -11.3643 | -49.7995 | 2025-10-23 03:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| b3cd0ff3-6620-3a40-8545-66e73d8d317a | -3.0353 | -49.4901 | 2025-10-23 03:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 66099c6c-9214-3ca1-aa5c-a5ea48739ac3 | -17.6173 | -46.5906 | 2025-10-23 03:50:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 7920b7a2-4e73-32a5-bdc3-0b61e7d922c8 | -3.0169 | -49.4694 | 2025-10-23 03:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 3ec287e4-9199-34e3-936f-5bc7ca25254a | -12.0032 | -46.7892 | 2025-10-23 03:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| ee10b017-9b94-35d6-beab-c723f58edee3 | -17.6167 | -46.614 | 2025-10-23 03:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 256.6 |
| 944b6d9a-9252-328e-9c4d-dffb83f3b3cc | -17.5967 | -46.6182 | 2025-10-23 03:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 068a7655-a304-30dd-8974-63ae39cc2da7 | -3.0168 | -49.4906 | 2025-10-23 03:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 44281467-f0e6-3697-baac-c055ac5b0cb9 | -17.6161 | -46.6373 | 2025-10-23 03:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 97.5 |


[Clique aqui para ver as próximas entradas](README6.md)
