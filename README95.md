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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e901680c-84cc-3dd3-a555-109549da6271 | -10.9402 | -50.2764 | 2026-08-30 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| d9b4c6f9-8524-364b-9673-fa07672df927 | -5.7197 | -52.28 | 2026-08-30 15:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 6878f552-7e71-394e-b020-280ef6093deb | -11.2109 | -51.2476 | 2026-08-30 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 38c64c12-bef6-31c8-b38f-eb5c4ad2d497 | -11.1807 | -55.1024 | 2026-08-30 15:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| a3c6a9f9-d147-3074-aff3-666be91508f2 | -13.3995 | -51.4397 | 2026-08-30 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 3a52d0a6-5211-301f-89e7-45cec5267488 | -6.9548 | -55.6948 | 2026-08-30 15:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 532ccbe6-02b0-3337-892f-154309458f58 | -6.0726 | -57.9583 | 2026-08-30 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 5c6fb4f6-ec06-3355-be5e-f9a63453b797 | -10.7644 | -50.6792 | 2026-08-30 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 398d3d9e-efa5-3711-9b5c-a6bc4e3e66fe | -10.7593 | -54.0589 | 2026-08-30 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| cbcb91d7-8c50-3879-996a-7165086ffa3d | -7.9907 | -46.5177 | 2026-08-30 15:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 6eba6e55-1871-306b-b0a1-892ac53922c0 | -9.9284 | -60.4856 | 2026-08-30 15:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| dad95f15-5249-36e9-81b8-899adf2efdea | -15.4601 | -52.806 | 2026-08-30 15:50:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 100.7 |
| dcb5af79-849f-3539-a054-7d4899ba1c0c | -11.1913 | -51.292 | 2026-08-30 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 06c81ae3-4c98-3a5b-955f-c8b99119f103 | -8.5925 | -66.9379 | 2026-08-30 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.8 |
| dda1592b-0db1-39fd-af47-2fa1e65782f8 | -21.0376 | -57.8284 | 2026-08-30 15:50:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 92.6 |
| 587b2d49-c402-32ff-8d57-930e76a72b7f | -10.4794 | -64.5012 | 2026-08-30 15:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| d825fc57-783e-34ec-a576-ac8d677e9fc2 | -10.5598 | -50.4236 | 2026-08-30 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| c54a783b-4f30-3cec-b9f5-839cf8736799 | -10.9592 | -50.2744 | 2026-08-30 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 18f22b6d-be61-3a2f-abba-52546e2a9b91 | -7.3479 | -55.1544 | 2026-08-30 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 7906a803-2db3-373f-97c0-5a2fde1891bc | -8.2229 | -54.9412 | 2026-08-30 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| ebadbf4f-4f80-34e8-a717-80380ee9c158 | -10.3202 | -49.9782 | 2026-08-30 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 07add3c7-8424-3f08-98e1-d0a042ac111d | -7.9169 | -61.3671 | 2026-08-30 15:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 07665dee-9c4d-3265-9492-b2615467371a | -10.3205 | -49.9567 | 2026-08-30 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 01b3156e-ce42-34f8-b014-ac72f93550f9 | -6.1294 | -57.6833 | 2026-08-30 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 4d61db2d-1263-33a4-ae18-4f8a4753fabd | -10.8253 | -45.3152 | 2026-08-30 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| a0c6c647-d5a3-3369-bc73-417a7a7f7252 | -6.8015 | -59.4586 | 2026-08-30 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| ca1bb2de-12cc-3ea2-a10c-504e26a629bf | -10.1538 | -45.6982 | 2026-08-30 15:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 1b900017-8e2a-36f8-bad3-9473d0c60460 | -9.0245 | -65.3994 | 2026-08-30 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| e7547077-52b9-357b-a2e7-85bc31b6857d | -10.9405 | -50.255 | 2026-08-30 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| d89e9e74-165e-39eb-8b9f-64287f21e1ab | -8.574 | -66.9569 | 2026-08-30 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 116.8 |
| c7a06455-29b9-3cae-b549-cb861b2368e4 | -11.2298 | -45.0759 | 2026-08-30 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 7ba411a1-3692-3b03-a214-98315ae3e1ad | -10.5593 | -50.4663 | 2026-08-30 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 833c3b3f-268e-365d-9bfa-1d6750ab0971 | -3.6033 | -60.5474 | 2026-08-30 15:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 3295ae04-b2d4-373e-b042-3e36fc8e7240 | -7.5272 | -44.3413 | 2026-08-30 15:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 207.0 |
| 8fa5b8f3-b3a0-383e-898c-48630669c32c | -15.2478 | -53.8666 | 2026-08-30 15:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 203.8 |
| f6c8ce81-4187-3d46-a9df-fd82668e0e66 | -10.7598 | -54.0179 | 2026-08-30 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 59dd8740-458a-39c0-b281-bfef454d3bc7 | -9.9282 | -60.5049 | 2026-08-30 15:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 168.8 |
| aab22393-e040-3121-86a2-5ed74b0b7946 | -9.8991 | -64.9945 | 2026-08-30 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.8 |
| d4b30ff5-d5d8-3519-af64-7cb4d9d218b1 | -10.3391 | -49.9762 | 2026-08-30 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 109.6 |
| ac54915c-4bee-31c0-8be6-e3d4fa6cd27f | -13.4191 | -51.4159 | 2026-08-30 16:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 9d66333d-d7d1-3972-b341-d46991401b32 | -7.6343 | -44.8358 | 2026-08-30 16:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 734476f6-a06c-3e46-a04a-44bf9e7b670d | -21.0372 | -57.8494 | 2026-08-30 16:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 53.9 |
| 75e8d879-cfa9-3e14-b757-83f4c35aff97 | -8.631 | -66.5473 | 2026-08-30 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 6b1b3717-9722-35ca-aca8-bbb2fbab6d76 | -14.2989 | -51.7072 | 2026-08-30 16:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 11af22c3-9f9f-3fb5-b1cb-5246d0391297 | -8.1534 | -45.4904 | 2026-08-30 16:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 3db10ab6-1a0c-31c1-9a72-9e806d9c828f | -6.1743 | -53.4834 | 2026-08-30 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 98aa6cf0-aa67-30f4-abee-552113db3458 | -10.8235 | -50.5026 | 2026-08-30 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| c89effc8-998d-334e-a1e6-9e8ff3ee262e | -11.3622 | -45.1494 | 2026-08-30 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.3 |
| f67204be-fffe-33f1-b54c-9049a8a9e275 | -10.3202 | -49.9782 | 2026-08-30 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 5ab9bd04-636b-3fb3-82c3-61863e289bbe | -11.0054 | -49.6893 | 2026-08-30 16:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| c6272dbe-14ee-3e3e-91e5-e2db2cfab108 | -8.5739 | -66.9754 | 2026-08-30 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 8385bbd3-112d-30fb-9afa-2cbc53eed49d | -11.6396 | -50.4553 | 2026-08-30 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 61cf075f-7ff5-38f6-981b-70276f87c4ac | -13.856 | -54.1175 | 2026-08-30 16:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 195.8 |
| b80288e9-e268-3b00-bf41-70546111a287 | -8.5925 | -66.9379 | 2026-08-30 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| ff6068a6-9d93-38f0-9edc-eebf58ec7111 | -10.5404 | -50.4683 | 2026-08-30 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| b4d92eff-d53a-3233-a306-89814f28abe6 | -6.7123 | -58.9412 | 2026-08-30 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 22776455-a684-33a7-aee1-506f76357858 | -15.2478 | -53.8666 | 2026-08-30 16:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 469.4 |
| 47f653a3-3ed3-3c3a-a58f-910aa19f803b | -7.717 | -70.0855 | 2026-08-30 16:00:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 22b6fb7a-8527-3fd9-8e76-3dac27099336 | -10.4794 | -64.5012 | 2026-08-30 16:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 489df5b3-c388-39d5-9955-ebfd3ea3a6c1 | -6.5331 | -55.1178 | 2026-08-30 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 5faaf146-1ef1-3185-89d5-4032ef246385 | -7.5662 | -61.3049 | 2026-08-30 16:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| ae00d18c-0b76-3c27-9191-6a92fdf8ffa5 | -9.2262 | -65.8784 | 2026-08-30 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 134.1 |
| 4a20d535-d8f3-3e2c-899a-009a13f7a193 | -7.9422 | -44.277 | 2026-08-30 16:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 600.4 |
| 2841c38e-8050-37d3-af9b-e2d837d68737 | -7.5272 | -44.3413 | 2026-08-30 16:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 254.0 |
| 32c667fe-df3e-34c4-8f9e-668a65f18c00 | -8.795 | -50.0387 | 2026-08-30 16:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 2d71de30-cf0e-3f8e-adf4-ac40ded4a169 | -7.1312 | -42.7708 | 2026-08-30 16:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 185.3 |
| c3c16aa0-f56b-36de-98ca-4b140bb79376 | -6.912 | -59.4927 | 2026-08-30 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.0 |
| e98aebda-f28d-358e-b61d-fb4658811520 | -7.1121 | -42.7963 | 2026-08-30 16:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 111.0 |
| 309dc98a-a9ab-340b-9e06-08dec82d4e43 | -13.8752 | -54.1153 | 2026-08-30 16:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 4fa09b1b-d077-3460-b529-9a960812dc0c | -13.4194 | -51.3945 | 2026-08-30 16:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 504afc38-091d-324b-9bc6-c4f20670269b | -10.5214 | -50.4702 | 2026-08-30 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 7899868c-c3c9-385c-b4a7-b8ac573e3db9 | -11.3431 | -45.1521 | 2026-08-30 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 145.7 |
| b26bdabd-f80f-3c59-9c08-3edc0d1e7bbd | -11.0244 | -49.6872 | 2026-08-30 16:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 15198a6d-4802-3062-a8b0-3a15d60a2d76 | -8.9142 | -70.6917 | 2026-08-30 16:00:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 925f46dd-aa03-383f-92b9-5e44c565aab1 | -7.6155 | -44.8376 | 2026-08-30 16:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 96.1 |
| d0cd2914-e998-3ff2-8ff9-7fed03024d0f | -10.559 | -50.4876 | 2026-08-30 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 7432eace-0517-3c3c-abc9-f5d0f3680842 | -6.0 | -45.0889 | 2026-08-30 16:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| e0ea7726-4969-39d9-8035-6e1c5e5b7c9c | -11.2302 | -45.0528 | 2026-08-30 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| f01d75b8-2c34-3b4c-a600-4c8022a9e71f | -10.3226 | -58.0847 | 2026-08-30 16:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| c5a815f1-6488-31ea-90c9-d5a36feb29c8 | -21.0172 | -57.8313 | 2026-08-30 16:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 153.1 |
| c3ddcd9c-dbd3-3b0c-a1c5-5380528984a0 | -15.3647 | -53.8307 | 2026-08-30 16:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 214.9 |
| 20c35d5e-8abd-37ef-8ce2-55ae1276b978 | -9.9284 | -60.4856 | 2026-08-30 16:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 626cda08-86ce-3181-83f1-efbb9b9a9e43 | -8.2312 | -61.4113 | 2026-08-30 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 5ae53937-f6f8-3327-9464-ac423e17f447 | -6.7691 | -58.6873 | 2026-08-30 16:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 90979604-8467-3cd1-8751-16eb9cb0d8ce | -6.4245 | -54.7628 | 2026-08-30 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| a041dc9b-57ec-3ca0-88ac-ace600dcc1a9 | -7.9169 | -61.3671 | 2026-08-30 16:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| ed57942c-a8b1-3b19-bef8-dc99aa025fe9 | -8.574 | -66.9569 | 2026-08-30 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 122.0 |
| bb3bf702-a24a-36a4-a27c-1e06bc1e9bfe | -6.7515 | -55.6455 | 2026-08-30 16:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 76b48620-2fae-3fa2-a2be-d288137f5092 | -11.6586 | -50.4532 | 2026-08-30 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 21fa5717-3e63-3d2c-b41b-1401be6db0e7 | -6.1467 | -57.8775 | 2026-08-30 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 8980309d-46ea-3003-bd70-0db852b66c9b | -8.2229 | -54.9412 | 2026-08-30 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 6a6105d6-daf8-3d51-bda8-f59e907012b7 | -1.8779 | -55.1287 | 2026-08-30 16:00:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| c31fae59-1b1e-3190-ac0b-f1dc233c742f | -9.9282 | -60.5049 | 2026-08-30 16:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 182.5 |
| 03d58782-de4d-3f5c-b87d-691191a0a1d3 | -5.9749 | -55.722 | 2026-08-30 16:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 458a441b-dd21-317f-8ae8-1d54aeb8f9f7 | -7.9425 | -44.2538 | 2026-08-30 16:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 338.4 |
| df72b064-0e0f-3903-b843-fe26cb9e2ad3 | -10.8249 | -45.3382 | 2026-08-30 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 176.1 |
| f648cec3-140f-32b6-8a93-b3758d5fe8d9 | -8.7767 | -49.9977 | 2026-08-30 16:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| f00bfdb2-cc74-3a77-9bb6-43a13ff28ee8 | -9.7374 | -67.8725 | 2026-08-30 16:00:00 | GOES-19 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 05accaad-022f-394f-bdfc-48a18a1f7a53 | -11.6247 | -50.1783 | 2026-08-30 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 0dbb11cd-a4f3-3eff-bf08-4e51b66d57f1 | -15.2283 | -57.6517 | 2026-08-30 16:00:00 | GOES-19 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |


[Clique aqui para ver as próximas entradas](README96.md)
