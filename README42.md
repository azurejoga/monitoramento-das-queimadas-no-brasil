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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61c2a08a-be2d-3533-bba1-a98a780ccf64 | -2.72473 | -47.03799 | 2026-08-29 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1109bfa6-edb5-30b5-afed-85efdf28d117 | -4.15374 | -60.69077 | 2026-08-29 04:51:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ddc955b-3f70-3d70-92ba-c4efdd6c4f87 | -6.63655 | -43.739 | 2026-08-29 04:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 453fa7c9-38f1-385e-9def-2335fd06bb1a | -2.50052 | -48.1357 | 2026-08-29 04:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a24af0f8-cbbd-32c0-a357-d312c4a475be | -2.50169 | -48.13653 | 2026-08-29 04:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b6750b45-62e8-303e-920c-bec629939fb6 | -3.42799 | -52.77628 | 2026-08-29 04:51:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2508e59d-a020-30dd-8c32-10d6c4124c2c | -4.97627 | -56.29558 | 2026-08-29 04:51:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c156c944-458d-3135-85df-e0c73330c092 | -1.59359 | -47.35551 | 2026-08-29 04:51:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 82a9d50c-3b86-3cbe-aa9c-fa2913a5dd44 | -6.62103 | -43.74574 | 2026-08-29 04:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 6c3a20f6-400c-39bd-b5b4-c7dfd750d855 | 3.23502 | -60.13966 | 2026-08-29 04:51:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8f71eda6-8bd1-3310-a131-869f73245413 | -3.09892 | -54.51546 | 2026-08-29 04:51:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 773a412f-e0f1-3be4-b845-3a4fdaafee98 | -3.66082 | -48.96309 | 2026-08-29 04:51:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ffe808c-43a6-33ee-9030-4c63a53c946b | -6.62769 | -43.73243 | 2026-08-29 04:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| ab0bf414-4f53-3e8b-b47a-7679706fc3d8 | 0.7935 | -51.96762 | 2026-08-29 04:51:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f1d284e-3591-39d6-bb84-316b0fbc0f0b | 2.4114 | -60.884 | 2026-08-29 04:51:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f5a29a86-ef19-321a-8db8-84e5780694b7 | -5.03824 | -51.93665 | 2026-08-29 04:51:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b087c39a-81c0-3423-b795-e6def1fa25db | -6.63062 | -43.74698 | 2026-08-29 04:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 2b62d44d-a29f-369d-90f0-e52e5af2fb3d | -6.63693 | -43.73731 | 2026-08-29 04:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7cc6be6e-c33a-3a3b-bd10-d61fe511c9fa | 0.14876 | -60.40636 | 2026-08-29 04:51:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b51b84e7-75b5-3eba-98bc-992f91ea9d9c | -3.77576 | -51.17904 | 2026-08-29 04:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a829e88d-bfaa-3f5f-898f-22c911fccc98 | -6.62735 | -43.73598 | 2026-08-29 04:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 04b80f9f-1e5d-3169-815b-de6b73507e21 | -6.54641 | -43.51055 | 2026-08-29 04:51:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c137ec6-e8d8-38e6-8b18-051bd5397433 | -6.62333 | -43.7301 | 2026-08-29 04:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 61944d09-366e-30cd-9fac-940b216dfa49 | -4.92479 | -55.77211 | 2026-08-29 04:51:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ce1d6f7-d8b9-303c-b00b-8c65976db227 | -5.04158 | -51.93719 | 2026-08-29 04:51:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9f0d3c2a-5bc9-3486-8ad0-f60e6a183231 | -3.52863 | -59.02802 | 2026-08-29 04:51:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 15e6a3a7-67d5-3a85-8aba-3431b6030c35 | -4.92535 | -55.76868 | 2026-08-29 04:51:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0d1f43c-1b7c-33f0-9e6c-d22f8a53688d | -6.71285 | -44.42565 | 2026-08-29 04:51:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e0ab7d5-0d71-3d4f-8e0f-2fc0f54ce622 | -3.18357 | -48.02165 | 2026-08-29 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1a547235-9e02-3a74-b905-df8b7b967d94 | -7.05823 | -42.15369 | 2026-08-29 04:51:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7c1739c5-fe17-3f23-b158-2856409fcb17 | -6.63214 | -43.73663 | 2026-08-29 04:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1a9ae5d8-4cb3-3ab0-9322-0dfcbb026061 | -7.07186 | -42.21439 | 2026-08-29 04:51:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b3e358c8-5716-3e93-abdf-cf3fcb0317ba | -4.16856 | -42.43821 | 2026-08-29 04:51:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 75fbe5d7-abdb-318a-bdee-6d2449510776 | -5.48284 | -45.12571 | 2026-08-29 04:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60dc499e-148c-318b-8269-32d38bac86a9 | -1.59296 | -47.35951 | 2026-08-29 04:51:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f6ac231b-108e-3551-8a85-c23c4ce77eaa | 0.14809 | -60.40212 | 2026-08-29 04:51:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0b22959b-9b6d-35a2-b4e3-f8a7049ccfaf | -4.33111 | -54.90215 | 2026-08-29 04:51:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd214bc0-41c8-374c-9125-0a7b813d6865 | -4.34047 | -55.43997 | 2026-08-29 04:51:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7cd9e530-5b1c-3934-a4d1-a13f2f72f9d0 | -1.2042 | -47.76062 | 2026-08-29 04:51:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1faf2aad-6e5b-31fa-8b00-1c84bb8290f9 | 0.1422 | -60.40315 | 2026-08-29 04:51:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f3b0e00d-786b-34f2-bf91-db7d16920f8c | -5.34074 | -45.1566 | 2026-08-29 04:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2f5c766e-4ce4-3c68-9f6e-bca0089334ee | -6.62028 | -43.75087 | 2026-08-29 04:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8201e7e-5893-3c99-b513-90c7d7968da6 | -4.18598 | -54.57554 | 2026-08-29 04:51:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 097f66b7-db1e-3762-85d4-ff62750ddfed | 2.4177 | -60.8831 | 2026-08-29 04:51:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1770b2ad-3aa4-3139-bfcb-9892dfefeb1c | -4.64488 | -42.43653 | 2026-08-29 04:51:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 88f28539-3ce6-3cd9-93b3-91c53b5481c5 | -4.36829 | -47.77528 | 2026-08-29 04:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4d577690-b1aa-33a9-89f1-02c68afc3d54 | -6.62812 | -43.73074 | 2026-08-29 04:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| c92e3aed-2c20-3ff0-ad73-dad6c5c48767 | -6.92799 | -42.67685 | 2026-08-29 04:51:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 817b0c0c-c095-39ab-9ef6-cac8a323e88a | -3.60969 | -60.54102 | 2026-08-29 04:51:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15ffb455-ab57-3de4-97c5-9208b02da55b | -4.97333 | -49.6201 | 2026-08-29 04:51:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4619b598-9c6b-38d5-9eb1-03881226ec10 | 0.14287 | -60.4074 | 2026-08-29 04:51:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c7b96557-1077-3295-ab19-2c27a67dfba6 | -6.63031 | -43.74866 | 2026-08-29 04:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d3be300c-baaa-324d-b132-9893c89f9e29 | -4.3657 | -55.77222 | 2026-08-29 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f373824c-160b-3c5c-ad8e-662df019ffde | -4.28211 | -48.19096 | 2026-08-29 04:51:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d08a4057-4425-3d1a-babe-b632516f6d36 | -3.20444 | -61.14789 | 2026-08-29 04:51:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| db252181-274e-3b02-9c6c-5c1017984961 | -3.97097 | -41.51672 | 2026-08-29 04:51:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6dd46713-3f6e-3669-9591-60401520031d | -2.02386 | -52.10868 | 2026-08-29 04:51:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08ea6dcc-f5ba-3af8-a422-a861e2fb6472 | -6.62507 | -43.75148 | 2026-08-29 04:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ff550c5-0f37-3701-a185-38d05590685e | -3.94065 | -59.33317 | 2026-08-29 04:51:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa241e79-702c-37fe-b5e4-6e2d8c02552c | -3.35443 | -44.22761 | 2026-08-29 04:51:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b8e69ce-7c89-39df-a9dd-d5ffde1da17d | -6.33985 | -44.09603 | 2026-08-29 04:51:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c8415abc-b1cb-36d9-98ec-071343a91765 | -2.71977 | -47.04587 | 2026-08-29 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29075b3f-fcaa-346b-afe8-bcd26a0379da | -3.2221 | -48.61174 | 2026-08-29 04:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f554ec1e-56be-3812-81dc-038b0cabcc35 | -5.03768 | -51.94017 | 2026-08-29 04:51:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e64f6ab-dffa-398f-9eb1-857aa44c45cb | -2.9863 | -48.95238 | 2026-08-29 04:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0c815a9e-7083-3522-b687-7a8e08c0d0fd | -3.87384 | -48.04724 | 2026-08-29 04:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0623dd13-24b6-3d2f-9779-d9377c9c8e52 | -6.92755 | -42.68 | 2026-08-29 04:51:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c1055fd6-8f55-3525-820b-a087661e3833 | -3.75472 | -53.35428 | 2026-08-29 04:51:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e0ffd11-719c-3df1-8bea-32ba11c43c82 | -2.72043 | -47.04165 | 2026-08-29 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e6f35cfc-935a-3fd6-af68-25ba7eabee8a | -5.29243 | -50.93493 | 2026-08-29 04:51:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b1d2771-cd0e-37ec-ae39-b0774e585579 | -4.1512 | -60.68737 | 2026-08-29 04:51:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99afd5db-768a-3269-b64a-dcba5bd96677 | -4.278 | -48.19433 | 2026-08-29 04:51:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cf24c85a-c59b-3de1-ab15-d781ab7ba29c | -6.71421 | -44.41637 | 2026-08-29 04:51:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41bc0514-c5be-3cb4-8132-228db91f1613 | -2.59628 | -49.33591 | 2026-08-29 04:51:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d34687ea-7809-3cd4-93a6-061822969c3a | -6.63176 | -43.73833 | 2026-08-29 04:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c0d0b513-65e2-3552-a9db-b1d9e95afd25 | -4.54126 | -54.92067 | 2026-08-29 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0603f9a-437d-3b7a-a6f3-721d167d96d4 | -3.82702 | -52.41054 | 2026-08-29 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fc1488d1-37bc-3f11-b25f-a4d90e67ef01 | -5.94216 | -44.77969 | 2026-08-29 04:51:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e853757e-6060-3c1e-9121-6860688431e4 | -6.63617 | -43.74247 | 2026-08-29 04:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 4eab2fb0-bb21-3c9b-af57-c8f01a587889 | -7.0772 | -42.21519 | 2026-08-29 04:51:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 392523c9-4e01-31ad-8506-dd5e80ce0ca6 | -5.64913 | -44.30205 | 2026-08-29 04:51:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7c52ffd6-eee4-3638-8cdd-433d88d377ce | -5.22851 | -52.02128 | 2026-08-29 04:51:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27f3b8d7-923d-3091-bd6a-2616cf4e798b | -5.29189 | -50.93837 | 2026-08-29 04:51:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b0820c2-a6c2-3c7c-8586-1706b0099e08 | -5.29134 | -50.94182 | 2026-08-29 04:51:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2648e198-fa71-39fe-b161-caa6006af595 | -4.18725 | -54.57404 | 2026-08-29 04:51:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| aa0eea94-502f-3853-8ada-536d38c200c7 | -4.91542 | -43.47301 | 2026-08-29 04:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 97e2c7ef-c11d-3bd3-a8af-dd296dbe8768 | -4.16813 | -42.44113 | 2026-08-29 04:51:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 59c144ab-d00b-33e0-a307-d130a701ac49 | -3.33479 | -52.52685 | 2026-08-29 04:51:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 295b8c95-dbaa-3bfb-ac9e-a66ba919745d | -5.34438 | -45.16122 | 2026-08-29 04:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e6185da7-a66f-3fe4-bc24-98278e389b41 | -4.18671 | -54.57098 | 2026-08-29 04:51:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc8ff134-612b-32c3-a0e9-04389a68a9c8 | -4.15802 | -60.69939 | 2026-08-29 04:51:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2481d70e-bf40-3800-9354-a123f1e33477 | -2.71847 | -47.05431 | 2026-08-29 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b6e2116-e238-359e-8880-49e1f40e9fa4 | -5.22573 | -52.01722 | 2026-08-29 04:51:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81d37419-a839-354a-82df-71ac30e66d2f | -5.40792 | -43.18831 | 2026-08-29 04:51:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ddcdf96-d153-3437-b1bf-d89256f66fa2 | -2.72108 | -47.03743 | 2026-08-29 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bafddd51-2b8a-321f-b32b-779960f25812 | -5.41517 | -43.19092 | 2026-08-29 04:51:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4f95330f-4f11-3fa5-93d8-77bfb78b973e | -4.74165 | -55.94697 | 2026-08-29 04:51:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6614e932-26d4-308a-a95a-c6ce221bc1fb | -6.62256 | -43.73535 | 2026-08-29 04:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 622dad46-6134-3650-b30d-b6aae85c4ca5 | -3.4339 | -52.76164 | 2026-08-29 04:51:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4fa219ca-52d0-3dba-a011-8082df9f3273 | -2.98911 | -48.9565 | 2026-08-29 04:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README43.md)
