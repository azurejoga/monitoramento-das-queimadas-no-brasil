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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 839d2d68-ef9d-399b-bf1d-0398962758db | -17.44925 | -47.19133 | 2026-06-10 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 988c672e-126d-3206-886f-35aedb3b3c14 | -14.40347 | -45.55954 | 2026-06-10 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91c247ac-486e-3007-9969-f3448713f1a9 | -12.31287 | -46.7385 | 2026-06-10 04:32:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd8bfcd0-afc0-35ee-9655-22b28248799e | -13.95953 | -46.18827 | 2026-06-10 04:32:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 442cc7f1-2283-343b-b0a5-e9c2c458ac75 | -11.38249 | -47.82079 | 2026-06-10 04:32:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c232b295-735d-3dce-8c81-0804baa18dba | -16.78744 | -49.30835 | 2026-06-10 04:32:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cdde59ea-c952-3dfe-97df-ffc1897d39e1 | -14.40009 | -45.55899 | 2026-06-10 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13c61fef-99bd-36f0-b32b-3c073185fc89 | -10.19089 | -49.59699 | 2026-06-10 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5eb4712e-ddfd-3515-8988-a4c31657e5ea | -11.65118 | -52.86637 | 2026-06-10 04:32:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 75b2aefc-22ac-357d-9f43-06c5917008a2 | -15.17779 | -43.85507 | 2026-06-10 04:32:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| acd4f684-7a5d-336d-b988-651a1a137982 | -11.1652 | -44.68763 | 2026-06-10 04:32:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84dd2c58-8e1f-331f-85a9-6af6cd3d1f49 | -14.36443 | -45.56129 | 2026-06-10 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7e761af-bd52-317e-95e9-0f885647310d | -12.30954 | -46.73795 | 2026-06-10 04:32:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b6eda039-e93d-3c53-8d16-b310b0262d62 | -17.79453 | -44.57288 | 2026-06-10 04:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d408abd-9d42-3580-a886-cc9022b32669 | -14.39926 | -45.55942 | 2026-06-10 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b94114f3-95c6-36e3-a44c-75171aa7a85c | -15.52176 | -42.62811 | 2026-06-10 04:32:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c468bff6-7981-300d-8cac-eb834ba850b3 | -14.4136 | -45.58371 | 2026-06-10 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33e71ce8-e4d6-3a54-8800-dc27b3b2f24d | -10.61829 | -52.2847 | 2026-06-10 04:32:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48559eed-564d-3a09-951a-61abb7b9935c | -12.85479 | -44.36901 | 2026-06-10 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 91eeab17-7440-3360-98d5-830fc61d2008 | -13.41908 | -43.73572 | 2026-06-10 04:32:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 27217157-799e-3336-a279-56a6dafaff78 | -14.64511 | -47.99611 | 2026-06-10 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 04020ded-be8c-3b05-b4cc-5a928970864a | -13.75376 | -47.11906 | 2026-06-10 04:32:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fff824c3-4588-3f71-93c0-d2714c67bd1b | -10.57992 | -49.64958 | 2026-06-10 04:32:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bee15542-a3e1-3ac9-98ec-82224d945a11 | -11.33807 | -51.39854 | 2026-06-10 04:32:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45bf4897-e8d2-3b03-9d2c-e51cdec235b2 | -12.77638 | -46.82579 | 2026-06-10 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54362c7d-bc6e-3e43-8678-a918e30da33d | -14.39954 | -45.56267 | 2026-06-10 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53ae1312-ebd6-3a04-bc49-a7fb89b4249b | -11.93387 | -43.39635 | 2026-06-10 04:32:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e924d6ae-f1f0-3cee-b6aa-9d7c01dd5e9c | -10.58925 | -46.74738 | 2026-06-10 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0adb47b3-d01e-3e16-bc98-18847c2cdea3 | -14.69743 | -48.31645 | 2026-06-10 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5381488-7e95-3ee8-ba76-7e2127198130 | -17.31792 | -44.91948 | 2026-06-10 04:32:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9614fe5e-7aff-3c97-ae57-de0be0670617 | -13.75319 | -47.12262 | 2026-06-10 04:32:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 28e0324e-ebca-3a26-ba28-b26f4da12dc6 | -17.44982 | -47.1877 | 2026-06-10 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06033a55-54a5-34f1-89df-69bd4ce8f8b7 | -12.85422 | -44.37284 | 2026-06-10 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 3a8fe6cf-8b98-3ec0-bfe8-920f36f8b8b7 | -14.3678 | -45.56183 | 2026-06-10 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 320d4ea7-43ca-39c4-a959-205554db8794 | -14.35488 | -45.53347 | 2026-06-10 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b3948444-ecf0-3a14-91fe-c86f7a6c0499 | -12.84947 | -44.36915 | 2026-06-10 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 357a6862-5369-37ae-adb4-2fe0688cb836 | -15.17841 | -43.85083 | 2026-06-10 04:32:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b8a3133e-c54d-3531-8dcd-26cc5d7f5ac0 | -10.51245 | -51.94042 | 2026-06-10 04:32:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5744ed99-0e41-3099-819a-c1b32c580fd9 | -16.48108 | -44.0172 | 2026-06-10 04:32:00 | NPP-375D | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0465bc7-e936-3e07-ba24-2e331598f056 | -14.63068 | -47.97847 | 2026-06-10 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b654e2f4-942b-3ff8-82d4-df02f80083e3 | -11.33872 | -51.39482 | 2026-06-10 04:32:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd069336-abda-33bb-8657-55250e4fce0d | -14.36106 | -45.53822 | 2026-06-10 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4c18420d-055a-3956-86b2-60877fbcc61b | -10.57694 | -49.64441 | 2026-06-10 04:32:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46bf8ff3-413d-39d1-81c6-cc5c8896dc1a | -12.05333 | -49.76624 | 2026-06-10 04:32:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69d6ff12-e3bc-3308-995c-c4a3e3c4c095 | -12.85134 | -44.36847 | 2026-06-10 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| f316a9fb-7e91-3a31-9e89-e6865f54a6e7 | -10.58068 | -49.64506 | 2026-06-10 04:32:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 881a4584-3a51-3012-9fc0-43e4470b95c6 | -14.63464 | -47.97535 | 2026-06-10 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0455d567-a2ef-3076-8302-57cbace89cc7 | -11.47675 | -52.91775 | 2026-06-10 04:32:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4bac697e-2999-3d24-80b1-9a15616ad502 | -11.3853 | -47.82509 | 2026-06-10 04:32:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2b11bb1-6ee8-3eda-816c-a311d3934a3d | -17.43362 | -43.81901 | 2026-06-10 04:32:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba4cdeb5-43ee-36be-8c26-5f10d4897715 | -10.51675 | -51.94127 | 2026-06-10 04:32:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f708c6c1-741e-3da4-9dc2-a4b21e382766 | -10.77467 | -44.84873 | 2026-06-10 04:32:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c707e265-b548-3ac7-a3d4-fcc511f570f0 | -14.62371 | -47.99997 | 2026-06-10 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59ac5182-2ce3-3cd3-9ff0-f202af1e3398 | -11.93447 | -43.39227 | 2026-06-10 04:32:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c03b434b-c1fe-34d4-b7a4-b03e431b1ac6 | -12.85767 | -44.37337 | 2026-06-10 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b489f040-4b48-3d3b-9d3a-90c9df77970d | -17.45258 | -47.1919 | 2026-06-10 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1cd23eea-8d30-3e8c-a8bb-4c7b1ff14fe7 | -14.365 | -45.5351 | 2026-06-10 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03179c18-6012-3627-a25b-a98cda044e76 | -13.51492 | -47.81699 | 2026-06-10 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 653875c0-310c-3527-9a5f-86c35c84e637 | -14.37117 | -45.56238 | 2026-06-10 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8dd6395f-ec09-3798-842f-1e23a91f5638 | -17.45095 | -47.18045 | 2026-06-10 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61d4acbb-50c9-3adf-813a-d30b8ab158d3 | -23.56396 | -47.50743 | 2026-06-10 04:34:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 738d87b9-2353-3e51-844e-0d3c875bf075 | -17.81624 | -50.64532 | 2026-06-10 04:34:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e33edf01-7a19-36d7-ab70-ad13fef3ee42 | -20.23242 | -41.89848 | 2026-06-10 04:34:00 | NPP-375D | REDUTO | MINAS GERAIS | Brasil | 3154150 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 18a133ce-245d-30a0-accf-594a41ff76f7 | -22.38119 | -49.79227 | 2026-06-10 04:34:00 | NPP-375D | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 14533f86-4028-37dc-945b-a73dd72a311c | -18.95839 | -52.46894 | 2026-06-10 04:34:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd198194-554e-34f2-b419-b115846af859 | -21.32008 | -48.54092 | 2026-06-10 04:34:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b08a4289-05a2-3779-b0dd-4e005e39c5b9 | -22.45047 | -47.15258 | 2026-06-10 04:34:00 | NPP-375D | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ce7f977c-a4f5-329b-a285-97999bb9214f | -20.66128 | -45.50249 | 2026-06-10 04:34:00 | NPP-375D | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d04a7577-1eaa-34f6-9f61-57a4559a710b | -18.9593 | -52.46393 | 2026-06-10 04:34:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc3fa450-7dc6-341a-bc95-e1621bfaeb72 | -19.26531 | -49.41825 | 2026-06-10 04:34:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| efb94c79-5121-39bb-a320-83f242a267b8 | -22.69943 | -43.36355 | 2026-06-10 04:34:00 | NPP-375D | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 836d4939-d0ed-3dd4-99df-e0e1063629b7 | -18.95452 | -52.46813 | 2026-06-10 04:34:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 40afead0-8fda-3a9a-9d20-96d82713f7ad | -21.21518 | -48.49982 | 2026-06-10 04:34:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 225ff161-3d4d-3bfd-ae1a-d82577c2c585 | -18.99651 | -49.77161 | 2026-06-10 04:34:00 | NPP-375D | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aa229272-8857-398e-8564-de78adebc88c | -19.92937 | -44.18389 | 2026-06-10 04:34:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7fe314d8-8f45-38d9-a831-8c2000900e6b | -17.81191 | -50.64884 | 2026-06-10 04:34:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4870339a-2d91-3c4e-8da9-296a425a09f6 | -23.56338 | -47.51137 | 2026-06-10 04:34:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5326051b-81f8-365e-acf6-f840367c3b7b | -21.47148 | -48.63663 | 2026-06-10 04:34:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 103e0bca-552c-3b64-b0f2-25abc17d6db8 | -19.47594 | -49.28807 | 2026-06-10 04:34:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 318f627a-fdae-3e1f-8fe3-d4f2cfe9ab61 | -17.81266 | -50.6446 | 2026-06-10 04:34:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5b9acfa-721e-3808-88ee-95e66eb8b223 | -21.31675 | -48.54031 | 2026-06-10 04:34:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2777f0ca-b29c-3ed4-b9fe-4bc9aea8850e | -22.74859 | -45.63344 | 2026-06-10 04:34:00 | NPP-375D | CAMPOS DO JORDÃO | SÃO PAULO | Brasil | 3509700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c2501407-27d6-3269-a23b-52117c371f36 | -9.3234 | -45.4787 | 2026-06-10 04:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 5844e36e-200b-34a6-b6d9-8866aed38056 | -9.3048 | -45.4581 | 2026-06-10 04:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 56.9 |
| ae204b98-f968-3cce-8c17-2fc463d93349 | -9.3045 | -45.4809 | 2026-06-10 04:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 4f7ddc36-da8e-39d4-bfb1-e273ceac8a1c | -0.08796 | -51.28024 | 2026-06-10 04:46:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 643096cc-f0ef-3acb-9c06-9f1183e99a1b | -5.41609 | -43.90186 | 2026-06-10 04:49:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 99e99415-d72c-367a-b5c4-2d0a1c905dfc | -5.93426 | -43.48732 | 2026-06-10 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d7a84073-d32a-3d65-9088-27244267a135 | -7.10439 | -46.51759 | 2026-06-10 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1ce85b7-62ab-3652-bf5c-75a83b17223d | -6.44098 | -44.58052 | 2026-06-10 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c33f7e52-372a-325e-a267-a59be003a707 | -6.00867 | -47.07756 | 2026-06-10 04:49:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c370da75-e085-3d1d-bc57-8cc1d15c5b2f | -3.49825 | -48.03755 | 2026-06-10 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38f68188-6492-3d3f-bc50-3c698f5015b6 | -4.57452 | -48.02493 | 2026-06-10 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fbda1be7-e619-3258-ab55-3a1f58fb2a52 | -5.61431 | -37.52755 | 2026-06-10 04:49:00 | NOAA-20 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 141e2417-3098-37a9-a026-5ea814caa0af | -5.7643 | -46.04578 | 2026-06-10 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0e68828-8fe2-33ad-93c6-dc1143b4668c | -5.04311 | -43.26108 | 2026-06-10 04:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b19f8ce3-2348-3ed0-8cdf-014612c3eb1d | -6.56885 | -47.91133 | 2026-06-10 04:49:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a8d37482-f87f-3a01-8a2f-4e47d22ec758 | -6.11906 | -53.08252 | 2026-06-10 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 41e22c5e-b4f6-3920-aebc-cbb1eadf3d07 | -5.41574 | -43.90278 | 2026-06-10 04:49:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b04f1541-9963-399c-93ff-46c9f081bad9 | -3.50173 | -48.03811 | 2026-06-10 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README9.md)
