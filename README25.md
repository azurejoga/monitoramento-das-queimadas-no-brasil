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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0433a54-e250-3542-b8c5-7e866b112dd6 | -18.6178 | -49.1884 | 2024-10-03 01:02:38 | METOP-C | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 898c684a-b91c-370b-a678-3a79321af332 | -18.619499 | -49.195702 | 2024-10-03 01:02:38 | METOP-C | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5de2393f-4001-3776-8f23-e0b86aa5445e | -18.1651 | -48.519001 | 2024-10-03 01:02:43 | METOP-C | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4237e8d5-961e-3fbd-8edb-cf3abd09bff2 | -18.1668 | -48.5266 | 2024-10-03 01:02:43 | METOP-C | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 768fe9e3-f3ed-31ac-9deb-07cfbc59e3c3 | -17.6003 | -46.959099 | 2024-10-03 01:02:46 | METOP-C | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c78e7a36-c02f-3089-8d85-4bff0b800f0b | -17.412701 | -46.313801 | 2024-10-03 01:02:46 | METOP-C | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 781715cf-b75c-310a-b536-7a27815ec8a0 | -16.3342 | -42.300499 | 2024-10-03 01:02:47 | METOP-C | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fe9cdebe-a909-32a3-a8c0-3617c91750d5 | -17.745701 | -48.448002 | 2024-10-03 01:02:49 | METOP-C | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cc911bad-4f17-3646-85ea-ef38c6d88c55 | -17.732401 | -48.435299 | 2024-10-03 01:02:49 | METOP-C | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9c34cff0-5b92-3d60-a603-87afa7990131 | -17.7342 | -48.442902 | 2024-10-03 01:02:49 | METOP-C | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 73e53a87-505e-3eab-83ce-6fb2e09ba4a2 | -17.735901 | -48.4505 | 2024-10-03 01:02:49 | METOP-C | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d8a250cc-2ea1-37ab-b811-1686de72e24d | -18.2603 | -50.820499 | 2024-10-03 01:02:50 | METOP-C | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 18ab71e4-22f5-324d-8078-c26269d8d29b | -18.249001 | -50.815498 | 2024-10-03 01:02:50 | METOP-C | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4cb4ec0b-4c87-3dd2-867d-47f6927d9eb2 | -18.250601 | -50.8228 | 2024-10-03 01:02:50 | METOP-C | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 716ee44d-37ec-3a8e-ba3f-20421311dfbc | -18.252199 | -50.830101 | 2024-10-03 01:02:50 | METOP-C | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cf96439a-49e0-36cf-9be4-3dfbdd1ec2e1 | -18.892401 | -54.496201 | 2024-10-03 01:02:52 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9d49c7b6-52cc-38eb-bb9d-f681b4d55e36 | -18.8944 | -54.506302 | 2024-10-03 01:02:52 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 75304a93-074f-3e10-875c-a8079976a46c | -18.8964 | -54.516399 | 2024-10-03 01:02:52 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 28a90d3c-b56d-3781-9ed5-fd91e565d8b6 | -18.8806 | -54.488201 | 2024-10-03 01:02:52 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0fa41cc2-ffed-370e-b30a-289fca721c23 | -18.882601 | -54.498299 | 2024-10-03 01:02:52 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2087580d-0bec-338d-9361-ea2faa6a171a | -18.8866 | -54.518501 | 2024-10-03 01:02:52 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 075078dd-f736-3405-8fde-f6e0494059f1 | -18.888599 | -54.528599 | 2024-10-03 01:02:52 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 65c708f5-56a4-3560-a604-307b1f067ffc | -18.8671 | -54.522598 | 2024-10-03 01:02:52 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ce4b88c5-dafc-3426-bc19-500064a4f267 | -18.869101 | -54.532799 | 2024-10-03 01:02:52 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 33cf0470-0268-3b30-b2e7-50a7b6e6abf6 | -17.111601 | -47.122002 | 2024-10-03 01:02:54 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ebd6d36a-9754-3a0e-a1b4-11dda1001be4 | -17.113701 | -47.130501 | 2024-10-03 01:02:54 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d83acadf-d158-3191-92bd-f8a5cab746f8 | -17.101801 | -47.1245 | 2024-10-03 01:02:55 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ca7f5f3d-aa93-38ea-a7f2-b7fac0457588 | -17.103901 | -47.133099 | 2024-10-03 01:02:55 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b8a652ff-ea04-3e92-b400-56d853d0dc94 | -17.1059 | -47.141701 | 2024-10-03 01:02:55 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1c6229f1-4588-3c9e-961d-2ef4d5bb0e89 | -17.8354 | -50.806499 | 2024-10-03 01:02:56 | METOP-C | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9301578c-68d1-3d1a-b432-670e44fd0303 | -17.837 | -50.813702 | 2024-10-03 01:02:56 | METOP-C | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ffc3a569-4dc3-3d0a-b5d7-9b539bacbf17 | -17.8386 | -50.8209 | 2024-10-03 01:02:56 | METOP-C | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7d8a3c68-9789-33d7-a875-e414c79588e9 | -18.7209 | -57.322399 | 2024-10-03 01:03:03 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 954792a4-d238-3d9f-a8c6-81d22c287f24 | -18.7237 | -57.337502 | 2024-10-03 01:03:03 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 20ccb4b7-b78c-3b46-bc57-9029e89acb64 | -18.7139 | -57.339401 | 2024-10-03 01:03:04 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0c26c9e0-380d-33d3-b3db-b2ccdd9802f3 | -17.685499 | -52.638802 | 2024-10-03 01:03:05 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 816ab40e-9dac-30d6-99e4-a66eed2606a7 | -17.7416 | -53.1026 | 2024-10-03 01:03:06 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7e204133-ad73-3f9a-85dd-c16f087930f6 | -17.726601 | -53.079899 | 2024-10-03 01:03:06 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4d832086-0120-32c4-93e7-5d870454da44 | -17.7318 | -53.104801 | 2024-10-03 01:03:06 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 30bbba0a-236f-3bdb-ad4c-6a3e59dbbd93 | -17.6161 | -53.139198 | 2024-10-03 01:03:08 | METOP-C | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 67ddf2a7-acf5-31fc-8212-d511bbd276cf | -17.617901 | -53.147499 | 2024-10-03 01:03:08 | METOP-C | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c9bc7000-e3d9-3d70-bf23-5e37f1427c56 | -15.2368 | -43.328602 | 2024-10-03 01:03:09 | METOP-C | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| ac72eece-225d-3fdb-9d51-c76997dbf95b | -15.2407 | -43.343601 | 2024-10-03 01:03:09 | METOP-C | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| d5b16a9f-7dbd-3dad-9dbf-7a9225b9f9f8 | -15.2271 | -43.331299 | 2024-10-03 01:03:09 | METOP-C | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 8b44ae56-1ad8-39b7-bf2d-181259cd3264 | -15.231 | -43.346298 | 2024-10-03 01:03:09 | METOP-C | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 2e50462d-b347-3e3a-9d38-5e4473763a2f | -16.807899 | -50.122601 | 2024-10-03 01:03:11 | METOP-C | PALMINÓPOLIS | GOIÁS | Brasil | 5215900 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4a85dfaa-71b5-30ca-b0fb-15be3b429706 | -16.7981 | -50.125 | 2024-10-03 01:03:11 | METOP-C | PALMINÓPOLIS | GOIÁS | Brasil | 5215900 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bcd84d7c-7056-34cc-a6f9-a89ca76b919d | -16.7997 | -50.132099 | 2024-10-03 01:03:11 | METOP-C | PALMINÓPOLIS | GOIÁS | Brasil | 5215900 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| edb1777b-4278-3e7d-a364-9e9974f691a0 | -15.7715 | -47.660999 | 2024-10-03 01:03:18 | METOP-C | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| bab4b197-14a0-3e03-8027-ddb0efc71d60 | -15.7735 | -47.6693 | 2024-10-03 01:03:18 | METOP-C | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| cde2bf3d-51b5-38d5-ba00-1c5bd622400b | -15.7755 | -47.677601 | 2024-10-03 01:03:18 | METOP-C | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| dc2c3c7b-9599-3b6a-9625-2f15f11e6947 | -15.6487 | -47.193001 | 2024-10-03 01:03:18 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8fa33e47-d018-3a2f-9f20-3888a222c8f7 | -15.6508 | -47.201801 | 2024-10-03 01:03:18 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d95b9bf8-e91c-30e1-bb5c-0d4bc398618b | -15.653 | -47.210602 | 2024-10-03 01:03:18 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b80a1a5e-7836-3c49-ae20-b47b3d3e513c | -17.851101 | -57.697201 | 2024-10-03 01:03:19 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e5e4dabf-7a11-3cbd-a2f3-e7c2ab2e2765 | -17.834499 | -57.7164 | 2024-10-03 01:03:19 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fa723072-a1db-3a44-801e-a114cdc780b1 | -13.506 | -48.611698 | 2024-10-03 01:03:19 | METOP-C | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| afff0c78-eca0-3feb-b94a-fe3302e5944f | -13.4944 | -48.606098 | 2024-10-03 01:03:19 | METOP-C | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a210b4a9-e94e-3cad-a89b-8174a22439e5 | -13.4963 | -48.614101 | 2024-10-03 01:03:19 | METOP-C | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7dd3153f-3b0f-3fdd-9ddd-ba0f92b3c7a5 | -15.7156 | -48.384102 | 2024-10-03 01:03:22 | METOP-C | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b578bc27-04d7-3a46-98c9-bc7118d27826 | -16.0973 | -50.262199 | 2024-10-03 01:03:23 | METOP-C | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 01564b59-7b11-3b11-a51e-ade308d81788 | -16.0989 | -50.269402 | 2024-10-03 01:03:23 | METOP-C | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fe9e4ae0-2997-368b-a102-cfb61042eaf2 | -16.1005 | -50.276501 | 2024-10-03 01:03:23 | METOP-C | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c124c26a-fc7a-379e-beb5-7cc91e18caaf | -16.1021 | -50.2836 | 2024-10-03 01:03:23 | METOP-C | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 730bec05-c36d-3b2e-9895-16df3a1b9888 | -16.0891 | -50.271702 | 2024-10-03 01:03:23 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 261fa2b9-827d-310c-9814-e7d7e9f9f58f | -16.0907 | -50.278801 | 2024-10-03 01:03:23 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 953ca386-8609-3270-b5d0-1450a1f6d3d5 | -16.101801 | -50.373699 | 2024-10-03 01:03:23 | METOP-C | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5cba1271-a9d7-3b45-8b50-fa6242f0778c | -16.114599 | -50.430599 | 2024-10-03 01:03:23 | METOP-C | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b0bbd975-3b1d-3f33-9f45-11c09a9c3b0c | -16.116199 | -50.437698 | 2024-10-03 01:03:23 | METOP-C | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 37ae79d4-399e-3f9b-ba8c-8cd74d403381 | -16.079201 | -50.319099 | 2024-10-03 01:03:23 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 42d493fe-2dce-3809-89b9-92192b582cd6 | -16.080799 | -50.326199 | 2024-10-03 01:03:23 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8e6da99d-c3ea-329b-bf2a-e1b81dfefdab | -16.082399 | -50.333302 | 2024-10-03 01:03:23 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 70ba7ffe-1a46-3e2a-b314-6c32e45fbc9f | -16.090401 | -50.3689 | 2024-10-03 01:03:23 | METOP-C | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 49edbca1-8221-30b3-9a23-758e08c493af | -16.091999 | -50.375999 | 2024-10-03 01:03:23 | METOP-C | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4e757d35-3f87-31cc-9158-91caf940f807 | -16.104799 | -50.432899 | 2024-10-03 01:03:23 | METOP-C | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9af758a7-6e76-379c-9c5e-3b759a7ec0b0 | -16.1064 | -50.439999 | 2024-10-03 01:03:23 | METOP-C | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e3ebdd9e-3383-3102-b402-2124d552c0ce | -16.0821 | -50.423302 | 2024-10-03 01:03:23 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 24f99252-cbae-34ae-8dda-c8ff27889412 | -13.2606 | -48.578899 | 2024-10-03 01:03:23 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5e078f8f-d5d0-3876-9085-72a6abf30fd7 | -13.2625 | -48.586899 | 2024-10-03 01:03:23 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4531fc54-4b24-3523-8e0a-873818bae988 | -13.2429 | -48.591702 | 2024-10-03 01:03:23 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 66940fdd-d608-3882-b105-62c3537a3ecb | -15.5984 | -48.544899 | 2024-10-03 01:03:24 | METOP-C | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 25c9bcb3-c578-3645-979a-c91257551238 | -15.6002 | -48.552601 | 2024-10-03 01:03:24 | METOP-C | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cf96f945-65bd-3ff0-99b1-b4855321e0c7 | -15.9217 | -49.988098 | 2024-10-03 01:03:24 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ea955018-c29b-3ce4-8e08-0417f8742b35 | -13.1941 | -48.6036 | 2024-10-03 01:03:24 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| feeefaa9-778f-36b9-a772-2c06eeb00481 | -13.196 | -48.611599 | 2024-10-03 01:03:24 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 621d0976-961c-3169-84a5-244c47f8a3be | -13.2016 | -48.635502 | 2024-10-03 01:03:24 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ca5d65ce-da52-32c1-aadd-014e780cddd9 | -13.2035 | -48.643501 | 2024-10-03 01:03:24 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a8c61907-f0a6-3893-8efd-8f2a6c1857a9 | -15.8987 | -50.159401 | 2024-10-03 01:03:25 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 37a6c7cc-3adc-3877-8818-decc83a7843b | -15.9102 | -50.1642 | 2024-10-03 01:03:25 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ea3bb4de-1655-315d-bfe2-22000a6f9c58 | -15.8955 | -50.1451 | 2024-10-03 01:03:25 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 393b21a5-7329-385b-b757-a41e80b8e769 | -15.9004 | -50.1665 | 2024-10-03 01:03:25 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 43e7e7b0-5f7d-3003-8908-e2e2c90c71a8 | -15.8874 | -50.154598 | 2024-10-03 01:03:26 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 04dea603-2641-3ee3-a7fb-39d36639a5c7 | -15.889 | -50.161701 | 2024-10-03 01:03:26 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 11d5231d-ad60-3053-b733-e50efada713f | -15.8906 | -50.1688 | 2024-10-03 01:03:26 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d7350826-de87-33da-a627-eccd260cc8d1 | -15.2462 | -47.497799 | 2024-10-03 01:03:26 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d157d3ec-e5cc-3f3e-85f1-b8d32ddd9e3f | -15.2482 | -47.506401 | 2024-10-03 01:03:26 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ebc9f5f4-91c3-3728-aad3-691da194825c | -15.2343 | -47.491699 | 2024-10-03 01:03:26 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b62ca9bd-dbe1-3d64-af26-b076fbf23ca4 | -15.2364 | -47.500301 | 2024-10-03 01:03:26 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| efae5c8d-c6b9-3e55-b9de-2b7624a50e5a | -15.2385 | -47.508801 | 2024-10-03 01:03:26 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a8be4b52-d10a-3fc3-a84b-286917ae038f | -15.2267 | -47.502701 | 2024-10-03 01:03:26 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README26.md)
