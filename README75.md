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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65a361d3-4d5f-3951-b914-fda2a9d2e0a6 | -18.718 | -57.289 | 2024-10-07 04:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.8 |
| 24bf2015-3a34-3368-ad3c-9cffbb3865ed | -18.7375 | -57.3071 | 2024-10-07 04:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.3 |
| aa753358-e43c-309c-ace6-bf9a9c05edef | -19.8838 | -42.641 | 2024-10-07 04:06:55 | GOES-16 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 44.5 |
| 762ed758-5419-3b44-81e2-69fc2fa9191e | -20.4238 | -47.7157 | 2024-10-07 04:06:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 9cf93b8d-5f83-38ff-9d64-71d22c08e57f | -20.4244 | -47.6922 | 2024-10-07 04:06:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 39116ee3-4825-3a60-90ef-781d7b389010 | -20.4443 | -47.7109 | 2024-10-07 04:06:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 134.7 |
| b41556a7-b801-3a19-8ba7-dc60f3939240 | -20.4449 | -47.6875 | 2024-10-07 04:06:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 188.1 |
| 541c3937-295d-3b39-8557-3c29935fa257 | -20.4655 | -47.6827 | 2024-10-07 04:06:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 176.1 |
| 3204d0ef-ed59-380d-8869-c969d98e8f69 | -20.4661 | -47.6592 | 2024-10-07 04:06:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 2909250e-9e03-302f-b93d-dcaa22395260 | -20.5138 | -48.1366 | 2024-10-07 04:06:59 | GOES-16 | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 086cc2f2-8419-3435-8c8c-cae9a01b56f5 | -20.5145 | -48.1132 | 2024-10-07 04:06:59 | GOES-16 | SÃO JOAQUIM DA BARRA | SÃO PAULO | Brasil | 3549409 | 35 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 8fb7ceb9-b5dd-329c-ba3d-57d6f1f734ba | -20.5643 | -48.5183 | 2024-10-07 04:07:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 132.5 |
| fad3de35-34ea-3d2c-b524-6d9eb923e72c | -20.5649 | -48.4951 | 2024-10-07 04:07:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 1d1b2045-351d-3c53-a0c7-a20c5834b087 | -20.5848 | -48.5137 | 2024-10-07 04:07:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 197.1 |
| 99da82cd-260a-3f3d-98e1-680e34bae3ca | -20.5855 | -48.4904 | 2024-10-07 04:07:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 145.9 |
| c00d5058-49fd-34a0-b8c2-6782b256b2db | -20.6053 | -48.509 | 2024-10-07 04:07:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 42adca4d-0e8e-3894-88a6-a607b4577896 | -20.606 | -48.4858 | 2024-10-07 04:07:00 | GOES-16 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 77.6 |
| caa40352-782f-3c83-9751-d7e23e060b1e | -20.7174 | -49.6306 | 2024-10-07 04:07:01 | GOES-16 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 4ae48a5c-2f1d-3bef-b8a4-7841577ce8a5 | -21.3274 | -47.5939 | 2024-10-07 04:07:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 0951be53-8b63-338f-9912-151aa134f6d1 | -21.5698 | -47.746 | 2024-10-07 04:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 5fe5a248-53b4-368d-ad82-4be806f0524e | -21.5705 | -47.7223 | 2024-10-07 04:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 47.6 |
| d0617b5f-093a-34f0-954b-4bb9d0373184 | -21.5906 | -47.7409 | 2024-10-07 04:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 6224d10d-8b74-329c-b8b3-08a0c717f9e5 | -21.5913 | -47.7172 | 2024-10-07 04:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 92.5 |
| c439a2ea-5cd8-3437-af19-ae61ec44f4cc | -21.605 | -47.9485 | 2024-10-07 04:07:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 60.7 |
| d6950954-958a-38e6-b3a5-f2061c083572 | -2.8753 | -52.9192 | 2024-10-07 04:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 55dd3fa0-09d6-34c5-bfa0-40542a10570c | -2.8754 | -52.8989 | 2024-10-07 04:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 42a28d55-87d9-3939-9ec5-9014154fe70d | -4.2729 | -43.737 | 2024-10-07 04:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| e1a074fc-5002-3b67-bf70-6682bce79012 | -8.1945 | -43.717 | 2024-10-07 04:15:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 124.8 |
| c507969f-ed81-345a-86c0-b6dd801a4847 | -10.8754 | -63.9169 | 2024-10-07 04:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 82d5ebb1-7871-3e28-9ee8-5d05afebea0d | -10.8755 | -63.8979 | 2024-10-07 04:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 1ca6e516-6807-34fd-be9b-badebc489fa0 | -11.2847 | -51.3878 | 2024-10-07 04:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| e96b3c2d-25e8-359a-8827-3de2bd8e5527 | -11.247 | -51.3706 | 2024-10-07 04:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 49277d18-2bb3-3077-9785-3e794d651478 | -11.2473 | -51.3495 | 2024-10-07 04:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| fe441227-fae6-309d-aea1-ab4939478d66 | -11.266 | -51.3686 | 2024-10-07 04:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| b4fb3b18-d232-380f-a9c0-80a42f09c8c3 | -11.285 | -51.3666 | 2024-10-07 04:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 7e393417-0175-37d6-94f6-c41a63faf831 | -11.7566 | -44.4897 | 2024-10-07 04:16:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 034d2b0a-c048-3a46-a512-7870674baf92 | -14.0703 | -45.4611 | 2024-10-07 04:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 2943702e-8382-3e54-ad70-2ab5ebafe61b | -14.0893 | -45.4809 | 2024-10-07 04:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 22c006f6-9480-3169-bb7e-2b47dab8d1e3 | -14.0898 | -45.4577 | 2024-10-07 04:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 7d59197a-cd55-3ac2-9515-f169bc3b917d | -14.1078 | -45.5241 | 2024-10-07 04:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| bcbb05d1-020c-306d-9936-24c4b288c43e | -14.1083 | -45.5008 | 2024-10-07 04:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 684a26f7-0ffa-320a-be49-0b3ece1f8f1d | -14.1273 | -45.5207 | 2024-10-07 04:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| bad1e099-6a8a-3ddd-95e3-4b244bd3df33 | -16.5072 | -57.7387 | 2024-10-07 04:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.1 |
| b461e588-45f3-312b-bf71-1cbe2e9cb6a0 | -16.5075 | -57.7183 | 2024-10-07 04:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.5 |
| 27c6d83b-6571-3458-abef-a3fe2dbb4031 | -16.5267 | -57.7365 | 2024-10-07 04:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 107.5 |
| 26e1d320-3860-3be6-a33f-f6455bce4ef0 | -16.5745 | -57.16 | 2024-10-07 04:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.2 |
| 03e89a7f-8567-3722-91c1-971a299a0f79 | -16.5749 | -57.1395 | 2024-10-07 04:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.1 |
| ac67be5f-a535-3dcf-955a-a55912517891 | -16.6136 | -57.1555 | 2024-10-07 04:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.4 |
| cf4a34a1-66f5-36b4-a823-c8da6e211591 | -16.614 | -57.135 | 2024-10-07 04:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.0 |
| 68cd37e4-72dd-3b4c-a843-433b410fb906 | -16.6332 | -57.1533 | 2024-10-07 04:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 120.9 |
| 7985d784-473e-33ee-8eb7-705a3b614942 | -16.6335 | -57.1328 | 2024-10-07 04:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 146.5 |
| 2be74688-73e9-3c3a-8755-f4599d0c1495 | -17.1182 | -57.4039 | 2024-10-07 04:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.1 |
| 5592ec15-9681-30a0-a486-177573c699c8 | -17.0989 | -57.3857 | 2024-10-07 04:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.3 |
| a3af593b-aa42-371b-b99f-54dff962aa19 | -17.0985 | -57.4062 | 2024-10-07 04:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.4 |
| 4f5ecec3-b036-37fc-b561-692c8c572a49 | -17.1185 | -57.3834 | 2024-10-07 04:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.8 |
| d5764223-72b1-398d-a903-16d6d7bbf139 | -17.1235 | -51.7238 | 2024-10-07 04:16:42 | GOES-16 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 9b8f1091-2729-38c4-b90a-b310d927a88f | -17.124 | -51.702 | 2024-10-07 04:16:42 | GOES-16 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 8fd53a59-295e-31a9-bfde-dd9ecb69ea62 | -17.1433 | -51.7206 | 2024-10-07 04:16:42 | GOES-16 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 161.3 |
| cc61cffc-4990-3ade-b23c-85d7cd02e7f5 | -17.1437 | -51.6989 | 2024-10-07 04:16:42 | GOES-16 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 197.9 |
| 0b94ee25-f365-3c76-98eb-f7967406d20f | -17.0319 | -56.6749 | 2024-10-07 04:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.9 |
| e0081104-0bbb-3b13-a11a-aeaae0bbcf45 | -17.0982 | -57.4267 | 2024-10-07 04:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.6 |
| 1e9fe923-8ad1-3951-8847-52c97977af3b | -17.012 | -56.698 | 2024-10-07 04:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.7 |
| 1394764c-95e4-3bac-8672-3a27e3fe53c9 | -17.0123 | -56.6773 | 2024-10-07 04:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.5 |
| 995271dc-6779-3393-84c1-e7b5511a276e | -17.1584 | -57.3377 | 2024-10-07 04:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.3 |
| e1163c23-5d5d-35f3-b005-b90aee39c273 | -17.1581 | -57.3582 | 2024-10-07 04:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.4 |
| f418ee9e-e5a0-3bd5-bda4-7c36180bf442 | -17.1375 | -57.4221 | 2024-10-07 04:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.5 |
| 3c3e3f27-9ea0-3bde-9146-4252b2f632e3 | -17.7918 | -53.8102 | 2024-10-07 04:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 3ae65220-bf5f-3929-8ec6-cecac5ab92e8 | -17.7724 | -53.7918 | 2024-10-07 04:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 103.4 |
| b84b904a-7d17-3a89-a2d2-5e85e1b6a0d9 | -17.7922 | -53.7889 | 2024-10-07 04:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 153.6 |
| f1c44035-13c6-3748-b6bd-3682d36506f5 | -17.772 | -53.8132 | 2024-10-07 04:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 94.6 |
| d061fa37-757e-3e9b-ab42-3ce103ea795a | -17.8319 | -53.7829 | 2024-10-07 04:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 828b3228-b9d3-3726-9e62-cf60ed949360 | -17.8314 | -53.8043 | 2024-10-07 04:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 80f902bf-dc13-3a83-9797-89f1563042ac | -18.4523 | -53.495 | 2024-10-07 04:16:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 73.4 |
| e7bc2747-6f46-3d51-8162-ed1d5036b677 | -18.6391 | -57.2578 | 2024-10-07 04:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.4 |
| 48199869-6c00-3cb8-a347-fe09ef3f1fcd | -18.659 | -57.2552 | 2024-10-07 04:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 36.8 |
| df1505b3-85de-3b23-903f-a2e55ec45fd4 | -18.7176 | -57.3097 | 2024-10-07 04:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.3 |
| 0d90c063-f494-3672-8319-df4c2264f2e2 | -18.718 | -57.289 | 2024-10-07 04:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.4 |
| 49b06f33-0ac2-3771-8aa3-312a490dcb1e | -18.8886 | -54.5587 | 2024-10-07 04:16:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 6ca9f802-1887-333f-bf35-d27018648db6 | -19.883 | -42.6663 | 2024-10-07 04:16:55 | GOES-16 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 46.5 |
| 321c925d-df61-3104-a6d9-c5011670206b | -19.8838 | -42.641 | 2024-10-07 04:16:55 | GOES-16 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 55.0 |
| 3de1d2bb-cd36-3bde-825a-3bbea685ae27 | -19.9044 | -42.6353 | 2024-10-07 04:16:55 | GOES-16 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 46.2 |
| 8350df78-6e62-341e-83b1-1406432f5def | -20.4443 | -47.7109 | 2024-10-07 04:16:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 86b9ef0f-48c2-3c33-929f-0d3b3490fa40 | -20.4449 | -47.6875 | 2024-10-07 04:16:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 00ccb8d6-1f3b-37b5-97b7-a0207f5c10c2 | -20.4655 | -47.6827 | 2024-10-07 04:16:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 162.5 |
| b6582fb3-6202-3d29-a2ab-394342bf2fbe | -20.4661 | -47.6592 | 2024-10-07 04:16:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 2b927833-7473-39c3-911f-cadd2f6ebd0d | -20.5145 | -48.1132 | 2024-10-07 04:16:59 | GOES-16 | SÃO JOAQUIM DA BARRA | SÃO PAULO | Brasil | 3549409 | 35 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 6da76036-8a9d-302e-abaf-3c21ea74108d | -20.5848 | -48.5137 | 2024-10-07 04:17:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 99.5 |
| c02ee05d-bd43-3f77-8ce0-cef24e99d2cf | -20.5855 | -48.4904 | 2024-10-07 04:17:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 940ad322-cf3e-32e7-a4f1-a8753c00c29f | -20.7168 | -49.6535 | 2024-10-07 04:17:01 | GOES-16 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Cerrado | 82.2 |
| cc21b8d9-10c8-3adf-b0a1-cfb8d9ed81fd | -20.7174 | -49.6306 | 2024-10-07 04:17:01 | GOES-16 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 1e506d62-b17e-3ad6-9d19-4007591397e1 | -21.3274 | -47.5939 | 2024-10-07 04:17:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 46740ef3-4825-3c4d-8075-1787224df125 | -21.5698 | -47.746 | 2024-10-07 04:17:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 100.2 |
| b0858b38-d8ad-3ed0-aecf-7cc80529aae2 | -21.5705 | -47.7223 | 2024-10-07 04:17:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 7a3a92e0-c3e0-3ed0-a594-7158a5408c1d | -21.5906 | -47.7409 | 2024-10-07 04:17:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 4dde1569-95f5-3108-94c9-28170e03997d | -21.5913 | -47.7172 | 2024-10-07 04:17:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 4823bfed-6470-3836-bd58-914136d96c2f | -1.0182 | -53.7189 | 2024-10-07 04:25:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 90f632ce-fac9-3105-a1d4-9760c57316ee | -2.857 | -52.8993 | 2024-10-07 04:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 41adb01a-60d2-3512-b2b5-b33001ba7aa9 | -2.8754 | -52.8989 | 2024-10-07 04:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 126.0 |
| bf23f18d-76f0-39e8-a105-fead0663bd86 | -2.8754 | -52.8785 | 2024-10-07 04:25:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| c4497759-461f-3300-9291-fb52b67d8a65 | -2.8937 | -52.8984 | 2024-10-07 04:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |


[Clique aqui para ver as próximas entradas](README76.md)
