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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cefb33ed-4fc0-371b-9c05-abef3d426b3d | -13.44643 | -47.0307 | 2025-08-23 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 153cd28c-7727-3879-81cd-20ff6e1adc41 | -12.70145 | -48.10693 | 2025-08-23 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f8138129-9354-39b7-94f2-85cc6ccb84e3 | -14.91739 | -47.32252 | 2025-08-23 04:02:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 71010f27-4c6a-3586-b8b1-a14d68855b14 | -12.30044 | -49.99379 | 2025-08-23 04:02:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fdbf88e-fd2d-3235-a3a8-97b26fc2aa3f | -15.19149 | -48.24475 | 2025-08-23 04:02:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 41ee9277-67a7-345a-a613-46afcdc48b4b | -13.3892 | -47.51417 | 2025-08-23 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a0c3315-e9a3-315c-bf55-8d32d4cfaea3 | -11.18714 | -55.02234 | 2025-08-23 04:02:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 25238f7f-dbaf-3f71-b041-60fe54d1ce8b | -13.32862 | -40.34144 | 2025-08-23 04:02:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| bc4928e2-97c3-3434-b0c3-f7a9debf9bde | -12.77815 | -48.70869 | 2025-08-23 04:02:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 7824ac8b-fe02-3ee7-946a-9e276c049d8f | -14.82215 | -47.95953 | 2025-08-23 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7443102a-f72a-3743-b1b3-ec9477044ba5 | -13.46276 | -47.03379 | 2025-08-23 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 732871e5-d1b1-3f41-96f6-ed2d021ae7f4 | -14.78631 | -45.48663 | 2025-08-23 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f4d2db1-fc75-3b67-8844-ca96efc65e8d | -13.41776 | -46.2667 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 9f148f51-0dd7-3824-82fd-bb2fc7194d15 | -11.44341 | -47.33235 | 2025-08-23 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f21fb157-9831-3a68-bf03-588513b07ea6 | -10.74431 | -48.24823 | 2025-08-23 04:02:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f985020d-ff59-33fc-b5c0-ab9e46466d3e | -13.49585 | -47.03767 | 2025-08-23 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f70ef8f4-b7f8-348d-9191-41c235a9586a | -10.64552 | -50.13357 | 2025-08-23 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3937097f-6bdf-3281-b165-bc650047b89e | -11.1208 | -44.75994 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 549d7d03-98fe-3a17-ac76-70a0cbce2818 | -14.77999 | -45.45813 | 2025-08-23 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da54bf6d-d758-32b1-a43f-57099203eb0b | -8.15832 | -47.31168 | 2025-08-23 04:02:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 08b0aefc-ba55-34ba-835a-336aae755915 | -13.37615 | -47.51401 | 2025-08-23 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dfe58237-b5a9-3ada-8666-ef4bfe5b2014 | -13.41953 | -46.25652 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4086cd3f-37ff-301d-8343-5e426f291112 | -12.78265 | -48.71774 | 2025-08-23 04:02:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e1fbb9b5-c1b8-30bd-9a03-d7717a8600b5 | -8.29802 | -47.26682 | 2025-08-23 04:02:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b1741cb5-24fa-34b6-9e4a-f1e4904f9a90 | -15.70701 | -41.92772 | 2025-08-23 04:02:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| d3df4118-31c4-3247-99ca-a27b0940bd31 | -13.04223 | -46.31617 | 2025-08-23 04:02:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ea913bca-a46b-316d-892e-5743d4d69718 | -8.78339 | -46.73939 | 2025-08-23 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a67711fb-3b75-3046-bf65-243590eb8719 | -13.12681 | -46.89882 | 2025-08-23 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77d2487b-976b-3bb2-96eb-2642150cd6a0 | -13.05119 | -44.06946 | 2025-08-23 04:02:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8aad01df-85d2-3d06-b4b6-a5b81fd12de0 | -14.37513 | -52.05233 | 2025-08-23 04:02:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4cdcc4ec-3fcd-3d9b-9eb7-7e507fea6545 | -8.79247 | -47.31815 | 2025-08-23 04:02:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc651d9d-703e-372c-9a8b-99a7e93667cd | -12.9384 | -46.31151 | 2025-08-23 04:02:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5eafad16-b5ff-3e87-8f26-773b3bd9d57d | -11.13777 | -44.77207 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 62a70629-2a98-35de-a816-7934e78aa032 | -8.52389 | -48.83289 | 2025-08-23 04:02:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 226f6fd4-e68e-3819-bacc-9ec541456b28 | -10.74156 | -48.26339 | 2025-08-23 04:02:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5d89a320-8777-3e77-9828-bfb67059b375 | -8.52867 | -48.83253 | 2025-08-23 04:02:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 214340c1-3d9c-38c9-b522-e331fc7e4d9d | -9.55472 | -47.93795 | 2025-08-23 04:02:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 35917f7d-f0f5-343b-bbbf-871aaca07c77 | -14.37836 | -52.06513 | 2025-08-23 04:02:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c37091c8-0200-34f6-8fca-701639521a46 | -10.20988 | -47.57488 | 2025-08-23 04:02:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec9b5234-89b8-3bed-9e33-ea6b2b71c472 | -14.94262 | -48.01504 | 2025-08-23 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1f0d887b-7cfa-3b89-beca-45c7d60fb347 | -13.37268 | -54.39994 | 2025-08-23 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db63641f-aba6-305c-926c-708f2bbe369b | -13.36993 | -54.40591 | 2025-08-23 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 87690f6b-9c3a-3627-80c3-1b73953d68f3 | -13.57959 | -43.35129 | 2025-08-23 04:02:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 4a2b33cc-7c70-3b59-aa39-f7315617ed74 | -14.47291 | -48.35291 | 2025-08-23 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 84da8477-884d-3647-aa1d-db54bcd6742f | -8.28976 | -47.26077 | 2025-08-23 04:02:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ce1d8ca-f411-3ab2-b2b2-644971d600ce | -14.4725 | -48.35594 | 2025-08-23 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e2d7b354-3747-3e81-9007-665b5f4aac26 | -15.55688 | -42.68407 | 2025-08-23 04:02:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0f016d13-d88c-36ea-9f1f-b2eb444cbfbb | -13.379 | -46.21271 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 93766565-0667-31d9-9f60-9cdab8bca30f | -11.12514 | -44.77916 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1e788c00-1254-341e-a74c-a2117e734d1b | -13.72525 | -44.40003 | 2025-08-23 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4e3c0b83-6ff9-3fd9-8217-238600c4d6a2 | -14.37591 | -52.04849 | 2025-08-23 04:02:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ecfcfb28-4a3c-3719-b143-d8a93e504570 | -13.04429 | -46.32752 | 2025-08-23 04:02:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 135a9704-b64a-3649-9391-85f0429f6743 | -14.80259 | -47.94673 | 2025-08-23 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| aa8642eb-fd96-3814-8c97-8886a0fd74c7 | -10.74988 | -48.24393 | 2025-08-23 04:02:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a68f5dca-646b-351c-9ee0-588e69e48102 | -13.47081 | -47.03604 | 2025-08-23 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aafb7b72-e19a-337c-be02-97f6acfbe915 | -11.29941 | -44.92049 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 642b482f-40a0-3b71-8a74-46ebcfc40f1a | -11.18015 | -55.02082 | 2025-08-23 04:02:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ef580967-96b3-3e07-aeac-139d59e93d25 | -9.79279 | -41.78191 | 2025-08-23 04:02:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 55264744-039e-3fbf-8935-54c4ea60415f | -9.87495 | -47.81291 | 2025-08-23 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1491189f-aa50-33dc-85f9-b071c9a268b4 | -11.13265 | -44.75742 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 706dd038-9c98-32b6-981a-d397a18ee5ba | -11.32516 | -55.22336 | 2025-08-23 04:02:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4143d3d8-fbfe-3fbf-9636-3c3348bd606e | -11.13189 | -44.76186 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2196f45a-65ae-3d04-b9a6-7ad23622b4de | -11.05808 | -44.60115 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae302860-e77c-3a78-8ccd-6ce71a266013 | -11.14353 | -46.05008 | 2025-08-23 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d1a76c33-fd1c-3f10-a0d5-75331e5c264c | -11.31662 | -55.22887 | 2025-08-23 04:02:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4410e34b-1825-3f4c-9350-1f0ff1080078 | -11.50121 | -50.46892 | 2025-08-23 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5daec537-d956-36b0-923a-84ebfddae6ce | -11.54303 | -44.83582 | 2025-08-23 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 015295f1-a998-3875-b0b0-a5ab4609ed03 | -12.78185 | -48.71441 | 2025-08-23 04:02:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 09be5954-3f1b-34f6-8d2b-d3ea39df67c2 | -13.40661 | -46.23839 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f94a2407-7140-3ccf-802c-621da0101b75 | -14.37436 | -52.05619 | 2025-08-23 04:02:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 45649b73-b6cf-3427-bd5f-40581b314592 | -13.38045 | -47.51438 | 2025-08-23 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 614efbd1-e201-3518-aa36-f289fcb9c97e | -11.11711 | -44.7593 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c927a4f8-4b56-3368-a2be-71d603c72a45 | -14.91004 | -48.00125 | 2025-08-23 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f9665ef-9f4c-3d75-bbb0-157c8ade722d | -14.90244 | -47.99482 | 2025-08-23 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c460a54a-981f-3571-8166-9c80a0355ecb | -9.95522 | -46.41333 | 2025-08-23 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1acfee49-6f67-394f-8498-ef3eac23184f | -13.72172 | -44.39941 | 2025-08-23 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| db944f38-2dbb-382b-9d91-d152033bbb03 | -15.05402 | -48.47007 | 2025-08-23 04:02:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b72caed9-6d6b-3e3f-8765-7576cbf3b1f6 | -13.64119 | -46.87727 | 2025-08-23 04:02:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0161ae6a-1c2f-32ff-8c42-1eabec339fc1 | -13.44909 | -50.67797 | 2025-08-23 04:02:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e592674b-9dc8-3057-9ed6-22321ffbb4e5 | -15.06553 | -48.48107 | 2025-08-23 04:02:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| adfbb057-9a07-3648-83c7-d4b0ecb1efc4 | -14.96279 | -48.67137 | 2025-08-23 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4949b76-9c69-339c-9a1a-a7cac41c681b | -14.77661 | -45.39167 | 2025-08-23 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62894c28-d926-3b89-b36a-fca8862d6308 | -10.85445 | -45.20359 | 2025-08-23 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0028a1ac-2fb0-34d1-ab43-cd9bdfc6fcdd | -14.75915 | -45.38394 | 2025-08-23 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c7642ff-b3c9-36a7-89bc-612e88c625b6 | -11.45092 | -50.67192 | 2025-08-23 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 665d01fc-6c4f-3b03-8e0f-f3466dc32b23 | -12.79106 | -48.71624 | 2025-08-23 04:02:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| badbbad6-e785-36da-b013-b665caeb1b1b | -12.98817 | -45.22516 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3fa3f141-66b0-3c91-84fb-4f7bb8ad8b1f | -9.55104 | -47.94079 | 2025-08-23 04:02:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47fc05bb-f99c-3e23-849a-515027313184 | -8.78335 | -46.74654 | 2025-08-23 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a30a6335-02fb-347c-acdd-001136f4f3cb | -15.20418 | -48.70827 | 2025-08-23 04:02:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f1f22294-b93d-3002-b11a-c67922b94e3c | -11.44414 | -47.32825 | 2025-08-23 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a77bab4b-6679-3dd7-9672-404185e8e4be | -10.28236 | -46.75201 | 2025-08-23 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7aefbe26-9488-35cf-9662-696df6e3d05c | -13.00003 | -45.22267 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f3a0848f-8ece-3f78-bcd8-ae1247fdda7d | -14.81868 | -47.95458 | 2025-08-23 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d3da6f9a-36d6-3c7e-b41c-f1f0259f8a28 | -13.36379 | -54.40985 | 2025-08-23 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4fea374d-db00-3803-a7fb-a2524deb5302 | -15.1857 | -48.11021 | 2025-08-23 04:02:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfa556eb-c498-39c8-8b25-48e3c4591ca0 | -11.18419 | -55.03614 | 2025-08-23 04:02:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 12786ee4-82f3-3e96-87c6-15498bd44da7 | -11.78323 | -46.4081 | 2025-08-23 04:02:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 752d95de-87fb-30f1-92b0-cad695bb744c | -12.54249 | -45.62101 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 61472879-8df2-3bf9-8496-1857f4c34f62 | -11.18976 | -55.0444 | 2025-08-23 04:02:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README28.md)
