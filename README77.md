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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37eeb8df-c6e1-3b2b-976f-716101b78163 | -2.63465 | -46.20578 | 2024-11-21 05:18:00 | AQUA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6142187e-d670-31f9-954e-0cf757101638 | -2.38095 | -48.92011 | 2024-11-21 05:18:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6a9576b6-e674-3fd0-b926-50e16e00159d | -1.46093 | -52.66486 | 2024-11-21 05:18:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 28fb9193-c58d-3820-9f07-f01ede3b66d3 | -2.64447 | -46.14011 | 2024-11-21 05:18:00 | AQUA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c87c7532-8829-3922-ab59-fc7a780df879 | -1.59671 | -47.13885 | 2024-11-21 05:18:00 | AQUA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| b635ebd4-b9f8-3c54-89cd-52c1a79f04e1 | -2.24808 | -48.16357 | 2024-11-21 05:18:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a6cc52cf-8f6a-3696-8b65-bc2a71aac59f | -2.7171 | -46.08978 | 2024-11-21 05:18:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ecfd2bc0-74c1-3161-830e-1faaeac6387d | -1.59271 | -47.49667 | 2024-11-21 05:18:00 | AQUA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 536f4afe-4b98-3ad9-ada3-6ea56b5cb477 | -2.83252 | -46.67532 | 2024-11-21 05:18:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 662fb0bc-2b66-3a70-a01c-60aa47d4cbfb | -2.62412 | -48.06591 | 2024-11-21 05:18:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| a7a01f26-eea7-36da-a60d-83bb7f1b7d93 | -2.17352 | -52.12061 | 2024-11-21 05:18:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 5e2c2604-3d6d-306d-8229-1e5311215ff3 | -2.55535 | -46.54632 | 2024-11-21 05:18:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 903ef140-f7c1-3407-a29e-23a105900436 | -2.69594 | -46.23032 | 2024-11-21 05:18:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e0e6c426-4727-364d-a4b9-5f9ff5c02cd6 | -2.6931 | -46.24918 | 2024-11-21 05:18:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 3586b67a-9491-3f57-9f02-424873aad88d | -2.63324 | -46.21523 | 2024-11-21 05:18:00 | AQUA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 6977c0cc-0b8f-3d15-9828-17e1e4222ab7 | -2.65766 | -46.54726 | 2024-11-21 05:18:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 26765b06-b97b-35b6-acb5-1267db91d82c | -2.24199 | -48.15577 | 2024-11-21 05:18:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 998c22fc-de78-3315-8c01-ed5658e8ab5a | -2.66943 | -46.15913 | 2024-11-21 05:18:00 | AQUA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 169522e0-ea62-3a61-a54d-be94f263ee90 | -2.84183 | -46.6767 | 2024-11-21 05:18:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ff010468-17a2-3fa3-99f4-6303c8138651 | -2.60884 | -49.24458 | 2024-11-21 05:18:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ae0c96dc-970a-35fb-9deb-1835a2aaf5e1 | -4.58 | -48.0132 | 2024-11-21 05:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 1afbab2c-ed7d-3d92-ad13-97a3342ddb33 | -2.0259 | -54.5289 | 2024-11-21 05:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 32307a8b-ef7f-34e7-ba05-924824457c9f | -3.2951 | -53.8395 | 2024-11-21 05:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| a088d718-3b9e-3bf8-b3c9-23e15745adb5 | -2.7675 | -52.1251 | 2024-11-21 05:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 1984d25a-1604-35b6-ba91-2b545a8a4b18 | -3.2767 | -53.84 | 2024-11-21 05:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 05630a4d-aa6a-3679-a409-c096cf3f68b6 | -3.2768 | -53.8199 | 2024-11-21 05:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| c802dd34-5e26-3af5-893e-2073b6a559ce | -2.7676 | -52.1045 | 2024-11-21 05:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| d26bd183-9bb0-3b7d-9767-290b10fe9aa4 | -3.295 | -53.8597 | 2024-11-21 05:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 8eb00a51-d313-3286-914f-551fd8ce61fc | -4.5799 | -48.0349 | 2024-11-21 05:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 7e77bcca-3cf0-33fa-8f99-fe71f9c13d9f | -6.82354 | -46.77739 | 2024-11-21 05:20:00 | AQUA_M-M | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 51e2c8f8-18c3-3795-bfc1-589bb79e948d | -3.39338 | -50.25301 | 2024-11-21 05:20:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 4ca8b430-185c-3897-8d42-a705819d4adc | -3.53123 | -50.43473 | 2024-11-21 05:20:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| e7ac9bff-137e-35be-8a93-2264e5167ff3 | -3.68889 | -50.21523 | 2024-11-21 05:20:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 2da62c2d-3694-37ca-904d-82655f51ee21 | -4.57657 | -48.0218 | 2024-11-21 05:20:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| c1c4e7d4-1e27-3503-a92b-1ce8bc062a77 | -3.0641 | -49.19984 | 2024-11-21 05:20:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| afd0de81-7e29-3ffd-b47e-485ae6c1a996 | -6.20674 | -46.21656 | 2024-11-21 05:20:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| a56d1ed4-2e96-3527-a58d-e36a02d5ea70 | -2.19334 | -53.63612 | 2024-11-21 05:20:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 3b72305a-0354-3006-b9ae-3731222eadd4 | -2.76339 | -52.11618 | 2024-11-21 05:20:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 9d522718-a9de-3fe4-8ffb-180c4cc20390 | -2.93154 | -48.33342 | 2024-11-21 05:20:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 62d1f1d2-c7fe-3010-a7ba-8e2b2b17e315 | -4.56674 | -48.02034 | 2024-11-21 05:20:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| d11b92b5-406d-3b31-bd1e-cb5a2be0270c | -4.38245 | -47.75713 | 2024-11-21 05:20:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 13d04d15-d94a-3baf-917c-d3c9188ad53f | -3.81356 | -47.79008 | 2024-11-21 05:20:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 19773e5c-3e90-3ac1-9bc5-bcb6cf9019aa | -3.46975 | -49.99896 | 2024-11-21 05:20:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 28c9be56-53c8-3ae0-8114-ae4acd65a598 | -3.09712 | -53.21069 | 2024-11-21 05:20:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 97697959-581e-3273-8a39-98fafe697e06 | -3.29858 | -50.35212 | 2024-11-21 05:20:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| f23d64ad-df03-3425-b43e-ba7a29279fc6 | -3.53307 | -50.53059 | 2024-11-21 05:20:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 871e1c83-5ea7-3e7f-9aac-ae712712d7fd | -6.11927 | -42.50943 | 2024-11-21 05:20:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 57.6 |
| cb367e86-ba9f-3db6-9d1f-3f60a07570a3 | -3.27337 | -53.84489 | 2024-11-21 05:20:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 80b2fbc5-f4bc-333f-97df-7167f9bd77c2 | -3.67887 | -50.22453 | 2024-11-21 05:20:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 84b933d7-5f70-3707-9e41-041d983609b7 | -3.67713 | -50.21336 | 2024-11-21 05:20:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 7066c769-b1a3-3e0f-83c3-590f6a07aa58 | -5.94845 | -44.2401 | 2024-11-21 05:20:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 581cae07-0dfc-3933-88e2-31413a07e919 | -2.75311 | -52.08969 | 2024-11-21 05:20:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 468885fd-f38a-3a97-a626-687703a835f8 | -3.24873 | -50.55172 | 2024-11-21 05:20:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 52ac1a87-0211-3d68-9773-e891a6e88f84 | -3.18369 | -46.54377 | 2024-11-21 05:20:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2dadf721-48d0-3fd9-a8a4-5392094106f0 | -2.74941 | -52.11403 | 2024-11-21 05:20:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 3d20c59d-0139-31d1-bb9e-ecb36f1c66c8 | -2.1883 | -53.66839 | 2024-11-21 05:20:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 6efb7cb5-7f46-3c7d-aaf3-79486a2c7d29 | -3.00728 | -51.01372 | 2024-11-21 05:20:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 7aa58c62-b040-3708-b704-ccc0c8b4afe0 | -5.42434 | -45.33971 | 2024-11-21 05:20:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f045a832-6248-340a-8749-9d19b55668ae | -3.57246 | -50.40607 | 2024-11-21 05:20:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| da388abe-0a2f-352c-819e-2e5248b1632f | -4.57825 | -48.01073 | 2024-11-21 05:20:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 1d1f82c7-3f53-3b6b-948f-6525052f7578 | -3.57645 | -50.4136 | 2024-11-21 05:20:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 28c6c7f1-8f9f-329c-b3d1-a511b91ea3d7 | -3.68132 | -50.20844 | 2024-11-21 05:20:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 0e718fc0-937f-388e-a5c3-04558b1c28e9 | -3.09663 | -49.44437 | 2024-11-21 05:20:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ac6f6842-0d68-3fcf-963a-7501e6058fc4 | -4.66283 | -46.53305 | 2024-11-21 05:20:00 | AQUA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| e948cce8-1a63-33d2-9f54-156c023e27c8 | -6.18076 | -43.41427 | 2024-11-21 05:20:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 41bfcfc1-038b-3f57-89b0-7aa096f851d0 | -3.28928 | -53.84705 | 2024-11-21 05:20:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 443c15ad-5d41-3ed2-8485-44eaf2647f82 | -3.28848 | -49.18082 | 2024-11-21 05:20:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 236c9159-2205-3a93-8407-120d00e3b27f | -3.29588 | -50.36907 | 2024-11-21 05:20:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| e7718d49-900f-33bf-a61e-25065607fed5 | -4.24487 | -46.11957 | 2024-11-21 05:20:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 37.5 |
| c1e33af9-d083-3d08-ae66-63a2cdc8bcc7 | -3.35134 | -50.17245 | 2024-11-21 05:20:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| a6bf0864-bbec-3cce-8e16-e15e867ecd42 | -2.20356 | -53.6428 | 2024-11-21 05:20:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| e7e5268c-a159-3fb5-9455-d922f0e14f1a | -3.00268 | -51.30402 | 2024-11-21 05:20:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| d5076496-2808-3b0b-866f-683c95f1244c | -4.38079 | -47.76791 | 2024-11-21 05:20:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ca4d7177-223b-381a-b6b8-c6b413ec7fb8 | -2.75282 | -52.12203 | 2024-11-21 05:20:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| c82ea469-4d00-32bb-9a9a-4215f8bcc806 | -6.81452 | -46.77603 | 2024-11-21 05:20:00 | AQUA_M-M | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 44a105fb-78d3-3eaf-930e-bcf80b0e83fd | -3.46724 | -50.01493 | 2024-11-21 05:20:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3738af02-51f2-390f-b2f6-5de98cc8835f | -3.80376 | -47.78862 | 2024-11-21 05:20:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 249d8e07-af9d-3767-9ce9-d33ae774e410 | -2.02152 | -54.51242 | 2024-11-21 05:20:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| c3a8fe87-cc72-361d-9f39-1de3a012f833 | -4.57814 | -48.02766 | 2024-11-21 05:20:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| a5bd4235-b973-33b6-a612-1fef69225d7c | -4.14787 | -43.87406 | 2024-11-21 05:20:00 | AQUA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c199e1cf-f328-3e64-b413-3a24a1fbd0c8 | -4.57988 | -48.01656 | 2024-11-21 05:20:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 5762530d-da80-3ca8-b430-322ed9cf744f | -6.1177 | -42.52024 | 2024-11-21 05:20:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 5b25e2a0-b574-3c92-acb2-9e574867590a | -3.28368 | -49.18848 | 2024-11-21 05:20:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 28483322-c85a-3307-be5f-6c41bc5a0750 | -5.71717 | -44.80619 | 2024-11-21 05:20:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 8df51fe1-5b2e-35b9-b36c-acdfeddaf376 | -4.63704 | -49.53759 | 2024-11-21 05:20:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 44352442-6245-330b-986f-0a3297d94423 | -3.2863 | -49.19459 | 2024-11-21 05:20:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 51482b23-620c-3eb1-ad7c-a8712da8343d | -4.06284 | -46.83468 | 2024-11-21 05:20:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e2eca7d2-3449-3c12-bb6c-0129ba7342d1 | -2.0202 | -54.5042 | 2024-11-21 05:20:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| a0c98ae4-f982-3569-b90f-d0f0c3253996 | -3.2946 | -49.1902 | 2024-11-21 05:20:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 464141b2-2122-3a20-8f6d-b150f3718ef2 | -2.7567 | -52.09772 | 2024-11-21 05:20:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 47a724be-88f3-3ba1-9ff7-80bd3bb2176d | -4.24626 | -46.11046 | 2024-11-21 05:20:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 012867bf-3edf-392e-88d2-286e12f31c58 | -4.66142 | -46.54232 | 2024-11-21 05:20:00 | AQUA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bfc5945f-263e-3a2e-91d3-0d0a6f16b993 | -3.5927 | -43.63565 | 2024-11-21 05:20:00 | AQUA_M-M | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f579a6ad-5527-3f79-a6e2-7e6937d8aeff | -4.23589 | -46.11825 | 2024-11-21 05:20:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0cfbddbf-fe4c-3062-b38a-f6471e435b20 | -3.88624 | -46.65804 | 2024-11-21 05:20:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 05a60067-c478-3b76-a241-fb2e59f17718 | -3.95836 | -46.72438 | 2024-11-21 05:20:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9032a178-0dbc-3ff7-a818-1f20e6476678 | -4.09702 | -48.47846 | 2024-11-21 05:20:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4c2a8710-d94f-39a6-82ab-bb031cca368d | -5.9471 | -44.24924 | 2024-11-21 05:20:00 | AQUA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| cb45b7ad-1442-32bd-8335-cb27bc03bc96 | -3.27839 | -53.81311 | 2024-11-21 05:20:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 83e5bd72-c4c8-3f40-a669-e5d6cdb41e56 | -3.2773 | -50.20615 | 2024-11-21 05:20:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |


[Clique aqui para ver as próximas entradas](README78.md)
