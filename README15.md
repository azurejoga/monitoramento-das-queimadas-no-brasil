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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9dab1ab4-3286-37f8-8e1e-3f345c63ec60 | -13.66437 | -53.9175 | 2026-06-25 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2336f67d-bf2a-3e87-8a05-fb8946e27320 | -17.34545 | -42.62502 | 2026-06-25 04:51:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 472ce077-8f68-3d97-bb24-01e34694f965 | -18.52096 | -47.24282 | 2026-06-25 04:51:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ae3fc17-b628-3730-9cb3-8555e392ecf1 | -12.55366 | -54.58311 | 2026-06-25 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| beba135d-eb8c-368f-aabb-3cc029e56c74 | -12.54252 | -54.60383 | 2026-06-25 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd313875-b1bc-3bd2-9a99-9f8e22345847 | -12.22225 | -55.49841 | 2026-06-25 04:51:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 410fed79-cf7a-3600-ba0c-09c2f741848a | -17.34394 | -42.62778 | 2026-06-25 04:51:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 53ecd00a-0085-35c0-a368-d31d7b3c2d7f | -18.4616 | -47.258 | 2026-06-25 04:51:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3bd9b814-4b8e-3d70-ab10-7940cc19fe19 | -14.38571 | -47.86617 | 2026-06-25 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9844990e-1bd0-3744-8389-791b7c44cf1e | -13.86997 | -47.14508 | 2026-06-25 04:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5bc69b29-f796-3376-9e7b-23e650027d24 | -14.21417 | -45.63071 | 2026-06-25 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eae24887-9e74-3120-901c-6a8261e5cdf2 | -19.52374 | -42.58852 | 2026-06-25 04:51:00 | NPP-375D | CORONEL FABRICIANO | MINAS GERAIS | Brasil | 3119401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 97329b13-e655-34f9-bc1f-fc80e9beb172 | -17.12213 | -41.34521 | 2026-06-25 04:51:00 | NPP-375D | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7a8568a7-aeb5-3309-b730-246b9f019b78 | -12.2175 | -55.50274 | 2026-06-25 04:51:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2fd1501f-3223-3264-b1d0-c59bf86f774d | -12.22528 | -55.5041 | 2026-06-25 04:51:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 68283dd9-2098-3dcc-a0a8-a1a3d41a9a62 | -18.46209 | -47.25435 | 2026-06-25 04:51:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c292c8d-071c-36a1-a385-c656a89444d1 | -13.07202 | -53.35766 | 2026-06-25 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dcd4e14d-13e5-3b02-9f8f-ddcec55abf70 | -19.52328 | -42.59293 | 2026-06-25 04:51:00 | NPP-375D | CORONEL FABRICIANO | MINAS GERAIS | Brasil | 3119401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7dbc3435-5edf-322c-becf-a2765c03cebb | -18.52502 | -47.24338 | 2026-06-25 04:51:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ba58aef-b6ad-324f-a15e-775d232e63f0 | -13.86234 | -47.14361 | 2026-06-25 04:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b872131-bbab-3818-bae3-1fb789c80efc | -12.55658 | -54.58819 | 2026-06-25 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b7291e29-d2ff-3eac-bff1-971be205b51b | -12.67373 | -54.57987 | 2026-06-25 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4937c2c1-e49b-3c63-b3f8-39f07cf0e0c4 | -14.21364 | -45.63475 | 2026-06-25 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20d92182-ec2d-3bf2-8d58-bfae1fc3ff90 | -13.82867 | -47.01982 | 2026-06-25 04:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e0f1b945-56b4-30cc-b97b-cd54fcb7395c | -17.34435 | -42.62414 | 2026-06-25 04:51:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29479d04-c791-3600-a398-ed3127ce93a0 | -11.94303 | -57.70565 | 2026-06-25 04:51:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5cb4dc82-d062-3e08-a307-0c16616484bd | -15.36945 | -47.35687 | 2026-06-25 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e921825-0cd0-3289-8fd3-3e0bbd71a0bd | -13.85539 | -47.13741 | 2026-06-25 04:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 769b6ab8-534e-3659-a6f1-da918716187f | -19.52852 | -42.59681 | 2026-06-25 04:51:00 | NPP-375D | CORONEL FABRICIANO | MINAS GERAIS | Brasil | 3119401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 25c6ee60-a736-308a-bd0f-68920164749c | -11.94212 | -57.70297 | 2026-06-25 04:51:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d168d32f-d5f1-3ef8-a23e-575f379b071c | -12.55291 | -54.5875 | 2026-06-25 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ce546765-4153-3d05-af73-e5f059a775fb | -12.6884 | -54.58251 | 2026-06-25 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7308bb74-b876-3199-90ed-197ddf6d3ce5 | -12.22311 | -55.49342 | 2026-06-25 04:51:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a4fd1ace-7996-3c20-b267-75bf1b6de79b | -14.2184 | -45.63138 | 2026-06-25 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a1ce062-3179-3d15-af43-74a9abc3528b | -12.22139 | -55.50341 | 2026-06-25 04:51:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b0699523-4fbc-343a-9916-7cb99fae6cfc | -17.34506 | -42.62865 | 2026-06-25 04:51:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fdfdda72-31ec-39aa-95c9-a15d43c3af85 | -13.95367 | -46.19845 | 2026-06-25 04:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55ec620d-f958-332e-ba45-c5488d056948 | -14.2802 | -47.41682 | 2026-06-25 04:51:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85614044-73c1-306f-974c-2a1769dcb106 | -14.28115 | -47.41483 | 2026-06-25 04:51:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d4a647e-e9c9-3d8a-b436-ea3ac6f5d1ce | -13.85854 | -47.14279 | 2026-06-25 04:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0230a9b8-abf7-3a55-a01e-45c37b3ae905 | -12.22442 | -55.50909 | 2026-06-25 04:51:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 92447456-3d40-3080-ae7f-e71a83254c53 | -13.863 | -47.13897 | 2026-06-25 04:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe94222f-5356-3b54-9d39-eb1213d1a9d9 | -13.85158 | -47.13664 | 2026-06-25 04:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e961e86-1b9e-30a3-9834-77805786dbd9 | -17.12257 | -41.34105 | 2026-06-25 04:51:00 | NPP-375D | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ae2636b9-39e4-307b-b7c8-5b502ef8339f | -15.371 | -47.35484 | 2026-06-25 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f4aa8f8-b6e7-37d7-ab75-05ffa33eea1a | -13.06509 | -53.35646 | 2026-06-25 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 41677105-f263-36fa-85c6-7cf054528a6f | -13.85606 | -47.13269 | 2026-06-25 04:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d017e9d-c684-376d-a77a-3ef0e00e6a85 | -14.17777 | -48.9973 | 2026-06-25 04:51:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| df8b471f-5a2f-3f9f-9102-ba06602f5eb8 | -14.21788 | -45.63538 | 2026-06-25 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f2858e7-72f4-3809-939e-ab1ae2dbfaf7 | -12.66931 | -54.58361 | 2026-06-25 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4099d05a-40d4-33c7-a4e0-41100d98c02e | -19.52891 | -42.59304 | 2026-06-25 04:51:00 | NPP-375D | CORONEL FABRICIANO | MINAS GERAIS | Brasil | 3119401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 29f141d1-08a8-3899-a971-2bb323fa950c | -11.90824 | -56.86871 | 2026-06-25 04:51:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1fbd92df-99e8-38f2-a236-5470510ce282 | -13.83641 | -47.02086 | 2026-06-25 04:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc414fb2-f966-3c4b-a0b4-010469b172f5 | -12.22053 | -55.50839 | 2026-06-25 04:51:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bbc429b0-6290-3c11-8cbf-b7fccb856526 | -17.34977 | -42.62485 | 2026-06-25 04:51:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7543c41b-d362-374d-9765-d8b01cd32ea5 | -13.8592 | -47.13819 | 2026-06-25 04:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b25e4941-d2ac-33e5-a1a6-7096a1f34ecf | -12.21836 | -55.49773 | 2026-06-25 04:51:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ea7af735-39ae-31b5-a0e9-8109c5e852c5 | -13.83254 | -47.02035 | 2026-06-25 04:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 667f3c65-119d-3868-927a-bb9821b66344 | -12.55582 | -54.59258 | 2026-06-25 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 352001f4-6fbd-31bd-a8b3-58c051e3b6bc | -12.21922 | -55.49274 | 2026-06-25 04:51:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b09a6567-0d78-3f46-afd8-34aa8c7457df | -17.33965 | -42.62796 | 2026-06-25 04:51:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0864e935-44b0-3ce4-8f0d-1055b6a3227e | -13.06163 | -53.35587 | 2026-06-25 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a05ac4df-74e2-3bdf-acfa-ad934fcd159c | -13.85225 | -47.13192 | 2026-06-25 04:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b406fff-7b40-392d-967b-4802bd4b4f18 | -19.53459 | -42.59275 | 2026-06-25 04:51:00 | NPP-375D | CORONEL FABRICIANO | MINAS GERAIS | Brasil | 3119401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| bc4d8660-fbfd-3cdc-bbf3-acb5ff994510 | -12.21664 | -55.50771 | 2026-06-25 04:51:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00598364-2d47-3a30-b8d9-4ef546341f86 | -21.0771 | -57.45682 | 2026-06-25 04:53:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 00d30add-066a-3fe1-bf05-d0b2ae615292 | -21.09138 | -57.465 | 2026-06-25 04:53:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4e4feed-4027-30a1-8b15-dda373b6f5d7 | -7.7498 | -44.6184 | 2026-06-25 05:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 49abe52b-ad8a-3b94-807c-53c987a947fb | -11.8678 | -51.7473 | 2026-06-25 05:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 289.1 |
| 43012cee-a700-392b-b7c6-96be32fd702d | -11.8865 | -51.7663 | 2026-06-25 05:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 56011bb2-9fea-3039-868e-a02b663fa993 | -11.8675 | -51.7684 | 2026-06-25 05:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 135.8 |
| 63759ab0-5561-300f-8946-9f89387a8735 | -11.8868 | -51.7452 | 2026-06-25 05:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 154.2 |
| e46e585f-c867-3f43-989e-3bf90e49076b | -7.64232 | -45.29545 | 2026-06-25 05:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18d4c47d-938b-36db-b44c-ea6b9aa2d02d | -7.64827 | -45.29646 | 2026-06-25 05:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c32f7b6d-1203-3fbf-9653-8218887d3d3e | -8.126 | -47.89004 | 2026-06-25 05:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 62485f49-14da-362c-8793-eadb1e141446 | -9.19378 | -45.32039 | 2026-06-25 05:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 21c70dea-f810-311b-9bf1-3bb7e986bd98 | -10.28763 | -44.68965 | 2026-06-25 05:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87d737b1-ec3d-3429-81b9-683ac28e6344 | -9.36902 | -50.53827 | 2026-06-25 05:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5179e59-3b17-3917-a81e-1b45b630dbba | -9.53256 | -47.75431 | 2026-06-25 05:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9518032-8705-30b7-9086-6457b653d0e9 | -10.28702 | -44.69469 | 2026-06-25 05:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a7bfc3b-f165-329f-9bb5-75004b429b1b | -9.20596 | -45.32188 | 2026-06-25 05:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2e3319c-0d1d-3b2a-bda6-b9f206274b69 | -7.63081 | -50.21439 | 2026-06-25 05:08:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 90cda61e-391a-303f-81fb-4928ea541e7a | -8.67713 | -47.85799 | 2026-06-25 05:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75e1bdc6-a243-38b2-8847-9c7b96924007 | -6.97435 | -42.88919 | 2026-06-25 05:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e60f33d9-99ca-3c65-a190-cb8adc847bd2 | -7.7551 | -44.62471 | 2026-06-25 05:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ad477509-c498-3739-b131-386111734ccc | -9.18769 | -45.31963 | 2026-06-25 05:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62c58ff1-4163-3303-9185-dbc970619197 | -6.76003 | -46.31449 | 2026-06-25 05:08:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af09d658-3164-31f3-beaf-608901342dd5 | -9.80605 | -48.92086 | 2026-06-25 05:08:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| eb057b4b-4b0a-38b2-9a70-33b0c24b2885 | -8.67671 | -47.86095 | 2026-06-25 05:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8468287d-b320-36be-acb9-360798f4357d | -7.73319 | -44.17992 | 2026-06-25 05:08:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0fdce17a-6f49-3ee1-b0a0-47c566619b5b | -9.57812 | -49.11914 | 2026-06-25 05:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4cc88262-eb38-3dab-88b0-49bbea9e7c58 | -8.8569 | -46.9333 | 2026-06-25 05:08:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 48856200-e59d-3733-b56e-4a5617d57af5 | -8.58037 | -46.90678 | 2026-06-25 05:08:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf7a3146-adbb-3c9a-9236-1265f246099e | -6.97299 | -42.89526 | 2026-06-25 05:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 67de23e7-fab5-38fe-b548-a55ce34c5f6f | -9.58343 | -49.12164 | 2026-06-25 05:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c3ba9dbb-21b4-3c6e-b636-a4de2f15f777 | -5.80741 | -45.05716 | 2026-06-25 05:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 918a274f-8cdc-39e8-8e95-3a636ad51500 | -8.68493 | -47.85974 | 2026-06-25 05:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ae2eb696-2d1b-3e22-b938-45cfdd202d50 | -5.8194 | -43.59326 | 2026-06-25 05:08:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 41af854f-2efc-39a2-a0a4-98287de6936b | -8.33117 | -51.34648 | 2026-06-25 05:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07969c8b-22d1-3434-b3a9-a474bf3da6cc | -8.57494 | -46.90596 | 2026-06-25 05:08:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README16.md)
