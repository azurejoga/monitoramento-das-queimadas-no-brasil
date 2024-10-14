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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc67f73e-fb3d-3b39-9a99-a0c6ad002baa | -30.0073 | -51.04303 | 2024-10-14 04:27:00 | NOAA-21 | ALVORADA | RIO GRANDE DO SUL | Brasil | 4300604 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| c0509192-ee93-3c8f-bf09-d07712900894 | -29.81547 | -51.17736 | 2024-10-14 04:27:00 | NOAA-21 | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| 317c807d-547a-3126-83d5-6cab72129fd2 | -29.64912 | -51.6623 | 2024-10-14 04:27:00 | NOAA-21 | TRIUNFO | RIO GRANDE DO SUL | Brasil | 4322004 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 051d20a6-a2b9-3ab7-b96e-74fc2602ccf0 | -31.58397 | -53.72963 | 2024-10-14 04:27:00 | NOAA-21 | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 5fb749c4-33f9-3744-bdf6-d045fd378f13 | -29.44583 | -56.35455 | 2024-10-14 04:27:00 | NOAA-21 | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| c105201c-0d90-342e-ab6a-3de072236ef9 | -2.4529 | -46.919 | 2024-10-14 04:35:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| ee67a442-9e7b-344b-a48d-eada38ab1fdb | -2.4344 | -46.9195 | 2024-10-14 04:35:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 24a294bc-05a9-3372-91c8-8d4f7e85caac | -2.6119 | -49.0772 | 2024-10-14 04:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 74fd3dea-8a37-3416-8498-2b92d68d466a | -2.6118 | -49.0985 | 2024-10-14 04:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 955d53e0-aacd-3fd2-ae36-ef2c41ae4cec | -3.3078 | -42.8084 | 2024-10-14 04:35:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 4244e12b-4c35-37ab-98dd-6ad29b1e3ccf | -3.3077 | -42.8318 | 2024-10-14 04:35:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 226.5 |
| 231fb85d-e79b-35e7-8740-bc48197e4fd4 | -3.3076 | -42.8553 | 2024-10-14 04:35:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| b4b9575f-bef2-34e1-9fd4-e339add01d9b | -3.289 | -42.8327 | 2024-10-14 04:35:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| c39103bd-bb9c-3a99-88c8-811a169e92b4 | -3.2889 | -42.8561 | 2024-10-14 04:35:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 46.3 |
| afe4530b-0a1d-3e17-86dd-65040a7ae2f2 | -3.7391 | -45.7195 | 2024-10-14 04:35:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 330.9 |
| c164c35a-8b54-328d-ae2b-13f997dc6e77 | -3.7205 | -45.7203 | 2024-10-14 04:35:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 160.9 |
| b6442c8d-f81c-32e0-96aa-f61ad5ed99cb | -3.7389 | -45.7419 | 2024-10-14 04:35:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 225.6 |
| fb05a310-9c54-38f4-b625-5791e7ce6152 | -3.7203 | -45.7427 | 2024-10-14 04:35:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 3508ae6c-da90-38a5-bef0-c3463e4c52a8 | -3.8383 | -55.9774 | 2024-10-14 04:35:28 | GOES-16 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| a0a44ab2-3d36-3eca-956a-81b41fe8f7cc | -3.9103 | -48.3466 | 2024-10-14 04:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| f3ec6793-460c-32ab-b458-da572d12724d | -4.1149 | -48.2299 | 2024-10-14 04:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 4c172377-a312-3d7f-9b28-bb46e000c930 | -7.9418 | -63.6365 | 2024-10-14 04:35:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| be2048fd-390d-33aa-b5e9-f5230ca9cbba | -7.9419 | -63.6177 | 2024-10-14 04:35:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| fa766da1-9055-32d3-b032-f537eaba8030 | -8.14235 | -42.32462 | 2024-10-14 04:36:00 | AQUA_M-M | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 53cc58c2-04f7-34a5-ba94-b28cc963f46b | -5.1291 | -41.70429 | 2024-10-14 04:36:00 | AQUA_M-M | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 21.2 |
| 3d573ee5-c63c-3db0-82bf-21cec2fc8077 | -5.125 | -41.7111 | 2024-10-14 04:36:00 | AQUA_M-M | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 25.3 |
| 013179a8-4992-3198-bc62-54f5a17b681e | -4.37776 | -37.89408 | 2024-10-14 04:36:00 | AQUA_M-M | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| ecd02340-8e83-39f7-a6ac-2c30a888706c | -4.37603 | -37.90522 | 2024-10-14 04:36:00 | AQUA_M-M | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 704d30e2-7a12-39fa-a076-11cf7df69f79 | -3.31825 | -42.82004 | 2024-10-14 04:36:00 | AQUA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 031423c9-e6b4-33ed-bb1a-4d550823c486 | -3.31569 | -42.84002 | 2024-10-14 04:36:00 | AQUA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| feab84b6-2be4-3a55-9a84-2bca14ec96c6 | -3.31383 | -42.84743 | 2024-10-14 04:36:00 | AQUA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| e8206b78-4efc-3370-840c-70d48bcbf501 | -3.30515 | -42.81021 | 2024-10-14 04:36:00 | AQUA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 72767950-2445-3592-8f5c-58aad59e8d1c | -3.30347 | -42.81774 | 2024-10-14 04:36:00 | AQUA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 756c28c3-5255-3220-bd16-af64efefbf99 | -3.30089 | -42.83762 | 2024-10-14 04:36:00 | AQUA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 369.2 |
| dccc6ea1-27f8-3e7a-8b73-7b2000850669 | -3.29902 | -42.84508 | 2024-10-14 04:36:00 | AQUA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 263.1 |
| cd16c1b4-4764-3124-b559-2f3043f7d5dd | -2.83005 | -40.35719 | 2024-10-14 04:36:00 | AQUA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 644a5af5-c68e-3507-8ca4-148598a2a6d1 | -10.0813 | -44.2366 | 2024-10-14 04:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 8672bc53-1dfc-3692-ab72-2e455045ee55 | -10.0809 | -44.2599 | 2024-10-14 04:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 2f8a2cce-f274-3f13-b22f-dfe900675a49 | -10.0622 | -44.2391 | 2024-10-14 04:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 148.8 |
| eff4271b-eaa6-3642-850c-fdba9d3c4755 | -10.0619 | -44.2624 | 2024-10-14 04:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 181.1 |
| 52de24c5-08ec-3a2b-a132-4b30f45ae958 | -10.8552 | -52.3971 | 2024-10-14 04:36:08 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| e6f9e79d-ab16-331e-9237-5f627b64612e | -10.8554 | -52.3762 | 2024-10-14 04:36:08 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| c458ff3c-e630-3dab-862e-d0d47b49526f | -17.0004 | -57.4176 | 2024-10-14 04:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.0 |
| fc93cc34-dfbd-3dcc-8672-6eb35f51a6a3 | -17.02 | -57.4153 | 2024-10-14 04:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.8 |
| ccae28fe-8e1c-3e81-9aa0-37e5840b59ca | -17.1957 | -57.4562 | 2024-10-14 04:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.3 |
| 3325b954-bcdf-3a30-905f-294ab6d6b5de | -17.196 | -57.4357 | 2024-10-14 04:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.2 |
| 5405f4ea-d801-3b66-90fb-cf93c8aab4b5 | -17.6474 | -56.2876 | 2024-10-14 04:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.3 |
| c0e588b3-74b5-38ba-866e-559a00a00964 | -18.1909 | -56.8186 | 2024-10-14 04:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.6 |
| 8a743aab-b481-3515-885d-78d6c76493a8 | -18.1905 | -56.8394 | 2024-10-14 04:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.8 |
| 29c1d3aa-9d7b-390e-8d44-22745ba9871d | -18.2346 | -56.5847 | 2024-10-14 04:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.1 |
| d5bc087e-6afa-3df1-8e28-7b407cae35af | -18.2342 | -56.6055 | 2024-10-14 04:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 144.9 |
| 8cd3cf7c-c681-3962-9a4a-46f281593563 | -18.2147 | -56.5873 | 2024-10-14 04:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.5 |
| 35469fd2-fc55-36c8-9415-e64a01483b62 | -18.2144 | -56.6081 | 2024-10-14 04:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 125.8 |
| 1feee682-a310-3644-8b1f-b4cb08cea822 | -10.06946 | -44.25287 | 2024-10-14 04:38:00 | AQUA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 300.3 |
| 1e9de74b-d363-39cc-ba1e-6cc75d725dba | -10.43987 | -44.94137 | 2024-10-14 04:38:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 35.0 |
| fb759239-dfa7-3fd8-ab70-383195cabf43 | -11.11678 | -43.33337 | 2024-10-14 04:38:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 25.3 |
| e528143f-3cad-3a69-9cb3-6f9e58d531a7 | -11.1148 | -43.31808 | 2024-10-14 04:38:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 21.2 |
| f92531bb-54a1-3eea-b373-4104b2d6c716 | -11.11096 | -43.33959 | 2024-10-14 04:38:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 36.2 |
| 1ded2977-4e8e-304e-b6d8-2365961756e5 | -11.10351 | -43.33096 | 2024-10-14 04:38:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 27.6 |
| c0fec677-8cc5-389b-8668-6543a36663ee | -10.91279 | -44.69276 | 2024-10-14 04:38:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 1e88edfa-737e-3d35-9021-7eda3c8e3b0f | -10.08804 | -44.23618 | 2024-10-14 04:38:00 | AQUA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 28.3 |
| da9ee013-3ad9-3d21-b0c9-795b1b7e530a | -10.07352 | -44.23348 | 2024-10-14 04:38:00 | AQUA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 110.7 |
| ea4c1d67-5ff0-322d-8f0d-e0a5318392a5 | -10.91053 | -44.69975 | 2024-10-14 04:38:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 3469cce2-833e-36ad-8d83-6f403685b73c | -10.49172 | -42.4404 | 2024-10-14 04:38:00 | AQUA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 59.1 |
| c9c147f3-79fe-383f-93d2-34161cffe5ff | -10.06486 | -44.27998 | 2024-10-14 04:38:00 | AQUA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 23.9 |
| d177fa7d-6591-3726-93b3-6d4f7066eb5a | -10.07403 | -44.22583 | 2024-10-14 04:38:00 | AQUA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 608cf6ee-d451-37a2-abc2-83e50d68dcb9 | -10.07829 | -44.20654 | 2024-10-14 04:38:00 | AQUA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 27.5 |
| cb4b5408-25e3-3854-a873-753dfcad9584 | -10.06876 | -44.26042 | 2024-10-14 04:38:00 | AQUA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 242.5 |
| f05345a4-0a63-3f95-8f8e-e32bbdf87c75 | -21.56171 | -48.00711 | 2024-10-14 04:42:00 | AQUA_M-M | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 71a3cbc8-27e3-33cb-b22a-441a64ddfb78 | 1.13183 | -59.52832 | 2024-10-14 04:42:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 697b8173-ae71-324e-9814-ea426076cebf | 1.03696 | -59.45126 | 2024-10-14 04:42:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a84b4dd-37f9-33d7-a125-f73efeda88b0 | 1.03119 | -59.4522 | 2024-10-14 04:42:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa1f2c6f-beb0-3e8b-9cba-2067ae12ce4f | -1.2918 | -46.32468 | 2024-10-14 04:42:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34897138-0b6f-3670-9eb7-d3c814bbc5b2 | -3.01264 | -41.16693 | 2024-10-14 04:42:00 | NPP-375D | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| aebc7b36-d8c8-37c6-86be-7ff8846b536c | -2.82162 | -40.35282 | 2024-10-14 04:42:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| ad0d324c-da97-39e0-a6a2-01ccf7f06e45 | -2.82106 | -40.35652 | 2024-10-14 04:42:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 16d01426-12db-3a94-a9f6-8cfb3585f9e9 | -2.37966 | -45.74237 | 2024-10-14 04:42:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac4af7e0-df44-3b4c-a5c8-8c74996f7782 | -2.40476 | -44.78434 | 2024-10-14 04:42:00 | NPP-375D | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9d49768-2422-3cd4-a02e-1e936d7cf708 | -2.393 | -44.77883 | 2024-10-14 04:42:00 | NPP-375D | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 741cd04f-662d-3772-b62d-a228e168f009 | -1.98303 | -46.60421 | 2024-10-14 04:42:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fabab112-28c3-3f43-8b73-7ced1f182190 | -1.82353 | -47.08462 | 2024-10-14 04:42:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3966b723-fb60-310a-b457-e9d0ec4c8972 | -1.28912 | -46.32633 | 2024-10-14 04:42:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37ceb093-3031-3420-b822-2e79117c8796 | -1.28812 | -46.32412 | 2024-10-14 04:42:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| acbbd3c1-bbdb-34bc-8a37-a02c61629336 | -2.25139 | -46.74895 | 2024-10-14 04:42:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ac505b6-70a4-3bcd-a131-19de26c1afe7 | -2.25074 | -46.75312 | 2024-10-14 04:42:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 809738ae-6254-3424-aaa4-cf9da1e92f9d | -2.24971 | -46.73581 | 2024-10-14 04:42:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e97433a1-db60-35b6-b109-5a8c2cf90794 | -2.24905 | -46.74002 | 2024-10-14 04:42:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3062f1f-ccc4-3264-8794-6275687689de | -2.2484 | -46.74421 | 2024-10-14 04:42:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7749526a-3c9b-3a71-8dd7-cbbe769645e1 | -2.24775 | -46.74838 | 2024-10-14 04:42:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c5a2bd9-cd9d-3147-8dcb-f69ff183c23f | -2.24581 | -46.76095 | 2024-10-14 04:42:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d9bbf5e-157a-3eec-9f9a-e2edb080f3d8 | -2.24542 | -46.73946 | 2024-10-14 04:42:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 28fb7685-befb-3409-a6bc-bfabe5658410 | -2.24477 | -46.74364 | 2024-10-14 04:42:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 177dd37d-b849-343f-9631-592197837fbd | -2.2 | -46.45508 | 2024-10-14 04:42:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8be84c9-3bcc-30c5-8ec4-91ee3278522f | -2.19631 | -46.45451 | 2024-10-14 04:42:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a0115e8-772b-3d34-ac8f-28896ae60f16 | -2.18625 | -46.56737 | 2024-10-14 04:42:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef33dbc2-aa35-3444-9caa-8db28c5016fb | -1.54993 | -47.71018 | 2024-10-14 04:42:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76b77258-66ff-3873-8a4b-9356fb3e7ca7 | -0.7827 | -48.68153 | 2024-10-14 04:42:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ae6e662-2bb5-3a87-bed5-dc03032378a2 | -0.78045 | -48.674 | 2024-10-14 04:42:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53312a79-5446-3958-9fe1-69708117f0a0 | -1.47615 | -49.32388 | 2024-10-14 04:42:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d78acbde-1d96-3e26-8269-8a6fef77b62d | 0.95247 | -50.20706 | 2024-10-14 04:42:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README69.md)
