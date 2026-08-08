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
| 3d951282-6a3c-3052-a990-7b98e1143b54 | -14.15464 | -54.00653 | 2026-08-08 04:27:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2eedafc4-bea3-33bc-891b-81344660dc0a | -18.35319 | -50.72563 | 2026-08-08 04:27:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 5ab15385-2ba8-31de-af77-5f571a5714d7 | -14.1594 | -54.00745 | 2026-08-08 04:27:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cf13cd5c-b747-321d-bff7-305a84ac2bf2 | -15.14899 | -52.73577 | 2026-08-08 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| beb06999-1202-3d29-9707-d2c0141c907b | -17.57631 | -49.66676 | 2026-08-08 04:27:00 | NPP-375D | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 512c5d4a-6ac9-3f32-8249-0a71c4d52c0f | -19.95362 | -44.1362 | 2026-08-08 04:27:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b8f9bc72-ff73-3d3c-96ff-be9d672b5dee | -14.41184 | -45.6627 | 2026-08-08 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18c838d8-5a2e-36a9-8da5-e516b724810f | -18.9425 | -43.4728 | 2026-08-08 04:27:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cb1ba34b-7a4d-3f7c-9884-8b06cf5dd10f | -14.27556 | -45.28885 | 2026-08-08 04:27:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 36a95db6-e85e-31fb-8b24-e9e80e29790a | -16.68685 | -51.34647 | 2026-08-08 04:27:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2024cffe-8b5e-3ea2-b994-f58ed480cc01 | -14.30767 | -54.99343 | 2026-08-08 04:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 458e9d04-ce6e-3be9-b96e-74fb065777ff | -14.32502 | -54.9362 | 2026-08-08 04:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ef339f62-1df5-3fc7-b301-8ed1b6cb43e0 | -14.31936 | -54.99213 | 2026-08-08 04:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e4f96d0a-7e82-3682-bd95-acb58d70f952 | -20.2377 | -46.90527 | 2026-08-08 04:27:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe81159b-7fc2-37bb-918b-3ca44882a979 | -15.82058 | -48.09502 | 2026-08-08 04:27:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cfabb831-3153-347e-80bc-3a9361dcd0ef | -15.70061 | -54.8526 | 2026-08-08 04:27:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 01f7c5ed-9652-347b-8273-e141f4491e24 | -16.68869 | -49.38399 | 2026-08-08 04:27:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c9991bd5-64ee-3e76-be34-2adf6c379b33 | -17.30611 | -42.67705 | 2026-08-08 04:27:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d9838b6-854c-369c-a0ed-3f5b95f9cde1 | -14.93169 | -48.25841 | 2026-08-08 04:27:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5a4e92dc-f426-3558-b69e-3ff8df8c0541 | -20.39008 | -49.31167 | 2026-08-08 04:27:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 352f3e46-528d-36cd-823b-642941185f6a | -14.90026 | -47.74352 | 2026-08-08 04:27:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4aa47d18-de5d-310b-ac55-0e050f8e6b7c | -14.27612 | -45.28529 | 2026-08-08 04:27:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec887897-bf55-369a-a949-de531970a540 | -14.41849 | -45.66383 | 2026-08-08 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6ac72041-5761-37ea-951d-a64a97bc2edb | -14.15425 | -54.00631 | 2026-08-08 04:27:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a45622e1-56c3-3d15-8ad5-19c53886e7d9 | -18.36476 | -50.70681 | 2026-08-08 04:27:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 576ad8e1-705a-3fb3-8ba3-23a0089c05c7 | -18.3493 | -50.7249 | 2026-08-08 04:27:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 2209501f-94ad-370d-b868-7f0caa3191f8 | -14.93027 | -48.24526 | 2026-08-08 04:27:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a72464d6-9e0e-32c5-8120-456281a30a71 | -19.74632 | -43.90624 | 2026-08-08 04:27:00 | NPP-375D | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 96990696-6839-39aa-9fbe-78fb4edad46c | -16.40117 | -49.93392 | 2026-08-08 04:27:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07a036e3-6bbc-30dc-8a5f-574b6bec5b3c | -18.50858 | -48.34444 | 2026-08-08 04:27:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb9b4d4b-8401-35e3-9ecf-4ff539eaffaa | -20.36251 | -41.16375 | 2026-08-08 04:27:00 | NPP-375D | VENDA NOVA DO IMIGRANTE | ESPÍRITO SANTO | Brasil | 3205069 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a8743a2e-8e0b-3e52-ad4f-fccf62ce5ec8 | -15.37864 | -53.79765 | 2026-08-08 04:27:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e3203c3a-31d4-3576-85f0-a7c40ff89eb0 | -19.64584 | -46.2066 | 2026-08-08 04:27:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2a6aaae-12d4-331c-8521-f827c0361c56 | -19.63978 | -46.20177 | 2026-08-08 04:27:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7cc7c06-ef00-3a4b-9fc0-143f0d37a125 | -20.35846 | -53.86353 | 2026-08-08 04:29:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7a7944f0-c28d-341f-9b61-a3561a758f18 | -14.3617 | -54.9701 | 2026-08-08 04:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 8c8882d6-6839-32dd-8089-f2dfe5bbd4cd | -4.2635 | -48.1799 | 2026-08-08 04:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| fc0bd0c5-51b0-3c23-9acf-6bd71ab884a7 | -4.2634 | -48.2016 | 2026-08-08 04:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 1e8d1a31-22c0-332d-97d1-bc6926fdc714 | -4.2635 | -48.1799 | 2026-08-08 04:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 6ecc90c2-4b6e-31b4-bc39-b692e736e8f8 | -4.2634 | -48.2016 | 2026-08-08 04:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 7bae6cb2-984d-3933-a636-2119c89ed3eb | -0.90146 | -50.67375 | 2026-08-08 04:42:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d453d69a-e6b5-3393-bf8c-9658346907e9 | -2.11289 | -48.99794 | 2026-08-08 04:44:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c9281d2-ea62-364a-85c7-011817dc4858 | -6.92193 | -41.96593 | 2026-08-08 04:44:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 97acf86f-f687-3f85-9aad-0298318da94a | -6.84003 | -58.9767 | 2026-08-08 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b127f77b-fbe0-3e91-986f-b43210e12284 | -4.26481 | -48.1946 | 2026-08-08 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| cf548f64-0043-3fa6-afea-557c585da6ab | -6.84062 | -58.97332 | 2026-08-08 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a1a5c43-5b03-33ca-bdbb-cb9e0a73e40b | -6.70718 | -58.9627 | 2026-08-08 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b871f1b-d1cd-370c-85fe-470221166021 | -8.33002 | -46.3889 | 2026-08-08 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00e962df-52cf-3477-b5fb-81c69cb1eb3e | -3.40622 | -49.77724 | 2026-08-08 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| afaa07c4-600f-38d9-8dcb-38a598aa1985 | -4.26814 | -48.19511 | 2026-08-08 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6137de4f-fc67-3081-9656-c71f766856d6 | -4.26924 | -48.18811 | 2026-08-08 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| c29153d1-bec5-318a-a21f-437737a34b63 | -3.96717 | -48.12286 | 2026-08-08 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce62403b-f5bc-3e37-b413-93568ba97b42 | -4.59871 | -45.58477 | 2026-08-08 04:44:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c39e508d-3db3-3685-bac8-71acc2ebe2aa | -6.91144 | -41.96992 | 2026-08-08 04:44:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b8bc717f-5929-3608-aee5-1374bb1a1172 | -3.19931 | -50.91019 | 2026-08-08 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb6e16b8-6210-3e2b-8786-247cb26c67e4 | -6.6483 | -56.40997 | 2026-08-08 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7ba725f7-27c9-3673-8462-5f2aa21b5cec | -7.04058 | -45.54414 | 2026-08-08 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 47a0f0ed-c549-34da-b2f6-a4dd2fff6fdf | -6.70838 | -58.95594 | 2026-08-08 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7c89849-725b-3026-aa59-cf7c1ef6ebd6 | -6.70957 | -58.94923 | 2026-08-08 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa336745-b6ca-3bd9-8b0f-8359891c42c5 | -4.26869 | -48.19161 | 2026-08-08 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f6a794f6-e875-3a05-a5c2-5e1ac3b63c8f | -7.18624 | -42.34133 | 2026-08-08 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 3406ef7f-ecbd-349b-a020-3096a808ad45 | -7.51275 | -46.99692 | 2026-08-08 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a250b86-5a58-3f43-b03a-7f7bd6fed28d | -6.72321 | -58.93442 | 2026-08-08 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0e1ef992-b203-3113-b806-f1f7dc55fbc5 | -6.96912 | -41.48751 | 2026-08-08 04:44:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 06b3cb1f-9047-3a34-a5cc-5164ac32057e | -8.08095 | -45.58316 | 2026-08-08 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3e2ef8e-e1ce-3644-9af5-bbca54235f74 | -7.18478 | -42.3516 | 2026-08-08 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| c9156624-50db-335e-8d0e-14ae31ba2d87 | -3.96051 | -48.12181 | 2026-08-08 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 32ad7a99-f1af-3c13-a701-47f1c8211d49 | -6.99533 | -42.10254 | 2026-08-08 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b8bcac3a-f1a7-3779-9d54-94ef3e783cd1 | -4.36897 | -47.77254 | 2026-08-08 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 5351d918-a6aa-3f40-95ef-a174df70faf6 | -6.64523 | -56.4282 | 2026-08-08 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26a16fa0-a179-35df-9899-c696bb3a0d6a | -6.90662 | -41.96898 | 2026-08-08 04:44:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 271579e9-e4e0-34d9-aee5-da1a2e14cb5d | -6.5378 | -47.48304 | 2026-08-08 04:44:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 219d281a-c430-3af1-afdb-217ca12bb08c | -2.81965 | -49.62025 | 2026-08-08 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63cd6d5f-189e-3820-9c94-0467bfc2a0cf | -7.77729 | -49.48822 | 2026-08-08 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f103b763-52e7-3b35-9416-5a220749c978 | -7.1624 | -44.06782 | 2026-08-08 04:44:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9de3ed77-dddc-3fc7-bfc1-bd9d5c7eaf9d | -4.52618 | -38.55097 | 2026-08-08 04:44:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a604bd0c-0a3b-36cc-9ffb-fc50d59bef6a | -4.1669 | -48.77297 | 2026-08-08 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a35d03b-2490-3b5a-af3a-f9976a63de3c | -7.03632 | -56.51203 | 2026-08-08 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 850923f0-3b19-3b01-a2d9-a7eec0725eee | -3.96439 | -48.11883 | 2026-08-08 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f10b416a-373d-3510-a0ff-f0d797b35d67 | -3.79961 | -51.19115 | 2026-08-08 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49e9b637-df3f-347b-8a24-0a60317d74e3 | -6.62142 | -56.37732 | 2026-08-08 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60c8ed88-77f4-361d-a782-43ca712a7a1d | -3.01464 | -48.84151 | 2026-08-08 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ee1b4e5-ae14-3e3f-bdba-469fee6e5075 | -7.03674 | -45.54359 | 2026-08-08 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| da3dbb3c-7194-3b16-8693-b6a9a6a7b4ed | -4.69464 | -50.43809 | 2026-08-08 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1c9eaf9-99de-3841-9a54-bc1bfd8929db | -3.58862 | -49.48549 | 2026-08-08 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02f27d5e-d810-323a-b970-6a9e5e7e06a3 | -6.88695 | -59.89707 | 2026-08-08 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 59412327-8056-3c75-8e63-42e0e0957b1d | -8.62355 | -50.02535 | 2026-08-08 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12c116d5-5950-3d3d-8e39-88f4a3e87d0f | -6.91217 | -41.96478 | 2026-08-08 04:44:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 3a5acfab-4792-38b6-9b11-0ce4ff62a81c | -2.8279 | -52.30194 | 2026-08-08 04:44:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0d8675bb-97f1-3f0c-ae3d-ca7369e2dcae | -6.97404 | -41.48896 | 2026-08-08 04:44:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3b9d21c2-d757-3b0c-868d-37e9926c40ff | -6.97445 | -41.48602 | 2026-08-08 04:44:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e860edde-10d9-392c-a4cd-324b61b42beb | -2.8306 | -46.72332 | 2026-08-08 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42b448fa-7b6e-3a17-b4a6-f4efe436fd8f | -7.1855 | -42.34655 | 2026-08-08 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 5c7d8d60-b797-35b9-b7bf-b42ff76ff3ce | -2.87932 | -40.30163 | 2026-08-08 04:44:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 39dc3704-3bc3-3422-9107-6275806f1cbe | -3.96772 | -48.11935 | 2026-08-08 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72c12a84-c020-3adf-a78b-a7d6bfb5242e | -6.64905 | -56.40554 | 2026-08-08 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b8a4fdf7-e000-3317-a058-db17f4439f53 | -7.74529 | -56.32887 | 2026-08-08 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d86f19c5-4a06-35fd-979f-c7806b20c0f4 | -3.05397 | -39.93034 | 2026-08-08 04:44:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bd074145-36d5-3bb0-94b8-5eadc60e8715 | -5.88236 | -57.65215 | 2026-08-08 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| a5232865-40cd-31cf-9719-a20a4d160e71 | -6.41442 | -55.78851 | 2026-08-08 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README15.md)
