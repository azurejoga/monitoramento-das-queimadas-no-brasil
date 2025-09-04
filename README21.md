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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ece71f9a-226b-3fdc-ae2c-4b87fbdc9d9f | -15.54818 | -48.38899 | 2025-09-04 03:38:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86a1d9fc-3de9-3cc0-8d2d-712f07baee8a | -13.70413 | -46.87846 | 2025-09-04 03:38:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af852d6f-7afb-3980-ae1f-f5a7ea63a859 | -13.86252 | -47.97968 | 2025-09-04 03:38:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 894a782c-ccaf-38d8-b931-c81c64891432 | -16.3002 | -45.69278 | 2025-09-04 03:38:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7fc8e3e4-5daa-3c09-8b5c-1c9623b4240b | -12.90278 | -48.05593 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 34fae389-5ad1-3690-b586-b1197cdeead7 | -14.80707 | -48.22697 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc26d106-01c1-3713-8444-cfab18984b50 | -15.53094 | -48.34547 | 2025-09-04 03:38:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8bf46566-9b31-3ad2-9d4f-c80e6087c650 | -13.57469 | -48.12887 | 2025-09-04 03:38:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| deb26476-cbb6-3534-8374-b6be64e7c1ce | -13.85599 | -47.97866 | 2025-09-04 03:38:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f3cbdf8e-0762-33f0-ac12-a3fd0196a00a | -12.48459 | -48.0792 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ed017cf-49c2-32a2-b907-caff206d79f6 | -17.18313 | -46.2617 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 16.9 |
| ca47ae93-5129-3f08-9940-65c79a9458c6 | -17.17635 | -46.26779 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 34487be9-6ce3-3ca8-aa60-777f6e312304 | -14.81322 | -48.22973 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d46059a2-efa1-3298-9191-7cf6c4df25ad | -17.17232 | -46.23173 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6934abcb-7886-321d-ac87-7c4f7100c766 | -17.04255 | -46.49295 | 2025-09-04 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4423ef0a-c88f-315f-8331-e430f3a9f8a8 | -15.02705 | -48.11244 | 2025-09-04 03:38:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b802047a-0a3d-3a5e-b072-ee6cf1f7e4f9 | -19.23244 | -48.68097 | 2025-09-04 03:38:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d736fb8a-0dbb-3d43-9ce5-3c58739d05e5 | -12.47682 | -48.08325 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc9fa306-b5ac-3257-961e-04e7974c0f24 | -17.61225 | -43.76348 | 2025-09-04 03:38:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7753f902-4f10-3ce2-995c-be10d97433eb | -14.56852 | -48.05068 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a033369-7b55-330d-ad0c-23708bece14e | -14.53581 | -48.0781 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f4aea7cb-6b69-3481-ab1d-1dfefeb77427 | -20.4663 | -42.45516 | 2025-09-04 03:38:00 | NOAA-20 | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 4ac4c16e-79c4-306a-961a-6f59b2baf242 | -17.17399 | -46.25136 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3b2ef113-837f-364e-85b8-cfda8239d38c | -17.04337 | -46.48906 | 2025-09-04 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cc7364e8-326e-3faf-9dbd-e9a185cc2684 | -14.81004 | -48.21301 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b24d2735-0c37-3c4a-90f2-e09a1c5078bb | -12.48332 | -48.08542 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af767f8c-7f92-3aa8-b0c3-449e866ced71 | -16.29483 | -45.69159 | 2025-09-04 03:38:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06667d46-ea71-31b3-82fb-487f8f722be7 | -12.47305 | -48.08468 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd55fd15-0da1-3f37-8df0-57d82fc13a89 | -17.1662 | -46.26137 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86fb4fcf-2813-3b6b-8e80-79b26ad0df1d | -19.75183 | -44.11071 | 2025-09-04 03:38:00 | NOAA-20 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b323f17f-f9dc-3cce-9cfb-0b7c5f54c4a2 | -18.0668 | -45.97308 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc45ab78-f3e1-3a44-8b40-912536ac9df3 | -18.0571 | -45.99312 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e36cf2e7-8dc5-3717-b66a-0134f2470edf | -17.03613 | -47.14359 | 2025-09-04 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 66871316-69fc-38e1-ac0a-b8d46ecb1845 | -17.16287 | -46.24911 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db4ad8cf-3d55-3e19-86f5-1a810e9532ab | -14.56311 | -48.04472 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98294392-07e9-32f9-b5f7-eedca5fdd05c | -14.75499 | -48.09403 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b4d5ec5-16fd-3313-a90f-03027e13bcab | -17.18151 | -46.2693 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| d290bc81-d703-34f8-96d2-61750e8fa556 | -15.02722 | -50.08385 | 2025-09-04 03:38:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc1c07c6-21bc-3083-bbf7-bd44101b4227 | -14.90527 | -49.62518 | 2025-09-04 03:38:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89fd3d0a-a91f-3bb5-adb1-0d4e50035622 | -14.54843 | -48.05072 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f85cbfad-97d0-3b27-8802-ddedbc459593 | -13.30905 | -46.82237 | 2025-09-04 03:38:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32a64c0d-0e3e-36f4-a3a2-e4599ec2d2d0 | -13.44358 | -46.93847 | 2025-09-04 03:38:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f6c00fd6-9262-369a-920e-957cd62afc41 | -17.04196 | -47.14471 | 2025-09-04 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 412ef95f-d328-3d5e-b238-906431db1eb0 | -13.56662 | -48.13467 | 2025-09-04 03:38:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8201e784-5d0c-37f8-93ea-8621b5e4c923 | -15.02771 | -48.11581 | 2025-09-04 03:38:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7fbe009d-56b5-369a-b0c6-93b7f0062da4 | -15.01649 | -50.03199 | 2025-09-04 03:38:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8ff87686-7581-30a4-b80d-9be1d12639c3 | -17.17322 | -46.25512 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0fd390e1-9bf1-3fbb-8d5a-c1959318acb1 | -14.19907 | -48.07612 | 2025-09-04 03:38:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 502f39e5-c7d2-3157-9518-230b60cbb683 | -12.9931 | -48.07226 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eff4b551-8c34-395e-8091-fd2246fb61fd | -14.56957 | -48.07708 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 345c0012-794d-3705-a89d-7ef5266aa549 | -15.03453 | -48.10865 | 2025-09-04 03:38:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4126c45f-194b-36c3-92c3-122e57403ca7 | -12.99828 | -48.0802 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 796b037f-7eba-3bd5-9bd5-86f66cd5193f | -16.30659 | -45.69753 | 2025-09-04 03:38:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5263a51c-5c80-3beb-a1d7-8bb16d274bb6 | -16.30412 | -45.70118 | 2025-09-04 03:38:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 67e9842f-25a6-3c8c-bcd8-fb04fb9314a5 | -19.25288 | -46.54125 | 2025-09-04 03:38:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f0bec6e-ea7a-3043-9d1a-e79325c7f2f8 | -17.15679 | -46.22379 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| efc9ffff-5924-31db-81fb-3644536e0cd1 | -12.98659 | -48.0705 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f34cced-d0f4-354c-83b1-dfc930ade781 | -14.2127 | -48.07544 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3b1e0b8-e2f4-3acc-8a2a-dce092d068b5 | -14.59655 | -48.01336 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3f1d7d8c-8cd5-327d-bc4c-9749b87102f2 | -12.90076 | -48.04414 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b1f3afb-2f66-3530-b6bd-ee9088308b70 | -12.4547 | -48.08952 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8768abd2-d9cd-3a0d-b19f-04434efe86e3 | -15.04818 | -50.07162 | 2025-09-04 03:38:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44f49e3a-2f94-3ac7-9742-ab6528b53248 | -15.02263 | -48.10857 | 2025-09-04 03:38:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c7e5c47-7b08-3932-8f9d-d8939a6ef452 | -16.07607 | -43.62266 | 2025-09-04 03:38:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f590e8cb-62bb-37a2-8aca-6bd8c255a843 | -17.17713 | -46.26396 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 6ecfad23-dceb-3459-ac75-a1a70fe0c354 | -12.49655 | -48.07204 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b50f8f72-b5da-3b07-8a4f-273d7ea6dd3c | -12.00363 | -46.75013 | 2025-09-04 03:38:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8d6de97-da80-3c22-9d75-80881fa494b7 | -13.29647 | -46.82175 | 2025-09-04 03:38:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a15da7ed-bc07-3a13-aa6e-892a81ff78a8 | -14.8183 | -48.2376 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64133945-b072-353f-ad47-fc6627f2a647 | -12.48092 | -48.08034 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8c361b97-ba6b-3260-a4b0-e18aee13667c | -18.68653 | -48.1874 | 2025-09-04 03:38:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f584b988-2f64-303e-8b25-f4d24e2ba556 | -18.06313 | -45.99078 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea07b519-79cb-3bf7-b9cb-a5920ae152c0 | -19.23144 | -48.68439 | 2025-09-04 03:38:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65a0d456-1f73-3dc1-9ff5-5c77ec1f9ef1 | -14.28725 | -45.2327 | 2025-09-04 03:38:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 395d01e0-7a61-3579-9403-b415fee98f73 | -14.8224 | -48.21949 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e2f415ef-ebcf-3598-968a-ce5f6960ba57 | -12.45596 | -48.08342 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 76e679c1-1cca-3d9a-81f0-e95237d0fd9d | -15.04121 | -50.08804 | 2025-09-04 03:38:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0bb6bc5c-b539-344a-850c-8aee31f33eb4 | -17.17604 | -46.26802 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 7b1c8054-b84a-3dbf-95c5-4194e8d9d8e3 | -17.16766 | -46.22674 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2b807a4-fb4e-3c42-bb05-9b3f3196e6a5 | -19.23753 | -48.68581 | 2025-09-04 03:38:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 246fa88d-9f9e-38eb-b35a-8e60b7619c7c | -15.0186 | -50.03812 | 2025-09-04 03:38:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 051fe6d3-5571-33a9-90f9-730aef8eaa1b | -13.73309 | -46.92213 | 2025-09-04 03:38:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ea452eee-a547-380e-8bec-cc9b51eff481 | -14.75621 | -48.08841 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57a3c59c-4134-35f5-8ddc-f3a6137b5e95 | -14.8098 | -48.21546 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83218403-6602-3ff3-9827-bc32f4b4cf59 | -14.32554 | -42.95827 | 2025-09-04 03:38:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 4a4f4b6e-40d9-3c91-97aa-453390e4a928 | -14.81109 | -48.20805 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2bf307c4-9619-3d81-aac8-59e4514d04af | -14.56423 | -48.03953 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd455ef4-4e46-3581-9162-6635554e7d14 | -12.94217 | -48.065 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf0426d9-a49a-3e50-84aa-81efe7df09f9 | -17.97057 | -47.12028 | 2025-09-04 03:38:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 997b8179-6dd7-38b7-9189-3774fb958e70 | -20.09772 | -44.13585 | 2025-09-04 03:38:00 | NOAA-20 | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4e465b83-568f-30ea-a5b9-19278bc1760d | -15.5496 | -48.41312 | 2025-09-04 03:38:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5888420-f949-3904-87be-5e3569f46b1f | -17.04811 | -46.49419 | 2025-09-04 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4a43a32-196a-31ba-a19d-bb8015e0bf1b | -17.18232 | -46.26548 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 0ab05f38-9de5-39df-87d7-ab4881cbcdbc | -16.30484 | -45.69761 | 2025-09-04 03:38:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f4bacdb7-7b80-3d76-afd1-33dcb941f8ac | -17.17708 | -46.23638 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b3308774-ef59-3022-a84f-68195194fe68 | -16.0606 | -41.83647 | 2025-09-04 03:38:00 | NOAA-20 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6f00d21e-a08f-3e90-af27-d95c3c86b02e | -14.78003 | -48.13328 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bc64623-19cd-3122-a0af-8c6669ea819a | -14.81641 | -48.21472 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 148e5ff5-449c-3e37-ab16-2c85caa3ae7b | -15.03078 | -50.08238 | 2025-09-04 03:38:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 458761e0-5b79-3dde-8545-f81633964e81 | -12.8889 | -48.035 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README22.md)
