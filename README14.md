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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f0e97ee-274f-3015-ad72-edc766ecc2c0 | -8.55427 | -63.11444 | 2025-11-21 05:57:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c84b8ab7-10eb-3ddc-9b48-3341af9d855d | -10.25227 | -67.14845 | 2025-11-21 05:57:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 990f0365-5559-30e3-88d1-99f58ef9c684 | -9.63528 | -67.481 | 2025-11-21 05:57:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 190102c9-a487-3d51-8a8f-c91e9f92498b | -10.8344 | -56.95789 | 2025-11-21 05:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b8dcf84f-20aa-3438-b60f-a0bcf2f5772d | -9.69175 | -64.23208 | 2025-11-21 05:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1eee6d69-947b-34a7-ba5b-c70d7ce5491a | -9.57236 | -65.17452 | 2025-11-21 05:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d415ecf-1790-35db-a7e8-d0ea32daa45a | -9.99606 | -65.18691 | 2025-11-21 05:57:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4776660d-ddb7-3286-a883-6409a5fe0b7b | -9.63472 | -67.48469 | 2025-11-21 05:57:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0a4b035-604f-3a14-a575-c2c53e38477d | -10.27473 | -67.09274 | 2025-11-21 05:57:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95c48b53-be22-3f5b-a381-339b0fd55d6b | -10.84102 | -56.95864 | 2025-11-21 05:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3dafb2f5-3773-3e42-b7d6-10bdea429951 | -10.05905 | -67.57199 | 2025-11-21 05:57:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f51456a5-5cc1-3aca-81d5-242534e5fa47 | -9.69295 | -65.71696 | 2025-11-21 05:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 093ad111-a2e6-35fd-994f-c4d1656c2c38 | -9.59347 | -66.59441 | 2025-11-21 05:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a790fba8-3ba6-3025-854c-f45325b8dca8 | -10.84034 | -56.96431 | 2025-11-21 05:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b0206ee5-152a-38d3-b43d-890c096d4853 | -10.84764 | -56.95937 | 2025-11-21 05:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| cae0c389-bb44-3ef2-9c52-b1ab2155f883 | -9.7339 | -63.64558 | 2025-11-21 05:57:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45de6d2c-44de-32cf-be17-8ef91192d616 | -10.83928 | -56.95667 | 2025-11-21 06:54:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 8e261b33-eae8-3f7b-805f-2158f145f561 | -10.84093 | -56.94488 | 2025-11-21 06:54:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| c5e05c5e-95a3-3364-a4df-e22558a83298 | -4.0385 | -42.4657 | 2025-11-21 11:40:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 102.8 |
| 72f208bf-a7a1-3495-ad51-3beaad47753e | -20.8921 | -52.3522 | 2025-11-21 11:40:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 1a9785a5-d7c9-33ab-98ca-fa63eeb535dc | 3.62387 | -51.28841 | 2025-11-21 12:33:00 | TERRA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 15.5 |
| e33270be-b304-3fed-8859-8bd9d915f7b4 | 3.259 | -51.19429 | 2025-11-21 12:33:00 | TERRA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 860fd108-1529-3a97-ab3a-d955b60acef6 | -2.84824 | -46.82901 | 2025-11-21 12:36:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 47b42ecd-a30c-3ebd-8efc-8aa4b851e603 | -1.26599 | -46.899 | 2025-11-21 12:36:00 | TERRA_M-T | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 9731fbec-3b80-39a0-a668-22525ebc49a5 | 0.33264 | -50.99991 | 2025-11-21 12:36:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 3cab338c-cd71-3db0-b0e2-e02e7ad64c1c | -3.63727 | -42.5603 | 2025-11-21 12:36:00 | TERRA_M-T | MADEIRO | PIAUÍ | Brasil | 2205854 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 3bda8ede-3909-3233-9481-bf1199f12231 | -0.25853 | -48.56191 | 2025-11-21 12:36:00 | TERRA_M-T | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 318e49fa-9c0b-3be3-9d48-e16ec2b4046a | -3.4906 | -42.05238 | 2025-11-21 12:36:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 101.0 |
| e7849817-4147-3647-82f1-bb19026cf59b | -1.26817 | -46.89287 | 2025-11-21 12:36:00 | TERRA_M-T | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| d907b06a-51a9-3d4a-93a1-aca2efdb49c4 | -3.4319 | -42.25278 | 2025-11-21 12:36:00 | TERRA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| e28b53e9-975e-3f80-b384-34923e81fa6a | -1.26809 | -46.88364 | 2025-11-21 12:36:00 | TERRA_M-T | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| e60ffe58-e7dc-30f9-b7c9-44232f32c93b | -3.48502 | -42.09333 | 2025-11-21 12:36:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 42.7 |
| 1d36f926-6c88-31d1-8df3-f61b32742f93 | -1.9309 | -47.07929 | 2025-11-21 12:36:00 | TERRA_M-T | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| fe84bb67-e26f-30d8-8410-6e6b0b311368 | -2.85094 | -46.84048 | 2025-11-21 12:36:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| c0d02fd0-6957-3cff-b9f6-bd80a1c430b0 | -3.68096 | -42.13548 | 2025-11-21 12:36:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 84.1 |
| b7bcad56-adca-3307-9949-dfc662021488 | -3.34359 | -45.01198 | 2025-11-21 12:36:00 | TERRA_M-T | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 19.0 |
| ebfdbe19-faa9-3a81-bed7-e07fcc47f017 | -2.8407 | -45.61602 | 2025-11-21 12:36:00 | TERRA_M-T | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 66.0 |
| b04217a1-36c2-34d7-a73c-8f68ba33a81c | -2.84282 | -45.61062 | 2025-11-21 12:36:00 | TERRA_M-T | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 667d65e1-4b02-31f4-97df-e109883cf117 | -2.85331 | -46.82389 | 2025-11-21 12:36:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| b7de2d92-c4cc-3914-9b19-26b9c3e0621e | -3.67911 | -42.13035 | 2025-11-21 12:36:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 167.5 |
| 21aefc78-57d1-34c3-a486-fe3bcf1db00f | -3.49205 | -42.05769 | 2025-11-21 12:36:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 102.6 |
| 0514fbb7-4ca6-312a-b62e-ba8b7fb286c9 | -1.00343 | -47.29463 | 2025-11-21 12:36:00 | TERRA_M-T | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| aa2bae61-a26b-340e-a405-83ea53a8f1cd | -3.62513 | -42.56378 | 2025-11-21 12:36:00 | TERRA_M-T | MADEIRO | PIAUÍ | Brasil | 2205854 | 22 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 4b54022a-de61-3731-a65f-96a677e08f0e | -3.69645 | -42.13283 | 2025-11-21 12:36:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 46.5 |
| 0d44913d-e088-339f-a353-5cb0887a91ba | -4.14757 | -43.67975 | 2025-11-21 12:38:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 43.5 |
| f437cff8-14ac-37cf-9945-34b2cbff45b0 | -4.16317 | -43.68169 | 2025-11-21 12:38:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 11a5ff60-e818-3e94-a088-60a87b78afc0 | -12.55604 | -54.5867 | 2025-11-21 12:40:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cd0a2d43-1b50-35a3-a8bf-54c42b526012 | -13.04886 | -53.7191 | 2025-11-21 12:40:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 46955b15-17e2-34db-83a9-c6a1c2fb1228 | -19.72688 | -54.86177 | 2025-11-21 12:40:00 | TERRA_M-T | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 40f5a83d-61b9-39e4-a294-3647cf6056bd | -18.75262 | -53.96958 | 2025-11-21 12:40:00 | TERRA_M-T | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 72b79644-99f3-37c2-a23e-c5400aac623f | -17.6261 | -54.19806 | 2025-11-21 12:40:00 | TERRA_M-T | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f2a6abb5-adc4-3361-bef6-5622f362fb10 | -17.04368 | -52.27975 | 2025-11-21 12:40:00 | TERRA_M-T | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e78cbef9-a4d8-30a9-9e37-6bd353ce862b | -13.02051 | -50.71458 | 2025-11-21 12:40:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 5ca0576a-bd1f-398f-ad7a-fe92dbbf7647 | -18.85337 | -53.62011 | 2025-11-21 12:40:00 | TERRA_M-T | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 40386b23-e2b4-3a17-9537-e2222795d9d9 | -15.91785 | -54.29556 | 2025-11-21 12:40:00 | TERRA_M-T | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 44c9421b-9a6d-3e1e-b053-a9617333b8b2 | -18.63511 | -51.77466 | 2025-11-21 12:40:00 | TERRA_M-T | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 90b3ec4f-5b89-3c4b-bad3-1cdbfd608121 | -18.21891 | -54.37616 | 2025-11-21 12:40:00 | TERRA_M-T | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 9e0777b9-555a-3c44-a1be-2d9c3cdf4f41 | -16.77575 | -52.37347 | 2025-11-21 12:40:00 | TERRA_M-T | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3049fc57-7dc4-38ee-acff-01e218430c22 | -18.76175 | -53.97087 | 2025-11-21 12:40:00 | TERRA_M-T | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d625a91f-b8df-3034-917f-c1de81ac1d29 | -17.61974 | -54.1777 | 2025-11-21 12:40:00 | TERRA_M-T | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 2ac088b7-a8b7-3085-ad77-a4f8f5d76349 | -20.14071 | -52.46095 | 2025-11-21 12:40:00 | TERRA_M-T | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 8f86c008-8446-3b99-a649-909fdb98229d | -12.37215 | -54.51982 | 2025-11-21 12:40:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e8c128bc-046b-3502-9eb8-1553b02f4729 | -12.7288 | -54.60616 | 2025-11-21 12:40:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e5bdd380-7995-3f36-9b5b-366283960974 | -18.63357 | -51.78746 | 2025-11-21 12:40:00 | TERRA_M-T | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 3770c927-dc47-3543-8cb7-163284effc94 | -18.10723 | -54.51847 | 2025-11-21 12:40:00 | TERRA_M-T | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d7d6c420-594a-37df-aa2d-9e34188e0538 | -16.99392 | -51.46828 | 2025-11-21 12:40:00 | TERRA_M-T | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 77868be2-8d3c-3242-ba79-668b0c683c0b | -19.62203 | -55.54789 | 2025-11-21 12:40:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 3d827c4b-db4e-3a3c-9054-d996c905b43a | -12.37345 | -54.51086 | 2025-11-21 12:40:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3ba3dc29-a2d2-37f5-bff8-30235eabb6e1 | -20.13919 | -52.4733 | 2025-11-21 12:40:00 | TERRA_M-T | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 93df0724-837c-3a24-b4f8-064633bdbe90 | -13.29932 | -53.50615 | 2025-11-21 12:40:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| df7978a5-c125-3485-8f0e-03e235b486fc | -17.61843 | -54.18723 | 2025-11-21 12:40:00 | TERRA_M-T | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 14.1 |
| e8ecb037-80fa-3afc-b532-a3dd745c0445 | -19.60048 | -54.50618 | 2025-11-21 12:40:00 | TERRA_M-T | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 21.1 |
| ec6a5ec3-7ae5-37d3-937a-b5c1530ed6de | -15.6682 | -54.36229 | 2025-11-21 12:40:00 | TERRA_M-T | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8a223197-39cb-36bf-be23-23f25aae107f | -18.86357 | -48.26963 | 2025-11-21 12:40:00 | TERRA_M-T | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 4cb6da7a-d3c4-3bc3-9918-cab503e7fe8c | -19.62071 | -55.55721 | 2025-11-21 12:40:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 34660198-bfda-3078-a86b-c51ab19ab740 | -17.7161 | -53.60482 | 2025-11-21 12:40:00 | TERRA_M-T | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b0ee2fcc-0926-3ba7-b31f-2ec754592f43 | -13.37615 | -53.55129 | 2025-11-21 12:40:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4410c931-cdf3-38f6-8cc6-f240a831d4f7 | -13.03546 | -53.67354 | 2025-11-21 12:40:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 0b3bb356-54cc-3afd-b01c-eb2cd81dca8e | -20.88691 | -52.35352 | 2025-11-21 12:40:00 | TERRA_M-T | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 96649994-2b78-3dd9-93d2-00db5b8493ce | -18.84729 | -53.61322 | 2025-11-21 12:40:00 | TERRA_M-T | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 17.1 |
| f34d568d-f036-3ab9-938a-1990d23b7fc6 | -21.27242 | -51.69223 | 2025-11-21 12:42:00 | TERRA_M-T | SÃO JOÃO DO PAU D'ALHO | SÃO PAULO | Brasil | 3549300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 457b1d33-3e46-37aa-8e1f-2d804800a479 | -23.17311 | -52.27621 | 2025-11-21 12:42:00 | TERRA_M-T | ALTO PARANÁ | PARANÁ | Brasil | 4100608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| daf835fc-064d-375f-839f-e3482a95192c | -25.57485 | -54.57615 | 2025-11-21 12:42:00 | TERRA_M-T | FOZ DO IGUAÇU | PARANÁ | Brasil | 4108304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| c553816a-f4a2-3435-8296-4a32fd956814 | -28.85287 | -51.88625 | 2025-11-21 12:42:00 | TERRA_M-T | GUAPORÉ | RIO GRANDE DO SUL | Brasil | 4309407 | 43 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 961eab3a-01ce-390f-b4bb-730f93c1ed34 | -25.08395 | -50.17231 | 2025-11-21 12:42:00 | TERRA_M-T | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 247ae9b5-92dd-3382-8d79-790e59b5e2ab | -27.37054 | -49.96512 | 2025-11-21 12:42:00 | TERRA_M-T | POUSO REDONDO | SANTA CATARINA | Brasil | 4213708 | 42 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| 0e1d5655-81ba-3402-bcb9-7000082328f4 | -23.02876 | -52.12932 | 2025-11-21 12:42:00 | TERRA_M-T | CRUZEIRO DO SUL | PARANÁ | Brasil | 4106704 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| 9393a72d-1165-36a3-8879-1e31761f869e | -26.26041 | -49.92387 | 2025-11-21 12:42:00 | TERRA_M-T | ITAIÓPOLIS | SANTA CATARINA | Brasil | 4208104 | 42 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| f04deb4d-ce47-3ca4-9418-6dd77288caf2 | -24.84244 | -49.98018 | 2025-11-21 12:42:00 | TERRA_M-T | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 23.7 |
| 75671097-b1ec-39f2-8baf-e45a57ee021a | -25.45449 | -49.51984 | 2025-11-21 12:42:00 | TERRA_M-T | CAMPO LARGO | PARANÁ | Brasil | 4104204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| df29a1a0-5715-3a0d-99b8-2855f217cd60 | -24.84409 | -49.9737 | 2025-11-21 12:42:00 | TERRA_M-T | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 22.1 |
| 449ee851-da5b-377a-b222-72ffd8ba3c1d | -21.82435 | -49.91465 | 2025-11-21 12:42:00 | TERRA_M-T | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 46.8 |
| eba12d3a-05df-30cc-99ac-6ec2f1c7e8c8 | -24.32811 | -50.61952 | 2025-11-21 12:42:00 | TERRA_M-T | TELÊMACO BORBA | PARANÁ | Brasil | 4127106 | 41 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| c1c005b8-4a1b-386c-be37-95c639257c52 | -25.48293 | -54.49903 | 2025-11-21 12:42:00 | TERRA_M-T | FOZ DO IGUAÇU | PARANÁ | Brasil | 4108304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 632575fe-9c5d-3347-a50b-ef42e263b101 | -23.28232 | -55.3861 | 2025-11-21 12:42:00 | TERRA_M-T | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 32.6 |
| a95a65d7-4b93-3c54-a29c-faa2b2fa7c50 | -30.63473 | -52.74576 | 2025-11-21 12:44:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 23.4 |
| 6d7e1b1c-cdbc-3413-a3ae-65933d59925f | -29.61003 | -52.19304 | 2025-11-21 12:44:00 | TERRA_M-T | VENÂNCIO AIRES | RIO GRANDE DO SUL | Brasil | 4322608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 7bd92a3e-ba11-3741-bb25-2442bcebfda0 | -29.09524 | -52.32435 | 2025-11-21 12:44:00 | TERRA_M-T | FONTOURA XAVIER | RIO GRANDE DO SUL | Brasil | 4308300 | 43 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| 3a65f0bf-c9e3-339d-a673-cb65a0314003 | -29.22694 | -51.32804 | 2025-11-21 12:44:00 | TERRA_M-T | FARROUPILHA | RIO GRANDE DO SUL | Brasil | 4307906 | 43 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |


