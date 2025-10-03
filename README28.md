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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ca121e6-1f8a-3405-ba28-e6e6d6ed4441 | -14.97583 | -49.96933 | 2025-10-03 03:45:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7cd5f601-d045-38ab-a31d-248daf7701c6 | -12.63436 | -46.977 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1cda487d-de8f-3686-a8e9-9311b6eabcc4 | -13.76907 | -48.04068 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 443a50ac-c46e-37d9-8f17-ff91049e6b3e | -13.96571 | -48.1083 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e03008ad-022a-3dfb-9551-cad176d31cb8 | -12.1193 | -43.44056 | 2025-10-03 03:45:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f6a06845-4634-3e43-afb8-33892e0df4ce | -14.208 | -46.08777 | 2025-10-03 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1c2edc6-7306-31eb-9da5-3f0bc070b85d | -13.80198 | -48.05973 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 210f515a-2d1d-30db-b13a-b0c7b80fc262 | -13.64765 | -47.30378 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e0b6bc5-2cf3-346f-a66b-eb021f2344e8 | -8.9102 | -45.04706 | 2025-10-03 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b7649d9f-99cc-31b1-b370-f0ce5faff048 | -15.24415 | -49.29687 | 2025-10-03 03:45:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca255e21-309f-3bc3-9e69-88725eb5a20f | -13.32068 | -47.58453 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d8d2681a-97cd-3fb8-aecc-862f4191caf9 | -14.94063 | -46.89177 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9198d3d9-bfcf-30e0-9a9d-023de6fedc87 | -13.20707 | -47.88056 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8f2e54ab-0bce-356f-8b85-fc6c51afab4b | -12.37366 | -46.5297 | 2025-10-03 03:45:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8befa7d-4cc7-3aa1-97da-4a6bc00cdb18 | -15.35813 | -47.06178 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5aae6ed0-2814-303c-b7d5-d7c8970048c6 | -13.12847 | -47.84511 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7540d68c-694b-3336-8722-f27ea6c1b2d7 | -8.55471 | -47.64298 | 2025-10-03 03:45:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7803ae84-09fb-393b-a687-13c795979ec2 | -15.08125 | -42.12291 | 2025-10-03 03:45:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 343637b8-6f89-3dee-897d-26a61cfc0eec | -11.5703 | -47.66002 | 2025-10-03 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 86238b39-dfdf-3274-bce6-53114226de91 | -11.83118 | -45.01925 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5bbdf53-5647-302e-b198-11fa6ee45487 | -14.65345 | -48.25386 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6fedf7d4-1a17-33d3-8a01-9aac46fd3f70 | -11.47807 | -44.97 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 34dcba70-1b2a-3551-9582-3fa027205d15 | -9.06298 | -46.65604 | 2025-10-03 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5bf83aad-52db-33ee-930d-01a03c503eb0 | -8.71003 | -47.97939 | 2025-10-03 03:45:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2a2cfb04-15bd-30df-8a3f-5c22ab330530 | -11.28916 | -47.83465 | 2025-10-03 03:45:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e793b538-2904-310e-b680-6f718bf17b6d | -14.23099 | -46.10762 | 2025-10-03 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 15ee8268-73d7-344e-8f47-66f30684e733 | -14.74608 | -48.12384 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1c43e732-318c-3124-9277-0a4d14bd23b2 | -9.9182 | -43.73646 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2fab8a11-0f74-3879-88b1-c023e31314b0 | -13.15808 | -47.82893 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d84c19b9-4240-36d5-9364-adcecbcc5cfa | -11.84269 | -45.0416 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2882ea3-3707-386a-93f4-60c5973fc7a9 | -11.55753 | -47.6618 | 2025-10-03 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 52b73532-ca1b-36ff-942d-376c88ee9afb | -14.94961 | -47.52463 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9f3fc77a-32b3-32bf-92fb-932c878a8687 | -15.27198 | -47.91174 | 2025-10-03 03:45:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eda9a8f9-bb13-3791-84fd-0d7b029151c0 | -13.59015 | -48.18824 | 2025-10-03 03:45:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| acd32797-efb0-30cc-9959-5c41534d24a0 | -13.16747 | -47.89428 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 913940bd-0479-335f-91af-9426f0a06897 | -12.42548 | -45.15751 | 2025-10-03 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd0ac555-6459-3df0-8cc3-3f10c043359a | -9.91625 | -43.71955 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| c6fd1673-2773-32d1-9d32-322423a21f82 | -12.12 | -43.43665 | 2025-10-03 03:45:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3229500d-58ac-30d6-a1f7-707ec115967b | -14.46942 | -48.41002 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f794b19d-00f1-3c66-98b7-bf5063a040e2 | -15.60555 | -46.92811 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 36c60d52-502a-3c48-b49b-a3a4d746275b | -15.52235 | -46.80354 | 2025-10-03 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c3702d59-6dff-330d-996e-a710639e2e03 | -12.38679 | -46.52085 | 2025-10-03 03:45:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d8fdbba-4cca-32f0-9050-a302ac3892dd | -14.74066 | -48.09172 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ff092559-8005-37fb-8bc4-b242bb466970 | -14.95156 | -47.52426 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e869be43-f538-31c8-8116-d794550a392c | -12.76381 | -44.90358 | 2025-10-03 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db7a8dde-8eba-3215-a881-c7423443965d | -13.1409 | -47.88466 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1b06e8ef-7ce5-3864-b5db-79503e379293 | -12.30571 | -46.87682 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c83d2629-bbcb-3ab8-8e29-abd021d29733 | -13.30067 | -47.26598 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 572d913a-c085-3db0-9b1a-b390bbe80437 | -11.62746 | -45.03234 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fe4c2d6f-32ba-3d26-a26a-e8eae9b84c15 | -13.30307 | -47.81973 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae8dccb8-2093-3195-ad18-fec41d0bb748 | -13.12947 | -47.88045 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1e1c16d3-19de-3888-aabc-c928683d2e3d | -15.29834 | -46.28944 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7480a3e-9a46-38e4-b2c9-a3418d97ef4b | -12.92791 | -46.38268 | 2025-10-03 03:45:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45d9c896-cd2d-3a82-b053-7a0dc8d6f8d6 | -14.38094 | -45.9356 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32db6beb-f950-3758-87ec-f4a29ec536ad | -12.64873 | -46.87392 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6933fc14-5756-383f-8338-b7846dc1bd37 | -11.90634 | -46.29001 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f04acb50-7619-30a6-9e99-86c5d7c33445 | -15.24641 | -49.31636 | 2025-10-03 03:45:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8b325973-cd25-393c-9f37-8f4e7b9b58ba | -12.29931 | -46.87965 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d1153dc-7786-30cc-9227-96d2c6ca7fda | -12.75396 | -50.55328 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 55993d9e-2bde-3405-a718-71f3949cd337 | -15.35504 | -47.05981 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3c80cfd2-ae5a-3b4a-8374-974a07899bb7 | -15.58215 | -46.91672 | 2025-10-03 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 310ac7b0-74d8-3249-bb5f-bcba8fd47f0a | -11.23585 | -48.20499 | 2025-10-03 03:45:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f6de28d1-b5ec-3b37-9fdb-539c69c49f7b | -10.86659 | -46.67418 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 71d7e1b0-0167-38e4-b7f6-949b194e87ce | -13.34308 | -48.12474 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f78238b7-5217-3091-a785-024b5c5c905a | -13.32137 | -47.58112 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| acac9f35-0989-33b8-b455-18a6e084bb1e | -14.44052 | -46.11986 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 54852831-25e3-384c-ab43-574ded026f6b | -12.61695 | -46.97632 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ac0f5549-6655-36fc-ac79-5bde9973ba2d | -14.06891 | -45.68485 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a15974f4-54f2-3a3e-8957-1cd38b26e3e2 | -13.2412 | -47.3465 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 34028707-a8e5-3939-a991-eede3ac4823f | -9.07787 | -48.02732 | 2025-10-03 03:45:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 932fed20-791f-38c8-b77c-82ee10eae6ee | -11.55156 | -47.6605 | 2025-10-03 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c8c4fd37-5122-3b2e-8e60-839725161cf8 | -11.64634 | -46.86505 | 2025-10-03 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee70a47a-5a32-3d27-b1bd-ed51dad1016a | -11.49133 | -45.01108 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 90d800a5-9fd6-34c9-a9d8-1fed2ab73cfc | -11.77393 | -46.8262 | 2025-10-03 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00976d87-488c-3233-b1cd-b6b38fa72969 | -11.91048 | -46.74131 | 2025-10-03 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5e054ef-55c9-32bf-9cfd-ddce28c357f6 | -14.90451 | -48.34551 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2dfeb7eb-4b63-3d0e-93c1-59349253b4da | -14.98025 | -45.05973 | 2025-10-03 03:45:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20e1a9a6-84d6-3eeb-9471-de6509a199e4 | -14.62081 | -48.23408 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16da3798-76d5-3e7b-9263-a46f2f598082 | -11.62131 | -45.02982 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ae942370-04c4-3215-9cfe-956bdd608bca | -14.74709 | -48.11898 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0c5f7236-8e64-3903-9756-5f73ddd22e54 | -11.62012 | -45.06333 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d932761f-7d31-323a-8838-9f9cd64d5924 | -14.65773 | -48.29269 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ded1acc6-aed7-33d0-94bd-ac9f67d4a272 | -11.08546 | -47.8705 | 2025-10-03 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2a842b60-ec60-30cb-b021-13e79b32c3be | -13.39752 | -42.64998 | 2025-10-03 03:45:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 80f4bb95-ef2f-3fdf-9c5b-27ad3411e81a | -14.20294 | -46.08619 | 2025-10-03 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 55af2b15-9d06-303e-999e-23a69e86fb66 | -12.12319 | -43.44478 | 2025-10-03 03:45:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 9163c05b-f309-361a-8505-34a4609b3c02 | -11.49194 | -45.00778 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7a2db620-74ee-307d-a703-a30d916409fe | -15.60814 | -46.92507 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 09929ec3-a434-3aa8-8a6e-a5a3963f7f61 | -13.30841 | -47.25674 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| acc32d5d-8ef1-3c58-b907-411d7c5d05f2 | -11.80777 | -45.00513 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0b6ce2ea-bfcf-3ae7-a4c9-4ca404d0f934 | -9.93305 | -43.76315 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 953a9de2-d653-3a78-9cc2-6b36de184c1e | -14.88061 | -46.85697 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 909b2e07-b03c-318b-967d-99d6655ea587 | -13.12591 | -47.88717 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| d1a2fc23-b6d1-3f16-b01a-9fbfda7a6761 | -15.58928 | -46.90868 | 2025-10-03 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a659bd5-429d-3cce-8961-82f2e892cd23 | -12.38826 | -46.51328 | 2025-10-03 03:45:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02347afa-e22f-3a6f-aaca-f4fe052f2b2d | -15.58918 | -46.93691 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6dc3720b-8581-3435-ba9c-7c4c4c149269 | -9.94745 | -43.76551 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d6a86f53-b721-3b7a-8ef5-f7f1f3840bcc | -13.13147 | -47.83969 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9d7912bf-f5f0-3bf1-8a8e-05dac38e3355 | -14.64107 | -44.74072 | 2025-10-03 03:45:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 234c133f-033e-3516-a90e-3cf77143026d | -13.65348 | -47.30397 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README29.md)
