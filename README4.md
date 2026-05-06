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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8e047b1-28bc-3d99-aeb0-cc5cfa9dae7e | -12.33359 | -44.59433 | 2026-05-06 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d85c4f7f-56b4-3a82-80a6-6d597249bdfb | -20.20814 | -50.65233 | 2026-05-06 03:47:00 | NPP-375D | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| c37dd874-49bb-3619-ad50-641ed8089254 | -11.99571 | -47.78018 | 2026-05-06 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32e925a1-3e07-322c-bcd3-89f808e67f85 | -13.65135 | -45.56069 | 2026-05-06 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e17eb7cc-82be-31ff-8768-c712c0e1b450 | -18.07624 | -46.36813 | 2026-05-06 03:47:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dad3ecd1-8096-3414-9177-85f8f1586be9 | -11.12534 | -45.11446 | 2026-05-06 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c21c702-47c2-36c8-beec-d825fb12dcaf | -13.22744 | -40.13116 | 2026-05-06 03:47:00 | NPP-375D | IRAJUBA | BAHIA | Brasil | 2914208 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5646846a-b097-342a-b4c4-ee92e6405cec | -12.27437 | -43.51262 | 2026-05-06 03:47:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3dd654e7-0f98-34ac-95e9-163b496a7223 | -19.72772 | -40.30445 | 2026-05-06 03:47:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f8c9d0e3-08b9-30a3-82b9-452caa99578b | -11.62002 | -48.06093 | 2026-05-06 03:47:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0329c9d-674f-3228-ba25-da16503dd8c3 | -13.99804 | -47.59702 | 2026-05-06 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ddda7cc0-5ec6-3307-9871-bb34abe31780 | -18.0763 | -46.37316 | 2026-05-06 03:47:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb613976-9e9d-3c4f-b29b-d943f39d0874 | -13.22352 | -40.13018 | 2026-05-06 03:47:00 | NPP-375D | IRAJUBA | BAHIA | Brasil | 2914208 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0ad1bb03-d636-3d61-8289-7b4419afeae8 | -13.79895 | -43.34782 | 2026-05-06 03:47:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 51ce2101-6d10-3364-bb4e-77bcd3b961a5 | -9.4711 | -47.80818 | 2026-05-06 03:47:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f128e57-8dc2-337d-a0d0-9fd216b73192 | -11.13715 | -45.14444 | 2026-05-06 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d746c195-fb4a-34f1-ae0a-20f2eeced55f | -13.22547 | -40.13262 | 2026-05-06 03:47:00 | NPP-375D | IRAJUBA | BAHIA | Brasil | 2914208 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1d2078c5-1795-3074-803c-55cd57d78263 | -11.13027 | -45.11935 | 2026-05-06 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 455b1901-d187-3449-8b52-deafa355b906 | -11.79838 | -43.61859 | 2026-05-06 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 51ac93bf-c711-30da-93a5-4be659c676ed | -18.23693 | -45.67038 | 2026-05-06 03:47:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71efe5e7-71a7-3789-ac1f-d8f4162d7e9a | -11.13219 | -45.13961 | 2026-05-06 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 05c0737c-b93b-310b-97aa-f11aa43f8fff | -11.80347 | -43.61959 | 2026-05-06 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 220a7a42-a594-3e81-85a0-53b443241322 | -9.46424 | -47.8068 | 2026-05-06 03:47:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 595f7e4b-dffc-3a01-95c4-ae97bfb2fc61 | -13.99676 | -47.60305 | 2026-05-06 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc0c5d43-8787-39b6-812d-06e1fbc673f0 | -12.27051 | -43.50575 | 2026-05-06 03:47:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 39ee5acf-b0c6-3a6b-92f2-f1d17bec5ec9 | -11.1379 | -45.14062 | 2026-05-06 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5398678c-43e6-323c-bc61-2600270dc433 | -11.79894 | -43.61559 | 2026-05-06 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e458bbdf-4825-3a1f-b84f-9088486e4b7f | -11.5542 | -48.27329 | 2026-05-06 03:47:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e186c71-cb8a-3811-a823-899304879aa4 | -12.27198 | -43.50542 | 2026-05-06 03:47:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 94fc62af-b5f5-35a0-9e25-ae092156df80 | -18.23739 | -45.67217 | 2026-05-06 03:47:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca85dadb-51fd-3678-ac2f-1920377e4090 | -11.44003 | -40.77427 | 2026-05-06 03:47:00 | NPP-375D | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dfb75d65-3479-3a0e-923e-f178528b2ef4 | -11.61087 | -48.06333 | 2026-05-06 03:47:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc7e8826-f433-3831-8eb9-4fd3befd0286 | -13.44177 | -43.84614 | 2026-05-06 03:47:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 9bd79ac0-cd39-32b7-a8bf-d9e9b03c40fd | -11.61328 | -48.0596 | 2026-05-06 03:47:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3f06fc91-8c47-3f20-be8c-2e4818d0a079 | -12.27589 | -43.51232 | 2026-05-06 03:47:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 66e9a437-8f56-3c58-bff8-8c9121e703ea | -14.07986 | -47.62397 | 2026-05-06 03:47:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9690cea9-27fc-34a8-9ef7-6b2f32233fa9 | -11.99687 | -47.77446 | 2026-05-06 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5b704898-03b7-375b-b0d9-366b1de97cca | -14.14162 | -45.35684 | 2026-05-06 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 809e5376-4e80-3832-9f35-a15d2060d2e9 | -14.13542 | -45.35939 | 2026-05-06 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24212283-312f-38a9-9752-326bab81a9b8 | -22.17022 | -42.8785 | 2026-05-06 03:47:00 | NPP-375D | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 68760e2a-937b-3a34-a3f2-672eecdda19c | -18.2363 | -45.6735 | 2026-05-06 03:47:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0df4b556-fb5d-3b08-8bbd-b88d27e42c4f | -11.13144 | -45.14342 | 2026-05-06 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 15ec145c-0c2a-3ba6-b786-c1c5dc2ab82c | -11.6121 | -48.05724 | 2026-05-06 03:47:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2841e6c9-55a8-3833-bdb9-85b293d66cdd | -12.27088 | -43.51129 | 2026-05-06 03:47:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cc5e470f-f260-3e6c-a4f6-4b793dce403d | -18.07709 | -46.36951 | 2026-05-06 03:47:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dcca1d0a-4189-3a37-982d-7330e31229a9 | -14.14088 | -45.3605 | 2026-05-06 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f59f8317-ec66-30af-88b4-f2a21b424f63 | -12.27552 | -43.50676 | 2026-05-06 03:47:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 13fc51e8-4fa4-37b7-9704-fd05803d20c5 | -18.07548 | -46.37177 | 2026-05-06 03:47:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a3909bf8-805e-3ceb-b013-4f1fb11afe1f | -12.32818 | -44.59344 | 2026-05-06 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da86a2bf-db0a-3f7d-8f87-17c836de085a | -10.58649 | -44.33248 | 2026-05-06 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e481dd6f-8ec1-3e2e-b002-d714db668958 | -13.43673 | -43.84528 | 2026-05-06 03:47:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 04d309ad-4ea1-3418-b302-9a5dba2c32e2 | -14.08497 | -47.63079 | 2026-05-06 03:47:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d066b28a-151e-32d5-aeb3-f5810ff4b531 | -21.7025 | -48.42244 | 2026-05-06 03:49:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f7cb3c4-5b6e-30bb-9f2c-9c07141c35f2 | -21.70903 | -48.42016 | 2026-05-06 03:49:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 0300bbef-8e20-3c9c-b1a3-8833b24a193f | -17.8629 | -42.57602 | 2026-05-06 03:49:00 | NPP-375D | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 77033fb1-0aca-3146-99a6-39a39f1a6532 | -17.80465 | -46.71698 | 2026-05-06 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a4f44bbe-8139-34e2-b7aa-a6d02e092c07 | -17.80294 | -46.71616 | 2026-05-06 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| baca6186-988e-3452-a0b3-66c0177b7e14 | -22.50699 | -47.31724 | 2026-05-06 03:49:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 10.0 |
| eaa0e49a-8fac-37e4-8932-601117ebf4dc | -23.55956 | -48.57283 | 2026-05-06 03:49:00 | NPP-375D | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76d74413-db61-36c6-8208-e9412bb067b8 | -22.50775 | -47.3138 | 2026-05-06 03:49:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 76ee117f-4c74-3a92-9973-3ed288c6da90 | -20.79001 | -51.66575 | 2026-05-06 03:49:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| e4f43137-7dd5-30fb-bd7e-905aad225de9 | -21.70719 | -48.42822 | 2026-05-06 03:49:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 43141835-b230-3717-9f06-d7421156ac76 | -17.80926 | -46.71384 | 2026-05-06 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| deabaeec-8abd-3089-bd9c-8e568826412b | -20.79576 | -51.66378 | 2026-05-06 03:49:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 19.4 |
| 3f9e70ff-f40a-3f1c-ab22-32e69a9771a5 | -20.79851 | -51.66107 | 2026-05-06 03:49:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 465d4d13-0fe6-3598-b42f-cecf0b3cbc0f | -22.70074 | -43.36356 | 2026-05-06 03:49:00 | NPP-375D | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a34d2e2d-bacb-3bca-ab5b-d17685f225d4 | -22.80505 | -49.34745 | 2026-05-06 03:49:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 867f4566-9d95-39c8-b628-6db1c8682dab | -20.79165 | -51.65906 | 2026-05-06 03:49:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| ca19f825-901a-313f-b9ae-e0ff0cccf2ad | -21.70811 | -48.42419 | 2026-05-06 03:49:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 72f53e31-1878-340f-9f33-63a3a261b0c5 | -20.78888 | -51.66186 | 2026-05-06 03:49:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 157bdcae-6dd6-3b8a-80cd-431cd439fdd8 | -20.79687 | -51.66776 | 2026-05-06 03:49:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 2ee9551d-92d2-3bc4-bdfd-eff6122c409b | -17.80847 | -46.71749 | 2026-05-06 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2015c75-fdde-3317-89ad-f452f7dd263f | -17.80541 | -46.71333 | 2026-05-06 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f9a5ba71-c22c-3014-b958-ba234df67581 | -17.80373 | -46.71252 | 2026-05-06 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad6dd098-65dc-3f7c-8746-9d24a8e9863d | -22.79928 | -49.34554 | 2026-05-06 03:49:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 959f1ade-1dce-38da-b2c5-9a6276d013bd | -17.79911 | -46.71568 | 2026-05-06 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 267bffbc-89c9-3514-9a4d-ba1cb188217b | -12.5033 | -58.4781 | 2026-05-06 03:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 6537718d-05bb-319c-a719-63dfc1f11028 | -12.5033 | -58.4781 | 2026-05-06 04:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 0d7ec9f6-38b8-3092-bcc6-87dbf110d7c7 | -5.51901 | -37.62062 | 2026-05-06 04:02:00 | NOAA-20 | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| da2ad89e-3805-35b6-a367-63b07b3a2783 | -11.60542 | -48.05844 | 2026-05-06 04:04:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de4d3942-6c99-3201-ab6f-a225583d8b23 | -12.15629 | -46.66241 | 2026-05-06 04:04:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96e6f668-01f3-346e-a93d-2e461951a340 | -12.15373 | -46.66209 | 2026-05-06 04:04:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef05a555-d6b0-3d7b-acfb-34d56a776e77 | -5.75504 | -43.18476 | 2026-05-06 04:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 849a2f07-99df-3ec6-903e-3c19ae484500 | -10.58781 | -44.32765 | 2026-05-06 04:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3a9bd1b-0396-3f8c-be2f-f05b80d85b0e | -11.55155 | -48.272 | 2026-05-06 04:04:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 76e724a1-9ea1-36b1-b826-31f3849d7f9f | -8.6143 | -49.52265 | 2026-05-06 04:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2490f3a-27c3-3711-8728-e3c02574b8c5 | -12.43941 | -44.62258 | 2026-05-06 04:04:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65e42af9-0deb-3919-a2dd-f0e30b9730ae | -12.38827 | -46.32511 | 2026-05-06 04:04:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e78fc3f1-16d9-37f6-a7f7-2fd18e0f685c | -11.79838 | -42.06395 | 2026-05-06 04:04:00 | NOAA-20 | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7df5587e-8525-3075-9cdf-5203267f4685 | -12.32842 | -44.59196 | 2026-05-06 04:04:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 269af0f9-d934-3351-b13e-3661b1c6cd5e | -13.22369 | -40.13214 | 2026-05-06 04:04:00 | NOAA-20 | IRAJUBA | BAHIA | Brasil | 2914208 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b922faa4-f2d4-3400-bc38-8005e2f570c5 | -11.12641 | -45.11446 | 2026-05-06 04:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 285869d9-b0c4-37c5-aafa-d540d5d4974e | -11.79684 | -43.61755 | 2026-05-06 04:04:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5327d39e-83bf-37d4-8840-846fcb3b5d17 | -12.13805 | -40.89257 | 2026-05-06 04:04:00 | NOAA-20 | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bff6df2d-f392-36a3-a4dd-70e485e91247 | -5.78727 | -45.12157 | 2026-05-06 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f832005-69b6-3689-a6e7-042492c42cb3 | -11.12684 | -45.11668 | 2026-05-06 04:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57a4656b-0ba1-3fd1-92bc-239f339757c3 | -5.78789 | -45.11782 | 2026-05-06 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 943ce561-1855-3442-8eda-2110e9a3b8dc | -9.25221 | -40.24212 | 2026-05-06 04:04:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 42f3851a-7603-3668-ae89-c8f6fd019502 | -8.22225 | -43.87727 | 2026-05-06 04:04:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a07b4698-9feb-32ec-bc4d-7f4bfa824ee7 | -11.60998 | -48.05924 | 2026-05-06 04:04:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README5.md)
