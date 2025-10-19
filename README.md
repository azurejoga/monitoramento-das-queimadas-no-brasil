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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f56d86d-32b7-3df3-b738-d6ce7f6a28f3 | -2.7026 | -49.5422 | 2025-10-19 00:00:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 9c11748f-307b-3b54-a9b5-2deb71067208 | -13.2209 | -44.3947 | 2025-10-19 00:00:00 | GOES-19 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 14a59603-c38b-3fa9-a404-6c70d158853b | -4.9141 | -45.4107 | 2025-10-19 00:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| c1eb8eb6-a88b-3c18-889a-41d6990034eb | -4.248 | -44.6787 | 2025-10-19 00:00:00 | GOES-19 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 8db45ea4-f1af-34c9-8ef7-0e4a21ac4e38 | -15.5686 | -42.3547 | 2025-10-19 00:00:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 64.1 |
| e6c72050-ae93-3095-9295-b73f5c736571 | -4.2987 | -45.4903 | 2025-10-19 00:00:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 0801a177-e2d3-358d-90c7-2a73e0179acc | -10.8891 | -46.0814 | 2025-10-19 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 73dafd3a-562e-388d-a2c4-f9adc447c93d | -17.8375 | -40.1319 | 2025-10-19 00:00:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 166.5 |
| d84e3a22-dc00-3150-ae4a-da6d4e9c56d1 | -2.6841 | -49.5427 | 2025-10-19 00:00:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| cfd1a47a-4fb0-3d88-b3c6-85a91485f03e | -5.3291 | -44.8411 | 2025-10-19 00:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 67bf44c3-3ed2-37c2-949c-33bdaa48b979 | -5.3105 | -44.8423 | 2025-10-19 00:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 7c1530e1-3e77-3549-be71-99bcbb9656c7 | -9.1174 | -65.359 | 2025-10-19 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 62cf1dd4-fe80-383c-b248-8ce6d1a71a34 | -5.2899 | -45.0707 | 2025-10-19 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 77875df5-501b-3d5c-8c69-5caf6480c529 | -5.3084 | -45.0921 | 2025-10-19 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| bf3a5bd9-e839-3b97-b3c0-f76221131dad | -17.8578 | -40.1263 | 2025-10-19 00:00:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 85.7 |
| 03377a19-27ef-30f0-ab8e-57f83d70d02b | -5.5525 | -44.9395 | 2025-10-19 00:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| c0d149b9-e745-349f-a322-572489f74949 | -11.6489 | -44.0854 | 2025-10-19 00:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 44bda03b-7222-3f45-86ef-6521c663c357 | -9.1173 | -65.3777 | 2025-10-19 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 7d4da8e6-d522-3f08-9acd-d4cca6b6558c | -15.8085 | -41.459 | 2025-10-19 00:00:00 | GOES-19 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 65.6 |
| 826df694-5624-3d72-86fa-d57538d198cc | -17.8367 | -40.158 | 2025-10-19 00:00:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 80.4 |
| 10595b12-59a0-349b-a901-8731193660ab | -10.8671 | -43.9428 | 2025-10-19 00:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 15a44717-cf22-3b5a-954b-ecd56919512d | -10.2232 | -44.889 | 2025-10-19 00:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 909c5980-2556-3c19-bed6-d66e20453897 | -2.9127 | -52.735 | 2025-10-19 00:00:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 873ad754-7494-3a3f-9bd8-d3faa066aba0 | -12.4682 | -45.4463 | 2025-10-19 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 120.4 |
| fec78d89-b3ea-332a-8fdb-8019a3da99a1 | -15.7886 | -41.4636 | 2025-10-19 00:00:00 | GOES-19 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 53.3 |
| ba689af8-3a49-3697-8a2d-be7f5459e831 | -13.2214 | -44.3711 | 2025-10-19 00:00:00 | GOES-19 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 09134f6d-5aeb-38fb-9e3e-e2099045feed | -10.9266 | -43.8171 | 2025-10-19 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| a88b5335-8ebe-3f41-9b3c-89c4c1ea8b5f | -10.9074 | -43.8198 | 2025-10-19 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| a9739081-8e38-318d-beaf-c3466a9ad2fd | -7.6238 | -60.9212 | 2025-10-19 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 893c0d79-9112-3403-ac96-029e2f17c299 | -2.9128 | -52.7146 | 2025-10-19 00:00:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| a5d9c2a2-0aa8-34c4-b6aa-5bc4f8da8cce | -5.2898 | -45.0934 | 2025-10-19 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 215db98d-0896-3d0d-a139-1656669df496 | -10.2419 | -44.9096 | 2025-10-19 00:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 1bf6daf2-1604-3da1-a76f-c7d00e2945cf | -9.221 | -46.0561 | 2025-10-19 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 87095e5b-e891-3c1c-a4d0-3bd4d5bbfecb | -5.0951 | -46.1391 | 2025-10-19 00:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 231.3 |
| 4dd0e8a9-8814-31eb-9679-fc4bd51b58a0 | -8.6219 | -40.2058 | 2025-10-19 00:00:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 104.5 |
| 0eceb4d0-70bf-3081-a0a6-88b0ffc89c85 | -4.2802 | -45.4688 | 2025-10-19 00:00:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 2042cdca-218c-31e5-936d-ecc2c627c831 | -10.2422 | -44.8866 | 2025-10-19 00:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 747c2c4e-5555-3db5-a489-e7352a08d944 | -10.5522 | -43.3761 | 2025-10-19 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 1a2a9442-109f-31fa-ad80-daf55288bd22 | -8.6223 | -40.1809 | 2025-10-19 00:00:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 148.6 |
| aa48c168-5057-3a39-a3af-528051a6f651 | -12.5072 | -45.4173 | 2025-10-19 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 126.7 |
| beac5882-c28b-3b8c-8be3-e48485dc6fef | -5.3665 | -47.2063 | 2025-10-19 00:00:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 67.0 |
| ef65fb51-f9a1-318a-8e6b-245e0c824fa9 | -12.4686 | -45.4232 | 2025-10-19 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| d393a41b-281a-3c0d-bd53-8b3afa609bcb | -5.0953 | -46.1168 | 2025-10-19 00:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 120.6 |
| a600278a-e3a0-353d-aae1-9efd7f74adf8 | -2.684 | -49.5639 | 2025-10-19 00:00:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 07cb4208-87e8-367e-a97c-27f90ec0b28d | -5.1139 | -46.1157 | 2025-10-19 00:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 94.5 |
| b4f7f615-7c8b-353a-baef-763fbc27b70f | 1.7481 | -55.961 | 2025-10-19 00:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| ce3598e3-fe92-3402-a76b-94f8042d8633 | -5.3086 | -45.0695 | 2025-10-19 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 39a8da4f-1a3b-38c8-9af1-79eb8f31fb01 | -12.4879 | -45.4203 | 2025-10-19 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 5d158a03-9d79-3156-8713-b097965c691c | -4.28 | -45.4913 | 2025-10-19 00:00:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 115.0 |
| cd6fa496-624f-3aba-900b-19e62d0bd366 | -5.5524 | -44.9622 | 2025-10-19 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 8a7457e5-84be-329d-8784-96f995ed3fb1 | -11.6297 | -44.0884 | 2025-10-19 00:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 0bc9ca4f-4f28-3518-a2b1-b7daaffe91d3 | -4.2988 | -45.4678 | 2025-10-19 00:00:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 3cec76d6-af2f-3efd-a7bf-129ee0f91989 | -5.1138 | -46.138 | 2025-10-19 00:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 181.5 |
| 7b8a312a-eda1-328f-81eb-64c170856232 | -5.3084 | -45.0921 | 2025-10-19 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 472086f7-ca89-3dd9-a9a4-22dfbadc5648 | -10.5522 | -43.3761 | 2025-10-19 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 378.1 |
| 2395d582-b4b7-3e31-96a1-4143ea3b9c51 | -10.571 | -43.3971 | 2025-10-19 00:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 197.2 |
| 9f8ca89c-2bad-3aaf-b236-1170d6db6a24 | -11.6297 | -44.0884 | 2025-10-19 00:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 781ad302-ba47-3b93-8ff4-18894271af62 | -2.684 | -49.5639 | 2025-10-19 00:10:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 14006cc2-d332-374b-8d31-bd788e9de5f4 | -8.2287 | -43.9924 | 2025-10-19 00:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 41.9 |
| ac6971fb-5059-3406-b617-8cd6f0704480 | -8.6223 | -40.1809 | 2025-10-19 00:10:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 112.4 |
| a2411f19-2c2c-37a5-81bb-6127624af5d5 | -12.4682 | -45.4463 | 2025-10-19 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 5e3bcc57-93b3-38b7-b4af-157f6efe5fff | -4.2802 | -45.4688 | 2025-10-19 00:10:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 908056dc-1615-3a8f-b9fa-3948e1e7d5fe | -5.3105 | -44.8423 | 2025-10-19 00:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 1e853e52-519c-3a89-a91e-2da53d6dad22 | -8.4531 | -44.1535 | 2025-10-19 00:10:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 7bac4d4e-7e1e-3af6-8b15-adb270a6362c | -8.229 | -43.9691 | 2025-10-19 00:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 8a80d6dd-418f-30a3-9e66-689f2ad39f1d | -14.4759 | -45.5751 | 2025-10-19 00:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| f333e95f-fde8-34ca-8af2-e0b2d4710ea9 | -8.4342 | -44.1556 | 2025-10-19 00:10:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 558.5 |
| e141c8ba-62ef-3def-b59b-440ed22136c9 | -2.6841 | -49.5427 | 2025-10-19 00:10:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| cb389abf-3952-3f33-89fe-fcc79acc0238 | -11.7804 | -47.536 | 2025-10-19 00:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| a04e2c43-bac7-3cbf-9d91-23e9ae3b3d24 | -10.8891 | -46.0814 | 2025-10-19 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| eb5bed7b-1fd0-313c-99f1-05bd3724d11a | -10.2422 | -44.8866 | 2025-10-19 00:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 8072d0b7-0c65-3d0f-b100-e072dfa16789 | -5.0953 | -46.1168 | 2025-10-19 00:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 94.3 |
| d20d522e-f535-354a-b07c-3e7857ac649d | -4.2988 | -45.4678 | 2025-10-19 00:10:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 59.5 |
| f23a9ed5-3447-3361-bd7a-4e3ad170f982 | -10.5518 | -43.3998 | 2025-10-19 00:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 199.0 |
| ebd0f8ae-305c-3e70-a7ca-db6e19a71e3d | 1.748 | -56.0004 | 2025-10-19 00:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| e0450770-8cfe-3b25-8c9e-22c8b8b564f7 | -10.5714 | -43.3734 | 2025-10-19 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 362.0 |
| 9890f205-0445-34f1-bbec-0e23039abc98 | -11.6489 | -44.0854 | 2025-10-19 00:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| c7a6a9a7-78b6-3db8-86e1-68d03d6ad0f6 | -8.4153 | -44.1576 | 2025-10-19 00:10:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 5206d6ad-2773-3b1d-af6f-311c985207d1 | -9.1174 | -65.359 | 2025-10-19 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| cf385553-2480-3944-af07-dc8cae2c4103 | -12.4686 | -45.4232 | 2025-10-19 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| c25d781b-c220-3eba-af8d-23e1f30f9212 | -8.4345 | -44.1324 | 2025-10-19 00:10:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 505.6 |
| 392d2768-eec8-326b-a130-b6f92b51c223 | -14.4949 | -45.5949 | 2025-10-19 00:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 10dc4304-0d30-30dc-a082-b0a6df811abd | -5.3291 | -44.8411 | 2025-10-19 00:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 3567bc62-1445-3a21-84a7-b593af1334b7 | -5.3086 | -45.0695 | 2025-10-19 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 7ee54033-7b5d-3436-810c-69be5f13fef6 | 1.7481 | -55.961 | 2025-10-19 00:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| d5e050be-73af-3cd4-ab18-e49f7566a3d3 | -4.28 | -45.4913 | 2025-10-19 00:10:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 124.3 |
| 47ea41f5-b299-3b27-b3cf-2841f1b4fda1 | -8.6219 | -40.2058 | 2025-10-19 00:10:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 97.6 |
| 6934f883-68e2-3427-87e7-c29c0aa36fec | -10.2419 | -44.9096 | 2025-10-19 00:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 66.5 |
| ccf11ec0-4b51-31c9-a0fe-8326019b559c | -2.9127 | -52.735 | 2025-10-19 00:10:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 65567ae6-e264-375e-a294-56d907d61318 | -8.2101 | -43.9712 | 2025-10-19 00:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 322d4658-52da-32a7-95ed-2ec42354b9d0 | -4.9141 | -45.4107 | 2025-10-19 00:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 017bb7d5-b641-329d-bacd-72ddb53e0bb0 | -5.2899 | -45.0707 | 2025-10-19 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| daab9577-6ac6-3cd1-8032-8276f17c5423 | -17.8375 | -40.1319 | 2025-10-19 00:10:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 124.1 |
| 1d95168e-b163-3129-a58b-1d57caf7994f | -13.2209 | -44.3947 | 2025-10-19 00:10:00 | GOES-19 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| ea37c5b3-1a6f-363b-b65f-742e7e4221cf | -8.2104 | -43.9479 | 2025-10-19 00:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 47.3 |
| ea16c488-df45-3c0b-a49e-4b7c54b87032 | -8.4156 | -44.1344 | 2025-10-19 00:10:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 129.8 |
| cd35bdc1-14b8-3e63-b5c9-af266e899ff8 | -5.0951 | -46.1391 | 2025-10-19 00:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 257.1 |
| 44ecabff-706c-38f0-aab8-d128551c4c19 | -4.2987 | -45.4903 | 2025-10-19 00:10:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 57a221d7-2443-3997-8646-0c5c91cbe326 | 1.7481 | -55.9807 | 2025-10-19 00:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 71dd8622-3b15-3e40-a368-e8d3d3472a67 | -5.3103 | -44.8651 | 2025-10-19 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |


[Clique aqui para ver as próximas entradas](README2.md)
