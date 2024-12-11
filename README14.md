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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9475cf91-6611-3876-a517-96a31950874e | -6.978 | -42.9977 | 2024-12-11 04:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 142.8 |
| 4ecebca4-05fd-3aee-8606-354d4b7b2413 | -6.8972 | -43.4969 | 2024-12-11 04:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 115.3 |
| d30a8ab1-ad8c-3cf2-b427-47b64573e31d | -2.9666 | -53.1201 | 2024-12-11 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| ec4da49e-db22-36d4-add5-e2f59e93ef24 | -6.9158 | -43.5185 | 2024-12-11 04:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 4721da82-71ac-301c-b8ef-9719f636f124 | -6.9592 | -42.9994 | 2024-12-11 04:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 130.7 |
| 613d5fef-1368-3244-951b-90247ed44f95 | -6.1178 | -42.5559 | 2024-12-11 04:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 79.5 |
| e271700a-4f24-375c-8089-c92eceec30c5 | -15.0865 | -59.6487 | 2024-12-11 04:20:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 40.1 |
| dd19f625-eb7d-32f0-b7ae-38d3b5977745 | 2.7444 | -60.6381 | 2024-12-11 04:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 8091834c-5785-3fa9-92f3-9019635111e2 | -6.118 | -42.5323 | 2024-12-11 04:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 101.2 |
| 78dfa186-d24f-3135-8f6b-aec1f9e5064d | -6.9783 | -42.9741 | 2024-12-11 04:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.2 |
| a4f6a1cf-1b97-3f08-b793-acba9f8a4bfc | -6.897 | -43.5202 | 2024-12-11 04:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 4f067ef1-e105-3eb9-8885-e426ca387492 | -6.1368 | -42.5307 | 2024-12-11 04:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 73.2 |
| 72251053-7ad2-3875-9e89-5b3793ff7f82 | -6.1366 | -42.5544 | 2024-12-11 04:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 52.3 |
| f45a9f2d-e93f-3f1d-977b-9c052d551170 | -6.9161 | -43.4952 | 2024-12-11 04:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 172204be-2934-386a-bc8b-e0ceae77ac09 | -6.978 | -42.9977 | 2024-12-11 04:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 105.7 |
| d48ae312-52ed-3366-ab99-c1125614df2e | -6.9158 | -43.5185 | 2024-12-11 04:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 4201f378-e9ad-3d37-97c3-a49587a1c6f3 | -6.1368 | -42.5307 | 2024-12-11 04:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 95.4 |
| 0a38796b-f48c-3d98-8b79-64642440b0c6 | -6.9783 | -42.9741 | 2024-12-11 04:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.3 |
| 5f3b5d93-af6a-3476-b6fc-f135714d9f70 | -6.9592 | -42.9994 | 2024-12-11 04:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 105.7 |
| 9928f8ee-4f88-3ac4-8398-cd3ba48a7f40 | 2.7444 | -60.6381 | 2024-12-11 04:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 58168bae-05d3-3437-8ea2-d2575885ff28 | -6.8972 | -43.4969 | 2024-12-11 04:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 117.2 |
| a5233a80-3bdb-39ac-8860-cf05a01a6df6 | 2.7627 | -60.6378 | 2024-12-11 04:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 93580729-0760-39c2-8f40-4b65b9cde0c8 | -6.9594 | -42.9759 | 2024-12-11 04:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 56.6 |
| 1edb955d-b29b-3501-a0bd-71c66a7ab46d | -6.1178 | -42.5559 | 2024-12-11 04:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 57.1 |
| a5b403fb-3f6d-3c8c-a98b-87eee981e360 | -6.118 | -42.5323 | 2024-12-11 04:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 73.4 |
| 4f3bca34-8ee1-3530-942d-c9761344bf42 | -6.897 | -43.5202 | 2024-12-11 04:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 117.7 |
| e186fc62-fad2-33b6-a83b-41c8b2c8c454 | -6.1366 | -42.5544 | 2024-12-11 04:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 68.2 |
| 83c4f359-5485-3d69-a394-deae5bf8d6f6 | -1.39673 | -55.08365 | 2024-12-11 04:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a64290b3-2416-3b36-a633-b4a66959de2f | -3.24062 | -42.42635 | 2024-12-11 04:31:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e67c99c1-a30d-3892-a274-52bd33e4f9d4 | -3.07245 | -40.05013 | 2024-12-11 04:31:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4d6fadb0-f504-355a-80db-6374316cf980 | -3.0732 | -40.04516 | 2024-12-11 04:31:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| de9010b4-d69f-3318-bb7c-c72a7c097aa0 | -1.4714 | -55.3942 | 2024-12-11 04:31:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e9778819-301b-3203-8443-57e9b2d79791 | -3.23105 | -42.43544 | 2024-12-11 04:31:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1cc6d646-9224-3922-81fe-dad63612f192 | -3.07715 | -40.05086 | 2024-12-11 04:31:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 746c64eb-2780-38b3-acb3-8bb4f8534623 | -1.54411 | -52.67942 | 2024-12-11 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0d59eb0-b5b5-34f9-abe2-bb812f47d72a | -3.23556 | -42.43266 | 2024-12-11 04:31:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d30d4443-960a-31a6-9654-3049b9354877 | -3.23609 | -42.42921 | 2024-12-11 04:31:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 84b01b32-f860-3f00-9219-0d95cc301ada | -1.47187 | -55.3912 | 2024-12-11 04:31:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 332418bf-9ee0-32de-b76d-b586d3a16431 | -3.24115 | -42.42286 | 2024-12-11 04:31:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 61eafc80-04ff-3691-86f6-04f2f26ccbf4 | -3.23156 | -42.43201 | 2024-12-11 04:31:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c7a3f293-47e4-305f-a606-3d1eb6abfc60 | -3.23661 | -42.42574 | 2024-12-11 04:31:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a99e1d78-eac7-349d-ba4b-cc6966d0bff7 | -3.24009 | -42.42983 | 2024-12-11 04:31:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d1e529b7-f8f8-3b81-b6a8-58b106c0b5d1 | -1.39792 | -55.08099 | 2024-12-11 04:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 083e333f-7422-3ab0-b6f0-79e6e7691107 | -2.71755 | -45.56646 | 2024-12-11 04:31:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d1f6e10-c87f-391e-95cc-6b51d010a8a2 | -1.39716 | -55.08088 | 2024-12-11 04:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 760d2dd2-f073-3cac-a5b8-a99eef5c2a1b | -1.39629 | -55.08643 | 2024-12-11 04:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71399f97-023f-3efe-90cf-e6d2fe3f7be0 | -6.90733 | -43.50341 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8de71b37-ff84-3a95-8600-44ace73277f2 | -9.19327 | -49.47389 | 2024-12-11 04:33:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9a445be-1cf7-3343-af83-947646b0206a | -6.96526 | -43.00098 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| c69c9aae-2b6e-37fd-bd96-89ff513c205f | -6.97393 | -42.99866 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 827ea3df-e9e0-3027-a8d4-b6d46dc77d9a | -9.33256 | -40.33204 | 2024-12-11 04:33:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 015aa4c2-1b2c-36df-8ff0-2368e498662b | -6.9557 | -42.98095 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f1fa6bed-d8ba-3f05-85e4-651fe019bca6 | -6.95517 | -42.98458 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7881c0d7-216a-3e22-84fb-f601c29d015b | -6.93861 | -43.53517 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f809c55f-8fa2-3bf3-b246-53cb94757f7a | -6.1272 | -42.5263 | 2024-12-11 04:33:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a6ba6f3c-0898-365b-a555-77de940e7381 | -9.54209 | -46.98691 | 2024-12-11 04:33:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eac4dd95-5c21-39bb-9907-05889a065711 | -6.97092 | -42.9908 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| ea7d8112-40a8-3d20-8cf3-006878763054 | -10.51105 | -44.93475 | 2024-12-11 04:33:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a4bace0-fad2-3dad-a9d7-298429012c44 | -1.47465 | -55.39603 | 2024-12-11 04:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 284b362a-a851-3c0b-b54e-a53aa3b37aac | -6.07385 | -42.63302 | 2024-12-11 04:33:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| f1cdf272-dba0-3e9b-9161-2a13edcb0f9a | -9.75176 | -41.99639 | 2024-12-11 04:33:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 48fe0ca2-cf35-3004-bc47-fadabf2c4fe3 | -6.9161 | -43.49567 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 36d14fae-368d-3d0c-9077-3ea965f21d7f | -2.30471 | -54.00245 | 2024-12-11 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 12d10640-87a8-3d39-8626-0a498aef3785 | -5.42593 | -39.52676 | 2024-12-11 04:33:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9f0877a7-91e1-39e0-92d0-452513e36dc3 | -6.97747 | -43.00287 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| ce9d2914-b634-3b9f-8826-e2a511459922 | -6.89796 | -43.51225 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 35c0a000-1694-3dfb-9448-66c3124dc709 | -6.90977 | -43.51404 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cc71ab65-fb51-34b4-ae51-92a0cf02a837 | -6.13275 | -42.54655 | 2024-12-11 04:33:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fe50324b-e64a-3fc4-868a-f1f5ebda812b | -6.94438 | -43.00144 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dbca2252-556d-3d9f-a31e-d3aa37a1812d | -6.96031 | -42.97793 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e34663b1-948b-3297-be39-948b84b031d0 | -6.95871 | -42.98885 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 85d320fd-8ec7-37f5-8470-c05431c073c3 | -6.90808 | -43.49834 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 4d46c1c6-7dc8-3bbe-ac6e-dbf1b310166f | -2.82069 | -53.07726 | 2024-12-11 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6de489f8-ff39-3c1e-a10d-970a69eea3e1 | -6.90748 | -43.49962 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 286b6d51-7192-3a79-a014-0e346f1f97bd | -2.29531 | -53.91598 | 2024-12-11 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4c8d592d-f32c-363c-a710-043b777f8baa | -6.97715 | -42.97678 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ecb8fe1d-3191-3339-960b-b61808225a05 | -6.9019 | -43.51283 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 28.3 |
| b8e6ccce-b9b5-3b82-b62a-2a5cad80b414 | -6.97499 | -42.99143 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| d0996b57-f331-3bf2-9b4d-02cc4922ca6b | -6.9495 | -42.99485 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 1a75e659-2c03-3d1d-aa25-d899d5bbbf8a | -6.97446 | -42.99505 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 79acb85c-d020-3019-be0b-0f2d9780f641 | -6.12806 | -42.54963 | 2024-12-11 04:33:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 19.7 |
| 57ac4530-b8be-3e7b-92cc-c0379b6437ca | -6.12032 | -42.54458 | 2024-12-11 04:33:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ee1e1eb2-3ccb-37ba-89c3-f92dfbfcdef6 | -2.25824 | -53.84711 | 2024-12-11 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b0839570-c43e-3a68-969e-84e3838dde56 | -9.37315 | -43.28409 | 2024-12-11 04:33:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 98da9ea9-da31-3130-b383-847cecfd462c | -5.29086 | -44.9138 | 2024-12-11 04:33:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a74f2b7-8e7d-3a55-9477-de28dcc9bc84 | -7.27206 | -34.93357 | 2024-12-11 04:33:00 | NOAA-21 | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| bec4f64a-4a9b-3bc8-9a2a-84ecf2dd5102 | -6.94845 | -43.00206 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| fed99def-882a-3fec-861c-98c8711e9473 | -6.13221 | -42.5503 | 2024-12-11 04:33:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| be5c8f3e-a84a-384d-b293-789789698248 | -6.95659 | -43.00333 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| d0f6a007-8ba8-31e8-a85f-190231da3064 | -6.94596 | -42.9906 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ade95d34-b702-3b96-b090-542932c16008 | -6.90508 | -43.51849 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0cd32e14-8b02-321d-a710-e9ae1f1c5b4b | -3.34212 | -53.07132 | 2024-12-11 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 694f7af4-0e5d-34e8-a4d7-fb632b127b3d | -3.13251 | -54.0951 | 2024-12-11 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4246bd94-6586-37cf-af52-d459f089b683 | -6.95252 | -43.0027 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 076155a8-2fe6-38b4-afb6-f13d077145b0 | -2.25973 | -53.84989 | 2024-12-11 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 89fe554f-b83e-37ba-a210-c8aaacc782fa | -6.96579 | -42.99736 | 2024-12-11 04:33:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 7a338531-448d-3432-a5e5-5fb279cb9833 | -2.33885 | -53.58968 | 2024-12-11 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 27e1d042-85ef-3bfb-b4fd-ce235fe6c026 | -6.90902 | -43.51908 | 2024-12-11 04:33:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cb591ff8-1420-3979-a054-c26fa7cec5ed | -6.12666 | -42.53004 | 2024-12-11 04:33:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9153e6a8-0679-38c5-aec8-64db80cbd477 | -6.09804 | -44.04856 | 2024-12-11 04:33:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README15.md)
