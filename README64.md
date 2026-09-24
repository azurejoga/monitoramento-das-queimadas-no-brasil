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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| beaf05cc-7d59-3c2b-ad92-9ebb866cae30 | -3.45431 | -50.06869 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79a4ef05-2051-3462-a593-cbd217ab8384 | -3.83571 | -59.35585 | 2026-09-24 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b1525d52-22d6-3d95-ab10-25ab89c51009 | -5.78977 | -49.19025 | 2026-09-24 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c692269-e40e-31cf-bcfc-c4e51d7c49ac | -1.61987 | -54.92068 | 2026-09-24 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a4577fe-ca3d-3367-a535-6b5eb6c61bd4 | -6.61562 | -59.92519 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da6d39c0-4fb7-33d9-94fc-dd82fbe4254d | -3.07312 | -54.39749 | 2026-09-24 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d752e7e-1232-363f-a30a-04e4a93e3990 | -6.4614 | -54.98962 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 789bf974-2165-346d-a671-fce9d1342741 | -9.14839 | -49.9739 | 2026-09-24 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10accd87-ee3b-3f2f-af68-4ac27971d57e | -3.4486 | -50.08142 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7f384029-aab7-3d76-9292-2ded72bc0dcd | -8.25566 | -54.77177 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6cae0a6-517b-3408-97e0-3284fded4034 | -8.35837 | -57.67516 | 2026-09-24 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 164467b0-7e92-3c5f-9865-3180406ece0b | -6.6139 | -43.73663 | 2026-09-24 05:04:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ebb95222-f3ed-35e4-aa36-f0cf31124499 | -7.4327 | -49.83051 | 2026-09-24 05:04:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76b4b52c-8474-3520-8118-a8bc2e38085d | -9.59455 | -47.77495 | 2026-09-24 05:04:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4bb5be52-28ae-39f1-b9ff-b9a917a6e39b | -3.76057 | -54.81817 | 2026-09-24 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d3c2fb5-b340-3706-841d-b50eee35184b | -6.45919 | -55.00354 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2526eb82-5d3d-3812-8fc8-25cc98989730 | -6.67427 | -58.54684 | 2026-09-24 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 871baa11-9b8b-3e5e-9aef-0543a110f917 | -1.63004 | -54.92227 | 2026-09-24 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e580630c-93ac-35cc-b18b-3e49a6a7e768 | -5.79029 | -49.18673 | 2026-09-24 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 738b12c5-2954-3420-b1ac-1e14ae165725 | -3.84913 | -58.67297 | 2026-09-24 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9aa1b4a3-8d0d-39b9-9aae-48d6e5fba21e | -6.27054 | -55.46236 | 2026-09-24 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c592c5b9-8113-38fd-b56d-ffbfe4fbb6ca | -2.63319 | -51.70351 | 2026-09-24 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2017da2e-4e9b-3a53-b230-7760e6557cea | -6.30894 | -57.75493 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbac2cfc-2d48-33c2-a8bc-8f8a80bd35d5 | -4.50836 | -54.98678 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| edc65c4e-5726-3b60-9ae8-fa1fcbc88a23 | -9.58187 | -46.51538 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c67cf86c-2157-3339-93ba-a91925addd53 | -10.09124 | -46.04754 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7bb7c3eb-95bf-3fa8-b9f6-d9b6070a36c1 | -7.57015 | -57.66015 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1835c96b-118e-3f03-818a-0d885d678009 | -6.347 | -57.77435 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6541b34e-b65b-3518-8ff2-03609a187ac9 | -7.67201 | -45.49298 | 2026-09-24 05:04:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a774c4f1-4ff9-30e3-a264-9feee993a05f | -6.11365 | -59.88905 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 416a6fdf-22d3-3bd1-8602-b18312081451 | -7.19163 | -47.47251 | 2026-09-24 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1855bca3-4195-39ec-9b92-25f7cbe69384 | -6.67349 | -58.55148 | 2026-09-24 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ace43f1-43d5-3c3b-9474-2b15a8738d59 | -8.25913 | -54.77265 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b731af46-8681-3e0a-b467-9f43c682d8f9 | -8.29432 | -50.85119 | 2026-09-24 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01cd9ccd-7b76-3cc2-a6bc-58c0fd32162e | -5.98911 | -44.42616 | 2026-09-24 05:04:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ec97cec-ff35-3fa9-9148-28261edb546f | -4.53278 | -54.97946 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de2c522c-936c-3ee6-8fd2-b809e400aaf4 | -8.45545 | -48.69558 | 2026-09-24 05:04:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3bc71be-e1f1-325e-bb8e-441e8b26aea7 | -5.87251 | -51.93829 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d6ff5bc-2879-38ef-892b-5178d2933082 | -8.29874 | -50.84742 | 2026-09-24 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 562922a8-49b0-3bd0-b2f1-b1343d70ab3a | -8.12275 | -54.81816 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7e537c5c-ad26-3894-b7d8-a5b10dab073e | -6.09399 | -57.62686 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6301c75c-b2cd-3660-b817-c5d143562a55 | -5.81468 | -47.76789 | 2026-09-24 05:04:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8300683e-e6eb-38f7-9d6d-acb1950ca9da | -3.67973 | -60.5905 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32f5a15d-c578-318b-a96f-8ed4e4d1074a | -6.78084 | -48.67758 | 2026-09-24 05:04:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d752139a-4f65-3506-b969-075d7b4ee82c | -4.51615 | -54.98078 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f873cbb3-ce03-31b0-8460-69469f2d6dcd | -6.58566 | -59.90088 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| caaf488c-7126-3c06-ba0f-ee30fd5b4f4a | -7.67304 | -45.48572 | 2026-09-24 05:04:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0c7bf1b-aa3d-35da-bec6-c48182533444 | -4.98908 | -45.55434 | 2026-09-24 05:04:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 52ad891f-9858-3008-8da8-f216271686a2 | -6.17949 | -57.74389 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2a1df9b6-3e6f-31e7-934a-1cc07c6348b7 | -9.14993 | -49.96323 | 2026-09-24 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8e483a1d-d3f7-37df-bb1d-14fc38dce241 | -3.156 | -54.60395 | 2026-09-24 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6b1aff52-5675-3bdf-9f46-7af5f0d81208 | -1.82934 | -55.7141 | 2026-09-24 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9d99ba2e-c293-32c6-8b48-5cf82822bed5 | -3.7645 | -60.73132 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6f7eea8-75bd-3627-beb0-3d31f6090abc | -6.7735 | -63.14707 | 2026-09-24 05:04:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c046a78e-81dc-3b5c-8feb-3ddba580e9af | -7.67253 | -45.48935 | 2026-09-24 05:04:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67997a45-ce56-3183-9b51-e13599cd9a99 | -2.5583 | -57.41902 | 2026-09-24 05:04:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2d0e56ad-72b6-308b-80c3-b0f2f06fcd01 | -7.60828 | -57.60769 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6ff66a79-0fc3-313e-b054-d695e37b96cb | -5.75539 | -49.96309 | 2026-09-24 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4238db9-177f-3c82-9b78-88fe9acb7704 | -5.95038 | -51.79119 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2999621-a638-31ab-9d83-3adfadba5687 | -6.64937 | -59.92719 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3223d36a-764e-3448-b03d-339e543036da | -2.3884 | -48.52414 | 2026-09-24 05:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f5a82f4c-502e-32c6-8701-aea7776bfef8 | -6.68279 | -55.05022 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd2738df-a407-386f-94c6-2ad03655cab1 | -7.39525 | -44.77465 | 2026-09-24 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 27386f90-31fa-3c71-be1d-7d62de0b074e | -6.19577 | -57.7818 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8fe5318-ee03-33dd-b988-e9d9da249c78 | -4.07109 | -59.86464 | 2026-09-24 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82be37fb-21f9-3afb-bdbb-4a633f01d4fa | -7.1937 | -47.45768 | 2026-09-24 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b98e9ed1-840b-3a12-b666-289fa57a9b99 | -8.588 | -54.62532 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ff7faac-9096-3286-84cf-b9d38fab41c3 | -5.82064 | -57.73759 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ed45365-3258-3231-ae2d-282842837635 | -4.98713 | -45.54846 | 2026-09-24 05:04:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| daa25e7c-5ccd-3034-b67d-37054d27a8b1 | -2.9483 | -50.48807 | 2026-09-24 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0032b707-83b0-39a4-8989-b865c151103c | -6.78144 | -48.67361 | 2026-09-24 05:04:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aaa0f4a9-e3ee-3958-b117-eb488be6d562 | -5.41264 | -60.21299 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df2eb6a8-8c9c-3e18-ba7d-a47413f759b1 | -6.58008 | -44.14628 | 2026-09-24 05:04:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ccf93c2e-9ce2-32de-a4f0-9b08eb00ddc0 | -5.37602 | -56.05478 | 2026-09-24 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4420fe6-4bef-3a83-9d79-caa228b5d224 | -2.92576 | -48.73787 | 2026-09-24 05:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b14fa19a-83ce-3b62-abf0-6b36d7bc60b1 | -3.18058 | -48.02374 | 2026-09-24 05:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b659fb27-bd17-35b8-b6d1-a4d9459ac646 | -6.88532 | -55.56846 | 2026-09-24 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e0ecd5d7-134c-3710-8dd6-97046214a692 | -3.52654 | -49.37057 | 2026-09-24 05:04:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62c8bfda-abab-3928-9e9c-388f2f995782 | -3.44793 | -50.08583 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2e957a4f-81f4-3da1-9472-bf2f2a68fd3b | -3.07422 | -54.39052 | 2026-09-24 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a971fb33-ae3e-353d-b33e-bf66c8cbeba6 | -5.83629 | -53.8545 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc454fe0-62a3-38f0-b02b-a1bd5b73ee3d | -2.97627 | -54.15175 | 2026-09-24 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f79ece6-c4a0-30f7-bfc7-3e52a4a26339 | -4.50282 | -54.95705 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60130579-3eee-3195-b5f4-43989dd4272d | -7.27198 | -46.79623 | 2026-09-24 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 73100215-9af2-36ac-84ae-06641b220f0a | -3.45973 | -50.08308 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dfcfae70-d606-3b0c-b992-80a4a39211a6 | -3.81728 | -58.89017 | 2026-09-24 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3065733b-5ef3-3bad-92b2-72f028b6d74b | -9.24071 | -47.37222 | 2026-09-24 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 88414308-246d-3229-a7e4-efcbc443c7de | -6.72213 | -44.15089 | 2026-09-24 05:04:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8256155c-4cfe-3a35-a2ad-c2b0c194c700 | -6.10091 | -57.67556 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18527720-ee6e-3cc7-af92-4fd84b90e91a | -6.29646 | -57.73972 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c38ab47d-1c5c-3511-91fc-b9ba53cbde00 | -8.27787 | -54.7614 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47c3589a-92ae-33f0-a866-adcdd1b65c50 | -3.67897 | -60.59512 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a127883b-062f-359b-a53c-13e73b83b0ae | -3.44422 | -50.08525 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b36da1b0-451e-3ca7-8ec2-ec67221aa31a | -3.66748 | -55.53423 | 2026-09-24 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0556561e-6911-37ce-a3a6-b3f4ef327c7f | -3.65242 | -55.47554 | 2026-09-24 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5cee4137-af8e-338f-bd6b-9ccaf5d97e90 | -7.03834 | -51.39521 | 2026-09-24 05:04:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8031852-499c-3ef9-9b3c-99f924bd7e5f | -6.87977 | -55.56032 | 2026-09-24 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62b1826a-147a-3605-8b12-906e119027e3 | -5.21443 | -56.07867 | 2026-09-24 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bc069d7-5f9f-3ae2-bd69-95321388fc4a | -6.45727 | -59.99189 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25a62d4e-e088-3131-b74b-94178b03e55a | -5.94978 | -51.79506 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README65.md)
