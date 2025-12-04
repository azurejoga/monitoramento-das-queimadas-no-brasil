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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c2938cb-2551-36d3-8304-97ba0f4f58ea | -3.54793 | -52.46537 | 2025-12-04 00:34:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bada50a9-bef6-33b4-884a-49fac3cc4d18 | -2.34281 | -45.603 | 2025-12-04 00:34:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 163.5 |
| 760db04b-2a4a-36da-8bfe-473b451fa85a | -2.94097 | -53.28283 | 2025-12-04 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 0a0c1aba-2ce5-36be-83f7-250a0ac80b5c | -3.23182 | -52.85084 | 2025-12-04 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7a2e65dc-75eb-3560-a721-b9ec09252479 | -3.08417 | -52.98143 | 2025-12-04 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 1a205716-ab21-3129-a569-baedc6476b82 | -3.01828 | -52.83045 | 2025-12-04 00:34:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| c5fd6002-3ee3-32fd-a5c4-f40aac8befaf | -2.00436 | -45.34336 | 2025-12-04 00:34:00 | TERRA_M-M | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 8ab1f920-4580-3f2b-adeb-c330be2958e4 | -1.41208 | -51.59995 | 2025-12-04 00:34:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 18ebb1d0-c527-3be5-a11b-922cdc1a31b0 | -4.82989 | -43.19931 | 2025-12-04 00:34:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| dd43a6c7-17d3-3e0b-afbf-d89a32bdd796 | -2.53047 | -51.23597 | 2025-12-04 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8ecca2a4-7016-3eff-b91b-75930a623683 | -3.38813 | -49.25399 | 2025-12-04 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 26a274c6-1e33-3163-af31-d544194ae736 | -3.04128 | -48.41588 | 2025-12-04 00:34:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 66b765e8-2c4d-3773-b8e3-1aa20104def1 | -1.84055 | -46.58432 | 2025-12-04 00:34:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 931495d8-da48-324e-9727-2a5d357919c4 | -2.7786 | -52.96008 | 2025-12-04 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| cd251c6d-2e99-39b7-ae45-af354798b279 | -2.92306 | -48.2288 | 2025-12-04 00:34:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| e07097f3-6f13-3252-b660-4899456a688e | -2.60574 | -49.25265 | 2025-12-04 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 38ef5663-97e0-3356-a92b-18565c33f6fb | -2.85332 | -45.23766 | 2025-12-04 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 3ba10f64-0b11-35f8-a5b1-59f0aa573dd4 | -2.93961 | -53.27273 | 2025-12-04 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e0b73f92-8e38-3314-8f75-2666164d4159 | -1.98459 | -52.08275 | 2025-12-04 00:34:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 16cd7d61-3cdb-3b20-b265-2f267cc07818 | -1.18557 | -49.04373 | 2025-12-04 00:34:00 | TERRA_M-M | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2c47779d-de9b-363e-b117-d6f06946756a | -3.33081 | -45.61604 | 2025-12-04 00:34:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 8b28414e-6627-3fbf-8e1f-84112e356bbd | -3.89222 | -45.76161 | 2025-12-04 00:34:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 7aeedca8-0de0-33df-ae17-b50cfef80bbf | 2.52407 | -50.86062 | 2025-12-04 00:34:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 10.2 |
| b808ad50-8b1a-3a31-abb9-f0b09351b38b | -3.22399 | -48.61337 | 2025-12-04 00:34:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| dd8980d2-abc2-3d51-b92a-00a8fdc664ce | -3.33166 | -44.39011 | 2025-12-04 00:34:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| f46b1441-6724-38a3-8020-c36be936ed96 | -3.69633 | -50.93908 | 2025-12-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 786362ef-9536-3ce8-9071-dc0a1ff81a68 | -2.09729 | -45.64025 | 2025-12-04 00:34:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| d98f57db-9711-3fa1-9ac0-2c4e4e028ecc | -2.79488 | -48.90314 | 2025-12-04 00:34:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 918c3b2f-180a-364e-8a10-aa98f24c4f33 | -3.2257 | -46.85248 | 2025-12-04 00:34:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| b94fe488-5c69-31a5-83bd-be6621339965 | -3.12176 | -52.24542 | 2025-12-04 00:34:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 16c9d4ab-9b61-3109-85c5-662f8904ba07 | -1.50474 | -46.07848 | 2025-12-04 00:34:00 | TERRA_M-M | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 370ea4ef-2c36-3fa5-b68d-4584d8b1eaf3 | -2.13757 | -47.87921 | 2025-12-04 00:34:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5759e9b2-4ad7-313c-a6da-c5a2dc724c5d | -4.69165 | -46.42871 | 2025-12-04 00:34:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 9996cabf-9ca0-3ec9-9aa4-16c837afc3ad | -2.95082 | -45.36423 | 2025-12-04 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 443976e9-1aa8-3165-a62b-711b61386aaa | -3.84896 | -50.90539 | 2025-12-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f0cfff34-57d1-312f-8a58-d904e33d0a7c | -2.3479 | -46.9167 | 2025-12-04 00:34:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| c1320624-037f-391f-8ede-5f538a009a51 | -4.70251 | -46.42714 | 2025-12-04 00:34:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| b7e01d6a-684b-3048-a885-15fb848187f2 | -2.97043 | -49.62478 | 2025-12-04 00:34:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5b2bfab8-cada-3b6f-8b06-a6e47cc8b9a3 | -4.77546 | -46.13829 | 2025-12-04 00:34:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 0c277241-2540-35db-9619-d4315732d6a7 | -4.69359 | -46.44219 | 2025-12-04 00:34:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 403de874-210c-3209-a22f-b1febc6c0d37 | -2.95339 | -45.38184 | 2025-12-04 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 2363d311-4ad5-3b67-8675-caa5df481023 | -2.3403 | -45.58567 | 2025-12-04 00:34:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f30326eb-9556-3aa0-b2e4-129766498200 | -2.38489 | -49.39528 | 2025-12-04 00:34:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 92f20385-6c44-3a3e-92b0-913864ced5c2 | -3.79745 | -50.59849 | 2025-12-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c1217de0-2717-3a44-8f72-1253f74c4ad0 | -4.0787 | -43.68519 | 2025-12-04 00:34:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 489b7034-ee7c-336c-ae83-2a10eed8dd87 | -3.38433 | -49.55101 | 2025-12-04 00:34:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8c3895e7-ef4c-3ef7-aaf7-073cd703b96f | -3.05244 | -48.42518 | 2025-12-04 00:34:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c8209686-3e45-349c-9eb2-a92725882dc9 | -4.40696 | -43.14268 | 2025-12-04 00:34:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 424da8aa-99a6-3cb9-9c67-e61b569cc9c6 | -1.95718 | -47.90523 | 2025-12-04 00:34:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 0ea56468-df8f-344b-8937-fc66ddf3ac27 | -1.12213 | -53.44626 | 2025-12-04 00:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 6a854f6f-3699-3aa8-8ed8-258e747557a5 | -2.88534 | -46.81566 | 2025-12-04 00:34:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7c647980-317d-39b6-a29d-06f4cb083087 | -4.20413 | -50.67853 | 2025-12-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b5321add-eeea-31e2-adb3-28cb6050110b | -3.63727 | -52.64421 | 2025-12-04 00:34:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3bf0e9b3-94bf-3c9d-a77e-2f9dcb7d938a | -3.8946 | -45.77753 | 2025-12-04 00:34:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 62d4e197-cbe7-3438-88e0-9529ef7d4bff | -4.77343 | -46.12399 | 2025-12-04 00:34:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 1417d05c-06aa-3ea1-8e86-dd2fc97ae958 | -1.12346 | -53.45593 | 2025-12-04 00:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 18022a78-3edd-3845-b400-aa5a59d9ab42 | -0.39128 | -51.61304 | 2025-12-04 00:34:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 30a58e04-d779-3687-a25c-dcd241513b3d | -4.12181 | -50.08417 | 2025-12-04 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| d596debb-8c6d-3a54-a051-2ca34737e749 | -2.48682 | -45.24164 | 2025-12-04 00:34:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 126.9 |
| 8d16a575-cf45-3401-a0e5-938a43c0b080 | -3.33817 | -45.66579 | 2025-12-04 00:34:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e7a1f5a9-74fe-31b9-9946-316149e248f0 | -3.44146 | -49.56516 | 2025-12-04 00:34:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4cb10554-030c-3d79-aaff-826fd6276cbb | -2.89952 | -50.23597 | 2025-12-04 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9f589acb-94d3-3831-ad5a-a1d8843f8a60 | -2.88626 | -45.37924 | 2025-12-04 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 118ecc4e-a31f-34cd-9b25-3e52f8ebc23c | -4.17253 | -50.30763 | 2025-12-04 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 3eb11d16-c8f2-37a9-a1b5-f286d32cdb5d | -2.54081 | -45.7014 | 2025-12-04 00:34:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 395e2384-d60c-3441-b7c9-93950d2da372 | -2.30226 | -52.18441 | 2025-12-04 00:34:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b4498190-3cf0-3ccb-b8ef-e55629094c4d | -1.43076 | -53.01031 | 2025-12-04 00:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 3e39478a-3b4d-3bfe-8089-75997a61a754 | -2.4277 | -50.28702 | 2025-12-04 00:34:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0e345b45-66cd-3481-9432-79eac2168761 | -1.69918 | -46.15409 | 2025-12-04 00:34:00 | TERRA_M-M | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 012bdc2e-25e6-3ace-8195-bbd49f8d9afd | -1.67375 | -45.80244 | 2025-12-04 00:34:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 3ccadeda-5d9b-3e14-bbca-fe11b38865c4 | -4.43053 | -43.85958 | 2025-12-04 00:34:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 849712b8-1ab4-326a-992b-4b744ebc1f17 | -3.38563 | -49.56038 | 2025-12-04 00:34:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| a6cf304a-6f5a-39d1-884f-be0ebd792d5d | -2.35637 | -50.10921 | 2025-12-04 00:34:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a1d37034-1984-3fc0-870b-430440aab06a | -3.93797 | -50.41323 | 2025-12-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 40dc5eb7-4cb0-307d-8d00-a0150593bea7 | -3.4195 | -52.40084 | 2025-12-04 00:34:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d431100b-fbe5-3668-b458-f93f33bdd80d | -4.0514 | -46.60873 | 2025-12-04 00:34:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 993e8ef9-492d-3a52-b51b-d46caa74c6a3 | -3.43238 | -49.56645 | 2025-12-04 00:34:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 8fe57f90-9e33-3124-bd4a-b307d682c49a | 1.97086 | -55.7151 | 2025-12-04 00:34:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f32b545c-6532-32d7-8fb8-b1c0f37733f4 | -1.88327 | -50.01909 | 2025-12-04 00:34:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 42543940-1386-3918-9950-c7bcde0fa827 | -2.62158 | -49.23043 | 2025-12-04 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1c73b89f-f345-3dbe-a00c-029c08b2827a | -4.08213 | -43.70805 | 2025-12-04 00:34:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 9ddfa45d-8cdb-340c-9c26-dec5daf45880 | -4.85828 | -44.8772 | 2025-12-04 00:34:00 | TERRA_M-M | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 1d9cf128-b1b8-3fba-a8dd-7e14cb432788 | -3.9155 | -50.31684 | 2025-12-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ec563d93-0f28-3ac3-b78d-6d04e4522920 | -4.70446 | -46.44071 | 2025-12-04 00:34:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b96e70e6-e311-3c76-9764-1a3691057270 | -3.27833 | -50.0476 | 2025-12-04 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 13080642-2dfb-3a96-bf40-b24c60a4599a | -3.6661 | -43.61108 | 2025-12-04 00:34:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 784dd612-717c-3543-bd4b-8ba9a31bd9bc | -2.6326 | -47.32138 | 2025-12-04 00:34:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e6738ce1-6e99-3061-9244-a3019d88511d | -2.08417 | -48.37055 | 2025-12-04 00:34:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 21e41748-d187-34b3-90f1-b3b3fdafac13 | -2.36493 | -47.68196 | 2025-12-04 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 8da9c82f-7c42-3919-8977-405199014c68 | -2.04569 | -46.57271 | 2025-12-04 00:34:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| b434225c-38b4-3791-ae01-c58a634344dc | -3.21593 | -48.62507 | 2025-12-04 00:34:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 31e39712-2bb0-3372-b485-6254564e1586 | -3.36178 | -46.85422 | 2025-12-04 00:34:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 68bdcc9e-188b-36f3-93b8-ef305eff4381 | -2.3035 | -52.19338 | 2025-12-04 00:34:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1d226aea-29c5-3f1c-b12e-2150646609f0 | -4.86406 | -44.88899 | 2025-12-04 00:34:00 | TERRA_M-M | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 104c17b2-8bb5-3d83-99cb-cfd0bef18c76 | -3.14728 | -50.56185 | 2025-12-04 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| e6317c38-efcb-39fe-92a0-d9aaed2f1f2f | -0.84159 | -52.34893 | 2025-12-04 00:34:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 20.3 |
| f507961c-409a-3ad2-b440-c4405da2123b | 2.91738 | -51.01529 | 2025-12-04 00:34:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 9492038b-a8c2-3a9c-91ce-a7e017bc3455 | -3.14369 | -49.41472 | 2025-12-04 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e5dce8a2-f305-30fa-b4f3-4f51f1f8a2ce | -2.66071 | -47.32448 | 2025-12-04 00:34:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b8c6b33c-3e45-3984-b962-058531eb6ae0 | -2.87249 | -46.80342 | 2025-12-04 00:34:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |


[Clique aqui para ver as próximas entradas](README3.md)
