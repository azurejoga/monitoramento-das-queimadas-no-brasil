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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bca39b42-ba7a-3f6a-869a-bee3a340c698 | -7.0215 | -42.78722 | 2025-10-07 04:36:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 26d081f9-e8ea-389a-af4c-2721404bb355 | -8.11522 | -49.84438 | 2025-10-07 04:36:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a84f4d37-6340-3973-8164-d9ccf4e00759 | -7.63479 | -43.06485 | 2025-10-07 04:36:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3f20c015-28c4-3498-8f79-05c5bb03d0b4 | -6.31813 | -46.10143 | 2025-10-07 04:36:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 64fac3c2-8aff-3f91-8f7f-e8156bff4265 | -7.46557 | -43.09192 | 2025-10-07 04:36:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8bb9c9d6-8ed9-3876-89f6-bc59667b1f6e | -7.52444 | -49.9083 | 2025-10-07 04:36:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 499b30e4-1848-3ac3-84e3-e77a4f5e73ef | -8.61631 | -44.93314 | 2025-10-07 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7efd1943-2516-327b-9732-7593b431e1e1 | -4.55267 | -46.68025 | 2025-10-07 04:36:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac7d82a1-089e-32be-a0dd-951781ce14c4 | -7.68219 | -50.21335 | 2025-10-07 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 395cf995-d17c-387d-abf7-85735de6e088 | -5.73863 | -42.5315 | 2025-10-07 04:36:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 55db650f-850c-3cc8-a17a-62a0210cde9a | -8.62007 | -54.99051 | 2025-10-07 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b64a9e16-36b4-3b5e-bcf3-21215efef8f4 | -5.25758 | -46.57263 | 2025-10-07 04:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fe7341bc-42f0-38b5-a2b5-e15622387a48 | -9.68696 | -48.39364 | 2025-10-07 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a39fd692-4336-349a-a3c3-f4e3624af93a | -8.61501 | -48.79588 | 2025-10-07 04:36:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc8ec64d-f793-3001-96b9-83570ef4bf6b | -7.02627 | -42.75423 | 2025-10-07 04:36:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 71f25b12-238e-3db2-8ac6-9458f2c41798 | -8.92947 | -46.59918 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7f641e5-2da7-381b-a106-68ad24351b62 | -9.67698 | -48.39204 | 2025-10-07 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69dc6c10-11e0-33a5-a503-0c38bb675b2f | -6.66653 | -42.75898 | 2025-10-07 04:36:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4b547d1e-2f21-3090-962d-015c5e75f4b0 | -10.31795 | -46.93714 | 2025-10-07 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d59143c3-79ca-3fec-85cc-244c1dae412b | -8.88187 | -46.7972 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 653fab61-512f-3e07-a9c8-aca39fd8b3b0 | -6.98202 | -42.86303 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bae06b62-1f0b-3a4e-8a18-28aa835aba86 | -6.64862 | -41.98047 | 2025-10-07 04:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 04fad60a-00f6-3734-ba65-fbd392ff838f | -5.25792 | -46.48174 | 2025-10-07 04:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0dad001a-6e46-33e1-ab1c-cc95bdd842da | -8.88472 | -46.80144 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a9a2ab65-b20e-3b29-b35a-e3d4181e99e3 | -9.19385 | -47.84737 | 2025-10-07 04:36:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81972742-dc80-35b2-afe6-aebe6d3f45e2 | -6.23683 | -43.2756 | 2025-10-07 04:36:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 96fcab40-dc73-3754-9c19-01de3cd5c91e | -9.18214 | -47.83463 | 2025-10-07 04:36:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0323a1cf-f815-3272-900f-ed5adf101811 | -6.98446 | -42.87456 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 40f5b581-3a4d-31fd-9794-8fa6bd1588eb | -8.26451 | -43.83045 | 2025-10-07 04:36:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c87c621f-8a0b-3676-8d7f-c877dca69643 | -5.74206 | -49.13611 | 2025-10-07 04:36:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbb13220-1122-3cc3-9389-54c1dfcb13cd | -9.03577 | -49.7655 | 2025-10-07 04:36:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8283131-682a-3d0d-8e94-f83e104ac8f9 | -8.49342 | -46.31148 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 05fc2446-3082-3d42-9cf3-119f85ae72cb | -10.19558 | -46.02684 | 2025-10-07 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0114868b-7832-3e60-8d14-bf01335a3685 | -8.60745 | -44.92485 | 2025-10-07 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0c56d68-d083-3593-87ff-52e02e8a6962 | -9.42083 | -49.10902 | 2025-10-07 04:36:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8de1be0-379f-3b1a-834a-5cb9f2f78141 | -8.48124 | -50.21344 | 2025-10-07 04:36:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9215d771-2c33-3a0d-80b9-cd2bab442bc6 | -10.36341 | -44.9791 | 2025-10-07 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 101c5bee-d4db-3c2f-b970-10b857181f5d | -6.70255 | -42.84546 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 69e255e0-6bcf-3418-8386-93bd98e148b4 | -8.60877 | -44.91612 | 2025-10-07 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8cb57a98-7026-35d6-bc23-1ccb56ed8469 | -7.68306 | -42.58006 | 2025-10-07 04:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6e8070c3-a2b8-30d6-b046-d414e749dc59 | -8.53663 | -46.24689 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9512dd45-9065-3dad-bf49-439123cfdb03 | -9.67894 | -45.66627 | 2025-10-07 04:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b89551a-2f2f-3bd0-8d43-28658356d8b3 | -8.6118 | -44.92104 | 2025-10-07 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f017d27f-c6dd-32c9-b5ac-dd57f8891098 | -5.32244 | -45.23903 | 2025-10-07 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f46e452c-3375-393d-9dab-c26cd47608e2 | -8.65698 | -46.28442 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c9d070a-4c6c-378e-afe3-6430d97f8e51 | -4.67183 | -44.85854 | 2025-10-07 04:36:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5911c38a-e305-3c5e-bcb1-d23cbe9581e9 | -4.69259 | -48.62615 | 2025-10-07 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6edf6b3-5527-3c91-9efd-76a1e81dce89 | -9.03037 | -50.58999 | 2025-10-07 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c597a3f9-9799-3904-9088-7d272fb981c9 | -5.59627 | -45.71172 | 2025-10-07 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7498b7a-915f-381a-a04f-834600ca1452 | -8.18391 | -50.30409 | 2025-10-07 04:36:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5a56cd38-608e-3ab2-99e4-0ef00f2ce9e7 | -6.25725 | -43.2738 | 2025-10-07 04:36:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9ffc2300-159b-3af9-a5d7-0e00b15a7298 | -6.16118 | -42.5932 | 2025-10-07 04:36:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0598615a-ad2e-3ce2-b14f-d86fbfa3efdb | -8.48595 | -46.29092 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 83201ecb-c0f3-34cf-bec0-d2b390f1c986 | -8.18046 | -50.30351 | 2025-10-07 04:36:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 318e2fdc-9857-31d6-804b-64f007822958 | -10.02609 | -48.30024 | 2025-10-07 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d65a14c4-0264-3213-935d-540e2afc6e68 | -8.48132 | -46.29802 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2193f199-4fb1-39cf-894f-30546a069a84 | -6.22105 | -44.33276 | 2025-10-07 04:36:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e86e4d21-7cc4-3df9-b42b-fdf7f6ee943a | -9.32911 | -54.51857 | 2025-10-07 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d81b19e5-3b74-3c42-bc28-5dc64f5388e3 | -8.87028 | -46.78466 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f5390f66-e5f8-3acb-844f-c7520dc0bc89 | -5.44884 | -44.6472 | 2025-10-07 04:36:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c4d9d51-215a-3bac-b2eb-b8efc9448eaf | -9.78556 | -48.27966 | 2025-10-07 04:36:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4154e009-65a5-33f0-96f1-e5d9427e14bf | -4.58089 | -48.12169 | 2025-10-07 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6323ce1d-956f-3e95-b660-93644035ee80 | -4.57976 | -48.02152 | 2025-10-07 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 830c3704-d0b2-32ab-91b1-a4ae9ae65c7b | -8.54066 | -46.24373 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 18c8324e-653e-32cd-9de2-3b3fc1a8c8b5 | -4.42673 | -47.752 | 2025-10-07 04:36:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 936b9e1d-b2e0-3c49-b5bf-54354056901f | -10.03106 | -48.29028 | 2025-10-07 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 333e5a72-4f9f-3c06-ad11-7ceb4c2d8766 | -7.62202 | -43.06681 | 2025-10-07 04:36:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 16141304-17db-3ea3-85cd-1c2b1b496bc3 | -10.26251 | -44.37579 | 2025-10-07 04:36:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3b7e880-b51f-33ce-8cd5-09a15d07eea4 | -5.8901 | -49.36708 | 2025-10-07 04:36:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f903ce22-4c30-3016-929f-a2901c650ca9 | -10.25863 | -44.37519 | 2025-10-07 04:36:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 11ec7673-0cb6-394e-8ea5-eb1cf5b40059 | -5.59973 | -45.71223 | 2025-10-07 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 867149d8-dd98-356d-835a-499aee775278 | -4.5712 | -55.95895 | 2025-10-07 04:36:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef2b6869-9ea0-3f96-9629-150e54e33da6 | -6.29498 | -42.94198 | 2025-10-07 04:36:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1e716636-b0fb-399a-97e2-a400c7f94e7d | -7.7322 | -42.38675 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4370dff1-b467-3e6c-8d6a-f5082f652a45 | -7.93175 | -50.00816 | 2025-10-07 04:36:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f54843dd-4eee-3333-a29b-bb2b45bf62ae | -7.02803 | -42.29491 | 2025-10-07 04:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 75606aff-7747-317b-8155-da4f76ac9f0f | -6.69541 | -42.86584 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| b64ad1f4-31f9-3428-b375-ad6a2e3ad162 | -5.82735 | -44.97554 | 2025-10-07 04:36:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ced52046-b6e6-39ee-bf65-72b64f68b324 | -9.96732 | -43.78291 | 2025-10-07 04:36:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3b7a7822-404e-3a1a-9a74-146df7c82d85 | -7.01845 | -42.7793 | 2025-10-07 04:36:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d4b40b53-9d99-3fa6-9a05-9acf56e562fb | -7.02108 | -42.76107 | 2025-10-07 04:36:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 78f84265-5cd9-3938-90a5-554015553249 | -6.75682 | -42.23375 | 2025-10-07 04:36:00 | NPP-375D | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ec8670e8-68ae-3db7-8d9a-318339174892 | -9.68308 | -48.39661 | 2025-10-07 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c701b00-1501-3a9c-90f1-5b97b3f2b250 | -5.22635 | -43.79876 | 2025-10-07 04:36:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aed16514-2e53-3872-9afe-c1d276aed283 | -5.49844 | -43.0651 | 2025-10-07 04:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 61916d87-6728-3e44-a1d9-ffb8a6ef9df3 | -5.25627 | -46.4924 | 2025-10-07 04:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e668100e-0152-3970-b571-411cb4e908e9 | -5.3753 | -40.99676 | 2025-10-07 04:36:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f0d8baa8-dafe-3ad9-b08c-7e5d83b11e18 | -8.96504 | -50.80421 | 2025-10-07 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37e6efee-1ccd-3d0a-b86a-aec9c1ca9b8c | -7.46623 | -42.62486 | 2025-10-07 04:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6b5a8200-0a4b-310c-9937-253a8405f9b7 | -6.7253 | -42.80422 | 2025-10-07 04:36:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ebe652fe-08fd-3aba-8a94-b740763e1be2 | -8.48766 | -46.30285 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b80ec175-7323-3955-acec-85074b020d2b | -7.65012 | -43.88677 | 2025-10-07 04:36:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8b75eff3-3b87-3327-85a4-a60e5aa20ef4 | -9.03297 | -50.58361 | 2025-10-07 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c290fc48-3be8-3357-9d18-906ab35367bf | -7.6783 | -42.58329 | 2025-10-07 04:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1439b479-9492-3676-b4bd-196d1200765d | -4.68404 | -45.84453 | 2025-10-07 04:36:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| bb0c965b-11e1-326a-a54a-8ce4b9227aa9 | -9.67753 | -48.38853 | 2025-10-07 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aab6ce34-4cf0-3ea3-a067-46b4023f2f0d | -9.18714 | -47.82457 | 2025-10-07 04:36:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f737bc64-592b-3653-ba13-169c41a9c899 | -7.25121 | -46.97152 | 2025-10-07 04:36:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1db4e7d7-6ec6-39e3-8d9c-825c28748671 | -8.20797 | -49.11964 | 2025-10-07 04:36:00 | NPP-375D | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a852d978-e998-3896-b696-70a956b0c2d8 | -5.46083 | -42.89537 | 2025-10-07 04:36:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README57.md)
