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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78d95924-cc21-34e1-b4ca-7cf0ed664629 | -21.708099 | -48.417599 | 2026-05-06 00:56:00 | METOP-C | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b6bcd985-ad29-3bbb-ad5b-5bd20ed7c009 | -19.945601 | -54.370701 | 2026-05-06 00:56:00 | METOP-C | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 915b35c4-40c5-3db5-9fe4-09a0865bc5b9 | -22.806801 | -49.336498 | 2026-05-06 00:56:00 | METOP-C | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| fd2ebc4b-a772-368e-a40e-46ea27872388 | -12.2797 | -43.510899 | 2026-05-06 00:56:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 68642409-9a70-36bc-8701-59d64bf1349a | -12.4884 | -58.473099 | 2026-05-06 00:56:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bf62fac3-f75e-3393-a43e-128fa90d18ee | -20.2064 | -50.634998 | 2026-05-06 00:56:00 | METOP-C | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5de36305-9eb4-397d-916a-49b2e574b470 | -18.4417 | -54.699501 | 2026-05-06 00:56:00 | METOP-C | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0bae5aed-56f6-352c-aa96-d25b17d451d7 | -12.3473 | -50.007198 | 2026-05-06 00:56:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cabae4fc-3f27-3804-9a79-2d2d80ee6df5 | -12.3456 | -49.999901 | 2026-05-06 00:56:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9fae8245-bc85-3dba-9628-3735ae4f1d1b | -18.0802 | -46.3507 | 2026-05-06 00:56:00 | METOP-C | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 967f0f97-b05f-3fda-8e0f-abc3dd78cf8a | -18.082399 | -46.359798 | 2026-05-06 00:56:00 | METOP-C | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a4dcf2ab-9e71-3e22-89f3-588abccb90ba | -12.4913 | -58.4874 | 2026-05-06 00:56:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6b08e7f9-786e-38b7-b3f1-83b38d060132 | -12.3523 | -50.028999 | 2026-05-06 00:56:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9c29258a-e8ca-3376-9ab6-3c070b3e7c29 | -11.4412 | -55.094799 | 2026-05-06 00:56:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 90296d5d-fff4-306a-b3a3-759471039437 | -18.7794 | -51.941002 | 2026-05-06 00:56:00 | METOP-C | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e0fde358-03b4-393e-a13e-2d467ed9d97a | -12.349 | -50.0144 | 2026-05-06 00:56:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 938b4609-328b-3df7-9e8f-6cac811561e3 | -12.508 | -58.469101 | 2026-05-06 00:56:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5ab1532f-8cb5-3095-aa5e-f842e483771c | -8.6172 | -49.509602 | 2026-05-06 00:56:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc9025c8-ed11-384a-8068-8e4d35c6a648 | -21.9729 | -57.579899 | 2026-05-06 00:56:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 98584fb1-4ba2-3ef0-aae0-3b3d4c304cba | -20.2096 | -50.649799 | 2026-05-06 00:56:00 | METOP-C | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d9059a12-a926-316e-83b6-fb7434e94f27 | -12.4954 | -58.456799 | 2026-05-06 00:56:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 64f48f0b-e163-3b8c-9b4b-64afa0572217 | -20.2194 | -50.647499 | 2026-05-06 00:56:00 | METOP-C | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bc0b504c-0de5-39dd-a42a-630473e3e50b | -19.947599 | -54.381001 | 2026-05-06 00:56:00 | METOP-C | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 38ce1f10-eb0c-369b-ad0a-173cecae86c4 | -16.4259 | -54.9175 | 2026-05-06 00:56:00 | METOP-C | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3c60cfcf-1c0a-31a1-8d16-e46a6a94966f | -18.4319 | -54.7015 | 2026-05-06 00:56:00 | METOP-C | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 4c5cd17b-3701-3430-bbf6-b3e43878c1b2 | -21.975901 | -57.5975 | 2026-05-06 00:56:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f6949fde-938b-3419-a8b1-6984776917f2 | -16.414101 | -54.909801 | 2026-05-06 00:56:00 | METOP-C | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fb7ce8ef-9de4-3f2a-8c0b-9b2548d2b586 | -23.554199 | -47.4459 | 2026-05-06 00:56:00 | METOP-C | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c08507be-98bc-31dc-b92f-755946ad1e02 | -22.6075 | -49.557701 | 2026-05-06 00:56:00 | METOP-C | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1994234f-f98f-370d-9c3f-52196c201455 | -17.8062 | -46.7169 | 2026-05-06 00:56:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7954b6c7-1047-324a-a385-bf872e516c6a | -12.2755 | -43.494598 | 2026-05-06 00:56:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6f2d5ad2-dfc0-33ed-bd59-cdab06c1e3b8 | -17.8041 | -46.708099 | 2026-05-06 00:56:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2a6d687f-29c3-3b92-b8a4-6a2af2d6721c | -12.5051 | -58.4548 | 2026-05-06 00:56:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 97ee48a3-07cd-36bd-b4df-40e2902e18a2 | -12.4856 | -58.458801 | 2026-05-06 00:56:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b1345741-417e-38b8-9935-6293b33cca2b | -11.4314 | -55.096901 | 2026-05-06 00:56:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b8ad9a5-eaa9-3f93-bb49-bcfe0c07fffa | -20.2178 | -50.640099 | 2026-05-06 00:56:00 | METOP-C | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 27e71257-0371-3bb6-9cea-088693c06669 | -12.3506 | -50.021702 | 2026-05-06 00:56:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6be8faf5-181e-3939-a99d-6c4658b3521c | -11.6205 | -48.0592 | 2026-05-06 00:56:00 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c71fd623-dcbd-3659-b47a-2878e82e91fe | -10.9417 | -49.4254 | 2026-05-06 00:56:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 10bce791-8ba7-3401-bcaa-508cadea0cdb | -17.813801 | -46.705601 | 2026-05-06 00:56:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ce49a488-d4d1-3b42-bc14-0d1cbd7dbb10 | -13.693 | -55.681301 | 2026-05-06 00:56:00 | METOP-C | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0cb89e05-b30f-3a1f-8650-2e431c701e28 | -21.7097 | -48.424999 | 2026-05-06 00:56:00 | METOP-C | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3f94671f-401e-3822-9035-7ce036b4b77e | -12.46 | -54.442799 | 2026-05-06 00:56:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a1e4602e-187d-350b-9016-550493c92ff7 | -11.4431 | -55.103401 | 2026-05-06 00:56:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5b4a4529-5ebc-3ad4-af0d-e3e4b4152fc7 | -21.1912 | -49.200199 | 2026-05-06 00:56:00 | METOP-C | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8d35c702-a5bb-394b-b500-53d424909012 | -21.192801 | -49.2075 | 2026-05-06 00:56:00 | METOP-C | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 53c70b22-ebca-35f9-8d53-da57a73377df | -16.4219 | -54.8979 | 2026-05-06 00:56:00 | METOP-C | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7404f8b8-e1ea-34b0-a01b-de56594a1575 | -12.4982 | -58.4711 | 2026-05-06 00:56:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3dadd782-684f-3e46-a67c-aec7c511e7ce | -23.083 | -48.618198 | 2026-05-06 00:56:00 | METOP-C | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5ff48a36-95cc-3dfa-9c45-74b3c1cba5e0 | -23.081301 | -48.610699 | 2026-05-06 00:56:00 | METOP-C | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| dc6e356b-969b-365e-ad38-7a91a6e49a97 | -8.6191 | -49.517601 | 2026-05-06 00:56:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3f27354-6780-30f9-b794-f98e48b56389 | -14.0775 | -47.7836 | 2026-05-06 00:56:00 | METOP-C | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fc59dc55-8ff3-3896-b935-7fb8182d4eec | -11.6184 | -48.0504 | 2026-05-06 00:56:00 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 67cc1407-92d5-364a-8204-70bc05754ee6 | -11.6396 | -54.159401 | 2026-05-06 00:56:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b91d4bf1-ec38-30ac-accc-aef74999dcff | -18.497299 | -55.506802 | 2026-05-06 00:56:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5950abbe-5375-37e3-b88d-b7e4a9b276c0 | -11.5564 | -48.267101 | 2026-05-06 00:56:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 00edb6b7-44ec-3b6a-afdc-b9186d69cae9 | -11.4333 | -55.105499 | 2026-05-06 00:56:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 23d6ae2f-d631-318d-91b6-7378bb186e09 | -12.5033 | -58.4781 | 2026-05-06 01:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 00927b0c-0319-3128-bb19-b619743d5673 | -12.5035 | -58.4582 | 2026-05-06 01:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 9491599c-0012-39c6-a7ed-1873eee273c2 | -12.5033 | -58.4781 | 2026-05-06 01:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 138.7 |
| c758096e-9b46-35cd-997b-c00f7cc4743f | -20.2033 | -50.6412 | 2026-05-06 01:10:00 | GOES-19 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.0 |
| c4ada959-e61d-3b8c-8d6c-cd05ac7e2eda | -12.5035 | -58.4582 | 2026-05-06 01:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 36aef753-67cd-32d5-9a2a-c8f69d67bbcf | -12.5031 | -58.4979 | 2026-05-06 01:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 9802cd9b-600e-33b8-845a-8bdf313e8231 | -12.5033 | -58.4781 | 2026-05-06 01:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 8e5d90e2-947b-374a-ae12-f9d8a4ba0a04 | -20.2237 | -50.6371 | 2026-05-06 01:20:00 | GOES-19 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 54.7 |
| 2358e4c5-fd80-32ed-818d-4ae2fc5001ed | -12.5031 | -58.4979 | 2026-05-06 01:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 44.0 |
| fd1834a8-de4c-3bd9-9ee2-af042a54c47c | -12.5033 | -58.4781 | 2026-05-06 01:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 106.3 |
| d29431d7-9303-3fc2-89ea-56e13027277b | -20.2033 | -50.6412 | 2026-05-06 01:40:00 | GOES-19 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 57.2 |
| 1643aeb3-1a0c-3c2e-bf33-f368c1f857c8 | -12.5035 | -58.4582 | 2026-05-06 01:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 460046a5-2f5f-3dc2-a6a4-e26d57f646a4 | -12.5033 | -58.4781 | 2026-05-06 01:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 28a3ca76-0155-30fa-a775-49093766843a | -12.4843 | -58.4795 | 2026-05-06 01:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 39.9 |
| dece8340-249f-317d-ac58-ff15374972a7 | -12.5033 | -58.4781 | 2026-05-06 01:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 2b3d7c21-7e5b-3ef5-8940-844ceae139a6 | -12.5033 | -58.4781 | 2026-05-06 02:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |
| e93c0812-6ebc-399c-92d8-16e8d5b19a68 | -12.5033 | -58.4781 | 2026-05-06 02:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| ae489da8-cafe-3af4-a7e0-88c3ad4bf956 | -12.5033 | -58.4781 | 2026-05-06 02:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 673fd6d0-8bcd-3d2c-89b8-0aab5314d29a | -12.5033 | -58.4781 | 2026-05-06 02:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 154c9cc4-ea71-3bb4-b19e-aa60f8bfa91c | -12.5033 | -58.4781 | 2026-05-06 02:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| b2d217ae-959d-3bc3-92ed-f4e8f2b3478d | -12.5033 | -58.4781 | 2026-05-06 02:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 86.7 |
| efae25cb-32a9-341c-84e3-3cc6ecacd3bb | -12.5033 | -58.4781 | 2026-05-06 03:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 0af034f0-5fd3-38f0-a909-7d403dfbfd75 | -12.5033 | -58.4781 | 2026-05-06 03:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 94165685-f31e-3240-bc76-cff98a4e4650 | -22.17135 | -42.87674 | 2026-05-06 03:17:00 | NOAA-21 | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0761c3ce-0c57-3410-856e-39afe64292d4 | -12.5033 | -58.4781 | 2026-05-06 03:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 73.1 |
| db35cd0c-9a61-3ac8-b8b2-db695043f847 | -12.5033 | -58.4781 | 2026-05-06 03:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 5bfffb2e-6bf4-3e22-a736-914f80e72ae8 | -12.5033 | -58.4781 | 2026-05-06 03:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| c4cc2811-624d-34f6-8b2a-70ccc3b84ce5 | -5.78589 | -45.12469 | 2026-05-06 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f2a82d1-77aa-3912-9ed6-337c4977f940 | -8.22535 | -43.88098 | 2026-05-06 03:45:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4d8d2504-bb05-359f-ae8f-9e73bcc7caf8 | -8.22494 | -43.88036 | 2026-05-06 03:45:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d37594c4-37b3-36ae-af4e-7ed9aadb5828 | -8.23046 | -43.8814 | 2026-05-06 03:45:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a5e19a8-dade-377c-b3d0-72962acaa027 | -5.78499 | -45.12968 | 2026-05-06 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa227b03-f79a-35d8-a756-d6a5473a4f32 | -5.78679 | -45.11974 | 2026-05-06 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01b3f911-04e2-38a2-be94-b7ab737b7976 | -8.45598 | -36.36376 | 2026-05-06 03:45:00 | NPP-375D | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 4bd63a55-eef5-3777-80e9-85a45eb79992 | -13.22264 | -40.13523 | 2026-05-06 03:47:00 | NPP-375D | IRAJUBA | BAHIA | Brasil | 2914208 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0caf6b04-f517-3dd0-bb98-9ebd6c8a1440 | -14.14707 | -45.35799 | 2026-05-06 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c6c2a0d-011b-3a2b-97ec-7692089f6dd5 | -11.1246 | -45.11819 | 2026-05-06 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55c1bf90-c1b8-3cf1-add8-03cce042c9be | -13.65212 | -45.55689 | 2026-05-06 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3023cb6a-0fc9-3fee-a6ae-d496f70e35cc | -11.61884 | -48.05856 | 2026-05-06 03:47:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2dd3832-dad5-30e1-ba09-6c7f5536a679 | -14.13616 | -45.35571 | 2026-05-06 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56771325-ff37-3b24-be71-0871603f21cf | -12.26937 | -43.5116 | 2026-05-06 03:47:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c2e26b3f-fb4b-3bcf-b6fc-cbd00eb28dfa | -10.58717 | -44.32884 | 2026-05-06 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99cf38ab-180d-3069-a0ca-239eedd84e94 | -11.60653 | -48.05836 | 2026-05-06 03:47:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README4.md)
