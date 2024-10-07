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
| 5bf6bed2-3738-30f6-971b-5a51d4c6f608 | -20.13 | -49.06 | 2024-10-07 01:03:30 | MSG-03 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bea4466d-ddab-3ab0-9829-9b6a9afaf00e | -19.87 | -42.67 | 2024-10-07 01:03:30 | MSG-03 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2573aa16-6365-3455-a21f-2cc24206d54d | -19.9 | -42.68 | 2024-10-07 01:03:30 | MSG-03 | SÃO JOSÉ DO GOIABAL | MINAS GERAIS | Brasil | 3163409 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| aafe1e63-24de-348e-b548-748749808ab6 | -17.77 | -53.81 | 2024-10-07 01:03:43 | MSG-03 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a4d17ea8-bde7-3483-bf4f-ec6ac450194f | -17.81 | -53.83 | 2024-10-07 01:03:43 | MSG-03 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e2e8f5a7-54cf-3488-83be-54dc131bf70a | -1.0365 | -53.7389 | 2024-10-07 01:05:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 8f53ed50-8b99-3e86-b0e7-9ba191f6882e | -1.0365 | -53.7187 | 2024-10-07 01:05:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 8c8bd8b7-f205-3cec-9dd3-3aa15ebdc85c | -2.87 | -52.89 | 2024-10-07 01:05:12 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7310791a-630a-3666-b02e-9bd936212c2e | -2.2113 | -53.7029 | 2024-10-07 01:05:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 4bb3333c-bb67-30a5-a784-365e077ed832 | -2.2114 | -53.6828 | 2024-10-07 01:05:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| fffde1bf-ab83-3c07-91ce-cb0a10dd1708 | -2.2297 | -53.7026 | 2024-10-07 01:05:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 40c34222-170a-3184-aeb1-29595ba5e277 | -2.2297 | -53.6824 | 2024-10-07 01:05:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| bb47d72e-7ebb-3a29-b8fd-c0ced393af9b | -2.8569 | -52.9197 | 2024-10-07 01:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 57e20adb-8c54-3341-8dcb-bdd7ffe7a6e9 | -2.857 | -52.8993 | 2024-10-07 01:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 129.6 |
| 029fba3f-fcd4-3fb5-a8cf-ba7331d73a05 | -2.8753 | -52.9192 | 2024-10-07 01:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 229.6 |
| 65292b1e-93c8-3c48-bda2-57bbdd16aed2 | -2.8754 | -52.8989 | 2024-10-07 01:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 273.4 |
| d3fdddf7-9252-31c9-8668-9252a541e5f0 | -2.8937 | -52.8984 | 2024-10-07 01:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 257ecf9f-ee11-3feb-ab0c-e0e2cfb14046 | -4.2728 | -43.7601 | 2024-10-07 01:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 1729238a-08e6-3487-94a6-5e3abbade2f8 | -4.2729 | -43.737 | 2024-10-07 01:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 2ea3bf1b-d703-3d14-bfdf-127b2a97c559 | -4.2916 | -43.736 | 2024-10-07 01:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 3ab89ac9-c1c4-31bf-87fb-829613d7fb3b | -10.8754 | -63.9169 | 2024-10-07 01:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 65.1 |
| ba7b5f25-9629-3a0b-bc14-1e80b0f9836d | -10.8755 | -63.8979 | 2024-10-07 01:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 6c1b0c9c-8b2e-371e-89ee-d52242b56fe6 | -10.8941 | -63.916 | 2024-10-07 01:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 60d89ff0-3a6a-3d2b-9c81-99cc76a8d12d | -10.8942 | -63.8971 | 2024-10-07 01:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.1 |
| e733a25e-95a6-3263-ad79-35a567d7d19b | -11.2654 | -51.411 | 2024-10-07 01:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 6e3d6704-ef24-3041-9179-5e9b8f26dfed | -11.2657 | -51.3898 | 2024-10-07 01:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 123.9 |
| deda05d8-45cb-3d91-b69b-69b0c331a6ed | -11.266 | -51.3686 | 2024-10-07 01:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 47d43fb7-5ae4-388a-8464-21b7b323b2f1 | -11.2844 | -51.409 | 2024-10-07 01:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 4627f5da-8735-354a-b1cd-b496dc35e6b2 | -11.2847 | -51.3878 | 2024-10-07 01:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 77aa2c04-aa66-3796-87d0-da7f84eb8bf8 | -11.7373 | -44.4926 | 2024-10-07 01:06:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 7a49a5da-a4ca-3378-a2b4-137420675581 | -11.7561 | -44.513 | 2024-10-07 01:06:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 9e953ac5-1a81-30ce-b7b2-9f5e613eebb9 | -11.7566 | -44.4897 | 2024-10-07 01:06:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 19c899b8-de16-3aa5-b4c1-463bf3248720 | -12.0585 | -63.7841 | 2024-10-07 01:06:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 757e8cb8-982b-3ac6-9023-f1871805ee11 | -12.0587 | -63.765 | 2024-10-07 01:06:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 47.5 |
| d6a53184-aac8-3278-ae33-c46811154aa2 | -13.8354 | -44.6398 | 2024-10-07 01:06:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| a27ab593-3f14-3169-86fe-6d0bb14b5623 | -13.8359 | -44.6162 | 2024-10-07 01:06:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| b78a41ce-6154-3e38-a30b-23a9d0d45eed | -16.6195 | -55.5892 | 2024-10-07 01:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 87.4 |
| 74532afc-9c0a-33ef-bac9-8731cad54edd | -16.6199 | -55.5684 | 2024-10-07 01:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 98.1 |
| 419c78e7-cbbb-35e8-9eb2-d8ae688784b0 | -16.6731 | -55.8934 | 2024-10-07 01:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 95.1 |
| dbcb6c3a-97d0-30ec-8575-d9c5962dbbaa | -16.9711 | -56.8058 | 2024-10-07 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.7 |
| 1d1ae419-3271-3168-8d79-ac9095f3353e | -16.992 | -56.721 | 2024-10-07 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.6 |
| 2034fe2f-e87c-3173-bd36-909cb4b4c453 | -17.0116 | -56.7186 | 2024-10-07 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 121.1 |
| 85602715-e924-32ab-ba32-c33980272452 | -17.012 | -56.698 | 2024-10-07 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 123.3 |
| ddf8c094-127e-3928-ac11-fc6a17706605 | -17.1581 | -57.3582 | 2024-10-07 01:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 117.7 |
| 296dad46-8551-3d2b-b116-dc9bf22138ff | -17.1584 | -57.3377 | 2024-10-07 01:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.2 |
| b984fd33-603b-35c6-ad35-34ee789edabe | -17.6279 | -53.1094 | 2024-10-07 01:06:45 | GOES-16 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 2a553a67-133f-386f-8be2-b716aab7e53a | -17.6283 | -53.088 | 2024-10-07 01:06:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 88530fe1-2a4e-3ae1-9ea6-97e63ffa15b1 | -17.6481 | -53.0849 | 2024-10-07 01:06:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 102d8c9b-7c1d-3c1f-a6b1-4d4488683d93 | -17.6679 | -53.0819 | 2024-10-07 01:06:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 112.9 |
| e3a83afc-8f6c-3999-bb05-17f150ae3e67 | -18.6391 | -57.2578 | 2024-10-07 01:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.6 |
| 2d2caab2-59db-3de8-b406-e4fd8d083bb1 | -18.659 | -57.2552 | 2024-10-07 01:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.4 |
| 8c461aae-007c-3197-94bc-fc153b137e66 | -18.718 | -57.289 | 2024-10-07 01:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.9 |
| e21b095f-fe41-3394-816a-72d35199e3a0 | -19.8104 | -42.3854 | 2024-10-07 01:06:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 84.3 |
| 87ac0f92-b9a7-3f4c-8ef4-ae04e05d1387 | -19.8112 | -42.36 | 2024-10-07 01:06:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 183.7 |
| d39048b2-afad-3867-8cd2-77df8e727c9a | -19.831 | -42.3796 | 2024-10-07 01:06:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 114.4 |
| 397bf5b3-21c0-3fa2-805b-da5bdb01511d | -19.8318 | -42.3542 | 2024-10-07 01:06:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 387.6 |
| a49c982c-7e43-379b-adaf-c8c443f5ef58 | -19.8326 | -42.3288 | 2024-10-07 01:06:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 100.8 |
| 2bd57f14-9665-3bf9-8094-b9655b991062 | -19.8524 | -42.3484 | 2024-10-07 01:06:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 84.1 |
| 9e6d7b2b-fb8d-34f4-917b-c4c37d337749 | -19.883 | -42.6663 | 2024-10-07 01:06:55 | GOES-16 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.5 |
| 095f1003-503a-3d70-a7a9-2cf5c84aed2e | -19.8838 | -42.641 | 2024-10-07 01:06:55 | GOES-16 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 108.9 |
| b63204ec-f339-3832-9765-c7d1354ae8e6 | -19.9036 | -42.6606 | 2024-10-07 01:06:55 | GOES-16 | SÃO JOSÉ DO GOIABAL | MINAS GERAIS | Brasil | 3163409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 83.7 |
| fb7d896f-ef02-3a54-81fe-1a238d07f49c | -19.9044 | -42.6353 | 2024-10-07 01:06:55 | GOES-16 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 116.2 |
| 429a76e1-9298-3359-b743-75d733824fe0 | -20.1019 | -49.0791 | 2024-10-07 01:06:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 80.6 |
| f0bf882e-6a1d-3579-ba0e-329627615509 | -20.1026 | -49.0562 | 2024-10-07 01:06:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 242.7 |
| def087f9-9b9d-3287-a11f-ccd65b55dbfa | -20.1223 | -49.0748 | 2024-10-07 01:06:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 209.4 |
| dd49e692-03e1-3a61-8b4d-938b01823a92 | -20.1229 | -49.0518 | 2024-10-07 01:06:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 677.0 |
| 4399f2a3-8506-3dfe-aa05-4e84cc7c42ac | -20.1236 | -49.0288 | 2024-10-07 01:06:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 199.4 |
| 9e3bb61b-9721-39bb-b0ab-38e3e5ee3696 | -20.1433 | -49.0474 | 2024-10-07 01:06:58 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 81.3 |
| e4e49947-e1d1-3e99-b5ee-0545e8c7249c | -20.4456 | -47.664 | 2024-10-07 01:06:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 78.6 |
| f85a2325-05d9-3ef6-a743-bdf606690489 | -20.4655 | -47.6827 | 2024-10-07 01:06:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 57b751df-4199-3b17-a56e-6c09d8a7d837 | -20.4661 | -47.6592 | 2024-10-07 01:06:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 290.2 |
| e1192743-bf43-376f-9470-db497570fc62 | -20.4668 | -47.6357 | 2024-10-07 01:06:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 98d700f6-5d68-37d6-a70e-1130f9fb51be | -20.4866 | -47.6544 | 2024-10-07 01:06:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 162.1 |
| 94b56565-2e13-3e16-b9bf-d72b7614dd8f | -20.4873 | -47.6309 | 2024-10-07 01:06:59 | GOES-16 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 63.5 |
| a22bca89-b96d-35ae-a4d8-9954298de1d8 | -21.0712 | -47.2331 | 2024-10-07 01:07:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 68d117e6-cd0b-310e-bca1-6a30bc7f5dd5 | -21.0919 | -47.228 | 2024-10-07 01:07:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 2477dce8-a7f0-376f-ab04-a86c31154c86 | -21.3582 | -50.1287 | 2024-10-07 01:07:04 | GOES-16 | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 82.7 |
| 7898eefc-eb70-330c-bd55-939aa47b3a22 | -21.585 | -47.93 | 2024-10-07 01:07:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 18344168-7212-3ba6-8f6a-e5c625ddf2c5 | -21.5843 | -47.9536 | 2024-10-07 01:07:05 | GOES-16 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 7804d5d9-26d4-3c3d-9ec9-5f311c82d489 | -21.605 | -47.9485 | 2024-10-07 01:07:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 89b176de-65a8-302f-95f7-138a11eed59a | -22.1974 | -48.1778 | 2024-10-07 01:07:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 90.5 |
| fbe487cc-d808-3211-bfac-00934b779e9a | -22.3922 | -48.598 | 2024-10-07 01:07:09 | GOES-16 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.2 |
| 223ad067-cda6-3347-9489-1809f92f256d | -1.0182 | -53.739 | 2024-10-07 01:15:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| e89d064c-3432-3a9e-a5b8-11f17c07d96a | -1.0182 | -53.7189 | 2024-10-07 01:15:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| f919ab3b-d4ef-37b2-bf3f-b417ba0706f3 | -2.2113 | -53.7029 | 2024-10-07 01:15:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 44f82f4a-1fb3-395e-9311-9f104ad51682 | -2.2114 | -53.6828 | 2024-10-07 01:15:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 54f8a85e-b6a5-31bb-bfc5-b86e39d0dfef | -2.2297 | -53.7026 | 2024-10-07 01:15:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| f469c125-2658-3f06-97d4-d147a4a1a596 | -2.8569 | -52.9197 | 2024-10-07 01:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 117.4 |
| c49e5b40-bfe8-3967-86d2-29fb73bae4dd | -2.857 | -52.8993 | 2024-10-07 01:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 143.9 |
| 9f42f576-9cc1-3d3f-a577-4f5b9ab3574c | -2.8753 | -52.9192 | 2024-10-07 01:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 173.7 |
| 96a2416c-26cf-375f-a8ea-7a8b6b08fd59 | -2.8754 | -52.8989 | 2024-10-07 01:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 220.0 |
| e6fdb376-c2a7-3a37-ae22-d8fba50af183 | -2.8937 | -52.9188 | 2024-10-07 01:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| b6d8a61a-7727-36cf-940f-b195b270067a | -2.8937 | -52.8984 | 2024-10-07 01:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 5ccc1a79-3bf5-3590-b4bf-6010f87b779f | -4.2728 | -43.7601 | 2024-10-07 01:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| b4e58eb1-e740-3248-8ed4-6f76f4bced9c | -4.2729 | -43.737 | 2024-10-07 01:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 54534e06-72eb-3760-bfa8-bc80cd4f70b2 | -4.2916 | -43.736 | 2024-10-07 01:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 8d61f5b5-697e-382d-a7fd-0dd927dd8076 | -10.4506 | -63.1393 | 2024-10-07 01:16:06 | GOES-16 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 61.1 |
| bd062941-d788-3636-ae13-55786682aa1d | -10.4508 | -63.1203 | 2024-10-07 01:16:06 | GOES-16 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 0e368b52-16d2-3128-b00a-59ae31f52bc8 | -10.8754 | -63.9169 | 2024-10-07 01:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 894f8da4-da48-39bf-a558-d4c59ec2200a | -10.8755 | -63.8979 | 2024-10-07 01:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 79.4 |


[Clique aqui para ver as próximas entradas](README15.md)
