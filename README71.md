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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5bd43e21-24d9-3e60-916d-178e75811c14 | -12.62669 | -56.98206 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f39ee77d-9eb3-3c33-beea-e0adc5527e86 | -15.11939 | -52.35398 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64cb9e8e-4e21-3c11-96e5-05ddf722ebe4 | -10.09321 | -59.18194 | 2025-09-08 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3667b74a-2ba8-3996-8c0d-55ef57cc681e | -13.81391 | -46.26495 | 2025-09-08 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d783be7a-ada9-3772-b5b3-f7bf9805f473 | -14.29202 | -44.87446 | 2025-09-08 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0e2a590-8280-32a0-a531-d84ebb0ccdc0 | -12.47623 | -53.85066 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39a2c68f-94b2-327a-be5f-c69565164e31 | -13.88962 | -53.98841 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd1e3f20-1b1a-395a-8956-22dabbd60f83 | -16.89436 | -45.77908 | 2025-09-08 04:53:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 72ef53a3-6840-39c3-add8-ed34ecf894c0 | -14.52377 | -48.76497 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 39a47a53-d617-32b8-9366-0235fc17e693 | -12.5269 | -53.8516 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6aa022bf-93b6-3062-bfb6-06a08658e1b2 | -15.29664 | -43.38259 | 2025-09-08 04:53:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 544b4d74-09ed-3cba-a5ca-be3d9b7dd1e3 | -14.83538 | -48.22312 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d40465d-1f32-314e-9b40-cb44fd0baa65 | -15.25151 | -52.36211 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41d311a3-7fd8-3b86-a661-7c6289830f23 | -11.10679 | -52.06289 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bcd97d0d-a41f-3505-919c-1b404ed1ff4e | -16.64079 | -49.14997 | 2025-09-08 04:53:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4dd8af2a-5587-3708-b1ea-53e6cfa2c176 | -11.18749 | -55.04858 | 2025-09-08 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b4eefe5-9d38-37e1-91b5-320519d114e3 | -14.69331 | -53.03536 | 2025-09-08 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28577e5d-e374-3c18-a4dd-9986cf001230 | -12.166 | -43.94072 | 2025-09-08 04:53:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76da6490-c722-3f4f-8adf-623de3525598 | -11.11518 | -52.0299 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 32a234c7-6ea9-30e1-b131-780e082d35d2 | -13.29921 | -51.73803 | 2025-09-08 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc2ab653-fbdf-3c3d-be43-c03369175b98 | -11.60734 | -47.15406 | 2025-09-08 04:53:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f6f51426-1fe0-3e0f-be4a-884f6bbfd50f | -16.33904 | -52.94375 | 2025-09-08 04:53:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9befa6cb-4da8-3a42-92a7-c77476917ded | -11.59705 | -52.20172 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40f71479-8bb3-315c-b44f-ac1b3fb6a85f | -12.87736 | -62.10715 | 2025-09-08 04:53:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 903af52c-5432-37ad-bd67-5da3f3c9c3ed | -13.00855 | -54.81504 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30a4705b-85d2-31db-aa83-10bb3cd20a33 | -17.66301 | -44.18539 | 2025-09-08 04:53:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 60ae580a-3e34-3d6f-a799-b9d51fff13f4 | -15.54568 | -48.38085 | 2025-09-08 04:53:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 479eb1e5-5af9-3f4d-8c8b-9b8d6650a910 | -10.3544 | -57.50346 | 2025-09-08 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8dedaebf-a3aa-3ba0-8238-9b6e788dc801 | -10.96805 | -56.20155 | 2025-09-08 04:53:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 642993d1-48f0-3d09-806e-dc98e69be3fa | -15.26655 | -52.38078 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 23d8c1d0-99fb-3713-b417-59807163f6a5 | -16.97909 | -45.83228 | 2025-09-08 04:53:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7333e320-c6c7-33d4-8710-d8e79ac6b4c5 | -11.62814 | -52.23299 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f557f124-cd5b-3fb1-ad82-04fb708b8746 | -12.94712 | -54.77246 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bd6ec36-7c02-3db3-b43f-0ae0f3a76556 | -11.10774 | -52.00969 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 10a3076c-3a5f-385f-89db-c93177350e3f | -15.83661 | -52.29119 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb3aed5a-e36c-3c40-a091-a033e043600b | -11.6761 | -47.17014 | 2025-09-08 04:53:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2d84fbc-d8d5-33b3-9f2a-e8338f2c24fc | -11.67452 | -47.16743 | 2025-09-08 04:53:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec2bf9cc-ccf5-363f-8a03-349cd6ee449f | -11.10283 | -52.06607 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 568d63e8-24db-3469-bfca-642b0682a98c | -14.50031 | -48.81359 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91129675-5a16-3293-b71b-4ed4025a9707 | -12.82386 | -52.88619 | 2025-09-08 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3d58498b-d44c-30c7-9369-34c80492d8ac | -15.7516 | -53.591 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a2ca651-46ed-33d2-85d8-77c45fc66fda | -11.22059 | -55.01345 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9942b081-4202-3ecb-904a-832a5ae5fab9 | -15.70575 | -46.55233 | 2025-09-08 04:53:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 54a82ccc-0719-3c93-abe8-b507ef9c3f46 | -14.7156 | -55.91116 | 2025-09-08 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b7727c5-7b4a-3541-ad89-ad9599f15d5a | -15.66818 | -53.87003 | 2025-09-08 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f917555-a8d2-313f-9dbc-b2ef210b79bd | -16.34992 | -52.9414 | 2025-09-08 04:53:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b5dc7bbb-bd67-3007-82cc-ddb628a18592 | -14.88262 | -55.80116 | 2025-09-08 04:53:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53d72da1-69f8-39eb-adf2-321fbae8f872 | -12.00136 | -47.76865 | 2025-09-08 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 683656bb-7740-3697-a49a-e44f573e0d51 | -11.22785 | -55.01099 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24fef30a-64d3-3a6b-963e-3b6f095f51f2 | -12.4207 | -63.89912 | 2025-09-08 04:53:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 284f1790-185a-3d17-a810-ab617d26bdc4 | -13.91939 | -53.97144 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 403bed2c-5c7d-3e3c-8445-192f894071f1 | -14.8092 | -48.18265 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39e45213-584c-3933-b615-f158e1861fec | -11.64179 | -46.63219 | 2025-09-08 04:53:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 24dadaf3-c8bf-3e0f-8746-863120c1ef28 | -16.43748 | -49.28951 | 2025-09-08 04:53:00 | NOAA-21 | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5a014f40-3369-3917-8a2e-37c120c7c43e | -13.0437 | -47.14352 | 2025-09-08 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a9b64eea-dc1b-3904-8b2c-777a07dc4ebf | -11.21115 | -55.00822 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe8ac4f5-0b8c-34bf-bac2-296e56a860a6 | -11.04081 | -52.05705 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c2b144f-0194-3dd8-a880-6e31df7d6d73 | -14.60596 | -48.08889 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a6f87e4-bbd8-351f-ac29-7b0c5e617698 | -15.68444 | -53.55757 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e82a2f84-e2a5-387c-a54b-dde8f17623d4 | -14.09238 | -46.60772 | 2025-09-08 04:53:00 | NOAA-21 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2ebaf7e0-2271-3fb4-b38e-2eb6dc55f844 | -10.1762 | -61.13715 | 2025-09-08 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3e8a4245-7225-382b-91cd-afdb0bdc9b23 | -9.3001 | -66.61258 | 2025-09-08 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d2adb708-0478-3d56-be58-0bb85028987f | -12.00453 | -47.77799 | 2025-09-08 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 931812c8-af46-3da2-864d-91bef2023d3d | -15.11069 | -48.07121 | 2025-09-08 04:53:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 955d7689-08a9-3573-8d20-51ea7c15fc54 | -10.5106 | -57.79636 | 2025-09-08 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 203d0c3f-f943-3236-bc40-37006ff5cd93 | -15.13738 | -48.06368 | 2025-09-08 04:53:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a72de2ca-1863-3aee-bc5c-19cbd3121e19 | -17.39994 | -49.30774 | 2025-09-08 04:53:00 | NOAA-21 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e7f86ff-65c5-3ce6-8d6e-dc189948a001 | -16.34591 | -52.94481 | 2025-09-08 04:53:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e6ee7459-5cca-34a5-bc97-4dd73be8c368 | -11.08267 | -51.98721 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 427fcfd8-71bb-3ae2-9f7e-7901bdd9ad03 | -11.32228 | -55.12223 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 328f8a10-799a-3508-82e4-f09ebf2d2d76 | -14.50922 | -56.49046 | 2025-09-08 04:53:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98b0b04e-45a3-34a2-a8af-c4b13ab060f4 | -12.41527 | -63.89804 | 2025-09-08 04:53:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04ecab9c-73c4-3b87-b324-596e806e9e9d | -14.52851 | -48.76154 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83d5eb1e-da82-3508-9a98-8bdc467dc993 | -12.20028 | -53.91759 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7b4c89ac-a664-3a9d-b89e-659879cc50fa | -14.50553 | -48.80637 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8de8ed06-809f-3184-bb6b-cdd438ac3710 | -15.74321 | -53.53275 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3bf0ae5e-0d31-33fb-af1e-a5ca1d662206 | -17.39941 | -49.31191 | 2025-09-08 04:53:00 | NOAA-21 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0541f063-f5cb-3d59-abcf-a3d5c16143a7 | -13.00799 | -54.81858 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c4cf02d-1363-3ec0-a011-3c224b482664 | -15.53568 | -49.23712 | 2025-09-08 04:53:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8ce007a-eea6-38c8-afce-e912c2227f84 | -13.91601 | -48.01624 | 2025-09-08 04:53:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92adfd1c-2684-30bc-b343-92119fce90bd | -12.94763 | -54.79069 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3d11800-f336-3dda-b6a8-f140df3f7cec | -16.33557 | -52.91932 | 2025-09-08 04:53:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c0caaa0-e449-3548-8b3b-bdb36b774a4d | -13.82418 | -43.86407 | 2025-09-08 04:53:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53dbaa72-09e8-325d-b50c-49f4ec9f2436 | -15.75216 | -53.58731 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43d323a2-34cf-37ec-a45f-7c66a946192b | -13.74685 | -46.91031 | 2025-09-08 04:53:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 106d90e9-1618-34c3-b6cf-65e9dd23d398 | -14.70851 | -60.25106 | 2025-09-08 04:53:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40fe7a0d-94a8-3f6b-8bf2-4fd9b3f58a0a | -11.11185 | -52.05224 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2006c5b6-dd84-3d82-a551-627814245e42 | -14.69725 | -53.03219 | 2025-09-08 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93f858c8-3f18-3fc1-beb2-1a9395bcfd46 | -15.83485 | -52.30319 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4314fdf-e5c5-3e22-b282-9407b45204bf | -9.12546 | -65.95815 | 2025-09-08 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7ae2221e-8f91-3ad8-805b-b92e02e0ab31 | -14.29746 | -44.87538 | 2025-09-08 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9777a26b-5813-33f8-a94f-c057290141ba | -15.7671 | -53.57073 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 661f0f0c-0970-3a8a-a527-9cad13cf466e | -11.11462 | -52.03362 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85cd9ed5-67c0-3e97-9d6c-9608ff88d7b4 | -12.528 | -53.84455 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c12f12fd-52aa-355a-a992-c770d345dd5c | -10.08906 | -59.18125 | 2025-09-08 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 695f0bb6-58cd-3bc1-a887-57a65088061b | -15.73929 | -53.5815 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 671f0afe-c40a-3640-907f-144e40d790e9 | -13.82596 | -46.24913 | 2025-09-08 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 29b0257d-1b20-3f23-99a6-e1feabd5dab1 | -11.66591 | -46.88455 | 2025-09-08 04:53:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1b02e2f8-1eb9-334a-95b8-f24e496061f9 | -10.05244 | -59.36598 | 2025-09-08 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9e2dacf5-12c0-3811-83c2-deefcc49814c | -17.66528 | -44.19022 | 2025-09-08 04:53:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README72.md)
