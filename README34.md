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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63df119a-6cba-34c4-a78e-3ffec30c8ee0 | -9.18481 | -59.64468 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f7cb6b4d-184b-3f96-8810-f8b50551dbdf | -13.03028 | -46.78743 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 67ac6a54-5017-3c29-bf36-65824ea1506a | -9.23132 | -59.59798 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c783737a-39e0-36db-845c-21d86ddd0781 | -11.66734 | -60.18348 | 2025-08-20 04:36:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2a8808b-f086-33ec-bf59-628af4b31ee0 | -15.3513 | -47.26577 | 2025-08-20 04:36:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8cfb345-0906-31fb-acbd-f3f539bb67db | -13.00468 | -45.18271 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8046d856-d856-3ed1-a419-75e59e12ebcf | -13.03029 | -46.8119 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec9a0443-0315-36dd-a4a7-e273e76e93e3 | -11.58646 | -50.54364 | 2025-08-20 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 440d6e8f-bdac-39b8-a6a0-b6b59748a2a5 | -9.19387 | -59.62864 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f11cce10-150a-35c8-82ff-6707e7c79424 | -9.17697 | -59.61952 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c1490ef-fc6d-3637-9002-94f57ced2eff | -14.89131 | -48.07125 | 2025-08-20 04:36:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29e8b6b8-c4e1-3ef8-8a30-bb2ab8c6ba6a | -14.61768 | -54.91151 | 2025-08-20 04:36:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9e5b13fc-b227-3f61-9c1a-bb60f32fcf61 | -11.44645 | -47.32146 | 2025-08-20 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a874a4e-529a-345b-87c2-171a38e9a1af | -12.99243 | -45.21438 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b5bc44d-7d84-357b-94fc-aaf863049dc4 | -13.30969 | -48.70193 | 2025-08-20 04:36:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1278f4d-51f3-3a04-acc3-dc1b7fd6f383 | -15.42969 | -46.71886 | 2025-08-20 04:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6276026c-9e50-3f3b-8dcd-2c87c83e16fd | -8.87545 | -62.40001 | 2025-08-20 04:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2bf2243f-1c3f-3beb-9333-ac8ae62bfde1 | -13.19616 | -50.74523 | 2025-08-20 04:36:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c718d2fb-03f1-34ee-93a4-ba9a74a2ad29 | -9.21242 | -59.69559 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 988c6d1c-7b20-3a46-a9dd-8aa9c820818c | -13.03376 | -46.7881 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6f4b2a3f-7fff-30ee-a22c-66ea731d9524 | -13.55744 | -44.45574 | 2025-08-20 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e968019-adb4-3760-82be-3240a0790b58 | -14.88852 | -48.08992 | 2025-08-20 04:36:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8fe8d903-b54d-3159-baf8-5c64458ecb9a | -12.97435 | -56.87103 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f34c7b9-06b8-3708-b825-65b6942d11cb | -14.89414 | -48.0756 | 2025-08-20 04:36:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef0ed21d-661b-3d11-a075-7f5766f0f9f2 | -13.57259 | -47.03469 | 2025-08-20 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a3649660-10f0-3c2d-a5ab-d4f9e64ae6e4 | -13.15552 | -54.92651 | 2025-08-20 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7364a396-ab7d-3a35-b5c6-9628f85a4675 | -15.57337 | -50.3077 | 2025-08-20 04:36:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6bd8fb2-d6c6-3a70-9cb8-50150596a51c | -9.18773 | -59.62776 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 159844d7-14a0-398d-af67-4a24b62f9005 | -13.10982 | -51.9123 | 2025-08-20 04:36:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a0794b75-a942-36d6-a078-7682d4359bcc | -11.75291 | -48.19067 | 2025-08-20 04:36:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 190155e9-dade-34d1-ab69-f469bb8874c4 | -14.322 | -51.98734 | 2025-08-20 04:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30caa2ef-5c1c-32ff-b2c9-69843314aeda | -14.70355 | -45.83877 | 2025-08-20 04:36:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 610fce05-c1c1-38f4-b4ec-98d0f58f09ff | -12.94371 | -46.12312 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c4a65862-bf79-3c64-8d6c-c729abbe39e2 | -12.66758 | -45.82024 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 768b73a8-57cd-330b-81bb-a1931212ca76 | -12.77578 | -48.26814 | 2025-08-20 04:36:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb2cf4fa-f15b-30cf-a450-cdc969ca49cf | -14.74996 | -48.38653 | 2025-08-20 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 513e6311-05e9-3230-9b37-10e252c9a5f0 | -13.18823 | -54.96091 | 2025-08-20 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 48db040f-0095-3114-ad03-c4a19ba76f83 | -13.57434 | -47.02285 | 2025-08-20 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce4f4cfb-afee-37d5-b4b8-41f2f88f27a4 | -12.95327 | -46.15872 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eeb612a4-dd07-36d2-958c-72cd12725f37 | -12.96957 | -56.8472 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4731a4b2-c629-3860-ab67-d9c9a5bf6686 | -8.88114 | -62.40875 | 2025-08-20 04:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 31ac0685-3545-36ce-a2d6-9d92461d5a3f | -13.14115 | -57.15605 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61bbea16-8f91-3598-8efd-22edbf65e816 | -14.3598 | -51.99827 | 2025-08-20 04:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55fb42c2-199b-30c3-9264-1b8f4bcd0791 | -13.58247 | -47.01611 | 2025-08-20 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 340ecad2-b7cd-3274-8ad4-b72059c4bfd9 | -9.20777 | -59.62202 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ae3c4c05-6e1b-3d8a-958c-1b3c39222551 | -12.98751 | -45.19455 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| bd98c7f5-c78c-35ce-8645-b574ad82e3f7 | -10.27253 | -46.76529 | 2025-08-20 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d82f265a-ba2d-3032-8dec-7763f7006ba3 | -13.33681 | -54.40477 | 2025-08-20 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 179ff15d-c5c9-352e-8546-a95e61c7797d | -13.13527 | -57.16055 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0312ceb7-80e8-359c-882f-198ddab47af6 | -13.1401 | -57.16153 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 340f678b-949a-3483-802c-e38612c8fc0f | -11.31821 | -55.21197 | 2025-08-20 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da51c815-3943-340e-b2da-bdf79a67c3e5 | -12.63749 | -46.88676 | 2025-08-20 04:36:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 860af386-fdba-3db3-a5c5-9b623a6d5b8c | -12.98483 | -56.86782 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 04ec4a75-237f-3759-a725-99aa32f84671 | -13.57608 | -47.03522 | 2025-08-20 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd7d2bc6-026d-3785-bcab-0747a21555ac | -12.96767 | -56.85756 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2dbbd5b-43be-301a-a286-74806f8fc423 | -13.22993 | -50.8157 | 2025-08-20 04:36:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 169e91e7-e062-3962-9e87-801c3fb63d4a | -12.96305 | -56.85277 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b04e285-4c34-3ddf-9d48-178c62412112 | -15.71381 | -48.62506 | 2025-08-20 04:36:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a39f3644-a361-3dad-96d4-5db5b20bab47 | -14.96309 | -50.12477 | 2025-08-20 04:36:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cfd81610-b499-3f6d-9d5d-5a6a028632b1 | -12.22678 | -53.60368 | 2025-08-20 04:36:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31e563c4-630b-3dcf-ba44-4b2a052ba93a | -15.43029 | -46.71463 | 2025-08-20 04:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab148808-ecbd-3d4f-914c-212a342f8a9c | -11.97366 | -46.78021 | 2025-08-20 04:36:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3780fe38-6080-37bc-bab3-80248df9b8dd | -13.19295 | -46.87598 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0699d5b6-12b8-3d94-a14f-e0e62f2aea14 | -11.56676 | -50.44944 | 2025-08-20 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad31a360-cdc1-3aad-9add-614d61c092bd | -10.47019 | -48.35288 | 2025-08-20 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 63c992a7-b05f-3adb-a57f-3f87a6113dd9 | -13.03725 | -46.78876 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15d32970-6317-319b-b620-e9e3440eca82 | -9.19182 | -59.64094 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ead38f26-1614-318e-85f9-8f9f7ea5ca17 | -14.45969 | -48.47919 | 2025-08-20 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 017c5894-6f31-3567-b8ae-4c90a299c21b | -13.1341 | -57.15362 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71b08e06-7f2d-316b-a29f-618ed57b17a9 | -9.19207 | -59.63784 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 63bbb8ef-e10c-389e-b262-3f4931375089 | -14.15791 | -45.28954 | 2025-08-20 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f204f61-4fee-3dba-8cf0-fa64d97970b3 | -12.43036 | -48.70266 | 2025-08-20 04:36:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5b05dc7-4a10-3c4d-a9e9-b38e8fb9b9e3 | -9.21336 | -59.69449 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db11eb35-f085-3933-9a4b-7ec05215dcee | -12.47976 | -44.78775 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d489b7e-8731-3e2e-80e8-0db6c776b86d | -12.99621 | -45.21494 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75dabde2-ca61-3fa7-b999-3fea50f9c60b | -13.57783 | -47.02339 | 2025-08-20 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 567e6b9f-d687-3803-aa81-6344eb0d38c5 | -13.00535 | -45.17802 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 437b96db-0f25-32ea-9008-b1b8974c1bf7 | -14.15858 | -45.28476 | 2025-08-20 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1eb3f428-aad8-388f-bef8-8e43f46e14e3 | -12.5098 | -47.43435 | 2025-08-20 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35e71ab5-dcba-3061-802f-d265eacd650d | -14.1624 | -45.28535 | 2025-08-20 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21e2478a-c62e-3f73-a087-1f73e292598a | -10.27878 | -46.77029 | 2025-08-20 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c87db72-5af5-3f84-a1ef-7df9c1bc096e | -14.63014 | -54.8832 | 2025-08-20 04:36:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8917b0c-b154-313a-8e55-979b58342698 | -13.32681 | -54.4141 | 2025-08-20 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fcdb6f6f-0ff4-3634-8e8a-27d28b42525e | -13.14646 | -54.92889 | 2025-08-20 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 21e03a33-b560-3a70-8cbb-edda3cfa1eb1 | -9.19265 | -59.63654 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d98bc4c5-6b9a-316b-b7b7-1568f37bc237 | -13.18938 | -50.74407 | 2025-08-20 04:36:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30f6a189-4863-3125-bea5-e76243cdf092 | -12.66411 | -55.79233 | 2025-08-20 04:36:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0dc4c0a-bff9-3c1b-958f-9f489a1df7f7 | -9.1753 | -59.59511 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 65f46c11-75f0-304f-8c35-bd9241e6f48e | -11.77534 | -47.56353 | 2025-08-20 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bce466cf-c1d9-3d76-b1fc-7519b8fc6b28 | -15.16221 | -49.80885 | 2025-08-20 04:36:00 | NPP-375D | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68eaf8f7-6acb-365a-b71c-d971b15f4069 | -12.81426 | -48.56433 | 2025-08-20 04:36:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10fb4277-d190-3628-bb0d-35db0bb8eba5 | -9.18745 | -59.5974 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e41f6712-5ada-3251-a65a-038bf68e6480 | -10.8178 | -43.28126 | 2025-08-20 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 680325e1-6f01-3fbf-93e1-107e53befd4e | -13.03242 | -56.85065 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b047b804-93be-3fae-8d42-9bad0f4753c7 | -13.40096 | -46.37357 | 2025-08-20 04:36:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5ee30bf4-d520-31eb-b32b-ae72249a5b2f | -12.09477 | -47.91117 | 2025-08-20 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ffa7e147-b170-362e-923a-71a91294b48a | -12.14207 | -48.01408 | 2025-08-20 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 531bda20-b506-3f97-83ce-9775d3a10adc | -13.48926 | -47.06234 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b511f706-4da9-3b88-bf84-034e0e5caf1f | -13.34148 | -54.40194 | 2025-08-20 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1da00be-1e7f-392c-9e11-b240eba264f2 | -13.60112 | -46.91413 | 2025-08-20 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README35.md)
