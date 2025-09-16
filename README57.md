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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44dae3d7-0dff-3794-98da-b6e1884e184e | -16.01761 | -59.42775 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2959617-72fa-3134-bac2-7aeedf3d6326 | -21.23153 | -46.70182 | 2025-09-16 04:32:00 | NPP-375D | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d7bfd4b4-b781-3f35-88b4-4705a51ae364 | -15.83626 | -53.47339 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| bae8e8d0-6dc4-3418-b2c8-82ad1324de8b | -21.21907 | -46.94904 | 2025-09-16 04:32:00 | NPP-375D | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1c898008-d4b5-3693-99b3-e43f725dda0a | -14.61802 | -46.37782 | 2025-09-16 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba12316c-c908-3b4f-b5bf-0eb45cce98e3 | -14.92991 | -51.66822 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c2a13acf-9d89-34dc-8b44-18ef064c1f59 | -16.28442 | -45.68344 | 2025-09-16 04:32:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7afeca42-b7c6-3519-9587-c087de086451 | -14.50815 | -47.32698 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66aeeafe-7641-36ce-9c66-9d881d92c995 | -16.67821 | -49.75807 | 2025-09-16 04:32:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea985ea8-6afd-3574-96b2-ee580d1e22a4 | -17.72306 | -47.94185 | 2025-09-16 04:32:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 140b27ca-7dea-3385-8dbe-4f9702435b1c | -15.09279 | -52.48434 | 2025-09-16 04:32:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| bab9cce1-513d-3212-9389-bc167d12d361 | -15.99941 | -59.42756 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3a637db-db53-33d2-9ebe-a636eb94256f | -15.53295 | -44.32658 | 2025-09-16 04:32:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 60108fd6-4a07-39a6-9fd3-79f9ecad3f76 | -14.63284 | -46.39584 | 2025-09-16 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6342394e-3854-3745-b501-ba0ba6189cda | -13.74549 | -48.7718 | 2025-09-16 04:32:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 89fd74c2-1083-3031-be82-790ecfdafa9d | -15.99312 | -59.25673 | 2025-09-16 04:32:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df9479e1-7883-3193-a178-1084e3a55558 | -20.41474 | -45.19035 | 2025-09-16 04:32:00 | NPP-375D | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7e273ec1-ee25-3ff7-8b09-f068d2dc2ffb | -15.78255 | -53.44376 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a031371-1ab3-335b-805d-eec70c94dc93 | -14.4596 | -47.28565 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34686f39-7433-37cb-9ae9-df974371da47 | -15.01117 | -47.97905 | 2025-09-16 04:32:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3bbefad6-b0f4-3725-9f34-707c9ae522be | -14.52199 | -47.37037 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43ca9e7e-63a6-3631-8e78-5b461e025c9e | -14.418 | -47.36421 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc948c5d-0edd-31c1-944a-9d6dfcdb10ba | -16.57682 | -49.40955 | 2025-09-16 04:32:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b41b9c1-8ccb-3c96-87a3-a56c09b24862 | -15.16147 | -52.46537 | 2025-09-16 04:32:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 589a8634-0593-3eb1-a66c-e67fa8cf0b95 | -16.01965 | -59.24499 | 2025-09-16 04:32:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 127c923a-3c40-39ea-95f3-8a9296116961 | -13.9304 | -47.99239 | 2025-09-16 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ec4c072-9132-37ae-8c35-2373afe64674 | -15.77263 | -53.45308 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 89048f0a-e1a2-3336-a8d8-d7abfe846ff9 | -14.38556 | -52.90541 | 2025-09-16 04:32:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9cb55710-0d7a-3e66-88a9-8837c6b2a65a | -14.66274 | -46.84269 | 2025-09-16 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3aff224-f291-31b5-bd62-830d1b7658d5 | -16.03074 | -59.45227 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 169619a7-9ba0-3c51-adf3-8c9f91b9f6a4 | -21.19816 | -44.3647 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 92d543ec-80c5-386b-9190-8c07edf572af | -14.63514 | -46.38052 | 2025-09-16 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40a068d9-bb87-3ce6-ac73-851f7fa11955 | -16.52345 | -43.73158 | 2025-09-16 04:32:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b8b54ece-4474-3753-800a-8a433621b036 | -20.4431 | -47.13185 | 2025-09-16 04:32:00 | NPP-375D | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c9c1a22-2ae3-3186-948e-b26409274b5d | -15.81934 | -53.47547 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bafeca97-72a4-3248-89b9-a02f5b3def3b | -14.52369 | -47.35945 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42c6c1f9-43fa-3df6-bf3e-eabfa9ddd3ae | -16.01472 | -59.2399 | 2025-09-16 04:32:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0d3e8f2c-b214-3a95-a2b2-8f34132a4e94 | -14.52253 | -47.38898 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58c85451-9908-3882-a8a8-0e7bf01a4da1 | -14.38646 | -52.90025 | 2025-09-16 04:32:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5aa5de2b-8ce7-36ed-a50f-091d20c1fb9e | -20.60916 | -50.14063 | 2025-09-16 04:32:00 | NPP-375D | FLOREAL | SÃO PAULO | Brasil | 3515905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 0179f90d-67ee-34db-81de-9378c6576ba1 | -15.81727 | -53.46416 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89189c12-28b3-3a1c-a2a4-560207338a8b | -16.70561 | -54.94978 | 2025-09-16 04:32:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4c78cd54-8c15-35ee-8bcf-84694013681c | -14.53765 | -47.35796 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d6699196-1095-3c80-bf7f-d76c33fdef40 | -18.62136 | -43.89626 | 2025-09-16 04:32:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5426104a-0ef4-3428-ac85-781989212001 | -20.09809 | -43.20045 | 2025-09-16 04:32:00 | NPP-375D | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ad295567-d77e-3301-a728-6c9f009624f8 | -15.79341 | -53.45905 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b9749b75-e279-356f-818d-d6572d303a6d | -16.28502 | -45.67929 | 2025-09-16 04:32:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe6edebd-81f0-3dda-a79f-cc208094fdef | -17.07437 | -45.82807 | 2025-09-16 04:32:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 31b86827-6b4f-3afe-99d7-b4470908cb12 | -14.50756 | -53.27911 | 2025-09-16 04:32:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 941b66ef-f712-3312-96f4-26d19264c475 | -14.51863 | -47.39203 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6495cde5-bcd0-3c90-b9ec-6104122cb8cf | -14.52476 | -47.39669 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 86706ff6-c6a0-37ed-862c-3f2e0ef03057 | -18.16164 | -49.20134 | 2025-09-16 04:32:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7c54225f-1d16-35a1-932f-6a053a12389d | -14.50692 | -53.28267 | 2025-09-16 04:32:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56c1951f-4868-3a29-960f-986c76f98eb8 | -21.27158 | -47.01327 | 2025-09-16 04:32:00 | NPP-375D | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 156ab46d-fd1f-3fbf-9763-d286bc45cf27 | -13.9243 | -47.98772 | 2025-09-16 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9bc8a90c-f8d8-30bd-96f6-aeef38e5bc90 | -14.52098 | -47.33281 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a9c5762-a784-3fc2-bb63-c00f1ddab69b | -21.11882 | -45.9477 | 2025-09-16 04:32:00 | NPP-375D | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3dfbad60-100d-3b74-a34a-30f3e5b83084 | -14.94042 | -46.59615 | 2025-09-16 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98e7abec-ba9d-3450-a00b-fc1c7d16471e | -16.02345 | -59.42887 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9035c3c0-2c62-3f3b-ac1c-ad543e3686a6 | -16.5002 | -45.9992 | 2025-09-16 04:32:00 | NPP-375D | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4d54888-03c3-3dcd-ac37-e13366ab93ae | -14.3855 | -52.89673 | 2025-09-16 04:32:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65e063ca-3f49-3ea2-ae3a-b9750ca4530e | -20.44019 | -47.12722 | 2025-09-16 04:32:00 | NPP-375D | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 266aaee8-ac55-35d9-a73d-afb630cd589a | -17.67514 | -44.21191 | 2025-09-16 04:32:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7121ad99-a6c3-3ed9-ad92-5ba1fa5af85a | -15.40828 | -47.34395 | 2025-09-16 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae1c2bdc-f549-3fe6-8905-675a40457d52 | -16.6871 | -49.76715 | 2025-09-16 04:32:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7f3fb34e-7fda-3b0e-b252-929e5eb64d44 | -14.51919 | -47.38844 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87a9f2d5-6aca-369b-b996-4b5bc4914f43 | -14.59982 | -46.38242 | 2025-09-16 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 745a5751-d38d-3a52-b668-74f18f51caf7 | -14.81129 | -51.66844 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ebcb8b91-6344-341d-800c-2e54574ae045 | -16.02896 | -59.4511 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f59089bb-f56f-34ac-b92c-3f13bf24b2a2 | -15.9997 | -59.25408 | 2025-09-16 04:32:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 68ff58d7-59a3-3058-b53d-2ff6d7cdd84c | -19.84784 | -46.4542 | 2025-09-16 04:32:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82022bec-2e3b-301e-8768-cd564c083776 | -15.82428 | -53.47104 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 128ed450-5c86-338a-9ce8-3c5159a0311a | -13.70934 | -49.85511 | 2025-09-16 04:32:00 | NPP-375D | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 800bb8f3-8224-3cfb-9816-5cd0a652a782 | -14.53256 | -47.39061 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b0e8736-699c-350d-8a8a-1f0241477eaf | -21.11048 | -46.47622 | 2025-09-16 04:32:00 | NPP-375D | NOVA RESENDE | MINAS GERAIS | Brasil | 3145109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e8f1157d-3d37-35be-91c4-1f5b0f161750 | -15.15848 | -52.46003 | 2025-09-16 04:32:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8d89f814-08af-3ce6-9aa0-ebab070bab85 | -14.53089 | -47.37929 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4fe70b7e-c777-3a4a-bce5-6999acda4a3a | -17.72832 | -46.7692 | 2025-09-16 04:32:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 787dadcd-7cb7-3323-a41a-93f7807a053a | -14.52755 | -47.40082 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 04cc818a-a5b6-3814-a972-b244d5829973 | -14.541 | -47.35846 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 87679362-0456-38f8-8432-7dd297e1cb34 | -14.27001 | -46.14622 | 2025-09-16 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7565efed-d847-3d33-94e7-7c5d52749fb6 | -14.51584 | -47.38789 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b86fafb4-5ec7-3d80-858f-7d36c2e833a7 | -14.29643 | -49.53244 | 2025-09-16 04:32:00 | NPP-375D | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 969cb23f-f808-307d-bc96-d406f4cd7b5a | -14.52978 | -47.38647 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54f5162c-8662-3e88-9ae9-db482b5cd060 | -16.52415 | -43.72639 | 2025-09-16 04:32:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8543190-4728-3043-b433-a5fe579476cc | -14.52319 | -47.34064 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d164b787-4baf-378a-8bd3-a2ac8541eb93 | -17.7312 | -46.77372 | 2025-09-16 04:32:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1a1d24e3-981f-3b64-839b-884a9a0917f9 | -18.55699 | -49.25444 | 2025-09-16 04:32:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.6 |
| 38eb738d-967d-3078-a65d-bce4a4253fcd | -16.03562 | -59.44841 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e69d335-17e6-3f6f-b5a6-b7eec2626c9a | -14.30322 | -49.5336 | 2025-09-16 04:32:00 | NPP-375D | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b15cc23e-b1d8-391e-853c-d61fb65ac804 | -14.94098 | -46.59237 | 2025-09-16 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ae4df20-cb8a-3904-8456-a22dcdd70777 | -18.61604 | -47.21242 | 2025-09-16 04:32:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38414897-1fbf-3938-b5c8-a01b78b3f358 | -20.4109 | -45.18974 | 2025-09-16 04:32:00 | NPP-375D | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bf15d27a-c5ac-3509-ab1d-d3e5569f01a4 | -16.47688 | -55.1049 | 2025-09-16 04:32:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 29.4 |
| 8a4e23f5-844a-306e-a2fd-e59b3f420fd4 | -14.5115 | -47.32753 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5420e78f-b745-3b8b-aecc-fa82f93e3d63 | -21.20173 | -44.36915 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 22a61222-3ab4-37da-a153-de12815881b1 | -19.08166 | -43.12927 | 2025-09-16 04:32:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 41930a64-bd60-3c72-a62d-78c60937eb95 | -14.53367 | -47.38343 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a1b17013-2261-3e4b-b522-86ad18ad4a89 | -19.38799 | -44.30263 | 2025-09-16 04:32:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e146ca8-f686-3a24-9728-e390dbfdd921 | -19.25983 | -51.43074 | 2025-09-16 04:32:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README58.md)
