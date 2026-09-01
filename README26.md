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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60b29d3d-82b3-3a52-b3ef-cba6727b2e21 | -11.20681 | -45.11956 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a3c05e5-97f6-3699-bb51-763094a16b50 | -11.20566 | -46.08107 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e28fc187-702a-3156-964c-c434c4daedf1 | -10.03182 | -44.70214 | 2026-09-01 03:55:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 758bf692-c755-3507-b6d3-754223a8f1e6 | -11.27971 | -50.57198 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 481a9b9f-0fc8-3000-a667-891985c6c6ab | -10.34 | -50.00375 | 2026-09-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 42597664-9978-3d47-8aa2-3d1c0ef87cd3 | -10.20844 | -50.32254 | 2026-09-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| deada9fa-0c3c-3df0-96e3-61f69ab5889b | -11.31526 | -45.17133 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1bc7b9d7-aad0-3b14-bd86-7c050674edb9 | -10.40395 | -48.23471 | 2026-09-01 03:55:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ca837cd-10c0-35e7-b7b4-b9a5f84b3656 | -11.32157 | -45.16271 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d28a6f70-ff39-3e40-a786-4f9ab217dbac | -11.28438 | -50.58336 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 68a0cb19-4c2c-3f27-a34e-e9ad4d6271f4 | -9.99665 | -46.44613 | 2026-09-01 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c12abfa-7119-3b30-b75a-980069d7f08d | -11.66904 | -47.59808 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| da0eb998-bb54-3c76-b3d8-e5f9ef0b87db | -7.54362 | -47.32522 | 2026-09-01 03:55:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6b98f4ff-0086-3d66-9bc5-713f6c8d7a73 | -11.06962 | -51.53736 | 2026-09-01 03:55:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e4a06e8-4169-3878-88c1-0301b7a332b8 | -13.45445 | -51.87645 | 2026-09-01 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4895a12b-1908-3f71-8867-f86173864c2e | -11.66604 | -47.59928 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9c4d027-d517-3bea-ac74-5eb0367349e3 | -10.04952 | -36.2107 | 2026-09-01 03:55:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f046e430-8b0c-3c6d-83f2-4941a3e7af24 | -11.2597 | -50.57222 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| acb96122-f236-3e9e-95b6-1cc53b6bd721 | -11.48804 | -45.10331 | 2026-09-01 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 81ede8df-2f84-315e-8eec-0eb7fc730911 | -11.25683 | -45.1041 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4aa26f0-ae3f-3f2f-9841-5e5f36370044 | -10.86613 | -45.35946 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9926c722-4314-31a3-aece-9fb314940968 | -10.32622 | -50.03917 | 2026-09-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0307e567-eb28-3440-88ec-9f084fec74aa | -11.31108 | -45.19421 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| eb196174-505f-3d8a-9f8f-1461aae0dcec | -11.911 | -45.06087 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e8c20640-3b88-3352-b6e3-d3fc4362dd94 | -10.82621 | -50.71558 | 2026-09-01 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 68048cb2-984e-3992-a8c1-753c26688077 | -11.09856 | -41.46449 | 2026-09-01 03:55:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b62472f0-fa7f-3110-be75-6f88ee901af3 | -11.35383 | -45.42239 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2f4266f9-ab58-3d3d-9630-2ad711a263ab | -11.94549 | -45.05879 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 54848b6c-3c16-3b12-a891-5b392f6ce2f4 | -7.28873 | -49.84193 | 2026-09-01 03:55:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8db3741f-9053-3d26-a0be-58fefde372dd | -11.37867 | -45.18581 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f65b30b8-f63b-37c4-9cd0-35d39231bb15 | -10.74113 | -47.98663 | 2026-09-01 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dcb7a457-225a-3853-87d0-fb3c1143cccc | -11.06279 | -51.53584 | 2026-09-01 03:55:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 997b54cc-606e-3a23-b822-429aa68bb4f4 | -15.19621 | -46.22291 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a031d7c4-b52b-3680-acff-1060fb92eccf | -8.84732 | -47.08847 | 2026-09-01 03:55:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d98a3b6-43e2-39f6-92b6-4ab0038ccba4 | -15.21011 | -46.2215 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f4342e69-bc11-3ae5-a5ac-0019af1c7191 | -11.93237 | -45.10419 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3f02aa5-bdc2-362d-b181-0441ee57810d | -11.27793 | -50.58195 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 0eae76ac-f72f-34a2-824a-30e638f38d5a | -10.75089 | -47.99584 | 2026-09-01 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50b07bce-d1f0-312d-be1f-7110d33f880a | -11.91957 | -45.09082 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f1c2e1b-5da5-331c-88c3-9ef8810be186 | -11.29677 | -50.58712 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 26f33770-ebf9-314e-83e2-d8af3cdb3747 | -12.9546 | -45.9617 | 2026-09-01 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f475e7cf-ebad-33d8-94ad-78efa0ef951d | -11.31441 | -45.17597 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1a5891d7-af6c-35f8-9b0e-05b04f047eb3 | -6.72509 | -50.46677 | 2026-09-01 03:55:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 826f2493-1e3c-3322-83ef-8d75e4a215da | -15.16901 | -46.24108 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0849c2c9-3067-35ec-a46a-7c1ec8946691 | -10.35373 | -50.00116 | 2026-09-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 30.7 |
| a2fa4f46-0725-3c79-95a5-8016062ae98a | -11.24747 | -45.15619 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 835ef509-8a93-35e3-9f24-5f914bbd8ab7 | -15.18178 | -46.2448 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 969ca1f4-7cd1-3b43-a41c-27a73f0d5eac | -15.1916 | -46.22219 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b7f4ab0-fff9-397b-88bf-dc1e6bfb157f | -15.71777 | -39.90083 | 2026-09-01 03:55:00 | NOAA-20 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6d5f6a13-9f88-35c5-b5ea-44006b53d8ea | -15.20084 | -46.22355 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 91dfa556-5d5b-30ef-8904-218e50aa49be | -10.04119 | -48.68907 | 2026-09-01 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d16eee40-614f-33ec-8672-5797345bc55b | -11.2031 | -45.11404 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6f879c5-13c1-35e2-804d-9883da1a6dd4 | -11.66399 | -47.60966 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 48514ffb-0611-3699-a9cf-7f9629049042 | -11.24681 | -50.5694 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 966fc2ab-c505-3878-bd7c-11b810961621 | -13.34579 | -43.67458 | 2026-09-01 03:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b260b675-86ba-3623-93b9-d39e742d0137 | -10.34634 | -50.00507 | 2026-09-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 3be5995e-8276-35bb-932b-d508994763c1 | -11.48349 | -45.10251 | 2026-09-01 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e8dc2faa-8b64-3d05-b51c-4d802c9d4e24 | -10.39173 | -48.23681 | 2026-09-01 03:55:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dbb1ceb7-9bbc-3894-8d9b-d880c9ca92c1 | -8.41901 | -44.99853 | 2026-09-01 03:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| fe4c1c12-70bc-3bac-b240-50b6009147b9 | -11.20072 | -46.0805 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dd7db5fd-bb2d-30a4-a06b-84ea71b4fa1e | -11.0683 | -51.54377 | 2026-09-01 03:55:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 35d274ec-786e-34a3-81a7-65c74e279b70 | -11.29032 | -50.58574 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 65696fd7-534d-309c-acd9-cd9f2ef4c506 | -11.29727 | -50.58617 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| a92ba565-a168-308c-bc72-409018457c26 | -11.26056 | -45.10961 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 00ccab13-3516-3f40-a284-29609dd1ded5 | -8.84861 | -47.08134 | 2026-09-01 03:55:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1ed4453-4a02-3efb-9280-66b05bdb645b | -15.19547 | -46.22343 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f3ede43-be49-3171-b02d-939a50b06190 | -15.57572 | -42.70989 | 2026-09-01 03:55:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bd369ea9-f875-39a4-8171-307544ae3712 | -11.29082 | -50.58476 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 563d6d5b-224f-3a9f-a907-bac568831377 | -10.31987 | -50.03785 | 2026-09-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b82ee82-127f-3790-a099-29c0d5ff25db | -11.32801 | -45.15329 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d831294-29c6-38e2-b4ae-2d40cc553626 | -10.0034 | -46.4382 | 2026-09-01 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 48ed3a0f-f11b-3b86-b48d-df26fa79f0be | -10.94417 | -49.77544 | 2026-09-01 03:55:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9ac18157-1348-33ea-a153-026a7adf700a | -11.51483 | -46.92685 | 2026-09-01 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fdc0346e-0c90-3270-bea6-b58fe7e9f437 | -10.40473 | -48.23065 | 2026-09-01 03:55:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef7b495a-e4c2-350b-9bde-975275dbf2fc | -12.09596 | -44.9836 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 491ecb4a-5bdc-35bd-8f39-15b54feccf6a | -15.20628 | -46.21985 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d437eded-485a-30d5-8579-6b54b30b52c0 | -12.95497 | -45.9695 | 2026-09-01 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 950f9f4b-f44e-3238-bb7b-0d158c98736f | -9.98866 | -46.43228 | 2026-09-01 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3424ff6-e2df-32f2-8fee-b81f365f0bf8 | -8.83953 | -40.53604 | 2026-09-01 03:55:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d8197ef0-f5e6-3c7e-a69c-186b03a405fe | -10.35018 | -50.01011 | 2026-09-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 8097ec63-fad4-34ee-9924-3e39e21a1664 | -10.34385 | -50.00876 | 2026-09-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 3b40f932-4a9e-383c-858d-a608b6632db7 | -10.95135 | -49.77177 | 2026-09-01 03:55:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94150100-8de0-3198-98b1-dc57f4ee6520 | -15.53987 | -43.18089 | 2026-09-01 03:55:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2789874e-b944-35c7-8fc2-76a13643a1af | -7.41449 | -49.73986 | 2026-09-01 03:55:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fd9508b-7ed0-3fb1-a745-1ee2723ee5f2 | -11.66255 | -47.61697 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9e115645-eeae-33c2-a459-c41fb41de0d8 | -11.37409 | -45.18497 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9b09d38-f46a-32ae-859a-228a6e35b919 | -11.20747 | -45.09017 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 259081e1-ddac-3f3a-b98a-79117c62854f | -11.68258 | -47.15451 | 2026-09-01 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61983f8f-c2c8-3c05-a232-79260146f4e5 | -11.204 | -45.10913 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f324461b-2141-3adc-8b70-d8cfa2e12218 | -11.67802 | -47.15023 | 2026-09-01 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4bd3cb53-5114-3287-b2cb-978b253ae088 | -11.28972 | -50.5903 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 95bb800e-e5d4-3742-a1fd-d0c77b5b3a11 | -11.6727 | -47.59358 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5f724bb4-8d3c-3e3a-926f-ec8202ead061 | -11.6774 | -47.15347 | 2026-09-01 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 43aab9d3-414b-3660-9f5c-1d808adc8b33 | -10.0289 | -44.69215 | 2026-09-01 03:55:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5e7a97d5-7293-3d4b-83a0-90c09dc21a91 | -9.99518 | -46.39722 | 2026-09-01 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 84bea3fa-ff17-3640-a9e9-563573944db0 | -8.79962 | -46.36914 | 2026-09-01 03:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b03ad42d-77ef-3944-9a4b-3bba6968f407 | -15.20099 | -46.21951 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 02f4fd79-ddcd-3682-88d6-83b117a9da92 | -8.91311 | -45.04528 | 2026-09-01 03:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3ca58c46-34c2-3056-ac1d-ceec03540db5 | -11.94249 | -45.04995 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 245d62e9-625c-3e66-bf45-97a11e0c35f5 | -15.18268 | -46.24434 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README27.md)
