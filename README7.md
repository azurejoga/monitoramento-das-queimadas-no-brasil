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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7df835b0-e42f-37c1-a68e-8c6aeb285105 | -7.24573 | -48.48546 | 2025-10-03 00:52:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 93f5bb9a-d457-32f7-894b-de55a92f9b67 | -11.81867 | -45.05397 | 2025-10-03 00:52:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 15b2df56-2b6b-3e7e-ab6c-debb01e43bdc | -15.22508 | -56.80863 | 2025-10-03 00:52:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 6892f50d-6ee6-3717-9e6b-2cd7d47276e1 | -12.75748 | -44.9037 | 2025-10-03 00:52:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 9ddf7da0-78b6-32ff-87ca-a97b3eca7228 | -10.89941 | -56.20948 | 2025-10-03 00:52:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| cbe88176-1177-35f7-8d8d-af30fe084c53 | -13.30417 | -47.59896 | 2025-10-03 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 9a348313-278d-3c41-80ee-c1c274fa496c | -11.90789 | -46.27563 | 2025-10-03 00:52:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 44.1 |
| db79d9fd-524b-338d-9794-ed65b71d5b4c | -14.61973 | -48.23826 | 2025-10-03 00:52:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 749e3466-44e9-3e18-9560-4ddadbe2fc0f | -13.63165 | -50.28942 | 2025-10-03 00:52:00 | TERRA_M-M | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c99a89fc-dbf8-3ffb-84fb-91681a9da07e | -13.76315 | -48.08346 | 2025-10-03 00:52:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 62a76449-04a2-35d1-a5b2-693d02160d8d | -10.27137 | -50.35546 | 2025-10-03 00:52:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 53070194-ba9c-331c-bfbc-23f3ab55c65b | -10.30154 | -48.28911 | 2025-10-03 00:52:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 1dcdbc70-ef46-3613-96c3-b07797016091 | -12.63942 | -46.97486 | 2025-10-03 00:52:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 0b7d74e5-ceef-3dcd-b4ac-8665c8ea67bc | -8.56059 | -48.65552 | 2025-10-03 00:52:00 | TERRA_M-M | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 13.8 |
| c5121a83-e872-3c7c-ab01-38ea5c6e7e93 | -7.79706 | -46.02569 | 2025-10-03 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 3ce2a240-a92d-3709-aca7-82619f4fccea | -12.30022 | -45.38263 | 2025-10-03 00:52:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 2ea2e953-bf05-3f3d-af97-fb93208901bd | -11.01703 | -46.54564 | 2025-10-03 00:52:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 15907a40-270a-3a15-a8fd-13d3d0b85375 | -13.79765 | -47.58682 | 2025-10-03 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| ccad41cd-dd8a-35e3-bc93-f2f8d8460bb1 | -12.47729 | -54.42203 | 2025-10-03 00:52:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e9fdba8a-bc53-342a-aa16-f1f26fd44986 | -8.65557 | -47.7238 | 2025-10-03 00:52:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 3f078f5c-31f2-3069-8224-ac7dfc786eef | -12.92468 | -46.38074 | 2025-10-03 00:52:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| bbd84376-7581-3682-a6bc-430a6673752c | -13.75692 | -48.0617 | 2025-10-03 00:52:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| d4dfb0af-baa2-3503-ad99-cd3d43823802 | -13.76122 | -48.08942 | 2025-10-03 00:52:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| cb14a43b-841f-389a-ae1b-3d69538c67d8 | -9.91197 | -43.72243 | 2025-10-03 00:52:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 178.7 |
| c152f5e6-2280-399a-bdde-cfa39b4a35ea | -13.64106 | -50.2879 | 2025-10-03 00:52:00 | TERRA_M-M | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 23.2 |
| a055bc53-a540-369f-95bc-845c94a0ccf2 | -10.17851 | -45.5119 | 2025-10-03 00:52:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 0ed5e071-08b9-363d-ab31-06c269a3b7f7 | -13.21566 | -47.84162 | 2025-10-03 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 2e0f6b44-74b3-30d7-bb97-e8b134aee211 | -13.35445 | -47.33461 | 2025-10-03 00:52:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| fdb010b3-82b3-3329-967f-cdba58e562e6 | -10.26157 | -50.35698 | 2025-10-03 00:52:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 1629f050-4477-3ce2-9f45-e8cac9924791 | -14.46629 | -48.40489 | 2025-10-03 00:52:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| cb33dd15-78e9-333a-93ef-cf5ae2b0c695 | -10.82965 | -49.37835 | 2025-10-03 00:52:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 29849fa2-021c-397d-b341-db5976ef4d44 | -7.2576 | -48.48367 | 2025-10-03 00:52:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| e15398d9-8d2c-3e82-b106-5a876d92f62f | -14.46303 | -48.41228 | 2025-10-03 00:52:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 9c6edcb5-b76f-3f85-b88d-57994ea19db9 | -11.13547 | -47.20734 | 2025-10-03 00:52:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| df3871e4-d91b-3a4e-b2ae-6a302c9d9f6e | -13.29498 | -47.26264 | 2025-10-03 00:52:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 20.5 |
| e2d6d85c-9501-33e8-b1dc-a5bdd0ce3e1a | -13.57846 | -47.58414 | 2025-10-03 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b6b6cfe8-626c-325f-9a8d-4e91325584aa | -9.92109 | -50.90559 | 2025-10-03 00:52:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7dcb05b4-718c-3ad5-9711-d080537305e5 | -13.34838 | -48.09565 | 2025-10-03 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5ecdc0d1-8ccd-35a3-bd2e-305eacafcb33 | -12.61231 | -46.96123 | 2025-10-03 00:52:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 43.9 |
| dccf677b-0aea-3982-abcc-619cef23e831 | -13.27604 | -47.26992 | 2025-10-03 00:52:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| bc9d79c0-8935-3792-97e9-746562114f44 | -8.62223 | -54.98479 | 2025-10-03 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 6d85d63b-78b4-3cb7-86b4-a70957bde6b6 | -6.95429 | -45.35005 | 2025-10-03 00:52:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 3d7ff845-1108-3ea8-aa83-500586478ab0 | -10.17427 | -45.48616 | 2025-10-03 00:52:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 42cbf076-6abd-3087-8061-c14c1880c183 | -6.2385 | -45.36051 | 2025-10-03 00:52:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 407.2 |
| b5a7bc7d-b7ad-304d-a444-9bb3115c91e1 | -14.61532 | -48.24517 | 2025-10-03 00:52:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 5bd52801-7b10-3fe3-8d53-bbdb6d8e9074 | -13.32511 | -47.5919 | 2025-10-03 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 9a3ca014-bd39-37af-86df-21de8da428d4 | -13.77407 | -47.582 | 2025-10-03 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 19.3 |
| b6c17cf4-1d2d-333c-b4ff-c5e49c885ba4 | -10.15992 | -45.48828 | 2025-10-03 00:52:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 647abf95-6dcc-3408-92d9-adb64293e5da | -7.66598 | -47.28944 | 2025-10-03 00:52:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| be8b5f3b-2150-3e56-8bf9-bb8b32cd83e7 | -7.25503 | -48.46662 | 2025-10-03 00:52:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 95256451-0993-3f83-b0f9-b877136f7cc4 | -13.67879 | -48.64024 | 2025-10-03 00:52:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 44aeb8ef-8e31-3051-8327-22b399b5aad4 | -11.32776 | -49.02291 | 2025-10-03 00:52:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 89450ddb-84c3-3a23-ab6c-3e17bcbe18c8 | -11.08731 | -47.87204 | 2025-10-03 00:52:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| baf63147-0557-3788-83a0-7747f30c8d28 | -11.5344 | -49.82626 | 2025-10-03 00:52:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 56207ad7-93d5-3e15-baee-dc9633dd1df2 | -11.8671 | -44.99103 | 2025-10-03 00:52:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 1fd6088d-197c-39c1-b88b-abb69b58995b | -10.89799 | -56.19846 | 2025-10-03 00:52:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 8b28624d-3847-3a8a-b5a7-f0ac173dd3a5 | -13.55793 | -47.30431 | 2025-10-03 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 21.0 |
| c68a0e30-c62e-30e0-8515-7408d95c02d3 | -11.91113 | -46.2958 | 2025-10-03 00:52:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 6bf067d0-1c1b-3b54-9e2d-b04fbf2eb611 | -13.77265 | -47.5759 | 2025-10-03 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 35.3 |
| b70e80c1-449c-3af5-8f01-cf19df665fa0 | -14.18546 | -46.69133 | 2025-10-03 00:52:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| e1c5dafc-fc1f-32c9-b21f-43aeeae63190 | -12.62737 | -46.9773 | 2025-10-03 00:52:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| c38441fc-4226-3cba-bf47-aafc45b44a37 | -12.38021 | -46.51206 | 2025-10-03 00:52:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| a113f454-7e06-376f-8828-04e0d8098b3f | -9.87886 | -47.80846 | 2025-10-03 00:52:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 44.4 |
| d1e5531a-1442-36be-a5c4-7a1d70c31795 | -12.29182 | -45.37744 | 2025-10-03 00:52:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 41.7 |
| a5227819-3249-3ab2-b4b7-c14c9a9adb02 | -8.58905 | -44.77641 | 2025-10-03 00:52:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 1b5d5ccf-9eef-338a-a716-8e929a8470f9 | -7.74486 | -46.24428 | 2025-10-03 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 900578fa-5a57-3a83-ba14-28156c1bd524 | -8.65264 | -47.70535 | 2025-10-03 00:52:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 3ac063b3-ab0e-3150-9371-3318c3d1b72c | -8.70991 | -47.98904 | 2025-10-03 00:52:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 7ae4abd6-2da8-3eb6-9623-cd0feba137dc | -14.58806 | -52.47104 | 2025-10-03 00:52:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 131c9857-6d5c-30d1-9784-329531963d51 | -14.87716 | -50.23661 | 2025-10-03 00:52:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 47cf8e22-cdf9-3ad9-809c-f4862b4b4e28 | -7.24759 | -49.40767 | 2025-10-03 00:52:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 2d6107db-3b3c-37a1-8b4c-6e6669d7fba9 | -10.82368 | -49.38511 | 2025-10-03 00:52:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 870157a5-f05c-3143-9291-f2fb3fd0b2be | -10.11513 | -54.99469 | 2025-10-03 00:52:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| fa7fc450-32a3-372b-b750-2b30cc010363 | -14.87867 | -50.24677 | 2025-10-03 00:52:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 832bfceb-20e3-3891-b55c-834b3d99ce30 | -8.37542 | -48.64907 | 2025-10-03 00:52:00 | TERRA_M-M | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 26.1 |
| d55c7fb3-5084-3748-b2f5-22d5a7936390 | -13.76553 | -48.04506 | 2025-10-03 00:52:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9e09eabc-b53f-353c-b104-2d583eb0c813 | -10.76163 | -45.34958 | 2025-10-03 00:52:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 4991b0b3-d5f0-37c6-812e-8519809cb9d3 | -13.76932 | -47.55186 | 2025-10-03 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 942255b6-dc0a-3614-b660-8ea6d6b062b8 | -11.86925 | -44.98438 | 2025-10-03 00:52:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 29.4 |
| ab34c606-c4ef-3fa8-a6ae-8ad44639a11c | -11.07445 | -48.37368 | 2025-10-03 00:52:00 | TERRA_M-M | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 0d7e1081-9cfe-330f-a5b3-032ea1efe375 | -13.77835 | -47.5353 | 2025-10-03 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 30.0 |
| c0df317c-a227-37e6-baad-0f8f0adcbd47 | -6.72629 | -44.15148 | 2025-10-03 00:52:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 423f224e-d8f4-397f-b91f-58eff619d881 | -14.04504 | -53.89248 | 2025-10-03 00:52:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| fb812c43-88e9-31e9-bfc6-3e92aa540a91 | -10.68137 | -48.58969 | 2025-10-03 00:52:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 46.1 |
| fbf3142c-b325-3b12-a872-6dce72b24c5f | -10.93264 | -51.08286 | 2025-10-03 00:52:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 048b58b6-9339-3461-9f21-ae111a92f8bb | -9.47704 | -47.86899 | 2025-10-03 00:52:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 30.4 |
| c9c7e4ee-90b1-3196-83d2-a55dede4eb11 | -11.90583 | -46.74435 | 2025-10-03 00:52:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| dfe1508b-dfb2-37c3-a68d-c643fa22b21f | -13.554 | -47.29888 | 2025-10-03 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 20.5 |
| a0535eee-e330-3b1c-a29b-b85938f1ea36 | -11.91829 | -46.26556 | 2025-10-03 00:52:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 77409999-5304-3a85-bb6c-9d4bee05d602 | -11.15289 | -43.43951 | 2025-10-03 00:52:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 8c355198-6807-31a8-a7eb-736ac4608d86 | -11.32569 | -49.00977 | 2025-10-03 00:52:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 0ae3729f-da59-3f50-b9fb-0895178124cf | -9.92262 | -50.49112 | 2025-10-03 00:52:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7c7d1c59-090e-34cc-9b86-42db5497b326 | -8.68959 | -47.69939 | 2025-10-03 00:52:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 43bf986b-385b-3f6f-936a-9b4315015ceb | -14.0148 | -44.97105 | 2025-10-03 00:52:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 45.0 |
| f814ed32-5e20-3f94-82ff-a2aa9c9c3e90 | -13.5399 | -47.28579 | 2025-10-03 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 773f18f1-c498-3c56-9d0f-8f3947317edd | -13.95902 | -48.10398 | 2025-10-03 00:52:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 5ccf623e-7e84-35f3-a17d-c6dc5bae0f22 | -10.87984 | -53.7748 | 2025-10-03 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 799eb22d-b3ad-373f-9795-4e9cc2133e9e | -7.5162 | -50.50434 | 2025-10-03 00:52:00 | TERRA_M-M | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ce4f0ba9-61e8-3527-b00f-0818edea3943 | -8.02635 | -55.41549 | 2025-10-03 00:52:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 89def45d-4f42-37a6-acff-ca5015129d75 | -10.41304 | -54.40483 | 2025-10-03 00:52:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README8.md)
