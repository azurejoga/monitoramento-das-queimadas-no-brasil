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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d773e27-74e6-3b8f-ad4b-ffc899eddd07 | -16.62441 | -42.79487 | 2024-10-14 03:06:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c8d64fb5-3b9b-3f02-99eb-0ffcc5c138b8 | -10.2187 | -36.3162 | 2024-10-14 03:06:03 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 79.9 |
| c5a88ff8-0efd-30b3-8296-9a2bd5576d35 | -10.0163 | -47.3308 | 2024-10-14 03:06:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 99cf874e-c466-36f3-bf74-a499af0f05f6 | -10.0619 | -44.2624 | 2024-10-14 03:06:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 3d860f9e-758c-3c1e-ab36-e5837fe5299f | -10.0622 | -44.2391 | 2024-10-14 03:06:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 2fb0744d-0a42-34dd-9b51-2616d6dc6140 | -10.0809 | -44.2599 | 2024-10-14 03:06:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 152.3 |
| cdeec523-f465-3c3a-9a9d-4f7f6d0dfcb8 | -10.0813 | -44.2366 | 2024-10-14 03:06:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 188.6 |
| 6c48da7a-c517-33b2-982d-26143a5f199e | -10.0816 | -44.2133 | 2024-10-14 03:06:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 3e2a3330-db4b-3958-a723-f91370175076 | -10.2182 | -36.3433 | 2024-10-14 03:06:03 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 163.1 |
| 9714ffd4-d737-36ec-8551-aa3eb17536c6 | -10.4633 | -47.8545 | 2024-10-14 03:06:05 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 29af5603-6b77-3492-a8bf-eba079c739b2 | -10.4629 | -47.8766 | 2024-10-14 03:06:05 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 4508cf55-a57a-318f-982a-5e4b45e6db59 | -10.5307 | -49.7843 | 2024-10-14 03:06:06 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| c6b1612c-23ec-39d6-be34-d7851a2ad310 | -11.5597 | -50.7208 | 2024-10-14 03:06:12 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| d3018b09-57a9-361d-ba3e-b04770f0980c | -12.3997 | -53.1147 | 2024-10-14 03:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 163.6 |
| 093b0a8a-152d-3141-9ccf-cacb79b6654a | -12.3994 | -53.1355 | 2024-10-14 03:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 96.5 |
| b6b91401-6cf2-39bf-92e7-6f44c03d3659 | -12.3807 | -53.1167 | 2024-10-14 03:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 145.6 |
| d0db163c-48dc-31f2-8b9b-4f5e05f8bb87 | -12.3804 | -53.1376 | 2024-10-14 03:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 876c1986-d125-3cf6-adee-07bb230c89ea | -12.8893 | -53.5194 | 2024-10-14 03:06:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 114513d0-c338-3b28-958b-331588335f58 | -12.889 | -53.5402 | 2024-10-14 03:06:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 4a33875b-6377-3ffe-8129-ce2ea99be2ba | -12.8702 | -53.5215 | 2024-10-14 03:06:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 228ef5ac-a474-3c0b-ba5e-13f9a57d1f2a | -12.8699 | -53.5423 | 2024-10-14 03:06:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 92bbc662-2c84-388f-abf1-3d983b1719ad | -18.1909 | -56.8186 | 2024-10-14 03:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.9 |
| 08e1e990-8ece-3ba2-8189-1113cd2e8f73 | -18.1905 | -56.8394 | 2024-10-14 03:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.4 |
| a3f79ab6-890e-3912-aa5f-0a9cbe40f278 | -18.2104 | -56.8368 | 2024-10-14 03:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.8 |
| b19c9f1f-3b9f-3dca-8284-878b68fc3e44 | -18.2107 | -56.816 | 2024-10-14 03:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.2 |
| 6733ee95-0d59-327a-bfcd-cc2cc7dd082e | -2.4529 | -46.919 | 2024-10-14 03:15:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| c5fc2502-6f91-312e-8c24-bea3e51a838f | -2.6303 | -49.098 | 2024-10-14 03:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| d018860f-588f-3b77-a032-370afd55ecf4 | -2.6118 | -49.0985 | 2024-10-14 03:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 4cdd1def-70f0-3343-9891-6ce4796262ef | -3.3076 | -42.8553 | 2024-10-14 03:15:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| ca01ea85-abbc-3f56-a388-23a27ab9626a | -3.289 | -42.8327 | 2024-10-14 03:15:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 44a8ea71-f12b-3391-81f5-7a2be204feac | -3.2889 | -42.8561 | 2024-10-14 03:15:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 47174582-569b-30bd-8410-89b2511ade22 | -3.3077 | -42.8318 | 2024-10-14 03:15:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 26317fd2-180d-3563-80ff-6469e4040bea | -3.9103 | -48.3466 | 2024-10-14 03:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| ef2c7e09-416e-33c7-b941-80366535b51f | -7.9603 | -63.6359 | 2024-10-14 03:15:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| f4052d28-2cb1-31aa-ad30-a6254d502a84 | -8.0486 | -44.8178 | 2024-10-14 03:15:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 98b05ef3-d504-3776-a5df-4866ba8710b9 | -7.9418 | -63.6365 | 2024-10-14 03:15:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 41ae1699-7cd3-34cc-890b-51e1d78be398 | -9.1043 | -61.162 | 2024-10-14 03:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| d78e0d3c-e58e-397b-8209-6601b723435c | -9.3264 | -52.8444 | 2024-10-14 03:15:59 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 7c263b53-3b0d-3aba-ae39-d31121625888 | -9.3451 | -52.8428 | 2024-10-14 03:16:00 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| c08ac946-7b59-3db0-9a46-4195d1382db1 | -10.0816 | -44.2133 | 2024-10-14 03:16:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 26a1e5aa-88b7-3098-9c07-05a2370512f6 | -10.0813 | -44.2366 | 2024-10-14 03:16:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 186.3 |
| 6770c4d5-3aca-3fb9-9a75-dd83f55f5c22 | -10.0809 | -44.2599 | 2024-10-14 03:16:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 170.4 |
| e557b7b4-c3ee-3d88-9a33-c018126bce34 | -10.0622 | -44.2391 | 2024-10-14 03:16:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 155.3 |
| ce2d7af8-6710-34e3-8c8b-467c08571f02 | -10.0619 | -44.2624 | 2024-10-14 03:16:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 198.3 |
| 0bacad1d-9c52-3494-af53-1eef7bdd17b0 | -10.0163 | -47.3308 | 2024-10-14 03:16:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 8d3c26cb-dc9a-3f1f-8ce7-84b1a3c28c8f | -10.4918 | -42.433 | 2024-10-14 03:16:05 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 75.5 |
| 43baf32c-eefa-337e-b57d-c10bc7e0d1b8 | -10.5307 | -49.7843 | 2024-10-14 03:16:06 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 27da0146-6959-37f7-80c1-570c69f69da6 | -10.9116 | -44.7048 | 2024-10-14 03:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 74001030-ddb1-3ad7-853a-608e0c11766b | -12.3807 | -53.1167 | 2024-10-14 03:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 191.9 |
| 3c620888-b87e-3979-aba2-b87c753f0a67 | -12.3994 | -53.1355 | 2024-10-14 03:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 30bfa12d-638c-3532-bd4b-5234cf7ef05c | -12.3997 | -53.1147 | 2024-10-14 03:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 182.7 |
| a6514e24-5c5b-3a06-a675-3725d2b7e9dc | -12.3804 | -53.1376 | 2024-10-14 03:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 3c540636-1ce9-3eb9-a20e-c85eb3d529f4 | -12.8699 | -53.5423 | 2024-10-14 03:16:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 38981d38-0695-3e0e-9f3e-850231d4abdb | -12.8702 | -53.5215 | 2024-10-14 03:16:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 2cda359c-0d82-3279-8aa9-99cd03f719cd | -12.889 | -53.5402 | 2024-10-14 03:16:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| ee85085d-26b4-3083-9744-f681385c0d83 | -12.8893 | -53.5194 | 2024-10-14 03:16:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 37e93328-12c8-36ed-a1fb-92c6b364ec8f | -18.1909 | -56.8186 | 2024-10-14 03:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.3 |
| 506ca937-edfa-39de-971a-c43743f67892 | -18.1905 | -56.8394 | 2024-10-14 03:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.8 |
| 2352df7d-efd4-37c7-bf4a-31a6f6e49184 | -18.2107 | -56.816 | 2024-10-14 03:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.9 |
| 7f8f99bb-04ba-31f8-8ae2-bd2dd653ebb6 | -18.2104 | -56.8368 | 2024-10-14 03:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.1 |
| 203eb243-effb-34e3-b086-faceb04e63e1 | -3.01417 | -41.16821 | 2024-10-14 03:25:00 | NOAA-20 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 453bbc9c-4519-3b35-b502-d61c5fa5cc76 | -3.01351 | -41.17207 | 2024-10-14 03:25:00 | NOAA-20 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c04ca790-0b06-37e1-8417-ac86898949ee | -3.01061 | -41.16961 | 2024-10-14 03:25:00 | NOAA-20 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b505000c-385d-35eb-88a3-31136fda4ce9 | -3.00854 | -41.16726 | 2024-10-14 03:25:00 | NOAA-20 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2ea296ba-c331-337d-8eaa-78d8d8385b58 | -3.00789 | -41.17107 | 2024-10-14 03:25:00 | NOAA-20 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8b62b7a7-6423-3c80-a29f-a8681199e7e1 | -2.4344 | -46.9195 | 2024-10-14 03:25:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| f2be2b1e-411e-399f-bf36-0773efbe22fc | -2.4529 | -46.919 | 2024-10-14 03:25:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 5f6d064f-09e8-3e5c-bfa8-8f21c6da7a2f | -2.6118 | -49.0985 | 2024-10-14 03:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 80d98d8a-b6df-3977-9224-c5752feeaeb0 | -2.6119 | -49.0772 | 2024-10-14 03:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 940169db-48ab-31f0-a567-a8321b40f886 | -3.2889 | -42.8561 | 2024-10-14 03:25:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 23f4388f-8e83-3486-8386-bef565c51beb | -3.289 | -42.8327 | 2024-10-14 03:25:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 79febabb-5de8-3625-bb92-d342b028be83 | -3.3076 | -42.8553 | 2024-10-14 03:25:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| f9a274aa-ae04-3e6b-914e-f9f5d3370df7 | -3.3077 | -42.8318 | 2024-10-14 03:25:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 153.3 |
| 0614b6f1-0ce9-3c1d-9f7f-986f822cfe87 | -3.8382 | -55.9972 | 2024-10-14 03:25:28 | GOES-16 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 0e841bcf-4d56-39a5-ad67-4ae72172c7ce | -3.8383 | -55.9774 | 2024-10-14 03:25:28 | GOES-16 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| fc78226b-9417-3182-8c57-f89f612b7958 | -4.1149 | -48.2299 | 2024-10-14 03:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 6fa3f1a4-bf69-3d62-b191-049c069be208 | -4.3718 | -37.9175 | 2024-10-14 03:25:31 | GOES-16 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 64.4 |
| 0662439f-29fb-30a5-92fd-b9ab7f2129a5 | -7.9418 | -63.6365 | 2024-10-14 03:25:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 9e7ba992-48dc-3095-9400-ec381c9dcd62 | -7.9419 | -63.6177 | 2024-10-14 03:25:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 2e217e5d-3502-352b-ac38-11177d531724 | -9.1043 | -61.162 | 2024-10-14 03:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 8403cccb-29a7-3102-bbce-833de62f080d | -9.3264 | -52.8444 | 2024-10-14 03:25:59 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 4138a1ab-f8c3-3d13-a547-c1cde7de92cd | -9.3451 | -52.8428 | 2024-10-14 03:26:00 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 794c5075-5525-375a-9c25-27298d66db50 | -9.4699 | -45.8249 | 2024-10-14 03:26:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| b486ae50-ed70-331f-940b-a5febc63c3f3 | -9.4885 | -45.8454 | 2024-10-14 03:26:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 31bb69df-1204-3951-957e-2007031fc78c | -9.4888 | -45.8228 | 2024-10-14 03:26:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 418.4 |
| 27a6ff05-81a8-36b3-b54e-b77b813e7453 | -9.4892 | -45.8001 | 2024-10-14 03:26:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 9e616440-6e08-3c4c-8f9e-237b72c64081 | -9.5078 | -45.8206 | 2024-10-14 03:26:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 4cbd5843-eb41-3175-a9d8-14878c10ca78 | -10.0619 | -44.2624 | 2024-10-14 03:26:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 190.0 |
| a8be4095-41e0-3f1f-825e-7a08168ceca6 | -10.0622 | -44.2391 | 2024-10-14 03:26:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 293e427d-5fac-3b96-97d6-01702b68e90d | -10.0809 | -44.2599 | 2024-10-14 03:26:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 5317deb5-3591-3f88-a50a-9e436efd2d2d | -10.0813 | -44.2366 | 2024-10-14 03:26:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 56df1151-f0b3-3c90-a081-30347f5d9b19 | -10.0816 | -44.2133 | 2024-10-14 03:26:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 94.9 |
| b54f26a6-ee3f-3d7a-a57a-0fb4d485d5be | -10.0163 | -47.3308 | 2024-10-14 03:26:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 55d5f6bc-85de-3ee2-bcc8-2ae68f80b9a1 | -10.5307 | -49.7843 | 2024-10-14 03:26:06 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| f8957d2d-2c71-39e7-80f1-e9e68531b724 | -12.3804 | -53.1376 | 2024-10-14 03:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 94c57f9e-4dc7-36dd-a6c0-27b42d5c3163 | -12.3807 | -53.1167 | 2024-10-14 03:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 189.3 |
| 048e861a-1caa-3038-9d03-31def846bce9 | -12.3994 | -53.1355 | 2024-10-14 03:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 49598b24-99f8-3c53-8a4a-ba0c929976ef | -12.3997 | -53.1147 | 2024-10-14 03:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 135.4 |
| 138ab0ed-e411-312f-a50a-b0ef40a0dfa2 | -12.8699 | -53.5423 | 2024-10-14 03:26:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 1b051999-2c01-346d-947c-18801ab22808 | -12.889 | -53.5402 | 2024-10-14 03:26:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |


[Clique aqui para ver as próximas entradas](README30.md)
