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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12478ebd-faac-3e15-ac52-25459afaf282 | -5.49993 | -42.6319 | 2025-09-03 03:53:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 16f30edb-5814-3edc-ac5a-ed90ef0d2d75 | -5.4033 | -42.33091 | 2025-09-03 03:53:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4fbc75b0-b028-3a56-8973-e3c8c64662ca | -4.16369 | -46.78802 | 2025-09-03 03:53:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e5903d8a-4d64-3124-8556-a3fce3e9a56c | -5.80347 | -43.2348 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83916a58-f8d6-3f69-b1d5-e494acc5a8e8 | -5.08179 | -42.87832 | 2025-09-03 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0447c1a1-fa79-3915-ba60-b7d9f9112855 | -4.90802 | -37.41649 | 2025-09-03 03:53:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5cfc5294-08cc-3df0-8138-9a52327ba0f7 | -4.90589 | -43.19128 | 2025-09-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 33b4c155-bc5a-3783-98e3-0d8aafe3fd0c | -3.78662 | -49.43172 | 2025-09-03 03:53:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd38fdf4-857a-340e-9b26-c93f3a4f8a30 | -5.53158 | -36.85334 | 2025-09-03 03:53:00 | NOAA-20 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 4.8 |
| a1c78439-5908-3c15-bbd8-6609ea1ad495 | -2.93326 | -49.46671 | 2025-09-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ec2c83d-703b-33f6-96d7-b925225d4b07 | -4.47883 | -48.12004 | 2025-09-03 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4e47bc1-5524-396d-a01b-a513397ee0cf | -4.66487 | -41.95905 | 2025-09-03 03:53:00 | NOAA-20 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7995c086-8358-3782-98a4-2157fa0f133f | -4.89362 | -43.21515 | 2025-09-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f68a074c-3f75-3e6c-be0d-a682e46b4b5f | -4.19132 | -46.84849 | 2025-09-03 03:53:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 22bb58f1-d5d9-384d-a9b6-c4fd7edeb7ff | -4.78091 | -43.66397 | 2025-09-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 410eafb2-48bf-30bf-b62e-3e81bb05c967 | -3.37529 | -47.15889 | 2025-09-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aff71daa-5c5d-3484-9cfe-82264fb86189 | -4.45003 | -38.44775 | 2025-09-03 03:53:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6844dfa0-3d53-35ab-9ffb-13d0d8605fa9 | -4.8183 | -43.64641 | 2025-09-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 13905e4a-03ea-3e21-a805-c8cb8613b4be | -5.79889 | -43.23763 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0104e36e-c836-31d1-a105-16fd3e7c617b | -5.40569 | -42.33328 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 72614cfe-92f7-3e4b-b69f-150b13892d8b | -4.45058 | -38.44429 | 2025-09-03 03:53:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 68bd1174-3f6a-347a-b5c8-8ce67dcb2f4d | -5.70681 | -43.11133 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0d5f622e-80a7-30e1-8d29-0c56d9174b50 | -4.47382 | -48.11505 | 2025-09-03 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d73908a9-59a6-3905-a2fb-b5d037ad1a42 | -3.79289 | -49.43277 | 2025-09-03 03:53:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6d53bc6a-42f2-3bb4-be02-249f1b597232 | -2.89944 | -48.29868 | 2025-09-03 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8475f8d3-3e06-38a6-896a-4e5993429486 | -5.1702 | -42.82745 | 2025-09-03 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a7e3c6b-697e-34cb-84ad-082c9d59aedb | -5.43849 | -42.90326 | 2025-09-03 03:53:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| ccbede69-d65a-35af-a635-caccb1525161 | -4.66939 | -41.95508 | 2025-09-03 03:53:00 | NOAA-20 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 51603234-dd6b-377b-9a32-ebc15789683d | -4.68231 | -42.93047 | 2025-09-03 03:53:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11fdbbec-a7e6-3e14-a0dc-6717dd0c16e2 | -3.22867 | -47.12408 | 2025-09-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| fac68812-fb2f-3ac5-a258-f72a42d68fa2 | -4.68241 | -43.65567 | 2025-09-03 03:53:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2258f48f-7935-3b77-9edf-c728625f3e74 | -5.56257 | -43.08005 | 2025-09-03 03:53:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c989dfb0-65fa-3fce-b6cc-7be4c7fee235 | -5.84274 | -42.99288 | 2025-09-03 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 016dae99-d49a-3ecd-8c98-ce63e4cc3b30 | -3.22687 | -47.13469 | 2025-09-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 8af07fba-d342-3ea3-81bd-49ffca330853 | -5.53268 | -36.84618 | 2025-09-03 03:53:00 | NOAA-20 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 4.7 |
| c95f5b07-c7da-38bd-bd3f-62e222676647 | -4.15315 | -46.78656 | 2025-09-03 03:53:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b93edcc9-8aec-3027-a95a-9ad427b67319 | -3.79074 | -49.43046 | 2025-09-03 03:53:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 17a02fc0-b733-3801-853d-105c2930467f | -3.22321 | -47.12325 | 2025-09-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 04b800f9-3737-3381-b9f9-1e99131394c7 | -5.79945 | -43.23417 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 293db8cb-6484-3d43-8b68-517ce39eccc0 | -5.53213 | -36.84976 | 2025-09-03 03:53:00 | NOAA-20 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 4.7 |
| c7b8b9ed-9630-3a6c-a2a2-d4d90b8a564e | -5.80291 | -43.23826 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 305a7f57-35c2-3a4c-9c46-2224c81928bd | -4.15843 | -46.78725 | 2025-09-03 03:53:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ae23e07b-df63-3997-bfb0-1066c83cdd0b | -4.15259 | -46.78983 | 2025-09-03 03:53:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f44da723-a84d-3bae-9ade-84e6c88eb404 | -4.15785 | -46.79062 | 2025-09-03 03:53:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7436d242-aac1-3369-bd78-62657d97622c | -5.80001 | -43.23073 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e637f447-f178-3e67-9587-d7c657f760e4 | -5.74231 | -39.75851 | 2025-09-03 03:53:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f6618cd5-9d0d-3252-9e60-ace975deebd3 | -4.67885 | -43.65113 | 2025-09-03 03:53:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c888c34-46f9-3851-b4da-e74afb9fd272 | -3.22262 | -47.12674 | 2025-09-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 8552ee3f-1f84-3f63-8f09-df27af67c242 | -10.49444 | -50.33507 | 2025-09-03 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b33e3be-dc68-3ab7-8df5-ba8af2329cc8 | -11.6093 | -52.0673 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 00fdcf14-24ec-3e98-b692-eed6d0c5a32e | -12.97488 | -48.09081 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e0e27097-b336-3bec-ae5b-f17d105afa4c | -14.79257 | -48.20102 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc3088bd-c68e-3edd-b838-e23e80c4fe8c | -9.13824 | -49.65424 | 2025-09-03 03:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 723c4bbc-4ffa-3451-9892-f3f7bbeec136 | -11.86032 | -51.47442 | 2025-09-03 03:55:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 556cfc5b-0508-3c83-b9ef-110ca28e66d5 | -14.05316 | -44.62187 | 2025-09-03 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a43f323-af1e-3dd3-b766-44b0d4f8d353 | -10.94767 | -50.78016 | 2025-09-03 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f82a8c14-886d-36a9-b6b8-c38aee51e449 | -9.15068 | -49.65217 | 2025-09-03 03:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34a906cb-8e13-346b-b0d1-a72c77a3016c | -13.30177 | -46.93162 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 331f7617-ebdd-3d45-abc5-997cf52ca557 | -13.66709 | -46.94664 | 2025-09-03 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34b66199-3329-38a0-9526-040fa237532a | -9.75081 | -46.91559 | 2025-09-03 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d6071004-9987-343c-b129-b6cd067ccb9d | -11.38494 | -43.5708 | 2025-09-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a63bfb06-ad09-3b6a-869c-6af8c3ff6d52 | -9.64118 | -47.85855 | 2025-09-03 03:55:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e639f8d7-3842-37d4-8846-af68a2fe5b75 | -15.15065 | -52.36323 | 2025-09-03 03:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bfb0c570-d465-32c0-9adf-e39db062ebec | -14.26615 | -51.23429 | 2025-09-03 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4098610-8344-321a-8d1a-9f98d9f2f536 | -9.64861 | -47.85831 | 2025-09-03 03:55:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 556bb720-e8d2-312e-82bc-93a9e7a24b3a | -11.90086 | -46.6641 | 2025-09-03 03:55:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a8f5fab-b763-3c3d-8a92-24bf24f6f271 | -13.31261 | -46.82491 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 22d56c46-fd97-39f5-8e1b-37ba11e7253f | -11.91893 | -46.6684 | 2025-09-03 03:55:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce4ab1a2-de90-35d7-a559-2fdb42788c4c | -13.50246 | -47.02054 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 461267d5-48a7-35ae-83e1-e53664cc5bd7 | -9.22565 | -47.13288 | 2025-09-03 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0db9fe8f-5214-37a3-97f9-7015a8ec5084 | -14.77899 | -47.52016 | 2025-09-03 03:55:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a601f59-5392-3221-8b40-e4e028418dbb | -15.54392 | -48.35348 | 2025-09-03 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c680604b-dd1c-35e8-977e-8a7fbbbd06cd | -11.9226 | -46.6742 | 2025-09-03 03:55:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f0d7eea-e44d-3ef0-9b18-15a8dd254685 | -12.49144 | -47.47812 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5f12881e-5832-36f6-82a1-cb3ae111e67a | -15.90098 | -48.16393 | 2025-09-03 03:55:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 475e2dbc-2777-3ecf-9074-a1d8e9dc130f | -11.60348 | -52.12924 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 28fb7044-2aed-3b2a-9c65-342ff25773c7 | -15.56089 | -48.41903 | 2025-09-03 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eeec2834-3a7e-3c34-a565-c05dc4600e85 | -9.13905 | -49.64998 | 2025-09-03 03:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8ed66b82-c53a-3b7a-b8ad-d8fc5ab64001 | -15.5482 | -48.3822 | 2025-09-03 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fe93c00a-7b4f-3722-9c65-400c369a25ab | -10.9499 | -50.77283 | 2025-09-03 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c41cdb1e-3694-3733-9f52-6e7256e49e01 | -13.31958 | -46.82758 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4c5ae404-eecb-3552-b67c-a0494ab3700a | -14.99341 | -48.80622 | 2025-09-03 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a568f4b9-4c99-30a3-bb4f-d125b1ff5559 | -14.80663 | -48.23083 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 56fcd3c4-edd1-3320-b555-d5916754d6e5 | -12.85781 | -48.02742 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba164b0c-09a3-34a8-9871-98b05e907405 | -13.29638 | -46.93533 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7b061d0-853c-3932-a81a-a6046ef4f169 | -11.05357 | -45.40369 | 2025-09-03 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 26d52549-0ddf-3cf7-9867-c0828eeb3e71 | -15.15814 | -52.35827 | 2025-09-03 03:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00322057-de33-3403-ac35-7e06be5119d0 | -9.71547 | -48.30852 | 2025-09-03 03:55:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22d810cb-6b40-3a6e-a6f9-5f3881dbbf16 | -15.02575 | -50.07484 | 2025-09-03 03:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f73d003-a334-3f82-b7a5-b2388a9617e6 | -12.84168 | -48.03215 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e410fbbc-219c-37e2-8552-5a763d677f30 | -14.0493 | -44.62115 | 2025-09-03 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f552fb16-4e9a-395f-927b-cf28b424acb8 | -15.1637 | -52.36248 | 2025-09-03 03:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a043d0df-47ac-316f-93f2-1bbffd90c83c | -15.02121 | -50.06957 | 2025-09-03 03:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b2c6f443-21ac-34bc-a305-5244503ecc19 | -10.93783 | -50.77033 | 2025-09-03 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 993f9712-a986-35b2-b2b3-8e6a29509146 | -12.51749 | -49.58287 | 2025-09-03 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f21bc56-008c-3104-b385-d7b3933ded49 | -9.6355 | -47.86063 | 2025-09-03 03:55:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fdd52e35-dcb8-3ce3-8426-77c5a6939ae5 | -11.61692 | -52.06284 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3c9c948d-e30b-379a-817c-37342d01ae6a | -13.2713 | -46.88805 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d6b32f9-9eac-3a6c-855c-faccdd596ef5 | -9.13985 | -49.64574 | 2025-09-03 03:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3b5a0088-fefa-3248-bd57-4ab6641071b9 | -11.59928 | -52.11665 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README38.md)
