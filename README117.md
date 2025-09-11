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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20788f11-2645-383b-ae7d-be981957b12c | -13.26815 | -43.7505 | 2025-09-11 04:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d40553bc-01d2-3125-8ee5-296391271c11 | -12.03646 | -50.93365 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f104399-4217-36e0-ba46-b3bfa18b4674 | -15.80781 | -52.28358 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6dc9630f-9dfc-3075-9cf1-458f8b14189b | -14.34204 | -45.06594 | 2025-09-11 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad3100fa-d90a-3782-a096-e7c5d05810a1 | -12.86074 | -47.95883 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e2fac97c-376b-3cb4-8cc7-480fc130e23e | -9.07065 | -49.83955 | 2025-09-11 04:46:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15d0e7b5-1a74-3fb9-b9fe-4ee41fed864a | -9.38176 | -46.77164 | 2025-09-11 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d942a1a6-cc72-3fa2-bfc1-87a5091c7577 | -11.10252 | -48.41929 | 2025-09-11 04:46:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2f0f7376-b968-3ff1-87ef-ec1a927f2cdc | -11.68166 | -46.91046 | 2025-09-11 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76c57772-645c-3be5-96fd-131822069f5c | -11.49035 | -43.65312 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3983f196-3fec-3e98-86cb-ae3d6998adaf | -11.71346 | -50.64402 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 52f84e98-bebb-350b-af6d-62430cf50692 | -9.80354 | -61.52268 | 2025-09-11 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1193beaf-18b5-3c95-8f49-234ea07d0989 | -11.87835 | -58.80469 | 2025-09-11 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97497e06-af4b-3311-8710-b99642238118 | -12.92459 | -54.77584 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ccea7b69-3247-381f-ab15-373786e48d66 | -11.98869 | -47.59144 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 85d9f27f-e6d1-39fa-96dc-cfc017b50cec | -11.15318 | -45.28888 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 40a1b901-b346-3080-817a-bcda1b405f01 | -12.96148 | -54.74644 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90319e3b-34ae-3baa-b676-f1fc79e6d98a | -15.67441 | -47.02268 | 2025-09-11 04:46:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 53d9ea57-b725-3b50-ac18-f30b16543eab | -9.13577 | -47.01055 | 2025-09-11 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 531ce01e-8494-31a8-a337-9e815f74deab | -13.90727 | -47.99153 | 2025-09-11 04:46:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ed282df5-c7da-37c2-8a22-1271777d26cd | -11.48739 | -43.65962 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7bba1f66-399f-32f0-a5fa-40f0ff4302d7 | -12.96879 | -46.73739 | 2025-09-11 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f17729fe-61c1-37eb-99ea-0c4e52d4cda1 | -11.48605 | -43.64642 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fc77b0f1-58e3-32a4-ad1f-e106d47c0732 | -13.84168 | -47.35456 | 2025-09-11 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f050bff7-d2b1-3ae3-8aa8-dd8df8e2e358 | -8.52043 | -51.39346 | 2025-09-11 04:46:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 76d8cd9a-9100-3a6c-b2a1-2fb59c75a20c | -12.06106 | -64.1721 | 2025-09-11 04:46:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 971897f5-e54d-36c1-8859-6c594775cb52 | -11.82077 | -46.7471 | 2025-09-11 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3116347a-c50e-3830-8554-de597229f5e4 | -15.82835 | -52.23878 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 37c226fa-fe9a-3c4a-a6a8-3e3d163418cb | -12.04013 | -47.5413 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2a174cf-af6d-3aae-bd93-16263d53f0bb | -9.45767 | -46.69985 | 2025-09-11 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1d2b52bb-8a08-32ca-9b73-8fc2837d5dac | -15.13904 | -52.44205 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9c72873f-3491-31e9-bea6-a29b6c7894bc | -13.16581 | -45.28216 | 2025-09-11 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| dc78065b-9d21-3fb8-8960-9c00bf462a3b | -13.59124 | -47.67286 | 2025-09-11 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84f5d022-5049-3cb5-aa59-bbea686c32fb | -12.92308 | -54.76362 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3336a256-6b60-3d6e-a1dd-079c8c9a5b6f | -12.06725 | -64.17346 | 2025-09-11 04:46:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 673d4554-6f62-3411-a917-d11d44604168 | -11.76595 | -46.49372 | 2025-09-11 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d2d4f68-e161-30b9-a4d3-b0cc6851385b | -15.95645 | -50.22144 | 2025-09-11 04:46:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 76b446ad-36f4-32ae-a45c-2cf29bbfe6e0 | -14.56822 | -48.77147 | 2025-09-11 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e6477a49-a664-3d61-8950-c0bd48a29f3d | -11.02062 | -45.06239 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 9b263a1c-c8a1-3e08-b4d4-4806614725d7 | -16.89011 | -45.82662 | 2025-09-11 04:46:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3f12d1ee-9baf-3100-80a4-435411eb1ddf | -9.51515 | -54.65073 | 2025-09-11 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7210debb-0813-358d-8282-e01a28e37571 | -8.61154 | -54.69999 | 2025-09-11 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f58034b-dce7-3bd4-b528-f4858d004777 | -15.55143 | -54.76863 | 2025-09-11 04:46:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02a465c7-83dd-3385-948b-fedd8ca2fad5 | -13.26894 | -43.74413 | 2025-09-11 04:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60f0fe27-9a07-381d-ac7e-ee828b09184c | -14.41391 | -47.32301 | 2025-09-11 04:46:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| db198bef-48bc-3636-b935-8c6894d2d856 | -10.56603 | -43.66443 | 2025-09-11 04:46:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1480c7f4-f606-3ed9-b046-74448c146d29 | -16.06481 | -48.133 | 2025-09-11 04:46:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c300a2ba-9509-3804-8a7f-010e88286625 | -13.25466 | -51.77225 | 2025-09-11 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88f90f68-673a-351a-8772-43b541f7f8b8 | -9.9204 | -49.86704 | 2025-09-11 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7542ff8c-9996-3b6d-b806-1ccb2dd7980c | -10.11624 | -48.18 | 2025-09-11 04:46:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 939aea91-e84a-37c2-85cd-a6e076e65ebc | -14.50252 | -53.95134 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3c75db4-7871-3b81-a00c-0ab46185b46b | -9.01996 | -49.78232 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fceac029-3ef5-3dee-9797-148070828373 | -9.89644 | -49.90946 | 2025-09-11 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 876465eb-57c9-32ea-b7ce-ed9497910e7f | -11.6524 | -46.9105 | 2025-09-11 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 741a38ce-878d-3964-8493-29dabe8917ba | -13.25521 | -51.76867 | 2025-09-11 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25f7f0c3-2fa8-35b0-bc23-12872f737145 | -10.17785 | -44.76497 | 2025-09-11 04:46:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b762a662-275c-39d6-a2cf-00b763826e62 | -12.9367 | -54.80995 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c15381da-3a90-32b4-8b82-9e4fa85af116 | -11.47519 | -49.25016 | 2025-09-11 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d7cc1ca-b4ae-38d5-9679-a043aef4aac2 | -11.40841 | -43.54145 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7fc95cc-4f62-3efe-bd0f-e564629782a2 | -15.19542 | -44.04455 | 2025-09-11 04:46:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0d356f3-554d-38f3-8175-6ce325d5d68c | -15.07798 | -50.0575 | 2025-09-11 04:46:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2bce50d3-7e02-3542-8582-65fadb101db3 | -11.7293 | -50.65405 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 886c4297-2ffb-3694-b199-a86bd24232f0 | -14.14249 | -45.41045 | 2025-09-11 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8fdc1cd7-ce91-3c50-bcc3-ed180da4aae1 | -11.49097 | -43.67248 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01332c25-7293-3bde-b7a5-bbff1506d91e | -11.80261 | -46.75597 | 2025-09-11 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5d9e6d3d-772a-3268-87ec-2a152d9fa3d8 | -11.48677 | -43.68032 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f0cfeea-4460-3e41-aa3e-854c7a0c136c | -11.09212 | -51.33818 | 2025-09-11 04:46:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b04b126-2c40-30f4-8bda-1abfe9735f5a | -13.84569 | -47.35583 | 2025-09-11 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fbeb8241-1701-372a-b902-8ec65564c013 | -15.28624 | -53.78997 | 2025-09-11 04:46:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f89220a-a2eb-3882-a558-a222dd4fe7c4 | -12.96991 | -54.75986 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89211ec9-4d05-3433-98d4-620788d151f6 | -11.71767 | -46.50034 | 2025-09-11 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b1801e4f-42d5-3927-b372-a8a3152ea7af | -9.67645 | -47.52602 | 2025-09-11 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 261d9ab5-8f6b-3bfb-b64b-6cbbeeb8476d | -15.80224 | -52.27525 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8bbda114-8f71-3484-ba6c-37d24be5bfd5 | -10.74048 | -48.90372 | 2025-09-11 04:46:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59bd57e4-22bf-3f86-aedd-ef2256eb00f9 | -15.2283 | -44.03552 | 2025-09-11 04:46:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22955bc2-d133-3084-8c47-7ca0a2341283 | -14.50528 | -53.95554 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 114d29ee-5859-31fb-9d38-34db8f179551 | -10.01519 | -51.73587 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ae24d95-fb8c-3128-900a-9bff72917544 | -12.95666 | -46.73165 | 2025-09-11 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7567decf-ce9b-3052-a6b0-445772b0fdec | -10.06031 | -50.37309 | 2025-09-11 04:46:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bed86d3f-4161-31e7-bc75-cca658c714b6 | -15.16399 | -52.32454 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c29c75f1-bda7-3a82-953b-48d55dc89d5c | -9.98636 | -51.70237 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba7b5543-d47f-3868-afa0-cadaab5839d8 | -12.16214 | -48.48973 | 2025-09-11 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 666a9bba-32a7-3250-964e-194303f48617 | -9.99796 | -51.71495 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc5bc264-a102-38d7-80fb-be5f4fd538c6 | -9.76225 | -51.05246 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24ab28d9-0f59-3c2c-9c1c-1b33579163f3 | -9.72099 | -48.09322 | 2025-09-11 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6bde68bf-f3ae-374d-b505-5a233d189d47 | -14.28861 | -54.76442 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d97310e0-8111-3d7d-b476-d245d24f5332 | -11.15009 | -52.033 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd4d1c18-ba47-31dd-9afe-f81d6ecc7366 | -12.05557 | -50.94414 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 01009b0f-d2e0-3b26-99f4-e83cf31db9c2 | -13.1374 | -54.9114 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 302850e1-c55c-3c4f-a508-e04a75627cbc | -12.06207 | -64.16714 | 2025-09-11 04:46:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4fbe7cbb-7684-3753-ad46-ca27a8c9b3fc | -9.80406 | -47.785 | 2025-09-11 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d076646d-5d78-3afb-9746-ea5a67919f8e | -9.07867 | -50.46998 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 045d51c3-d4a7-382f-a5bf-b612f62623e7 | -15.14249 | -48.61656 | 2025-09-11 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0913b457-7c93-38ff-a5a8-37b8f7c2e41f | -10.40722 | -50.52653 | 2025-09-11 04:46:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8ef71fa-5f16-3df2-93ad-3d011e56bdbd | -15.83393 | -52.24709 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dcf24ac1-057c-34e5-92ed-dd0313519e38 | -10.11427 | -48.18181 | 2025-09-11 04:46:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 158e0aef-9e6d-351a-b9d8-b534a9ce500f | -15.13931 | -48.6112 | 2025-09-11 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7844bbc4-2f31-30ed-a0fd-88bc8cbcec85 | -9.8119 | -47.75782 | 2025-09-11 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 990074e6-6c94-391b-b3bd-01e1e23f6cf9 | -15.13517 | -52.44507 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0a8b53e3-1cf6-373b-9bf5-9b5cb7c9dfb9 | -11.68577 | -46.91097 | 2025-09-11 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README118.md)
