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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 487193bf-1b0c-337d-961b-4daaf8fb2b86 | -12.33346 | -50.73237 | 2026-09-19 04:40:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dfc0562d-b509-32a2-92c2-69d7359a0a78 | -13.60692 | -48.30312 | 2026-09-19 04:40:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f5e279af-1bb1-3f7f-ace8-275f49265001 | -12.97725 | -46.98223 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6719a7c6-bcb2-3fa9-9f2c-3b194d0bf596 | -13.23847 | -46.9011 | 2026-09-19 04:40:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a67458f-42df-3915-85ff-c222e25a3b7b | -9.79086 | -48.33574 | 2026-09-19 04:40:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07a137ce-ba86-3aa7-a950-3f3a890b2a45 | -9.73144 | -48.14164 | 2026-09-19 04:40:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7fdd9418-3966-35d7-93fb-d8d1b5b32ba1 | -12.58335 | -42.22303 | 2026-09-19 04:40:00 | NPP-375D | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 321e8a5e-0f8c-306e-b4c4-b252ac132084 | -8.88284 | -50.78253 | 2026-09-19 04:40:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef36a8c1-171f-3505-a4c7-e62e753dba84 | -9.94917 | -45.27578 | 2026-09-19 04:40:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 31397792-86a5-3dc1-bbe3-50da2ee32136 | -11.12253 | -45.28087 | 2026-09-19 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 015a7632-5775-319e-94fe-a54b16de6be7 | -11.91239 | -50.12064 | 2026-09-19 04:40:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 17d87171-a99a-39cc-9ab0-f3f4af70b76c | -12.98173 | -46.97555 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c38e0c0c-5af9-342e-8339-39f9ccaf99b5 | -9.80273 | -48.32667 | 2026-09-19 04:40:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1f0d34a8-99dc-3da0-9c82-f74633afd0bc | -8.77985 | -48.68856 | 2026-09-19 04:40:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 40a764dc-6836-3111-86d6-a204753c432d | -12.86695 | -46.34626 | 2026-09-19 04:40:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 248a7da3-7f52-34d6-a668-69ab443fb8bb | -10.17306 | -48.45795 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b08ccd1-6075-3614-b812-a6563a289417 | -12.69032 | -45.95147 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f4fa3ec4-efdd-3800-b38b-fe34df1667f6 | -11.79445 | -46.82619 | 2026-09-19 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8239a9f4-9805-3f50-8e2f-3db860834324 | -11.05778 | -49.74544 | 2026-09-19 04:40:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3ad5a2c-28fe-38e9-b5bf-3a994f4ffe88 | -10.20911 | -46.58875 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 241d016f-e723-3508-84c4-772113d1131c | -10.80033 | -50.8756 | 2026-09-19 04:40:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9d140a4e-a096-3626-bc2c-29cb60d1f363 | -7.5733 | -57.69444 | 2026-09-19 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 339b1baf-56f8-3408-8784-6369fb84b4a6 | -8.42349 | -54.73173 | 2026-09-19 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| ff9d9e4e-c32c-3753-9edc-b1f59f914550 | -9.9613 | -46.61401 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 929bdba6-f4b7-398d-a716-52133cdf5e3d | -10.45216 | -48.67589 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cf00e0ea-1810-3b91-aaa9-83022b3b93da | -10.5358 | -46.74195 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2e580a2e-a4fc-349b-b165-674f2e13a6dc | -12.34851 | -50.70911 | 2026-09-19 04:40:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5f995c1a-3c70-3a94-81fd-ad3508a6238e | -13.00338 | -46.97862 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 69aad196-8aea-3686-880a-ba5c09ba85b4 | -11.28457 | -43.50824 | 2026-09-19 04:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd3409f2-13ba-321e-901f-df896cfc3225 | -13.38231 | -48.03262 | 2026-09-19 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 338e830f-9c00-3247-b982-ec7c40c5dea4 | -9.83739 | -50.64727 | 2026-09-19 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 764e93c8-bcf7-375d-847e-5b861020c536 | -15.87842 | -49.89516 | 2026-09-19 04:40:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a94baf7-133c-374c-b4d8-6653bd77f7f9 | -10.83428 | -50.93027 | 2026-09-19 04:40:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6496f8b0-92ae-3a75-8dab-6d938eb7a4f8 | -10.793 | -46.6559 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b93cffef-64f1-35e1-9b10-647253a11514 | -9.90257 | -45.10361 | 2026-09-19 04:40:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc0dd2bb-efcb-3666-87f1-002c5918184e | -11.98325 | -52.45761 | 2026-09-19 04:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b0df68fd-b2a9-3064-ac20-7d199fbb0a5e | -12.37813 | -47.00269 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f798b102-f95d-3d50-8718-06385a98ed3e | -10.09942 | -48.41654 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5694720-7afd-3dac-887c-afd2587a9116 | -9.67577 | -48.33582 | 2026-09-19 04:40:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14228d37-05e1-3937-afb4-562d5e8442df | -12.14051 | -45.14067 | 2026-09-19 04:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e37f75c-02b3-325f-9603-91e3832ea7cc | -10.93453 | -53.95053 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9ab58a31-4091-3d89-b1b8-68757c200950 | -12.74116 | -47.02098 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 57c4f582-2d54-3c0a-b90d-87b582593c84 | -11.97528 | -52.4562 | 2026-09-19 04:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41618fcf-1989-337b-a5d8-12478571c75a | -8.76983 | -48.66359 | 2026-09-19 04:40:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bd40a03d-9f9c-3a2b-8f87-5fb8e113dabe | -10.40266 | -48.33627 | 2026-09-19 04:40:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| da9cb264-2c27-3851-94a7-d382e303d6a2 | -13.38625 | -49.44924 | 2026-09-19 04:40:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2d61f6f-a522-30cf-a146-2092cfe81bc3 | -9.76604 | -46.072 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 17020302-bfbf-3fbd-9164-efe39373cff6 | -9.32684 | -48.17932 | 2026-09-19 04:40:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17d1b1ff-9130-3efa-b035-749c1cd9e4cb | -13.68145 | -48.57597 | 2026-09-19 04:40:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e897b0c-6971-3c7c-9f6f-4027acc54909 | -10.43843 | -47.50821 | 2026-09-19 04:40:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f2a760d-64d0-3935-9b17-c62a8b6fa354 | -9.04043 | -48.7152 | 2026-09-19 04:40:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f9d4bb4e-d0c8-3698-901e-7d81eb11ff05 | -7.57978 | -57.6886 | 2026-09-19 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 54d1c66c-004c-389f-a949-c14be630be4a | -11.77279 | -47.43554 | 2026-09-19 04:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce74783f-7cdb-366a-aba1-0c26d171bcca | -10.18502 | -45.42184 | 2026-09-19 04:40:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 00a4d454-a8e2-3e31-8a50-60cd2e4d2fe5 | -9.91294 | -46.57379 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9acfcb4a-bf51-3998-9b33-685e32fb0861 | -11.08381 | -48.27093 | 2026-09-19 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 101fb293-8d81-33fb-a051-fececb80936c | -8.61402 | -54.61639 | 2026-09-19 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 969d4b56-e773-3106-8392-56e3b9036878 | -12.99558 | -46.98465 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 32bb2274-87c2-3f85-94aa-b055b4342f6b | -12.60648 | -50.73262 | 2026-09-19 04:40:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f325f6dc-93e3-3e2d-a651-3f186aa3c06a | -11.48652 | -45.72985 | 2026-09-19 04:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| af203bd4-bb9a-3624-84f5-44a85ce27d48 | -13.62967 | -48.31055 | 2026-09-19 04:40:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e527c626-dab6-36d2-895b-84778b55cbdc | -11.94197 | -50.13774 | 2026-09-19 04:40:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b064d9c-171f-385c-845f-c13c39b0c778 | -12.14978 | -46.97019 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 04347585-1422-3a44-8f4f-27f8400b60ee | -12.15423 | -47.00746 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad98d4c0-ae46-3b9f-b089-106dc38e891c | -14.68806 | -46.65509 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 16f7423d-5da0-3fe5-85e2-36e4831fcba6 | -9.75448 | -46.59581 | 2026-09-19 04:40:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8644a3ba-2c1b-3b9e-9a8d-a074162a5cea | -13.61396 | -46.92744 | 2026-09-19 04:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| edbc6778-ccb1-3cc4-8f2a-a62a52b3a499 | -9.24122 | -46.20035 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b72947f-34ac-3733-9b33-d8f44e7e331c | -12.13087 | -47.00361 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db456e7d-71a1-3878-9678-605d1d1151ad | -15.78243 | -48.36447 | 2026-09-19 04:40:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 66b5978c-e1ca-37a2-9b5b-4d47ffb3d47c | -8.60813 | -54.59327 | 2026-09-19 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 923ea98f-0da3-3df0-9f37-2704fed74cf5 | -11.12137 | -45.2885 | 2026-09-19 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de10de57-b80d-3a9e-9b98-a2ce4941d41f | -9.26735 | -48.24734 | 2026-09-19 04:40:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a1240e8-41e0-33bd-9407-56eb33d21048 | -11.13915 | -54.02357 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2260f09f-fc97-3da3-ae73-a52674695b6c | -9.78753 | -45.05882 | 2026-09-19 04:40:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d867e3d-f05b-3c6d-8bcb-4cead07eaf62 | -11.81658 | -48.83337 | 2026-09-19 04:40:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48cc511c-2d6b-3917-abb0-c8921256bad6 | -9.69069 | -45.23233 | 2026-09-19 04:40:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ef3c1b7-39a9-3b3b-9f2b-2442ffb0ca6c | -14.69146 | -46.65564 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 67d11c8c-f441-30f5-8e9f-27a481cc9c38 | -14.6807 | -46.68068 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 692420ed-def8-3045-a29e-5998591ad000 | -10.98161 | -49.70471 | 2026-09-19 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b62b8082-e10a-38c6-a299-e2032d6ad32a | -11.29884 | -46.76903 | 2026-09-19 04:40:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b332d782-3e0a-3bce-a6df-fd114d74be9c | -10.07326 | -45.64952 | 2026-09-19 04:40:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b966b2d-567d-36cc-8301-c7d5c99be1fd | -11.30942 | -46.78889 | 2026-09-19 04:40:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d4e544d7-e02e-39a5-b545-b503a77cffae | -10.87192 | -56.2068 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a481b113-5d28-3972-b845-4e1248ffe498 | -13.01509 | -46.94728 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4132f49f-ecfb-3f4f-9dc7-eff6ab6d18ff | -9.94174 | -45.27844 | 2026-09-19 04:40:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85d02441-1522-314e-9121-173fa0765071 | -11.0704 | -48.26873 | 2026-09-19 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d42a9df1-9ef4-3b0f-af10-6329a135a7e2 | -9.48661 | -54.4814 | 2026-09-19 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d7571409-0152-3437-a980-9a37842335df | -10.30822 | -49.95576 | 2026-09-19 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a52a5a0c-a016-3e0a-a004-b0de0eeff41f | -10.46795 | -51.25955 | 2026-09-19 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f66cb78d-c409-32d6-a7b2-01d32b605719 | -12.13754 | -46.98279 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| dc244a15-a205-395b-b435-2c39e8a5d106 | -9.7864 | -45.04317 | 2026-09-19 04:40:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 88b0d547-fc5e-33e1-9455-78224f7227b7 | -11.22269 | -42.82531 | 2026-09-19 04:40:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| be16d240-8ed2-3bdb-b694-30292a00619b | -16.0974 | -49.64349 | 2026-09-19 04:40:00 | NPP-375D | TAQUARAL DE GOIÁS | GOIÁS | Brasil | 5221007 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17237d41-d560-369c-9e7c-bfd758867201 | -9.70024 | -54.8237 | 2026-09-19 04:40:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 03fd560b-3285-31c6-8852-8941d898d78b | -10.86674 | -56.20575 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6594522f-8dc2-332d-bc9f-8691ec1521be | -10.91107 | -53.97853 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec3be5b6-202e-34ac-a063-7182cceb3b2d | -11.43485 | -51.46368 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbe5f3c0-0faf-3184-84a1-5597a8c953fc | -14.93814 | -49.93511 | 2026-09-19 04:40:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 992f86b0-618c-3738-9b19-4a3e304e73d9 | -9.05291 | -48.72496 | 2026-09-19 04:40:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README57.md)
