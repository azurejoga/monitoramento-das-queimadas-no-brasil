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
| 598efda0-0bc8-3d3e-b5a9-72a45b683044 | -15.0892 | -50.06838 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3bc39ce4-0411-3a2f-8fba-c4d025245005 | -18.03048 | -47.14886 | 2025-09-10 04:44:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| bf867690-ed6e-3550-b5c1-ecc3fea6514b | -15.14363 | -44.03005 | 2025-09-10 04:44:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27687338-d387-376c-8012-e2b7b3650ae9 | -15.27848 | -53.78897 | 2025-09-10 04:44:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0241744f-6ceb-3e75-a34e-9b650e426628 | -12.01366 | -50.99005 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d8c7c756-969f-3475-b132-a9ebc406fdaa | -18.05904 | -50.72787 | 2025-09-10 04:44:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1f834c3-9fe5-3e10-b235-f67e97f2d9b4 | -12.54858 | -49.10282 | 2025-09-10 04:44:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cdd2f5e9-fb97-3896-9c0b-4f45e30045b2 | -14.90639 | -50.12302 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 87f7c91e-0960-3bf8-b75d-05107c9c56eb | -15.86162 | -51.827 | 2025-09-10 04:44:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb77a76a-673c-3945-90c9-db666dd56eee | -16.05817 | -49.97119 | 2025-09-10 04:44:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e2cd848-5fb4-3c06-a0bd-b98885eb648d | -12.92737 | -54.76525 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 66314732-1dac-35bb-92ff-ce640c904ecf | -16.62565 | -51.82923 | 2025-09-10 04:44:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9862f5d5-9ff5-3aac-8ccd-b800c267913c | -18.12963 | -51.72381 | 2025-09-10 04:44:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 477a12b1-7e89-3fae-aa3f-a0e5cb7adc8a | -12.01891 | -50.99435 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fc9aa836-ca2a-3a99-84ed-15dd9f455d29 | -13.82217 | -43.86224 | 2025-09-10 04:44:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b78d3667-8159-30f9-bd85-03a17c34af17 | -16.46548 | -50.66404 | 2025-09-10 04:44:00 | NPP-375D | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b76aea6-4f9d-3b97-a140-e4511f41a540 | -17.32243 | -46.70014 | 2025-09-10 04:44:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc6e1c53-7d1b-39f5-a049-89a809a44ac0 | -15.09769 | -50.08098 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 41c4432e-3f8a-31e0-9485-7a6d360bc0dd | -12.93756 | -54.79553 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e7f3bffb-9c7b-3f23-93e3-18e31319e071 | -11.21735 | -54.99509 | 2025-09-10 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 304dad74-57cb-31e8-a990-9314f60b06c6 | -12.61286 | -56.96777 | 2025-09-10 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 841ea19e-9df1-3bad-9e6f-bcd8f1c77737 | -11.5977 | -52.21203 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73de432b-da68-30ff-ab50-e42247c6957e | -13.11933 | -54.92926 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 249f7c64-d794-3dd4-8119-5b2b1e7526b4 | -12.93192 | -54.76133 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5f017b4f-8def-39fd-8f46-abe466e893ee | -12.93596 | -54.80478 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a6f1d521-94a6-3f43-b71e-644e471ade97 | -13.29059 | -51.72261 | 2025-09-10 04:44:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d7bc1c47-23ab-308f-a198-4ff2b465702f | -12.06262 | -51.06324 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52a16dff-6bc5-3c7c-9614-e35017fc1047 | -13.93957 | -48.26217 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a2758bbb-a31f-325a-b81f-c95f39836be6 | -13.13235 | -47.15559 | 2025-09-10 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f068bb15-bd0c-3fa7-8c0d-9e890dd136a7 | -16.0542 | -49.97436 | 2025-09-10 04:44:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 719b2902-f45d-3af8-bf83-0ad4981bcc63 | -15.85815 | -56.08474 | 2025-09-10 04:44:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 977bebc5-a6f6-3e1d-a649-506a29054995 | -17.24381 | -46.08256 | 2025-09-10 04:44:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6059f68-1504-3d56-9d5f-fc1c83beb85a | -15.47764 | -49.3844 | 2025-09-10 04:44:00 | NPP-375D | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 56700be7-c150-3cdd-8e49-230cef2dfb25 | -12.552 | -49.10336 | 2025-09-10 04:44:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33fa1098-ee76-35b5-b01e-988cfab79307 | -11.293 | -53.95265 | 2025-09-10 04:44:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e49e1ee-f68b-3aa5-bbba-21e0c349725d | -19.68861 | -46.17485 | 2025-09-10 04:44:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5635dde3-a470-3fcd-adac-933c85a7f8b9 | -15.66014 | -49.93257 | 2025-09-10 04:44:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 547a9315-4881-3ca6-9b2d-af0856dc8f80 | -13.1822 | -47.2632 | 2025-09-10 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6893856e-6943-3291-ae4f-d8daf6eb2e31 | -14.91056 | -55.85827 | 2025-09-10 04:44:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0fd454cc-cc1d-3b9c-b1e8-0afcf2d9b96a | -15.79974 | -52.25711 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47fe742e-36d7-3b06-8883-b22a3b49b55a | -17.19721 | -50.1581 | 2025-09-10 04:44:00 | NPP-375D | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d461805c-2639-3cf8-bcfb-ec99936b5c86 | -15.09321 | -50.08763 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7376c2da-91f3-36a9-a71e-c37a9698f6d6 | -15.80918 | -52.26247 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d4fc7ce-c0b7-3b44-a404-d7fdd6adfee4 | -17.73818 | -44.48936 | 2025-09-10 04:44:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ef622b87-d094-3768-abdb-1dab7225b3b0 | -14.88921 | -55.86295 | 2025-09-10 04:44:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9283743c-c67a-309e-b617-1bd2bb41291d | -12.06872 | -51.06787 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8be3d59d-12d6-373c-a8ce-d39084f204ac | -16.62326 | -49.7589 | 2025-09-10 04:44:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2863829-e0c3-395d-acb6-aea001b73af5 | -11.20652 | -54.98814 | 2025-09-10 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bd88ffb0-16a6-35d6-9836-5d176af958f1 | -18.13906 | -51.72916 | 2025-09-10 04:44:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 39becad6-02be-36c9-8788-eb774988d24a | -13.02901 | -48.01545 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f45b3f03-4e2e-33e7-a706-c5747fd25f88 | -16.62149 | -49.77073 | 2025-09-10 04:44:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70f5aad5-db41-36da-97ac-89525277171c | -15.16207 | -52.32029 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e532769-6bb5-30c1-ba24-e37d67048e7e | -15.02192 | -49.26007 | 2025-09-10 04:44:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3147c47-a8df-3ce2-affc-c8024a12a96b | -17.58539 | -49.81898 | 2025-09-10 04:44:00 | NPP-375D | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70e261ee-8628-38cc-95cf-0a727947393b | -14.45857 | -53.34008 | 2025-09-10 04:44:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4a67cf6e-e60b-3df3-b0c0-b0c84fdeb3d0 | -12.1803 | -50.62207 | 2025-09-10 04:44:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1dca1b78-7d2e-337d-b568-07b639830386 | -17.34034 | -46.72139 | 2025-09-10 04:44:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 38897864-2fa1-37e3-8b32-b006523b2ca7 | -16.04284 | -49.98022 | 2025-09-10 04:44:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 277597fa-edd5-3768-9c00-1d3c6e19f657 | -15.01088 | -48.02835 | 2025-09-10 04:44:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 418d090e-19cf-34d0-8212-09c87bcc085e | -13.03926 | -47.16507 | 2025-09-10 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bcb608cd-2be9-365d-87d7-0eed0c56942b | -12.95381 | -54.74648 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a6aa1465-b38e-3e0b-9b6f-c0b0f62cb73f | -11.60533 | -52.20887 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4cf69835-4981-39bb-ad52-b5b6972bd859 | -13.0326 | -48.01593 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd662bc0-2c43-323d-9d7c-c657b749a781 | -18.69883 | -52.59149 | 2025-09-10 04:44:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d7f4822-d767-3bd2-97ef-045380e15832 | -13.31406 | -51.71506 | 2025-09-10 04:44:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb96c2bb-b843-3b69-8c3f-7c6cae1fab75 | -13.02127 | -48.01834 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 094dab9d-4152-3464-88eb-8a4b4f8fbb3f | -12.92657 | -54.76985 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5c748a9-c6f6-3636-93fa-ac0937a98dcb | -15.47766 | -49.36047 | 2025-09-10 04:44:00 | NPP-375D | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef678ede-00a4-30ac-895d-2ec13d11fc46 | -12.84305 | -52.9485 | 2025-09-10 04:44:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03593bfe-060e-357c-87aa-ae3c6ef11fc7 | -14.58397 | -52.11166 | 2025-09-10 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a466150-a881-305a-abae-8e8b6b736e5b | -12.88198 | -47.97192 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 96dd31a8-ab41-33d3-876f-974ca7bba80c | -15.09313 | -50.06533 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 117d0e6e-63b1-38c6-bfa7-0a225e5e5552 | -13.17849 | -47.26251 | 2025-09-10 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 046fd903-0b3c-330d-a68b-58d51f00fc87 | -16.38858 | -46.87496 | 2025-09-10 04:44:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 475090a4-5135-33ab-8358-9284b7d5eb5f | -14.58339 | -52.11527 | 2025-09-10 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a6a8e04-bd82-36e5-9471-649182337c80 | -12.92201 | -54.77379 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4625df5-b2f8-37e9-8fce-bb3fff037692 | -11.94024 | -50.77176 | 2025-09-10 04:44:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b776d661-e10a-33b9-beca-ba761ba77201 | -14.78466 | -48.23127 | 2025-09-10 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa47d030-cc2e-3bfd-af0f-00134ee0c089 | -17.309 | -46.7397 | 2025-09-10 04:44:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e63d6ce-08a4-3951-a402-73521ad84dd1 | -18.95834 | -42.38966 | 2025-09-10 04:44:00 | NPP-375D | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b152310e-9a79-35c4-aed8-60d4b93765d8 | -16.62775 | -49.77603 | 2025-09-10 04:44:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5b620b76-d09b-3c62-a218-6b146158bb5d | -15.16608 | -47.9603 | 2025-09-10 04:44:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fb81472-66de-37fc-aa67-d5def2dcaf8b | -16.54581 | -55.13804 | 2025-09-10 04:44:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0d8443a5-a1ec-36ed-9b7c-50b6cd034330 | -12.9263 | -54.79354 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 143e9bc0-78ed-3a63-a964-0bb155a56ebe | -12.92817 | -54.76065 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7cdd872f-5133-3124-8470-fb671c87d8e9 | -15.27915 | -53.78501 | 2025-09-10 04:44:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 50efbe01-e2a7-32d8-8cf3-f763ef7477d0 | -13.15338 | -45.28999 | 2025-09-10 04:44:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5c4c747-b563-3719-9284-ecb2f087a371 | -19.29848 | -47.98462 | 2025-09-10 04:44:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d4db275c-b3d7-390e-b7e7-d679ab77dc22 | -20.15518 | -43.65746 | 2025-09-10 04:44:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 54a3deaf-7b24-3568-a769-26ee32df1e41 | -13.2945 | -51.71958 | 2025-09-10 04:44:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8d7e28f9-a60e-3f33-b036-50b39b6b0abb | -18.46089 | -46.47144 | 2025-09-10 04:44:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81f2d2d5-94b4-387d-be42-8e9a92564a7b | -13.13607 | -47.15804 | 2025-09-10 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 987df889-b6c6-3aa4-82d7-104480b40d9c | -14.89503 | -55.85559 | 2025-09-10 04:44:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a76e7535-ab2d-3ecc-beaf-c6eade6b8d60 | -12.98912 | -48.02803 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3941e3a9-66cb-322c-88be-3dd24c7034c4 | -17.3023 | -46.72766 | 2025-09-10 04:44:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 04c885c7-21a5-326c-96a3-16f5ccb0c2ad | -14.33093 | -47.29699 | 2025-09-10 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d453f74a-def2-3213-a45f-ade842d59170 | -13.97708 | -48.21963 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1032bf61-a664-3ad6-a202-f0484d5140b2 | -16.12581 | -55.86679 | 2025-09-10 04:44:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c50244fe-fd4e-38cf-b637-b246f26537d5 | -13.92642 | -48.25219 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a388567c-2f30-3fd3-b13a-6449d3dd5ca4 | -17.23958 | -46.08203 | 2025-09-10 04:44:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README76.md)
