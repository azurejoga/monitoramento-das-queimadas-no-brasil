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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89dfdef6-23c4-389c-9b39-9da151aace23 | -8.75469 | -44.94028 | 2025-05-28 12:42:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 35672b01-adea-3080-8b53-402c03df248e | -8.39817 | -47.0928 | 2025-05-28 12:42:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c2833826-b637-3083-9dd7-60ea7a10a2b3 | -7.67308 | -46.10362 | 2025-05-28 12:42:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| d42d642b-f1d2-3833-ba58-c7e4c7576217 | -7.97992 | -50.71488 | 2025-05-28 12:42:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 9eb4f0b5-7d95-3dd9-836c-475a3a858ae9 | -11.22221 | -48.61997 | 2025-05-28 12:42:00 | TERRA_M-T | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 32.3 |
| b5b8bdc8-8101-356c-a72a-c27915e34b44 | -11.77846 | -47.32544 | 2025-05-28 12:42:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 8089b1f9-2ad5-30a1-8a61-e45884799edb | -10.45714 | -47.9374 | 2025-05-28 12:42:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b6f4dab2-7401-305f-8992-c2ce93f66964 | -5.77848 | -43.62649 | 2025-05-28 12:42:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| b14680f4-21dc-3110-96cd-5bc00efd148d | -7.35572 | -43.71746 | 2025-05-28 12:42:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 09f8ef53-64fc-3539-a336-c8de8c399238 | -7.97864 | -50.72375 | 2025-05-28 12:42:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 93e6acdd-6429-316d-9859-141b1aae0802 | -10.06307 | -48.28305 | 2025-05-28 12:42:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 618fd51b-c620-37f7-b428-3ff173d63f58 | -7.07186 | -44.92683 | 2025-05-28 12:42:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 4216b12d-62eb-3fcd-bb66-83df8c664967 | -10.62184 | -48.07901 | 2025-05-28 12:42:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 325fef40-6645-381d-a9bd-e4b1defb20f2 | -10.65985 | -52.70871 | 2025-05-28 12:42:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 41d3dfe7-72df-3daa-a014-3524b26e80dc | -7.18274 | -43.75097 | 2025-05-28 12:42:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 9156d2c9-ee4c-3a03-928a-656ff6062fab | -8.75902 | -44.92733 | 2025-05-28 12:42:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 057d9cb9-dd4d-3a3c-9c71-2a7c133d4a0d | -5.77313 | -43.4889 | 2025-05-28 12:42:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| a988ef0c-1672-3e37-84f2-591e9b5a2fe9 | -11.82372 | -44.25828 | 2025-05-28 12:42:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 28.8 |
| f3c16f8d-63ec-377a-8eae-ec0379c7a1f5 | -7.62765 | -45.75748 | 2025-05-28 12:42:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| d5710e03-6692-3614-bed2-e3ca215478f0 | -11.22365 | -48.62607 | 2025-05-28 12:42:00 | TERRA_M-T | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c43bf018-3dc5-3e68-a545-9e27aaa95ed0 | -8.01663 | -49.68649 | 2025-05-28 12:42:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 95dd350a-9ef9-3151-8783-8ac45f1ec4af | -11.82093 | -44.28196 | 2025-05-28 12:42:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 651ee135-a84a-31e1-8f44-925229439227 | -11.26624 | -52.47638 | 2025-05-28 12:42:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| c1dcc423-1cc6-31c4-9441-bb0291897c58 | -10.84972 | -44.78175 | 2025-05-28 12:42:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 1a77bec2-153c-3f13-bfb7-2da03e08882f | -10.24101 | -52.23187 | 2025-05-28 12:42:00 | TERRA_M-T | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| aa45e9c1-e316-36c9-9bdc-4892753a4d24 | -8.0041 | -47.34769 | 2025-05-28 12:42:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 47ddb664-2093-381b-bbe2-88ccb4aad66c | -11.27655 | -52.46851 | 2025-05-28 12:42:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 9690c47a-f30a-3c0e-8bd3-7c5ac34d504e | -11.2676 | -52.46718 | 2025-05-28 12:42:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 23.0 |
| a00d7f28-3ea3-348e-b4cd-f4c955ac8097 | -9.17299 | -45.33624 | 2025-05-28 12:42:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 91292b03-2f60-36e8-aaab-7180cd41b237 | -8.28245 | -47.03282 | 2025-05-28 12:42:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a33fc8b1-17c7-323e-be19-e2e5502b3c07 | -11.91692 | -54.4094 | 2025-05-28 12:44:00 | TERRA_M-T | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 01a8cdf7-2d89-3f42-a054-dc4e9fbfe228 | -12.34166 | -49.96465 | 2025-05-28 12:44:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 651b563a-21a7-314c-94fb-3c179ab768a7 | -12.34033 | -49.97446 | 2025-05-28 12:44:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 05b6e219-b067-3e18-9f52-3cab1482eddb | -12.40353 | -49.99325 | 2025-05-28 12:44:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 0a23232d-c628-3607-8520-a6e07b8f9d7b | -14.68764 | -45.10286 | 2025-05-28 12:44:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| bf07143b-809b-3e6d-bf30-288830831f29 | -13.09299 | -45.29477 | 2025-05-28 12:44:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| ffdf835c-c0da-34d7-b0e1-f8d91f1a47dd | -13.71262 | -45.23345 | 2025-05-28 12:44:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 32.7 |
| e7241440-8ab9-35f0-9fa0-ea31c533b4fa | -11.14184 | -53.91872 | 2025-05-28 12:44:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 3b909909-64af-328d-a5c9-0bebf27e96ce | -14.69024 | -45.07906 | 2025-05-28 12:44:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 91dcbc72-bf66-35ca-8f42-09eba64574a8 | -12.34955 | -49.97578 | 2025-05-28 12:44:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 31a38b31-5b5b-3f50-b1b5-d4c8c10c87d9 | -12.92536 | -44.95587 | 2025-05-28 12:44:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 4240fff7-ea32-3dd8-b4e1-7cb750511018 | -13.08414 | -45.26706 | 2025-05-28 12:44:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 4c594928-f693-3dcd-8779-0a8c4a1c2b0e | -14.67995 | -45.09505 | 2025-05-28 12:44:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 9f0e3b56-2e5b-3183-878f-0713c7d575f4 | -13.09715 | -45.2686 | 2025-05-28 12:44:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| a17af6b6-aab9-3ec3-9e15-d22790f268b1 | -16.28514 | -48.64743 | 2025-05-28 12:44:00 | TERRA_M-T | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 24dd1b2e-66ad-3bd2-a4cf-d3355168d4ee | -13.08167 | -45.28778 | 2025-05-28 12:44:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 0ab2fe96-084a-3275-a264-4aad28be73c7 | -14.11733 | -45.67025 | 2025-05-28 12:44:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 78913294-6105-38e5-ae33-be86ab85cf5e | -12.35089 | -49.96595 | 2025-05-28 12:44:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 156.6 |
| f1556b5e-330b-338e-94e3-f4b322740745 | -11.81367 | -55.07793 | 2025-05-28 12:44:00 | TERRA_M-T | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 3c6d0573-d2b8-34c0-9b63-cd52b6f6d36f | -12.40218 | -50.003 | 2025-05-28 12:44:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 299d6136-53d8-36ee-98dc-28c4670cf77c | -12.92281 | -44.97765 | 2025-05-28 12:44:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 7bf8bef8-f805-3aa5-ba48-afd4f8fb8578 | -13.09532 | -45.27403 | 2025-05-28 12:44:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 135.7 |
| a5f15010-7979-3f50-8082-27179d9a9810 | -13.09465 | -45.28932 | 2025-05-28 12:44:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 2344dea7-0e09-3b48-9953-58ac4cfd659b | -12.3205 | -49.99572 | 2025-05-28 12:44:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 131.5 |
| d2091e07-ee7c-3049-97b6-4bb4c2749c2d | -14.6823 | -45.39418 | 2025-05-28 12:44:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 49.4 |
| a5234f42-1be2-33b6-9696-fa8c5e3a7d79 | -12.41275 | -49.99451 | 2025-05-28 12:44:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2a964e1d-1b27-32e9-9060-358ad9d6e6d8 | -12.41139 | -50.0043 | 2025-05-28 12:44:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2bf3b303-6c77-3363-9d4a-e01de044813f | -12.11481 | -54.66175 | 2025-05-28 12:44:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| dbc74c08-6047-3cf5-bf7a-8e1bba64a624 | -14.67413 | -45.1013 | 2025-05-28 12:44:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| e58af90f-f9f5-34b6-8a7f-470823eac311 | -12.32186 | -49.98594 | 2025-05-28 12:44:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| dd6ec3a7-f40e-3e15-8b18-bfe2b13f520a | -13.71013 | -45.25494 | 2025-05-28 12:44:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 8c38b73a-f903-3daa-a7ba-61e95af38e46 | -12.37192 | -46.9724 | 2025-05-28 12:44:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| bf82662c-2e9c-3d83-9fe3-68641eb3e77a | -12.3324 | -49.9857 | 2025-05-28 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 8497055d-ad26-32e5-9de1-e4298f309e5b | -14.681 | -45.0956 | 2025-05-28 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 94b2ddf5-f034-37e7-94d2-2936c6a046ab | -7.6762 | -46.0995 | 2025-05-28 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| cb5cf980-4ca4-326f-af67-d82e54a4bdb9 | -13.0874 | -45.2791 | 2025-05-28 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 227.8 |
| 2e8b5d4b-955e-355d-a2c9-3c22bad56f6b | -12.4086 | -49.9978 | 2025-05-28 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 61bc1eab-7154-35b2-9f94-f274d10391eb | -7.9827 | -50.7201 | 2025-05-28 12:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 120.7 |
| d3b41682-d6a0-3cf0-8413-2fcd886a4d09 | -13.0874 | -45.2791 | 2025-05-28 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 233.0 |
| 0703a084-e600-3c0b-93c5-d460c5d83831 | -14.681 | -45.0956 | 2025-05-28 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 0ff59568-6d83-311d-92b2-3182fcdc7445 | -13.7065 | -45.2454 | 2025-05-28 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 106.0 |
| c2bd4c91-eaf0-31eb-9c4f-602b724e97bf | -7.6762 | -46.0995 | 2025-05-28 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| a40ed19e-d628-3241-81a4-0521232f6118 | -7.983 | -50.699 | 2025-05-28 13:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 35d3482f-1025-30ea-a43c-4293d1ded3ea | -7.9827 | -50.7201 | 2025-05-28 13:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 145.1 |
| 027436d3-7ee5-3c52-b20b-58d75b980d63 | -12.3324 | -49.9857 | 2025-05-28 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 5ef2af07-99fe-3090-96d8-ed0e91ad9429 | -5.7713 | -43.4752 | 2025-05-28 13:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| b555dc87-f8f8-3130-b4c2-e0bc06f59486 | -7.983 | -50.699 | 2025-05-28 13:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| ee7a6789-16d1-3fdf-bf0c-d8137d61cfda | -7.964 | -50.7215 | 2025-05-28 13:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| d20ffcbf-d875-37cb-9159-7b775e8f0789 | -12.3324 | -49.9857 | 2025-05-28 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 198.4 |
| 038612a0-50b4-37f2-94c3-6db09eec6344 | -14.681 | -45.0956 | 2025-05-28 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 99662081-8e70-360b-bdbe-90d7e80a2046 | -7.9827 | -50.7201 | 2025-05-28 13:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 1516bdaa-d1a4-3ecb-aff2-5d91ff6ae80e | -5.7711 | -43.4985 | 2025-05-28 13:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 661b6fde-f275-36e2-a348-ec9f71d6925e | -13.7065 | -45.2454 | 2025-05-28 13:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| fafe9490-de86-3033-99c8-e6642cdec4ea | -8.6286 | -51.5507 | 2025-05-28 13:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| cd5a101a-4113-331f-ad09-4d1fd3b5b48d | -13.0874 | -45.2791 | 2025-05-28 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 314.6 |
| d324569f-791e-3ba0-a4fb-74736cf2d0fb | -7.6762 | -46.0995 | 2025-05-28 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| b5351ad8-1653-3d15-a0c6-423436b628ce | -7.6762 | -46.0995 | 2025-05-28 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.0 |
| a11d911d-a79e-323d-83fb-423132c06295 | -11.818 | -44.2703 | 2025-05-28 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 227aead3-5988-3617-9fee-9db6adf3b5b5 | -13.0874 | -45.2791 | 2025-05-28 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 340.7 |
| b0a2bb72-3d85-3263-8a88-dd9655e2f262 | -5.7713 | -43.4752 | 2025-05-28 13:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| cb22b39b-f3a1-336e-a69a-f7604feda0d3 | -13.7065 | -45.2454 | 2025-05-28 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 969658f1-e1c7-3f9c-a1c5-319c21de9013 | -12.3324 | -49.9857 | 2025-05-28 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 232.3 |
| e6f7b6b2-5db4-3fb4-a32f-ce5d2906faf4 | -7.964 | -50.7215 | 2025-05-28 13:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 4ae9328e-cf41-388e-808e-d42c4e82b916 | -7.983 | -50.699 | 2025-05-28 13:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 08dd9fa0-9152-3978-b62f-8b3b61f68aaf | -14.681 | -45.0956 | 2025-05-28 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 8237024f-a23f-3467-8dc4-ae81d604719b | -7.9827 | -50.7201 | 2025-05-28 13:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 08550141-16f5-34d4-8b26-75b3cad3377c | -12.3324 | -49.9857 | 2025-05-28 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 239.6 |
| 06d48cb9-f580-3e28-afc7-0959491872a1 | -7.6133 | -43.4277 | 2025-05-28 13:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 122.5 |
| cb1cd214-43b8-3318-a1ab-af19e869a188 | -13.0681 | -45.2823 | 2025-05-28 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| bf71d483-b3b1-3b6b-938f-6711d7ef1946 | -13.7065 | -45.2454 | 2025-05-28 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |


[Clique aqui para ver as próximas entradas](README18.md)
