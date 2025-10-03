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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e76b7b70-2cb7-3796-95f1-258dc56005c1 | -12.92307 | -45.08608 | 2025-10-03 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 45f78604-3470-3909-af5e-5755b7fcdb3d | -15.92157 | -43.34364 | 2025-10-03 04:34:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dc1479f0-b27c-3c3f-9f7a-4a8a89748845 | -13.96387 | -48.10544 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf4293f5-c087-3fbe-a2c1-f989e028f995 | -13.13656 | -47.83804 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 271b9b0c-0e70-395e-a23e-e81514451bc8 | -15.35584 | -47.06894 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73aa9e52-4d32-32fc-90a2-0dca6bd5cb89 | -13.08797 | -47.07146 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 138a9c91-1d86-30cb-a1bd-3b595004a836 | -14.941 | -46.89354 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36ceb1b3-409d-30fb-9a98-70aa6d79c63e | -14.67374 | -48.09033 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a1ac713-eb14-38ea-bf87-14f56de1b471 | -13.55201 | -47.59423 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7892e85-838f-34a1-9ff5-a6ed0e3e6aae | -19.9487 | -46.81161 | 2025-10-03 04:34:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e13c11a-e6d5-3f03-8482-cd957eabe1d5 | -14.24936 | -47.27893 | 2025-10-03 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c358f16-8e93-3b35-85a5-527b9738fdf9 | -18.25272 | -53.32016 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec1e9ccd-47d9-34aa-9ab5-59ba9ca1936b | -15.32525 | -45.05263 | 2025-10-03 04:34:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44887cd6-a766-3fbc-98ea-16824c3978db | -16.05137 | -50.91582 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| bf304a37-cac3-3156-be20-cdd3f8065f6b | -14.94155 | -46.91486 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e58a125-6625-3416-bf0b-e0084cc7da8c | -16.04293 | -50.92551 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c23d66a7-b791-3006-a72b-264a30e215da | -13.77029 | -47.53814 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2c56179b-8bd1-33cc-849c-ffc1cd587ba2 | -14.98448 | -49.96426 | 2025-10-03 04:34:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 923ec899-743a-3ff2-8bfb-e4dcdad8334d | -13.33717 | -47.2086 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b6fc86fa-14ea-3573-82a8-7d4070702bc1 | -18.22085 | -53.35873 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 601a39e4-efa5-3bce-90ec-00f1007a1a0e | -15.94704 | -46.21683 | 2025-10-03 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0ded2356-cb5a-3957-adb7-0f3f2201bd86 | -20.38451 | -44.13396 | 2025-10-03 04:34:00 | NOAA-20 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e66df3f5-f9d3-3301-bcf6-4b51e9c7ca10 | -16.40291 | -52.16209 | 2025-10-03 04:34:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 05dec9d1-ba0c-32b1-8dbe-17a8c936cac3 | -13.74639 | -48.01813 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbbb1375-128b-35eb-972d-4f8931072669 | -12.64235 | -46.96261 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0ff89cd2-ad04-36f9-a2c5-c018d650191d | -13.3091 | -47.81244 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 335c98a5-455a-3c60-a27d-a514eadbca6a | -13.51661 | -43.41339 | 2025-10-03 04:34:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4afca73d-cc89-3b36-9c11-4c2aaec1ede4 | -13.76701 | -47.5834 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 66d89b56-9795-32a3-b691-50909499005e | -15.22173 | -47.95933 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f2c3f7d-1fa1-3996-bf6e-f0beb256c054 | -12.91152 | -46.89579 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99bac797-55e6-3a07-8646-cc7369f658b5 | -19.86456 | -43.64639 | 2025-10-03 04:34:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a831acd8-a009-3d7f-9bfa-a3b70e900b49 | -18.23127 | -53.35942 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1474c591-74aa-37f9-81b0-25b093c80553 | -13.75366 | -48.08326 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 347f7ec9-e080-3394-94f2-d95499ac3c94 | -12.80727 | -47.01088 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8266a133-ccc5-3e3a-8b3b-ef5870cd4034 | -14.66544 | -48.25933 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 873ca302-1729-3efa-af86-ace1a81e3692 | -13.15149 | -47.81671 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0b1f9372-d278-3d0c-8396-316c07ac5d2c | -18.257 | -53.31649 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17e17276-5c93-3c98-9adb-a9734e3eec3e | -15.99705 | -50.91779 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 144e3813-12b8-350b-8903-27c5b597a48e | -13.74804 | -47.98464 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47c5f68e-aef2-3c39-9009-c27f470188e2 | -14.93862 | -46.91007 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e3ac0f2-b427-32c7-a9e6-b92d3a9bb1ef | -14.07368 | -45.68169 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f8c9dab-01cf-37e8-9554-558cd3d35ad6 | -16.33635 | -49.94073 | 2025-10-03 04:34:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52a3c8f2-1225-3081-866d-f3165110b447 | -16.34579 | -47.10846 | 2025-10-03 04:34:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f052e9ba-5ead-3063-b339-f760b07b66c1 | -15.99273 | -50.90212 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6f3b3a3c-2d57-3b09-a9ad-37e7b95216c6 | -14.40297 | -46.1687 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db617a0e-1386-385c-8490-702ba7ebcdcb | -14.90477 | -48.33912 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c759f64e-5cfa-337e-aafc-4218d5b085b4 | -13.52 | -47.27092 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aef86a6a-6c07-3ef4-8b87-f04197893c01 | -13.85172 | -47.92485 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c92580fb-698d-3595-b6ee-8a9483cda2c0 | -13.19924 | -47.33489 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 174fa8e6-5ca5-3aa8-a61f-30cf2e2fab27 | -12.94158 | -46.37265 | 2025-10-03 04:34:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1bf7a0e6-a33e-30e6-867c-b75faced8b29 | -13.49009 | -48.5786 | 2025-10-03 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d67369ac-6e79-362f-a1a0-c97364b5bb5c | -17.31936 | -49.38034 | 2025-10-03 04:34:00 | NOAA-20 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 637188fc-62a4-30eb-8de4-03890696f34b | -15.78912 | -43.68395 | 2025-10-03 04:34:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bbe08f35-29eb-3b32-994c-20124868cf14 | -13.1944 | -48.51719 | 2025-10-03 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d1c93417-d9e0-355f-b8d8-0242953a5e7f | -12.38135 | -46.5281 | 2025-10-03 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 802ee6fc-1811-3cd3-bd94-a3d999a02d1f | -13.20431 | -47.87837 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52638073-094c-39da-ab0d-5647af8e0617 | -15.32935 | -47.32533 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de04c7ba-c5eb-3123-bc8d-3710faaeba9d | -14.20664 | -46.05476 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 7e2ea5d6-f4fc-383f-8ba5-26a10611258e | -12.62149 | -46.96875 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf7bcd01-7d94-3cc4-9d0e-6510aa03eaa2 | -14.09987 | -44.30634 | 2025-10-03 04:34:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f99a5653-f52d-3f73-9aa8-ee7a594fb58d | -12.60804 | -49.90892 | 2025-10-03 04:34:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37000d14-50a1-38d7-a8fb-31ef21644003 | -18.01634 | -51.20907 | 2025-10-03 04:34:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ff63248-7244-3c7e-8a5f-16ff23ed9516 | -14.30597 | -45.87591 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba18907d-2aff-387b-8807-a2a6abea7624 | -14.30015 | -46.02491 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9e4997cd-c4ba-3158-a9af-b688682c2e95 | -13.16281 | -47.90184 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1ee16a04-8981-31d6-9773-54b1346330dc | -14.9398 | -46.90191 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 102d4f12-add5-32cf-989e-d3cf7e055beb | -14.74544 | -48.12825 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b5f7e6f7-6e6c-3262-959d-373f93f78470 | -19.45992 | -43.64725 | 2025-10-03 04:34:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 13103bb6-192d-3e69-9a59-40f9728d7732 | -12.61976 | -46.98019 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 549c06e4-7fcc-3d74-a9df-2c1a4f79a0e8 | -12.1933 | -47.81088 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93219ae9-c523-3375-be24-d4a72ca5c2ec | -15.34089 | -46.25628 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 338669d0-c3f6-3cb0-ba24-4c35a1cd13c8 | -15.19254 | -46.40828 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d849666e-b88f-36a9-9773-7f94a7ad5dd9 | -19.23269 | -43.72118 | 2025-10-03 04:34:00 | NOAA-20 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e43cc10b-91b2-3123-9b35-565302c7cf8f | -12.37312 | -46.51075 | 2025-10-03 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b4f1b659-bdfa-38b2-8680-6dcf9447cfb6 | -14.8823 | -46.85096 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| eea871d4-9df7-3bdb-8a2e-baef15e051bc | -13.7345 | -47.91452 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c7290c0-2f03-3d43-a46c-60d4eb0a605b | -14.29903 | -45.88217 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a895af70-97fe-3923-a45f-9cfe2b45e257 | -12.80037 | -47.03335 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 184f9b80-eea3-3b6b-863b-c94175358e1f | -12.59912 | -49.90456 | 2025-10-03 04:34:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92a4d1c4-aa1c-3daa-8e69-56e1d05764a4 | -13.37178 | -47.27903 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 81f092fc-04e8-3440-b156-c5e3ef8a6bcf | -15.25179 | -47.92159 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e01f139d-6269-319a-92d6-9d00341446fd | -13.39902 | -42.64638 | 2025-10-03 04:34:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 80747e1b-0e9d-309a-aa7e-e079ba0676e3 | -15.83116 | -46.24448 | 2025-10-03 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1791ffd1-0793-3307-9167-eea06fd11265 | -13.33209 | -48.12543 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d332641-d056-36e1-afbb-7d8e43b052b0 | -18.20341 | -53.31163 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a2bdc24-ee04-3344-a4c9-20655f6df1ef | -19.71985 | -45.88075 | 2025-10-03 04:34:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7cb7dbf9-77f1-3aeb-9db5-9d8821038165 | -13.28283 | -47.26585 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6f5428b0-2c1e-3575-b7b9-3c15b733eac7 | -14.97673 | -49.9703 | 2025-10-03 04:34:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8446e096-b8b5-343b-80ed-6465a87bad6c | -15.57488 | -46.9499 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a3fc7d6-ea26-3449-83c8-9f146fbce57b | -13.15325 | -47.89667 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2cae318b-39cc-329f-9221-699c6befd2eb | -12.61058 | -46.97081 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| edd1102b-9386-37cd-9020-9c624d56bd67 | -19.46841 | -43.65387 | 2025-10-03 04:34:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 460386fa-ad71-3c28-8678-c5bf4b3c2443 | -11.91146 | -54.83471 | 2025-10-03 04:34:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6921b76e-df25-3158-a487-5ee1f84bf8c2 | -12.80152 | -47.02567 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 13c367e4-2831-3590-84bc-d4f1e3804b65 | -14.87564 | -48.32672 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b62fc7e3-caa3-3463-bad1-c0242f569939 | -14.63278 | -48.13259 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d56bd057-da80-347c-9dc4-f8e3915d3a74 | -13.26567 | -47.26303 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29d417c1-d5da-3463-a442-aa59232e223a | -14.66206 | -48.25887 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| af4b4743-c10b-3d40-a2d3-4a4741d387f5 | -12.92022 | -46.37493 | 2025-10-03 04:34:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ead8cdc7-d6c1-3fdf-ba8a-f8b202cc30b0 | -13.76631 | -47.54136 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README120.md)
