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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7faae05b-6c39-3091-8cff-194f1f664f0e | -10.8362 | -49.10891 | 2025-07-12 00:24:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 53f27469-a58c-3a28-9d24-b25daa3e066f | -8.25984 | -46.09836 | 2025-07-12 00:24:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c0d28c00-0781-31c5-9efa-33f8caf64484 | -11.7343 | -48.52706 | 2025-07-12 00:24:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 793061b7-5a62-3342-9390-d5f0b157dc3c | -10.89292 | -49.2042 | 2025-07-12 00:24:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| a92f3b45-272f-34a8-a289-8cd1189cbd37 | -7.46951 | -47.52882 | 2025-07-12 00:24:00 | TERRA_M-M | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 796c0bdc-721c-383d-b4f2-80573fb69309 | -6.24718 | -43.36227 | 2025-07-12 00:24:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3b765333-0579-315b-aad5-12602a74d25d | -11.46602 | -45.10882 | 2025-07-12 00:24:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2b641795-479c-3d2e-9c2b-46b7fc2b2a55 | -11.94711 | -49.30413 | 2025-07-12 00:24:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| de8815f6-20e9-3dfe-8468-697f3fe6ced3 | -11.7296 | -47.45647 | 2025-07-12 00:24:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 8b908061-2b0f-31c8-93f9-3a62b20b8862 | -7.08291 | -49.6041 | 2025-07-12 00:24:00 | TERRA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 1914b2a9-3542-3170-bf5d-1b949169875b | -10.66788 | -49.5068 | 2025-07-12 00:24:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 43e09449-952c-3bd8-8d88-46842da184a0 | -7.23249 | -43.09842 | 2025-07-12 00:24:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| ef665a3f-102c-36ce-a655-472fb0d317bb | -11.83906 | -47.51716 | 2025-07-12 00:24:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 0ff60f0f-5ca0-3399-84c3-f497fc236f7f | -8.68738 | -47.99373 | 2025-07-12 00:24:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 45c1cbd3-a376-30cd-a166-21692ab9c926 | -8.47237 | -49.6248 | 2025-07-12 00:24:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 169.8 |
| f2aebe17-783c-30f8-8793-ccc0e6b0e4a4 | -7.98892 | -46.40743 | 2025-07-12 00:24:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 161062b1-d937-327d-a717-02a199eb5422 | -8.47053 | -49.61063 | 2025-07-12 00:24:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 337e97c1-9423-3da1-9fbe-314134653e7d | -7.95244 | -49.66603 | 2025-07-12 00:24:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 4996929d-f0c9-335a-bfae-55d1e2615ace | -9.85665 | -47.88285 | 2025-07-12 00:24:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| dbd7c8ec-463a-38b7-a6b9-4768f9f62d6f | -7.99793 | -46.40616 | 2025-07-12 00:24:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b9142d8c-6085-3655-a1bb-aeba33b9c806 | -13.11673 | -47.30464 | 2025-07-12 00:24:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 048aefc9-14bf-3aca-aac4-857092168dd7 | -10.85817 | -49.10608 | 2025-07-12 00:24:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 1b8247c2-c611-3d54-80ae-87240a59fcec | -11.43812 | -45.10357 | 2025-07-12 00:24:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2076d8ec-79cc-3802-ae42-0dade567e51f | -12.41934 | -45.35117 | 2025-07-12 00:24:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| e2afc3ad-a25e-3795-81c3-8afa03de83a3 | -5.83825 | -48.38667 | 2025-07-12 00:24:00 | TERRA_M-M | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| eedb52b3-da19-3088-86b9-7e24bb91ec43 | -9.80278 | -48.56776 | 2025-07-12 00:24:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 87837b5f-8017-3ea6-9349-4a030ee94f90 | -7.17712 | -42.9814 | 2025-07-12 00:24:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| f734bbca-576f-3253-b4c7-3f81e53e10fc | -12.61032 | -48.37838 | 2025-07-12 00:24:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d8c54709-352e-392c-9272-5a8a53799579 | -11.49306 | -48.07654 | 2025-07-12 00:24:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 52aee0b9-e2a8-3c4b-aaa0-2aa6d9496a06 | -7.67102 | -47.32959 | 2025-07-12 00:24:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8424abad-4b09-3b9e-b61e-c9fbbf497004 | -7.23393 | -43.10858 | 2025-07-12 00:24:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 6a31fa93-f1a5-359d-91e2-e04da4b3714d | -7.18661 | -42.98003 | 2025-07-12 00:24:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 8de9dea7-fd30-3865-8cc3-0dd057590c21 | -10.84894 | -49.12162 | 2025-07-12 00:24:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 992243c0-3e03-37c0-b9f8-f737de175135 | -7.22307 | -43.09981 | 2025-07-12 00:24:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 30.5 |
| ab72d444-312c-3441-af83-b6cc25953db2 | -11.8376 | -47.50572 | 2025-07-12 00:24:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 36689e8c-563a-3d13-885a-a1c1574a6c35 | -10.83795 | -49.12317 | 2025-07-12 00:24:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 6f12c313-8877-3e93-a224-9256214a9666 | -10.85994 | -49.12028 | 2025-07-12 00:24:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 47.3 |
| f0740068-b1d1-3270-839f-11f975874f83 | -12.47711 | -44.49296 | 2025-07-12 00:24:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0cde0c15-63a4-3247-bd68-6b1cb9d60a93 | -10.66596 | -49.49168 | 2025-07-12 00:24:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 990c3e01-3b17-324b-b1ff-64ae64769dd0 | -8.92604 | -47.34569 | 2025-07-12 00:24:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 05ad3564-c4f7-3521-8d55-fdbe1c71ed55 | -4.09013 | -40.98678 | 2025-07-12 00:24:00 | TERRA_M-M | CARNAUBAL | CEARÁ | Brasil | 2303402 | 23 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 6ddc8fc1-dce3-3dd5-a41f-4f03c8e9d90a | -12.60869 | -48.36526 | 2025-07-12 00:24:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| d058ff29-d47c-3134-adb9-b8ada412474b | -13.28897 | -49.16272 | 2025-07-12 00:24:00 | TERRA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 65389220-f8d8-3aac-95f6-70155bbbcc2f | -11.73245 | -47.47895 | 2025-07-12 00:24:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 9f6847ec-32b4-3fe1-bdcd-704935826916 | -10.80868 | -49.63233 | 2025-07-12 00:24:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| b800831e-f21f-32ae-9da6-ae8f5eae67a6 | -4.27711 | -46.93998 | 2025-07-12 00:26:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 3ed7da32-2bf6-3350-9592-56123d136e6f | -3.51436 | -47.21552 | 2025-07-12 00:26:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c18a1882-eac0-3ba0-baaa-b0ab025429bd | -4.54332 | -48.01345 | 2025-07-12 00:26:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 7e56547f-33e7-3d04-a669-00a49f0587f0 | -4.2862 | -46.93246 | 2025-07-12 00:26:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c06c693c-487b-382a-8da3-f4afd861affd | -4.27218 | -48.19104 | 2025-07-12 00:26:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 301f96aa-6df2-3a2f-bcc5-d09bbe95f865 | -3.38171 | -43.13302 | 2025-07-12 00:26:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9189d3d9-138c-3d60-9ebb-2e89331c13d0 | -4.82388 | -47.09665 | 2025-07-12 00:26:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2ed86586-4c80-3302-813d-95ca877a915b | -3.38995 | -43.12035 | 2025-07-12 00:26:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 2e89274f-8746-3829-87bd-c83d8b3b4f5d | -3.37956 | -43.12824 | 2025-07-12 00:26:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b8d04f53-fdfc-3958-8f62-4a3f42e86b88 | -3.74868 | -47.11516 | 2025-07-12 00:26:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| ded15152-c4e3-3f53-9026-627463ab4f9a | -3.40344 | -43.37104 | 2025-07-12 00:26:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 0ab4a28b-62f3-3dff-8000-a6d44aa62a69 | -3.75761 | -47.1076 | 2025-07-12 00:26:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 041ad081-4afa-33d4-b930-cf772e031d76 | -3.86574 | -54.23873 | 2025-07-12 00:26:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 67afe129-51a5-3036-a1d4-fa38f1945867 | -3.38008 | -43.12181 | 2025-07-12 00:26:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 22704117-fccb-3575-bf45-ec605b3b5fcd | -3.74994 | -47.12423 | 2025-07-12 00:26:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 15e9d2ee-0a1e-3b2c-8527-fe6aed39a4d2 | -4.27083 | -48.181 | 2025-07-12 00:26:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| d2096991-578f-38cc-9b24-b3f979ccd4b7 | -4.54199 | -48.00358 | 2025-07-12 00:26:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b0a48046-12ad-3690-82e9-38c580093a95 | -4.27585 | -46.93094 | 2025-07-12 00:26:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 81ea3097-e9ac-3a4f-8da7-f0ca4cfa2d0a | -3.39817 | -46.90723 | 2025-07-12 00:26:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5dc4cd21-b597-3be0-a8e9-7f409f89e5fe | -3.9985 | -43.23088 | 2025-07-12 00:26:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a8512595-f7df-3021-a292-3051246623d7 | -3.39157 | -43.13151 | 2025-07-12 00:26:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0e2c76d3-3d5e-3f21-a6f8-9a0e03577052 | -4.00005 | -43.24174 | 2025-07-12 00:26:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4c91b393-0e8c-379e-8bb8-c55c5013ab12 | -3.75885 | -47.11666 | 2025-07-12 00:26:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| ea323308-975f-376a-b7a3-50d26a04c474 | -2.92669 | -48.23687 | 2025-07-12 00:26:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0d720e6f-4f76-3c66-9143-0e8430aa664c | -3.41316 | -43.36963 | 2025-07-12 00:26:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 2848b3e3-62e6-355d-b6aa-7cb52a88dfe4 | -3.66444 | -48.31814 | 2025-07-12 00:26:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 947b06f9-e702-3aca-834b-fe12510bc8de | -3.37799 | -43.11697 | 2025-07-12 00:26:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cd3cc5a9-0157-3bd6-927e-fa6fd3400647 | -10.8429 | -49.1236 | 2025-07-12 00:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| e9bbcd06-f19e-3306-895c-25507c5ebed7 | -7.4733 | -47.5149 | 2025-07-12 00:30:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 191.9 |
| e4fcd6c4-f1d9-3723-aaa0-c808f7c8293d | -8.4622 | -49.6193 | 2025-07-12 00:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 13afca38-1294-3c00-b76f-68c6dd4257a6 | -3.75 | -47.1144 | 2025-07-12 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 25cb536d-9f0f-3835-a99a-b27712ca155a | -11.7241 | -47.4766 | 2025-07-12 00:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 875d05ad-dcc7-32d9-904f-eb331112652e | -11.7436 | -47.4518 | 2025-07-12 00:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 8dc4a086-a05d-3617-96c0-7b0f143a339d | -8.4809 | -49.6177 | 2025-07-12 00:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 121.8 |
| 2d7302a8-f2a9-3979-bcc4-9bf45211e0c6 | -11.7433 | -47.4741 | 2025-07-12 00:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 28afcea8-b5a4-3c83-8402-8752204603d7 | -10.8619 | -49.1214 | 2025-07-12 00:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 7fd65d7c-d717-33f8-8a6d-5a6fc0bcae66 | -10.8986 | -49.204 | 2025-07-12 00:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 4f2441cd-098d-37be-8a3f-e5acde7b6a22 | -7.4731 | -47.5369 | 2025-07-12 00:30:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 8d6bd2c9-3ddc-31a8-acc1-f9c5924ef85c | -10.8622 | -49.0997 | 2025-07-12 00:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 3605036a-d1c9-3222-8d99-539ab6b280c5 | -11.7245 | -47.4543 | 2025-07-12 00:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| d77b665b-e29e-3e01-a47c-f0c063eb563d | -7.492 | -47.5134 | 2025-07-12 00:30:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 6ff14b8c-d008-33d8-9969-9badf74733cc | -10.8432 | -49.1018 | 2025-07-12 00:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 3f769c8f-f4a0-3c95-b7db-3244b15a07a3 | -8.4622 | -49.6193 | 2025-07-12 00:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 58ec877e-c234-3a0a-83af-e757c185f501 | -11.7241 | -47.4766 | 2025-07-12 00:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| b5369aa8-ccef-3575-ae82-e9147955aa29 | -10.8429 | -49.1236 | 2025-07-12 00:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 4a3bd44c-7d2f-3cdb-87ff-decc5fa75e95 | -7.492 | -47.5134 | 2025-07-12 00:40:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| c3125b91-febb-347e-98f3-1cd1b1ea6e02 | -7.4733 | -47.5149 | 2025-07-12 00:40:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 184.4 |
| 90f7227f-f0d8-34aa-866e-127276628894 | -8.4809 | -49.6177 | 2025-07-12 00:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 2f02116e-8d28-3176-830f-b4249fb178a9 | -11.7436 | -47.4518 | 2025-07-12 00:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 3fbba7e5-3a63-39e5-b429-b6415f6cbaef | -10.8619 | -49.1214 | 2025-07-12 00:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 68aea007-1ca6-3a72-8663-10139737138a | -7.4731 | -47.5369 | 2025-07-12 00:40:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 03a07fb8-131d-32c3-a34e-4ad50886442b | -10.8986 | -49.204 | 2025-07-12 00:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 5eaaf052-7cc2-3c91-8a34-6b06a06e5988 | -11.7433 | -47.4741 | 2025-07-12 00:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 462c3a6e-4512-3eed-ae22-08b70ab1d77c | -11.7245 | -47.4543 | 2025-07-12 00:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| d753a8ff-82b9-33e3-b636-7007eff9d861 | -10.8622 | -49.0997 | 2025-07-12 00:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |


[Clique aqui para ver as próximas entradas](README4.md)
